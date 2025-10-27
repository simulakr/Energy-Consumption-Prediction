import pandas as pd, numpy as np, datetime

def create_features(df):
    df["hour"] = df["date"].dt.hour
    df["day_of_week"] = df["date"].dt.dayofweek
    df["day_name"] = df["date"].dt.day_name()
    df["day_name"] = df["day_name"].astype(cat_type)
    df["quarter"] = df['date'].dt.quarter
    df["month"] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['day_of_year'] = df['date'].dt.dayofyear
    df['day_of_month'] = df['date'].dt.day
    df['week_of_year'] = df['date'].dt.isocalendar().week
    df["season"] = df["month"].apply(get_season)


df = create_features(df)
