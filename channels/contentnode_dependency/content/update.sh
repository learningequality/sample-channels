#!/usr/bin/env bash
set -e

# DO NOT RUN THIS TO MAKE SURE ZIP FILE DOESN'T CHANGE (need to keep the same hash)
# if [ -f zipfiles/shared.zip ]; then
#   rm zipfiles/shared.zip
# fi
# 
# echo "Creating HTML5Zip file shared.zip from shared/ directory"
# cd shared
# zip -r ../zipfiles/shared.zip *
# cd ..


if [ -f zipfiles/thinapp1.zip ]; then
  rm zipfiles/thinapp1.zip
fi

echo "Creating HTML5Zip file thinapp1.zip from thinapp1/ directory"
cd thinapp1
zip -r ../zipfiles/thinapp1.zip *
cd ..

