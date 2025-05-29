#!/bin/bash

# Load env variables from .env file
set -a
source core/.env
set +a

OUTPUT="core/static/model/model.pkl"

echo 'Downloading model from drive...'

# Now use $FILE_ID from the .env
gdown --fuzzy https://drive.google.com/file/d/${FILE_ID}/view?usp=sharing -O ${OUTPUT}

echo 'Download complete...' 
echo 'Download model to' $OUTPUT
