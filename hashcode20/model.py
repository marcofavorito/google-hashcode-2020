# -*- coding: utf-8 -*-
from typing import Set


class Library:

    def __init__(self, library_id: int, books: Set[int], nb_signup_days: int, ship_book_rate: int):
        """Init a library."""
        self.library_id = library_id
        self.books = books
        self.nb_signup_days = nb_signup_days
        self.ship_book_rate = ship_book_rate

