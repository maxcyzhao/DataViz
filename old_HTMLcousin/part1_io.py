from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def super_request_soup(base, save_source, saved_source_filename):
    print('\npart1 running')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(base)

    source = driver.page_source

    soup = BeautifulSoup(source, 'lxml')

    if save_source:
        f = open(saved_source_filename, 'wb+')
        f.write(source.encode('utf-16'))
        # .decode('utf-8')  ???
        f.close()
        print('unsoupped source saved as: ' + saved_source_filename)
    else:
        print('didnt demand sourced to be saved')

    # print(soup)
    driver.close()

    return soup
