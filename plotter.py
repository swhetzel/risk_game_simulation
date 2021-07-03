# this file is quick and dirty, please improve

import pandas as pd
import matplotlib.pyplot as plt
import main
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)



armySizes = list(range(5,51))
attWinProb = main.main()
attWinPer = [i/100 for i in attWinProb]

df = pd.DataFrame({'armies':armySizes, "attacker win prob":attWinPer})
df.plot.bar(x='armies',y='attacker win prob')

plt.show()