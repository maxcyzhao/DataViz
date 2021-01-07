def get_soup_cousins_of_single_pattern(single_soup, single_pattern):
    print('\npart7 running')

    single_pattern.append('html')
    print('after append html, pattern is: ' + str(single_pattern))

    single_soup = [[single_soup]]

    i, l = len(single_pattern), len(single_pattern)

    while i != 1:
        poped = single_pattern.pop()
        print('poped:' + poped)

        ans = []
        for rs in single_soup:
            for tags in rs:
                tag = tags.find_all(poped, recursive=False)
                if tag:
                    ans.append(tag)
        single_soup = ans
        i -= 1
        print('index now:' + str(i))

    target_tag_name = single_pattern.pop()
    print('desired target_tag_name is: ' + target_tag_name)


    ans = []
    for rs in single_soup:
        for tags in rs:
            tag = tags.find_all(target_tag_name)
            if tag:
                for t in tag:
                    ans.append(t)

    # from php_implode import implode
    # return implode(ans)
    return ans
