USE iotdatabase;

DROP TABLE IF EXISTS `telemetry`;

CREATE TABLE `telemetry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bookingid` mediumtext NOT NULL,
  `accuracy` float DEFAULT NULL,
  `bearing` float DEFAULT NULL,
  `acceleration_x` double DEFAULT NULL,
  `acceleration_y` double DEFAULT NULL,
  `acceleration_z` double DEFAULT NULL,
  `gyro_x` double DEFAULT NULL,
  `gyro_y` double DEFAULT NULL,
  `gyro_z` double DEFAULT NULL,
  `seconds` int DEFAULT NULL,
  `speed` double DEFAULT NULL,
  `speedkmhour` double DEFAULT NULL,
  PRIMARY KEY (`id`)
);
