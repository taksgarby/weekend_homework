# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    
    pet_shop["admin"]["total_cash"] += cash
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, increase_by):

    pet_shop["admin"]["pets_sold"] += increase_by

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []

    for pet_breed in pet_shop["pets"]:
        if breed == pet_breed["breed"]:
            pets_by_breed.append(pet_breed) 
    return pets_by_breed

def find_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            return pet

def remove_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):

    pet_shop["pets"].append(new_pet) 

def get_customer_cash(customers):
    customer_cash = customers["cash"]
    return customer_cash

def remove_customer_cash(customers, cash):
    customers["cash"] = customers["cash"] - cash

def get_customer_pet_count(customers):
    customer_pet_count = customers["pets"]
    return len(customer_pet_count)

def add_pet_to_customer(customers, new_pet):

    customers["pets"].append(new_pet)

def customer_can_afford_pet(customers, new_pet):

    if customers["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):

    # append a pet to a customer "pet"

    add_pet_to_customer(customer, pet)

    # add one to admin "pets_sold"

    increase_pets_sold(pet_shop, 1)

    # get the price of pet pet "price"
    print(pet)
    pet_price = pet["price"]
    
    # if (find_pet_by_name):
    #     pet_price = pet["price"]
    # else:
    #     pet_price = 0

    # remove_customer_cash(customer, pet_price)

    remove_customer_cash(customer, pet_price)

    # add pet price to admin "total_cash"

    add_or_remove_cash(pet_shop, pet_price)
    
# get customer pet count as 0




#  get pet sold as 0

# customer cash remain as 1000 

# the total cash remains as 1000
    
