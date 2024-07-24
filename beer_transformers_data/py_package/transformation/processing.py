# py-package/transformation/processing.py

import pandas as pd

def normalize_beer_data(data):
    df = pd.DataFrame(data)
    # Normalização: Exemplo simples de renomear colunas
    df.rename(columns={
        'id': 'beer_id',
        'uid': 'beer_uid',
        'brand': 'beer_brand',
        'name': 'beer_name',
        'style': 'beer_style',
        'hop': 'beer_hop',
        'yeast': 'beer_yeast',
        'malts': 'beer_malts',
        'ibu': 'beer_ibu',
        'alcohol': 'beer_alcohol',
        'blg': 'beer_blg'
    }, inplace=True)
    return df
