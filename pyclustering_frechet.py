# -*- coding: utf-8 -*-
"""pyclustering_frechet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GGmuRQU7aBG8PJGOXdfasByIrgMYLl-Q
"""

!pip install pyclustering

!pip install similaritymeasures

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import random
import time
from numpy.random import seed
from numpy.random import randint
from sklearn.metrics import mean_squared_error
import similaritymeasures as sm
from numpy.random import seed
from pyclustering.cluster.kmeans import kmeans
from pyclustering.cluster.kmeans import kmeans_visualizer
from pyclustering.cluster import cluster_visualizer_multidim
from pyclustering.utils.metric import type_metric, distance_metric
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

random.seed(1)
seed(1)
tic1 = time.time()

vectore1 = np.zeros((128, 2), dtype=np.float32)
vectore2 = np.zeros((128, 2), dtype=np.float32)
sample = np.zeros((50, 256), dtype=np.float32)

sample = pd.read_csv(r"/content/drive/My Drive/Created_dataset/samples.csv")
print("sample.shape",sample.shape)

# for i in range(50):
#     lat = np.random.uniform(low=-90, high=90, size=(128,))
#     long = np.random.uniform(low=-180, high=180, size=(128,))

#     lat = np.round(lat, 5)
#     long = np.round(long, 5)

#     sample[i, :] = np.concatenate((lat, long))


def ds_frechet(point1, point2):
    vectore1[:, 0] = point1[:128]
    vectore1[:, 1] = point1[128:]

    vectore2[:, 0] = point2[:128]
    vectore2[:, 1] = point2[128:]

    distance = sm.frechet_dist(vectore1, vectore2)
   
    return distance


# create K-Means algorithm with specific distance metric
user_function = lambda point1, point2: ds_frechet(point1, point2)
metric = distance_metric(type_metric.USER_DEFINED, func=user_function)

start_centers = kmeans_plusplus_initializer(sample, 4).initialize()
kmeans_instance = kmeans(sample, start_centers,  metric=metric)    #

# run cluster analysis and obtain results
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()
centers = kmeans_instance.get_centers()
print("clusters", clusters)


toc1 = time.time()
print("time of clustering : ", str((toc1 - tic1)*1000), " ms")