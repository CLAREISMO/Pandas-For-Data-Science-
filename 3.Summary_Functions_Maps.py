
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
