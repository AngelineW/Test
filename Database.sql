-- DROP database IF EXISTS hospital_db;
CREATE database IF NOT EXISTS hospital_db;
USE hospital_db;

-- DROP TABLE IF EXISTS patient_detail;
CREATE table IF NOT EXISTS patient_detail(
					  id varchar(500) NOT NULL,
                                          date varchar(500) NOT NULL,
                                          card_no varchar(500) NOT NULL,
					  first_name varchar(500) NOT NULL,
					  last_name varchar(500) NOT NULL,
                                          other_name varchar(500) NOT NULL,
                                          date_of_birth varchar(500) NOT NULL,
                                          gender varchar(500) NOT NULL,
                                          phone varchar(500) NOT NULL
                                          );

SELECT department FROM  patient_detail GROUP BY name ORDER BY name desc;
SELECT specialist FROM  patient_detail GROUP BY name ORDER BY name desc;
INSERT INTO patient_detail VALUES (A007, Angeline, Kagunda, 20/11/2021, female, 079854567, Reception, Angie, 1234);

UPDATE patient_detail SET date_of_birth = '2002-12-05' WHERE card_no LIKE 'AB001';
UPDATE patient_detail SET gender = 'FEMALE' WHERE card_no LIKE 'AB001';
SELECT * FROM  patient_detail;

SELECT first_name, last_name, other_name FROM patient_detail WHERE card_no LIKE 'MH018';






-- DROP TABLE IF EXISTS employee_detail;

-- DROP TABLE IF EXISTS employee_detail;
CREATE table IF NOT EXISTS employee_detail( 
								id  varchar(500) PRIMARY KEY NOT NULL,
                                date  varchar(500) NOT NULL,
								staff_id  varchar(500)  NOT NULL UNIQUE,
                                title varchar(500),
                                first_name varchar(500) NOT NULL,
                                last_name varchar(500) NOT NULL,
                                other_name varchar(500),
                                user_type  varchar(500) NOT NULL,
                                username  varchar(500) NOT NULL,
                                password  varchar(500) NOT NULL
                                )
ENGINE=INNODB;

SELECT * FROM employee_detail;

SELECT * FROM employee_detail;
INSERT INTO employee_detail VALUES (1, DR1001, 20/11/2021, DR1001, Angeline, Kagunda, Reception, Angie, 1234);
INSERT INTO employee_detail VALUES (2, Harriet, Kagunda, Minor_Surgery, Harriet1, 4321);                              


-- DROP TABLE IF EXISTS department;
CREATE table IF NOT EXISTS department ( id varchar(250) NOT NULL PRIMARY KEY,
			   date varchar(500) NOT NULL,
			   name varchar(500) NOT NULL UNIQUE
                            );

-- DESCRIBE department;

INSERT INTO department (id, date, name) VALUES ('1', '20/11/2021', 'Maternity');                      
INSERT INTO department (id, date, name) VALUES ('2', '20/11/2021', 'Major_Surgery');
INSERT INTO department (id, date, name) VALUES ('3', '20/11/2021', 'Med_Lab');
INSERT INTO department (id, date, name) VALUES ('4', '20/11/2021', 'Orthopedic');
INSERT INTO department (id, date, name)  VALUES ('5', '20/11/2021', 'Peadetrics');
SELECT * FROM department;
SELECT name FROM department GROUP BY name ORDER BY name desc;

-- DROP TABLE IF EXISTS role;
CREATE table IF NOT EXISTS role (id varchar(500) NOT NULL PRIMARY KEY,
					 date varchar(500) NOT NULL,
                     department  varchar(500) NOT NULL,
                     name  varchar(500) NOT NULL UNIQUE,
                     FOREIGN KEY (department)
		     REFERENCES department(name)
                     ON DELETE RESTRICT
                     ON UPDATE cascade
					);

-- DESCRIBE role;

INSERT INTO role VALUES ('1', '20/11/2021', 'Major_Surgery', 'Surgeon');                   
INSERT INTO role VALUES ('2', '20/11/2021', 'Peadetrics', 'Doctor');
INSERT INTO role VALUES ('3', '20/11/2021', 'Med_Lab', 'Lab_technician');
INSERT INTO role VALUES ('4', '20/11/2021', 'Orthopedic', 'Doctor');

SELECT * FROM role;


-- DROP TABLE IF EXISTS specialist;
CREATE TABLE IF NOT EXISTS specialist (id varchar(500) NOT NULL,
						 date varchar(500) NOT NULL,
						 department varchar(500) NOT NULL,
						 role varchar(500) NOT NULL,
                         			 staff_id varchar(500),
                        			 queue int,
                        			 queue_length int,
						 FOREIGN KEY (department)
						 REFERENCES department(name),
                        			 FOREIGN KEY (role)
						 REFERENCES role(name)
                         );
                        
INSERT INTO specialist VALUES (1, 20/11/2021, Paedetric, Doctor, DR, Patriciah);  
INSERT INTO specialist VALUES (1, 20/11/2021, Paedetrician, Doctor, DR, Peadetrician);
INSERT INTO specialist VALUES (1, 20/11/2021, paedetrician, Doctor, DR, Peadetrician);
INSERT INTO specialist VALUES (1, 20/11/2021, Paedetrician, Doctor, DR, Peadetrician);			

SELECT * FROM specialist;

-- DROP TABLE IF EXISTS queue;
CREATE TABLE IF NOT EXISTS queue (
						id varchar(500) NOT NULL,
						date varchar(500) NOT NULL,
						department varchar(500) NOT NULL,
						role varchar(500) NOT NULL,
                        			staff_id varchar(500),
                        			specialist_name varchar(500),
						patient_card_no varchar(500) NOT NULL,
                       				patient_name varchar(500) NOT NULL,
                        			queue_no varchar(500),
                        			status varchar(500)
                        )

SELECT * FROM queue;

DELETE FROM queue WHERE staff_id LIKE 'A001';

-- DROP TABLE IF EXISTS visit;
CREATE TABLE IF NOT EXISTS visit (
						id varchar(500) NOT NULL,
						date varchar(500) NOT NULL,
						card_no varchar(500),
						staff_id varchar(500),
						visit_note varchar(500),
						referral_note varchar(500),
					 	tests varchar(500),
						diagnosis varchar(500),
						prescription varchar(500) 
)

SELECT * FROM visit;

DELETE FROM visit WHERE referral_note IS NULL;
