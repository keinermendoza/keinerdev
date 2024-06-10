#!bin/bash
. ./load_env.sh

BACKUP_FILE=$1
docker cp $BACKUP_FILE $CONTAINER_NAME:/var/backups
docker exec -i $CONTAINER_NAME pg_restore -U $POSTGRES_USER -d $POSTGRES_DB --clean --create /var/backups/$BACKUP_FILE
echo "DB restored"

#!bin/bash
. ./load_env.sh

BACKUP_FILE=$1
sudo docker cp $BACKUP_FILE $CONTAINER_NAME:/var/backups
sudo docker exec -i $CONTAINER_NAME pg_restore -U $POSTGRES_USER -d $POSTGRES_DB --clean --create /var/backups/$BACKUP_FILE
echo "DB restored"











