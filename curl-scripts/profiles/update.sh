#!/bin/bash

curl "http://localhost:8000/profiles/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "buffpost": {
      "name": "'"${NAME}"'",
      "about": "'"${ABOUT}"'"
    }
  }'

echo
