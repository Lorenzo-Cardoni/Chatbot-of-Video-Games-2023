import os
import shutil
import pandas as pd

small_df = pd.read_csv('games.csv')
big_df = pd.read_csv('./bigger/games.csv')

small_df['BigId'] = 0

not_found = []


for index, small_row in small_df.iterrows():
    result = big_df[big_df['name'] == small_row['Title']]

    if not result.empty:
        big_row = result.iloc[0]
    else:
        print(f"No game named {small_row['Title']} found")
        continue

    game_id = big_row['id']
    small_df.at[index, 'BigId'] = game_id

    source_file = f'./bigger/posters/{game_id}.jpg'
    destination_file = f'./posters/{game_id}.jpg'

    try:
        if not os.path.exists(source_file):
            raise FileNotFoundError(f'Source file not found: {source_file}')
        shutil.copy(source_file, destination_file)
    except Exception as e:
        print(f'Error: {e}')

small_df.to_csv('new_games.csv', index=False)
