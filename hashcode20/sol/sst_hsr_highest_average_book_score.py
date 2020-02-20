# -*- coding: utf-8 -*-
import random

from hashcode20.helpers import Input, Output
import numpy as np

def main(i: Input) -> Output:
    """shortest signing time and higher shipping book rate and highest average book score"""

    book_scores_per_library = {
        library.library_id: list(map(lambda book_id: i.scores[book_id], library.books))
        for library in i.libraries
    }

    libraries_sorted = sorted(i.libraries, key=lambda library:
        (library.nb_signup_days, -library.ship_book_rate, np.mean(book_scores_per_library[library.library_id])))
    library_order = list(map(lambda l: l.library_id, libraries_sorted))
    book_order_per_library = [list(l.books) for l in libraries_sorted]
    return Output(library_order, book_order_per_library)

