import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def findNearest(data_file, test_value):
    pass

data = pd.read_excel('TestFile1.xlsx')
plt.plot(data['Height'], data['HasCandy'], '.')
plt.ylabel('Height')
plt.show()
