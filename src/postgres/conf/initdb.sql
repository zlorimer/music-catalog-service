CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE artists(uuid UUID DEFAULT uuid_generate_v4 () PRIMARY KEY, artist_name VARCHAR(150) NOT NULL);
COPY artists(artist_name) FROM '/docker-entrypoint-initdb.d/artists.csv' DELIMITER ',' CSV HEADER;
CREATE TABLE albums(uuid UUID DEFAULT uuid_generate_v4 () PRIMARY KEY, artist_name VARCHAR(150) NOT NULL, album_title VARCHAR(150) NOT NULL, release_date INTEGER NOT NULL, price FLOAT NOT NULL);
COPY albums(artist_name, album_title, release_date, price) FROM '/docker-entrypoint-initdb.d/albums.csv' DELIMITER ',' CSV HEADER;