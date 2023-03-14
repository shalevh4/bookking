-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: group23
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_number` int NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `author_name` varchar(255) NOT NULL,
  `year_published` int NOT NULL,
  `publisher` varchar(255) NOT NULL,
  PRIMARY KEY (`book_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'The Fellowship of the Ring','J.R.R. Tolkien',1954,'George Allen & Unwin'),(2,'The Two Towers','J.R.R. Tolkien',1954,'George Allen & Unwin'),(3,'The Return of the King','J.R.R. Tolkien',1955,'George Allen & Unwin'),(4,'1984','George Orwell',1949,'Secker & Warburg'),(5,'Brave New World','Aldous Huxley',1932,'Chatto & Windus'),(6,'To Kill a Mockingbird','Harper Lee',1960,'J.B. Lippincott & Co.'),(7,'The Great Gatsby','F. Scott Fitzgerald',1925,'Charles Scribner\'s Sons'),(8,'Moby-Dick','Herman Melville',1851,'Richard Bentley'),(9,'Pride & Prejudice','Jane Austen',1813,'Thomas Egerton'),(10,'Jane Eyre','Charlotte Bronte',1847,'Smith, Elder & Co.'),(11,'The Catcher in the Rye','J.D. Salinger',1951,'Little, Brown & Company'),(12,'The Book Thief','Markus Zusak',2005,'Knopf Books for Young Readers'),(13,'The Hunger Games','Suzanne Collins',2008,'Scholastic Press'),(14,'The Shining','Stephen King',1977,'Doubleday'),(15,'The Picture of Dorian Gray','Oscar Wilde',1890,'Ward, Lock & Co.'),(16,'The Alchemist','Paulo Coelho',1988,'Rocco'),(17,'Harry Potter & the Sorcerer\'s Stone','J.K. Rowling',1997,'Bloomsbury'),(18,'The Lord of the Rings','J.R.R. Tolkien',1954,'George Allen & Unwin'),(19,'The Da Vinci Code','Dan Brown',2003,'Doubleday'),(20,'One Hundred Years of Solitude','Gabriel Garcia Marquez',1967,'Harper & Row'),(21,'The Chronicles of Narnia: The Lion, the Witch & the Wardrobe','C.S. Lewis',1950,'Geoffrey Bles'),(22,'The Giver','Lois Lowry',1993,'Houghton Mifflin Harcourt'),(23,'The Handmaid\'s Tale','Margaret Atwood',1985,'McClelland & Stewart'),(24,'Ender\'s Game','Orson Scott Card',1985,'Tor Books'),(25,'The Dark Tower Series','Stephen King',1982,'Grant'),(26,'test','test and testor',2023,'testing'),(27,'ziv & fried','ziv',1998,'someone'),(28,'Bibi','Benjamin Netanyahu',2023,'ISRAEL TODAY'),(29,'Bibi','Yair lapid',2023,'Yesh Atid'),(30,'Bibi','Beni Genz',2021,'Blue And White'),(31,'HAPOAL OLA','ziv',2022,'ADOM ADOM'),(32,'trying','tryor',1990,'traior'),(33,'Mama Mia','Mimi Mama',1995,'Mommy'),(90,'try','tryor',1990,'trying');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_in_branch`
--

DROP TABLE IF EXISTS `books_in_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_in_branch` (
  `amount_in_stock` int NOT NULL,
  `amount_available` int NOT NULL,
  `book_number` int NOT NULL,
  `branch_number` varchar(45) NOT NULL,
  PRIMARY KEY (`book_number`,`branch_number`),
  KEY `Branch_number` (`branch_number`),
  CONSTRAINT `books_in_branch_ibfk_1` FOREIGN KEY (`book_number`) REFERENCES `book` (`book_number`),
  CONSTRAINT `books_in_branch_ibfk_2` FOREIGN KEY (`branch_number`) REFERENCES `branch` (`branch_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_in_branch`
--

LOCK TABLES `books_in_branch` WRITE;
/*!40000 ALTER TABLE `books_in_branch` DISABLE KEYS */;
INSERT INTO `books_in_branch` VALUES (1,1,1,'1'),(3,3,1,'2'),(2,0,1,'5'),(1,0,2,'1'),(2,2,2,'2'),(1,0,2,'3'),(2,0,2,'5'),(1,0,3,'1'),(2,1,3,'3'),(1,1,4,'1'),(1,1,4,'4'),(1,0,4,'5'),(1,0,5,'1'),(4,4,5,'2'),(1,0,5,'4'),(1,0,5,'5'),(1,1,6,'1'),(1,2,6,'4'),(2,2,7,'1'),(1,0,7,'3'),(1,0,7,'5'),(1,0,8,'5'),(1,0,10,'1'),(2,1,10,'2'),(1,0,10,'5'),(1,1,11,'1'),(1,1,11,'4'),(1,0,11,'5'),(1,1,12,'3'),(1,1,13,'1'),(1,1,13,'2'),(3,2,13,'5'),(1,1,15,'1'),(3,1,15,'5'),(2,2,16,'1'),(1,0,16,'5'),(2,1,17,'5'),(1,0,18,'1'),(1,1,19,'1'),(1,1,19,'2'),(1,1,19,'4'),(1,0,19,'5'),(2,0,20,'1'),(1,1,20,'3'),(1,1,20,'5'),(1,1,21,'5'),(1,1,22,'1'),(1,1,23,'1'),(1,1,23,'5'),(1,1,24,'1'),(1,1,25,'5'),(1,1,26,'1'),(1,0,26,'5'),(1,1,27,'5'),(2,1,28,'1'),(1,0,29,'1'),(1,0,29,'5'),(1,1,30,'5'),(1,0,31,'4'),(1,1,32,'2'),(2,1,33,'2'),(1,0,90,'2');
/*!40000 ALTER TABLE `books_in_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrow`
--

DROP TABLE IF EXISTS `borrow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow` (
  `borrow_date` date NOT NULL,
  `return_date` date NOT NULL,
  `copy_number` int NOT NULL,
  `customer_email` varchar(45) NOT NULL,
  `extension_date` date DEFAULT NULL,
  PRIMARY KEY (`borrow_date`,`copy_number`,`customer_email`),
  KEY `Copy_number` (`copy_number`),
  KEY `Customer_Email_` (`customer_email`),
  CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`copy_number`) REFERENCES `copy` (`copy_number`),
  CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow`
--

LOCK TABLES `borrow` WRITE;
/*!40000 ALTER TABLE `borrow` DISABLE KEYS */;
INSERT INTO `borrow` VALUES ('2020-01-09','2020-01-23',50,'tal@walla.com',NULL),('2020-01-25','2020-02-09',50,'roni@yahoo.com',NULL),('2020-07-13','2020-07-27',51,'yotam@gmail.com',NULL),('2020-07-28','2020-08-11',51,'yair@yahoo.com',NULL),('2021-01-09','2021-01-14',14,'dudi@gmail.com',NULL),('2021-01-14','2021-01-28',14,'yair@yahoo.com',NULL),('2021-03-01','2021-03-15',72,'ziv@a.com',NULL),('2021-03-17','2021-03-31',72,'ziv@b.com',NULL),('2021-04-01','2021-04-15',66,'yotam@gmail.com',NULL),('2021-04-16','2021-04-30',66,'yossi@gmail.com',NULL),('2021-06-12','2021-06-26',67,'ziv@a.com',NULL),('2021-06-28','2021-07-12',67,'ziv@b.com',NULL),('2021-07-13','2021-07-27',48,'yotam@gmail.com',NULL),('2022-01-15','2022-01-29',18,'shalevh88@gmail.com',NULL),('2022-01-30','2022-02-11',18,'moshe@walla.com',NULL),('2022-11-05','2022-11-26',21,'tal@walla.com','2022-11-17'),('2023-01-05','2023-01-13',38,'moshe@walla.com','2023-01-12'),('2023-01-09','2023-01-11',15,'sara@gmail.com',NULL),('2023-01-11','2023-02-07',70,'ziv@b.com','2023-01-17'),('2023-01-12','2023-01-26',13,'dana@yahoo.com',NULL),('2023-01-12','2023-01-17',15,'dana@yahoo.com',NULL),('2023-01-12','2023-01-26',17,'yair@yahoo.com',NULL),('2023-01-12','2023-01-22',19,'dudi@gmail.com',NULL),('2023-01-12','2023-01-26',22,'moshe@walla.com',NULL),('2023-01-12','2023-01-26',25,'roni@yahoo.com',NULL),('2023-01-12','2023-01-17',35,'roni@yahoo.com',NULL),('2023-01-13','2023-01-27',20,'dudi@gmail.com',NULL),('2023-01-13','2023-01-27',23,'yotam@gmail.com',NULL),('2023-01-13','2023-01-27',24,'tal@walla.com',NULL),('2023-01-13','2023-01-27',30,'tal@walla.com',NULL),('2023-01-13','2023-01-27',49,'yair@yahoo.com',NULL),('2023-01-15','2023-01-29',14,'dudi@gmail.com',NULL),('2023-01-15','2023-01-29',29,'shalevh88@gmail.com',NULL),('2023-01-15','2023-02-07',39,'naama@gmail.com','2023-01-17'),('2023-01-15','2023-01-29',63,'shalevh88@gmail.com',NULL),('2023-01-15','2023-01-29',64,'moshe@walla.com',NULL),('2023-01-16','2023-01-30',16,'ziv@a.com',NULL),('2023-01-16','2023-01-30',21,'naama@gmail.com',NULL),('2023-01-16','2023-01-30',34,'ziv@a.com',NULL),('2023-01-16','2023-01-30',37,'ziv@b.com',NULL),('2023-01-16','2023-02-06',40,'adi@walla.com','2023-01-17'),('2023-01-16','2023-01-30',46,'yotam@gmail.com',NULL),('2023-01-16','2023-02-06',48,'ziv@a.com','2023-01-16'),('2023-01-16','2023-01-30',61,'shlomi@walla.com',NULL),('2023-01-16','2023-01-30',66,'sara@gmail.com',NULL),('2023-01-16','2023-02-06',68,'gali@gmail.com','2023-01-17'),('2023-01-16','2023-02-06',76,'shlomi@walla.com','2023-01-17'),('2023-01-16','2023-02-06',85,'adi@walla.com','2023-01-17'),('2023-01-16','2023-02-06',94,'gali@gmail.com','2023-01-17'),('2023-01-17','2023-01-31',31,'naama@gmail.com',NULL),('2023-01-17','2023-01-31',56,'shlomi@walla.com',NULL),('2023-01-17','2023-02-06',71,'ziv@b.com','2023-01-17');
/*!40000 ALTER TABLE `borrow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `branch_number` varchar(45) NOT NULL,
  `branch_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `street` varchar(45) NOT NULL,
  `house_number` int NOT NULL,
  PRIMARY KEY (`branch_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES ('1','Tel Aviv Tchernichovsky','036792309','Tel Aviv','Shaul Tchernichovsky',3),('2','Jerusalem Agnon','026504930','Jerusalem','Shmuel Yosef Agnon',22),('3','Haifa Bialik','048905600','Haifa','Haim Nahman Bialik',16),('4','Beer Sheva Shazar ','075234590','Beer Sheva','Shazar',13),('5','Eilat HaTmarim','076201010','Eilat','HaTmarim',9);
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `copy`
--

DROP TABLE IF EXISTS `copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `copy` (
  `copy_number` int NOT NULL AUTO_INCREMENT,
  `current_status` enum('borrowed','ordered','available') NOT NULL,
  `book_number` int NOT NULL,
  `branch_number` varchar(45) NOT NULL,
  PRIMARY KEY (`copy_number`),
  KEY `Book_number` (`book_number`),
  KEY `Branch_number` (`branch_number`),
  CONSTRAINT `copy_ibfk_1` FOREIGN KEY (`book_number`) REFERENCES `book` (`book_number`),
  CONSTRAINT `copy_ibfk_2` FOREIGN KEY (`branch_number`) REFERENCES `branch` (`branch_number`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copy`
--

LOCK TABLES `copy` WRITE;
/*!40000 ALTER TABLE `copy` DISABLE KEYS */;
INSERT INTO `copy` VALUES (13,'borrowed',1,'5'),(14,'borrowed',2,'5'),(15,'borrowed',4,'5'),(16,'borrowed',5,'5'),(17,'borrowed',7,'5'),(18,'available',8,'5'),(19,'borrowed',10,'5'),(20,'borrowed',11,'5'),(21,'borrowed',13,'5'),(22,'borrowed',15,'5'),(23,'borrowed',16,'5'),(24,'borrowed',17,'5'),(25,'borrowed',19,'5'),(26,'available',21,'5'),(27,'available',23,'5'),(28,'available',25,'5'),(29,'borrowed',26,'5'),(30,'borrowed',15,'5'),(31,'borrowed',1,'5'),(32,'available',27,'5'),(33,'available',1,'1'),(34,'borrowed',2,'1'),(35,'borrowed',3,'1'),(36,'available',4,'1'),(37,'borrowed',5,'1'),(38,'available',6,'1'),(39,'borrowed',7,'1'),(40,'borrowed',10,'1'),(41,'available',11,'1'),(42,'available',13,'1'),(43,'available',15,'1'),(44,'available',16,'1'),(45,'available',16,'1'),(46,'borrowed',18,'1'),(47,'available',19,'1'),(48,'borrowed',20,'1'),(49,'borrowed',20,'1'),(50,'available',22,'1'),(51,'available',23,'1'),(52,'available',24,'1'),(53,'available',26,'1'),(54,'available',15,'5'),(55,'available',7,'1'),(56,'borrowed',2,'5'),(57,'available',17,'5'),(58,'available',13,'5'),(59,'available',13,'5'),(60,'available',20,'5'),(61,'borrowed',28,'1'),(62,'available',28,'1'),(63,'borrowed',29,'1'),(64,'borrowed',29,'5'),(65,'available',30,'5'),(66,'borrowed',31,'4'),(67,'available',1,'2'),(68,'borrowed',10,'2'),(69,'available',13,'2'),(70,'borrowed',2,'3'),(71,'borrowed',3,'3'),(72,'available',3,'3'),(73,'available',7,'3'),(74,'available',20,'3'),(75,'available',4,'4'),(76,'borrowed',5,'4'),(77,'available',6,'4'),(78,'available',11,'4'),(79,'available',19,'4'),(81,'available',2,'2'),(83,'available',1,'2'),(85,'borrowed',90,'2'),(86,'available',32,'2'),(87,'available',2,'2'),(88,'available',19,'2'),(89,'available',5,'2'),(90,'available',5,'2'),(91,'available',5,'2'),(92,'available',5,'2'),(93,'available',1,'2'),(94,'borrowed',33,'2'),(95,'available',33,'2'),(96,'available',10,'2'),(97,'available',12,'3');
/*!40000 ALTER TABLE `copy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `email_address` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `date_of_birth` date NOT NULL,
  `city` varchar(45) NOT NULL,
  `street` varchar(45) NOT NULL,
  `house_number` int NOT NULL,
  PRIMARY KEY (`email_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('adi@walla.com','123','Adi','Lavi','0579898888','1973-08-12','Tel Aviv','Lea',22),('dana@yahoo.com','234','Dana','Levi','0502345678','1980-09-24','Jerusalem','King George',3),('dudi@gmail.com','789','Dudi','Livni','0507890123','1991-08-03','Jerusalem','Jabotinsky',24),('gali@gmail.com','123','Gali','Clay','0595959999','1999-09-13','Hedera','Brosh',5),('moshe@walla.com','345','Moshe','Katz','0503456789','1990-06-02','Haifa','Ben Gurion',20),('naama@gmail.com','123','Naama','Gad','0540404444','1998-05-10','Haifa','Got',7),('roni@yahoo.com','567','Roni','David','0505678901','1998-12-12','Eilat','Weizmann',3),('sara@gmail.com','456','Sara','Shapira','0504567890','1995-09-09','Beer Sheva','Herzl',12),('shalevh88@gmail.com','123','shalev','haba','0503441633','2023-01-06','HOLON','Menachem Begin',15),('shlomi@walla.com','678','Shlomi','Greenspan','0506789023','1999-11-30','Tel Aviv','Rothschild',2),('tal@walla.com','901','Tal','Mizrahi','0509012345','1999-04-11','Beer Sheva','Begin',9),('yair@yahoo.com','890','Yair','Friedman','0508901234','1999-06-23','Haifa','Herzog',16),('yossi@gmail.com','123','Yossi','Cohen','0501234567','1970-12-01','Tel Aviv','Ibn Gvirol',24),('yotam@gmail.com','012','Yotam','Rabin','0501012345','1985-01-01','Eilat','Ben Zvi',18),('ziv@a.com','123','Ziv','Fried','0545454444','1998-06-12','J','S',5),('ziv@b.com','123','Someone','Youlove','0522323333','1999-09-12','k','k',5);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarian`
--

DROP TABLE IF EXISTS `librarian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarian` (
  `email_address` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `street` varchar(45) NOT NULL,
  `house_number` int NOT NULL,
  `working_Since` date NOT NULL,
  `password` varchar(255) NOT NULL,
  `branch_number` varchar(45) NOT NULL,
  PRIMARY KEY (`email_address`),
  KEY `Branch_number` (`branch_number`),
  CONSTRAINT `librarian_ibfk_1` FOREIGN KEY (`branch_number`) REFERENCES `branch` (`branch_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarian`
--

LOCK TABLES `librarian` WRITE;
/*!40000 ALTER TABLE `librarian` DISABLE KEYS */;
INSERT INTO `librarian` VALUES ('aviv@bookking.com','Aviv','Rosenberg','0505678901','Eilat','Weizmann',1,'2020-12-12','459','5'),('dana@bookking.com','Dana','Sasson','0503456789','Haifa','Ben Gurion',16,'2015-06-29','979','3'),('dror@bookking.com','Dror','Cohen','0505055555','Kfar Saba','Bialik',1,'2023-01-16','123','3'),('nimrod@bookking.com','Nimrod','Klein','0504567890','Beer Sheva','Herzl',8,'2018-03-09','699','4'),('shalevh8@gmail.com','shalev','haba','0503441633','HOLON','Menachem Begin',15,'2023-01-15','123','1'),('shlomi@bookking.com','Shlomi','Gonen','0501234567','Tel Aviv','Ibn Gvirol',12,'2010-02-07','616','1'),('yair@bookking.com','Yair','Nissim','0502345678','Jerusalem','King George',3,'2017-11-18','765','2'),('ziv@z.com','Ziv','Fr','0505050555','jer','S',1,'2023-01-16','123','2');
/*!40000 ALTER TABLE `librarian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_date` date NOT NULL,
  `order_status` enum('completed','in library','currently borrowed','expired') NOT NULL,
  `copy_number` int NOT NULL,
  `customer_email` varchar(45) NOT NULL,
  PRIMARY KEY (`order_date`,`copy_number`,`customer_email`),
  KEY `Copy_number` (`copy_number`),
  KEY `Customer_Email` (`customer_email`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`copy_number`) REFERENCES `copy` (`copy_number`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('2020-01-15','completed',50,'roni@yahoo.com'),('2020-07-24','completed',51,'yair@yahoo.com'),('2021-01-11','completed',14,'yair@yahoo.com'),('2021-03-13','completed',72,'ziv@b.com'),('2021-04-10','completed',66,'yossi@gmail.com'),('2021-06-18','completed',67,'ziv@b.com'),('2022-01-17','completed',18,'moshe@walla.com'),('2023-01-10','completed',15,'dana@yahoo.com'),('2023-01-10','completed',38,'yossi@gmail.com'),('2023-01-13','currently borrowed',15,'tal@walla.com'),('2023-01-15','currently borrowed',29,'shalevh88@gmail.com'),('2023-01-15','currently borrowed',63,'moshe@walla.com'),('2023-01-16','currently borrowed',23,'ziv@b.com'),('2023-01-16','currently borrowed',64,'ziv@a.com'),('2023-01-16','currently borrowed',66,'yossi@gmail.com'),('2023-01-17','currently borrowed',17,'naama@gmail.com'),('2023-01-17','currently borrowed',19,'naama@gmail.com');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-17 14:42:53
