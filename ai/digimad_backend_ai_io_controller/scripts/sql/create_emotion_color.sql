DROP TABLE emotion_color;
CREATE TABLE emotion_color (emotion_name VARCHAR(255) NOT NULL, nth_color INT NOT NULL, color_name VARCHAR(255) NOT NULL, PRIMARY KEY (emotion_name, nth_color));

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("HAPPY", 1, "YELLOW1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("HAPPY", 2, "YELLOW2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("HAPPY", 3, "YELLOW3");

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SURPRISED", 1, "ORANGE1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SURPRISED", 2, "ORANGE2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SURPRISED", 3, "ORANGE3");

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("NEUTRAL", 1, "GREEN1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("NEUTRAL", 2, "GREEN2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("NEUTRAL", 3, "GREEN3");

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("DISGUST", 1, "BROWN1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("DISGUST", 2, "BROWN2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("DISGUST", 3, "BROWN3");

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SAD", 1, "BLUE1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SAD", 2, "BLUE2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SAD", 3, "BLUE3");

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SCARED", 1, "PURPLE1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SCARED", 2, "PURPLE2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("SCARED", 3, "PURPLE3");

INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("ANGRY", 1, "RED1");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("ANGRY", 2, "RED2");
INSERT INTO emotion_color (emotion_name, nth_color, color_name) VALUES ("ANGRY", 3, "RED3");
