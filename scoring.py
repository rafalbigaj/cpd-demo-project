import datetime as dt

from special_score.cpu_calculation import super_complexs_score
from special_score.gpu_calculation import good_neigbour
from special_score.dbscan import my_dbscan


def compute_score(trades_prepared_filtered_df):
    # One score representing expert knowledge. Should use models
    scores_df['individual_score'] = super_complexs_score(scores_df)
    return scores_df

# Training an unsupervised model
# Applying an unsupervised model for inference
dbscan_model = my_dbscan(trades_prepared_filtered_df)

# One score that is compute intensive and has to run on GPU
buddy = good_neigbour(trades_prepared_filtered_df['account', 'date', 'volume'])