#!/usr/bin/env bash
set -e

npm -g install yarn


if [ -d webroot ]; then
  rm -rf webroot
fi
mkdir webroot

if [ -f webroot.zip ]; then
  rm webroot.zip
fi

if [ ! -d node_modules ]; then
  yarn install
fi


npm run build


echo "Makeing paths relative"
cd build
sed -i -e 's/href="\//href="/g;' index.html
sed -i -e 's/src="\//src="/g;' index.html
rm service-worker.js   # fancy for nothing...


echo "Creating HTML5Zip file webroot.zip from build/ directory"
zip -r ../webroot.zip *
cd ..

wget "https://assets.hongkiat.com/uploads/thumbs/640x410/getting-started-react-js-twitter.jpg" -O thumbnail.jpg



