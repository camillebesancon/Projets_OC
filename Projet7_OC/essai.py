import pandas as pd

test=pd.read_csv('final_data/df_train.csv', sep=',').drop(columns="Unnamed: 0").sample(1)
test.to_csv(r'final_data/model_outputs.csv')
