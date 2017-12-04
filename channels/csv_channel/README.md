CSV-based workflow
==================

Simplified interface for ricecooker library that automatically reads:
  - content files from the local file system
  - content structure from the filesystem hierarchy
  - metadata from two manually curated/edited CSV files:
      - Channel metadata provided in Chaannel.csv
      - Files metadata provided in Content.csv



Inputs:
  - Channel files are organized into a directory hierarchy on the local filesystem
  - Supported formats are `document`(PDF), `audio` (mp3), `video` (mp4), and `html5` (zip), but not exercises
  - Channel metadata provided in Chaannel.csv
  - Files metadata provided in Content.csv



Use case
--------
  - Good interface for both developers and content experts
  - Developers must populate a directory structure containing different content nodes
    and ensure the appropriate metadata is in Channel.csv and Content.csv
  - Content experts can author, edit, and Q/A titles, descriptions, and other
    metadata without the need for support from developers




Usage
-----

    ./update.sh

    ./sushichef.py -v --reset \
      --token="../../credentials/studiotoken.txt" \
      --channeldir='./content/sample-csv-channel-root'





Links
-----
See also `souschef` workflow which is the same format of CSV, but CSVs are generated
programatically using Python (or could use `ruby` or `js`).
