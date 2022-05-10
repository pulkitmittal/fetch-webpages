import argparse
import os
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from app.load_page import load_page
from app.metadata import print_metadata

if __name__ == '__main__':

    # cache driver in local directory
    os.environ['WDM_LOCAL'] = '1'

    parser = argparse.ArgumentParser(description='Fetch webpages.')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+',
                        help='URLs to fetch webpages for')
    parser.add_argument('--metadata', action='store_true',
                        help='print details about what was fetched')

    args = parser.parse_args()
    # print(args.urls)
    # print(args.metadata)

    options = Options()
    options.add_argument("--headless")
    options.log.level = "trace"

    driver = webdriver.Firefox(
        service=Service(
            GeckoDriverManager().install(),
            log_path=os.path.join(sys.path[0], 'geckodriver.log')
        ),
        options=options)

    out_dir = './'
    os.makedirs(out_dir, exist_ok=True)

    for url in args.urls:
        contents = load_page(driver, url)
        site = url.replace('https://', '').replace('http://', '')
        filename = os.path.join(out_dir, site + '.html')
        f = open(filename, "w")
        f.write(contents)
        f.close()

        if args.metadata is True:
            print('------------------------------------------')
            print_metadata(site, contents)
            print('------------------------------------------')

    driver.quit()
