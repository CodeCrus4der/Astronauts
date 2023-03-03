import pandas as pd
import collections


def get_grads():
    df = pd.read_csv('astronauts.csv')
    grad_majors = pd.concat([df['Graduate Major'], df['Undergraduate Major']])
    grads = []
    for grad in grad_majors:
        if isinstance(grad, str):
            grad = grad.split('&')
            grad = [text.strip() for text in grad]
            for txt in grad:
                grads.append(txt)
    return grads


def main():
    print('A program az "astronauts.csv" fájlból beolvasott asztronauták végzettségei közül kírja a 3 leggyakoribbat.')
    grads = get_grads()
    print('Leggyakoribb végzettségek')
    for grad in collections.Counter(grads).most_common(3):
        print(f'{grad[0]}, {round(grad[1] / len(grads) * 100, 1)}%')
