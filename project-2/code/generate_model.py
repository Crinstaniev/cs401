import os
import pickle
import time

import pandas as pd
from model import Model


def main():
    # load data from github
    try:
        data_path = os.environ['DATA_PATH']
        data_version = os.environ['DATA_VERSION']
        df_playlist = pd.read_csv(data_path)

        print(time.strftime('%Y-%m-%d %H:%M:%S'), '[ML-INFO] data loaded from {}'.format(data_path))
        print(time.strftime('%Y-%m-%d %H:%M:%S'), '[ML-INFO] data version: {}'.format(data_version))

    except:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), '[ML-INFO] load data error')
        return
    try:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), '[ML-INFO] start model generating')

        mdl = Model()
        mdl.train(df_playlist)
        mdl_with_metadata = dict(
            model=mdl,
            version=data_version,
            model_date=time.strftime('%Y-%m-%d %H:%M:%S')
        )
        print(time.strftime('%Y-%m-%d %H:%M:%S'), '[ML-INFO] model generating success')
        # save to pickle
        with open('./data/model.pkl', 'wb') as f:
            pickle.dump(mdl_with_metadata, f)
            print('[ML-INFO] model saved')
    except:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), '[ML-INFO] error generating/saving model')


if __name__ == "__main__":
    main()
