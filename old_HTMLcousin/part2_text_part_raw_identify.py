from bs4 import SoupStrainer, BeautifulSoup
from re import compile as reCompile
from re import I as reI


## index card 2 & 3

def get_souped_html_element_results_by_text_part(text_part_input, souped_page_all):
    print('\npart2 running')
    search_prase = text_part_input

    print('search_prase is :' + search_prase)
    print('text_part_appearance is: ' + str(len(souped_page_all.find_all(text=reCompile(search_prase, reI)))))

    '''
    for r in souped_page_all.find_all(text=reCompile(search_prase, reI)):
        text_part_appearance += 1
        print(r)
        print(r.parent)
        text_part_extend.append(r.parent)
    '''
    # return {r.parent for r in souped_page_all.find_all(text=reCompile(search_prase, reI))}
    try:
        search_result = [r.parent for r in souped_page_all.find_all(text=reCompile(search_prase, reI))]
    except:
        print('notfound as text')
    '''    
    try:
        search_result = [r.parent for r in souped_page_all.find_all(href=reCompile(search_prase, reI))]
    except:
        print('notfound as href')
    try:
        search_result = [r.parent for r in souped_page_all.find_all(src=reCompile(search_prase, reI))]
    except:
        print('not found as src')
    '''
    for s in (search_result):
        print(s)

    return search_result
