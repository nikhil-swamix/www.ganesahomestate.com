import modulex as mx


def gather_css():
    mx.touch('css/')
    SUPER_CSS = ''
    for l in soup.select('link'):
        url = l['href']

        if url.startswith('//'):
            url = 'http:' + url

        if 'css' in url:
            SUPER_CSS += mx.get_page(url).text
            print(url)

    mx.fwrite('css/style.css', SUPER_CSS)


def gather_js():
    mx.touch('js/')
    EXCLUDE = ['www.googletagmanager.com']
    SUPER_JS = ''
    for l in soup.select('script'):  # noqa: E741
        url = l.get('src')
        if not url:  # exclude empty src
            continue

        if url.split('/')[2] in EXCLUDE:
            continue

        if url.startswith('//'):
            url = 'http:' + url

        if 'js' in url:
            SUPER_JS += mx.get_page(url).text
            print(url)

    mx.fwrite('js/main.js', SUPER_JS)


def gather_images():
    """
        Implement Folder hirerarchy according to url
    """
    mx.touch('img/')
    print(len(soup.select('img')))
    for i in soup.select('img'):
        url = i.get('src')
        if not url:  # exclude empty src
            continue
        category_folder = url.split('/')[-2]
        mx.touch(f'img/{category_folder}/')
        ext = url.split('.')[-1]
        url_hash = mx.hash(url)
        save_path=f'./img/{category_folder}/{url_hash}.{ext}'
        try:
            def dl_fn(): 
                return open(save_path, 'wb').write(mx.get_page(url).content)
            dl_fn()
            i['src'] = save_path

        except:  # noqa: E722
            pass

        print(i)


def transform_imgurl():
    for i in soup.select('img'):
        url = i['src']
        ext = url.split('.')[-1]
        url_hash = mx.hash(url)

        orignal = i['src']
        i['src'] = f'./img/{url_hash}.{ext}'
        i['src-orignal'] = orignal

    # print(soup.select('img'))


if __name__ == '__main__':
    url = 'https://www.realtimerealtors.in/'
    soup = mx.get_page_soup(url)
    print(soup)

    gather_css()
    gather_js()
    gather_images()
    # transform_imgurl()
    save = mx.fwrite('index.html',str(soup),)
    # print(soup)
