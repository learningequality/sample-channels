#!/usr/bin/env bash

export CHANNEL_NAME="ricecooker-channel-files"

if [ ! -d content ]; then
  mkdir content
fi

# Make sure channel + contentnodes/ dirs exist
cd content
if [ -d "${CHANNEL_NAME}" ]; then
  rm -rf "${CHANNEL_NAME}"
fi
mkdir "${CHANNEL_NAME}"
cd ..

for html5zip in `ls -1 ../../contentnodes/*/*zip`; do
  appdir_abspath="$(dirname "$html5zip")"
  appdir="$(basename ${appdir_abspath})"
  echo "Copying ${html5zip} to content/${CHANNEL_NAME}/${appdir}.zip"
  cp ${html5zip} "content/${CHANNEL_NAME}/${appdir}.zip"
  if [ -f "${appdir_abspath}/thumbnail.jpg" ]; then
    echo "Copying ${appdir_abspath}/thumbnail.jpg to content/${CHANNEL_NAME}/${appdir}.jpg"
    cp "${appdir_abspath}/thumbnail.jpg" "content/${CHANNEL_NAME}/${appdir}.jpg"
  fi
done

for pdfdoc in `ls -1 ../../contentnodes/document/*pdf`; do
  echo "Copying ${pdfdoc} to content/${CHANNEL_NAME}/"
  cp ${pdfdoc} "content/${CHANNEL_NAME}/"
done

for audiofile in `ls -1 ../../contentnodes/audio/*mp3`; do
  echo "Copying ${audiofile} to content/${CHANNEL_NAME}/"
  cp ${audiofile} "content/${CHANNEL_NAME}/"
done

for videofile in `ls -1 ../../contentnodes/video/*mp4`; do
  echo "Copying ${videofile} to content/${CHANNEL_NAME}/"
  cp ${videofile} "content/${CHANNEL_NAME}/"
done

for exercise in `ls -1 ../../contentnodes/exercise/*json`; do
  echo "Copying ${exercise} to content/${CHANNEL_NAME}/"
  cp ${exercise} "content/${CHANNEL_NAME}/"
done
