-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 11, 2020 at 03:34 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ss_sludinajumi`
--

-- --------------------------------------------------------

--
-- Table structure for table `dzivokli_ogre`
--

DROP TABLE IF EXISTS `dzivokli_ogre`;
CREATE TABLE IF NOT EXISTS `dzivokli_ogre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `rajons` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `pilseta` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `iela` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `istabas` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `kvm` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `stavs` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `cena` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
