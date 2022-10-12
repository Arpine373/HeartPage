import pandas as pd
heart_data = pd.read_csv('heart.csv')
print(heart_data.columns)
print(heart_data.head())
print(heart_data.tail())

print(heart_data.describe())
print(heart_data["sex"].head())
print(heart_data[["age","ca"]].head())

from sklearn.cluster import KMeans
model = KMeans(n_clusters= 5)
X = heart_data[["age", "sex"]]
model.fit(X)
labels = model.predict(X)
print(labels)

clusters = {}
i = 0
for label in labels:
    if label in clusters:
        clusters[label].append(X.loc[i])
    else:
        clusters[label]= X.loc[i]
    i += 1   

for cluster in clusters:
    print("Cluster: ", cluster) 
    for item in clusters[cluster]:
        print(item)
