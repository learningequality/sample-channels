Python interface
================

Naming: Our ETL scripts are called sushi chefs scripts. We eat a lot of sushi as
a result o this ;)


Inputs:

  - Any source of metadata (titles, descriptions, licenses, etc)
  - Any source of files (local or URL)
  - Supported content types (formats):
    - `document`(PDF)
    - `audio` (mp3)
    - `video` (mp4)
    - `html5` (zip),
    - `exercise` (json)


Side effects:

  - Channel created on Kolibri Studio
     - Check channel metadata valid
     - Begin transaction
       - Upload structure
       - Get files diff for files alrady on Studio
       - Upload new files
       - Commit tree
       - optional: ACTIVATE / PUBLISH

Outputs:

  - URL of channel studio where you can view for (review, ACTIVATE/PUBLISH/etc.)





Use case
--------
  - Best interface for working with Kolibri Studio
  - Many examples available to imitate. See all the repositires that start with
    `sushi-chef-`... on [github](https://github.com/learningequality/).



Usage
-----

    ./chef.py -v --reset \
      --token="../../credentials/studiotoken.txt" \
      --channeldir='./content/sample-csv-channel-root'


See all CLI args and options here:

   ./chef.py -h



Links
-----
See also `souschef` workflow which is the same format of CSV, but CSVs are generated
programatically using Python (or could use `ruby` or `js`).
