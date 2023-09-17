# Models go here
from peewee import *


db = SqliteDatabase("database.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    streetname = CharField()
    house_nr = CharField() 
    zipcode = CharField()
    city = CharField()
    iban = CharField()

class Catagory(BaseModel):
    name = CharField()# tags should not be duplicated. tags hebben eigen tabellen

class Product(BaseModel):
    name = CharField()
    description = CharField()
    tag = ForeignKeyField(Catagory, backref="catagory_name")

class UserProduct(BaseModel):
    user = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    price = DecimalField(decimal_places=2) 
    quantity = IntegerField(default=0)
    status = BooleanField()
    
class Transaction(BaseModel):
    buyer_id = ForeignKeyField(User)
    seller_id = ForeignKeyField(UserProduct)
    product_id = ForeignKeyField(UserProduct)
    quantity = IntegerField(default=0)
    price = ForeignKeyField(UserProduct)
    sold = BooleanField()
