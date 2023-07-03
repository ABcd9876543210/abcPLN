# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:20:21 2023

@author: Aditi
"""

import numpy as np
import re
import textdistance

import sklearn
from sklearn.cluster import AgglomerativeClustering

texts =['Reliance supermarket', 'Reliance hypermarket', 'Reliance', 'Reliance', 'Reliance downtown', 'Relianc market','Mumbai', 'Mumbai Hyper', 'Mumbai dxb', 'mumbai airport','k.m trading', 'KM Trading', 'KM trade', 'K.M. Trading', 'KM.Trading']

def normalize(texts):
    return re.sub('[^a-z0-9]+','',texts.lower())

def grp_text (texts):
    normalixe_txt = np.array([normalize(text) for text in texts])
    dist = 1 - np.array([[textdistance.jaro_winkler(one, another) for one in normalixe_txt] for another in normalixe_txt])
    clustering = AgglomerativeClustering(distance_threshold=0.4, affinity="precomputed", linkage="complete", n_clusters=None).fit(dist)
    centers = dict()
    for clust_id in set(clustering.labels_):
        ind = clustering.labels_ == clust_id
        center = dist[:,ind][ind].sum(axis=1)
        centers[clust_id] = normalixe_txt[ind][center.argmin()]
    return [centers[i] for i in clustering.labels_]
print(grp_text(texts))