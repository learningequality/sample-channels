LE Demo Channel
===============

This channel was created from a hierarchy of folders and files in the local filesystem + metadata specified in .CSV files that were created using spreadshseet software.

### Final results

  - Studio: https://develop.studio.learningequality.org/channels/f4dd668af2a35917a97b3e96864e5a47/edit
  - Demo: http://35.196.115.213/learn/#/topics/f4dd668af2a35917a97b3e96864e5a47


## Setup

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install /Users/ivan/Projects/FLECode/le-utils
    pip install  /Users/ivan/Projects/FLECode/ricecooker


## Usage

### 1. Curation



### 2. Generate CSV templates

    ./sushchef.py --generate --channeldir channelrootfolder



### 3. Fill in CSV metadata 


  
### 4. Upload to Studio



    export STUDIO_URL="https://develop.studio.learningequality.org"
    ./sushichef.py -v --reset --token=<YOURSTUDIOTOKEN> --channeldir=channelrootfolder





Cheffing environment tutorial
-----------------------------

    > source venv/bin/activate

To "source" a file is to run it

    > which python
    /Users/ivan/Desktop/csv_channel_demo/venv/bin/python

# ^ we're in the python virtual environment

    > which pip
    /Users/ivan/Desktop/csv_channel_demo/venv/bin/pip

# ^ if you pip install something ur not messing up your system python
