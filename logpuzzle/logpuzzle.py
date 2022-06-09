#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    puzzle_url_set = set()
    prefix = 'http://'

    match = re.search(r'(\w+)_(.+)', filename)
    type_sort = match.group(1)
    domain = match.group(2)

    f = open(filename, 'r')

    for line in f:
        match = re.search(r'\s(\S+puzzle\S+)\s', line)
        if match:
            url = match.group(1)
            puzzle_url_set.add(prefix + domain + url)

    puzzle_url_list = []
    if type_sort == 'animal':
        puzzle_url_list = sorted(list(puzzle_url_set))

    if type_sort == 'place':
        puzzle_url_list = sorted(list(puzzle_url_set), key=lambda i: re.search(r'-(\w+).jpg', i).group(1))

    f.close()
    return puzzle_url_list


def download_images(img_urls, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    count = 0
    for img in img_urls:
        img_file_name = dest_dir + 'img' + str(count) + '.jpg'
        urllib.request.urlretrieve(img, img_file_name)
        count += 1

    complete_name = os.path.join(dest_dir, "index.html")
    f = open(complete_name, 'w')
    html_text = """
    <html>
    <body>
    <img src="img0.jpg"><img src="img1.jpg"><img src="img2.jpg"><img src="img3.jpg"><img src="img4.jpg"><img src="img5.jpg"><img src="img6.jpg"><img src="img7.jpg"><img src="img8.jpg"><img src="img9.jpg"><img src="img10.jpg"><img src="img11.jpg"><img src="img12.jpg"><img src="img13.jpg"><img src="img14.jpg"><img src="img15.jpg"><img src="img16.jpg"><img src="img17.jpg"><img src="img18.jpg"><img src="img19.jpg">
    </body>
    </html>"""

    f.write(html_text)
    f.close()


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
