#! /usr/bin/env bash

find accc -type d | grep -v "__pycache__" | xargs -I {} touch {}/__init__.py
find tests -type d | grep -v "__pycache__" | xargs -I {} touch  {}/__init__.py
