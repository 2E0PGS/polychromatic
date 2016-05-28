#!/usr/bin/env python3
"""
Fixes IDs in the keyboard SVG.
Inkscape hates it that there are multiple keyboard layouts in one svg

Run this after editing ../data/img/blackwidow-chroma-keyboard-layout.svg in Inkscape.
"""
import re, os

path = '../data/img/blackwidow-chroma-keyboard-layout.svg'

def regex_replace_func(match_obj):
    """
    String replace function for regex

    :param match_obj: re Match object

    :return: Edited string
    :rtype: str
    """
    row = match_obj.group('row')
    col = match_obj.group('col')

    return re.sub(r'id=".*"', 'id="key{0}-{1}"'.format(row, col), match_obj.group())

in_file = open(path, 'r').read()

edited_string = re.sub(r'(onclick="key\(this,(?P<row>[0-9]+),(?P<col>[0-9]+)\)".\s+id="g[0-9]+")', regex_replace_func, in_file, flags=re.DOTALL)
edited_string = re.sub(r'(id="g[0-9]+".\s+onclick="key\(this,(?P<row>[0-9]+),(?P<col>[0-9]+)\)")', regex_replace_func, edited_string, flags=re.DOTALL)

out_file = open(path + '.new', 'w')
out_file.write(edited_string)
out_file.close()

os.rename(path, path + '.bak')
os.rename(path + '.new', path)

print("")
