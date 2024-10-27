import pandas as pd

csv_file_path = 'games.csv'
videogames_output_file_path = 'videogames.txt'
genres_output_file_path = 'genres.txt'
softwarehouses_output_file_path = 'team.txt'

def extract_unique_items_from_list_column(column_name, output_file_path):
    df = pd.read_csv(csv_file_path)
    df[column_name] = df[column_name].apply(lambda x: eval(x) if isinstance(x, str) else x)
    print(df[column_name])
    all_items = set(item for sublist in df[column_name] if isinstance(sublist, list) for item in sublist )
    all_items_list = list(all_items)

    with open(output_file_path, 'w') as file:
        for item in all_items_list:
            file.write(f"\"{item}\"\n")

def extract_items_from_column(column_name, output_file_path):
    df = pd.read_csv(csv_file_path)
    all_items_list= list(item for item in df[column_name])

    with open(output_file_path, 'w') as file:
        for item in all_items_list:
            file.write(f"\"{item}\"\n")

extract_items_from_column("Title", videogames_output_file_path)
print(f"Videogames written into {videogames_output_file_path}")
extract_unique_items_from_list_column("Genres", genres_output_file_path)
print(f"Genres written into {genres_output_file_path}")
extract_unique_items_from_list_column("Team", softwarehouses_output_file_path)
print(f"Software houses written into {softwarehouses_output_file_path}")

