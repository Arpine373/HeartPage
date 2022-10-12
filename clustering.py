import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def get_clusters(data_file = 'heart.csv', clusters_number = 2):
    heart_data = pd.read_csv(data_file)

    model = KMeans(n_clusters= clusters_number)
    X = heart_data.drop('target', axis=1)
    model.fit(X)
    clusters = model.predict(X)
    
    cluster_map = pd.DataFrame()
    cluster_map['data_id'] = heart_data.index.values
    cluster_map['cluster_id'] = clusters # model.labels_

    def get_cluster_indexes(cluster_id):
        cluster_map_subset = cluster_map[cluster_map.cluster_id == cluster_id]
        return np.array(cluster_map_subset['data_id'])

    clusters_rows_ids = list(map(get_cluster_indexes, set(clusters)))
    clusters_dfs = list(map(lambda i: heart_data.iloc[i], clusters_rows_ids))
    return clusters_dfs