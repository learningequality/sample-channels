#!/usr/bin/env bash
set -e

export TEXT_SLUG="the-supreme-court-s-ruling-in-brown-vs-board-of-education"

if [ -d webroot ]; then
  rm -rf webroot
fi
mkdir webroot

if [ -f webroot.zip ]; then
  rm webroot.zip
fi

if [ ! -d node_modules ]; then
  npm install
fi

npm run build

cp index.html webroot/
cp -r dist webroot/

echo "Makeing paths relative"
cd webroot
sed -i -e 's/\/dist/dist/g;' index.html
sed -i -e 's/\/dist/dist/g;' dist/build.js


echo "Creating HTML5Zip file webroot.zip from webroot/ directory"
zip -r ../webroot.zip *
cd ..


wget "https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR.jpg" -O thumbnail.jpg



