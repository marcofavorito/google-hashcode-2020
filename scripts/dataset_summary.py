import argparse

from hashcode20.helpers import Input
import numpy as np

parser = argparse.ArgumentParser("hashcode20", description="CLI util for Google Hash Code 2019. "
                                                           "It assumes the input provided in stdin.")

parser.add_argument("--in",  dest="in_file",  type=str, default=None, help="provide an input data file.")
args = parser.parse_args()


def _score_book_list(book_ids, score):
    return sum(map(lambda book_id: score[book_id], book_ids))

if __name__ == '__main__':
    input_ = Input.read(args.in_file)  # type: Input

    print("# Libraries: {}".format(len(input_.libraries)))
    print("# Book: {}".format(input_.nb_books))
    print("# Days: {}".format(input_.nb_days))

    print("Avg Books per Library: {}".format(np.mean([len(l.books) for l in input_.libraries])))
    print("Std Books per Library: {}".format(np.std([len(l.books) for l in input_.libraries])))

    print("Avg Score per Library: {}".format(np.mean([_score_book_list(l.books, input_.scores) for l in input_.libraries])))
    print("Std Score per Library: {}".format(np.mean([_score_book_list(l.books, input_.scores) for l in input_.libraries])))

    print("Avg Shipping rate: {}".format(np.mean(list(map(lambda l: l.ship_book_rate, input_.libraries)))))
    print("Std Shipping rate: {}".format(np.std(list(map(lambda l: l.ship_book_rate, input_.libraries)))))

    print("Avg signup day period: {}".format(np.mean(list(map(lambda l: l.nb_signup_days, input_.libraries)))))
    print("Std signup day period: {}".format(np.std(list(map(lambda l: l.nb_signup_days, input_.libraries)))))

    print("Avg Book score: {}".format(np.mean(input_.scores)))
    print("Std Book score: {}".format(np.std(input_.scores)))

