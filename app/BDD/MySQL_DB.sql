-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : ven. 25 nov. 2022 à 19:35
-- Version du serveur :  8.0.31-0ubuntu0.20.04.1
-- Version de PHP : 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `snmp`
--

-- --------------------------------------------------------

--
-- Structure de la table `equipements`
--

CREATE TABLE `equipements` (
  `id` int NOT NULL,
  `constructeur` text NOT NULL,
  `type_de_material` text NOT NULL,
  `ipdns` text NOT NULL,
  `description` text NOT NULL,
  `level` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- --------------------------------------------------------

--
-- Structure de la table `oids`
--

CREATE TABLE `oids` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `oids` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `oids`
--

INSERT INTO `oids` (`id`, `name`, `oids`) VALUES
(1, 'High Level', '{\"cpu\": \"1.3.6.1.4.1.14988.1.1.3.6\",\r\n\r\n            \"ram\": \"1.3.6.1.2.1.25.2.3.1.5.65536\",\r\n\r\n            \"debit_entrant\": \"1.3.6.1.2.1.25.2.3.1.6.65536\",\r\n\r\n            \"debit_sortant\": \"1.3.6.1.2.1.31.1.1.1.10.1\"}'),
(2, 'Low Level', '{\"cpu\": \"1.3.6.1.4.1.14988.1.1.3.6\",\r\n            \"ram\": \"1.3.6.1.2.1.25.2.3.1.5.65536\"}');

-- --------------------------------------------------------

--
-- Structure de la table `snmp_result`
--

CREATE TABLE `snmp_result` (
  `id` int NOT NULL,
  `timestamp` varchar(255) NOT NULL,
  `equipement_id` int NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Index pour la table `equipements`
--
ALTER TABLE `equipements`
  ADD PRIMARY KEY (`id`);


--
-- Index pour la table `oids`
--
ALTER TABLE `oids`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `snmp_result`
--
ALTER TABLE `snmp_result`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `equipements`
--
ALTER TABLE `equipements`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `oids`
--
ALTER TABLE `oids`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `snmp_result`
--
ALTER TABLE `snmp_result`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=144;

--
-- Contraintes pour les tables déchargées
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
