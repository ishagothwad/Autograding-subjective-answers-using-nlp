# src/evaluate.py
import pandas as pd
from src.scoring import compute_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy.stats import pearsonr

def evaluate_csv(path, method='bert'):
    df = pd.read_csv(path)
    preds, humans = [], []
    for i, row in df.iterrows():
        res = compute_score(row['model_answer'], row['student_answer'], method=method)
        preds.append(res['final_score'])
        if 'human_score' in row and not pd.isna(row['human_score']):
            humans.append(row['human_score'])
    if humans:
        mae = mean_absolute_error(humans, preds[:len(humans)])
        mse = mean_squared_error(humans, preds[:len(humans)])
        corr, _ = pearsonr(humans, preds[:len(humans)])
        return dict(mae=mae, mse=mse, pearson=corr)
    return dict(message="No human scores to evaluate.")
