# this file is quick and dirty, please improve

import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)

armySizes = list(range(5,51))
attWinPer = [40.5, 40.9, 45.4, 47.7, 51.7, 52.5, 55.2, 56.6, 58.9, 62.4, 58.8, 59.8, 62.7, 62.6, 63.9, 64.9, 66.2, 63.0, 67.6, 68.4, 67.5, 71.0, 68.5, 68.7, 70.8, 71.7, 71.1, 71.2, 70.2, 73.1, 71.2, 75.1, 77.0, 72.7, 75.6, 75.4, 78.0, 79.8, 79.2, 78.4, 76.4, 79.4, 78.1, 81.8, 80.0, 81.6]

df = pd.DataFrame({'armies':armySizes, "attacker win prob":attWinPer})
df.plot.bar(x='armies',y='attacker win prob')

plt.show()