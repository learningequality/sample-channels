#!/usr/bin/env bash

export CHANNEL_NAME="sample-csv-channel-root"


if [ ! -d content ]; then
  mkdir content
fi

# Make sure channel + contentnodes/ dirs exist
cd content
if [ -d "${CHANNEL_NAME}" ]; then
  rm -rf "${CHANNEL_NAME}"
fi
mkdir "${CHANNEL_NAME}"
mkdir "${CHANNEL_NAME}/contentnodes"
mkdir "${CHANNEL_NAME}/contentnodes/html5"
mkdir "${CHANNEL_NAME}/contentnodes/document"
mkdir "${CHANNEL_NAME}/contentnodes/audio"
mkdir "${CHANNEL_NAME}/contentnodes/video"
wget "https://cdn.arstechnica.net/wp-content/uploads/2013/04/8206085512_12c122ca2e.jpg" -O "${CHANNEL_NAME}/channel_thumbnail.jpg"
cd ..


for html5zip in `ls -1 ../../contentnodes/*/*zip`; do
  appdir_abspath="$(dirname "$html5zip")"
  appdir="$(basename ${appdir_abspath})"
  # mkdir "content/${CHANNEL_NAME}/contentnodes/html5/${appdir}/"
  echo "Copying ${html5zip} to content/${CHANNEL_NAME}/contentnodes/html5/${appdir}.zip"
  cp ${html5zip} "content/${CHANNEL_NAME}/contentnodes/html5/${appdir}.zip"
  if [ -f "${appdir_abspath}/thumbnail.jpg" ]; then
    echo "Copying ${appdir_abspath}/thumbnail.jpg to content/${CHANNEL_NAME}/contentnodes/html5/${appdir}.jpg"
    cp "${appdir_abspath}/thumbnail.jpg" "content/${CHANNEL_NAME}/contentnodes/html5/${appdir}.jpg"
  fi
done

for pdfdoc in `ls -1 ../../contentnodes/document/*pdf`; do
  echo "Copying ${pdfdoc} to content/${CHANNEL_NAME}/contentnodes/"
  cp ${pdfdoc} "content/${CHANNEL_NAME}/contentnodes/document/"
done

for audiofile in `ls -1 ../../contentnodes/audio/*mp3`; do
  echo "Copying ${audiofile} to content/${CHANNEL_NAME}/contentnodes/"
  cp ${audiofile} "content/${CHANNEL_NAME}/contentnodes/audio/"
done

for videofile in `ls -1 ../../contentnodes/video/*mp4`; do
  echo "Copying ${videofile} to content/${CHANNEL_NAME}/contentnodes/"
  cp ${videofile} "content/${CHANNEL_NAME}/contentnodes/video/"
done
