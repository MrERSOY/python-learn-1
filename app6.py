successful = False
for number in range(3):
    print("Başlatılıyor", number + 1, "Deneme")
    if successful:
        print("Başarılı")
        break
else:
    print("3 kere başlatma denemesi başarısız oldu.")
