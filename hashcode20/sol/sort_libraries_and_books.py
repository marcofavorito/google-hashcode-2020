from hashcode20.helpers import Input, Output


def main(i: Input) -> Output:
    """naive: take order as the order of appearance"""
    libraries_sorted = sorted(i.libraries, key=lambda l: (l.nb_signup_days, -len(l.books)/l.ship_book_rate))
    library_order = list(l.library_id for l in libraries_sorted)
    book_order_per_library = [sorted(list(l.books), key=lambda b: -i.scores[b]) for l in libraries_sorted]
    return Output(library_order, book_order_per_library)