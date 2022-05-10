from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


def load_page(driver: WebDriver, url: str):
    try:
        driver.get(url)
        html = driver.page_source
        sleep(2)
        # we could use execute_script to execute Javascript, but it is easier to match regex in html
        # num_links = driver.execute_script(
        #     'return document.querySelectorAll("a").length')
        # print(num_links)
        return html
    except Exception as e:
        print('Some error occurred when loading page...')
        print(e)
