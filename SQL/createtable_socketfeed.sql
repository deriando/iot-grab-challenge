USE iotdatabase;
DROP TABLE IF EXISTS `socketfeed`;
CREATE TABLE `socketfeed` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bookingid` mediumtext NOT NULL,
  `startdatetime_value` datetime DEFAULT NULL,
  `enddatetime_value` datetime DEFAULT NULL,
  `timestamp_value` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) 