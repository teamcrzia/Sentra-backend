from pymongo import MongoClient

client = MongoClient("mongodb+srv://Admin:1qaz2wsx%40@creziaai.qsjle74.mongodb.net/crezia")

db = client["crezia"]

users = db["users"]
chats = db["chats"]
usage = db["usage"]