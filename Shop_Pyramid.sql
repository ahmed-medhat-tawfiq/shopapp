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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `month`
--

LOCK TABLES `month` WRITE;
/*!40000 ALTER TABLE `month` DISABLE KEYS */;
INSERT INTO `month` VALUES (4,0,0,0,0,0,'2016-03-11 01:10:39','2016-03-11 13:10:39',0,0,0,0,0,'2016-03-11','2016-04-10',1,6),(5,0,0,0,0,0,'2016-03-11 02:55:43','2016-03-11 14:55:43',0,0,0,0,0,'2016-03-11','2016-04-10',1,7),(6,0,0,0,0,0,'2016-03-11 02:55:43','2016-03-11 14:55:43',0,0,0,0,0,'2016-03-11','2016-04-10',0,7),(7,0,0,0,0,0,'2016-03-11 02:55:43','2016-03-11 14:55:43',0,0,0,0,0,'2016-03-11','2016-04-10',1,6),(8,0,0,0,0,0,'2016-03-11 02:55:43','2016-03-11 14:55:43',0,0,0,0,0,'2016-03-11','2016-04-10',1,5),(9,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,8),(10,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',0,8),(11,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,6),(12,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,5),(13,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,6),(14,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,5),(15,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,6),(16,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,5),(17,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,6),(18,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',1,5),(19,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',0,6),(20,0,0,0,0,0,'2016-03-11 18:36:13','2016-03-12 06:36:13',0,0,0,0,0,'2016-03-11','2016-04-10',0,5);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone`
--

LOCK TABLES `phone` WRITE;
/*!40000 ALTER TABLE `phone` DISABLE KEYS */;
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
  UNIQUE KEY `latitude` (`latitude`),
  UNIQUE KEY `longitude` (`longitude`),
  KEY `user` (`user`),
  CONSTRAINT `shops_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shops`
--

LOCK TABLES `shops` WRITE;
/*!40000 ALTER TABLE `shops` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Ahmed','Medhat','admin','admin','medhat1471993@gmail.com',NULL,'egypt',NULL,NULL,0,'none','x',0,0,0,'2016-03-09','04:15:36'),(2,'ezat','mazen','hopa93','a8888','not exist','uu','uu','18292829','989898',0,'none','n',0,0,0,'2016-03-09','04:15:39'),(5,'a','a',NULL,'1','1@',NULL,NULL,'1',NULL,0,'none','a',0,0,0,'2016-03-10','22:29:24'),(6,'s1','s1','','1','s1','','','s1','',0,'none','s',0,5,0,'2016-03-10','22:29:24'),(7,'Raouf','b','b','b','b@','b','b','b','b',0,'none','b',0,0,0,'2016-03-11','01:10:39'),(8,'a1','s',NULL,'a','a@',NULL,NULL,'s',NULL,0,'none','a',0,0,0,'2016-03-11','01:10:39'),(9,'cu','cu',NULL,NULL,'a@a','herr',NULL,'0111',NULL,0,'none','o',6,0,0,'2016-03-11','02:55:43'),(10,'ahmed','sayed',NULL,'1','12',NULL,NULL,NULL,NULL,0,'none','n',0,0,0,'2016-03-11','18:36:12'),(11,'u','u',NULL,'u','u',NULL,NULL,'u',NULL,0,'none','s',0,0,1,'2016-03-11','18:36:12');
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

-- Dump completed on 2016-03-12  0:41:25
