# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

import logging
from enum import Enum
from typing import List, Set, Dict

logger = logging.getLogger(__name__)


class Input(object):
    """This class manages the input of the problem."""

    def __init__(self):
#        self._build_indexes()

#    def _build_indexes(self):
#        logger.debug("Start building indexes...")
#        self.id_to_pic = dict(enumerate(self.pictures))
#        self.type_to_pics = {PictureType.H: [], PictureType.V: []}  # type: Dict[PictureType, List[int]]
#        self.numtag_to_pics = defaultdict(lambda: [])  # type: Dict[int, List[int]]
#
#        self.tag_to_idx = {}  # type: Dict[str, int]
#        self.idx_to_tag = {}  # type: Dict[int, str]
#
#        self.tag_to_pics = defaultdict(lambda: set())  # type: Dict[int, Set[int]]
#        self.tag_to_count = defaultdict(lambda: 0)  # type: Dict[int, int]
#
#        for i, p in enumerate(self.pictures):
#            self.type_to_pics[p.type_].append(i)
#            self.numtag_to_pics[len(p.tags_str)].append(i)
#
#            for t in p.tags_str:
#                idx = self.tag_to_idx.get(t, len(self.tag_to_idx))
#                self.idx_to_tag[idx] = t
#                self.tag_to_idx[t] = idx
#                self.tag_to_pics[idx].add(p.id_)
#                self.tag_to_count[idx] += 1
#
#            p.tags_idx = set(map(lambda t: self.tag_to_idx[t], p.tags_str))
#
#        logger.debug("Done!")

    @classmethod
    def read(cls, filename=None):
        """Returns an Input instance. If filename is None, read from stdin."""
        if filename is None:
            lines = sys.stdin
        else:
            lines = iter(open(filename).readlines())

        # line = next(lines)
        # N = int(line.strip())

        # pictures = []
        # for id_ in range(N):
        #     tokens = next(lines).strip().split(" ")

        #     picture_type = PictureType(tokens[0])

        #     tags = tokens[2:]
        #     picture = Picture(id_, picture_type, tags)
        #     pictures.append(picture)

        # assert len(pictures) == N
        # logger.debug("Parsed input: {} pictures.".format(N))
        # return Input(N, pictures)


class Output(object):
    """This class manages the output of the problem."""

    def __init__(self, slides: List[Slide]):
        self.slides = slides

    def write(self, filename=None) -> None:
        if filename is not None:
            file = open(filename, "w")
        else:
            file = None
        logger.debug("Printing to {}...".format("stdout" if file is None else filename))
        print(len(self.slides), file=file)
        for s in self.slides:
            if len(s.pictures) == 1:
                print("{}".format(s.pictures[0].id_), file=file)
            else:
                print("{} {}".format(s.pictures[0].id_, s.pictures[1].id_), file=file)

    @classmethod
    def read(cls, in_file=None, solution_file=None):
        i = Input.read(in_file)

        if solution_file is None:
            lines = sys.stdin
        else:
            lines = iter(open(solution_file).readlines())

        # line = next(lines)
        # N = int(line.strip())

        # slideshow = []
        # for id_ in range(N):
        #     tokens = map(int, next(lines).strip().split(" "))
        #     pictures = [i.id_to_pic[idx] for idx in tokens]
        #     slideshow.append(Slide(pictures))

        return Output(slideshow)

    def score(self) -> int:
        """Score the output."""
        raise NotImplementedError

