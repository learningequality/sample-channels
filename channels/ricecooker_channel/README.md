Python interface
================
Before we begin, a note on naming is in order. All our ETL scripts are called
**sushi chef** scripts. We eat a lot of sushi as a result o this ;)

Using the `ricecooker` Python library is the most versatile and powerful approach
for uploading content to Kolibri Studio.




Inputs:

  - Any source of metadata (titles, descriptions, licenses, etc)
  - Any source of files (local or URL)
  - Supported content types (formats):
    - `document`(PDF)
    - `audio` (mp3)
    - `video` (mp4) (including subtitles)
    - `html5` (zip),
    - `exercise` (perseus json, or simple question types)


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

    ./sushichef.py -v --reset --token="../../credentials/studiotoken.txt"


See all CLI args and options here:

    ./sushichef.py -h







Links
-----
Ricecooker docs: https://github.com/learningequality/ricecooker/tree/master/docs

