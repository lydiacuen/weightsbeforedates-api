#!/bin/bash

curl "http://localhost:8000/profiles/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
