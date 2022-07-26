-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema cc500226_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cc500226_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cc500226_db` DEFAULT CHARACTER SET utf8 ;
USE `cc500226_db` ;

-- -----------------------------------------------------
-- Table `cc500226_db`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500226_db`.`region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cc500226_db`.`comuna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500226_db`.`comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comuna_region1_idx` (`region_id` ASC),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `cc500226_db`.`region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cc500226_db`.`tema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500226_db`.`tema` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cc500226_db`.`actividad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500226_db`.`actividad` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `sector` VARCHAR(100) NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `celular` VARCHAR(15) NULL,
  `dia_hora_inicio` TIMESTAMP NOT NULL,
  `dia_hora_termino` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  `descripcion` VARCHAR(500) NULL,
  `tema_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_evento_comuna1_idx` (`comuna_id` ASC),
  INDEX `fk_actividad_tema1_idx` (`tema_id` ASC),
  CONSTRAINT `fk_evento_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `cc500226_db`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_actividad_tema1`
    FOREIGN KEY (`tema_id`)
    REFERENCES `cc500226_db`.`tema` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cc500226_db`.`foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500226_db`.`foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ruta_archivo` VARCHAR(300) NOT NULL,
  `nombre_archivo` VARCHAR(300) NOT NULL,
  `actividad_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_foto_actividad1_idx` (`actividad_id` ASC),
  CONSTRAINT `fk_foto_actividad1`
    FOREIGN KEY (`actividad_id`)
    REFERENCES `cc500226_db`.`actividad` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cc500226_db`.`contactar_por`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500226_db`.`contactar_por` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` ENUM('whatsapp', 'telegram', 'twitter', 'facebook', 'instagram', 'tiktok', 'otra') NOT NULL,
  `identificador` VARCHAR(150) NOT NULL,
  `actividad_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_contactar_por_actividad1_idx` (`actividad_id` ASC),
  CONSTRAINT `fk_contactar_por_actividad1`
    FOREIGN KEY (`actividad_id`)
    REFERENCES `cc500226_db`.`actividad` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
