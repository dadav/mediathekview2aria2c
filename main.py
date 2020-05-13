#!/usr/bin/env python3

import os
import sys
import feedparser
import unicodedata
import re


BASE = 'https://mediathekviewweb.de/feed?query={}&everywhere=true'

keywords = "+".join(sys.argv[1:])
feed = feedparser.parse(BASE.format(keywords))

def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

for entry in feed.entries:
    print(entry.link)
    print("  out=" + slugify(entry.title))
