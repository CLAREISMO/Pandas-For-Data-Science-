#* displaying data with the head method()

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.head(7))
print(dataFrameMay.shape)


#* displaying data columns with the pd.set_option() function

import pandas as pd
dataFrameMay = pd.read_csv("May_2022.csv", index_col=0)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
print(dataFrameMay)

dataFrameMay = pd.read_csv("May_2022.csv", index_col=0)
pd.set_option("display.max_rows", 1)
print(dataFrameMay )

dataFrameMay = pd.read_csv("May_2022.csv", index_col=0)
pd.set_option("display.max_columns", 2) 
print(dataFrameMay )

#* Access the property of an object by accessing it as an attribute

#?Example1

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', header = 0,  index_col = 0)

print(dataFrameMay.Category)
print(dataFrameMay.Category.shape)


#* Access the property of an object by accessing it as an attribute

#?Example2

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', header = 0,  index_col = 0)

print(dataFrameMay.Sku)
print(dataFrameMay.Sku.shape)

#* Access the property of an object by accessing it as an attribute

#?Example3

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', header = 0,  index_col = 0)

print(dataFrameMay.Ajio MRP)
print(dataFrameMay.Ajio MRP.shape)


#* Acces by the indexing ([]) operator:

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', header = 0,  index_col = 0)

print(dataFrameMay['Category'])
print(dataFrameMay.Category.shape)

#* Accessing a specific value through the undefine operator ([]):

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', header = 0,  index_col = 0)
print(dataFrameMay['Category'][0])


#* iloc

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.iloc[0])


#* iloc: print rows and columns

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.iloc[ : , 0])

#* iloc: print rows and columns

#? 1 Example

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.iloc[ :3 , 0])

#* iloc: print rows and columns

# #? 2 Example

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.iloc[ 1:3 , 0])

# #* iloc: printing rows and columns through a list

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.iloc[ [0, 1, 2] , 0])

#* iloc: printing rows and columns with negative number in the indexing operator []

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.iloc[ -5 :  ])

# #* lOC

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.loc[0, 'Sku'])

#* Simpler operation with loc

import pandas as pd

dataFrameMay = pd.read_csv('May_2022.csv', index_col = 0)
print(dataFrameMay.loc[:, ['Sku', 'Category', 'Weight', 'TP' ]])

#* Method set_index()

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0)
dfMay.set_index('Catalog', inplace = True)
print(dfMay)

dfMay = pd.read_csv('May_2022.csv', index_col = 0)
dfMay.set_index('Catalog', inplace = True, drop = True, append = False, verify_integrity=False)
print(dfMay)

#* Conditional based selection 1:

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(dfMay.Catalog == 'Moments')


#* Conditional based selection 2:

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(dfMay.TP == '538') # this numerical data was stored as text!!!

#* To know the percentage of occurrence of a value

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(dfMay.loc[dfMay.TP == '538']) # this numerical data was stored as text!!!
print((dfMay.loc[dfMay.TP == '538']).shape)

#* Join two queries through &

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(dfMay.loc[(dfMay.TP == '538')  & (dfMay.Weight  <= '0.4')]) # this numerical data was stored as text!!!

#* Join two queries through | 

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(dfMay.loc[(dfMay.TP == '538')  | (dfMay.Weight  <= '0.4')]) # this numerical data was stored as text!!!

#* isin method
import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
filter1 = dfMay["Catalog"].isin(["Moments"])
print(filter1)

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
filter2 = dfMay["Catalog"].isin(["Moments", "", "Rozana", "Surmaya" ])
print(filter2)

#* Applying the iloc selector together with the isin method

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
filter_list = ['Moments', 'Rozana', 'Surmaya']
new_df = dfMay.loc[dfMay['Catalog'].isin(filter_list)]
print(new_df)


#* Filtering data with the isin method and operator(~)

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
filter_list = ['Moments', 'Rozana', 'Surmaya']
new_df = dfMay.loc[~dfMay['Catalog'].isin(filter_list)]
print(new_df)

#* isnull method

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 

print(dfMay.loc[dfMay.Catalog.isnull()])
print((dfMay.loc[dfMay.Catalog.isnull()]).shape)

#* notnull  method

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 

print(dfMay.loc[dfMay.Catalog.notnull()])
print((dfMay.loc[dfMay.Catalog.notnull()]).shape)

#* Null Register check in DF**

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(pd.isnull(dfMay))

#* Not-Null with Notna Register check in DF **

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 
print(dfMay.notna())

#* Assigning data

import pandas as pd

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 

dfMay['critic'] = 'everyone'
print(dfMay['critic'])
print(dfMay)

import pandas as pd

#* Iterable data Assignment 

dfMay = pd.read_csv('May_2022.csv', index_col = 0) 

dfMay['index_backwards'] = range(len(dfMay), 0, -1)
print(dfMay['index_backwards'])

print(dfMay)
