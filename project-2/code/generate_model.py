from model import Model
import pandas as pd
import pickle
import time
import os
from urllib import request
import json


def main():
    # load data from github
    try:
        data_path = os.environ['DATA_PATH']
        meta_path = os.environ['META_PATH']
        df_playlist = pd.read_csv(data_path)

        print('[ML-INFO] data loaded from {}'.format(data_path))
        print('[ML-INFO] meta loaded from {}'.format(meta_path))

        # read version
        with request.urlopen(meta_path) as f:
            meta = json.load(f)
            version = meta['version']
    except:
        print('[ML-INFO] load data error')
        return
    try:
        print('[ML-INFO] start model generating')

        mdl = Model()
        mdl.train(df_playlist)
        mdl_with_metadata = dict(
            model=mdl,
            version=version,
            model_date=time.strftime('%Y-%m-%d %H:%M:%S')
        )
        print('[ML-INFO] model generating success')
        # save to pickle
        with open('./data/model.pkl', 'wb') as f:
            pickle.dump(mdl_with_metadata, f)
            print('[ML-INFO] model saved')
    except:
        print('[ML-INFO] error generating/saving model')


if __name__ == "__main__":
    main()
