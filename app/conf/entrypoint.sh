#!/bin/bash
DB_HOST=db
until nc -z -v -w30 $DB_HOST 3306
do
  echo "Waiting for database connection..."
  sleep 5
done
uvicorn main:app --host 0.0.0.0 --port 80 --reload