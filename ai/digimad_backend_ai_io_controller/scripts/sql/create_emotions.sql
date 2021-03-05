DROP TABLE emotions;
CREATE TABLE emotions (id INT PRIMARY KEY, emotion_name VARCHAR(255) NOT NULL);

INSERT INTO emotions (id, emotion_name) VALUES (1, 'HAPPY');
INSERT INTO emotions (id, emotion_name) VALUES (2, 'SURPRISED');
INSERT INTO emotions (id, emotion_name) VALUES (3, 'NEUTRAL');
INSERT INTO emotions (id, emotion_name) VALUES (4, 'DISGUST');
INSERT INTO emotions (id, emotion_name) VALUES (5, 'SAD');
INSERT INTO emotions (id, emotion_name) VALUES (6, 'SCARED');
INSERT INTO emotions (id, emotion_name) VALUES (7, 'ANGRY');
