#!/usr/bin/env python

from bs4 import BeautifulSoup
import logging
import os
import sys
import tempfile

from le_utils.constants import licenses
from ricecooker.utils import data_writer, path_builder, downloader, html_writer
from ricecooker.utils.html import download_file
from ricecooker.utils.zip import create_predictable_zip



""" Run Constants"""
###########################################################

CHANNEL_NAME = 'Sample Souschef Channel (Wikipedia)'         # Name of channel
CHANNEL_SOURCE_ID = 'sample-souschef-channel' # Channel's unique id
CHANNEL_DOMAIN = 'en.wikipedia.org'        # Who is providing the content
CHANNEL_LANGUAGE = 'en'                    # Language of channel
CHANNEL_DESCRIPTION = ''                   # Description of the channel (optional)
CHANNEL_THUMBNAIL = 'https://vignette2.wikia.nocookie.net/uncyclopedia/images/6/63/Wikipedia-logo.png' # Local path or url to image file (optional)
PATH = path_builder.PathBuilder(channel_name=CHANNEL_NAME)
WRITE_TO_PATH = "{}{}{}.zip".format(os.path.dirname(os.path.realpath(__file__)), os.path.sep, CHANNEL_NAME) # Where to generate zip file



""" Additional Constants """
###########################################################
BASE_URL = 'https://en.wikipedia.org/wiki'

# Set up logging tools
LOGGER = logging.getLogger()
__logging_handler = logging.StreamHandler()
LOGGER.addHandler(__logging_handler)
LOGGER.setLevel(logging.INFO)

# License to be used for content under channel
CHANNEL_LICENSE = licenses.PUBLIC_DOMAIN


""" Main Scraping Method """
###########################################################
def scrape_source(writer):
    """ scrape_source: Scrapes channel page and writes to a DataWriter

        Wikipedia is organized with the following hierarchy:
            Citrus (Folder)
            |   Citrus Page HTML Zip (File)
            Potatoes (Folder)
            |   Potatoes Page HTML Zip (File)

        Args: writer (DataWriter): class that writes data to folder/csv structure
        Returns: None
    """
    LOGGER.info('Parsing HTML from {}...'.format(BASE_URL))

    create_folder('Citrus!', 'List_of_citrus_fruits')           # Add Citrus folder
    create_folder('Potatoes!', 'List_of_potato_cultivars')      # Add Potatoes folder


""" Helper Methods """
###########################################################
def create_folder(title, endpoint):
    """ Write folder to zip and download pages """
    PATH.open_folder(title)
    LOGGER.info('   Writing {} Folder...'.format(title))
    add_subpages_from_wikipedia_list(writer, '{}/{}'.format(BASE_URL, endpoint))
    writer.add_folder(str(PATH), title)
    PATH.go_to_parent_folder()

def make_fully_qualified_url(url):
    """ Ensure url is qualified """
    if url.startswith("//"):
        return "https:" + url
    elif url.startswith("/"):
        return "https://en.wikipedia.org" + url
    assert url.startswith("http"), "Bad URL (relative to unknown location): " + url
    return url

def read_source(url):
    """ Read page source as beautiful soup """
    html = downloader.read(url)
    return BeautifulSoup(html, 'html.parser')

def download_wikipedia_page(url, title, writer, thumbnail=None):
    """ Create zip file to use for html pages """
    destpath = tempfile.mkdtemp() # Create a temp directory to house our downloaded files

    # Generate details for files
    details = {
        'thumbnail': thumbnail,
        'source_id': url.split("/")[-1],
        'license': CHANNEL_LICENSE,
    }

    # Download the main wikipedia page, apply middleware processor, and call it index.html
    localref, _ = download_file(
        url,
        destpath,
        filename="index.html",
        middleware_callbacks=process_wikipedia_page
    )

    zippath = create_predictable_zip(destpath) # Turn the temp folder into a zip file
    writer.add_file(str(PATH), title, zippath, **details)

def process_wikipedia_page(content, baseurl, destpath, **kwargs):
    """ Saves images to html zip folder """
    page = BeautifulSoup(content, "html.parser")
    index = 0

    # Add style sheets to zip file
    for link in page.find_all("link"):
        if link.get('href') and 'stylesheet' in link['rel']:
            try:
                subpath = "item_{}".format(index)
                link["href"], _ = download_file(make_fully_qualified_url(link['href']), destpath, subpath=subpath)
                index = index + 1
            except Exception:
                link["href"] = "#"

    # Add images to zip file
    for image in page.find_all("img"):
        try:
            relpath, _ = download_file(make_fully_qualified_url(image["src"]), destpath)
            image["src"] = relpath
        except Exception:
            image["src"] = "#"

    # Replace links with text to avoid broken links
    content = str(page)
    for link in page.find_all("a"):
        if link.get('href') and not link['href'].startswith("#"):
            content = content.replace(str(link), link.text)

    return content

def add_subpages_from_wikipedia_list(writer, list_url):
    """ add_subpages_from_wikipedia_list: Parses wiki pages and creates corresponding files
        To understand how the following parsing works, look at:
            1. the source of the page (e.g. https://en.wikipedia.org/wiki/List_of_citrus_fruits), or inspect in chrome dev tools
            2. the documentation for BeautifulSoup version 4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    """
    page = read_source(list_url)        # Parse the the page into BeautifulSoup format, so we can loop through and manipulate it
    table = page.find("table")          # Extract the main table from the page

    # Loop through first 10 rows of the table
    all_rows = table.find_all("tr")
    first_ten_rows = list(all_rows)
    for row in first_ten_rows[0:10]:
        columns = row.find_all("td")    # Extract the columns (cells, really) within the current row
        if not columns:                 # Some rows are empty, so just skip
            continue

        link = columns[0].find("a")     # Get the link to the subpage
        if not link:                    # Some rows don't have links, so skip
            continue

        # Extract the URL and title for the subpage
        url = make_fully_qualified_url(link["href"])
        title = link.text
        LOGGER.info("      Writing {}...".format(title))

        # Attempt to extract a thumbnail for the subpage, from the second column in the table
        image = columns[1].find("img")
        thumbnail_url = make_fully_qualified_url(image["src"]) if image else None
        thumbnail = None
        if thumbnail_url and (thumbnail_url.lower().endswith("jpg") or thumbnail_url.lower().endswith("png")):
            thumbnail = writer.add_file(str(PATH), title, thumbnail_url, write_data=False)

        # Download the wikipedia page and add file in the path
        download_wikipedia_page(url, title, writer, thumbnail=thumbnail)


""" This code will run when the sous chef is called from the command line. """
if __name__ == '__main__':
    with data_writer.DataWriter(write_to_path=WRITE_TO_PATH) as writer:

         # Write channel details to spreadsheet
        thumbnail = writer.add_file(str(PATH), "Channel Thumbnail", CHANNEL_THUMBNAIL, write_data=False)
        writer.add_channel(CHANNEL_NAME, CHANNEL_SOURCE_ID, CHANNEL_DOMAIN, CHANNEL_LANGUAGE, description=CHANNEL_DESCRIPTION, thumbnail=thumbnail)

        # Scrape source content
        scrape_source(writer)

        sys.stdout.write("\n\nDONE: Zip created at {}\n".format(writer.write_to_path))
