import sys
import os
import site
import pathlib
import re

from src.conf import TOP_LEVEL


def _get_all_modules():
    modules = set()
    for folder in site.getsitepackages():
        for pkg in pathlib.Path(folder).iterdir():
            pkg = str(pkg).split(os.path.sep)[-1].strip()
            modules.add(pkg)
    return modules


USER_MODULES = _get_all_modules()


def _ensure_module(pkg: str):
    return True if pkg in USER_MODULES or pkg in sys.modules else False



try:
    REQUIRED = open(os.path.join(TOP_LEVEL, 'requirements.txt')).readlines()

except FileNotFoundError:
    print("Missing requirements.txt file")


missing = []

if 'REQUIRED' in globals().keys():
    for each in globals()['REQUIRED']:
        if len(each.replace('\n', '')) > 0:
            each = each.replace('\n', '')
            if re.search(r'>', str(each)):
                each = str(each).split('>')[0]
            if re.search(r'=', str(each)):
                each = str(each).split('=')[0]
            if not _ensure_module(str(each).strip()):
                missing.append(each)

try:
    if len(missing) > 0:
        raise RuntimeWarning

except RuntimeWarning:
    print('%s Dependencies not found %s' % (str(len(missing)), str(missing)))

