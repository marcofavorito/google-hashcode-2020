# -*- coding: utf-8 -*-
import random

from hashcode20.helpers import Input, Output


def main(i: Input) -> Output:
    """shortest signing time and higher shipping book rate"""
    libraries_sorted = sorted(i.libraries, key=lambda library: (library.nb_signup_days, -library.ship_book_rate))
    library_order = list(map(lambda l: l.library_id, libraries_sorted))
    book_order_per_library = []
    for i, l in enumerate(libraries_sorted):
        if i % 2 == 0:
            books = list(l.books)
            book_order_per_library.append(books)
        else:
            books = list(l.books)[::-1]
            book_order_per_library.append(books)
    return Output(library_order, book_order_per_library)