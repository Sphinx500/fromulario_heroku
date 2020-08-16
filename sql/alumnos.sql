
USE hd331w2qe3rpldjj;

CREATE TABLE students(
	id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    matricula char(10) NOT NULL,
    nombre char(10) NOT NULL,
    pri_ap varchar(100) NOT NULL,
    seg_ap varchar(100) NOT NULL,
    age char(3) NOT NULL,
    fdate date ,
    gender varchar(20) NOT NULL,
    state varchar(100) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO students(id,matricula,nombre,pri_ap,seg_ap,age,fdate,gender,state)
VALUES
(null,'1718110040','Fernando','Hernandez', 'Vazquez', '20','2000/01/27', 'Masculino','hidalgo'),
(null,'1719112255','Guadalupe','Espinoz','Riveros','20','2000/05/04','Femenino','Hidalgo');




