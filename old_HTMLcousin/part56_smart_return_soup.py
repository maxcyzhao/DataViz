def url_or_fname_to_soup(url_or_fname):
    print('\npart 56 running')
    print('using url/fname: ' + url_or_fname)

    if 'http' in url_or_fname:
        print('triggering broswer driver')
        print('smart action always save')

        import part1_io
        import string
        soup = part1_io.super_request_soup(
            url_or_fname,
            True,
            str(url_or_fname.translate(None, string.punctuation) + '.html')
        )
        print('saved as :' + str(url_or_fname.translate(None, string.punctuation) + '.html'))
    else:
        print('using local file: ' + url_or_fname)

        import part3_get_soupify_file_content
        soup = part3_get_soupify_file_content.from_file_made_by_part1_return_souped_version(
            url_or_fname,
        )

    return soup
