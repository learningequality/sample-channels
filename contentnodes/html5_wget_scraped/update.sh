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

cd webroot
wget --no-parent \
  --convert-links \
  --page-requisites \
  --no-directories \
  --no-host-directories \
  --span-hosts \
  --adjust-extension \
  https://www.commonlit.org/texts/${TEXT_SLUG}

mv ${TEXT_SLUG}.html index.html

sed -i -e 's/<head>/<head><meta charset="UTF-8">/;' index.html

echo "Creatin HTML5Zip file webroot.zip"
zip ../webroot.zip *

wget "https://d11in36igezwwb.cloudfront.net/texts/images/000/000/972/medium/The_Supreme_Court's_Ruling_in_Brown_vs._Boar.jpg?1492106121" -O ../thumbnail.jpg



