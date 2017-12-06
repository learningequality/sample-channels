#!/usr/bin/env python
import logging

from ricecooker.chefs import JsonTreeChef
from ricecooker.config import LOGGER


# LOGGING SETTINGS
################################################################################
logging.getLogger("cachecontrol.controller").setLevel(logging.WARNING)
logging.getLogger("requests.packages").setLevel(logging.WARNING)
LOGGER.setLevel(logging.DEBUG)


# CSV SAMPLE CHANNEL LINE COOK
################################################################################

class SampleJsonTreeChef(JsonTreeChef):
    """
    Sushi chef reads the metadata and file references from RICECOOKER_JSON_TREE.
    """
    RICECOOKER_JSON_TREE = 'sample_ricecooker_json_tree.json'
    # no custom methods needed: uses generic `JsonTreeChef` main and run methods

    def pre_run(self, args, options):
        print('Normally this is where code would run to generate the Ricecooker '
              'JSON tree, but since we started with a ready json file, there '
              'is nothing to do for us here...')


# CLI
################################################################################

if __name__ == '__main__':
    chef = SampleJsonTreeChef()
    chef.main()

