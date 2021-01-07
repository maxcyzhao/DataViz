from bs4 import SoupStrainer, BeautifulSoup
from re import compile as reCompile
from re import I as reI


def get_pattern_of_tags(tags):
    print('\npart4 running')
    print('tags :')
    for t in tags:
        print(t)
    # pattern = {}
    pattern = []

    non_script_tag_counter = 0

    # js动态加载总是出问题
    #for tag in [t for t in tags if t.name != 'script']:

    # 强行加载js里的对象
    for tag in tags:
        non_script_tag_counter += 1
        name_pattern = []
        attrs_pattern = []

        while not (tag.name == 'html' or tag.name == 'HTML'):
            name_pattern.append(tag.name)
            # attrs_pattern.append(tag.attrs)
            tag = tag.parent
            # print(tag.name)
            # print(type(tag.name))
            # print(tag.attrs)
        '''
        print("name_pattern:")
        print(name_pattern)
        print('attrs_pattern:')
        print(attrs_pattern)
        '''

        pattern.append(
            [
                n for n in name_pattern
                # [n, a] for n, a in zip(name_pattern, attrs_pattern)
            ]
        )
    print('non_script_tag :' + str(non_script_tag_counter))
    return pattern

# 还没想好如何记录sub-element的单层内'序号'， 所以也用不到attrs。后面想好了可以用
