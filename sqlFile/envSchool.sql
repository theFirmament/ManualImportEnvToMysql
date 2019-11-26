DROP TABLE IF EXISTS `school_env`;
CREATE TABLE IF NOT EXISTS `school_env` (
    `id` tinyint PRIMARY KEY NOT NULL auto_increment COMMENT "序号",
    `frpc_remote_port` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "远程连接端口",
    `campus_env` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "学校部署环境",
    `school_ip` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "学校代理服务器IP",
    `school_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "学校代理服务器ID",
    `signature_key` varchar(1023) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "signature_key",
    `cjpadc_unlock_password` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT "1" COMMENT "unlock_password",
    `cjcbs_docker_version` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "cjcbs版本",
    `cjpadc_docker_version` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "cjpadc版本",
    `cjpad_docker_version` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "apk版本",
    `ip_whitelist` varchar(1023) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT "教室IP白名单"
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;