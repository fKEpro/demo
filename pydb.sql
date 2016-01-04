
CREATE DATABASE `pydb`;

CREATE TABLE `pydb`.`product` (
  `idproduct` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL,
  `code` VARCHAR(10) NOT NULL,
  `price` DECIMAL NOT NULL,
  `quantity` INT NULL,
  `created` DATETIME NULL,
  PRIMARY KEY (`idproduct`));
