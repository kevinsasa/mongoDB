import pymongo
import csv
import pandas as pd
client = pymongo.MongoClient("mongodb+srv://catfood_db:passwordtest@cluster0.rvn03z4.mongodb.net/?retryWrites=true&w=majority")
mydb = client["catfood_db"]
mycol = mydb["test"]
