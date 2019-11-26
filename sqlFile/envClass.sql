DROP TABLE IF EXISTS `class_env`;
CREATE TABLE IF NOT EXISTS `class_env` (
    `id` tinyint PRIMARY KEY NOT NULL auto_increment COMMENT "序号",
    `frpc_remote_port` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "远程连接端口",
    `class_ip` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "教室IP",
    `class_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "教室ID",
    `cjpadc_cbs_host` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "AP连接IP"
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;