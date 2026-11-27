CREATE DATABASE IF NOT EXISTS disease_iot_agriculture;
USE disease_iot_agriculture;

DROP TABLE IF EXISTS `alerts`;
CREATE TABLE `alerts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `type` varchar(50) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `alerts` (`id`, `title`, `message`, `type`, `date`) VALUES ('1', 'Heavy Rain Warning!', 'High chances of heavy raining and lightning.', 'Weather', '2026-03-20');


DROP TABLE IF EXISTS `branch`;
CREATE TABLE `branch` (
  `branch_id` varchar(20) NOT NULL,
  `address` varchar(450) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(45) NOT NULL,
  `pincode` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `iddistrict` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `branch` (`branch_id`, `address`, `phone`, `email`, `pincode`, `password`, `iddistrict`) VALUES ('Krishi', 'Sample Block A, Alappuzha', '9000000001', 'branch1@example.com', '680001', 'branch123', '1');
INSERT INTO `branch` (`branch_id`, `address`, `phone`, `email`, `pincode`, `password`, `iddistrict`) VALUES ('Krishi Bhavan Karuma', 'Sample Block B, Ernakulam', '9000000002', 'branch2@example.com', '680002', 'branch123', '2');
INSERT INTO `branch` (`branch_id`, `address`, `phone`, `email`, `pincode`, `password`, `iddistrict`) VALUES ('Krishi wayanad', 'Sample Block C, Wayanad', '9000000003', 'branch3@example.com', '680003', 'branch123', '14');
INSERT INTO `branch` (`branch_id`, `address`, `phone`, `email`, `pincode`, `password`, `iddistrict`) VALUES ('Krishibhavan Kannur', 'Sample Block D, Kannur', '9000000004', 'branch4@example.com', '680004', 'branch123', '4');
INSERT INTO `branch` (`branch_id`, `address`, `phone`, `email`, `pincode`, `password`, `iddistrict`) VALUES ('Meenachil', 'Sample Block E, Kottayam', '9000000005', 'branch5@example.com', '680005', 'branch123', '7');


DROP TABLE IF EXISTS `crop`;
CREATE TABLE `crop` (
  `crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT '0',
  PRIMARY KEY (`crop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `crop` (`crop_id`, `name`, `description`, `quantity`) VALUES ('1', 'Rice', 'Staple food for over half the world''s population', '1000');
INSERT INTO `crop` (`crop_id`, `name`, `description`, `quantity`) VALUES ('2', 'Wheat ', 'Major temperate cereal for bread and flour.', '850');
INSERT INTO `crop` (`crop_id`, `name`, `description`, `quantity`) VALUES ('3', 'Maize', ' Versatile for food, fodder, and industry', '600');
INSERT INTO `crop` (`crop_id`, `name`, `description`, `quantity`) VALUES ('4', 'Soybean ', 'used for oil, animal feed, and protein-rich', '350');
INSERT INTO `crop` (`crop_id`, `name`, `description`, `quantity`) VALUES ('7', 'pea', 'green pea from australia', '100');


DROP TABLE IF EXISTS `crop_booking`;
CREATE TABLE `crop_booking` (
  `crop_booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `branch_id` varchar(50) DEFAULT NULL,
  `crop_id` varchar(50) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  `book_date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `quantity` int(11) DEFAULT 1,
  PRIMARY KEY (`crop_booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('1', 'Krishi', '1', 'farmer1', '2026-02-24', 'Approved', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('2', 'krishi', '3', 'farmer1', '2026-02-26', 'Approved', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('3', 'krishi', '2', 'farmer1', '2026-02-26', 'Pending', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('4', 'krishi', '4', 'farmer1', '2026-02-26', 'Approved', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('5', 'krishi', '6', 'farmer1', '2026-02-26', 'Approved', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('6', 'krishi', '3', 'farmer1', '2026-02-26', 'Approved', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('7', 'krishi', '6', 'farmer1', '2026-02-27', 'Pending', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('8', 'Krishi', '1', 'farmer1', '2026-03-02', 'Approved', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('9', 'Krishi', '2', 'farmer1', '2026-03-17', 'Pending', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('10', 'Krishi', '1', 'farmer1', '2026-03-17', 'Pending', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('11', 'Krishi', '7', 'farmer1', '2026-03-17', 'Rejected', '1');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('12', 'Krishi', '3', 'farmer1', '2026-03-19', 'Approved', '50');
INSERT INTO `crop_booking` (`crop_booking_id`, `branch_id`, `crop_id`, `user_id`, `book_date`, `status`, `quantity`) VALUES ('13', 'Krishi', '3', 'farmer1', '2026-03-19', 'Approved', '650');


DROP TABLE IF EXISTS `data_from_hardware`;
CREATE TABLE `data_from_hardware` (
  `iddata_from_hardware` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `farm_id` varchar(45) NOT NULL,
  `temparature` varchar(45) NOT NULL,
  `moisture` varchar(45) NOT NULL,
  `on_date` varchar(45) NOT NULL,
  PRIMARY KEY (`iddata_from_hardware`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('74', 'f100', '31.80*C', 'Motor_ON', '2023-03-31');
INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('75', 'f100', '31.80*C', 'Motor_ON', '2023-03-31');
INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('76', 'f100', '31.80*C', 'Motor_ON', '2023-03-31');
INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('77', 'f100', '31.80*C', 'Motor_ON', '2023-03-31');
INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('78', 'f100', '31.80*C', 'Motor_ON', '2023-03-31');
INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('79', 'f100', '31.80*C', 'Motor_ON', '2023-03-31');
INSERT INTO `data_from_hardware` (`iddata_from_hardware`, `farm_id`, `temparature`, `moisture`, `on_date`) VALUES ('80', 'f100', '31.90*C', 'Motor_ON', '2023-03-31');


DROP TABLE IF EXISTS `disease_prediction`;
CREATE TABLE `disease_prediction` (
  `prediction_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) NOT NULL,
  `disease_name` varchar(255) NOT NULL,
  `confidence` varchar(20) NOT NULL,
  `prediction_date` date NOT NULL,
  PRIMARY KEY (`prediction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `disease_prediction` (`prediction_id`, `user_id`, `disease_name`, `confidence`, `prediction_date`) VALUES ('1', 'farmer1', 'Tomato Mosaic Virus (ToMV)', '90%', '2026-03-20');
INSERT INTO `disease_prediction` (`prediction_id`, `user_id`, `disease_name`, `confidence`, `prediction_date`) VALUES ('2', 'farmer1', 'Leaf Miner Damage', '95%', '2026-03-20');
INSERT INTO `disease_prediction` (`prediction_id`, `user_id`, `disease_name`, `confidence`, `prediction_date`) VALUES ('3', 'farmer1', 'Tomato Mosaic Virus (ToMV)', '90%', '2026-03-20');
INSERT INTO `disease_prediction` (`prediction_id`, `user_id`, `disease_name`, `confidence`, `prediction_date`) VALUES ('4', 'farmer1', 'Magnesium Deficiency', '95%', '2026-03-21');


DROP TABLE IF EXISTS `district`;
CREATE TABLE `district` (
  `iddistrict` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iddistrict`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `district` (`iddistrict`, `name`) VALUES ('1', '	Alappuzha');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('2', '	Ernakulam');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('3', '	Idukki');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('4', '	Kannur');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('5', '	Kasaragod');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('6', '	Kollam');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('7', '	Kottayam');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('8', '	Kozhikode');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('9', 'Malappuram');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('10', '	Palakkad');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('11', 'Pathanamthitta');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('12', 'Thiruvananthapuram');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('13', '	Thrissur');
INSERT INTO `district` (`iddistrict`, `name`) VALUES ('14', '	Wayanad');


DROP TABLE IF EXISTS `farmer_items`;
CREATE TABLE `farmer_items` (
  `farmer_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `total_price` varchar(50) DEFAULT NULL,
  `upload_date` varchar(50) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `branch_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`farmer_item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `feedback`;
CREATE TABLE `feedback` (
  `feedback_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `date_of_feedback` varchar(45) NOT NULL,
  `feedback_details` varchar(1045) NOT NULL,
  `reply` varchar(45) DEFAULT NULL,
  `reply_date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('1', 'farmer2', '2026-02-24', 'good', 'ok', '2026-02-24');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('5', 'farmer3', '2026-02-24', 'good ', 'thanks', '2026-02-24');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('6', 'farmer4', '2026-02-24', 'Very very good', 'Thanks:)', '2026-02-24');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('7', 'farmer5', '2026-02-24', 'good user experience', 'THANKS', '2026-02-24');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('8', 'farmer9', '2026-02-24', 'hi', 'ok', '2026-02-24');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('9', 'farmer9', '2026-02-24', 'hi', 'ok', '2026-02-25');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('10', 'farmer1', '2026-02-26', 'Good application', 'thanks', '2026-02-26');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('11', 'farmer1', '2026-02-26', 'good', 'thank you!', '2026-03-18');
INSERT INTO `feedback` (`feedback_id`, `user_id`, `date_of_feedback`, `feedback_details`, `reply`, `reply_date`) VALUES ('12', 'farmer1', '2026-03-04', 'great service', '', '');


DROP TABLE IF EXISTS `fertilizer`;
CREATE TABLE `fertilizer` (
  `fertilizer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `dosage` varchar(500) DEFAULT NULL,
  `purpose` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`fertilizer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `fertilizer` (`fertilizer_id`, `name`, `dosage`, `purpose`) VALUES ('1', 'Tnt', 'one litter', 'for crop growth ');
INSERT INTO `fertilizer` (`fertilizer_id`, `name`, `dosage`, `purpose`) VALUES ('2', 'Foly', '10 ml for 1 litter', 'for insects ');


DROP TABLE IF EXISTS `local_alerts`;
CREATE TABLE `local_alerts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `branch_id` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `local_alerts` (`id`, `branch_id`, `title`, `message`, `type`, `date`) VALUES ('1', 'krishi', 'Crops Now Available for Booking!', 'A wide range of crops are now available for booking.', 'Info', '2026-03-20');


DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `admin_id` varchar(20) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `login` (`admin_id`, `password`) VALUES ('admin', 'admin');


DROP TABLE IF EXISTS `market_prices`;
CREATE TABLE `market_prices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(100) NOT NULL,
  `category` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `date` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `market_prices` (`id`, `item_name`, `category`, `price`, `unit`, `date`) VALUES ('1', 'Cardamom', 'Crop', '1600', 'per kg', '2026-03-20');
INSERT INTO `market_prices` (`id`, `item_name`, `category`, `price`, `unit`, `date`) VALUES ('2', 'Floy', 'Fertilizer', '350', 'per Litre', '2026-03-20');


DROP TABLE IF EXISTS `purchase_history`;
CREATE TABLE `purchase_history` (
  `purchase history_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) DEFAULT NULL,
  `farmer_item_id` int(11) DEFAULT NULL,
  `purchase_date` varchar(50) DEFAULT NULL,
  `shipping_address` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`purchase history_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `queries`;
CREATE TABLE `queries` (
  `idqueries` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `user_query` varchar(45) NOT NULL,
  `reply` varchar(45) NOT NULL,
  `branch_id` varchar(45) NOT NULL,
  PRIMARY KEY (`idqueries`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('1', 'farmer2', 'is there any subsidy for buying cow', 'ok', 'krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('2', 'farmer3', 'Need info on soil testing', 'Available at branch', 'krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('3', 'farmer4', 'Will it rain tomorrow', 'yes', 'krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('4', 'farmer4', 'Temperature for tomorrow', '38 degree celsius', 'Krishibhavan Kannur');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('5', 'farmer8', 'any cattle subsidies', 'ok', 'Krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('6', 'farmer8', 'rain today', 'yes', 'Krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('7', 'farmer8', 'rain today', '', 'Krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('8', 'farmer8', 'rain today', 'yes', 'Krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('9', 'farmer5', 'any cattle feeds available', '', 'Krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('10', 'farmer7', 'Best way to cure greying of leaf', '', 'Krishi wayanad');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('11', 'farmer1', 'best coconut tree variety', 'sree rekha', 'krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('12', 'farmer1', 'how to book seeds', '', 'krishi');
INSERT INTO `queries` (`idqueries`, `user_id`, `user_query`, `reply`, `branch_id`) VALUES ('13', 'farmer1', 'fertilizer availability', '', 'krishi');


DROP TABLE IF EXISTS `request_subsidy`;
CREATE TABLE `request_subsidy` (
  `idrequest_subsidy` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) DEFAULT NULL,
  `request_date` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `idsubsidy` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `branch_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idrequest_subsidy`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('1', 'farmer2', '2026-02-24', 'subsidy', '3', 'approved', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('2', 'farmer3', '2026-02-24', 'cattle feed request', '3', 'approved', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('3', 'farmer4', '2026-02-24', '10 kg required', '3', 'approved', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('4', 'farmer4', '2026-02-24', 'is there any off for pottasium', '4', 'approved', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('5', 'farmer8', '2026-02-24', 'High quality Banana crops', '5', 'requested', 'Krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('6', 'farmer4', '2026-02-24', 'Am I eligible', '4', 'approved', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('7', 'farmer6', '2026-02-24', 'cattle feed', '3', 'requested', 'Krishibhavan Kannur');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('8', 'farmer5', '2026-02-24', 'cattle feed needed', '3', 'approved', 'Krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('9', 'farmer7', '2026-02-24', 'Want full details', '7', 'requested', 'Krishi wayanad');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('10', 'farmer9', '2026-02-24', 'hi', '3', 'requested', 'Krishi Bhavan Karuma');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('11', 'farmer3', '2026-02-24', 'cattle feed free', '3', 'approved', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('12', 'farmer1', '2026-02-26', 'hi', '4', 'requested', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('13', 'farmer1', '2026-02-27', 'please review', '3', 'rejected', 'krishi');
INSERT INTO `request_subsidy` (`idrequest_subsidy`, `user_id`, `request_date`, `description`, `idsubsidy`, `status`, `branch_id`) VALUES ('14', 'farmer1', '2026-03-02', 'please approve', '3', 'approved', 'Krishi');


DROP TABLE IF EXISTS `sensor_history`;
CREATE TABLE `sensor_history` (
  `idsensor_history` int(11) NOT NULL AUTO_INCREMENT,
  `motor_on_date` varchar(45) DEFAULT NULL,
  `temperature` varchar(45) DEFAULT NULL,
  `humidity` varchar(45) DEFAULT NULL,
  `moisture` varchar(45) DEFAULT NULL,
  `farm_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsensor_history`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `sensor_history` (`idsensor_history`, `motor_on_date`, `temperature`, `humidity`, `moisture`, `farm_id`) VALUES ('1', '2021-11-04', '35', '45', '20', '8');
INSERT INTO `sensor_history` (`idsensor_history`, `motor_on_date`, `temperature`, `humidity`, `moisture`, `farm_id`) VALUES ('2', '2023-03-15', '35', '45', '20', '8');
INSERT INTO `sensor_history` (`idsensor_history`, `motor_on_date`, `temperature`, `humidity`, `moisture`, `farm_id`) VALUES ('3', '2023-03-20', '35', '45', '20', '8');


DROP TABLE IF EXISTS `sensor_values`;
CREATE TABLE `sensor_values` (
  `idsensor_values` int(11) NOT NULL AUTO_INCREMENT,
  `farm_id` varchar(45) DEFAULT NULL,
  `current_date` varchar(45) DEFAULT NULL,
  `moisture` varchar(45) DEFAULT NULL,
  `temperature` varchar(45) DEFAULT NULL,
  `humidity` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsensor_values`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `sensor_values` (`idsensor_values`, `farm_id`, `current_date`, `moisture`, `temperature`, `humidity`) VALUES ('1', '8', '2023-03-20', '25', '22', '25');
INSERT INTO `sensor_values` (`idsensor_values`, `farm_id`, `current_date`, `moisture`, `temperature`, `humidity`) VALUES ('2', '9', '2023-03-28', '21', '21', '21');


DROP TABLE IF EXISTS `subsidy`;
CREATE TABLE `subsidy` (
  `idsubsidy` int(11) NOT NULL AUTO_INCREMENT,
  `current_date` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsubsidy`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `subsidy` (`idsubsidy`, `current_date`, `description`) VALUES ('3', '2026-02-24', 'Cattle Feed Free');
INSERT INTO `subsidy` (`idsubsidy`, `current_date`, `description`) VALUES ('4', '2026-02-24', 'fertilizer 50% off');
INSERT INTO `subsidy` (`idsubsidy`, `current_date`, `description`) VALUES ('6', '2026-02-24', 'Agricultural Equipment Subsidy');
INSERT INTO `subsidy` (`idsubsidy`, `current_date`, `description`) VALUES ('7', '2026-02-24', 'Agricultural Infrastructure Subsidy');


DROP TABLE IF EXISTS `subsidy_request`;
CREATE TABLE `subsidy_request` (
  `idsubsidy_request` int(11) NOT NULL,
  `user_id` varchar(45) DEFAULT NULL,
  `request_date` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `idsubsidy` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsubsidy_request`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

DROP TABLE IF EXISTS `user_farms`;
CREATE TABLE `user_farms` (
  `farm_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `date_of_register` varchar(45) NOT NULL,
  `farm_address` varchar(450) NOT NULL,
  `farm_details` varchar(450) NOT NULL,
  `farm_image` varchar(450) NOT NULL,
  `branch_id` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`farm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `user_farms` (`farm_id`, `user_id`, `date_of_register`, `farm_address`, `farm_details`, `farm_image`, `branch_id`, `status`) VALUES ('8', 'farmer3', '2023-03-02', 'Sample Farm 1', 'Poultry Farm', 'coc1.jpg', NULL, 'Approved');
INSERT INTO `user_farms` (`farm_id`, `user_id`, `date_of_register`, `farm_address`, `farm_details`, `farm_image`, `branch_id`, `status`) VALUES ('9', 'farmer10', '2023-03-03', 'Sample Farm 2', 'agri farm', 'coc1.jpg', 'krishi', 'Approved');
INSERT INTO `user_farms` (`farm_id`, `user_id`, `date_of_register`, `farm_address`, `farm_details`, `farm_image`, `branch_id`, `status`) VALUES ('10', 'farmer4', '2023-03-10', 'Sample Spice Farm', 'Coffee, cardamom, pepper and other spices.', 'coc.jpg', 'Krishibhavan Kannur', 'Approved');
INSERT INTO `user_farms` (`farm_id`, `user_id`, `date_of_register`, `farm_address`, `farm_details`, `farm_image`, `branch_id`, `status`) VALUES ('11', 'farmer7', '2023-03-14', 'Sample Orchid Farm', 'Orchid plants and flowers.', 'coc1.jpg', 'Krishi wayanad', 'Approved');
INSERT INTO `user_farms` (`farm_id`, `user_id`, `date_of_register`, `farm_address`, `farm_details`, `farm_image`, `branch_id`, `status`) VALUES ('12', 'farmer3', '2023-04-04', 'Sample Coconut Farm', 'coconut tree farm ', 'coc.jpg', NULL, 'Approved');
INSERT INTO `user_farms` (`farm_id`, `user_id`, `date_of_register`, `farm_address`, `farm_details`, `farm_image`, `branch_id`, `status`) VALUES ('18', 'farmer1', '2026-03-21', 'Sample Dairy Farm', 'Cow Farm', 'ai-generated-group-of-cows-at-cowshed-eating-hay-or-fodder-on-dairy-farm-photo.jpg', 'Krishi', 'Pending');


DROP TABLE IF EXISTS `user_register`;
CREATE TABLE `user_register` (
  `user_id` varchar(20) NOT NULL,
  `name` varchar(45) NOT NULL,
  `address` varchar(450) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(45) NOT NULL,
  `branch_id` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer1', 'Demo Farmer 1', 'Sample Address 1, Kerala', '9000000101', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer2', 'Demo Farmer 2', 'Sample Address 2, Kerala', '9000000102', 'demo1234', 'krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer3', 'Demo Farmer 3', 'Sample Address 3, Kerala', '9000000103', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer4', 'Demo Farmer 4', 'Sample Address 4, Kerala', '9000000104', 'demo1234', 'Krishibhavan Kannur');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer5', 'Demo Farmer 5', 'Sample Address 5, Kerala', '9000000105', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer6', 'Demo Farmer 6', 'Sample Address 6, Kerala', '9000000106', 'demo1234', 'Krishibhavan Kannur');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer7', 'Demo Farmer 7', 'Sample Address 7, Kerala', '9000000107', 'demo1234', 'Krishi wayanad');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer8', 'Demo Farmer 8', 'Sample Address 8, Kerala', '9000000108', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer9', 'Demo Farmer 9', 'Sample Address 9, Kerala', '9000000109', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer10', 'Demo Farmer 10', 'Sample Address 10, Kerala', '9000000110', 'demo1234', 'krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer11', 'Demo Farmer 11', 'Sample Address 11, Kerala', '9000000111', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer12', 'Demo Farmer 12', 'Sample Address 12, Kerala', '9000000112', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer13', 'Demo Farmer 13', 'Sample Address 13, Kerala', '9000000113', 'demo1234', 'Krishi');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer14', 'Demo Farmer 14', 'Sample Address 14, Kerala', '9000000114', 'demo1234', 'Krishi Bhavan Karuma');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer15', 'Demo Farmer 15', 'Sample Address 15, Kerala', '9000000115', 'demo1234', 'Krishi Bhavan Karuma');
INSERT INTO `user_register` (`user_id`, `name`, `address`, `phone`, `password`, `branch_id`) VALUES ('farmer16', 'Demo Farmer 16', 'Sample Address 16, Kerala', '9000000116', 'demo1234', 'Krishi Bhavan Karuma');


