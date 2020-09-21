# I used an AWS LINUX machine to do this part of the assignment.

#this is the shell script to run run the docker container using sql image and then execute all the files in the folder,

#!/bin/bash
#Docker-SQL-SEVER

docker build -t sqlserver:latest .
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Revanth@1server" -p 1433:1433 -d --name sqlserver sqlserver:latest
sleep 30
docker exec sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Revanth@1server" -i /DBscripts/01-create-database.sql
docker exec sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Revanth@1server" -i /DBscripts/02-create-table.sql
docker exec sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Revanth@1server" -i /DBscripts/03-insert-data.sql

#this is the dockerfile to build custom image of the sql server with a DBscripts folder in the root directory copied from the linux home directory.
FROM mcr.microsoft.com/mssql/server:2019-latest
WORKDIR /
USER root
RUN mkdir -p DBscripts/
COPY DBScripts/* /DBscripts/