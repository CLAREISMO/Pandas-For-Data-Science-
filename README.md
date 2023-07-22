

![image](https://github.com/CLAREISMO/Pandas-For-Data-Science-/assets/63759427/da26ede4-3224-4e66-8c46-a786ce6d4bb6)<img src="https://media.tenor.com/Nk6wJhshPaMAAAAi/dm4uz3-foekoe.gif" width="60px">


**This repository contains the Pandas by Kaggle course also implemented in the VSC code editor in order to observe all the requirements and behavior of the code in a real production environment.**

**You can see the respective outputs in this file and the code in the Python language you will get for each topic in the repository files.**

**Enjoy it**




## **1. CLASS: Creating, Reading, and Writing**

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

## **2. CLASS: Indexing, Selecting & Assigning**

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

































