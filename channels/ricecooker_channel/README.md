Ricecooker python interface
===========================
Using the `ricecooker` Python library is the most versatile and powerful approach
for uploading content to Kolibri Studio.
A note terminology: content integration scripts are called **sushi chef** scripts.


What is a content integration script?
-------------------------------------

Inputs:

  - Any source of metadata (titles, descriptions, licenses, etc)
  - Any source of files (the `path` attribute can be a local filesystem path or a URL)
  - Supported content types (formats):
    - `audio` (mp3)
    - `document` (PDF)
    - `html5` (zip),
    - `video` (mp4 or youtube) (including subtitles)
    - `exercise` (perseus json, or simple question types)


Outputs:

  - URL of channel on Kolibri Studio where you can view, review, DEPLOY/PUBLISH,
    then after the channel is PUBLISHed, you'll be able to IMPORT it in Kolibri.



Use case
--------
  - Large channels (100+ nodes) which would take too long to upload manually
  - Channels that need to be updated regularly (e.g. website with new lessons published every month)
  - Scraping web content (download HTML/js/css/assets from a website and package as standalone `HTML5Zip` file)
  - Use for content that requires transformations (format conversions or video compression)
  - Most of the channel in the Kolibri Content Library are created this way


Usage
-----

    ./sushichef.py -v --reset --token="../../credentials/studiotoken.txt" --thumbnails



See all CLI args and options here:

    ./sushichef.py -h







Links
-----
Ricecooker docs: https://github.com/learningequality/ricecooker/tree/master/docs

