#!bin/bash

# Get env variables
. ./load_env.sh

# backup database
docker exec -i "$CONTAINER_NAME" pg_dump \
 -Fc -U "$POSTGRES_USER" "$POSTGRES_DB" > ../backups/postgres-backup.dump 

#  #!bin/bash

# # Get env variables
# . ./load_env.sh

# # backup database
# sudo docker exec -i "$CONTAINER_NAME" pg_dump \
#  -Fc -U "$POSTGRES_USER" "$POSTGRES_DB" > ../backups/postgres-backup.dump 







