import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Kaç haneli bir şifre istersin?"))

parola = ''

karakter = random.choice(karakterler)
print(karakter)