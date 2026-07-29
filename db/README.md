# 🎛️ 中控控制面資料庫庫 (Control Plane DB Directory)

- **版本：** v0.1
- **定位：** 本目錄存放中控控制面資料庫之 DDL (`schema.sql`)、種子資料 (`seeds.sql`) 與 Python 初始化建置腳本 (`init_db.py`)，將 SOP 上的 APQC 條號 physical 翻譯為 SQL/API 驅動指令。

---

## 🗄️ 檔案說明

1. `schema.sql` - 包含 4 大 L3 控制面數據表 DDL (`external_connectors`, `apqc_data_mappings`, `agent_permissions`, `execution_audit_logs`)
2. `seeds.sql` - 通用虛擬企業預設數據種子
3. `init_db.py` - 一鍵建置或重置 `control_plane.sqlite` 資料庫檔之初始化腳本
