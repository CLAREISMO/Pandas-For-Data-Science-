
#* General features of our  new dataset
#* Describe() method in not_numeric values

import pandas as pd
import numpy as np

dfInt = pd.read_csv('International_sale_Report.csv', index_col = 0)
print(dfInt)
print(type(dfInt))

print(dfInt.Size.describe())
print(type('Size'))

print(dfInt.CUSTOMER.describe())
print(type('CUSTOMER'))

print(dfInt.DATE.describe())
print(type('Date'))

print(dfInt.PCS.describe())
print(type('PCS'))


#* Describe() method in numeric values

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)
print(type(dfEmer))
print(dfEmer.N_HIJOS_MENORES_15ANOS.describe())
