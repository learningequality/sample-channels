CSV-based exercises workflow
============================

This sample channel is similar to the `csv_channel` sample, but also has exercsies.

Recall the CSV-based workflow for reads data from the following places:
  - content files from the local file system
  - content structure from the filesystem hierarchy
  - metadata from two manually curated/edited CSV files:
      - Channel metadata provided in Chaannel.csv
      - Files metadata provided in Content.csv

The CSV exercises workflow requires at least two additional files
  - Exercises.csv to store exercise metadata and master model
  - ExerciseQuestions.csv to store individual questions



Inputs:
  - Channel files organized into a directory hierarchy under on the local filesystem
  - Supported formats are `document`(PDF), `audio` (mp3), `video` (mp4), and `html5` (zip), but not exercises
  - Thumbnails (`.jpg`) can be placed along side the main content files
  - Channel metadata provided in `Chaannel.csv`
  - Files metadata provided in `Content.csv`
  - `Exercises.csv`
  - `ExerciseQuestions.csv`
  - Any images to be included in question fields that allow markdown syntax.


See the [csv_channel/README.md](../csv_channel/README.md) for info about CSV channel metadata.

See https://github.com/ivanistheone/ricecooker/blob/feature/csvexercises/docs/csv_exercises.md
for instructions specific to CSV exercises.



Install
-------

    virtualenv -p python3  venv
    source venv/bin/activate
    pip install -r ../../requirements.txt
    pip install git+https://github.com/ivanistheone/ricecooker@feature/csvexercises



Usage
-----

    ./linecook.py -v --reset \
      --token="../../credentials/studiotoken.txt" \
      --channeldir='./content/sample-csv-channel-root'

If you get an error when running the linecook script (in the end), you have to
change the channel Source ID column in `Channel.csv`, or ask the LE team to
make you an editor for the channel with this source id.

This above commands will create or update the channel on Kolibri Studio. As part
of the upload process, the file `chefdata/trees/ricecooker_json_tree.json` which
shows the exact data and metadata that was uploaded to Kolibri Studio. You can use
this file to debug all kinds of problems: missing descriptions, bad formats, etc.
