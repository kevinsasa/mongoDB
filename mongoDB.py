import pymongo

client = pymongo.MongoClient("mongodb+srv://catfood_db:passwordtest@cluster0.rvn03z4.mongodb.net/?retryWrites=true&w=majority")
mydb = client["catfood_db"]
mycol = mydb["catfood_db"]

#新增資料
# mycol.insert_one()
# mycol.insert_many

#刪除資料
# mycol.delete_one()
# mycol.delete_many()