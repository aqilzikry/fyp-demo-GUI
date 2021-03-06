-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2021 at 11:01 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ccas_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `calls`
--

CREATE TABLE `calls` (
  `id` int(11) NOT NULL,
  `audio` varchar(30) DEFAULT NULL,
  `operator_id` int(11) NOT NULL,
  `emotion` varchar(99) NOT NULL,
  `emotion_prob` float NOT NULL,
  `sentiment` varchar(99) NOT NULL,
  `sentiment_prob` float NOT NULL,
  `topics` varchar(999) NOT NULL,
  `cust_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `calls`
--

INSERT INTO `calls` (`id`, `audio`, `operator_id`, `emotion`, `emotion_prob`, `sentiment`, `sentiment_prob`, `topics`, `cust_id`) VALUES
(168, 'Demo_A1_en.wav', 1, 'angry', 1, 'positive', 0.625797, '{\"bekalan elektrik\": 0.023788364604115486, \"view bill\": 0.0005619777366518974, \"bantuan\": 0.00048859539674595}', 1),
(169, 'Demo_A1_my.wav', 1, 'angry', 0.999241, 'negative', 0.71793, '{\"view bill\": 0.42353513836860657, \"bekalan elektrik\": 0.27019578218460083, \"bantuan\": 0.002550041303038597}', 1),
(170, 'Demo_A2_my.wav', 1, 'angry', 0.976738, 'negative', 0.727058, '{\"bekalan elektrik\": 0.687667727470398, \"view bill\": 0.005314135458320379, \"bantuan\": 0.0029956160578876734}', 1),
(171, 'Demo_H1_my.wav', 1, 'happy', 0.989176, 'neutral', 0.55052, '{\"bantuan\": 0.30933457612991333, \"bekalan elektrik\": 0.05384734645485878, \"view bill\": 0.01397037785500288}', 1),
(172, 'Demo_H2_en.wav', 1, 'neutral', 0.99394, 'positive', 0.786764, '{\"view bill\": 0.9502496123313904, \"bekalan elektrik\": 0.10964389890432358, \"bantuan\": 0.0004794459673576057}', 1),
(173, 'Demo_H2_my.wav', 1, 'happy', 0.975272, 'neutral', 0.958025, '{\"view bill\": 0.2081340253353119, \"bekalan elektrik\": 0.06033230200409889, \"bantuan\": 0.0031719498801976442}', 1),
(174, 'Demo_N1_my.wav', 1, 'neutral', 0.999998, 'neutral', 0.765348, '{\"bekalan elektrik\": 0.0507981963455677, \"view bill\": 0.006741737946867943, \"bantuan\": 0.001981559442356229}', 1),
(175, 'Demo_N2_my.wav', 1, 'neutral', 1, 'negative', 0.530615, '{\"bekalan elektrik\": 0.950131356716156, \"view bill\": 0.2022281140089035, \"bantuan\": 0.0003692386671900749}', 1),
(176, 'Demo_A1_en.wav', 1, 'angry', 1, 'positive', 0.625797, '{\"bekalan elektrik\": 0.009634116664528847, \"view bill\": 0.0031559274066239595, \"bantuan\": 0.0005303985089994967}', 1),
(177, 'Demo_A1_my.wav', 1, 'angry', 0.999241, 'negative', 0.71793, '{\"bekalan elektrik\": 0.8638232350349426, \"view bill\": 0.06791139394044876, \"bantuan\": 0.0024341039825230837}', 1),
(178, 'Demo_A2_my.wav', 1, 'angry', 0.976738, 'negative', 0.727058, '{\"bekalan elektrik\": 0.8926474452018738, \"view bill\": 0.007258742582052946, \"bantuan\": 0.0019215159118175507}', 1),
(179, 'Demo_H1_my.wav', 1, 'happy', 0.989176, 'neutral', 0.55052, '{\"bantuan\": 0.32834187150001526, \"bekalan elektrik\": 0.009765243157744408, \"view bill\": 0.0027817394584417343}', 1),
(180, 'Demo_H2_en.wav', 1, 'neutral', 0.99394, 'positive', 0.786764, '{\"view bill\": 0.9893932342529297, \"bekalan elektrik\": 0.14477171003818512, \"bantuan\": 0.02528749592602253}', 1),
(181, 'Demo_H2_my.wav', 1, 'happy', 0.975272, 'neutral', 0.958025, '{\"view bill\": 0.17570193111896515, \"bekalan elektrik\": 0.023865168914198875, \"bantuan\": 0.021153511479496956}', 1),
(182, 'Demo_N1_my.wav', 1, 'neutral', 0.999998, 'neutral', 0.765348, '{\"bekalan elektrik\": 0.3008139729499817, \"view bill\": 0.010017802007496357, \"bantuan\": 0.008694930002093315}', 1),
(183, 'Demo_N2_my.wav', 1, 'neutral', 1, 'negative', 0.530615, '{\"bekalan elektrik\": 0.9686925411224365, \"view bill\": 0.0988699421286583, \"bantuan\": 0.0031167680863291025}', 1),
(184, 'Demo_angry_malay.wav', 1, 'angry', 0.976738, 'negative', 0.727058, '{\"bekalan elektrik\": 0.9009358882904053, \"bantuan\": 0.019422948360443115, \"view bill\": 0.004480236209928989}', 1),
(185, 'Demo_happy_manglish.wav', 1, 'happy', 0.992078, 'neutral', 0.714153, '{\"bantuan\": 0.9852684140205383, \"bekalan elektrik\": 0.9578856825828552, \"view bill\": 0.0025226527359336615}', 1),
(186, 'Demo_neutral_english.wav', 1, 'neutral', 0.825352, 'positive', 0.649841, '{\"bekalan elektrik\": 0.7101370692253113, \"view bill\": 0.006729545537382364, \"bantuan\": 0.0002916516095865518}', 1),
(187, 'Demo_angry_malay.wav', 1, 'angry', 0.976738, 'negative', 0.727058, '{\"bekalan elektrik\": 0.9117812514305115, \"view bill\": 0.010914583690464497, \"bantuan\": 0.004529035650193691}', 1),
(188, 'Demo_happy_manglish.wav', 1, 'happy', 0.992078, 'neutral', 0.714153, '{\"bekalan elektrik\": 0.9754698872566223, \"bantuan\": 0.3950842618942261, \"view bill\": 0.079994335770607}', 1),
(189, 'Demo_neutral_english.wav', 1, 'neutral', 0.825352, 'positive', 0.649841, '{\"bekalan elektrik\": 0.3181312382221222, \"view bill\": 0.00619124760851264, \"bantuan\": 0.0015200850320979953}', 1),
(190, 'Demo_angry_malay.wav', 1, 'angry', 0.976738, 'negative', 0.727058, '{\"bekalan elektrik\": 0.8598216772079468, \"view bill\": 0.004213410895317793, \"bantuan\": 0.002416403731331229}', 1),
(191, 'Demo_happy_manglish.wav', 1, 'happy', 0.992078, 'neutral', 0.714153, '{\"bekalan elektrik\": 0.9744877815246582, \"bantuan\": 0.05937793105840683, \"view bill\": 0.01616702787578106}', 1),
(192, 'Demo_neutral_english.wav', 1, 'neutral', 0.825352, 'positive', 0.649841, '{\"bekalan elektrik\": 0.6064078211784363, \"view bill\": 0.0034028547815978527, \"bantuan\": 0.0002385981206316501}', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `calls`
--
ALTER TABLE `calls`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `calls`
--
ALTER TABLE `calls`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=193;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
