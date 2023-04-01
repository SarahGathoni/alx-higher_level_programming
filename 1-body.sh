#!/bin/bash
# Get the response body for a given URL for 200 status code responses.

url=$1
response=$(curl --write-out '%{http_code}' --silent --output - "$url")

if [[ $response -eq 200 ]]; then
  body=$(curl --silent --location "$url")
  echo "$body"
else
  echo "Request failed with status code: $response"
fi
