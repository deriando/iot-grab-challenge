USE iotdatabase;
DROP TABLE IF EXISTS `iotapp`;

CREATE TABLE iotapp
(
  id int NOT NULL AUTO_INCREMENT,
  datetime_value datetime,
  timestamp_value TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  datetimestart_value varchar(255),
  bookingid mediumtext NOT NULL,
  bookingidwithtime mediumtext NOT NULL,
  accuracy float,
  bearing float,
  acceleration_x double,
  acceleration_y double,
  acceleration_z double,
  gyro_x double,
  gyro_y double,
  gyro_z double,
  seconds int, 
  speed double,
  speedkmhour double, 
  PRIMARY KEY (id)
);
