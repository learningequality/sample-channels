CSV-based exercises workflow
============================
This sample channel is similar to the `csv_channel` sample, but also has exercises.
Before running this example, we recommend you read about the CSV Workflow that
for building channels by reading information from the following places:
  - channel structure from the filesystem hierarchy
  - metadata from two manually curated/edited CSV files:
    - Channel metadata provided in `Chaannel.csv`
    - Files metadata provided in `Content.csv`
See the [csv_channel/README.md](../csv_channel/README.md) for info about CSV channel metadata.
See https://ricecooker.readthedocs.io/en/latest/concepts/content_workflows.html#csv-metadata-workflow
for general info about CSV metadata uploads. This sample channel is specific to CSV exercises.

The CSV Exercises Workflow is a special case of the CSV Workflow that also allows
to provide the information for Exercise nodes and associate one or more questions
(assessment items) to each exercise. Two additional files are required:
  - `Exercises.csv` to store exercise metadata and mastery model
  - `ExerciseQuestions.csv` to store individual questions

Inputs:
  - Empty folder hierarchy on the local filesystem that defines the channel's topic structure
  - Channel metadata provided in `Chaannel.csv` 
  - Files metadata provided in `Content.csv`
  - Exercise nodes provided in `Exercises.csv`
  - Exercise questions (assessment items) provided in `ExerciseQuestions.csv`


Install
-------

    virtualenv -p python3  venv
    source venv/bin/activate
    pip install -r requirements.txt


Usage
-----
Assuming Linux or other UNIX system, run the command:

    ./linecook.py --token=<STUDIOAPITOKEN> --channeldir='./content/exercises-csv-channel-root'

If you get an error when running the linecook script (in the end), you have to
change the channel Source ID column in `Channel.csv`, or ask the LE team to
make you an editor for the channel with this source id.

This above commands will create or update the channel on Kolibri Studio. As part
of the upload process, the file `chefdata/trees/ricecooker_json_tree.json` will
be created, which shows the exact metadata that was uploaded to Kolibri Studio.
You can use this file to debug problems like missing descriptions, bad formats, etc.




Metadata details
----------------

### Topic structure
The structure of the channel is determined by the folder structure under the
directory `content/exercises-csv-channel-root`:

    content
    └── exercises-csv-channel-root
        ├── mathexercises             # an empty folder to put exercises in
        └── physicsexercises          # an empty folder to put exercises in

The folders `mathexercises` and `physicsexercises` will correspond to two topic
nodes inside the final channel. The metadata for these topic nodes is provided
in the file `Content.csv` (to be described below).



### Channel metadata
Channel metadata must be provided the file `Channel.csv` which should live next
to the channel root folder. The channel metadata fields are:
  - `Title`: The name of the channel as it will shown to users.
  - `Description`: Channel description used by curators when looking through channels.
  - `Domain`: The domain of the organization providing the content, e.g. `learningequality.org`
  - `Source ID`: A unique machine-readable identifier for this channel within domain, e.g., `eduvideos`
  - `Language`: A two-letter or three-letter code used by Kolibri for language
     representation: [see full list here](https://github.com/learningequality/le-utils/blob/master/le_utils/resources/languagelookup.json).
  - `Thumbnail`: path to a thumbnail file for the channel (will be displayed when browsing channels, optional)

### Content metadata
For each file or folder in the folder structure, an appropriate metadata entry
must be provided in the file `Content.csv`:
  - `Path *`: The full path of a file or directory, starting with the root directory for the channel.
  - `Title *`: The title of the folder or content node that will be shown to users.
  - `Source ID`: The unique identifier used on source website or DB (optional)
    Set this to the primary key for the content item if the content comes from a
    database, or a unique path segment or slug if we content comes from a website.
  - `Description`: Content item and folder descriptions to be displayed to users.
  - `Author`: The author of the content (optional)
  - `Language`: A two-letter or three-letter code used by Kolibri for language
     representation: [see full list here](https://github.com/learningequality/le-utils/blob/master/le_utils/resources/languagelookup.json).
  - `License ID *`: This column indicates the license type and is required for all
    content items (files). License ID must one of the following: `CC BY`, `CC BY-SA`,
    `CC BY-ND`, `CC BY-NC`, `CC BY-NC-SA`, `CC BY-NC-ND`, `All Rights Reserved`,
    `Public Domain`, or `Special Permissions`.
    If the `Special Permissions` key is used, the details of the license information
    must be provided in the column `License Description`, else the column `License Description`
    can be left blank.
  - `Copyright Holder`: specifies the copyright holder for content items.
    This field is required for all licenses except `Public Domain`.
  - `Thumbnail`: path to thumbnail image for the content item or folder (optional)


### Exercise metadata
The contents of `Exercises.csv` is similar to the metadata for content nodes,
but there are additional fields:
  - `Path *`: The full path of a file, starting with the root directory for the channel.
     **Note: no file should exist in that place.** The `Path *` is used just
     to determine where the exercise appear in the tree, and the sort order.
  - `Title *`: The title of the exercise that will be shown to users.
  - `Source ID *`: The unique identifier for this exercise. This key is important
     because exercises questions will refer to exercises by their source id.
  - `Description`: Exercise description to be displayed to users.
  - `Author`: The author of the exercise (optional)
  - `Language`: A two-letter or three-letter code used by Kolibri for language
     representation: [see full list here](https://github.com/learningequality/le-utils/blob/master/le_utils/resources/languagelookup.json).
  - `License ID *`: This column indicates the license type and is required for all
    content items (files). License ID must one of the following: `CC BY`, `CC BY-SA`,
    `CC BY-ND`, `CC BY-NC`, `CC BY-NC-SA`, `CC BY-NC-ND`, `All Rights Reserved`,
    `Public Domain`, or `Special Permissions`.
    If the `Special Permissions` key is used, the details of the license information
    must be provided in the column `License Description`, else the column `License Description`
    can be left blank.
  - `Copyright Holder`: specifies the copyright holder for content items.
    This field is required for all licenses except `Public Domain`.
  - `Number Correct` (integer): how many a student needs to get right in a row to achieve mastery.
  - `Out of Total` (integer): how many questions total will be presented in a sequence in the exercise.
  - `Randomize` (boolean): Use `TRUE` (default) to make question within the exercise appear in random order
    or `FALSE` to make the questions appear in fixed order.
  - `Thumbnail`: path to thumbnail image for the content item or folder (optional)


### Exercise questions
Individual exercise questions (assessment items) must be provided in `ExerciseQuestions.csv`
in the following format:
  - `Source ID *`: The unique identifier for this exercise this question is part of.
  - `Question ID *`: a unique identifier for this question
  - `Question type *`: one of `single_selection`, `multiple_selection`, `input_question` (the tree supported types).
    If you want to create a true-false question, use `single_selection` with two answers.
  - `Question *`: string that contains the question setup and the prompt
  - `Option A`: the first answer option that will be shown (`single_selection` and `multiple_selection` only)
  - `Option B`: the second answer option that will be shown (`single_selection` and `multiple_selection` only)
  - `Option C`: the third answer option that will be shown (`single_selection` and `multiple_selection` only)
  - `Option D`: the fourth answer option that will be shown (`single_selection` and `multiple_selection` only)
  - `Option E`: the fifth answer option that will be shown (`single_selection` and `multiple_selection` only)
  - `Option F..`: special extended field to use when six or more options are required.
    This field can contain a list of multiple '🍣'-separated string values,
    e.g.,   `Anser F🍣Answer G🍣Answer H`.
  - `Correct Answer *`: A string that corresponds to the correct answer.
    For `single_selection` the string must match **exactly** one of the answer options.
  - `Correct Answer 2`: another correct answer for `multiple_selection`
  - `Correct Answer 3`: a third correct answer for `multiple_selection`
  - `Hint 1`, `Hint 2`, ..., `Hint 5`: hints to be provided to learners (optional)
  - `Hint 6+`: this field can contain a list of multiple '🍣'-separated string values,
     e.g., `Hint 6 text🍣Hint 7 text🍣Hing 8 text` in cases where more than 6 hints are required.


### Exercise figures and LaTeX math
Exercise questions and answer option columns can include images using the standard
markdown syntax for including images: `![](path/to/some/image.png)`.

It is also possible to include math expressions using the LaTeX-syntax supported
by the KaTeX engine, see https://katex.org/. Use the dollar-sign delimiter to 
denote the beginning and end of a math expression, example `$x^2=4$`.



### Overview
Putting all of the above together, the combined info about structure, metadata,
and exercise figures should look like this:

    linecook.py                         # the script that will be used to upload
                                        # the channel to Kolibri Studio
    content/
    ├── exercises-csv-channel-root      # folder which represents the root of the channel
    │   ├── mathexercises               # an empty folder to put exercises in
    │   └── physicsexercises            # an empty folder to put exercises in
    │
    ├── Channel.csv                     # channel metadata
    ├── Content.csv                     # metadata for topics and content nodes
    ├── Exercises.csv                   # metadata for exercise nodes
    └── ExerciseQuestions.csv           # questions content

    figures/                            # A separate folder for exercise images.
    ├── exrc3                           # Files here can be organized in any way
    │   └── circle-of-radius-2.png      # and the structure doesn't make any difference
    └── exrc5                           # the example shown on the left uses the
        ├── hexagon.png                 # exercise `Source ID *` key to groupd
        ├── octagon.png                 # the individual files so you know which
        ├── ...                         # figure corresponds to which exercise
        └── triangle5.png               # but any other structure would be OK.

Important notes:
  - The CSV metadata files are placed in the same directory as `exercises-csv-channel-root`.
    This is important since the script will look for the metadata files in this
    exact location (assume CSV files are siblings of the channel root directory).
  - The `mathexercises` and `physicsexercises` are empty folders. Do not put
    any files in these folders or the script will not function properly. These
    folders server as placeholders for the channel structure so we have somewhere
    to "attach" the exercises.
  - The `figures/` directory is completely separated from the `content/` dir.
    To include the figure `hexagon.png` in an exercise, use the markdown syntax
    `![](figures/exrc5/hexagon.png)` which uses the path relative to the directory
    where the script `linecook.py` will be run in (the current working directory).
  - Exercise figures must be appropriately sized to work well in Kolibri (not too large).
