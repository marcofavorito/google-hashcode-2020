# -*- coding: utf-8 -*-
import random

from hashcode20.helpers import Input, Output


def main(i: Input) -> Output:
    """schedule libraries with shortest signing time"""
    libraries_sorted = sorted(i.libraries, key=lambda library: library.nb_signup_days)
    library_order = list(map(lambda l: l.library_id, libraries_sorted))
    book_order_per_library = [list(l.books) for l in libraries_sorted]
    return Output(library_order, book_order_per_library)

