def cousins_of_one_tag_one_pattern(whole_page_soup, pattern):
    print('\n part6 running')

    print('\n')

    cousin_list = []

    pattern.append('html')

    while len(pattern) != 0:
        print('whole_page_soup len:')
        print(len(whole_page_soup))
        print('\nwhole_page_soup.name:')
        print([n.name for n in whole_page_soup])


        print('pattern :')
        print(pattern)

        try:
            pattern_pop = pattern.pop()
            whole_page_soup = [
                n for n in whole_page_soup.find_all(
                    pattern_pop,
                    recursive=False
                )
                if n.name == pattern_pop
            ][0]
        except IndexError:
            print('whole_page_soup:')
            print(whole_page_soup)