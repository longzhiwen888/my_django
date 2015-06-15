#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'chenhailong'

import os
import re
import urllib


root = os.path.dirname(__file__)
file_name = '5629533619073584608.css'
file_path = os.path.join(root, file_name)

with open(file_path, 'rb') as f:
    content = f.read()
    relist = re.findall('(?is)http://[\s\S]*?\.(?:gif|png|jpg)', content)
    for url in relist:
        img = urllib.urlopen(url).read()
        new_name = url.split('/')[-1]

        new_f = open(new_name, 'wb')
        new_f.write(img)
        new_f.close()

        new_url = '''http://127.0.0.1:8000/static/document/img/%s''' % new_name
        content = content.replace(url, new_url)

with open(file_path, 'wb') as f:
    f.write(content)

