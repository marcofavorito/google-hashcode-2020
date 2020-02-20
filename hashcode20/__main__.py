#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import inspect
import logging
import os
import importlib
import re

from hashcode20.helpers import Input, Output, score

logger = logging.getLogger("hashcode20")

PACKAGE_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))
ALGORITHMS = [s.replace(".py", "") for s in os.listdir(PACKAGE_DIRECTORY + "/sol") if re.match("[^_].+.py", s)]

parser = argparse.ArgumentParser("hashcode20", description="CLI util for Google Hash Code 2019. "
                                                           "It assumes the input provided in stdin.")

parser.add_argument("--alg", required=True, choices=ALGORITHMS, help="The algorithm to use for computing the solution.")
parser.add_argument("--in",  dest="in_file",  type=str, default=None, help="provide an input data file.")
parser.add_argument("--out", dest="out_file", type=str, default=None, help="provide an output data file.")

args = parser.parse_args()
solution = importlib.import_module('hashcode20.sol.{}'.format(args.alg))


def main():
    logger.debug("Chosen algorithm: {}".format(args.alg))
    input_ = Input.read(args.in_file)  # type: Input
    output = solution.main(input_)  # type: Output
    # logger.debug("Score of the solution: {}".format(score(input_, output)))
    output.write(args.out_file)


if __name__ == '__main__':
    main()
