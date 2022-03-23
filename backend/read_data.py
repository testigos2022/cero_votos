
import pandas as pd
import os, sys
from os import walk

from settings import partidos

sys.path.append('../')

# Define working directory
d = os.path.dirname(os.getcwd())

def read_data():
    all_data = []
    for p in partidos:
        data = pd.read_json(d + '/cero-votos/data/' + partidos[0] + '.json')
        data['partido'] = p
        all_data.append(data)

    all_zeros = pd.concat(all_data)

    return all_zeros