import argparse

from hashcode20.helpers import Input
import numpy as np

parser = argparse.ArgumentParser("hashcode20", description="CLI util for Google Hash Code 2019. "
                                                           "It assumes the input provided in stdin.")

parser.add_argument("--in",  dest="in_file",  type=str, default=None, help="provide an input data file.")
args = parser.parse_args()


def _score_book_list(book_ids, score):
    return sum(map(lambda book_id: score[book_id], book_ids))


def print_stats(data, label):
    print("Avg {}: {}".format(label, np.mean(data)))
    print("Std {}: {}".format(label, np.std(data)))
    print("Max {}: {}".format(label, np.max(data)))
    print("Min {}: {}".format(label, np.min(data)))
    print("00th {}: {}".format(label, np.percentile(data, 0)  ))
    print("25th {}: {}".format(label, np.percentile(data, 25) ))
    print("50th {}: {}".format(label, np.percentile(data, 50) ))
    print("75th {}: {}".format(label, np.percentile(data, 75) ))
    print("100th {}: {}".format(label, np.percentile(data, 100)))
    print("-"*50)



if __name__ == '__main__':
    input_ = Input.read(args.in_file)  # type: Input

    print("# Libraries: {}".format(len(input_.libraries)))
    print("# Book: {}".format(input_.nb_books))
    print("# Days: {}".format(input_.nb_days))


    print_stats(input_.scores, "Book score")
    print_stats([len(l.books) for l in input_.libraries], "Books per Library")
    print_stats([_score_book_list(l.books, input_.scores) for l in input_.libraries], "Score per Library")
    print_stats(list(map(lambda l: l.ship_book_rate, input_.libraries)), "Shipping rate")
    print_stats(list(map(lambda l: l.nb_signup_days, input_.libraries)), "signup day period")


