import pandas as pd
import collections


def get_major_list():
    df = pd.read_csv('astronauts.csv')
    major_series = pd.concat([df['Graduate Major'], df['Undergraduate Major']])
    major_list = []
    for major in major_series :
        if isinstance(major, str):
            major = major.split('&')
            major = [text.strip() for text in major]
            for txt in major:
                major_list.append(txt)
    return major_list


def main():
    print('A program az "astronauts.csv" fájlból beolvasott asztronauták végzettségei közül kírja a 3 leggyakoribbat.')
    major_list = get_major_list()
    print('Leggyakoribb végzettségek:')
    for major_tuple in collections.Counter(major_list).most_common(3):
        print(f'{major_tuple[0]}, {round(major_tuple[1] / len(major_list) * 100, 1)}%')
