#!/usr/bin/env python

from le_utils.constants import licenses
from le_utils.constants.languages import getlang  # see also getlang_by_name, getlang_by_alpha2
from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import TopicNode
from ricecooker.classes.nodes import VideoNode
from ricecooker.classes.files import VideoFile
from ricecooker.classes.licenses import get_license
from ricecooker.exceptions import raise_for_invalid_channel


# A sampling of videos from the Sikana channel
VIDEO_URLS = [
    'http://studio.learningequality.org/content/storage/c/0/c0f2f4321a7c60516db965cc742d9f24.mp4',
    'http://studio.learningequality.org/content/storage/0/d/0d66de8a1b365d7e414a6e2ea02dc601.mp4',
    'http://studio.learningequality.org/content/storage/a/a/aa207693b4be610d3c094ce2bdf9f198.mp4',
    'http://studio.learningequality.org/content/storage/4/f/4f10c57ea0da164b2bf3618823788106.mp4',
]

CRF_CHOICES = [24, 28, 32]


def make_video_node(title, video_url, video_language='en', ffmpeg_settings=None):
    """
    Create a VideoNode from video_url. Assumes title is unique within containin topic.
    """
    content_node = VideoNode(
            source_id=title,
            title=title,
            author='Sikana',
            description='',
            language=getlang(video_language).id,
            license=get_license(licenses.CC_BY_NC_ND, copyright_holder='Sikana Education'),
            thumbnail=None,
            derive_thumbnail=True,
            files=[VideoFile(
                        path=video_url,
                        language=getlang(video_language).id,
                        ffmpeg_settings=ffmpeg_settings,
                   )]
    )
    return content_node

def make_topic_for_settings(title, ffmpeg_settings):
    """
    Assumes global VIDEO_URLS available.
    """
    topic = TopicNode(
            source_id=title,
            title=title,
            description='',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
    )
    for counter, video_url in enumerate(VIDEO_URLS):
        vid_number = counter+1
        video_title = 'Video ' + str(vid_number)
        video_node = make_video_node(video_title, video_url,ffmpeg_settings=ffmpeg_settings)
        topic.add_child(video_node)
    return topic
        


class SikanaVideoCompressionTestChef(SushiChef):
    """
    The chef creates a test channel of Sikana videos with different compression
    settings in order to help with research on video playback performance.
     - A. Original videos form current Sikana channel (vres=720, ~10MB/min)
     - B. Re-encoded with different CRF factors: 24, 28, 32
     - C. Re-encode to 854x480 and different CRFs
    """

    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'sikana.tv',                  # content provider's domain
        'CHANNEL_SOURCE_ID': 'sikana-video-compression-test',       # an alphanumeric channel ID
        'CHANNEL_TITLE': 'Sikana Video Compression Test Channel',           # a humand-readbale title
        'CHANNEL_LANGUAGE': getlang('en').id,                   # language code of channel
        'CHANNEL_THUMBNAIL': 'http://riendeneuf.org/wp-content/uploads/2017/12/sikana.png',
        'CHANNEL_DESCRIPTION': """test channel of Sikana videos with different compression
            settings in order to help with research on video playback performance.
             - A. Original videos form current Sikana channel (vres=720, ~10MB/min)
             - B. Re-encoded with different CRF factors: 24, 28, 32
             - C. Re-encode to 854x480 and different CRFs"""
    }


    def construct_channel(self, *args, **kwargs):
        """
        Create ChannelNode and build topic tree.
        """
        channel = self.get_channel(*args, **kwargs)   # create ChannelNode from data in self.channel_info
        self.create_video_subfolders(channel)
        raise_for_invalid_channel(channel)
        return channel


    def create_video_subfolders(self, channel):
        """
        Create subfolders for each A/B/C scnarios.
        """
        
        # A: Original videos
        orig = make_topic_for_settings('A: Original videos', ffmpeg_settings=None)
        channel.add_child(orig)
        
        # B: Compressed videos
        for crf in CRF_CHOICES:
            topic_title = 'B' + str(crf) + ': Compressed with crf=' + str(crf)
            b_topic = make_topic_for_settings(topic_title, ffmpeg_settings={'crf': crf})
            channel.add_child(b_topic)
        

        # C: Resized and compressed videos
        for crf in CRF_CHOICES:
            topic_title = 'C' + str(crf) + ': Resized to 480vert and compressed with crf=' + str(crf)
            c_topic = make_topic_for_settings(topic_title, ffmpeg_settings={'crf': crf, 'max_height': 480})
            channel.add_child(c_topic)




if __name__ == '__main__':
    """
    This code will run when the sushi chef scripy is called on the command line.
    """
    chef = SikanaVideoCompressionTestChef()
    chef.main()

