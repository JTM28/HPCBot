""" Parser for credentials & configuration settings """

import os
import pathlib
import re
import ast
import logging
import datetime as dt


HPCBot = os.path.sep.join(os.path.normpath(__file__).split(os.path.sep)[:-3])


RUNTIME = {}

try:
    contents = [str(x) for x in list(pathlib.Path(HPCBot).iterdir())]
    if not re.search(r'credentials.txt', str(contents)):
        raise FileNotFoundError

except FileNotFoundError:
    print('RuntimeException: No "credentials.txt" file was found in the /Crate/ root directory')

pth_to_creds = os.path.join(HPCBot, 'credentials.txt')

RUNTIME_LIBS = {
    'brokers': [
        'rabbitmq',
        'zeromq',
        'mplite'
    ],

    'dbs': [
        'mongodb'
    ]
}


lines = open(pth_to_creds).readlines()


def _get_config_line(search, runtime_key, to_dict=True, split_on_find=True):
    for l in lines:
        if re.search(str(search), l):
            if split_on_find is True:
                if to_dict is True:
                    RUNTIME[runtime_key] = ast.literal_eval(str(l).split(search)[1])
                else:
                    RUNTIME[runtime_key] = str(l).split(search)[1]


_get_config_line('MONGO=', 'MONGO_URI', to_dict=False)
_get_config_line('GCP=', 'GCP_CREDS')




