# the code generate mdl.pkl file.

import pandas as pd
from fpgrowth_py import fpgrowth


def trim_songs(song_name: str):
    # remove the "Remastered" kind of text
    song_name = song_name.split('-')[0].strip()
    return song_name


def is_subset(list_1, list_2):
    if set(list_1).issubset(set(list_2)):
        return True
    return False


def songs_df_to_list(df_songs):
    list_songs = df_songs['track_name'].unique().tolist()
    return list_songs


def recommend_from_rules(rules, songs):
    recommendation = []
    for rule in rules:
        song_source = rule[0]
        song_target = rule[1]
        score = rule[2]

        if is_subset(song_source, songs) and not is_subset(song_target, songs):
            for song in song_target:
                recommendation.append(
                    dict(
                        song=song,
                        score=score
                    )
                )
    return recommendation


class Model(object):
    def __init__(self) -> None:
        pass

    def train(self, df_playlist):
        df_playlist['track_name'] = df_playlist['track_name'].apply(trim_songs)
        gp_playlists = df_playlist.groupby('pid')

        list_playlists = []
        for _, album in gp_playlists:
            list_tracks = album['track_name'].unique().tolist()
            list_playlists.append(list_tracks)

        freq_item_set, rules = fpgrowth(
            list_playlists, minSupRatio=0.005, minConf=0)

        self.freq_item_set = freq_item_set
        self.rules = rules

    def predict(self, df_songs):
        recommendation = recommend_from_rules(
            rules=self.rules, songs=df_songs['track_name'].unique().tolist())

        if len(recommendation) == 0:
            recommendation_sorted = pd.DataFrame(dict(song=[], score=[]))
        else:
            recommendation_sorted = pd.DataFrame(recommendation).sort_values(
                'score', ascending=False).drop('score', axis=1).drop_duplicates()['song'].to_list()

        return recommendation_sorted

    def __call__(self, df_songs) -> list:
        return self.predict(df_songs)


def main():
    df_playlist_sample_ds1 = pd.read_csv(
        'data/playlist-sample-ds1.csv').drop_duplicates().dropna()
    df_songs = pd.read_csv('data/songs.csv').drop_duplicates().dropna()

    mdl = Model()
    mdl.train(df_playlist_sample_ds1)
    recommendation = mdl.predict(df_songs)
    print(recommendation)


if __name__ == '__main__':
    main()
