-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Shop_Pyramid
-- ------------------------------------------------------
-- Server version	5.5.47-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `code`
--

DROP TABLE IF EXISTS `code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `code` (
  `code_id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `period` int(11) DEFAULT NULL,
  `answer_image` varchar(100) DEFAULT NULL,
  `used` tinyint(1) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  PRIMARY KEY (`code_id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `code`
--

LOCK TABLES `code` WRITE;
/*!40000 ALTER TABLE `code` DISABLE KEYS */;
/*!40000 ALTER TABLE `code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `star` int(11) NOT NULL,
  `period` int(11) DEFAULT NULL,
  `used` tinyint(1) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `month`
--

DROP TABLE IF EXISTS `month`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `month` (
  `month_id` int(11) NOT NULL AUTO_INCREMENT,
  `t_purse` float DEFAULT NULL,
  `t_customer` int(11) DEFAULT NULL,
  `t_pcustomer` int(11) DEFAULT NULL,
  `t_vcustomer` int(11) DEFAULT NULL,
  `t_time` int(11) DEFAULT NULL,
  `t_sdate` datetime DEFAULT NULL,
  `t_edate` datetime DEFAULT NULL,
  `m_purse` float DEFAULT NULL,
  `m_customer` int(11) DEFAULT NULL,
  `m_pcustomer` int(11) DEFAULT NULL,
  `m_vcustomer` int(11) DEFAULT NULL,
  `m_time` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `old` tinyint(1) DEFAULT NULL,
  `user` int(11) NOT NULL,
  PRIMARY KEY (`month_id`),
  KEY `user` (`user`),
  CONSTRAINT `month_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `month`
--

LOCK TABLES `month` WRITE;
/*!40000 ALTER TABLE `month` DISABLE KEYS */;
INSERT INTO `month` VALUES (3,340,5,5,0,0,'2016-03-15 02:06:44','2016-03-15 14:06:44',340,11,10,2,19,'2016-03-14','2016-04-13',0,5),(4,480,12,11,2,0,'2016-03-14 06:21:58','2016-03-14 18:21:58',480,14,13,3,0,'2016-03-14','2016-04-13',0,2),(5,20,1,1,0,0,'2016-03-15 02:23:40','2016-03-15 14:23:40',140,3,3,1,0,'2016-03-14','2016-04-13',0,4),(6,70,2,2,1,1,'2016-03-15 00:58:29','2016-03-15 12:58:29',70,2,2,1,0,'2016-03-14','2016-04-13',0,6),(7,210,6,5,2,0,'2016-03-14 06:21:58','2016-03-14 18:21:58',210,6,5,2,0,'2016-03-14','2016-04-13',0,3),(8,140,4,3,1,1,'2016-03-15 01:06:51','2016-03-15 13:06:51',140,4,3,1,0,'2016-03-14','2016-04-13',0,7),(9,0,0,0,0,0,'2016-03-15 16:06:14','2016-03-16 04:06:14',0,0,0,0,0,'2016-03-15','2016-04-14',1,24),(10,0,0,0,0,0,'2016-03-15 16:06:14','2016-03-16 04:06:14',0,0,0,0,0,'2016-03-15','2016-04-14',1,23),(11,80,5,4,0,0,'2016-03-15 22:43:12','2016-03-16 10:43:12',80,5,4,0,0,'2016-03-15','2016-04-14',0,24),(12,80,5,4,0,0,'2016-03-15 16:06:14','2016-03-16 04:06:14',80,5,4,0,0,'2016-03-15','2016-04-14',0,23);
/*!40000 ALTER TABLE `month` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone`
--

DROP TABLE IF EXISTS `phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phone` (
  `phone_id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `Primary` tinyint(1) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  `shop` int(11) NOT NULL,
  PRIMARY KEY (`phone_id`),
  UNIQUE KEY `number` (`number`),
  KEY `shop` (`shop`),
  CONSTRAINT `phone_ibfk_1` FOREIGN KEY (`shop`) REFERENCES `shops` (`shop_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone`
--

LOCK TABLES `phone` WRITE;
/*!40000 ALTER TABLE `phone` DISABLE KEYS */;
INSERT INTO `phone` VALUES (1,'6611',0,'2016-03-14','06:21:58',1),(2,'6622',0,'2016-03-14','06:21:58',1),(3,'7711',0,'2016-03-14','06:21:58',2),(4,'7722',0,'2016-03-14','06:21:58',2),(7,'8822',0,'2016-03-14','07:09:42',4),(8,'8811',0,'2016-03-14','07:09:42',4),(9,'9911',0,'2016-03-14','07:09:42',5),(10,'9922',0,'2016-03-14','07:09:42',5),(11,'9933',0,'2016-03-14','07:09:42',6),(12,'9944',0,'2016-03-14','07:09:42',6),(13,'11111',0,'2016-03-15','00:40:45',7),(14,'11122',0,'2016-03-15','00:40:45',7),(15,'11133',0,'2016-03-15','00:40:45',7),(16,'11155',0,'2016-03-15','00:40:45',8),(17,'11144',0,'2016-03-15','00:40:45',8),(18,'11166',0,'2016-03-15','00:40:45',8),(19,'33322',0,'2016-03-15','00:40:45',9),(20,'33333',0,'2016-03-15','00:40:45',9),(21,'33311',0,'2016-03-15','00:40:45',9),(22,'44411',0,'2016-03-15','00:40:45',10),(23,'44422',0,'2016-03-15','00:40:45',10),(24,'44433',0,'2016-03-15','00:40:45',10),(25,'55533',0,'2016-03-15','01:55:20',11),(26,'55511',0,'2016-03-15','01:55:20',11),(27,'55522',0,'2016-03-15','01:55:20',11),(37,'55544',0,'2016-03-15','02:16:19',19),(38,'555344',0,'2016-03-15','02:16:19',20),(39,'555334',0,'2016-03-15','02:16:19',21);
/*!40000 ALTER TABLE `phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shops`
--

DROP TABLE IF EXISTS `shops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shops` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `ads` text,
  `rank` int(11) DEFAULT NULL,
  `latitude` decimal(10,0) NOT NULL,
  `longitude` decimal(10,0) NOT NULL,
  `types` varchar(255) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  `user` int(11) NOT NULL,
  PRIMARY KEY (`shop_id`),
  KEY `user` (`user`),
  CONSTRAINT `shops_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shops`
--

LOCK TABLES `shops` WRITE;
/*!40000 ALTER TABLE `shops` DISABLE KEYS */;
INSERT INTO `shops` VALUES (1,'shop1','pharmacy',NULL,NULL,NULL,12,12,'normal','2016-03-14','2016-04-13','2016-03-14','06:21:58',8),(2,'shop2','food',NULL,NULL,NULL,12,12,'special','2016-03-14','2016-05-13','2016-03-14','06:21:58',9),(4,'shop3','food',NULL,NULL,NULL,12,12,'no','2016-03-14','2016-03-14','2016-03-14','07:09:42',11),(5,'shop4','pharmacy',NULL,NULL,NULL,12,12,'special','2016-03-14','2016-04-13','2016-03-14','07:09:42',12),(6,'shop4','pharmacy',NULL,NULL,NULL,13,13,'special','2016-03-14','2016-04-13','2016-03-14','07:09:42',12),(7,'marawan','mobile shop','hadaek',NULL,NULL,12,12,'normal','2016-03-15','2016-04-14','2016-03-15','00:40:45',13),(8,'behery','mobile shop','hadaek',NULL,NULL,12,12,'special','2016-03-15','2016-04-14','2016-03-15','00:40:45',14),(9,'abo rabe3','food','hadaek',NULL,NULL,12,12,'special','2016-03-15','2016-05-14','2016-03-15','00:40:45',15),(10,'costa','food','naser city',NULL,NULL,13,12,'no','2016-03-15','2016-03-15','2016-03-15','00:40:45',16),(11,'costa2','food','naser city',NULL,NULL,13,12,'normal','2016-03-15','2016-04-14','2016-03-15','01:55:20',17),(19,'costa3','food','naser city',NULL,NULL,13,12,'normal','2016-03-15','2016-04-14','2016-03-15','02:16:19',17),(20,'costa4','food','naser city',NULL,NULL,13,12,'normal','2016-03-15','2016-04-14','2016-03-15','02:16:19',17),(21,'roka','food','naser city',NULL,NULL,13,12,'normal','2016-03-15','2016-04-14','2016-03-15','02:16:19',17);
/*!40000 ALTER TABLE `shops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `phone1` varchar(255) DEFAULT NULL,
  `phone2` varchar(255) DEFAULT NULL,
  `shop_no` int(11) DEFAULT NULL,
  `avatar` text,
  `groups` varchar(255) DEFAULT NULL,
  `sales_id` int(11) DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL,
  `block` tinyint(1) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone1` (`phone1`),
  UNIQUE KEY `phone2` (`phone2`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Ahmed','Medhat','admin','admin','medhat1471993@gmail.com','hadaek al kuba','egypt','01158668048','01019572326',0,'none','b',0,0,0,'2016-03-14','05:38:59'),(2,'admin1','a','admin1','123','admin1@gmail.com','abaseya','egypt','0000','13131313',0,'none','a',0,0,0,'2016-03-14','05:45:10'),(3,'admin2','a','admin2','123','admin2@gmail.com','abdo basha','egypt','1111','7y96969',0,'none','a',0,0,0,'2016-03-14','05:45:10'),(4,'sale1','s','sale1','123','sale1@gmail.com','','','2222','9y9yy',0,'none','s',0,2,0,'2016-03-14','05:45:10'),(5,'sale2','s',NULL,'123','sale2@gmail.com',NULL,NULL,'3333',NULL,0,'none','s',0,2,0,'2016-03-14','05:45:10'),(6,'sale3','s',NULL,'123','sale3@gmail.com',NULL,NULL,'4444',NULL,0,'none','s',0,3,0,'2016-03-14','05:45:10'),(7,'sale4','s',NULL,'123','sale4@gmail.com',NULL,NULL,'5555',NULL,0,'none','s',0,3,0,'2016-03-14','05:45:10'),(8,'customer1','c',NULL,NULL,'customer1@gmail.com',NULL,NULL,'6666',NULL,1,'none','o',4,0,0,'2016-03-14','06:21:58'),(9,'customer2','c',NULL,NULL,'customer2@gmail.com',NULL,NULL,'7777',NULL,1,'none','o',4,0,0,'2016-03-14','06:21:58'),(11,'customer3','c',NULL,NULL,'customer3@gmail.com',NULL,NULL,'8888',NULL,2,'none','o',5,0,0,'2016-03-14','06:21:58'),(12,'customer4','c',NULL,NULL,'customer4@gmail.com',NULL,NULL,'9999',NULL,2,'none','o',5,0,0,'2016-03-14','06:21:58'),(13,'customer5','c',NULL,NULL,'customer5@gmail.com',NULL,NULL,'11111',NULL,2,'none','o',6,0,0,'2016-03-15','00:40:45'),(14,'customer6','c',NULL,NULL,'customer6@gmail.com',NULL,NULL,'22222',NULL,1,'none','o',6,0,0,'2016-03-15','00:40:45'),(15,'customer7','c',NULL,NULL,'customer7@gmail.com',NULL,NULL,'33333',NULL,1,'none','o',7,0,0,'2016-03-15','00:40:45'),(16,'customer8','c',NULL,NULL,'customer8@gmail.com',NULL,NULL,'44444',NULL,1,'none','o',7,0,0,'2016-03-15','00:40:45'),(17,'customer9','c',NULL,NULL,'customer9@gmail.com',NULL,NULL,'55555',NULL,11,'none','o',5,0,0,'2016-03-15','01:55:20'),(18,'y','y','1','111','1',NULL,NULL,NULL,NULL,0,'none','n',0,0,0,'2016-03-15','16:06:13'),(19,'Huth','Sam','01121s','1','n@n.com',NULL,NULL,NULL,NULL,0,'none','n',0,0,0,'2016-03-15','16:06:13'),(23,'ad','ad',NULL,'1','ad@a.com',NULL,NULL,'ad',NULL,0,'none','a',0,0,0,'2016-03-15','16:06:13'),(24,'sa','sa',NULL,'1','sa@s.com',NULL,NULL,'sa',NULL,0,'none','s',0,23,0,'2016-03-15','16:06:13'),(25,'c1','c1',NULL,NULL,'c1@c.com','madina',NULL,'c1',NULL,21,'none','o',24,0,0,'2016-03-15','16:06:13');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-16  0:40:06
