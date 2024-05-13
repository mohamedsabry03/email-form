import pandas as pd
import numpy as np

np.random.seed(259)
collected_emails = pd.read_csv('collected_emails.csv')
print(np.random.choice(collected_emails.iloc[:,0]))