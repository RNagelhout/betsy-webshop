# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line
from models import *

def search(term):
    query = (
        UserProduct.select()
        .join(Product)
        .where(Product.name ** term | Product.description.contains(term))  
    )

    for user_product in query:
        print (user_product.quantity, user_product.product.name, user_product.product.description, user_product.price,)
    
def list_user_products(user_id):
    query = (
        UserProduct.select().where(UserProduct.user_id == user_id).join(Product)      
    )
    for user_product in query:
        print (user_product.user_id, user_product.quantity, user_product.product.name, user_product.product.description, user_product.price,)
    

def list_products_per_tag(tag_id):
    query = (
        UserProduct.select().join(Product).where(Product.tag_id == tag_id)
    )
    
    for user_product in query:
        print (user_product.user_id, user_product.quantity, user_product.product.name, user_product.product.tag_id )

def add_product_to_catalog(user_id, product_id, price, new_quantity):
    query = (
        UserProduct.select().where(UserProduct.user==user_id, UserProduct.product == product_id, UserProduct.price == price) 
    )
    if len(query) == 0:
        UserProduct.create(user=user_id ,product=product_id, price=price, quantity=new_quantity, status=0)
    else: 
        UserProduct.update(quantity = UserProduct.quantity + new_quantity).where(UserProduct.user==user_id, UserProduct.product_id == product_id, UserProduct.price == price).execute()

def update_stock(user_id: int, product_id, new_quantity: int):
    UserProduct.update(quantity = new_quantity).where(UserProduct.user_id == user_id, UserProduct.product_id == product_id).execute()

def purchase_product(user_id: int, product_id: int, buyer_id: int, quantity: int):
    query = (
        UserProduct.select().where(UserProduct.user_id == user_id, UserProduct.product_id == product_id)
        )
    for user_product in query: 
        if user_product.quantity > 0:
            product_price = user_product.price
            new_quantity = user_product.quantity - quantity
            UserProduct.update(status = 1, quantity = new_quantity).where(UserProduct.user_id == user_id, UserProduct.product_id == product_id).execute()
            Transaction.create(buyer_id=buyer_id, seller_id=user_id, product_id=product_id, quantity=quantity, price=product_price, sold=1)
        else:
            print("Sorry the stock has run out!")

def remove_product(product_id):
    Product.delete().where(Product.id == product_id).execute()

def remove_user_product(product_id):
    UserProduct.delete().where(UserProduct.id == product_id).execute()


if __name__ == "__main__":
    # search("st")
    # list_user_products(1)
    # list_products_per_tag(1)
    add_product_to_catalog(1,5,155.75,20)
    # update_stock(1,1,250)
    # purchase_product(1,5,1,1) 
    # remove_product(9)
    # remove_user_product(9)
     