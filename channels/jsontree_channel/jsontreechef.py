#!/usr/bin/env python
import logging

from le_utils.constants import content_kinds, file_types, exercises, licenses
from ricecooker.chefs import JsonTreeChef
from ricecooker.classes.licenses import get_license
from le_utils.constants.languages import getlang  # see also getlang_by_name, getlang_by_alpha2
from ricecooker.config import LOGGER
from ricecooker.utils.jsontrees import write_tree_to_json_tree


# LOGGING SETTINGS
################################################################################
logging.getLogger("cachecontrol.controller").setLevel(logging.WARNING)
logging.getLogger("requests.packages").setLevel(logging.WARNING)
LOGGER.setLevel(logging.DEBUG)


# CSV SAMPLE CHANNEL LINE COOK
################################################################################

class SampleJsonTreeChef(JsonTreeChef):
    """
    This sushi chef example uses "ricecooker json" as an intermediary format for
    creting the channel tree structure. The format for the json metadata is the
    same as for the Python classes. Indicate content node but instead of 
    """
    RICECOOKER_JSON_TREE = 'sample_ricecooker_json_tree.json'
    # no custom methods needed: uses generic `JsonTreeChef` main and run methods

    def pre_run(self, args, options):
        """
        Build the ricecooker json tree for the channel.
        The code here is similar to the code in `ricecooker_channel/chef.py`, but
        the channel hiearachy is build using dictionary objects instead of classes.
        """
        LOGGER.info('In pre_run...')

        # 1. Create the channel tree
        ricecooker_json_tree = dict(
            title='Sample JSON channel',
            source_domain='source.org',
            source_id='sample-json-channel',
            description='This channel was created from the files in the content/ ' \
                + 'directory and the metadata in sample_ricecooker_json_tree.json',
            thumbnail='./content/sample-json-channel-files/channel_thumbnail.jpg',
            language='en',
            children=[],
        )
        # The root object of the ricecooker json tree contains the channel info;
        # add topic and content nodes and to the children list to build the tree.

        # 2. Add topics nodes and content nodes as to the tree
        self.create_content_nodes(ricecooker_json_tree)
        self.create_exercise_nodes(ricecooker_json_tree)
        
        # 3. Save the tree to chefdata/trees/sample_ricecooker_json_tree.json
        json_tree_path = self.get_json_tree_path()
        write_tree_to_json_tree(json_tree_path, ricecooker_json_tree)
        LOGGER.info('Finished writing ricecooker json tree.')


    def create_content_nodes(self, ricecooker_json_tree):
        """
        This function build the hierarchy of topic and content nodes dicts by
        appending to the `children` attribute of the `ricecooker_json_tree` (dict).
        """
        content_nodes_folder = dict(
            kind=content_kinds.TOPIC,
            source_id='121232ms',
            title='Content Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').code,
            thumbnail=None,
            children=[],
        )
        ricecooker_json_tree['children'].append(content_nodes_folder)

        # AUDIO FOLDER
        audio_nodes_folder = dict(
            kind=content_kinds.TOPIC,
            source_id='138iuh23iu',
            title='Audio Files',
            description='Put folder description here',
            author=None,
            language=getlang('en').code,
            thumbnail=None,
            children=[],
        )
        content_nodes_folder['children'].append(audio_nodes_folder)

        # First content node metadata...
        audio_node = dict(
            kind=content_kinds.AUDIO,
            source_id='940ac8ff',
            title='Whale sounds',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            thumbnail=None,
            files=[],
        )
        audio_nodes_folder['children'].append(audio_node)
        # ...then add the file for this content node:
        audio_file = dict(
            file_type=file_types.AUDIO,
            path='./content/sample-json-channel-files/Whale_sounds.mp3',
            language=getlang('en').code
        )
        audio_node['files'].append(audio_file)


        # DOCUMENTS
        documents_folder = dict(
            kind=content_kinds.TOPIC,
            source_id='asanlksnaklsn',
            title='Document Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').code,
            thumbnail=None,
            children=[],
        )
        content_nodes_folder['children'].append(documents_folder)

        document_node = dict(
            kind=content_kinds.DOCUMENT,
            source_id='80b7136f',
            title='The Supreme Court\u2019s Ruling in Brown vs. Board of Education',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            thumbnail=None,
            files=[dict(
                     file_type=file_types.DOCUMENT,
                     path='./content/sample-json-channel-files/commonlit_the-supreme-court-s-ruling-in-brown-vs-board-of-education_student.pdf',
                     language=getlang('en').code
                )]
        )
        documents_folder['children'].append(document_node)


        # HTML5 APPS
        html5apps_folder = dict(
            kind=content_kinds.TOPIC,
            source_id='asasa331',
            title='HTML5App Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').code,
            thumbnail=None,
            children=[],
        )
        content_nodes_folder['children'].append(html5apps_folder)

        html5_node_a = dict(
            kind=content_kinds.HTML5,
            source_id='302723b4',
            title='Sample React app',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            thumbnail='./content/sample-json-channel-files/html5_react.jpg',
            files=[dict(
                      file_type=file_types.HTML5,
                      path='./content/sample-json-channel-files/html5_react.zip',
                      language=getlang('en').code
                 )]
        )
        html5apps_folder['children'].append(html5_node_a)

        html5_node_b = dict(
            kind=content_kinds.HTML5,
            source_id='3f91184e',
            title='Sample Vue.js app',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            thumbnail='./content/sample-json-channel-files/html5_vuejs.jpg',
            files=[dict(
                      file_type=file_types.HTML5,
                      path='./content/sample-json-channel-files/html5_vuejs.zip',
                      language=getlang('en').code
                 )]
        )
        html5apps_folder['children'].append(html5_node_b)

        html5_node_c = dict(
            kind=content_kinds.HTML5,
            source_id='0aec4296',
            title='Sample wget-scraped web content',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            thumbnail='./content/sample-json-channel-files/html5_wget_scraped.jpg',
            files=[dict(
                      file_type=file_types.HTML5,
                      path='./content/sample-json-channel-files/html5_wget_scraped.zip',
                      language=getlang('en').code
                 )]
        )
        html5apps_folder['children'].append(html5_node_c)


        # VIDEOS
        videos_folder = dict(
            kind=content_kinds.TOPIC,
            source_id='121213m3m3',
            title='Video Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').code,
            thumbnail=None,
            children=[],
        )
        content_nodes_folder['children'].append(videos_folder)
        video_node = dict(
            kind=content_kinds.VIDEO,
            source_id='9e355995',
            title='Wave particle duality explained in 2 mins',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            derive_thumbnail=True,  # video-specicig flag
            thumbnail=None,
            files=[dict(
                     file_type=file_types.VIDEO,
                     path='./content/sample-json-channel-files/Wave_particle_duality.mp4',
                     language=getlang('en').code
                   )]
        )
        videos_folder['children'].append(video_node)



    def create_exercise_nodes(self, ricecooker_json_tree):
        """
        This function adds an exercise node to the channel content tree.
        """

        # EXERCISES
        exercices_folder = dict(
            kind=content_kinds.TOPIC,
            source_id='mdmdmai3i13',
            title='Exercise Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').code,
            thumbnail=None,
            children=[],
        )
        ricecooker_json_tree['children'].append(exercices_folder)

        exercise2a = dict(
            kind=content_kinds.EXERCISE,
            source_id='asisis9',
            title='Basic questions',
            author='LE content team',
            description='Showcase of the simple exercises supported by Ricecooker and Studio',
            language=getlang('en').code,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name').as_dict(),
            thumbnail=None,
            exercise_data={
                'mastery_model': exercises.M_OF_N,         # or exercises.DO_ALL
                'randomize': True,
                'm': 2,
                'n': 3,
            },
            questions=[
                dict(
                    question_type=exercises.MULTIPLE_SELECTION,
                    id='ex2aQ1',
                    question = "Which numbers are even?",
                    correct_answers = ["2", "4",],
                    all_answers = ["1", "2", "3", "4", "5"],
                    # hints?
                ),
                dict(
                    question_type=exercises.SINGLE_SELECTION,
                    id='ex2aQ2',
                    question = "What is 2 times 3?",
                    correct_answer = "6",
                    all_answers = ["2", "3", "5", "6"],
                    # hints?
                ),
                dict(
                    question_type=exercises.INPUT_QUESTION,
                    id='ex2aQ3',
                    question = "Name a factor of 10.",
                    answers = ["1", "2", "5", "10"],
                    # hints?
                )
            ]
        )
        exercices_folder['children'].append(exercise2a)



# CLI
################################################################################

if __name__ == '__main__':
    chef = SampleJsonTreeChef()
    chef.main()
