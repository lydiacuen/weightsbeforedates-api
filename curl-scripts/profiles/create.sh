#!/bin/bash

curl "http://localhost:8000/profiles/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "profile": {
      "name": "'"${NAME}"'",
      "about": "'"${ABOUT}"'"
    }
  }'

echo
