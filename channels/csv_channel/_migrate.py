#!/usr/bin/env python
"""
This script creats an archive with blank CSV metadata for all files in some folder.
NOT READY FOR PUBLIC CONSUMPTION --- JUST A TEMPORARY HACK TO MAKE CSV SAMPLE CHANNEL!!!
"""

import argparse
import os
from os.path import join
import sys
from ricecooker.utils import data_writer, path_builder, downloader, html_writer
from ricecooker.utils.linecook import FolderExistsAction
from le_utils.constants import licenses, languages, file_types
import uuid


THUMBNAIL_EXTS = [ext for (ext, fmt) in file_types.MAPPING.items() if fmt==file_types.THUMBNAIL]


# DEFAULTS to put in Channel.csv
################################################################################

CHANNEL_NAME = "Name of channel"
CHANNEL_DOMAIN = "source.org"
CHANNEL_SOURCE_ID = "sample-csv-channel"
CHANNEL_LANGUAGE = "en"      # Language of channel
CHANNEL_DESCRIPTION = "Description of the channel (optional)"
CHANNEL_THUMBNAIL = "Local path or url to image file (optional)"
PATH = path_builder.PathBuilder(channel_name=CHANNEL_NAME)  # Keeps track of path to write to csv
WRITE_TO_PATH = "{}{}{}.zip".format(                # Where to generate zip file
    os.path.dirname(os.path.realpath(__file__)),
    os.path.sep,
    CHANNEL_SOURCE_ID)

# DEFAULTS to put in  Content.csv
################################################################################
DEFAULT_FOLDER_DESCRIPTION = 'Put folder description here'
DEFAULT_FILE_DESCRIPTION = 'Put file description here'
DEFAULT_FILE_AUTHOR = 'First Last (author\'s name)'




# LINECOOK HELPER FUNCTIONS
################################################################################

def path_to_tuple(path, windows=False):
    """
    Used to split a `chan_path`
    """
    if windows:
        path_tup = tuple(path.split('\\'))
    else:
        path_tup = tuple(path.split('/'))
    return path_tup

def chan_path_from_rel_path(rel_path, channeldir):
    """
    Convert `rel_path` form os.walk tuple format to a tuple of directories and
    subdirectories, starting with the `channeldir` folder, e.g.,
    >>> chan_path_from_rel_path('content/open_stax_zip/Open Stax/Math/Elementary',
                               'content/open_stax_zip/Open Stax')
    'Open Stax/Math/Elementary'
    """
    rel_path_parts = rel_path.split(os.path.sep)
    dirs_before_channeldir = channeldir.split(os.path.sep)[:-1]
    channel_chan_path = []  # path relative to channel root, inclusive
    for idx, part in enumerate(rel_path_parts):
        if idx < len(dirs_before_channeldir) and dirs_before_channeldir[idx]==part:
            continue
        else:
            channel_chan_path.append(part)
    chan_path = os.path.join(*channel_chan_path)
    return chan_path

def rel_path_from_chan_path(chan_path, channeldir, windows=False):
    """
    Convert `chan_path` as obtained from a metadata provider into a `rel_path`
    suitable for accessing the file from the current working directory, e.g.,
    >>> rel_path_from_chan_path('Open Stax/Math', 'content/open_stax_zip/Open Stax')
    'content/open_stax_zip/Open Stax/Math'
    """
    if windows:
        chan_path_list = chan_path.split('\\')
    else:
        chan_path_list = chan_path.split('/')
    chan_path_list.pop(0)  # remove the channel root dir
    rel_path = os.path.join(channeldir, *chan_path_list)
    return rel_path

def filter_thumbnail_files_by_extension(filenames):
    """
    We don't want to create `ContentNode` from thumbnail files: .png / .jpg / .jpeg
    """
    filenames_cleaned = []
    for filename in filenames:
        keep = True
        for ext in THUMBNAIL_EXTS:
            if filename.endswith('.'+ext):
                keep = False
        if keep:
            filenames_cleaned.append(filename)
    return filenames_cleaned


# MAIN
################################################################################

def process_folder(writer, channeldir, rel_path, filenames):
    """
    Create row in Content.csv from all files and subforlders of the path `rel_path`.
    """

    print('in process_folder', channeldir, rel_path, filenames)
    chan_path = chan_path_from_rel_path(rel_path, channeldir)
    chan_path_tuple = path_to_tuple(chan_path)
    chan_path_list = list(chan_path_tuple)

    # A. FIND PARENT DIR
    folder_name = chan_path_list.pop()

    # create this folder (and parents if necessary) inside zip
    parent_path = join(*chan_path_list)
    print('   Writing {} Folder...'.format(folder_name))
    writer.add_folder(
        parent_path,                            # (str) where in zip to write folder
        folder_name,                            # (str) content's title
        source_id=str(uuid.uuid4())[0:8],       # (str) content's original id (optional)
        description=DEFAULT_FOLDER_DESCRIPTION, # (str) description of content (optional)
        language='en',                          # (str): language of content (optional)
        # thumbnail (str):  path to thumbnail in zip (optional)
    )

    # filter out thumbnails filenames
    filenames_cleaned = filter_thumbnail_files_by_extension(filenames)


    # B. PROCESS FILES
    for filename in filenames_cleaned:
        print('   Writing file {}...'.format(filename))
        chan_filepath = os.path.join(chan_path, filename)
        zip_filepath = join(*chan_path_tuple)
        filename_noext, _ = os.path.splitext(filename)


        # check for file thumbnail (same name as file but with extentions .jpg)
        thumbnail = None
        for ext in THUMBNAIL_EXTS:
            thumbnail_path = join(rel_path, filename_noext+'.' + ext)
            if os.path.exists(thumbnail_path):
                thumbnail = writer.add_file(zip_filepath, filename_noext, thumbnail_path, ext='.'+ext, write_data=False)
                break

        writer.add_file(
                zip_filepath,                   # (str) where in zip to write file
                filename_noext,                       # content's title
                join(rel_path,filename),
                # download_url: (str) url or local path to download from
                # write_data: (boolean) indicates whether to add as a csv entry (optional)
                # ext: (str) extension to use for file
                license='CC BY',  # (str): content's license
                copyright_holder='Copyright holder name', # holder of content's license (required except for PUBLIC_DOMAIN)
                # license_description= (str): description of content's license (optional)
                source_id=str(uuid.uuid4())[0:8], # content's original id (optional)
                description=DEFAULT_FILE_DESCRIPTION ,#  description of content (optional)
                author=DEFAULT_FILE_AUTHOR, # (str): who created the content (optional)
                language='en', #  (str): language of content (optional)
                thumbnail=thumbnail,  # (str):  path to thumbnail in zip (optional)
        )


def create_CSVs_from_channeldir(channeldir):

    # Open a writer to generate files
    with data_writer.DataWriter(write_to_path=WRITE_TO_PATH) as writer:

        # Write channel details to spreadsheet
        thumbnail = writer.add_file('.', "channel_thumbnail", 'content/channel_thumbnail.jpg', write_data=False)
        writer.add_channel(CHANNEL_NAME, CHANNEL_SOURCE_ID, CHANNEL_DOMAIN, CHANNEL_LANGUAGE, description=CHANNEL_DESCRIPTION, thumbnail=thumbnail)

        content_folders = list(os.walk(channeldir))

        # MAIN PROCESSING OF os.walk OUTPUT
        ############################################################################
        _ = content_folders.pop(0)  # Skip over channel folder because handled above
        for rel_path, _subfolders, filenames in content_folders:
            process_folder(writer, channeldir, rel_path, filenames)

        sys.stdout.write("\n\nDONE: Zip created at {}\n".format(writer.write_to_path))



# CLI
################################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Generate CSV metadata templates for each file in `channeldir`.",
    )
    parser.add_argument('--channeldir', required=True, action=FolderExistsAction,
                        help='The dir that corresponds to the root of the channel.')
    args = parser.parse_args()
    create_CSVs_from_channeldir(args.channeldir)

