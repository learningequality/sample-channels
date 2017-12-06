Ricecooker's JsonTreeChef-based workflow
========================================

Inputs:
  - Content metadata provided json tree structure
  - Files imported can be local or represented as URLs


Use cases
---------
If you have existing code in another language (Ruby/JavaScript/?) you can interface
with the ricecooker library by preparing a ricecooker-json-tree, a json representation
of calls to the ricecooker API.
To produce a valid `json` tree, each node must have the `kind` property wchich specifies
either

  - one of the supported contenty types defined in `le_utils`
    https://github.com/learningequality/le-utils/blob/master/le_utils/constants/content_kinds.py

or

  - one of the supported file types defined in `le_utils`
    https://github.com/learningequality/le-utils/blob/master/le_utils/constants/file_types.py



Usage
-----

    # copy files from ../contentnodes/?? to content/sample-json-channel-files/
    ./update.sh

    ./jsontreechef.py -v --reset --token="../../credentials/studiotoken.txt"

If you get an error when running the linecook script (in the end), you might
have to change the channel's `source_id` proprty in `chefdata/trees/sample_ricecooker_json_tree.json`,
or ask the LE team to make you an editor for the channel with this source id.

By default assumes json input is in `chefdata/trees/ricecooker_json_tree.json`,
but the class the script `jsontreechef.py` contains a subclass of `JsonTreeChef`
with a custom ricecooker tree path `chefdata/trees/sample_ricecooker_json_tree.json`.
This flexibility for specifying different input files is necessary when a single
chef script handles multiple languages.