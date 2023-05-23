CREATE DATABASE IF NOT EXISTS `games` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GO
USE `games`;
GO
CREATE TABLE `users_scores` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL DEFAULT '' PRIMARY KEY,
  `score` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
GO
ALTER TABLE `users_scores`
  ADD CONSTRAINT UC_Person UNIQUE (`user_id`,`name`);
GO
ALTER TABLE `users_scores`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;