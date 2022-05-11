import datetime
import re


def print_metadata(site, html):
    """
        Prints metadata of page loaded (num_links, images, last_fetch)
    """
    # site: www.google.com
    print('site: ' + site)

    # we could use execute_script to execute Javascript when loading page,
    # but I would like to keep it separate and match regex in html
    # num_links = driver.execute_script(
    #     'return document.querySelectorAll("a").length')
    # print(num_links)

    # num_links: 35
    print('num_links: ' + str(len(re.findall(r'\<a\s', html))))

    # images: 3
    print('images: ' + str(len(re.findall(r'\<img\s', html))))

    # last_fetch: Tue Mar 16 2021 15:46 UTC
    print('last_fetch: ' +
          datetime.datetime.utcnow().strftime("%a %b %d %Y %H:%M") + ' UTC')
