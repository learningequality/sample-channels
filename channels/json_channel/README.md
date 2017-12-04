Ricecooker's JsonChef-based workflow
====================================

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
By default assumes json input is in `chefdata/trees/ricecooker_json_tree.json`

    ./jsonchef.py -v --reset \
      --token="../../credentials/studiotoken.txt"
