#!/bin/bash

curl "http://localhost:8000/buffposts/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "buffpost": {
      "content": "'"${CONTENT}"'",
      "image": "'"${IMAGE}"'"
    }
  }'

echo
