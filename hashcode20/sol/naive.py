# -*- coding: utf-8 -*-
import random

from hashcode20.helpers import Input, Output


def main(i: Input) -> Output:
    """naive: take order as the order of appearance"""
    library_order = list(map(lambda l: l.library_id, i.libraries))
    book_order_per_library = [list(l.books) for l in i.libraries]
    return Output(library_order, book_order_per_library)

