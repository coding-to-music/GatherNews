""" Gather RSS news feeds into a pandas dataframe. """

import logging

import feedparser

from gathernews.template import ITEM
from gathernews.parse import map_rss

logger = logging.getLogger(__name__)

def get_rss(link: str):
    """ Get RSS from link. """
    try:
        d = feedparser.parse(link)

        return map_rss(d)

    except Exception as ex:
        logger.exception(ex)
        return []



    


