import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ratings_processing():
    ratings_csv = pd.read_csv('../ml-latest-small/ratings.csv').drop('timestamp', 1).query('movieId<=10000')
    toystory_ratings = ratings_csv.query('movieId == 1').drop('movieId', 1)

    new_idx = [i for i in range(len(toystory_ratings))]
    toystory_ratings.insert(0, 'idx', new_idx)
    max_movie_id = ratings_csv['movieId'].max()
    max_user_idx = toystory_ratings['idx'].max()

    vector = []
    for i in range(max_user_idx + 1):
        vector.append(float(toystory_ratings.query('idx==' + str(i))['rating']))

    frames = []
    for i in toystory_ratings['userId']:
        frames.append(ratings_csv.query('userId==' + str(i)))

    matrix = np.zeros((max_user_idx + 1, max_movie_id + 1))

    for i in frames:
        for j in i.iterrows():
            movie_id = int(j[1]['movieId'])
            user_idx = int(toystory_ratings.query('userId==' + str(j[1]['userId']))['idx'])
            matrix[user_idx][movie_id] = float(j[1]['rating'])

    matrix = matrix[:, 2:]

    return matrix, vector


def linear_regression(X, Y):
    return np.linalg.lstsq(X, Y, rcond=None)[0]


'''
PROGRAM DLUGO LADUJE DANE Z PLIKU, TRZEBA POCZEKAC 
'''


def main():
    X, Y = ratings_processing()

    """    
    Pierwsza czesc zadania- regresja dla danego m
    """
    fig1, plots1 = plt.subplots(3)
    fig1.suptitle('Stosunek wartości oczekiwanych do regresjii:')
    z = 0

    for m in [10, 1000, len(X[0])]:
        temp = X[:, 0:m]
        temp = np.hstack([temp, np.ones((len(temp), 1))])
        coefficients = linear_regression(temp, Y)
        predictions = []

        for i in range(len(temp)):
            mark = 0
            for j in range(len(temp[0])):
                mark += coefficients[j] * temp[i][j]
            predictions.append(mark)

        plots1[z].plot([i for i in range(len(Y))], Y, 'o', markersize=3, color='red', label='Orginalne wartosci')
        plots1[z].plot([i for i in range(len(predictions))], predictions, 'o', markersize=1, color='blue',
                       label='Wartosci regresjii')
        plots1[z].vlines([i for i in range(len(predictions))], predictions, Y, colors="g",
                         linestyles="dashed", label='Roznica')
        plots1[z].set_title('m=' + str(m))
        z += 1

    plt.legend()
    plt.show()

    """    
    Druga czesc zadania- predykcje dla 15 userow
    """
    fig2, plots2 = plt.subplots(2, 3)
    fig2.suptitle('Stosunek wartości oczekiwanych do przewidywanych:')
    x, y = 0, 0

    for m in [10, 100, 200, 500, 1000, len(X[0])]:
        temp_x = X[0:200, 0:m]
        temp_x = np.hstack([temp_x, np.ones((len(temp_x), 1))])
        temp_y = Y[0:200]
        coefficients = linear_regression(temp_x, temp_y)
        subjects = X[200:215, 0:m]
        subjects = np.hstack([subjects, np.ones((len(subjects), 1))])
        predictions = []

        for i in range(len(subjects)):
            mark = 0
            for j in range(len(subjects[0])):
                mark += coefficients[j] * subjects[i][j]
            predictions.append(mark)

        if m >= 500:
            x = 1

        plots2[x, y].plot([i for i in range(len(Y[200:215]))], Y[200:215], 'o', markersize=3, color='red',
                          label='Orginalne wartosci')
        plots2[x, y].plot([i for i in range(len(predictions))], predictions, 'o', markersize=1, color='blue',
                          label='Wartosci regresjii')
        plots2[x, y].vlines([i for i in range(len(predictions))], predictions, Y[200:215], colors="g",
                            linestyles="dashed", label='Roznica')
        plots2[x, y].set_title('m=' + str(m))

        y = (y + 1) % 3

        print("Predykcje (prawa kolumna) dla m=", m)
        for i in range(len(Y[200:215])):
            print(Y[200:215][i], predictions[i])

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
