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




Further reading
===============

To learn more about the Kolibri Content Platform, see the 
[ricecooker docs](https://github.com/learningequality/ricecooker/tree/master/docs).

