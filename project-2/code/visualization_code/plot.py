import pandas as pd
import matplotlib.pyplot as plt

data = [
    {
        'data': 'result/modify_replica_num.json',
        'title': 'Modify Replica Number',
    },
    {
        'data': 'result/update_code.json',
        'title': 'Update Code',
    },
    {
        'data': 'result/update_data.json',
        'title': 'Update Data',
    },
]


def draw(data, title):
    print("data: {}, title: {}".format(data, title))
    df = pd.read_json(data, lines=True)

    df['status'] = df['status'].apply(lambda x: 0 if x == 'offline' else 1)

    df = df.iloc[30:50]

    df.plot(y='status', color='green', lw=2)

    for i in range(31, 50):
        if df.loc[i, 'status'] != df.loc[i-1, 'status']:
            plt.axvline(x=i, color='black', ls='--')
            print(
                f"Status change from {df.loc[i-1, 'status']} to {df.loc[i, 'status']} at timestamp {df.loc[i, 'time']}")
            plt.text(i, df.loc[i, 'status'],
                     f"{'online' if df.loc[i, 'status'] == 1 else 'offline'}")

    plt.title(title)
    plt.savefig('figures/{}.png'.format(data.split('/')[-1].split('.')[0]))


for d in data:
    draw(d['data'], d['title'])
