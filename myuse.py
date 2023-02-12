import pymongo
import csv
import pandas as pd
from pymongo import MongoClient
import json


client = pymongo.MongoClient("mongodb+srv://catfood_db:<password>@cluster0.rvn03z4.mongodb.net/?retryWrites=true&w=majority")
mydb = client["catfood_db"]
mycol = mydb["test"]

data = pd.read_csv('CV_LatLon_21Jan_12Mar.csv', encoding = 'UTF-8')
data_json = json.loads(data.to_json(orient='records'))
mycol.insert_many(data_json)
