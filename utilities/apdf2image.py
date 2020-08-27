from __future__ import print_function
from wand.image import Image

with Image(filename='/Users/mukeshkhattar/github_public_repos/python-samples/utilities/abc.pdf') as img:
    print('pages = ', len(img.sequence))

    with img.convert('png') as converted:
        converted.save(filename='page.png')
