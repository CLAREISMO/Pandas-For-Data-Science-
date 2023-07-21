

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

































