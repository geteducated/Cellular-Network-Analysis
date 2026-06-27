import numpy as np
import pandas as pd
import kagglehub

kagglehub.login()
#export KAGGLE_API_TOKEN=KGAT_fa20022d2a0efe8547032b4849d2414d

df=pd.read_csv(r'/kaggle/input/cellular-network-analysis-dataset/signal_metrics.csv')
print("Number of rows in dataset: ", len(df.index))
print("Number of columns in dataset: ", len(df.columns))
df.head(1)
