FROM postgres:alpine

RUN apk add -u git && \
        mkdir /code && \
        cd /code && \
        git clone https://github.com/zlorimer/music-catalog-service.git && \
        cp /code/music-catalog-service/src/postgres/conf/* /docker-entrypoint-initdb.d/.
