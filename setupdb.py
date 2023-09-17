from models import *
import os

def delete_database():
    """
    Delete the database.
    """
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)

def populate_database():
    db.connect()		
    db.create_tables(
            [
                User,
                Catagory,
                Product,
                UserProduct,
                Transaction
            ]
        )
    
    users = [
        ["Harry", "De Brink", "16", "2052KL", "Rotterdam", "NL23INGB4746672490" ],
        ["Bert", "Welle", "1", "1025DD", "Bergen", "NL81RABO3025195118"],
        ["Gerard", "Broekweg", "2", "2014GL", "Uithuizen", "NL33RABO5311809574"],
        ["Hazan", "Simonstraat", "6", "1152SB", "Den Haag", "NL28INGB9248708374"],
        ["Johnny", "Boomweg", "1A", "7844UY", "Maastricht", "NL34RABO6212151431"],
        ]

    for user in users:
        User.create(
            name=user[0], 
            streetname=user[1], 
            house_nr=user[2], 
            zipcode=user[3], 
            city=user[4], 
            iban=user[5]
            )

    catagories = ["Vervoersmiddelen", "Televie", "Speelgoed", "Gereedschap"]

    for catagory in catagories:
        Catagory.create(name=catagory)

    products = [
        ["Fiets", "Mooie oude fiets, heeft wel gebruikersporen", "1"],
        ["Zaag", "Oude zaag, doet het nog prima", "4"],
        ["TV", "Zo goed als nieuw!", "2"],
        ["Step", "Mooie rode step, leuk voor de kids", "1"],
        ["Auto", "van een oud vrouwtje geweest, altijd binnen gestaan.", "1"],
        ["Knikkers", "Oude verzameling knikkers", "3"],
    ]
    for product in products:
        Product.create(
            name=product[0], 
            description=product[1], 
            tag=product[2]
            )

    userProducts = [
        [1, 4, 750.50, 1, True],
        [1, 1, 20.25, 4, False],
        [3, 5, 10.00, 1, True],
        [4, 1, 5.00, 10, True],
        [2, 4, 750.00, 1, True],
        [4, 2, 20.25, 4, False],
        [3, 3, 10.00, 1, True],
        [4, 5, 5.00, 10, True],
    ]
    for userProduct in userProducts:
        UserProduct.create(
            user=userProduct[0], 
            product=userProduct[1], 
            price=userProduct[2], 
            quantity=userProduct[3], 
            status=userProduct[4]
            )

    transactions = [
        [ 0, 1, 2, 1, 2, True ],
        [ 4, 2, 4, 1, 4, True ],
        [ 4, 1, 5, 1, 1, True ],
        [ 1, 2, 1, 1, 2, True ],
        [ 0, 1, 2, 1, 2, True ],
        [ 0, 1, 2, 1, 2, True ],
        [ 0, 1, 2, 1, 2, True ],
        [ 0, 1, 2, 1, 2, True ],
    ]
    for transaction in transactions:
        Transaction.create(
            buyer_id=transaction[0],
            seller_id=transaction[1],
            product_id=transaction[2],
            quantity=transaction[3],
            price=transaction[4],
            sold=transaction[5],
            )

    db.close()

if __name__ == "__main__":
    # delete_database()
    populate_database()    