Python interface
================

Naming: Our ETL scripts are called sushi chefs scripts. We eat a lot of sushi as a result o this ;)


Inputs:

  - Any source of metadata (titles, descriptions, licenses, etc)
  - Any source of files (local or URL)
  - Supported content types (formats):
    - `document`(PDF)
    - `audio` (mp3)
    - `video` (mp4)
    - `html5` (zip),
    - `exercise` (json)


Operation:

  - Check channel tree and metadata valid
  - Calls Studio internal APIs (sequence of steps using multiple API endpoints)
    - Upload tree structure
    - Get files diff for files already on Studio
    - Upload new files
    - Commit tree
  - Channel created on Kolibri Studio
    - optional: ACTIVATE / PUBLISH


Outputs:

  - URL of channel on Kolibri Studio where you can view, review, ACTIVATE/PUBLISH, etc.





Use case
--------
  - Best interface for working with Kolibri Studio
  - Many examples available to imitate. See the repos that start with
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
Ricecooker docs: https://github.com/learningequality/ricecooker/tree/master/docs

