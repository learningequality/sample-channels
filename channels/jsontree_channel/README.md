Ricecooker's JsonTreeChef-based workflow
========================================

Inputs:
  - Any source of metadata (titles, descriptions, licenses, etc)
  - Any source of files (local or URL)
  - Supported content kinds:
    - `document`(PDF)
    - `audio` (mp3)
    - `video` (mp4) (including subtitles)
    - `html5` (zip),
    - `exercise` (simple question types)


Use cases
---------
The `JsonTreeChef` is similar to the basic `SushiChef` approach with an additional
intermediate JSON serialization step, the so-called ricecooker json tree.
The ricecooker json tree is useful for debugging metadata problems and generally
seeing the data before handing it over to the ricecooker library.

If you have existing code in another language (Ruby/JavaScript/?) you can interface
with the ricecooker library by preparing a ricecooker-json-tree, a json representation
of calls to the ricecooker API.

To produce a valid `json` tree, each node must have the `kind` property wchich
specifies one of the [content kinds](https://github.com/learningequality/le-utils/blob/master/le_utils/constants/content_kinds.py)
defined in `le_utils`. Similarly, each of the files associated with the content
nodes must be one of the supported [file types](https://github.com/learningequality/le-utils/blob/master/le_utils/constants/file_types.py)
defined in `le_utils`.


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


Note: See the `ricecooker_channel/chef.py` code example for the simpler chef script
that uses the Ricecooker Python API, which is simpler and doesn not require creating
the JSON intermediate format.
