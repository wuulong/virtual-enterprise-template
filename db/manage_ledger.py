#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[metadata]
name: manage_ledger
description: 全域實體狀態總控表 (entity_state_ledger) CLI 維運與全資產自動掃描登錄工具。
author: wuulong
date: 2026-07-31
category: virtual_enterprise
"""

import os
import sys
import csv
import json
import sqlite3
import argparse
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "control_plane.sqlite")

STATUS_MAP = {
    10: "10-虛擬發想 (VIRTUAL_IDEATION)",
    20: "20-虛擬確認 (VIRTUAL_CONFIRMED)",
    30: "30-真實對接啟動 (REAL_INTEGRATION_STARTED)",
    40: "40-對齊進行中 (ALIGNMENT_IN_PROGRESS)",
    50: "50-已對齊 (ALIGNED)",
    60: "60-已確認 (CONFIRMED)",
    70: "70-修訂中 (REVISION_IN_PROGRESS)",
    80: "80-修訂確認 (REVISION_CONFIRMED)"
}

STATUS_CODE_MAP = {
    "10": 10, "VIRTUAL_IDEATION": 10, "虛擬發想": 10,
    "20": 20, "VIRTUAL_CONFIRMED": 20, "虛擬確認": 20,
    "30": 30, "REAL_INTEGRATION_STARTED": 30, "真實對接啟動": 30,
    "40": 40, "ALIGNMENT_IN_PROGRESS": 40, "對齊進行中": 40,
    "50": 50, "ALIGNED": 50, "已對齊": 50,
    "60": 60, "CONFIRMED": 60, "已確認": 60,
    "70": 70, "REVISION_IN_PROGRESS": 70, "修訂中": 70,
    "80": 80, "REVISION_CONFIRMED": 80, "修訂確認": 80
}

def get_connection(db_path=DB_PATH):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"找不到中控 SQLite 資料庫: {db_path}，請先執行 init_db.py")
    return sqlite3.connect(db_path)

def list_ledger(status_filter=None, item_type_filter=None, db_path=DB_PATH):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    query = "SELECT item_id, item_type, item_name, prefix_code, apqc_id, status, memo, meta_data, owner_agent_id, last_updated_by, updated_at FROM entity_state_ledger"
    conditions = []
    params = []
    
    if status_filter is not None:
        status_code = STATUS_CODE_MAP.get(str(status_filter).upper(), None)
        if status_code is not None:
            conditions.append("status = ?")
            params.append(status_code)
        else:
            print(f"【警告】無法識別的狀態過濾值: {status_filter}", file=sys.stderr)

    if item_type_filter:
        conditions.append("item_type = ?")
        params.append(item_type_filter.upper())
        
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
        
    query += " ORDER BY status ASC, item_id ASC"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    print(f"📊 【entity_state_ledger 全域實態看板】 (總計: {len(rows)} 筆)")
    print("=" * 110)
    print(f"{'ITEM ID':<22} | {'TYPE':<10} | {'STATUS':<32} | {'NAME':<35}")
    print("-" * 110)
    for row in rows:
        item_id, item_type, item_name, prefix, apqc, status, memo, meta_data, owner, updated_by, updated_at = row
        status_display = STATUS_MAP.get(status, f"{status}-未知狀態")
        print(f"{item_id:<22} | {item_type:<10} | {status_display:<32} | {item_name:<35}")
        if memo or (meta_data and meta_data != '{}'):
            print(f"   ↳ 📝 Memo: {memo or '無'} | 🏷️ Meta: {meta_data}")
    print("=" * 110)

def update_ledger(item_id, status, memo=None, meta_data=None, updated_by="HUMAN_ADMIN", db_path=DB_PATH):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    status_code = STATUS_CODE_MAP.get(str(status).upper(), None)
    if status_code is None:
        try:
            status_code = int(status)
        except ValueError:
            print(f"【錯誤】無效的狀態碼: {status}，可用值: 10, 20, 30, 40, 50, 60, 70, 80", file=sys.stderr)
            conn.close()
            return

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fields = ["status = ?", "last_updated_by = ?", "updated_at = ?"]
    params = [status_code, updated_by, now_str]
    
    if memo is not None:
        fields.append("memo = ?")
        params.append(memo)
    if meta_data is not None:
        fields.append("meta_data = ?")
        params.append(meta_data if isinstance(meta_data, str) else json.dumps(meta_data, ensure_ascii=False))
        
    params.append(item_id)
    sql = f"UPDATE entity_state_ledger SET {', '.join(fields)} WHERE item_id = ?"
    
    cursor.execute(sql, params)
    if cursor.rowcount == 0:
        print(f"【警告】未找到指定項目: {item_id}", file=sys.stderr)
    else:
        conn.commit()
        print(f"✅ 成功更新 [{item_id}] 狀態為 [{STATUS_MAP.get(status_code, status_code)}] (更新者: {updated_by})")
    conn.close()

def add_ledger_item(item_id, item_type, item_name, prefix_code="", apqc_id="", status=10, memo="", meta_data="{}", owner_agent_id="", updated_by="HUMAN_ADMIN", db_path=DB_PATH):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    status_code = STATUS_CODE_MAP.get(str(status).upper(), 10)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    meta_str = meta_data if isinstance(meta_data, str) else json.dumps(meta_data, ensure_ascii=False)

    try:
        cursor.execute(
            """INSERT INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, meta_data, owner_agent_id, last_updated_by, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (item_id, item_type.upper(), item_name, prefix_code, apqc_id, status_code, memo, meta_str, owner_agent_id, updated_by, now_str)
        )
        conn.commit()
        print(f"✅ 成功註冊資產 [{item_id}] ({item_name}) - 狀態: {STATUS_MAP.get(status_code, status_code)}")
    except sqlite3.IntegrityError:
        print(f"【錯誤】項目已存在: {item_id}，請使用 update 指令進行變更", file=sys.stderr)
    conn.close()

def scan_and_register_all(ve_root_dir, db_path=DB_PATH):
    """
    物理全量掃描 ve_root_dir 下的所有清單、SOP、Agent 與 Workflow，並 100% 登錄至 entity_state_ledger。
    """
    print(f"🔍 開始全量物理掃描虛擬企業全清單資產...")
    print(f"  * 掃描根目錄: {ve_root_dir}")
    print(f"  * 目標資料庫: {db_path}")

    conn = get_connection(db_path)
    cursor = conn.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registered_count = 0

    # 1. 掃描各部門之 functional_list.csv (FNC-xxx)
    for root, dirs, files in os.walk(ve_root_dir):
        for f in files:
            if f == "functional_list.csv" or f == "CORE_L3_RACI_003_functional_list.csv":
                fp = os.path.join(root, f)
                with open(fp, "r", encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        f_id = row.get("function_id", "").strip()
                        f_name = row.get("function_name", "").strip()
                        dept = row.get("department", "").strip()
                        apqc = row.get("apqc_mapping", "").strip()
                        agent = row.get("primary_agent", "").strip()
                        if f_id:
                            cursor.execute(
                                """INSERT OR IGNORE INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at)
                                   VALUES (?, 'FUNCTION', ?, ?, ?, 20, '自動掃描登錄之職能項目', ?, 'AUTO_SCANNER', ?)""",
                                (f_id, f_name, dept, apqc, agent, now_str)
                            )
                            registered_count += 1

    # 2. 掃描各部門之 system_catalog.csv (SYS-xxx)
    for root, dirs, files in os.walk(ve_root_dir):
        for f in files:
            if f == "system_catalog.csv" or f == "CORE_L3_TRUTH_004_system_catalog.csv":
                fp = os.path.join(root, f)
                with open(fp, "r", encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        sys_id = row.get("system_id", "").strip()
                        sys_name = row.get("system_name", "").strip()
                        dept = row.get("owner_dept", "").strip()
                        category = row.get("category", "").strip()
                        if sys_id:
                            cursor.execute(
                                """INSERT OR IGNORE INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at)
                                   VALUES (?, 'SYSTEM', ?, ?, '', 20, ?, '', 'AUTO_SCANNER', ?)""",
                                (sys_id, sys_name, dept, f"系統類別: {category}", now_str)
                            )
                            registered_count += 1

    # 3. 掃描各部門之 workflow_list.csv (WF-xxx)
    for root, dirs, files in os.walk(ve_root_dir):
        for f in files:
            if f == "workflow_list.csv":
                fp = os.path.join(root, f)
                with open(fp, "r", encoding="utf-8") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        wf_id = row.get("workflow_id", "").strip()
                        wf_name = row.get("workflow_name", "").strip()
                        dept = row.get("department", "").strip()
                        apqc = row.get("apqc_code", "").strip()
                        agent = row.get("primary_agent", "").strip()
                        if wf_id:
                            cursor.execute(
                                """INSERT OR IGNORE INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at)
                                   VALUES (?, 'WORKFLOW', ?, ?, ?, 20, '自動掃描登錄之 Workflow', ?, 'AUTO_SCANNER', ?)""",
                                (wf_id, wf_name, dept, apqc, agent, now_str)
                            )
                            registered_count += 1

    # 4. 掃描所有 _SOP/*.md 文件 (SOP-xxx)
    for root, dirs, files in os.walk(ve_root_dir):
        if "_SOP" in root:
            dept_name = os.path.basename(os.path.dirname(root))
            for f in files:
                if f.endswith(".md"):
                    sop_id = f.replace(".md", "")
                    cursor.execute(
                        """INSERT OR IGNORE INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at)
                           VALUES (?, 'DOCUMENT', ?, ?, '', 20, '自動掃描登錄之 SOP 文件', '', 'AUTO_SCANNER', ?)""",
                        (sop_id, f"SOP: {f}", dept_name, now_str)
                    )
                    registered_count += 1

    # 5. 掃描所有 Agents/*.json 文件 (AGT-xxx)
    for root, dirs, files in os.walk(ve_root_dir):
        if "Agents" in root:
            dept_name = os.path.basename(os.path.dirname(root))
            for f in files:
                if f.endswith(".agent.json"):
                    agt_id = f.replace(".agent.json", "")
                    cursor.execute(
                        """INSERT OR IGNORE INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at)
                           VALUES (?, 'AGENT', ?, ?, '', 20, '自動掃描登錄之 Agent 設定檔', ?, 'AUTO_SCANNER', ?)""",
                        (agt_id, f"Agent: {f}", dept_name, agt_id, now_str)
                    )
                    registered_count += 1

    conn.commit()
    conn.close()
    print(f"🎉 掃描完成！共處理/同步登錄 {registered_count} 項全資產至 entity_state_ledger 表。")

def main():
    parser = argparse.ArgumentParser(description="全域實態總控表 (entity_state_ledger) CLI 工具與全資產掃描器")
    subparsers = parser.add_subparsers(dest="command", help="子指令")
    
    # List command
    list_parser = subparsers.add_parser("list", help="查詢實態總控清單")
    list_parser.add_argument("--status", help="依狀態過濾 (可填數字碼 10~80 或名稱，如 20 或 VIRTUAL_CONFIRMED)")
    list_parser.add_argument("--type", help="依類型過濾 (FUNCTION, SYSTEM, DOCUMENT, AGENT, WORKFLOW, TASK)")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="手動更新項目狀態、Memo 與 Meta Data")
    update_parser.add_argument("item_id", help="項目唯一 ID (例: SOP-OPS-001)")
    update_parser.add_argument("--status", required=True, help="新數字狀態碼 (例: 10, 20, 30, 40, 50, 60, 70, 80)")
    update_parser.add_argument("--memo", help="補充審查備註或理由")
    update_parser.add_argument("--meta", help="JSON 格式後續擴充 Metadata (例: '{\"alignment_rate\": 87.5}')")
    update_parser.add_argument("--by", default="HUMAN_ADMIN", help="更新者標識")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="手動註冊資產狀態")
    add_parser.add_argument("item_id", help="項目唯一 ID (例: AGT-MED-001)")
    add_parser.add_argument("item_type", help="項目類型 (FUNCTION, SYSTEM, DOCUMENT, AGENT, WORKFLOW, TASK)")
    add_parser.add_argument("item_name", help="項目名稱 (例: 行一診所院長 Agent)")
    add_parser.add_argument("--prefix", default="", help="Prefix 編碼")
    add_parser.add_argument("--apqc", default="", help="APQC 條碼")
    add_parser.add_argument("--status", default=10, help="初始數字狀態碼 (預設 10:虛擬發想)")
    add_parser.add_argument("--memo", default="", help="審查備註")
    add_parser.add_argument("--meta", default="{}", help="JSON 格式 Metadata")
    add_parser.add_argument("--owner", default="", help="主責 Agent ID")
    
    # Scan command
    scan_parser = subparsers.add_parser("scan", help="全量物理掃描全公司清單、SOP 與 Agents 100% 登錄至中控 DB")
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_ledger(status_filter=args.status, item_type_filter=args.type)
    elif args.command == "update":
        update_ledger(item_id=args.item_id, status=args.status, memo=args.memo, meta_data=args.meta, updated_by=args.by)
    elif args.command == "add":
        add_ledger_item(
            item_id=args.item_id,
            item_type=args.item_type,
            item_name=args.item_name,
            prefix_code=args.prefix,
            apqc_id=args.apqc,
            status=args.status,
            memo=args.memo,
            meta_data=args.meta,
            owner_agent_id=args.owner
        )
    elif args.command == "scan":
        ve_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        scan_and_register_all(ve_root_dir=ve_root)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
