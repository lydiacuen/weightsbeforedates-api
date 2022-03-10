#!/bin/bash

curl "http://localhost:8000/buffposts/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "mango": {
      "content": "'"${CONTENT}"'",
      "image": "'"${IMAGE}"'"
    }
  }'

echo
