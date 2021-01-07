from bs4 import BeautifulSoup


def from_file_made_by_part1_return_souped_version(fname):
    print('\npart3 running')
    f = open(fname, 'rb+')

    # lxml据说是最好用的。目前没出问题
    soup = BeautifulSoup(f, 'lxml')
    # soup = BeautifulSoup(f, 'html.parser')

    f.close()
    return soup
