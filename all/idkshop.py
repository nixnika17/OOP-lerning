import time

class Shop:
    def __init__(self):
        self.shopname = "PETRYSKA" #атрибут(дані)
        self.shoptype = "adorable" #атрибут(дані)
        self.number_of_units = 0
    def describe(self): #метод(дії)
        print(f"назва магазину: {self.shopname} він має тип {self.shoptype} ")
        time.sleep(1.2)
    def openshop(self): #метод(дії)
        print(f"Магазин {self.shopname} відкритий,обирайте замовлення😉😉")
    def set_number_of_units(self, number):
        self.number_of_units = number
    def increment_number_of_units(self, count):
        self.number_of_units += count
            
store = Shop() #екземпляр


print(store.shopname) # виведення атрибута
print(store.shoptype) # виведення атрибута
store.describe() #виклик метода
store.openshop() #виклик метода

stor1 = Shop()
stor1.describe()


print(store.number_of_units) #початкове значення
store.set_number_of_units(17)
print(store.number_of_units)
store.increment_number_of_units(60)
print(store.number_of_units)

class Discount(Shop):
    def __init__(self):
        super().__init__()
        self.discount_products = ["кукумбер", "кіт", "Казакстан"]
    def get_discounts_products(self):
        print(f"Список товарів зі знижкою: {self.discount_products}")
        
        # for product in self.discount_products:
        #     print(f"- {product}")

store2 = Discount()
store2.get_discounts_products()
store2.describe() # Виклик методу нащадка


