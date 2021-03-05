-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: HDYFT
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `colors`
--

DROP TABLE IF EXISTS `colors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colors` (
  `color_name` varchar(255) NOT NULL,
  `hex_value` varchar(255) NOT NULL,
  PRIMARY KEY (`color_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colors`
--

LOCK TABLES `colors` WRITE;
/*!40000 ALTER TABLE `colors` DISABLE KEYS */;
INSERT INTO `colors` VALUES ('BLUE1','#0000FF'),('BLUE2','#5900FF'),('BLUE3','#8576FF'),('BROWN1','#964B00'),('BROWN2','#784B00'),('BROWN3','#5E4B00'),('GREEN1','#00FF00'),('GREEN2','#00A900'),('GREEN3','#A6A900'),('ORANGE1','#FF7F00'),('ORANGE2','#CB7200'),('ORANGE3','#A67200'),('PURPLE1','#800080'),('PURPLE2','#8000C7'),('PURPLE3','#80005A'),('RED1','#FF0000'),('RED2','#BA0000'),('RED3','#770000'),('YELLOW1','#F0F000'),('YELLOW2','#FFC900'),('YELLOW3','#FFB100');
/*!40000 ALTER TABLE `colors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emotion_color`
--

DROP TABLE IF EXISTS `emotion_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emotion_color` (
  `emotion_name` varchar(255) NOT NULL,
  `nth_color` int NOT NULL,
  `color_name` varchar(255) NOT NULL,
  PRIMARY KEY (`emotion_name`,`nth_color`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emotion_color`
--

LOCK TABLES `emotion_color` WRITE;
/*!40000 ALTER TABLE `emotion_color` DISABLE KEYS */;
INSERT INTO `emotion_color` VALUES ('ANGRY',1,'RED1'),('ANGRY',2,'RED2'),('ANGRY',3,'RED3'),('DISGUST',1,'BROWN1'),('DISGUST',2,'BROWN2'),('DISGUST',3,'BROWN3'),('HAPPY',1,'YELLOW1'),('HAPPY',2,'YELLOW2'),('HAPPY',3,'YELLOW3'),('NEUTRAL',1,'GREEN1'),('NEUTRAL',2,'GREEN2'),('NEUTRAL',3,'GREEN3'),('SAD',1,'BLUE1'),('SAD',2,'BLUE2'),('SAD',3,'BLUE3'),('SCARED',1,'PURPLE1'),('SCARED',2,'PURPLE2'),('SCARED',3,'PURPLE3'),('SURPRISED',1,'ORANGE1'),('SURPRISED',2,'ORANGE2'),('SURPRISED',3,'ORANGE3');
/*!40000 ALTER TABLE `emotion_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emotions`
--

DROP TABLE IF EXISTS `emotions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emotions` (
  `id` int NOT NULL,
  `emotion_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emotions`
--

LOCK TABLES `emotions` WRITE;
/*!40000 ALTER TABLE `emotions` DISABLE KEYS */;
INSERT INTO `emotions` VALUES (1,'HAPPY'),(2,'SURPRISED'),(3,'NEUTRAL'),(4,'DISGUST'),(5,'SAD'),(6,'SCARED'),(7,'ANGRY');
/*!40000 ALTER TABLE `emotions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-19 12:01:36
