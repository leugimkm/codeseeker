# -*- coding: utf-8 -*-

# CodeSeeker
from .seeker import Seeker, open_url, to_txt, get_file
from .utils import show
from .base import parse_args

__all__ = [
    "Seeker",
    "open_url",
    "to_txt",
    "get_file",
    "show",
    "parse_args",
]

__version__ = "0.0.1"
