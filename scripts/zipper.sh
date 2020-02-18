#!/usr/bin/env bash
rm solution.zip
zip -r solution.zip hashcode20/* \
    README.md \
    Pipfile \
    Pipfile.lock \
    .gitignore \
    LICENSE \
    zipper.sh \
    scripts/* \
    SUBMISSION \
    setup.py \
    data/.gitkeep \
    out/.gitkeep \
    -x *__pycache__* *.pyc
