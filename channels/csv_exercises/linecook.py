#!/usr/bin/env python
import logging

from ricecooker.chefs import LineCook
from ricecooker.config import LOGGER


# LOGGING SETTINGS
################################################################################
logging.getLogger("cachecontrol.controller").setLevel(logging.WARNING)
logging.getLogger("requests.packages").setLevel(logging.WARNING)
LOGGER.setLevel(logging.DEBUG)


# CSV CHANNEL WITH EXERCISES
################################################################################

class CsvExercisesChef(LineCook):
    """
    Sushi chef for uploading the results of the files + Channel.csv + Content.csv
    to Kolibri Studio.
    """
    RICECOOKER_JSON_TREE = 'ricecooker_json_tree.json'
    # no custom methods needed: will use generic `LineCook` main and run methods



# CLI
################################################################################

if __name__ == '__main__':
    chef = CsvExercisesChef()
    chef.main()
