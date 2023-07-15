import pandas as pd
for i in range(0,10):
    print(i)



import pandas as pd
import numpy as np

# Example DataFrame
df = pd.DataFrame({
    'A': [1, -2, 3, -4],
    'B': [5, 6, -7, 8],
    'C': [-9, 10, -11, 12]
})

# Iterate over each row and change values less than 0 to null
for index, row in df.iterrows():
    for column in df.columns:
        if row[column] < 0:
            df.at[index, column] = np.nan

print(df)
