from sklearn.pipeline import Pipeline
import datetime as dt
import pandas as pd
import numpy as np

# from special_score.cpu_calculation import super_complexs_score
from special_score.gpu_calculation import good_neighbours
from special_score.dbscan import my_dbscan
from preprocess_data import one_hot_encoder

reference_df = pd.read_csv("data/credit_risk_reference.csv")
input_df = reference_df.drop(['Risk'], axis=1)

transformer = one_hot_encoder(input_df)

# Training an unsupervised model
# Applying an unsupervised model for inference
dbscan = my_dbscan()

pipeline_linear = Pipeline([('transformer', transformer), ('dbscan', dbscan)])
model = pipeline_linear.fit(input_df)

print(input_df)

# One score that is compute intensive and has to run on GPU
# buddy = good_neighbours(input_df['account', 'date', 'volume'])

print(np.unique(dbscan.labels_))
