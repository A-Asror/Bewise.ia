#!/bin/sh

# Install package
#pip install -r requirements/dev.txt

echo "DB Connection --- Establishing . . ."

while ! nc -z fast-api-postgresql 5432; do

    echo "DB Connection -- Failed!"

    sleep 1

    echo "DB Connection -- Retrying . . ."

done

echo "DB Connection --- Successfully Established!"

exec "$@"
