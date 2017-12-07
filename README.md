Sample Kolibri Channels
=======================

Showcase for the different content types currently supported by the Kolibri platform,
and sample code that shows the different methods for uploading content into Kolibri Studio.


Links
-----

  - Quickstart: https://github.com/learningequality/ricecooker/blob/master/docs/tutorial/quickstart.ipynb
  - Ricecooker README: https://github.com/learningequality/ricecooker/blob/master/README.md
  - Ricecooker docs: https://github.com/learningequality/ricecooker/tree/master/docs
  - Tutorial: https://docs.google.com/document/d/1iiwce8B_AyJ2d6K8dYBl66n9zjz0zQ3G4gTrubdk9ws/edit
  - [sample channels](./channels)  
  - [sample content types](./contentnodes)



Technical Summary
-----------------

The following options are available for importing content into Kolibri Studio:
  - Manual upload of content through the studio web interface
     - GOOD FOR: one off tests,
     - BAD FOR: large channels, channels that need to be updated regularly
  - Studio low level internal API (**not recommended**, use `ricecooker` instead)
  - Ricecooker interfaces, based on the [`ricecooker`](https://github.com/learningequality/ricecooker) library:
      - CSV interface, see [channels/csv_channel](./channels/csv_channel):
         - GOOD FOR: quick prototypes, non-technical project lead (no need for code, use Excel to prepare CSVs)
         - BAD FOR: large channels, channels that need to be updated regularly
      - JSON tree interface, see [channels/jsontree_channel](./channels/jsontree_channel):
         - GOOD FOR: if content structure can be generated from existing code in other languages (e.g. ruby/js)
      - Python interface, see [channels/ricecooker_channel](./channels/ricecooker_channel):
         - GOOD FOR: most control and extensibility



Install
-------
1. Clone this repository and go into it, then run:

       virtualenv -p python3  venv
       source venv/bin/activate
       pip install -r requirements.txt

2. Crete an account on [Kolibri Studio](http://studio.learningequality.org/)
   and save your access token to the file `credentials/studiotoken.txt` (on a single line)

3. Follow the instructions in the README.md files in each sample channel directory.




Extra notes on supported content types
======================================

(these notes which will soon be merged into [main docs](https://github.com/learningequality/ricecooker/tree/master/docs).)


Exercises
---------
Kolibri exercises are based on the `perseus` exercise framework developed by Khan Academy.
Perseus provides a free-form interface for questions based on various "widgets" buttons,
draggables, expressions, etc. This is the native format for exercises on Kolibri.
An exercise question item is represented as a giant json file, with the main question
field stored as Markdown. Widgets are included in the "main" through a unique-Unicode
character and then widget metadata is stored separately as part of the json data.

Exercises can be created programmatically or interactively using the perseus editor through the web: [http://khan.github.io/perseus/](http://khan.github.io/perseus/)
(try adding different widgets in the Question area and then click the JSON Mode
checkbox to "view source" for the exercise.

You can then copy-paste the results as a .json file and import into Kolibri using ricecooker library (Python).

Sample: [https://github.com/learningequality/sample-channels/blob/master/contentnodes/exercise/sample_perseus04.json](https://github.com/learningequality/sample-channels/blob/master/contentnodes/exercise/sample_perseus04.json)  


Kolibri Studio provides helper classes for creating single/multiple-select questions, and numeric input questions:
[https://github.com/learningequality/ricecooker/blob/master/docs/exercises.md](https://github.com/learningequality/ricecooker/blob/master/docs/exercises.md)

A simple multiple choice (single select) question can be created as follows:

    SingleSelectQuestion(
        question = "What was the main idea in the passage you just read?",
        correct_answer = "The right answer",
        all_answers = ["The right answer", "Another option", "Nope, not this"]
        ...


Exercise activities allow student answers to be logged and enable progress reports
for teachers and coaches. Exercises can also be used as part of individual assignments
(playlist-like thing with a mix of content and exercises), group assignments, and exams.




HTML5Apps
---------
The most versatile and extensible option for importing content into Kolibri is to
package the content as HTML5App nodes. The HTML5 content type on Kolibri, consists
of a zip file with web content inside it. The Kolibri application serves the file
`index.html` from the root of the zip folder inside an iframe. It is possible to
package any web content in this manner: text, images, CSS, fonts, and JavaScript code.
The `iframe` rendering the content in Kolibri is sandbox so no plugins are allowed (no swf/flash).
In addition, it is expected that oh web resources are stored within the zip file,
and referenced using relative paths. This is what enables Kolibri to used in offline settings.  


Here are some samples:

  - [Sample Vue.js App](contentnodes/html5_vuejs): Proof of concept of minimal
    webapp based on the vue.js framework. Note the [shell script](contentnodes/html5_vuejs/update.sh)
    tweaks the output a little to make references local paths.

  - [Sample React App](contentnodes/html5_react): Proof of concept of minimal
    webapp based on the React framework.
    Note the [shell script](contentnodes/html5_react/update.sh) tweaks.



Extending Kolibri
-----------------
New content types and presentation modalities will become available and supported
natively by future version of Kolibri. The Kolibri software architecture is based
around the plug-in system that is easy to extend. All currently supported content
type renderers are based on this plug-in architecture. It might be possible to create
a Kolibri plugin for rendering specific content in custom ways.


