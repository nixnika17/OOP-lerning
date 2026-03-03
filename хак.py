class nikitos:
    def __init__(self):
        self.name = "NIXINDUSTIS" #публічне
        self.__security_code = 171717 #інкапсульоване
    def getcode(self, code):
        return code == self.__security_code
                                                                                                                                                                                         
myh = nikitos()

print(f"Знайдено прихований код: {myh._nikitos__security_code}")


myh._nikitos__security_code = 999999
print(f"Код змінено в обхід системи: {myh._nikitos__security_code}")

# можна ще використовувати кампіляцію




