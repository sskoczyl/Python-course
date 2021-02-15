import numpy as np
from scipy.sparse import lil_matrix
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def ratings_processing():
    ratings_csv = pd.read_csv('../ml-latest-small/ratings.csv')  # .query('movieId<=10000')
    max_user = ratings_csv['userId'].max()
    max_movie = ratings_csv['movieId'].max()
    data = ratings_csv.loc[ratings_csv["movieId"] <= max_movie, ['userId', 'movieId', 'rating']].to_numpy()

    matrix = np.zeros((max_user + 1, max_movie + 1))
    for j in data:
        matrix[int(j[0])][int(j[1])] = float(j[2])

    matrix = lil_matrix(matrix)

    return matrix


def get_movie_title(movie_id):
    movies_csv = pd.read_csv('../ml-latest-small/movies.csv')  # .query('movieId<=10000')
    name = movies_csv.loc[ movies_csv['movieId'] == movie_id, ['title']].to_numpy()

    return name[0][0]


def get_my_ratings(x):
    vector = lil_matrix((1, x), dtype=np.float).toarray()
    vector[0][2571] = 5
    vector[0][32] = 4
    vector[0][260] = 5
    vector[0][1097] = 4

    vector = lil_matrix(vector)

    return vector


def main():
    rating_matrix = ratings_processing()
    my_ratings = get_my_ratings(len(rating_matrix.toarray()[0]))
    profile = cosine_similarity(rating_matrix, my_ratings, dense_output=False)

    recommendations = cosine_similarity(rating_matrix.transpose(), profile.transpose(), dense_output=False)

    for i in [260, 2571, 1196, 1210, 1097, 32, 1198, 1240, 1270]:
        print(recommendations[i][0].toarray()[0][0], ' ', get_movie_title(i))


if __name__ == '__main__':
    main()
