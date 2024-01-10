

CREATE DATABASE `planthealthdb` 

CREATE TABLE `sensor_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `humidity` int DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
)