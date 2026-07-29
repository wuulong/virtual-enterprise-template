# 🔒 跨部門系統級硬性規則 (Global ISO 27001 Guardrails)

本規範為全域硬性 Guardrails，任何跨部門 Workflow 與 Agent 在執行時均自動載入並強制遵守。

---

## 強制控制點 (Mandatory Guardrails)

1. **資安與個資去識別化 (Privacy & Anonymization)：**
   - 任何涉及真實客戶、員工或第三方之敏感資料，於傳送至外部 LLM 之前，必須完成 PII (Personally Identifiable Information) 去識別化。
2. **金流與高風險 API 審核 (Human-in-the-loop)：**
   - 採購或支出金額超過單筆門檻 (預設 NT$ 50,000) 時，Workflow 必須掛起 (Suspend) 並等待真實主管 Human-in-the-loop 簽核。
3. **最小權限原則 (Principle of Least Privilege)：**
   - 各部門 Agent 僅具備所屬部門目錄與對應 APQC 碼之讀寫權限。
