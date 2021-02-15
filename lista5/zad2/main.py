import numpy as np
import pandas as pd


def ratings_processing():
    ratings_csv = pd.read_csv('../ml-latest-small/ratings.csv').drop('timestamp', 1).query('movieId<=10000')
    max_user = ratings_csv['userId'].max()
    max_movie = ratings_csv['movieId'].max()
    matrix = np.zeros((max_user + 1, max_movie + 1))

    for j in ratings_csv.iterrows():
        matrix[int(j[1]['userId'])][int(j[1]['movieId'])] = float(j[1]['rating'])

    return matrix


def get_movie_title(movie_id):
    movies_csv = pd.read_csv('../ml-latest-small/movies.csv').drop('genres', 1).query('movieId<=10000')
    name = movies_csv.query('movieId==' + str(movie_id))

    title = None
    for i in name.iterrows():
        title = i[1]['title']

    return title


def get_my_ratings(x):
    vector = np.zeros((1, x))
    vector[0][2571] = 5
    vector[0][32] = 4
    vector[0][260] = 5
    vector[0][1097] = 4

    return vector


def main():
    rating_matrix = ratings_processing()
    my_ratings = get_my_ratings(len(rating_matrix[0]))

    print(np.nan_to_num(rating_matrix / np.nan_to_num(np.linalg.norm(rating_matrix, axis=0))))
    z = np.nan_to_num(np.dot(np.nan_to_num(rating_matrix / np.nan_to_num(np.linalg.norm(rating_matrix, axis=0))),
                             np.nan_to_num(my_ratings.T / np.nan_to_num(np.linalg.norm(my_ratings.T, axis=0)))))

    X = np.nan_to_num(rating_matrix / np.nan_to_num(np.linalg.norm(rating_matrix, axis=0)))
    Z = np.nan_to_num(z / np.nan_to_num(np.linalg.norm(z)))
    recommendations = np.nan_to_num(np.dot(X.T, Z))


    for i in [260, 2571, 1196, 1210, 1097, 32, 1198, 1240, 1270]:
        print(recommendations[i][0], ' ', get_movie_title(i))


if __name__ == '__main__':
    main()
