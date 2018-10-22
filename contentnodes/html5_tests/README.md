Web capabilities test
=====================
This HTML/JS/CSS content serves as the testing ground for the capabilities allowed 
and disallowed by the sandboxed iframe used to render HTML5App nodes on Kolibri.

  - The dir `webroot` contains the files that will be packaged as part of the HTML5Zip.
  - The file `kolibri.html` can be used to test locally:
    - Clone the `serving_up_iframes` branch from here:
       https://github.com/kollivier/ricecooker/tree/serving_up_iframes
    - Run `python /Users/ivan/Projects/FLECode/ricecooker/preview.py  --iframe .`
    - Navigate to http://127.0.0.1:8282/kolibri.html
  - Use `update.sh` to rebuild the webroot.zip if you make changes.
  - Check the `ricecooker_channel` chef to see how this is used.


See the result on Kolibri demo here: http://35.196.115.213/learn/#/topics/c/5f522e58754c5eb397dfa7df6b7f10eb

