#!/bin/bash

curl "http://localhost:8000/profiles/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
