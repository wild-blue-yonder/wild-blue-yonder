# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from src.wild_blue_yonder.lm import GRQ


gro = GRQ()
#
# answer = gro._send(messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user","content": "What model are you?"}
#     ])

messages = [
    # {'role': 'system', 'content': 'You are an image recognising assistant.'}, # prompting with images is incompatible with system messages, if you add it it will not work.
    {'role': 'user', 'content': 'I want to show you a picture...'},
    {'role': 'assistant', 'content': 'Go ahead...'},
]
text = 'What is in this picture?'
image_url = 'https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:yjvzk3c3uanrlrsdm4uezjqi/bafkreicww64gk45uiwsytagoculecgcpl5xfutku67jj47yl3r6oavlx4y@jpeg'
answer = gro.text_and_image_url(messages, text, image_url)
...
