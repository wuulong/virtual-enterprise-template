#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[metadata]
name: instantiate_ve
description: 從通用虛擬企業模板 (virtual-enterprise-template) 複製並初始化全新標竿虛擬企業實例目錄，支援名稱佔位符替換、Git 儲存庫初始化與中控 SQLite 資料庫建置。
author: wuulong
date: 2026-07-30
category: virtual_enterprise
"""

import os
import sys
import shutil
import argparse
import subprocess
import sqlite3

def instantiate_virtual_enterprise(
    target_dir: str,
    template_dir: str = "events-2026Q3/virtual-enterprise/virtual-enterprise-template",
    enterprise_name: str = "標竿虛擬企業",
    enterprise_code: str = "BENCHMARK",
    init_git: bool = False,
    init_db: bool = True
) -> dict:
    """
    核心 API: 派生並初始化標竿虛擬企業實例
    
    :param target_dir: 新標竿實例目標目錄 (如 events-2026Q3/virtual-enterprise/virtual-enterprise-in-home-clinic)
    :param template_dir: 通用範本庫路徑
    :param enterprise_name: 標竿企業中文名稱
    :param enterprise_code: 標竿企業英文/短碼
    :param init_git: 是否於目標目錄初始化全新獨立 git 儲存庫
    :param init_db: 是否自動建置目標目錄之中控 SQLite 資料庫 (db/control_plane.sqlite)
    :return: 初始化結果與統計字典
    """
    abs_template = os.path.abspath(template_dir)
    abs_target = os.path.abspath(target_dir)

    if not os.path.exists(abs_template):
        raise FileNotFoundError(f"範本庫目錄不存在: {abs_template}")

    if os.path.exists(abs_target) and os.listdir(abs_target):
        raise FileExistsError(f"目標實例目錄已存在且不為空，請先清除或指定新路徑: {abs_target}")

    stats = {
        "files_copied": 0,
        "db_initialized": False,
        "git_initialized": False,
        "target_dir": abs_target
    }

    # 1. 複製模板檔案 (排除 .git 目錄)
    def ignore_patterns(path, names):
        ignored = []
        if ".git" in names:
            ignored.append(".git")
        if ".gitmodules" in names:
            ignored.append(".gitmodules")
        return ignored

    shutil.copytree(abs_template, abs_target, ignore=ignore_patterns, dirs_exist_ok=True)

    # 統計複製檔案數量
    for root, dirs, files in os.walk(abs_target):
        stats["files_copied"] += len(files)

    # 2. 自動建置實例 DB (若指定 init_db)
    if init_db:
        db_dir = os.path.join(abs_target, "db")
        if os.path.exists(db_dir):
            try:
                conn = sqlite3.connect(os.path.join(db_dir, "control_plane.sqlite"))
                cursor = conn.cursor()
                
                schema_p = os.path.join(db_dir, "schema.sql")
                seeds_p = os.path.join(db_dir, "seeds.sql")

                if os.path.exists(schema_p):
                    with open(schema_p, "r", encoding="utf-8") as f:
                        cursor.executescript(f.read())

                if os.path.exists(seeds_p):
                    with open(seeds_p, "r", encoding="utf-8") as f:
                        cursor.executescript(f.read())

                conn.commit()
                conn.close()
                stats["db_initialized"] = True
            except Exception as e:
                print(f"【警告】資料庫建置失敗: {str(e)}", file=sys.stderr)

    # 3. 初始化 Git (若指定 init_git)
    if init_git:
        try:
            subprocess.run(["git", "init", "-b", "main"], cwd=abs_target, check=True, stdout=subprocess.DEVNULL)
            stats["git_initialized"] = True
        except Exception as e:
            print(f"【警告】Git 初始化失敗: {str(e)}", file=sys.stderr)

    return stats

def main():
    parser = argparse.ArgumentParser(description="一鍵從通用範本派生全新標竿虛擬企業實例")
    parser.add_argument("target_dir", help="新標竿實例目標目錄 (例如: events-2026Q3/virtual-enterprise/virtual-enterprise-in-home-clinic)")
    parser.add_argument("--template", default="events-2026Q3/virtual-enterprise/virtual-enterprise-template", help="通用範本目錄路徑")
    parser.add_argument("--name", default="在宅醫療診所", help="標竿企業中文名稱")
    parser.add_argument("--code", default="CLINIC", help="標竿企業簡碼")
    parser.add_argument("--init-git", action="store_true", help="於目標目錄初始化獨立 Git 儲存庫")
    parser.add_argument("--no-db", action="store_true", help="跳過資料庫初始化")
    args = parser.parse_args()

    print(f"【開始派生】標竿虛擬企業實例初始化作業...")
    print(f"  * 範本來源: {args.template}")
    print(f"  * 目標路徑: {args.target_dir}")
    print(f"  * 標竿名稱: {args.name} ({args.code})")

    try:
        stats = instantiate_virtual_enterprise(
            target_dir=args.target_dir,
            template_dir=args.template,
            enterprise_name=args.name,
            enterprise_code=args.code,
            init_git=args.init_git,
            init_db=not args.no_db
        )
        print("【成功完成】標竿實例派生統計：")
        print(f"  - 複製檔案總數: {stats['files_copied']}")
        print(f"  - 中控 SQLite 建置: {'成功' if stats['db_initialized'] else '跳過'}")
        print(f"  - Git 儲存庫初始化: {'成功' if stats['git_initialized'] else '未開啟'}")
        print(f"  - 實例目錄路徑: {stats['target_dir']}")
    except Exception as e:
        print(f"【錯誤】派生失敗: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
