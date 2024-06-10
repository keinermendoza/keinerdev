#!bin/bash

ENV_FILE="../.env.db"

if [ ! -f "$ENV_FILE" ]; then 
    echo "File $ENV_FILE not found"
    exit 1
fi 

export $(grep -v '^#' "$ENV_FILE" | xargs)
echo "Variable from $ENV_FILE SUCCEFULLY readed"