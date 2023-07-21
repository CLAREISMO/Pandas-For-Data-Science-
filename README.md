

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












