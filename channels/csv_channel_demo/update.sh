#!/usr/bin/env bash

CHANNEL_ROOT_DIR="channelrootfolder"
CHANNEL_ROOT_ABSPATH="/Users/ivan/Desktop/csv_channel_demo/$CHANNEL_ROOT_DIR"

SOURCE_DIR_BASE="../Source Material/Final - V2"
DEST_DIR_BASE="$CHANNEL_ROOT_ABSPATH/Toolkit"


echo "Copying PDF files from $SOURCE_DIR_BASE    -->   $DEST_DIR_BASE"
cd "$SOURCE_DIR_BASE"
find . -name '*.pdf'  -print0 |
    while IFS= read -r -d $'\0' filepath;
    do
        echo "  - copying $filepath";
        subdir=$(dirname "$filepath")
        filename=$(basename "$filepath")
        destdir="$DEST_DIR_BASE/$subdir"
        if [ ! -d "$destdir" ]; then
            mkdir -p "$destdir"
        fi
        cp "$subdir/$filename" "$destdir/$filename"
    done


# TODO download docs automatically and move
# TODO re-root the html docs using    zip -r ../kolibri-dev-webroot.zip *
# zip -r ../kolibri-studio-webroot.zip *