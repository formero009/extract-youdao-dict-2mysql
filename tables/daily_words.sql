CREATE TABLE `daily_words` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `word` varchar(32) COLLATE utf8_bin DEFAULT NULL COMMENT 'english word',
  `trans_cn` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT 'word translation in english\r\nword_type | trans;trans;trans',
  `trans_en` varchar(512) COLLATE utf8_bin DEFAULT NULL COMMENT 'word translation in chinese\r\nword_type | trans;trans;trans',
  `usphone` varchar(64) COLLATE utf8_bin DEFAULT NULL COMMENT '美式发音音标',
  `usspeech` varchar(32) COLLATE utf8_bin DEFAULT NULL COMMENT '美式发音api 参数',
  `ukphone` varchar(64) COLLATE utf8_bin DEFAULT NULL COMMENT '英式发音音标',
  `ukspeech` varchar(32) COLLATE utf8_bin DEFAULT NULL COMMENT '英式发音api参数',
  `phrase` text COLLATE utf8_bin COMMENT '短语json列表',
  `sentences` text COLLATE utf8_bin COMMENT '例句json列表',
  `book_id` varchar(16) COLLATE utf8_bin DEFAULT NULL COMMENT '关联book',
  `book_name` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '关联的book 名字',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90120 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;