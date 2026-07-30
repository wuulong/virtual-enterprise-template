---
title: "通用型虛擬企業實體落地與分階段導入推動指引方案 (VE Adoption Guide)"
version: "v1.5"
status: "Approved"
last_updated: "2026-07-31"
author: "wuulong / Antigravity"
---

# 🚀 通用型虛擬企業實體落地與分階段導入推動指引方案 (VE Adoption Guide)

## 📌 Executive Summary (執行摘要)

本指引旨在為**通用型虛擬企業 (Generic Virtual Enterprise Template)** 提供一套完全抽象、跨產業適用的實體落地推動框架。

依據 `[ADR-005]` 抽象隔離原則：**通用型虛擬企業永遠保持純粹與通用，不綁定任何特定產業之領域特徵**。轉型推動的核心戰略在於**「真實企業 (POC KMS) 與 對標虛擬企業 (VE) 雙軌完全隔離 (Complete Isolation)」**：
1. **真實企業：`POC KMS` (檔案型 POC 知識管理系統)**：代表正在啟動 AI 賦能的**真實企業本身**。無需資料庫或複雜 SE 建模，僅透過意圖目錄 (`00_toc.md`) + 匯入 Markdown 檔案 + 本地相對路徑索引。在個人 Agentic AI 賦能下，**當下即可獨立產出真實業務成果（提案書、草案、SOP）**。
2. **對標虛擬企業：`Virtual Enterprise (VE)` (SE-6D 標竿模擬中控系統)**：作為架構對標、影子模式 (Shadow Mode) 測試與 SE-6D 治理的**虛擬模擬載體**。
3. **完全隔離原則**：**真實企業 (`POC KMS`) 與 對標虛擬企業 (`VE`) 兩者完全隔離，絕不進行強行檔案匯入或合併**。兩者各自獨立運轉，透過指標對齊（如 85% 影子比對）確保真實企業順利推進。

---

## 🏛️ 雙軌完全隔離架構圖 (Strict Dual-Track Isolation)

```
【真實企業 (Real Enterprise)】                         【對標虛擬企業 (Benchmark VE)】
  系統 A: POC KMS (檔案型知識庫)                           系統 B: Virtual Enterprise (SE-6D 載體)
┌───────────────────────────────────────┐               ┌───────────────────────────────────────┐
│ 1. 外顯公開資料採集 (官網/申請單/FAQ) │               │ 1. 通用範本派生 (virtual-enterprise-  │
│ 2. 結構化意圖目錄 (00_toc.md)         │   ⚡ 完全隔離  │    template / SSOT Vessel)            │
│ 3. 匯入標準 Markdown 檔案與物理索引   │   (無匯入動作)│ 2. 7 大部門 (00_CORE ~ 06_MKT)        │
│ 4. 個人 Agentic AI 賦能               │  ───────────  │ 3. 中控 SQLite (entity_state_ledger)  │
│ ★ 當下即刻獨立運轉產出真實業務成果！  │               │ 4. 8 大數字狀態碼 (10~80) 狀態機      │
└───────────────────────────────────────┘               └───────────────────────────────────────┘
                    │                                                       │
                    └───────────────── 影子模式 (Shadow Mode) ──────────────┘
                                       (指標對齊度 >= 85% 驗收)
```

---

## 🗺️ 5 階段詳細推進工序與操作指引

### Stage 1: 真實企業 (`POC KMS`) 零障礙建構與獨立運轉 (即刻產出)

#### Step 1.0: 外顯公開資料採集 (Explicit Public Knowledge Ingestion)
**【真實企業啟動】：** 無需等待內部複雜機敏 DB 洗牌，直接採集真實企業早已對外公開之養分：
1. **外顯資料標的**：企業官網、對外服務申請單、客戶需求問卷、對外產品 FAQ 與說明文宣。
2. **零障礙啟動**：單人即可啟動前台諮詢與需求解讀 Agent。

#### Step 1.1: 建構真實企業獨立 `POC KMS` (檔案型 POC 知識管理系統)
**【核心架構】：** **`POC KMS` 即是開始建構的真實企業本身，與對標虛擬企業完全隔離！** 在個人配備 Agentic AI 助手（如 Antigravity / Agentic IDE）的賦能下，無需複雜 SE 建模或伺服器 DB，光靠 `POC KMS` 即可即刻獨立運轉並產出真實業務成果（如提案書、SOP、業務草案、分析報告）：

1. **結構化意圖目錄 (Intent-Driven ToC)**：
   於真實企業 `POC KMS` 目錄下建立 `00_toc.md` 兩層結構化意圖目錄作為知識索引標籤。
2. **匯入標準 Markdown 檔案 (Markdown Ingestion)**：
   將採集之外顯資料與業務規範，一律轉化匯入為乾淨、標準的 Markdown 檔案。
3. **檔案型物理相對路徑索引 (Relative Path Indexing)**：
   採用極簡本地相對路徑（如 `[SOP說明](file:///path/to/sop.md)`），零伺服器資料庫架設成本。
4. **個人 Agentic 獨立運轉產出**：
   賦能代理人直接讀取 `POC KMS` 檔案索引，當下即可協助產出專業提案書、客戶簡報草案、SOP 初稿與分析報告！

---

### Stage 2: 對標虛擬企業 (`VE`) 建構與全資產物理盤點 (Status `10` ➔ `20`)

#### Step 2.1: 獨立派生對標虛擬企業 (`VE`) 與全資產物理掃描
在獨立於 `POC KMS` 的對標虛擬企業 (`VE`) 中，於中控 DB 發動物理掃描，將範本 7 大部門的所有職能 (`FNC-xxx`)、擬真系統 (`SYS-xxx`)、Workflow (`WF-xxx`)、SOP Markdown (`SOP-xxx`) 與 Agent JSON (`AGT-xxx`) 寫入中控 SQLite：

```bash
cd VE/db
python3 manage_ledger.py scan
```

#### Step 2.2: 四維價值矩陣評估與二維座標 ID 定錨
針對 `VE` 盤點資產進行四維評分（商業效益 ROI、技術可行性、合規資安風險、人機協作複雜度），並打上 `[DEPT]_[Lx]_[TYPE]_[NUM]` 座標 ID，升級為 **`20` (虛擬確認 / VIRTUAL_CONFIRMED)**：
```bash
python3 manage_ledger.py update FNC-MKT-001 --status 20 --memo "對標 VE 盤點完成，通過虛擬審查"
```

---

### Stage 3: 影子模式 (Shadow Mode) 對齊測試 (Status `30` ➔ `50`)

#### 1. 通用關鍵 POC 挑選原則 (The 80/20 Rule)
精選 1~2 個高頻率、高重複性、成果易量化的流程（如：第一線業務訪談紀錄摘要、發票憑證自動勾稽、HR 履歷自動匹配）。

#### 2. 雙軌影子測試與 85% 對齊度驗收
- 將真實企業 (`POC KMS`) 產出之去識別化個案，抄送至對標虛擬企業 (`VE`) 進行影子測試。
- `VE` 中控 DB 狀態升級為 **`30` (真實對接啟動)** ➔ **`40` (對齊進行中)**。
- 比對兩者決策一致性。一致性 **>= 85%** 時，升級為 **`50` (已對齊 / ALIGNED)**：
  ```bash
  python3 manage_ledger.py update SOP-OPS-001 --status 50 --memo "雙軌影子比對一致性達 87.5%，通過驗收" --meta '{"alignment_rate": 87.5}'
  ```

---

### Stage 4: 全社分階段擴展導入路徑 (Status `60`)

| 推進階段 | 時間軸 | 主體系統 | 推動核心任務 | 驗收與解鎖條件 | 狀態標誌 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 0: 外顯知識與 POC KMS** | **Day 1-14** | **真實企業 (POC KMS)** | 建構獨立 `POC KMS` (`00_toc.md` + Markdown + 檔案索引)，上線前台諮詢 Agent。 | 個人 Agentic 賦能即刻產出提案與草案，產生真實降本效益。 | `20` (虛擬確認) |
| **Phase I: 雙軌影子測試** | **Month 1-2** | **POC KMS + VE 雙軌** | 雙軌完全隔離，去識別化個案抄送進行 1~2 個內部 POC 影子比對。 | POC 流程影子對齊度 >= 85%，產出定量 ROI 報告。 | `50` (已對齊) |
| **Phase II: 核心鏈串接** | **Month 3-6** | **對標 VE 系統** | 跨部門核心業務鏈串接 (例: `05_OPS` + `03_FIN` + `00_CORE` 聯動)。 | 完成 HitL 簽核門檻（如 50,000 元以上自動觸發人工審核）。 | `60` (已確認) |
| **Phase III: 全社例外管理** | **Month 7-12** | **對標 VE 系統** | 全面解鎖「例外管理 (Management by Exception)」，AI 處理 90% 例行事務。 | 全公司 80% 資產處於 `60` 狀態，營運邊際成本顯著下降。 | `60` (已確認) |

---

### Stage 5: 長效營運與動態修訂維護 (Status `70` ➔ `80`)

- 外部法規、市場環境變更時，於 `VE` 中控 DB 觸發修訂 **`70` (修訂中)**。
- 二次審查確認後升級 **`80` (修訂確認)**，驗收無誤重置回 **`60` (正式營運)**。

---

## 📄 關聯文件與存檔資訊

- **檔案絕對路徑：** [events-2026Q3/virtual-enterprise/sys_eng/06_release_operations/ve_adoption_guide.md](file:///Users/wuulong/github/bmad-pa/events-2026Q3/virtual-enterprise/sys_eng/06_release_operations/ve_adoption_guide.md)
- **模板隨附路徑：** [virtual-enterprise-template/docs/ve_adoption_guide.md](file:///Users/wuulong/github/bmad-pa/events-2026Q3/virtual-enterprise/virtual-enterprise-template/docs/ve_adoption_guide.md)
