Sample Kolibri Channels
=======================

Showcase for the different content types currently supported by the Kolibri platform,
and sample code that shows the different methods for uploading content into Kolibri Studio.


Links
-----
  - Content Integration Guide: https://learningequality.org/r/integration-guide
  - Ricecooker docs: https://ricecooker.readthedocs.io/
  - [sample channels](./channels)
  - [sample content types](./contentnodes)


Technical Summary
-----------------
The following options are available for integrating content into Kolibri Studio:
  - Integration Method 1: manual content upload through the Studio web interface
     - USE FOR: small and medium size channels, upload files from your computer, maximum control of channel structure
     - NOT GOOD FOR: large channels or channels that need to be updated regularly
  -  Integration Method 2: Upload content using a content integration script based
     on the [`ricecooker`](https://github.com/learningequality/ricecooker) package:
      - Python interface, see [channels/ricecooker_channel](./channels/ricecooker_channel):
         - USE FOR: most channels, full control and extensibility throug Python scripts
      - CSV workflow, see [channels/csv_channel](./channels/csv_channel):
         - GOOD FOR: non-technical people (no need for coding; use Excel to metadata)



Install
-------
1. Clone this repository and go into it, then run:

       virtualenv -p python3  venv
       source venv/bin/activate
       pip install -r requirements.txt

2. Crete an account on [Kolibri Studio](http://studio.learningequality.org/)
   then obtain your Access Token from the [settings page](https://studio.learningequality.org/settings/tokens).

3. Follow the instructions in the `README.md` files of each sample channel.



Further reading
---------------
To learn more about content integration into the Kolibri ecosystem, read the
comprehensive [Content Integration Guide](https://learningequality.org/r/integration-guide)
while more technical details see the [Ricecooker Docs](https://ricecooker.readthedocs.io/).
