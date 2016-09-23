import pandas as pd
import sys

col = sys.argv[1]
fileName = sys.argv[2]

df = pd.read_table(fileName)

print df
