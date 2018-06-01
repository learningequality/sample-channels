#!/usr/bin/env bash
CURDIR=`pwd`

cd thinAwebroot
zip -r ../thinAwebroot.zip *

cd "$CURDIR"

cd thinBwebroot
zip -r ../thinBwebroot.zip *