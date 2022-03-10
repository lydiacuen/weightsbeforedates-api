#!/bin/bash

curl "http://localhost:8000/buffposts/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
