# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
from openai import OpenAI


class XAI(OpenAI):
    def __init__(self, *args, **kwargs):
        api_base = environ.get("XAI_API_BASE", "https://api.x.ai/v1")
        api_key  = environ.get("XAI_API_KEY")
        super().__init__(api_key=api_key, base_url=api_base, *args, **kwargs)


class GRQ(OpenAI):
    def __init__(self, *args, **kwargs):
        api_base = environ.get("GROQ_API_BASE", "https://api.groq.com/openai/v1")
        api_key = environ.get("GROQ_API_KEY")
        super().__init__(api_key=api_key, base_url=api_base, *args, **kwargs)