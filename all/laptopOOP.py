class Laptop:
    def __init__(self, brend, processor, RAM):
        self.brend = brend
        self.processor = processor
        self.ram =  RAM
  
    def upgrade_RAM(self):
        while True:

            x = int(input(f"how many GB of RAM do u want to add?(now {self.ram} )  "))
        #  self.ram = self.ram + x
        # тут додати алгоритм який не дає додати дуже багато пам'яті,наприкладки не більше 34гб
            if x > 34:
               print("too much ram..try less")
            else:
             self.ram = self.ram + x
             print(f"you are upgrade you RAM! Added: {x}GB, Current total: {self.ram}GB")
             break
    def display_info(self):
        print(f"Характиристики вашого {self.brend}: процесор: {self.processor}, обє'м оперативки {self.ram}")

over = Laptop("Lenovo ThinkPad", "AMD Ryzen 9", 64)

over.display_info()
over.upgrade_RAM()

over.display_info()

class Gaming_laptop(Laptop):
     def __init__(self, brend, processor, RAM, gb_gpu, brand_gpu):
            super().__init__( brend, processor, RAM)
            self.gb_gpu = gb_gpu
            self.brand_gpu = brand_gpu

     def display_info(self):
            super().display_info()
            print(f"GPU: {self.gb_gpu}, кількісь гб: {self.gb_gpu}")
     
over2 = Gaming_laptop("Asus ROG Flow", "Intel i5", 16, "NVIDIA RTX 3450", 8)

over2.display_info()
over2.upgrade_RAM()
over2.display_info()
     


class ServiceCenter:
     def __init__(self):
            pass #чому не потрібно?так,сюди не потрібні дані 
     def clean_coolers(self, laptop ):
          price = 500

          if isinstance(laptop, Gaming_laptop):
                price = 200
                print("--- О, ігровий ноутбук! Вам діє знижка на чистку ---")

          print(f"--- Сервісна операція ---")
          print(f"Обслуговуємо: {laptop.brend}")
          print(f"Вартість: {price} грн")
          print(f"Готово! Процесор {laptop.processor} тепер не гріється.")

service = ServiceCenter()

service.clean_coolers(over)