#!/usr/bin/env python

from le_utils.constants import format_presets, licenses, exercises
from le_utils.constants.languages import getlang  # see also getlang_by_name, getlang_by_alpha2
from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import TopicNode

from ricecooker.classes.nodes import DocumentNode, AudioNode, VideoNode, HTML5AppNode
from ricecooker.classes.files import DocumentFile, AudioFile, VideoFile, HTMLZipFile

from ricecooker.classes.nodes import ExerciseNode
from ricecooker.classes.questions import SingleSelectQuestion, MultipleSelectQuestion, InputQuestion, PerseusQuestion

from ricecooker.classes.licenses import get_license
from ricecooker.exceptions import raise_for_invalid_channel

from ricecooker.config import LOGGER
import logging
LOGGER.setLevel(logging.INFO)



class ContentNodeDependencyChef(SushiChef):
    """
    The chef class that takes care of uploading channel to Kolibri Studio.
    We'll call its `main()` method from the command line script.
    """

    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'learningequality.org',                  # content provider's domain
        'CHANNEL_SOURCE_ID': 'content-node-dependency-test',       # an alphanumeric channel ID
        'CHANNEL_TITLE': 'ContentNode Dependency Test Channel', # a humand-readbale title
        'CHANNEL_LANGUAGE': getlang('en').id,                   # language code of channel
        'CHANNEL_THUMBNAIL': 'https://s3-us-west-2.amazonaws.com/testdrivenlearningbucket/htmlcss.jpg', # (optional) local path or url to image file
        'CHANNEL_DESCRIPTION': 'Test if content node dependecies work given iframe sandboxing'
    }


    def construct_channel(self, *args, **kwargs):
        """
        Create ChannelNode and build topic tree.
        """
        channel = self.get_channel(*args, **kwargs)   # create ChannelNode from data in self.channel_info

        topic1 = TopicNode(
                source_id='121232ms',
                title='Content Nodes',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        channel.add_child(topic1)

        # HTML5 APPS
        topic13 = TopicNode(
                source_id='asasa331',
                title='HTML5App Nodes',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        topic1.add_child(topic13)

        content13a = HTML5AppNode(
              source_id='302723b4',
              title='Shared Zip File app',
              author='First Last (author\'s name)',
              description='Put file description here',
              language=getlang('en').id,
              license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
              thumbnail=None,
              files=[HTMLZipFile(
                          path='./content/zipfiles/shared.zip',
                          language=getlang('en').id
                     )]
        )
        topic13.add_child(content13a)

        raise_for_invalid_channel(channel)
        return channel


if __name__ == '__main__':
    """
    This code will run when the sushi chef scripy is called on the command line.
    """
    chef = ContentNodeDependencyChef()
    chef.main()
