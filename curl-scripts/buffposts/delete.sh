#!/bin/bash

curl "http://localhost:8000/buffposts/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
