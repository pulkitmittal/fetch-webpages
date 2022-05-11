import json
import os
from threading import local
from time import sleep

import requests
from selenium.webdriver.remote.webdriver import WebDriver


def download_assets(driver: WebDriver, url: str, site_dir: str, html: str):
    """
        Download the referenced files to the same path as in the html.
        Also, modify html so that absolute paths starting with / start with ./
    """
    sess = requests.Session()
    sess.get(url)            # sets cookies

    resources = driver.execute_script('''
        return (function () {
            var localOnly = s => s && !s.startsWith('https://') && !s.startsWith('http://');
            return {
                js: Array.from(document.querySelectorAll('script')).map(s => s.getAttribute('src')).filter(localOnly),
                css: Array.from(document.querySelectorAll('link')).map(s => s.getAttribute('href')).filter(localOnly),
                img: Array.from(document.querySelectorAll('img'))
                    .map(s => s.srcset ? s.srcset.trim().split(',').map(s => s.trim().split(' ')[0].replace('\\n', '')) : [s.getAttribute('src')])
                    .reduce((p, c) => { p.push(...c); return p; }, [])
                    .filter(localOnly)
                    .filter(s => !s.startsWith('data:image'))
            };
        })();
    ''')
    images = resources['img']

    # image resources, make sure they are unique
    for img in list(set(images)):
        hr = url + img
        res = sess.get(hr)
        local_path = site_dir + img
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, 'wb') as fp:
            fp.write(res.content)
            print('saved ' + img)
        # make it relative
        if img.startswith('/'):
            html = html.replace(img, '.' + img)

    return html


def download_page(driver: WebDriver, url: str, out_dir: str, include_assets=False):
    """
        Download page, assets and save them to a folder
    """
    site = url.replace('https://', '').replace('http://', '')
    site_dir = os.path.join(out_dir, site)
    os.makedirs(site_dir, exist_ok=True)
    filename = os.path.join(site_dir, 'index.html')
    try:
        driver.get(url)
        contents = driver.page_source
        sleep(2)

        try:
            if include_assets:
                contents = download_assets(driver, url, site_dir, contents)
        except Exception as e:
            # don't prevent saving index.html if assets fail
            print('Some error occurred when downloading assets...')
            print(e)

        # save index.html file
        with open(filename, 'w') as fp:
            fp.write(contents)
            print('Saved ' + url + ' to ' + filename)

        return [site, contents]
    except Exception as e:
        print('Some error occurred when loading page...')
        print(e)
