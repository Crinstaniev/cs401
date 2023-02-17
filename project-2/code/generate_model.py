from model import Model
import pandas as pd
import pickle
import time


def main():
    # read data
    df_playlist_sample_ds1 = pd.read_csv(
        'data/playlist-sample-ds1.csv').drop_duplicates().dropna()

    mdl = Model()
    mdl.train(df_playlist_sample_ds1)
    mdl_with_metadata = dict(
        model=mdl,
        version='0.0.1',
        model_date=time.strftime('%Y-%m-%d %H:%M:%S')
    )
    # save to pickle
    with open('model.pkl', 'wb') as f:
        pickle.dump(mdl_with_metadata, f)


if __name__ == "__main__":
    main()
