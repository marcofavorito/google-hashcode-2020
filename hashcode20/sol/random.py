# -*- coding: utf-8 -*-
import random

from hashcode20.helpers import Input, Output, Slide, PictureType


def main(i: Input) -> Output:
    """Pick every picture at random, make a slide, and make a sequence."""
    random.shuffle(i.pictures)
    horizontal_pictures = list(filter(lambda x: x.type_ == PictureType.H, i.pictures))
    vertical_pictures = list(filter(lambda x: x.type_ == PictureType.V, i.pictures))
    paired_vertical_pictures = [[vertical_pictures[i], vertical_pictures[i+1]]
                                for i in range(0, len(vertical_pictures)//2, 2)]

    horizontal_slides = [Slide([h]) for h in horizontal_pictures]
    vertical_slides = [Slide(pair) for pair in paired_vertical_pictures]
    slides = horizontal_slides + vertical_slides
    random.shuffle(slides)
    return Output(slides)
