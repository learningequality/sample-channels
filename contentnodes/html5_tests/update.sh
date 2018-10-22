#!/usr/bin/env bash
set -e

if [ -f webroot.zip ]; then
  rm webroot.zip
fi

cd webroot
echo "Creatin HTML5Zip file webroot.zip"
zip ../webroot.zip *


