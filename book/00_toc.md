# 📖 虛擬企業總體白皮書 (Virtual Enterprise Book) 總目錄大綱

- **專書名稱：** 虛擬企業建模與 AI 原生賦能總體白皮書 (Virtual Enterprise Master Book)
- **大綱模式：** 意圖驅動式兩層大綱 (Intent-Driven 2-Level ToC)
- **版本：** v0.1
- **規範對接：** `sovereign-writing-navigator` & `Chapter_1_3.md`

---

## 📚 兩層大綱與寫作意圖 (Intent-Driven ToC)

### 第一章：虛擬企業願景與雙軌融合方法學 (Virtual Enterprise Vision & Hydration Methodology)
- `[寫作意圖 (Intent)]`：闡明企業導入 AI 避開舊官僚流程摩擦的核心戰略，奠定以終為始建立數位雙生體並實施 Token 套利與雙軌融合的總體思維。
- `[實體地基 (Grounding Base)]`：對接 `Chapter_1_3.md` L0-L4 團隊級層次化賦能架構與 `virtual-enterprise-idea.md` Token 套利邏輯。

#### 1.1 兩階段職能解耦與 Token 套利機制
- `[寫作意圖 (Intent)]`：定義將高能耗網頁檢索外包給 Deep Research 工具、內建 AI 僅處理結構對齊的兩階段作業規範。
- `[實體地基 (Grounding Base)]`：`REQ-001` Token 套利規格、`SPC-001` 兩階段解耦作業流程。

#### 1.2 確定性骨架與血肉融合 (Hydration) 物理工序
- `[寫作意圖 (Intent)]`：說明如何將外部收集之真實企業產品、團隊特色與營運痛點血肉，注入至 APQC 與 ISO 剛性骨架中。
- `[實體地基 (Grounding Base)]`：APQC PCF 標準編號與 ISO 9001/27001 控制點法規。

---

### 第二章：L0-L4 團隊級遺傳密碼與二維座標體系 (L0-L4 Genetic Code & Coordinate Architecture)
- `[寫作意圖 (Intent)]`：建立企業團隊級脈絡封裝格式，將企業資產分層樂高化並以二維座標精確定位，徹底消滅 RAG 隨機幻覺。
- `[實體地基 (Grounding Base)]`：`Chapter_1_3.md` L0-L4 五大遺傳感官與二維座標矩陣。

#### 2.1 L0-L4 5-Layer 賦能載體定義
- `[寫作意圖 (Intent)]`：詳細定義 L0 (型態), L1 (文明), L2 (習慣), L3 (真相), L4 (專家手感) 五層載體的邊界與實體檔案形式。
- `[實體地基 (Grounding Base)]`：`REQ-002` L0-L4 座標化目錄與二維座標 ID 語法 `[DEPT]_[Lx]_[TYPE]_[NUM]`。

#### 2.2 脈絡堆疊優先級與後項覆蓋邏輯
- `[寫作意圖 (Intent)]`：規範 Agent 啟動時脈絡載入之優先級，確保現場專家靈魂手感 (L4) 擁有最高裁決權。
- `[實體地基 (Grounding Base)]`：`SPC-006` 堆疊邏輯 `L4 > L3 > L2 > L1 > L0`。

---

### 第三章：全域核心資產與 RACI 組織圖譜 (Enterprise Core Assets & RACI Governance)
- `[寫作意圖 (Intent)]`：構建企業運作之全域事實基礎 (Ground Truth)，包含組織圖、職能列表與 RACI 權責邊界，防止 Agent 越權與語意歧義。
- `[實體地基 (Grounding Base)]`：`00_Enterprise_Core/` 資料夾中之 Org Chart JSON、Functional Matrix 與 Glossary。

#### 3.1 人發財採產銷六大職能劃分與組織階層
- `[寫作意圖 (Intent)]`：定義 `01_HR` 至 `06_MKT` 六大部門之營運職能範疇與主管 Agent 角色分配。
- `[實體地基 (Grounding Base)]`：`CORE_L3_TRUTH_002_Master_Org_Chart.json`。

#### 3.2 RACI 權責矩陣與安全過濾邊界
- `[寫作意圖 (Intent)]`：明確劃分各業務節點 Responsible、Accountable、Consulted、Informed 權責，建立金流與開藥防線。
- `[實體地基 (Grounding Base)]`：`CORE_L3_RACI_003_Functional_Matrix.md` 與 ISO 27001 硬性 Guardrails。

---

### 第四章：Database-First 中控控制面與 SQLite 實體架構 (Database-First Control Plane)
- `[寫作意圖 (Intent)]`：解構傳統純向量 RAG 之漏失痛點，說明如何以關聯式 DB 作為底層硬核控制面，連結白皮書 SOP 與實體 API/SQL。
- `[實體地基 (Grounding Base)]`：`db/` 目錄、`schema.sql`、`seeds.sql` 與 `init_db.py`。

#### 4.1 中控 Meta DB 四大實體數據表設計
- `[寫作意圖 (Intent)]`：詳細說明 `external_connectors`, `apqc_data_mappings`, `agent_permissions`, `execution_audit_logs` 的數據模型與運作機制。
- `[實體地基 (Grounding Base)]`：`DSN-004` SQL Schema 與 `db/control_plane.sqlite` 實體庫。

#### 4.2 APQC 流程條碼 physical 翻譯與 SQL/API 指令驅動
- `[寫作意圖 (Intent)]`：闡述 Agent 如何將 SOP 上的條號 (如 `APQC-4.1.2`) 實體翻譯為對外部 HIS/EMR/ERP 的 SQL/API 驅動指令。
- `[實體地基 (Grounding Base)]`：`SPC-005` 控制面數據介面規格。

---

### 第五章：跨部門自動化管線與 Agent 劇本編排 (Workflows & Multi-Agent Orchestration)
- `[寫作意圖 (Intent)]`：說明 Antigravity 聲明式劇本引擎如何將碎裂的 SOP 串聯為自動化管線，並與各部門 `_workflow/` 深度結合。
- `[實體地基 (Grounding Base)]`：`_Workflow/` 與各部門 `_workflow/` 劇本 YAML 檔案。

#### 5.1 全域與部門級 `_workflow/` 劇本結構設計
- `[寫作意圖 (Intent)]`：說明跨部門全域劇本 (如新進報到 `WF-CROSS-001`、採購簽核 `WF-CROSS-002`) 與部門專屬劇本之階層編排。
- `[實體地基 (Grounding Base)]`：`_Workflow/Workflows/` 與 `01_HR`~`06_MKT` 之 `_workflow/` 目錄。

#### 5.2 Human-in-the-loop 掛起與例外管理 (Management by Exception)
- `[寫作意圖 (Intent)]`：設計超過金額門檻或高風險操作時自動掛起等待真實主管審核的人機協同機制。
- `[實體地基 (Grounding Base)]`：`iso_27001_guardrails.md` 與 `agent_permissions` 金額限制。

---

### 第六章：影子模式對齊與漸進式切換維運 (Shadow Mode Alignment & Cutover Operations)
- `[寫作意圖 (Intent)]`：提供從虛擬數位雙生體過渡至真實企業營運的物理切換指南與 Gap Analysis 方法論。
- `[實體地基 (Grounding Base)]`：`deploy_guide.md` 與 `test_plan.md` 中之 `TCV-003` 測試案例。

#### 6.1 影子測試數據雙送與 Gap Analysis 比對工序
- `[寫作意圖 (Intent)]`：說明去識別化日常數據抄送流程與獨立比較員工 vs Agent 輸出結果的工序。
- `[實體地基 (Grounding Base)]`：`SPC-004` 影子模式差異分析規格。

#### 6.2 流程重構 (BPR) 與 85% 對齊度解鎖切換標誌
- `[寫作意圖 (Intent)]`：闡述如何剔除舊官僚流程並向 AI 原生流程靠攏，以及達 85% 對齊度後解鎖自動切換的閥值機制。
- `[實體地基 (Grounding Base)]`：`REQ-005` 雙軌對齊與 BPR 轉型需求。
