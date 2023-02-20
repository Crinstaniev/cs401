from model import Model
import pandas as pd
import pickle
import time


def main():
    # read data
    try:
        df_playlist_sample_ds1 = pd.read_csv(
            './data/playlist.csv').drop_duplicates().dropna()
    except:
        print('read data error')

    try:
        mdl = Model()
        mdl.train(df_playlist_sample_ds1)
        mdl_with_metadata = dict(
            model=mdl,
            version='0.0.1',
            model_date=time.strftime('%Y-%m-%d %H:%M:%S')
        )
        # save to pickle
        with open('./data/model.pkl', 'wb') as f:
            pickle.dump(mdl_with_metadata, f)
    except:
        print('model generating error')


if __name__ == "__main__":
    main()
