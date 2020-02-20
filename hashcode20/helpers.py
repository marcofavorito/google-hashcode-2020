# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

import logging
from enum import Enum
from functools import partial
from typing import List, Set, Dict, Optional

from hashcode20.model import Library

logger = logging.getLogger(__name__)


def _parse_library(library_id, lines) -> Library:
    line = next(lines)
    library_nb_books, library_nb_signup_days, library_ship_book_rate = map(int, line.strip().split())
    line = next(lines)
    books = set(map(int, line.strip().split()))
    assert len(books) == library_nb_books
    library = Library(library_id, books, library_nb_signup_days, library_ship_book_rate)
    return library


class Input(object):
    """This class manages the input of the problem."""

    def __init__(self, nb_books: int, nb_libraries: int, nb_days: int,
                 scores: List[int], libraries: List[Library]):
        self.nb_books = nb_books
        self.nb_libraries = nb_libraries
        self.nb_days = nb_days
        self.scores = scores
        self.libraries = libraries

    @classmethod
    def read(cls, filename=None):
        """Returns an Input instance. If filename is None, read from stdin."""
        if filename is None:
            lines_iterator = sys.stdin
        else:
            lines_iterator = iter(open(filename).readlines())

        line = next(lines_iterator)
        nb_books, nb_libraries, nb_days = map(int, line.strip().split())
        line = next(lines_iterator)
        scores = list(map(int, line.strip().split()))
        libraries = [_parse_library(library_id, lines_iterator) for library_id in range(nb_libraries)]
        logger.debug("Parsed input: {} libraries.".format(len(libraries)))
        return Input(nb_books, nb_libraries, nb_days, scores, libraries)


class Output(object):
    """This class manages the output of the problem."""

    def __init__(self,
                 library_order_for_signup_process: List[int],
                 books_order_per_library: List[List[int]]):
        self.library_order_for_signup_process = library_order_for_signup_process
        self.books_order_per_library = books_order_per_library

    @property
    def nb_libraries_for_signup(self):
        return len(self.library_order_for_signup_process)

    def write(self, filename=None) -> None:
        if filename is not None:
            file = open(filename, "w")
        else:
            file = None
        logger.debug("Printing to {}...".format("stdout" if file is None else filename))

        print(self.nb_libraries_for_signup, file=file)

        for library_position in range(len(self.library_order_for_signup_process)):
            library_id = self.library_order_for_signup_process[library_position]
            nb_books_library = len(self.books_order_per_library[library_position])

            print("{} {}".format(library_id, nb_books_library), file=file)
            print(" ".join(map(str, self.books_order_per_library[library_position])), file=file)

    @classmethod
    def read(cls, solution_file=None):
        if solution_file is None:
            lines = sys.stdin
        else:
            lines = iter(open(solution_file).readlines())

        line = next(lines)
        nb_libraries_scheduled = int(line.strip())

        library_order_for_signup_process = []
        books_order_per_library = []

        for library_idx in range(nb_libraries_scheduled):
            line = next(lines)
            library_id, nb_books = list(map(int, line.strip().split()))
            library_order_for_signup_process.append(library_id)

            line = next(lines)
            book_order = list(map(int, line.strip().split()))
            books_order_per_library.append(book_order)

        return Output(library_order_for_signup_process, books_order_per_library)

    def score(self) -> int:
        """Score the output."""
        raise NotImplementedError


class Task:

    def step(self) -> None:
        """Schedule the task for the next day."""

    def done(self) -> bool:
        """"""


class SigningTask(Task):

    def __init__(self, simulator: 'Simulator', library: Library):
        self.library_to_sign_up = library
        self.simulator = simulator

        self.current_signing_day = 0

    def step(self) -> 'Task':
        self.current_signing_day += 1

    def done(self):
        # we count from zero :-)
        return self.current_signing_day > self.library_to_sign_up.nb_signup_days - 1


class ShippingBookTask(Task):

    def __init__(self, simulator: 'Simulator', library: Library, book_order: List[int]):
        self.simulator = simulator
        self.library = library
        self.book_order = book_order

        self.last_book_idx_processed = -1

    def step(self) -> None:
        # process books
        rate = self.library.ship_book_rate
        for _ in range(rate):
            idx_to_process = self.last_book_idx_processed + 1
            if idx_to_process >= len(self.book_order):
                return

            book_id = self.book_order[idx_to_process]
            self.simulator.ship_book(book_id)
            self.last_book_idx_processed = idx_to_process


class Simulator:

    def __init__(self, input: Input, output: Output):
        self.input = input
        self.output = output


        self.reset()

        self.already_shipped_books = set()  # type: Set[int]

    def compute_score(self) -> int:
        self.reset()
        for days in range(self.input.nb_days):
            self.step()
        return self.score

    def reset(self):
        self.score = 0
        self.day = -1
        self.current_signing_task = None

        # schedule the first sign up process - if any
        if len(self.output.library_order_for_signup_process) > 0:
            next_library_id = self.output.library_order_for_signup_process[0]
            next_library = self.input.libraries[next_library_id]
            self.next_signing_task = SigningTask(self, next_library)
            self.last_scheduled_library_index = 0
        else:
            self.last_scheduled_library_index = -1
            self.next_signing_task = None

        self.current_shipping_tasks = []
        self.next_shipping_tasks = []
        self.already_shipped_books = set()  # type: Set[int]

    def step(self):
        """Do a simulation step, and schedule tasks for the next days"""
        self.day += 1
        self.current_signing_task = self.next_signing_task
        self.next_signing_task = None
        self.current_shipping_tasks = self.next_shipping_tasks
        self.next_shipping_tasks = []

        # signing process
        if self.current_signing_task is not None:
            self.current_signing_task.step()
            if not self.current_signing_task.done():
                self.next_signing_task = self.current_signing_task
            else:
                # schedule next signing task and schedule ship book task
                current_index = self.last_scheduled_library_index
                self.last_scheduled_library_index += 1
                self.next_signing_task = self._get_next_signing_task_if_any(self.last_scheduled_library_index)

                signed_library = self.current_signing_task.library_to_sign_up
                shipping_task = ShippingBookTask(self,
                                                 signed_library,
                                                 self.output.books_order_per_library[current_index])
                self.next_shipping_tasks.append(shipping_task)


        for shipping_task in self.current_shipping_tasks:
            shipping_task.step()
            if not shipping_task.done():
                self.next_shipping_tasks.append(shipping_task)

    def _get_next_signing_task_if_any(self, library_idx: int) -> Optional[SigningTask]:
        if library_idx < len(self.output.library_order_for_signup_process):
            library_id = self.output.library_order_for_signup_process[library_idx]
            library = self.input.libraries[library_id]
            return SigningTask(self, library)
        else:
            return None

    def ship_book(self, book_id: int):
        if book_id in self.already_shipped_books:
            return
        else:
            self.score += self.input.scores[book_id]
            self.already_shipped_books.add(book_id)


def score(input: Input, output: Output) -> int:
    """Get the score (does not implement all the checks..."""
    return Simulator(input, output).compute_score()
