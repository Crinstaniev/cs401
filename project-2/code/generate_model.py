from model import Model
import pandas as pd
import pickle
import time
import os


def main():
    # load data from github
    try:
        data_path = os.environ['DATA_PATH']
        meta_path = os.environ['META_PATH']
        df_playlist = pd.read_csv(data_path)
    except:
        print('[ML-INFO] load data error')
        return
    try:
        print('[ML-INFO] start model generating]')
        mdl = Model()
        mdl.train(df_playlist)
        mdl_with_metadata = dict(
            model=mdl,
            version=os.environ['VERSION'],
            model_date=time.strftime('%Y-%m-%d %H:%M:%S')
        )
        print('[ML-INFO] model generating success')
        # save to pickle
        with open('./data/model.pkl', 'wb') as f:
            pickle.dump(mdl_with_metadata, f)
            print('[ML-INFO] model saved')
    except:
        print('[ML-INFO] model generating error')


if __name__ == "__main__":
    main()
