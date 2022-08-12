import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# @pytest.fixture(scope='function')
# def driver(request):
#     options = chrome_options()
#     options.add_argument('--start-maximixed')
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()



@pytest.fixture(scope='function')
def driver(request, wdwsize='--start-maximized'):
    options = chrome_options()
    options.add_argument(wdwsize)
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd
