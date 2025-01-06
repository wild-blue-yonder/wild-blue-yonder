# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from src.wild_blue_yonder.lm import GRQ


gro = GRQ()

completion, headers = gro.chat(messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user","content": "What model are you?"}
    ])

...
