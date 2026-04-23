class Laptop:
    def __init__(self, brend, processor, RAM):
        self.brend = brend
        self.processor = processor
        self._ram =  RAM # дві __ для не можливості змінити код одна _ можуть змінювати нащадки
        self.needs_cleaning = False
        self.temperature = 30

    def upgrade_RAM(self): 
        while True: #  аналог do-while
              user_input = input(f"How many GB to add? (now {self._ram}): ")
        
              try:
                 x = int(user_input)
# тут додати алгоритм який не дає додати дуже багато пам'яті,наприкладки не більше 34гб
                 if x > 34:
                        print("Too much RAM... try less.")
                 elif x < 0:
                        print("You can't add negative RAM! Try again.")
                 else:
                     self._ram += x 
                     print(f"Upgrade successful! Total: {self._ram}GB")
                     break
              except ValueError: # ОСЬ ЦЬОГО НЕ ВИСТАЧАЄ
               print("Це не число! Введіть, будь ласка, цифрами.")
   
# self._ram = self._ram + x #тут хіба не потрібно змінити на нову змінну?щоб ноут памяьав що було до.чи для нащадків буде погано? все. не актуально
    def display_info(self):
        print(f"Характиристики вашого {self.brend}: процесор: {self.processor}, обє'м оперативки {self._ram}")
        status = "needs cleaning" if self.needs_cleaning else "absolutely clean"
        print(f"condition: {status}")

    def run_heavy_task(self):
         self.temperature = self.temperature + 20
         if self.temperature > 70:
                self.needs_cleaning = True
         print(f"you are run heavy task..now you temperature is {self.temperature}")
         
over = Laptop("Lenovo ThinkPad", "AMD Ryzen 9", 64)

over.display_info()
over.upgrade_RAM()

over.display_info()

class Gaming_laptop(Laptop):
     def __init__(self, brend, processor, RAM, gb_gpu, brand_gpu):
            super().__init__( brend, processor, RAM)
            self.gb_gpu = gb_gpu
            self.brand_gpu = brand_gpu
            self.temperature = 40

     def display_info(self):
            super().display_info()
            print(f"GPU: {self.brand_gpu}, кількісь гб: {self.gb_gpu}")
     def run_heavy_task(self):
         self.temperature = self.temperature + 20
         if self.gb_gpu > 6:
                  self.temperature = self.temperature + 15
         else:
                 if self.temperature > 70:
                  self.needs_cleaning = True
                  print(f"you are run heavy task..now you temperature is {self.temperature}")
        

over2 = Gaming_laptop("Asus ROG Flow", "Intel i5", 16, 8,  "NVIDIA RTX 3450")

over2.display_info()
over2.upgrade_RAM()
over2.display_info()
     


class ServiceCenter:
     def __init__(self):
            pass #так,сюди не потрібні дані 
     def clean_coolers(self, laptop ):
            price = 500

            if isinstance(laptop, Gaming_laptop): #перевірка чкий саме дочірній обєкт
                price = 200
                print("--- О, ігровий ноутбук! Вам діє знижка на чистку ---")

            laptop.temperature = 30
            print(f"--- Сервісна операція ---")
            print(f"Обслуговуємо: {laptop.brend}")
            print(f"Вартість: {price} грн")
            print(f"Готово! Процесор {laptop.processor} тепер не гріється.")
            
            if laptop.needs_cleaning:
                print(f"cleaning {laptop.brend}")
                laptop.needs_cleaning = False
                
            else:
              print(f"Your {laptop.brend} absilutely clean!Good! ")
              

            
service = ServiceCenter()

service.clean_coolers(over)

