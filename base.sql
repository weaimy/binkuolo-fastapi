/*
 Navicat Premium Data Transfer

 Source Server         : 本地连接
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : 127.0.0.1:3306
 Source Schema         : base

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 01/06/2023 22:41:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for access
-- ----------------------------
DROP TABLE IF EXISTS `access`;
CREATE TABLE `access`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `access_name` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '权限名称',
  `parent_id` int(11) NOT NULL DEFAULT 0 COMMENT '父id',
  `scopes` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '权限范围标识',
  `access_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '权限描述',
  `menu_icon` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '菜单图标',
  `is_check` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否验证权限 True为验证 False不验证',
  `is_menu` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否为菜单 True菜单 False不是菜单',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `scopes`(`scopes`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '权限表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of access
-- ----------------------------
INSERT INTO `access` VALUES (1, '2022-05-18 18:28:15.699736', '2022-05-18 18:28:15.699771', '用户中心', 0, 'user', NULL, NULL, 0, 1);
INSERT INTO `access` VALUES (2, '2022-05-18 18:28:55.162023', '2022-05-18 18:28:55.162070', '用户管理', 1, 'user_m', NULL, NULL, 0, 1);
INSERT INTO `access` VALUES (3, '2022-05-18 18:31:48.630306', '2022-05-18 18:31:48.630354', '角色管理', 1, 'role_m', NULL, NULL, 0, 1);
INSERT INTO `access` VALUES (4, '2022-05-18 18:32:45.768538', '2022-05-19 07:27:43.328990', '用户查询', 2, 'user_query', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (5, '2022-05-18 18:33:05.634450', '2022-05-18 18:33:05.634498', '用户添加', 2, 'user_add', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (6, '2022-05-18 18:33:35.677990', '2022-05-18 18:33:35.678038', '用户编辑', 2, 'user_update', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (7, '2022-05-18 18:33:53.455916', '2022-05-18 18:33:53.455964', '用户删除', 2, 'user_delete', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (8, '2022-05-18 18:34:55.614617', '2022-05-19 11:32:14.861397', '角色分配', 2, 'user_role', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (9, '2022-05-18 18:35:16.093767', '2022-05-19 09:15:13.190683', '角色查询', 3, 'role_query', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (10, '2022-05-18 18:35:35.856673', '2022-05-19 09:14:55.453576', '角色添加', 3, 'role_add', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (11, '2022-05-18 18:35:53.266453', '2022-05-19 09:14:41.721341', '角色编辑', 3, 'role_update', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (12, '2022-05-18 18:36:27.876248', '2022-05-19 09:14:23.501602', '角色删除', 3, 'role_delete', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (13, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', '权限分配', 3, 'role_access', NULL, NULL, 1, 0);

-- ----------------------------
-- Table structure for access_log
-- ----------------------------
DROP TABLE IF EXISTS `access_log`;
CREATE TABLE `access_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `user_id` int(11) NOT NULL COMMENT '用户ID',
  `target_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '访问的url',
  `user_agent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '访问UA',
  `request_params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '请求参数get|post',
  `ip` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '访问IP',
  `note` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '用户操作记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of access_log
-- ----------------------------

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `role_name` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色名称',
  `role_status` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'True:启用 False:禁用',
  `role_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '角色描述',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '角色表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------

-- ----------------------------
-- Table structure for role_access
-- ----------------------------
DROP TABLE IF EXISTS `role_access`;
CREATE TABLE `role_access`  (
  `role_id` int(11) NOT NULL,
  `access_id` int(11) NOT NULL,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `access_id`(`access_id`) USING BTREE,
  CONSTRAINT `role_access_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `role_access_ibfk_2` FOREIGN KEY (`access_id`) REFERENCES `access` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role_access
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户名',
  `user_type` tinyint(1) NOT NULL DEFAULT 0 COMMENT '用户类型 True:超级管理员 False:普通管理员',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'binkuolo' COMMENT '昵称',
  `user_phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `user_email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `full_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '姓名',
  `user_status` int(11) NOT NULL DEFAULT 0 COMMENT '0未激活 1正常 2禁用',
  `header_img` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '头像',
  `sex` int(11) NULL DEFAULT 0 COMMENT '0未知 1男 2女',
  `remarks` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  `client_host` varchar(19) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '访问IP',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '用户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '2022-05-18 18:25:56.776176', '2022-05-19 09:51:02.845342', 'admin', 1, '$pbkdf2-sha256$29000$TYnxfk.pNYZwLgXA2DsHgA$8x2oHJzqMjATdVnHIO86DsU3xhQ7IzvIB.1H8tDyHpQ', 'binkuolo', '13345678120', NULL, NULL, 1, NULL, 0, 'string', NULL);

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role`  (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_role
-- ----------------------------

-- ----------------------------
-- Table structure for weaimy_article
-- ----------------------------
DROP TABLE IF EXISTS `weaimy_article`;
CREATE TABLE `weaimy_article`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标题',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '正文内容',
  `img` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '缩略图',
  `seo_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `seo_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `tags` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标签',
  `source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '来源',
  `category_id` int(11) NOT NULL COMMENT '所属栏目',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_weaimy_a_weaimy_c_0116f642`(`category_id`) USING BTREE,
  CONSTRAINT `fk_weaimy_a_weaimy_c_0116f642` FOREIGN KEY (`category_id`) REFERENCES `weaimy_category` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '栏目表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of weaimy_article
-- ----------------------------
INSERT INTO `weaimy_article` VALUES (1, '2023-05-21 08:55:08.738662', '2023-05-21 08:55:08.738662', '测试一下', '<p><span style=\"\">sfk</span><span class=\"transmart-tgt-font-container\" style=\"\">瑞典自由党</span><span style=\"\">c</span></p>', NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `weaimy_article` VALUES (2, '2023-05-21 09:04:01.330223', '2023-05-21 09:04:01.330223', '测试公司新闻文章标题', '<p><span style=\"\">s</span><span style=\"\">s翻到的多多多多多多多多多多多多多多多多</span></p>', NULL, NULL, NULL, NULL, NULL, 2);
INSERT INTO `weaimy_article` VALUES (3, '2023-05-21 09:04:31.601638', '2023-05-21 09:04:31.601638', '测试行业资讯是框架的疯狂拉设计费', '<p>沙发的说法水电费<span style=\"\">电风扇</span><span style=\"\">sssssssssssssssss</span><span class=\"transmart-tgt-font-container\" style=\"\">ssssssssssssssssss</span><span style=\"\">ssssssssssss</span><span class=\"transmart-tgt-font-container\" style=\"\">ssssssssssssssss</span></p>', NULL, NULL, NULL, NULL, NULL, 3);

-- ----------------------------
-- Table structure for weaimy_category
-- ----------------------------
DROP TABLE IF EXISTS `weaimy_category`;
CREATE TABLE `weaimy_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '网站名称',
  `parent_id` int(11) NOT NULL DEFAULT 0 COMMENT '父id',
  `type` smallint(6) NOT NULL DEFAULT 1 COMMENT '栏目类型',
  `url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '链接地址',
  `seo_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `seo_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `sort` int(11) NOT NULL DEFAULT 0 COMMENT '排序',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '栏目表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of weaimy_category
-- ----------------------------
INSERT INTO `weaimy_category` VALUES (1, '2023-05-21 08:54:51.161868', '2023-05-21 08:54:51.161868', '新闻资讯', 0, 1, NULL, NULL, NULL, 1, 0);
INSERT INTO `weaimy_category` VALUES (2, '2023-05-21 09:03:10.803667', '2023-05-21 09:03:10.803667', '公司新闻', 1, 1, NULL, NULL, NULL, 1, 0);
INSERT INTO `weaimy_category` VALUES (3, '2023-05-21 09:03:28.122500', '2023-05-21 09:03:28.122500', '行业资讯', 1, 1, NULL, NULL, NULL, 1, 0);

-- ----------------------------
-- Table structure for weaimy_job
-- ----------------------------
DROP TABLE IF EXISTS `weaimy_job`;
CREATE TABLE `weaimy_job`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标题',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '工作内容',
  `work_address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '工作地点',
  `work_nature` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '全职' COMMENT '工作性质',
  `work_education` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '不限' COMMENT '学历要求',
  `work_money` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '面议' COMMENT '薪资待遇',
  `work_age` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '不限' COMMENT '工作年限',
  `work_num` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '若干' COMMENT '招聘人数',
  `category_id` int(11) NOT NULL COMMENT '所属栏目',
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '状态',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_weaimy_j_weaimy_c_50310dfb`(`category_id`) USING BTREE,
  CONSTRAINT `fk_weaimy_j_weaimy_c_50310dfb` FOREIGN KEY (`category_id`) REFERENCES `weaimy_category` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '招聘表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of weaimy_job
-- ----------------------------

-- ----------------------------
-- Table structure for web_category
-- ----------------------------
DROP TABLE IF EXISTS `web_category`;
CREATE TABLE `web_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '网站名称',
  `url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '链接地址',
  `parent_id` int(11) NOT NULL DEFAULT 0 COMMENT '父id',
  `type` smallint(6) NOT NULL DEFAULT 2 COMMENT '栏目类型',
  `seo_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `seo_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `sort` int(11) NOT NULL DEFAULT 0 COMMENT '排序',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '栏目表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_category
-- ----------------------------
INSERT INTO `web_category` VALUES (1, '2023-05-03 21:05:44.172077', '2023-05-03 21:05:44.172094', '新闻资讯', NULL, 0, 1, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (2, '2023-05-03 21:38:50.773123', '2023-05-03 21:38:50.773141', '公司新闻', NULL, 1, 1, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (3, '2023-05-09 00:37:09.178291', '2023-05-10 07:09:09.593791', '产品展示', NULL, 0, 2, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (4, '2023-05-09 00:37:57.147228', '2023-05-09 00:37:57.147242', '前端产品', NULL, 3, 2, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (5, '2023-05-09 22:34:09.130316', '2023-05-09 22:37:18.106012', '关于我们', NULL, 0, 4, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (6, '2023-05-09 22:39:23.735230', '2023-05-09 22:39:35.845197', '公司简介', NULL, 5, 4, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (7, '2023-05-09 22:42:49.917574', '2023-05-09 22:44:18.214605', '发展历程', NULL, 5, 4, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (8, '2023-05-09 22:45:51.762264', '2023-05-09 22:53:56.411845', '企业形象', NULL, 5, 4, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (9, '2023-05-10 07:13:35.029029', '2023-05-10 07:13:35.029046', '客户案例', NULL, 0, 2, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (10, '2023-05-10 07:14:55.397973', '2023-05-10 07:14:55.397991', '城市规划', NULL, 9, 2, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (11, '2023-05-10 07:15:22.052337', '2023-05-10 07:15:52.300994', '居住建筑', NULL, 9, 2, NULL, NULL, 1, 0);
INSERT INTO `web_category` VALUES (12, '2023-05-10 07:16:21.719686', '2023-05-10 07:16:21.719702', '公共建筑', NULL, 9, 2, NULL, NULL, 1, 0);

-- ----------------------------
-- Table structure for web_news
-- ----------------------------
DROP TABLE IF EXISTS `web_news`;
CREATE TABLE `web_news`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '网站名称',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '正文内容',
  `img` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '缩略图',
  `seo_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `seo_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `category_id` int(11) NOT NULL DEFAULT 0 COMMENT '栏目id',
  `tags` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标签',
  `source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '来源',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '栏目表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_news
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;