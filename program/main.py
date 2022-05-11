import argparse
import os
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from app.download_page import download_page
from app.metadata import print_metadata

if __name__ == '__main__':

    # cache driver in local directory
    os.environ['WDM_LOCAL'] = '1'

    parser = argparse.ArgumentParser(description='Fetch webpages.')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+',
                        help='URLs to fetch webpages for')
    parser.add_argument('--metadata', action='store_true',
                        help='print details about what was fetched')
    parser.add_argument('--assets', action='store_true',
                        help='download assets as well')

    args = parser.parse_args()

    options = Options()
    options.add_argument("--headless")
    options.log.level = "trace"

    print(os.path.join(sys.path[0], 'geckodriver.log'))

    driver = webdriver.Firefox(
        service=Service(
            GeckoDriverManager().install(),
            log_path=os.path.join(sys.path[0], 'geckodriver.log')
        ),
        options=options)

    out_dir = os.path.join(sys.path[0], 'output')
    os.makedirs(out_dir, exist_ok=True)

    for url in args.urls:
        [site, contents] = download_page(
            driver, url, out_dir, include_assets=args.assets)

        if args.metadata is True:
            print('------------------------------------------')
            print_metadata(site, contents)
            print('------------------------------------------')

    driver.quit()
