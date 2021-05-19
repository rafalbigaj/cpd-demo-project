from sklearn.cluster import DBSCAN

def my_dbscan(X):
    clustering = DBSCAN(eps=3, min_samples=2).fit(X)
    return clustering