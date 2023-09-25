

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/da26ede4-3224-4e66-8c46-a786ce6d4bb6)<img src="https://media.tenor.com/Nk6wJhshPaMAAAAi/dm4uz3-foekoe.gif" width="60px">


**This repository contains the Pandas by Kaggle course and all the knowledge I have acquired over time on this subject. Also implemented in the VSC code editor in order to observe all the requirements and behavior of the code in a real production environment.**

**You can see the respective outputs in this file and the code in the Python language you will get for each topic in the repository files.**

**Enjoy it**




## **1. Creating, Reading, and Writing**

### **Introduction**

Pandas is a Python library specialized in handling and analyzing data structures. Pandas define new data structures based on the arrays of the NumPy library but with new functionalities. It also provides flexible, high-performance data structures and tools for data analysis. In this micro-course, you'll learn all about pandas, the most popular Python library for data analysis.

Along the way, you'll complete several hands-on exercises with real-world data. We recommend that you work on the exercises while reading the corresponding tutorials. In this tutorial, you will learn how to create your own data, along with how to work with data that already exists.

To use pandas, you'll typically start with the following line of code.

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/7f4f2ee2-79ad-4a69-9c3b-4792e04f12eb)


### **Creating data**
There are two core objects in pandas: the DataFrame and the Series.

**DataFrame**: A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.
																				
For example, consider the following simple DataFrame:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/2123b696-743f-42ed-92ea-4393907974ce)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/8ddda458-53d8-4c2d-8869-775c577ac922)


+ In this example, the "0, No" entry has the value of 131. The "0, Yes" entry has a value of 50, and so on. 
+ DataFrame entries are not limited to integers. For instance, here's a DataFrame whose values are strings:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/9d4f3357-bdda-4d08-b0f1-ac064756377c)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/8537ddeb-3de3-4140-8247-ec77f88fc757)

+ We are using the pd.DataFrame() constructor to generate these DataFrame objects. The syntax for declaring a new one is a dictionary whose keys are the column names (Bob and Sue in this example), and whose values are a list of entries. This is the standard way of constructing a new DataFrame, and the one you are most likely to encounter.
+ The dictionary-list constructor assigns values to the column labels, but just uses an ascending count from 0 (0, 1, 2, 3, ...) for the row labels. Sometimes this is OK, but oftentimes we will want to assign these labels ourselves.
+ The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/af0a6495-adb2-4242-9b87-5785da65dc2c)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/bd83f202-acb0-4766-8206-6785bc5ffc73)

**Series**: A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact, you can create one with nothing more than a list:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/2eeed9bc-fb9d-43a7-bc1d-457199a1e5c2)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/f3d425b7-187c-4003-b8d0-95bd5dd8590c)

A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/22aa96f0-2ee5-4543-8a90-5d525a0f93e0)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/a2b62018-7bca-42dc-9823-ba754f5eed86)

The Series and the DataFrame are intimately related. It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together". We'll see more of this in the next section of this tutorial.


### **Reading data files**

Being able to create a DataFrame or Series by hand is handy. But, most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.

Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file. When you open a CSV file you get something that looks like this:


![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/b70522db-078a-4b01-b662-5d2734f2cc20)



So a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.
Let's now set aside our toy datasets and see what a real dataset looks like when we read it into a DataFrame. We'll use the pd.read_csv() function to read the data into a DataFrame. This goes thusly:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/8f02e5f3-8a3c-421c-b807-a7e248ea1a31)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/a7301f4e-b60b-4433-954a-fba0054109b3)

We can use the shape attribute to check how large the resulting DataFrame is:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/38062534-4d7e-40b0-b256-54c53f4d3728)

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/70278072-869d-42e1-a320-a9afb3798495)

So our new DataFrame has 1330 records split across 17 different columns. 

We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/1e80d0a5-9dc5-4795-a81f-a94c18014546)

## **2. Indexing, Selecting & Assigning**

### **Introduction**

The data scientists do this dozens of times a day. You can, too!

Selecting specific values of a pandas DataFrame or Series to work on is an implicit step in almost any data operation you'll run, so one of the first things you need to learn in working with data in Python is how to go about selecting the data points relevant to you quickly and effectively.

### **Selecting data**
There are two core objects in pandas: the DataFrame and the Series.

**head() method**: The first way we as data scientists can display a maximum number of columns is with the method head(x) where x is the number of records we want to display.

![image](https://github.com/CLAREISMO/test/assets/63759427/a6ca679e-c60d-470c-a52a-7113ae6b82bb)

**pd.set_option() function**: This is a function in pandas that allows you to set specific options for the behavior of the library, such as the number of rows or columns to be displayed in the output.

![image](https://github.com/CLAREISMO/test/assets/63759427/ee8c1c18-ea9e-4588-89a0-cca650c23a78)

![image](https://github.com/CLAREISMO/test/assets/63759427/b7582614-b16d-4b6f-90dd-92a9ddba64db)

![image](https://github.com/CLAREISMO/test/assets/63759427/e7c08e26-588e-4e4d-8871-5dba1e97316b)


### **Native accessors**

Native Python objects provide good ways of indexing data. Pandas carry all of these over, which helps make it easy to start with.

In Python, we can access the property of an object by accessing it as an attribute. A book object, for example, might have a title property, which we can access by calling book.title. Columns in a Pandas DataFrame work in much the same way.

![image](https://github.com/CLAREISMO/test/assets/63759427/b23dd4af-1abf-4b87-b6b6-7715be263919)

Let's see a second example with the Sku column:

![image](https://github.com/CLAREISMO/test/assets/63759427/1e00ccb1-e145-4095-b1f5-42452efd0c9f)

Let's see a third example with the column Ajio MRP

![image](https://github.com/CLAREISMO/test/assets/63759427/3c266f16-ca09-4933-a1c1-403b856109b9)

If the attribute name has spaces in it, as in this case "Ajio MRP", we can't access it in this way because it will generate an error. We can access it by the column number or by the indexing operator ([]).

**the indexing ([]) operator**: If we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:

![image](https://github.com/CLAREISMO/test/assets/63759427/dbd26057-6837-446a-99e8-b0d1a65f05c3)

These are the two ways of selecting a specific Series out of a DataFrame. Neither of them is more or less syntactically valid than the other, but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

Doesn't a Pandas Series look kind of like a fancy dictionary? It pretty much is, so it's no surprise that to drill down to a single specific value, we need only use the indexing operator [] once more:

![image](https://github.com/CLAREISMO/test/assets/63759427/d90835ea-1667-4871-ada9-3939032fb73d)


### **Indexing in Pandas**

The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem. As a novice, this makes them easy to pick up and use. 
However, Pandas have their own accessor operators, loc and iloc. For more advanced operations, these are the ones you're supposed to be using.

**Index-based selection**

**iloc**: Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.

To select the first row of data in a DataFrame, we may use the following:

![image](https://github.com/CLAREISMO/test/assets/63759427/29ff61b9-a3f5-4103-aa82-32d63abe794c)

![image](https://github.com/CLAREISMO/test/assets/63759427/b72aa2ad-7d68-45d0-b239-4a214924afa9)

+ **Both loc and iloc are row-first, and column-second. This is the opposite of what we do in native Python, which is column-first, row-second. This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns.** 


+ To get a column with iloc, we can do the following:

![image](https://github.com/CLAREISMO/test/assets/63759427/4497b583-5196-4fa9-853b-490baa735420)

![image](https://github.com/CLAREISMO/test/assets/63759427/38c34db6-998e-4277-ac5b-079daa7d6f55)

On its own, the (:) operator, which also comes from native Python, means "everything". When combined with other selectors, however, it can be used to indicate a range of values. 

+ For example, to select the first, second, and third rows of the first column, we would have to:

![image](https://github.com/CLAREISMO/test/assets/63759427/67d8d95d-d6a3-4796-9a91-a8ac64bfcfc4)

+ If we want to select the second and third row of column 0, we have to:

![image](https://github.com/CLAREISMO/test/assets/63759427/7fc2842c-1a97-433c-8409-9d797955b5c8)

+ It's also possible to pass a list:

![image](https://github.com/CLAREISMO/test/assets/63759427/56d50fdd-7372-4993-a972-60f449170de7)


Finally, it's worth knowing that negative numbers can be used in selection. This will start counting forwards from the end of the values. So for example here are the last five elements of the dataset.

![image](https://github.com/CLAREISMO/test/assets/63759427/f6ab155f-cc17-49cc-8ec8-1266e580a93e)

**Label-based selection**

**loc**: The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. In this paradigm, it's the data index value, not its position, that matters.

For example, to get the first entry in reviews, we would now do the following:

![image](https://github.com/CLAREISMO/test/assets/63759427/33b03190-3814-4b31-8803-c064286cefda)

![image](https://github.com/CLAREISMO/test/assets/63759427/396fd907-bc5c-4076-988a-92b9dd2c0899)

+ **iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index by position.**

+ **loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:**

![image](https://github.com/CLAREISMO/test/assets/63759427/2746fee0-7409-4dbc-978a-6d695a221a9f)

### **Choosing between loc and iloc**

When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.

**iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9.**

**loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.**

Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoes'] (t coming after s in the alphabet).

**This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999]. Otherwise, the semantics of using loc are the same as those for iloc.**


### **Manipulating the index**

Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

The set_index() method can be used to do the job. Here is what happens when we set_index to the title field:

![image](https://github.com/CLAREISMO/test/assets/63759427/efda0bcf-75ea-45ca-80bb-8598049a8878)

![image](https://github.com/CLAREISMO/test/assets/63759427/17db00a1-c3ef-470a-9804-b6580412022c)

This is useful if you can come up with an index for the dataset which is better than the current one


### **Link code Conditional selection**

So far we've been indexing various strides of data, using the structural properties of the DataFrame itself. To do interesting things with the data, however, we often need to ask questions based on conditions.

Let's see the following example:

![image](https://github.com/CLAREISMO/test/assets/63759427/d0e2bd34-37b4-4678-b6a5-c19a2253ad65)

![image](https://github.com/CLAREISMO/test/assets/63759427/208d70fc-ac5a-4fc7-81f6-2c0cde6d3ec4)

![image](https://github.com/CLAREISMO/test/assets/63759427/70a7fc9e-f638-4c58-901d-cf7e892e10de)

This operation produced a Series of True/False booleans based on the condition of each record. This result can then be used inside of loc to select the relevant data:

+ We can know the percentage of occurrence of a value:

![image](https://github.com/CLAREISMO/test/assets/63759427/410f6a20-30e4-4b9f-bf60-050d3965cf0c)

![image](https://github.com/CLAREISMO/test/assets/63759427/d0f22c8a-b834-4b96-a23b-fcc8d70a3c87)

![image](https://github.com/CLAREISMO/test/assets/63759427/2631d85f-076e-429f-bd13-361481375ba9)


+ We can use the ampersand (&) to join two queries: in this case, we want to return the records of the DataFrame that meet the following conditions at the same time:  TP =="538" & Weight <= 0.4

![image](https://github.com/CLAREISMO/test/assets/63759427/914d38ca-cd3a-459d-8c62-a898d693a272)

![image](https://github.com/CLAREISMO/test/assets/63759427/0193d308-2cc0-4d17-9bed-8a4300e5fa45)

![image](https://github.com/CLAREISMO/test/assets/63759427/7e721f49-9cc5-4503-8135-988352413944)


+ We can also use the conditional pipe (|) to join two queries: in this case, we want to return the records of the DataFrame that meet one of the two requested queries, they only have to meet one condition TP =="538" | Weight <= 0.4. For this, we use a pipe (|):

![image](https://github.com/CLAREISMO/test/assets/63759427/4aa13e35-16c3-48cf-8a4c-0215135fd488)

**We can conclude that the ampersand(&) operator behaves as an AND conditional while the pipe (|) operator behaves as an OR conditional.**


### **Pandas  built-in conditional selectors**

Pandas come with a few built-in conditional selectors, two of which we will highlight here. The first is isin. isin lets you select data whose value "is in" a list of values.


**isin method**: 

![image](https://github.com/CLAREISMO/test/assets/63759427/def24936-ab29-48d3-893d-0fd3fac1e7fd)

+ We can request several objects that meet the given condition through the isin method!

![image](https://github.com/CLAREISMO/test/assets/63759427/add5a376-ac4f-4653-b18b-106d8d13e659)

+ We can also apply the loc selector together with the method isin:

![image](https://github.com/CLAREISMO/test/assets/63759427/d20951b8-79cd-4f41-9f2c-523e53e8645d)


+ It is also possible to filter the data given a condition:

![image](https://github.com/CLAREISMO/test/assets/63759427/2ba2c723-6380-463d-91ee-4cbd33fe5639)


**isnull and notnull methods**

The second Pandas built-in conditional selector is isnull (and its companion notnull). These methods let you highlight values that are (or are not) empty (NaN). 


**isnull method**

Return the null records from our DataFrame or from the given DataFrame selection.

![image](https://github.com/CLAREISMO/test/assets/63759427/d4ff87eb-6363-487f-8edf-3e5f2a64aec2)



**notnull method**

Returns the notnull records, that is to say, that do not have a null value from our DataFrame or from the given DataFrame selection.

![image](https://github.com/CLAREISMO/test/assets/63759427/f60ce9b1-8496-4f33-a717-a70a5204e252)


**Null Register check in DF**

We can check for the existence of null records in our DataFrame:
![image](https://github.com/CLAREISMO/test/assets/63759427/ffc97f76-51cc-4dfa-9f04-9354e8a7ca0d)



**Not-Null with Notna Register check in DF**
Also, we can check for the existence of not-null records in our DataFrame with notna function:

![image](https://github.com/CLAREISMO/test/assets/63759427/63de664b-2064-44eb-9cdd-25109bedf98b)


### **Assigning data**

Going the other way, assigning data to a DataFrame is easy. You can assign either a constant value:

![image](https://github.com/CLAREISMO/test/assets/63759427/048fca6d-846f-446f-8603-f86c1cb53a79)


![image](https://github.com/CLAREISMO/test/assets/63759427/95d24d4c-d8e0-46a0-84f9-eb78d02142cc)


**Iterable data Assignment** 

We generate a new column index_backwards which returns an inverted index starting with the last value of the index of the original DataFrame and ending with the first record of the index of the original DataFrame.

![image](https://github.com/CLAREISMO/test/assets/63759427/84b778fc-4843-4c9c-a1c3-8a01fb567e50)

When printing the DataFrame again we get an additional index_backwards column. Therefore the value of the columns increases to 17:

![image](https://github.com/CLAREISMO/test/assets/63759427/5143fa61-c669-43ee-a2f3-a2948ee065fa)


## **3. Summary Functions and Maps**

### **Introduction**

we learned how to select relevant data out of a DataFrame or Series. Plucking the right data out of our data representation is critical to getting work done, as we demonstrated in the exercises.

However, the data does not always come out of memory in the format we want it in right out of the bat. Sometimes we have to do some more work ourselves to reformat it for the task at hand. 

This tutorial will cover different operations we can apply to our data to get the input "just right".

we will use a new dataset so that you can observe different behaviors and infer that any code provided throughout these tutorials can be applied to any dataset.

**You can get different datasets on different topics to practice on the Kaggle portal: https://www.kaggle.com/datasets**


### **Sumary Function**

**describe() method:**

The describe() method: returns a DataFrame with a statistical summary of the columns of the DataFrame df of the type


**describe() method for numeric values:** . For numeric data (number) the mean, standard deviation, minimum, maximum, and quartiles are calculated. This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output changes based on the data type of the input. The output above only makes sense for numerical data.

Below we can see the describe() method applied to numeric data:

![image](https://github.com/CLAREISMO/test/assets/63759427/289faa50-8e29-4c90-bfff-dc030d44e5fe)

![image](https://github.com/CLAREISMO/test/assets/63759427/ba6c869f-de48-4f6f-a31d-d57cfad90d92)


**describe() method for non-numeric values:** For non-numeric data (object) the number of values, the number of distinct values, the mode, and their frequency are calculated. If the type is not specified, only numeric columns are considered. 

Below we can see the describe() method applied to string data:

![image](https://github.com/CLAREISMO/test/assets/63759427/18f00235-934c-4d8e-93d7-1a1686846314)

![image](https://github.com/CLAREISMO/test/assets/63759427/d8af7196-77cf-4a3f-a812-dbdca59c5e75)

![image](https://github.com/CLAREISMO/test/assets/63759427/701f1d5a-be72-491b-af4e-ce54e634db77)




**mean() function**

If you want to get some particular simple summary statistic about a column in a DataFrame or a Series, there is usually a helpful Pandas function that makes it happen.

![image](https://github.com/CLAREISMO/test/assets/63759427/98a03d1e-1bf0-4d17-88ad-686ae1a788a1)


**unique() function**

To see a list of unique values we can use the unique() function:

![image](https://github.com/CLAREISMO/test/assets/63759427/4ddce6a4-e628-4bd4-84e7-eade13986739)


**value_counts() method**
To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:

![image](https://github.com/CLAREISMO/test/assets/63759427/1e195f53-dc86-4e15-875f-082ff38380cc)

![image](https://github.com/CLAREISMO/test/assets/63759427/36d4f2b1-c5eb-4091-bbdd-de218f645fa3)


### **Maps**

A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values. 

In data science, we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later. 

Maps are what handle this work, making them extremely important for getting your work done!

There are two mapping methods that you will use often.


**1. map() method**: map() is the first, and slightly simpler one

![image](https://github.com/CLAREISMO/test/assets/63759427/03f880fe-19e4-4273-b90b-32fd21fb0db4)
![image](https://github.com/CLAREISMO/test/assets/63759427/4c99a60c-187e-4ee9-8c6f-b99e29f81687)


Going deeper into the map() method we have that:

![image](https://github.com/CLAREISMO/test/assets/63759427/d0f1bb60-d6e3-4955-9d74-ac27fa69123c)

![image](https://github.com/CLAREISMO/test/assets/63759427/d65c7d74-f377-47de-9148-04d98b3680a7)


**2. apply() method**: The function you pass to map() should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. map() returns a new Series where all the values have been transformed by your function.
apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

As we will see below to implement the apply() method it is required to implement the map() method first.

Let's see the development below:

![image](https://github.com/CLAREISMO/test/assets/63759427/213db147-bf27-4851-a4d1-4f9f4d3129dd)

![image](https://github.com/CLAREISMO/test/assets/63759427/e158d6a9-bea9-4838-81f7-467ca397d445)

![image](https://github.com/CLAREISMO/test/assets/63759427/f4f413db-211b-45da-884b-f7e11689f6c8)


**Important**

+ If we had called dfEmer.apply() with axis='index', then instead of passing a function to transform each row, we would need to give a function to transform each column.

+ Note that map() and apply() return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on. 

+ If we look at the first row of reviews, we can see that it still has its original points value.


Let's see the original DataFrame to corroborate the above.

![image](https://github.com/CLAREISMO/test/assets/63759427/65784b54-224a-4f31-a5f7-a49aeb41dff0)

![image](https://github.com/CLAREISMO/test/assets/63759427/b4c239bb-66a2-42be-8406-44d5f48b4f2b)



### **Common mapping operations as built-ins**

Pandas provides many common mapping operations as built-ins. For example, here's a faster way of remeaning our N_CHILDREN_15_YEARS_OVER column with respect to the mean:

+ In this code we are performing an operation between a lot of values on the left-hand side (everything in the Series) and a single value on the right-hand side (the mean value). 

+ Pandas looks at this expression and figures out that we must mean to subtract that mean value from every value in the dataset.

+ Pandas will also understand what to do if we perform these operations between Series of equal length. 


![image](https://github.com/CLAREISMO/test/assets/63759427/3f60a6c6-b48f-416a-acb4-00a8e43a2edf)


As we saw before this common mapping operation built into Pandas allows us to have a second way of applying the mean() method. 


### **operators applied to the combination of information**

In Pandas we can apply mathematical operators to combine in an easy way information that is present in the dataset. 

+ These operators are faster than map() or apply() because they use speed-ups built into pandas. 

+ All of the standard Python operators (>, <, ==, and so on) work in this manner.

+ However, they are not as flexible as map() or apply(), which can do more advanced things, like applying conditional logic, which cannot be done with addition and subtraction alone.


![image](https://github.com/CLAREISMO/test/assets/63759427/20100358-d8e9-451f-93b6-98e2aca83507)


## **4. Grouping and Sorting**

### **Introduction**

Scale up your level of insight. The more complex the dataset, the more this matters!

Maps allow us to transform data in a DataFrame or Series one value at a time for an entire column. However, often we want to group our data, and then do something specific to the group the data is in.

As you'll learn, we do this with the groupby() operation. We'll also cover some additional topics, such as more complex ways to index your DataFrames, along with how to sort your data.

**Groupwise analysis**: One function we've been using heavily thus far is the value_counts() function. We can replicate what value_counts() does by doing the following:

![image](https://github.com/CLAREISMO/test/assets/63759427/235bfc4b-f289-47e4-a7cb-a81ee130702b)

+ value_counts() is just a shortcut to this groupby() operation.  

+ We can use any of the summary functions we have used before with this data!


**Groupwise analysis and min() function**: For example, we can use the min() function. We then group by the variable ANOS_ESCOLARIDAD and ask it to return the minimum value associated with the variable ESTRATO_VIVIENDA associated with.

![image](https://github.com/CLAREISMO/test/assets/63759427/27988d25-9dee-4bf4-b4d1-4aafe2f5b051)

![image](https://github.com/CLAREISMO/test/assets/63759427/13454ca3-bd0a-4642-8bfe-fed1f7f78f6c)


Let's see another example with the min() function associated with the groupby() method. We see the behavior of the minimum values of the salaries with respect to the variable ANOS_ESCOLARIDAD. 

![image](https://github.com/CLAREISMO/test/assets/63759427/b881c626-2cee-4aab-9d69-01aba174bf39)

We obtain the minimum value of the salaries with respect to the variable SCHOOL_YEARS


![image](https://github.com/CLAREISMO/test/assets/63759427/14544a7a-69dc-4379-af0c-2f6e602b68ca)

**Groupwise analysis and max() function**: We can also use the max() function to obtain the maximum values of the variable to be analyzed with respect to the variable established in the groupby() method.

Next, we are going to make a comparison with the previous example. We are going to analyze the maximum values of the salaries with respect to the variable  SCHOOL_YEARS.

![image](https://github.com/CLAREISMO/test/assets/63759427/fa925a30-274d-4c7f-8c84-6ffd969429ad)

![image](https://github.com/CLAREISMO/test/assets/63759427/3e70aa48-aa30-4089-8ea3-082019ba7c5d)

Through the relationship between Groupwise analysis and other functions, we can obtain valuable information in the analysis of our data.


**Apply() method**
You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data in any way we see fit.

For a better understanding of the Apply method let's take a look at the following example.

![image](https://github.com/CLAREISMO/test/assets/63759427/106eab59-f535-453a-9837-0aa566ce3d36)


![image](https://github.com/CLAREISMO/test/assets/63759427/d137afea-6eab-4513-bce4-d031f810ed45)

**More detailed control with apply:** For even more fine-grained control, you can also group by more than one column.


![image](https://github.com/CLAREISMO/test/assets/63759427/e446101a-29ed-4a15-a746-90d6242b4aac)

In the first detailed apply( we are grouping HOUSING_STRATUM AND N_CHILDREN WITH RESPECT TO LABOUR INCOME THAT'S WHY THE COLUMN OF N_CHILDREN_MINOR_15TH ANNUAL INCOME IS kept with the original information of the dataset.

![image](https://github.com/CLAREISMO/test/assets/63759427/e91e58c3-96de-40b2-8279-62d13c4795fe)

![image](https://github.com/CLAREISMO/test/assets/63759427/2d9483a3-23b8-46fc-8a4c-ce73690f607e)

In the second apply() the labels ESTRATO_VIVIENDA and N_HIJOS_HIJOS within the groupby are maintained, these labels are compared with respect to the label N_HIJOS_MENORES_15ANOS through the method apply(). the output shows the change in the presentation of the information.

![image](https://github.com/CLAREISMO/test/assets/63759427/fa695387-bd4c-4a2f-8896-eec363086a51)

![image](https://github.com/CLAREISMO/test/assets/63759427/7bf5e2ee-9d22-4a21-bd4f-51f3a1f39721)


**Agg() METHOD**

Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your DataFrame simultaneously. For example, we can generate a simple statistical summary of the dataset as follows:

![image](https://github.com/CLAREISMO/test/assets/63759427/7c9f0cbf-5682-4959-8b57-640595d2548d)

![image](https://github.com/CLAREISMO/test/assets/63759427/40f83f9e-e4b7-4862-885d-897428e9f94f)

We determine the length and the minimum and maximum values present along the values of the variables ESTRATO_VIVIENDA and NOMBRE_DEPT.

**Multi-indexes**

In all of the examples we've seen thus far we've been working with DataFrame or Series objects with a single-label index. groupby() is slightly different in the fact that, depending on the operation we run, it will sometimes result in what is called a multi-index.

A multi-index differs from a regular index in that it has multiple levels. For example:

![image](https://github.com/CLAREISMO/test/assets/63759427/bda70594-0c34-4e4a-ac9d-5406919edd97)

![image](https://github.com/CLAREISMO/test/assets/63759427/029fef30-9f60-4498-a4f3-0b5b2c8ee6bc)


Within groupby() we group the variables ANOS_ESCOLARIDAD and ESTRATO_VIVIENDA. The variable N_CHILDREN will be analyzed with respect to the previous ones in terms of length and maximum and minimum values.


**Various methods for the multiple indices**

Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. They also require two levels of labels to retrieve a value. Dealing with multi-index output is a common "gotcha" for users new to pandas.

The use cases for a multi-index are detailed alongside instructions on using them in the MultiIndex / Advanced Selection section of the pandas documentation.

However, in general, the multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method.

![image](https://github.com/CLAREISMO/test/assets/63759427/61993f70-3dfb-4b70-8e0d-ed25b5fb0e1b)

![image](https://github.com/CLAREISMO/test/assets/63759427/1ef309c8-85e6-413c-9d15-72e8666d76e5)


**Sorting**
We can see that grouping returns data in index order, not in value order. That is to say, when outputting the result of a groupby, the order of the rows is dependent on the values in the index, not in the data.

To get data in the order want it in we can sort it ourselves. The sort_values() method is handy for this.

![image](https://github.com/CLAREISMO/test/assets/63759427/eb14a5b3-2287-4e38-8bb8-a42fe0dfbe7d)

![image](https://github.com/CLAREISMO/test/assets/63759427/2ebca645-4d79-4df9-b680-e1301a6a21ba)


**Sorted by max():** We will then apply the sort method on the variable ESTRATO_VIVIENDA by max

![image](https://github.com/CLAREISMO/test/assets/63759427/d12ba6fa-57ed-48bf-b04c-c7ca7a607ae0)

![image](https://github.com/CLAREISMO/test/assets/63759427/744f63f8-9900-4d40-80be-07eb0996586c)


**Sort Value()**
sort_values() defaults to an ascending sort, where the lowest values go first. 

However, most of the time we want a descending sort, where the higher numbers go first. That goes thusly:

![image](https://github.com/CLAREISMO/test/assets/63759427/51632402-1353-42e1-848f-c87d6ec68dd5)

![image](https://github.com/CLAREISMO/test/assets/63759427/4b716658-9331-4952-ab4c-71310e273d1f)


**Sort_Index()**
To sort by index values, use the companion method sort_index(). This method has the same arguments and default order:

![image](https://github.com/CLAREISMO/test/assets/63759427/a1d532a7-82ad-4406-b09c-6b234975c000)

![image](https://github.com/CLAREISMO/test/assets/63759427/2696e4fd-7cd1-4b6f-9b5d-3d5e3152409e)


**Sort by more than one column at a time**
Finally, know that you can sort by more than one column at a time:

![image](https://github.com/CLAREISMO/test/assets/63759427/7b010db0-3ada-4671-99a3-6226b9f08697)

![image](https://github.com/CLAREISMO/test/assets/63759427/85a2584b-172b-4b30-9653-8524bebcf162)































































