# -*- coding: utf-8 -*-
import random

from hashcode20.helpers import Input, Output


def main(i: Input) -> Output:
    """shortest signing time and higher shipping book rate"""
    libraries_sorted = sorted(i.libraries, key=lambda library: (library.nb_signup_days, -library.ship_book_rate))
    # library_order = list(map(lambda l: l.library_id, libraries_sorted))
    library_order = []
    book_order_per_library = []
    total_signup_days = 0
    scanned_books = set()
    while total_signup_days < i.nb_days:
        library = libraries_sorted[0]
        total_signup_days += library.nb_signup_days
        library_books = library.books
        library_books = set(book for book in library_books if book not in scanned_books)
        library_books = list(library_books)
        library_books = library_books[:library.ship_book_rate*(i.nb_days - total_signup_days)]
        if not library_books:
            continue
        scanned_books.update(library_books)
        library_order.append(library.library_id)
        book_order_per_library.append(library_books)
        if len(libraries_sorted) == 1:
            break
        libraries_sorted = libraries_sorted[1:]
        # libraries_sorted = sorted(i.libraries, key=lambda library: (library.nb_signup_days, -library.ship_book_rate/(len([b for b in library.books if b not in scanned_books]) + 1)))
        
    return Output(library_order, book_order_per_library)