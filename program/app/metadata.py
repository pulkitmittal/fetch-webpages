import datetime
import re


def print_metadata(site, html):
    # site: www.google.com
    print('site: ' + site)
    # num_links: 35
    print('num_links: ' + str(len(re.findall(r'\<a\s', html))))
    # images: 3
    print('images: ' + str(len(re.findall(r'\<img\s', html))))
    # last_fetch: Tue Mar 16 2021 15:46 UTC
    print('last_fetch: ' +
          datetime.datetime.utcnow().strftime("%a %b %d %Y %H:%M") + ' UTC')
