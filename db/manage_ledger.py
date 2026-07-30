#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[metadata]
name: manage_ledger
description: 全域實體狀態總控表 (entity_state_ledger) CLI 維運腳本，支援狀態查詢、更新、註冊與自動檔名掃描帶入。
author: wuulong
date: 2026-07-31
category: virtual_enterprise
"""

import os
import sys
import sqlite3
import argparse
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "control_plane.sqlite")

def get_connection(db_path=DB_PATH):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"找不到中控 SQLite 資料庫: {db_path}，請先執行 init_db.py")
    return sqlite3.connect(db_path)

def list_ledger(status_filter=None, item_type_filter=None, db_path=DB_PATH):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    query = "SELECT item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at FROM entity_state_ledger"
    conditions = []
    params = []
    
    if status_filter:
        conditions.append("status = ?")
        params.append(status_filter)
    if item_type_filter:
        conditions.append("item_type = ?")
        params.append(item_type_filter)
        
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
        
    query += " ORDER BY item_id ASC"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    print(f"📊 【entity_state_ledger 實體狀態總控清單】 (總計: {len(rows)} 筆)")
    print("-" * 100)
    print(f"{'ITEM ID':<20} | {'TYPE':<12} | {'STATUS':<15} | {'NAME':<30}")
    print("-" * 100)
    for row in rows:
        item_id, item_type, item_name, prefix, apqc, status, memo, owner, updated_by, updated_at = row
        print(f"{item_id:<20} | {item_type:<12} | {status:<15} | {item_name:<30}")
        if memo:
            print(f"   ↳ 📝 Memo: {memo}")
    print("-" * 100)

def update_ledger(item_id, status, memo=None, updated_by="HUMAN_ADMIN", db_path=DB_PATH):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if memo:
        cursor.execute(
            "UPDATE entity_state_ledger SET status = ?, memo = ?, last_updated_by = ?, updated_at = ? WHERE item_id = ?",
            (status, memo, updated_by, now_str, item_id)
        )
    else:
        cursor.execute(
            "UPDATE entity_state_ledger SET status = ?, last_updated_by = ?, updated_at = ? WHERE item_id = ?",
            (status, updated_by, now_str, item_id)
        )
        
    if cursor.rowcount == 0:
        print(f"【警告】未找到指定項目: {item_id}", file=sys.stderr)
    else:
        conn.commit()
        print(f"✅ 成功更新 [{item_id}] 狀態為 [{status}] (更新者: {updated_by})")
    conn.close()

def add_ledger_item(item_id, item_type, item_name, prefix_code="", apqc_id="", status="DRAFT", memo="", owner_agent_id="", updated_by="HUMAN_ADMIN", db_path=DB_PATH):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor.execute(
            """INSERT INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, updated_by, now_str)
        )
        conn.commit()
        print(f"✅ 成功註冊資產 [{item_id}] ({item_name}) - 初始狀態: {status}")
    except sqlite3.IntegrityError:
        print(f"【錯誤】項目已存在: {item_id}，請使用 update 指令進行變更", file=sys.stderr)
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="全域實體狀態總控表 (entity_state_ledger) CLI 維運工具")
    subparsers = parser.add_subparsers(dest="command", help="子指令")
    
    # List command
    list_parser = subparsers.add_parser("list", help="查詢實體狀態清單")
    list_parser.add_argument("--status", help="依狀態過濾 (例: DRAFT, ACTIVE, IN_SHADOW_TEST, DEPRECATED, BLOCKED)")
    list_parser.add_argument("--type", help="依類型過濾 (例: DOCUMENT, AGENT, WORKFLOW, TASK)")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="手動更新項目狀態與 Memo")
    update_parser.add_argument("item_id", help="項目唯一 ID (例: SOP-OPS-001)")
    update_parser.add_argument("--status", required=True, help="新狀態 (例: ACTIVE, IN_SHADOW_TEST, BLOCKED)")
    update_parser.add_argument("--memo", help="補充審查備註或理由")
    update_parser.add_argument("--by", default="HUMAN_ADMIN", help="更新者標識")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="手動註冊資產狀態")
    add_parser.add_argument("item_id", help="項目唯一 ID (例: AGT-MED-001)")
    add_parser.add_argument("item_type", help="項目類型 (例: DOCUMENT, AGENT, WORKFLOW)")
    add_parser.add_argument("item_name", help="項目名稱 (例: 行一診所院長 Agent)")
    add_parser.add_argument("--prefix", default="", help="Prefix 編碼")
    add_parser.add_argument("--apqc", default="", help="APQC 條碼")
    add_parser.add_argument("--status", default="DRAFT", help="初始狀態 (預設 DRAFT)")
    add_parser.add_argument("--memo", default="", help="審查備註")
    add_parser.add_argument("--owner", default="", help="主責 Agent ID")
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_ledger(status_filter=args.status, item_type_filter=args.type)
    elif args.command == "update":
        update_ledger(item_id=args.item_id, status=args.status, memo=args.memo, updated_by=args.by)
    elif args.command == "add":
        add_ledger_item(
            item_id=args.item_id,
            item_type=args.item_type,
            item_name=args.item_name,
            prefix_code=args.prefix,
            apqc_id=args.apqc,
            status=args.status,
            memo=args.memo,
            owner_agent_id=args.owner
        )
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
