-- Control Plane Seeds Data (v0.1)

INSERT INTO external_connectors (connector_id, system_name, api_endpoint, auth_type, status)
VALUES ('CONN-001', 'GENERIC_ERP_SYSTEM', 'https://api.generic-enterprise.local/v1', 'JWT', 'ACTIVE');

INSERT INTO apqc_data_mappings (mapping_id, apqc_code, layer_level, sop_id, target_table, target_api_action)
VALUES ('MAP-001', 'APQC-7.1', 'L2', 'HR_L2_SOP_001_recruitment_sop.md', 'employees', 'POST /onboarding');

INSERT INTO agent_permissions (permission_id, agent_id, apqc_code, raci_role, max_approval_amount)
VALUES 
('PERM-001', 'AGT-HR-001', 'APQC-7.1', 'A', 0.00),
('PERM-002', 'AGT-FIN-001', 'APQC-9.1', 'A', 50000.00),
('PERM-003', 'AGT-PROC-001', 'APQC-4.2', 'R', 10000.00);

-- 全域實體狀態總控表預設種子資料
INSERT INTO entity_state_ledger (item_id, item_type, item_name, prefix_code, apqc_id, status, memo, owner_agent_id, last_updated_by)
VALUES
('SOP-HR-001', 'DOCUMENT', '醫護招募與在宅護理師排班 SOP', '01_HR_01', 'APQC-7.1', 'ACTIVE', '通用範本正式上線條目', 'AGT-HR-001', 'HYDRATION_ENGINE'),
('SOP-OPS-001', 'DOCUMENT', '現場床邊診療與語音口述 SOAP 病歷轉換 SOP', '05_OPS_01', 'APQC-4.2', 'IN_SHADOW_TEST', '進行 85% 影子對齊測試中', 'AGT-MED-001', 'HYDRATION_ENGINE'),
('WF-FIN-001', 'WORKFLOW', '財務費用報支審核與月度結帳劇本', '03_FIN_01', 'APQC-5.2', 'ACTIVE', '門檻 50,000 以上觸發 HitL 審核', 'AGT-FIN-001', 'HYDRATION_ENGINE'),
('AGT-MED-001', 'AGENT', '行一診所院長/主治醫師 Agent', '05_OPS_00', 'APQC-4.2', 'ACTIVE', '主責現場診療與 SOAP 裁決', 'AGT-MED-001', 'HUMAN_ADMIN');
