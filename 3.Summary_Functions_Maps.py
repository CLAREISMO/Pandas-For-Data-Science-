
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



#* mean() function
import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)
print(type(dfEmer))
print(dfEmer.N_HIJOS_MENORES_15ANOS.mean())



#* unique() function

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)
print(type(dfEmer))
print(dfEmer.N_HIJOS_MENORES_15ANOS.unique())



#* VALUE_COUNTS()
import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)
print(type(dfEmer))
print(dfEmer.N_HIJOS_MENORES_15ANOS.value_counts())



#* map() method
import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)
print(type(dfEmer))
print(dfEmer.N_HIJOS_MENORES_15ANOS.mean())

dfEmer_N_HIJOS_MENORES_15ANOS_mean = dfEmer.N_HIJOS_MENORES_15ANOS.mean()
dfEmer.N_HIJOS_MENORES_15ANOS.map(lambda p: p - dfEmer_N_HIJOS_MENORES_15ANOS_mean)
print(dfEmer_N_HIJOS_MENORES_15ANOS_mean)


#* deeper in to the map() method

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)
print(type(dfEmer))
print(dfEmer.N_HIJOS_MENORES_15ANOS.mean())

dfEmer_N_HIJOS_MENORES_15ANOS_mean = dfEmer.N_HIJOS_MENORES_15ANOS.mean()
dfEmer.N_HIJOS_MENORES_15ANOS.map(lambda p: p - dfEmer_N_HIJOS_MENORES_15ANOS_mean)
print(dfEmer_N_HIJOS_MENORES_15ANOS_mean)
print(dfEmer.N_HIJOS_MENORES_15ANOS.map(lambda p: p - dfEmer_N_HIJOS_MENORES_15ANOS_mean))


#*  apply() method

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 

dfEmer_N_HIJOS_MENORES_15ANOS_mean = dfEmer.N_HIJOS_MENORES_15ANOS.mean()
dfEmer.N_HIJOS_MENORES_15ANOS.map(lambda p: p - dfEmer_N_HIJOS_MENORES_15ANOS_mean)
print(dfEmer_N_HIJOS_MENORES_15ANOS_mean)
print(dfEmer.N_HIJOS_MENORES_15ANOS.map(lambda p: p - dfEmer_N_HIJOS_MENORES_15ANOS_mean))


def remean_N_HIJOS_MENORES_15ANOS(row):
    row.N_HIJOS_MENORES_15ANOS = row.N_HIJOS_MENORES_15ANOS - dfEmer_N_HIJOS_MENORES_15ANOS_mean
    return row

print(dfEmer.apply(remean_N_HIJOS_MENORES_15ANOS, axis='columns'))


#* Original DataFrame

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 
print(dfEmer)

#* Common mapping operations as built-ins

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 

dfEmer_N_HIJOS_MENORES_15ANOS_mean = dfEmer.N_HIJOS_MENORES_15ANOS.mean()
print(dfEmer.N_HIJOS_MENORES_15ANOS - dfEmer_N_HIJOS_MENORES_15ANOS_mean)

#* Common mapping operations as built-ins

import pandas as pd
import numpy as np

dfEmer = pd.read_csv('population.csv', index_col = 0) 

dfEmer_N_HIJOS_MENORES_15ANOS_mean = dfEmer.N_HIJOS_MENORES_15ANOS.mean()
print(dfEmer.N_HIJOS_MENORES_15ANOS - dfEmer_N_HIJOS_MENORES_15ANOS_mean)


#* operators applied to the combination of information

import pandas as pd
import numpy as np

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 

print(dfMay.TP + " - " + dfMay.Weight)
print(dfMay.TP + " < " + dfMay.Weight)







