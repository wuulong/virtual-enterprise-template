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
