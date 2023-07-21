#* Creating DataFrame with int values
import pandas as pd

DataFra = pd.DataFrame({"Yes" : [50 , 21], "No": [131,2]})
print(DataFra)

#* Creating DataFrame with strings  values
import pandas as pd

DataFra1 = pd.DataFrame(({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))
print(DataFra1)

#*Creating a DataFrame with an index
import pandas as pd

x = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
                  'Sue': ['Pretty good.', 'Bland.']},
                 index=['Product A', 'Product B'])
print(x)

#* Creation of a Panda series

import pandas as pd

Serie1 = pd.Series([1, 2, 3, 4, 5])
print(Serie1)

#*Creating a Pandas Serie with an index
import pandas as pd

Serie2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(Serie2)


#* Read to csv file
import pandas as pd

datos = pd.read_csv('May_2022.csv', header = 0)
print(datos)

print(datos.shape)


#* Read the first 5 records of the CSV file 

import pandas as pd

datos = pd.read_csv('May_2022.csv', header = 0, index_col = 0)
print(datos.head())
print(datos.shape)
