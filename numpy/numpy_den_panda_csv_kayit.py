import pandas as pd
import numpy as np


time1 = np.arange(0, 10, 0.01)

amplitude = np.sin(time1)

dict = {"zaman": time1, "genlik": amplitude}

df = pd.DataFrame(dict)
df.to_csv('file2.csv', index=False)
