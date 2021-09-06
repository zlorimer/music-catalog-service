# music-catalog-service
This is meant to showcase a tiny API for reading/writing to a Postgres DB.

## INSTALLATION - Using docker-compose
- Clone the repository: https://github.com/zlorimer/music-catalog-service
- Change directories to <newly_cloned_dir>/src
- Run docker-compose build
- Then run docker-compose up

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

## Tests
List all artists or albums (after runing docker-compose up)
- curl http://localhost/artistlist or curl http://localhost/albumlist (respectively)

Post an artist
- curl -X POST http://localhost/postartist
   -H 'Content-Type: application/json'
   -d '{"artist_name":"new_artist_name_here"}'
   
 And so on...
 
 ## ToDo v1
 - Rewrite the album queries to perform a check for existing artist before inserting
 - Fix the 405 errors being presented in some methods
 ## ToDo v2
 - Rewrite the app to use the following: 
   - Flask-Restful, Flask-SQLAlchemy, Flask-Marshmallow (this v2 was SO much cleaner and easier to support)
 - Create helm chart to allow deploying against k8s clusters
 - Create tests for CI/CD (eg: Do all methods work correctly?)
## In AWS Context / Production
- Run the Postgres instance in RDS w/RDS Proxy to handle connection pooling
  - DBs in containers worry me
- Store app container in ECR and pull into EKS as needed
- Make sure there are separate Landing Zones (dev, stage, prod)
  - Keep clusters segmented to avoid accidentally grenading prod

