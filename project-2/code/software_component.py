# %%
import pandas as pd
from fpgrowth_py import fpgrowth

df_playlist_sample_ds1 = pd.read_csv(
    'data/playlist-sample-ds1.csv').drop_duplicates().dropna()
df_playlist_sample_ds2 = pd.read_csv(
    'data/playlist-sample-ds2.csv').drop_duplicates().dropna()
df_songs = pd.read_csv('data/songs.csv').drop_duplicates().dropna()

# %%
gp_playlists = df_playlist_sample_ds1.groupby('pid')

# %%
# construct item list
list_playlists = []

for _, album in gp_playlists:
    list_tracks = album['track_name'].unique().tolist()
    list_playlists.append(list_tracks)
# %%
# prediction using fpgrowth
freq_item_set, rules = fpgrowth(list_playlists, minSupRatio=0.01, minConf=0.01)

# %%


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


# %%
recommendation = recommend_from_rules(
    rules=rules, songs=df_songs['track_name'].unique().tolist())

# %%
recommendation_sorted = pd.DataFrame(
    recommendation).sort_values('score', ascending=False).drop('score', axis=1).drop_duplicates()['song'].to_list()
# %%
