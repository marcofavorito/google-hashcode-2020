import argparse

from hashcode20.helpers import Input
import numpy as np

parser = argparse.ArgumentParser("hashcode20", description="CLI util for Google Hash Code 2019. "
                                                           "It assumes the input provided in stdin.")

parser.add_argument("--in",  dest="in_file",  type=str, default=None, help="provide an input data file.")
args = parser.parse_args()


if __name__ == '__main__':
    input_ = Input.read(args.in_file)  # type: Input

    print("# Libraries: {}".format(len(input_.libraries)))
    print("# Book: {}".format(len(input_.libraries)))

    print("Avg Shipping rate time: {}".format(np.mean(list(map(lambda l: l.ship_book_rate, input_.libraries)))))
    print("Std Shipping rate time: {}".format(np.std(list(map(lambda l: l.ship_book_rate, input_.libraries)))))

    print("Avg signup day: {}".format(np.mean(list(map(lambda l: l.nb_signup_days, input_.libraries)))))
    print("Std signup day: {}".format(np.std(list(map(lambda l: l.nb_signup_days, input_.libraries)))))

    print("Avg Rate time: {}".format(np.mean(input_.scores)))
    print("Std Rate time: {}".format(np.std(input_.scores)))

    print("Avg Book score: {}".format(np.mean(input_.scores)))
    print("Std Book score: {}".format(np.std(input_.scores)))

