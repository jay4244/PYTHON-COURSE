# pip install pandas
"""
pip : python index package : this is a package manager.
      using of pip we can install 3rd party modules in python.
      
pandas come in 2 bulding blocs

1) series : which is contain column records only 
2) Dataframe : which is contain row and cloumn in table format      
"""
import pandas as pd
fruit_products =pd.Series(
    [30,45,57,89,34],
    index=["kiwi","Apple","mango","grapes","banana"],
    name = "qty"
)

print(fruit_products)

print("####Analiys####")

print(f"highest selling unit :: {fruit_products.idxmax()} - {fruit_products.max()}")