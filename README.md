# music-catalog-service
This is meant to showcase a tiny API for reading/writing to a Postgres DB.

## INSTALLATION - Using docker-compose
Clone the repository: https://github.com/zlorimer/music-catalog-service

Change directories to <newly_cloned_dir>/src
Run docker-compose build
Then run docker-compose up

## API ENDPOINTS Exposed
---
| Endpoint | Function
| :--- | ---:
| /  | Returns "connection accepted" or similar
| /artistlist | Returns a list of artists
| /albumlist | Returns a list of albums
| /getartist/\<uuid\> | Returns a single artist based on their UUID
| /getalbum/\<uuid\> | Returns a single album based on UUID
| /postartist/ | Inserts a new artist to the artists table
| /postalbum/ | Inserts a new album to the albums table
| /putartist/\<uuid\> | Updates an artist based on matching UUID
| /putalbum/\<uuid\> | Updates an album based on matching UUID
| /deleteartist/\<uuid\> | Delets an artist based on UUID
| /deletealbum/\<uuid\> | Dletes an album base don UUID
