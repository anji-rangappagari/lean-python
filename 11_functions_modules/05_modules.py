#  In  python two type of modules available are built-in modules and user-defined modules.
#  built-in modules are the modules that are included in the python standard library. They are available for use without the need for installation. Some examples of built-in modules are math, random, datetime, os, sys, etc. 
# external modules are the modules that are not included in the python standard library. They need to be installed before they can be used. Some examples of external modules are numpy, pandas, matplotlib, etc.

# internal/buit in  modules : https://docs.python.org/3/py-modindex.html CAN REFER THIS LINK FOR MORE INTERNAL MODULES
# external modules : 

import math   # importing the math module to use its functions
import mymodule  # importing the mymodule module to use its functions
import requests  # importing the requests module to use its functions
import pandas as pd  # importing the pandas module to use its functions

print(math.sqrt(16))  # 4.0  # using the sqrt function from the math module to calculate the square root of 16

# importing the mymodule module to use its functions

mymodule.hello()  # Hello, World!  # using the hello function from the mymodule module to print "Hello, World!"

# pip install requests  # using pip to install the requests module (external module) to make HTTP requests
r = requests.get("https://www.google.com")  # using the get function from the requests module to make a GET request to the Google homepage
print(r.status_code)  # 200  # printing the status code of the response from the GET request
print(r.text)  # printing the content of the response from the GET request

# file_path = "/c/Users/anjin/Downloads/drift-engine-2026-04-26.csv"  # defining the file path for the CSV file to be read
# data = pd.read_csv(file_path)  # using the read_csv function from the pandas module to read the CSV file and store it in a DataFrame
# print(data.head())  # printing the first 5 rows of the DataFrame to check if


