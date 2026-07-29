#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[metadata]
name: init_db
description: 一鍵初始化或重置虛擬企業中控 Meta DB (control_plane.sqlite)。
author: wuulong
date: 2026-07-30
category: virtual_enterprise
"""

import os
import sqlite3

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "control_plane.sqlite")
SCHEMA_PATH = os.path.join(SCRIPT_DIR, "schema.sql")
SEEDS_PATH = os.path.join(SCRIPT_DIR, "seeds.sql")

def init_database():
    print(f"【開始建置】正在建置中控 Meta DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 執行 schema.sql
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)

    # 執行 seeds.sql
    with open(SEEDS_PATH, "r", encoding="utf-8") as f:
        seeds_sql = f.read()
    cursor.executescript(seeds_sql)

    conn.commit()
    conn.close()
    print("【成功】`control_plane.sqlite` 資料庫與種子數據建置完成！")

if __name__ == "__main__":
    init_database()
