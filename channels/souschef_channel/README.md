Ricecooker's JsonChef-based workflow
====================================


Simplified interface for ricecooker:
  - Supported formats are `document`(PDF), `audio` (mp3), `video` (mp4), and `html5` (zip), but not exercises
  - Defines an informal "portable channel archive" format that consists of a zip file containing:
      - Channel files are organized into a directory hierarchy on the local filesystem
      - Channel metadata provided in `Chaannel.csv`
      - Files metadata provided in `Content.csv`


Note this is the same format as used by the [CSV-based workflow](../csv_channel),
but we've zipped the source content directory.


Use cases
---------

### For Python users:

  - Use simplified souschef interface: DataWriter, read, add_file, etc.


This "zip archive" approach for packaging a content source doesn't need to be done
in Python. You can create the zip archive using any any methods. Just copy-paste
this code and re-implement in your faivourite scripting language:
https://github.com/learningequality/ricecooker/blob/master/ricecooker/utils/data_writer.py
Alternatively, you can write the Channel.csv + Content.csv and the files to a local directory
then zip it.


### For Non-Pythnon users:

You can programatically create CSV + file hierarchy through another language (e.g. ruby/js).
So long as it's has supported file types and for each file there is a matching metadata line in Content.csv, it's all good.

Unintended benefits of CSV+files_in_.zip archive format:
  - a "debugging interface" for all the metadata (can review ans QA in Excel)
  - ability to transport channel from one machine to another
  - files stored within zip file so no possibility of Win32 / UNIX path sep. confusion

Alternatively you can use your favourite language to produce ricecooker json format
and then use the [JsonTreeChef-based workflow](../jsontree_channel).



Details
-------
See here for how to write a souschef script:  
https://github.com/learningequality/ricecooker/blob/master/docs/souschef.md

For sample souschef scripts, see the examples directory:
https://github.com/learningequality/cookiecutter-chef/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/examples



Usage
-----

You can run the whole ETL pipeline `souschef.py`, unzip, `LineCook` script as follows:

    ./souschef.py

    ARCHIVE_NAME="souschef-sample-channel-root"
    mkdir content
    mv ${ARCHIVE_NAME}.zip content/
    cd content
    unzip -oq ${ARCHIVE_NAME}.zip
    cd ..

    ./linecook.py -v --reset \
        --token="../../credentials/studiotoken.txt" \
        --channeldir="./content/${ARCHIVE_NAME}"

Note the third part of this workflow is identical to the [CSV-based](../csv_channel) workflow.
