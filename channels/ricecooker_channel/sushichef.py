#!/usr/bin/env python

from le_utils.constants import licenses, exercises
from le_utils.constants.languages import getlang  # see also getlang_by_name, getlang_by_alpha2
from pressurecooker.youtube import YouTubeResource, is_youtube_subtitle_file_supported_language

from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import TopicNode

from ricecooker.classes.nodes import DocumentNode, AudioNode, VideoNode, HTML5AppNode
from ricecooker.classes.files import DocumentFile, AudioFile, VideoFile, YouTubeVideoFile, YouTubeSubtitleFile, HTMLZipFile

from ricecooker.classes.nodes import ExerciseNode
from ricecooker.classes.questions import SingleSelectQuestion, MultipleSelectQuestion, InputQuestion, PerseusQuestion

from ricecooker.classes.licenses import get_license
from ricecooker.exceptions import raise_for_invalid_channel

from ricecooker.config import LOGGER
import logging
LOGGER.setLevel(logging.INFO)



class SampleChef(SushiChef):
    """
    The chef class that takes care of uploading channel to Kolibri Studio.
    We'll call its `main()` method from the command line script.
    """

    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'source.org',                  # content provider's domain
        'CHANNEL_SOURCE_ID': 'sample-ricecooker-channel',       # an alphanumeric channel ID
        'CHANNEL_TITLE': 'Sample Ricecooker Channel',           # a humand-readbale title
        'CHANNEL_LANGUAGE': getlang('en').id,                   # language code of channel
        'CHANNEL_THUMBNAIL': 'http://quantlabs.net/blog/wp-content/uploads/2015/11/pythonlogo.jpg', # (optional) local path or url to image file
        'CHANNEL_DESCRIPTION': 'This channel was created from the files in the ' 
                               'content/ dir and metadata specified in Python'
    }


    def construct_channel(self, *args, **kwargs):
        """
        Create ChannelNode and build topic tree.
        """
        channel = self.get_channel(*args, **kwargs)   # create ChannelNode from data in self.channel_info
        self.create_content_nodes(channel)
        self.create_exercise_nodes(channel)
        raise_for_invalid_channel(channel)
        return channel


    def create_content_nodes(self, channel):
        """
        This function uses the methods `add_child` and `add_file` to build the
        hierarchy of topic nodes (nested folder structure) and content nodes.
        Every content node is associated with one or more files.
        """
        content_nodes_folder = TopicNode(
            source_id='uniqid001',
            title='Content Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        channel.add_child(content_nodes_folder)

        # AUDIO
        audio_nodes_folder = TopicNode(
            source_id='uniqid002',
            title='Audio Files Folder',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        content_nodes_folder.add_child(audio_nodes_folder)

        audio_node = AudioNode(
            source_id='uniqid003',
            title='Whale sounds',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail=None,
            files=[],
        )
        audio_nodes_folder.add_child(audio_node)
        audio_file = AudioFile(
            path='./content/ricecooker-channel-files/Whale_sounds.mp3',  # note path can also be a URL
            language=getlang('en').id
        )
        audio_node.add_file(audio_file)


        # DOCUMENTS
        documents_folder = TopicNode(
            source_id='uniqid004',
            title='Document Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        content_nodes_folder.add_child(documents_folder)

        document_node = DocumentNode(
            source_id='uniqid005',
            title='The Supreme Court\u2019s Ruling in Brown vs. Board of Education',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail=None,
            files=[DocumentFile(
                        path='./content/ricecooker-channel-files/brown-vs-board-of-education.pdf',
                        language=getlang('en').id
                )]
        )
        documents_folder.add_child(document_node)


        # HTML5 APPS
        html5apps_folder = TopicNode(
            source_id='uniqid006',
            title='HTML5App Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        content_nodes_folder.add_child(html5apps_folder)


        html5_node = HTML5AppNode(
            source_id='uniqid007',
            title='HTMLWeb capabilities test',
            author='First Last (author\'s name)',
            description='Tests different HTML/JS capabilities. What capabilities are allowed and disallowed by the sandboxed iframe used to render HTML5App nodes on Kolibri.',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail='./content/ricecooker-channel-files/html5_tests.jpg',
            files=[HTMLZipFile(
                      path='./content/ricecooker-channel-files/html5_tests.zip',
                      language=getlang('en').id
                 )]
        )
        html5apps_folder.add_child(html5_node)

        html5_node2 = HTML5AppNode(
            source_id='uniqid008',
            title='Sample Vue.js app',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail='./content/ricecooker-channel-files/html5_vuejs.jpg',
            files=[HTMLZipFile(
                      path='./content/ricecooker-channel-files/html5_vuejs.zip',
                      language=getlang('en').id
                 )]
        )
        html5apps_folder.add_child(html5_node2)


        # VIDEOS
        videos_folder = TopicNode(
            source_id='uniqid009',
            title='Video Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        content_nodes_folder.add_child(videos_folder)
        video_node = VideoNode(
            source_id='uniqid010',
            title='Wave particle duality explained in 2 mins',
            author='First Last (author\'s name)',
            description='Put file description here',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            derive_thumbnail=True,  # video-specicig flag
            thumbnail=None,
            files=[VideoFile(
                        path='./content/ricecooker-channel-files/Wave_particle_duality.mp4',
                        language=getlang('en').id
                   )]
        )
        videos_folder.add_child(video_node)

        youtube_id='VJyk81HmcZQ'
        video_node2 = VideoNode(
            source_id=youtube_id,  # usually set source_id to youtube_id
            title='Estimating division that results in non whole numbers',
            author='Sal Khan',
            description='Video description would go here',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Khan Academy'),
            derive_thumbnail=True,  # video-specicig flag
            thumbnail=None,
            files=[
                YouTubeVideoFile(youtube_id=youtube_id, high_resolution=False, language='en'),
                YouTubeSubtitleFile(youtube_id=youtube_id, language='ko')
            ]
        )
        videos_folder.add_child(video_node2)



    def create_exercise_nodes(self, channel):
        """
        This function adds a few exercise nodes to the channel content tree.
        TODO: handle exercises with embedded image links + base64 encoded data.
        """

        # EXERCISES
        exercices_folder = TopicNode(
            source_id='uniqid011',
            title='Exercise Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        channel.add_child(exercices_folder)

        exercise1 = ExerciseNode(
            source_id='uniqid012',
            title='Basic questions',
            author='LE content team',
            description='Showcase of the simple exercises supported by Ricecooker and Studio',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail=None,
            exercise_data={
                'mastery_model': exercises.M_OF_N,         # or exercises.DO_ALL
                'randomize': True,
                'm': 2,
                'n': 3,
            },
            questions=[
                MultipleSelectQuestion(
                        id='ex2aQ1',
                        question = "Which numbers are even?\n\nTest local image include: ![](content/ricecooker-channel-files/html5_vuejs.jpg)",
                        correct_answers = ["2", "4",],
                        all_answers = ["1", "2", "3", "4", "5"],
                        hints = ["There are two answers.", "Both answers are multiples of two."]
                ),
                SingleSelectQuestion(
                        id='ex2aQ2',
                        question = "What is 2 times 3?",
                        correct_answer = "6",
                        all_answers = ["2", "3", "5", "6"],
                ),
                InputQuestion(
                        id='ex2aQ3',
                        question = "Name a factor of 10.",
                        answers = ["1", "2", "5", "10"],
                )
            ]
        )
        exercices_folder.add_child(exercise1)

        # LOAD JSON DATA (as string) FOR PERSEUS QUESTIONS
        SAMPLE_PERSEUS_4_JSON = open('./content/ricecooker-channel-files/perseus_graph_question.json','r').read()
        exercise2 = ExerciseNode(
            source_id='baszzzs1',
            title='Perseus questions',
            author='LE content team',
            description='An example exercise with Persus questions',
            language=getlang('en').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail=None,
            exercise_data={
                'mastery_model': exercises.M_OF_N,         # or exercises.DO_ALL
                'randomize': True,
                'm': 1,
                'n': 1,
            },
            questions=[
                PerseusQuestion(
                        id='ex2bQ4',
                        raw_data=SAMPLE_PERSEUS_4_JSON,
                        source_url='https://github.com/learningequality/sample-channels/blob/master/contentnodes/exercise/sample_perseus04.json'
                ),
            ]
        )
        exercices_folder.add_child(exercise2)



if __name__ == '__main__':
    """
    This code will run when the sushi chef scripy is called on the command line.
    """
    chef = SampleChef()
    chef.main()

