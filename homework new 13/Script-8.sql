CREATE TABLE pupils (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(30) NOT NULL,
	birthday DATE NOT NULL,
	gender TINYINT DEFAULT 1
);


CREATE INDEX pupils_id_IDX ON pupils (id);



CREATE TABLE courses (
	id INTEGER,
	title VARCHAR(50),
	is_children INTEGER, lang VARCHAR(30),
	CONSTRAINT courses_PK PRIMARY KEY (id)
);


CREATE TABLE school (
	pupil_id INTEGER NOT NULL,
	course_id INTEGER NOT NULL,
	rating INTEGER,
	CONSTRAINT school_PK PRIMARY KEY (pupil_id,course_id),
	CONSTRAINT school_FK FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT school_FK_1 FOREIGN KEY (pupil_id) REFERENCES pupils(id) ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO pupils
(name, birthday, gender)
VALUES('Andrew', '2000-10-5', 1);

INSERT INTO pupils
(name, birthday, gender)
VALUES('Yana', '2001-10-7', 2);

INSERT INTO pupils
(name, birthday, gender)
VALUES('Gindenburg', '1995-10-5', 3);

INSERT INTO courses
(id, title, is_children, lang)
VALUES(1, 'Java', 2, 'Python');

SELECT COUNT(*) AS PYTHON_STUDENT
FROM school s ,courses c
WHERE lang = 'C#' and c.id = s.course_id

SELECT COUNT(*) AS PYTHON_STUDENT
FROM school s ,courses c
WHERE lang = 'python' and c.id = s.course_id

SELECT MAX(rating) AS best_rating FROM courses c, school s 
WHERE lang = 'python' AND c.id = s.course_id

SELECT COUNT(*) AS STUDENT, lang 
FROM school s ,courses c
WHERE  c.id = s.course_id 
GROUP BY lang 
ORDER BY STUDENT DESC ,lang

SELECT c.title  
  FROM  pupils p, school s, courses c
 WHERE gender = 2 
   AND p.id = s.pupil_id 
   AND s.course_id = c.id;
   
  DELETE FROM school
WHERE pupil_id IN (SELECT  id FROM pupils 
 WHERE name = 'Maksim')