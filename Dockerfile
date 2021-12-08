FROM tiangolo/docker-with-compose:latest AS main

RUN mkdir -p ELN
RUN mkdir -p ELN/db-data
COPY ./shared ELN/shared
COPY docker-compose.yml ELN/docker-compose.yml