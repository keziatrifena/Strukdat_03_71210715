kali = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dicari: ")

kali = kali.lower().split()
kata = kata.lower()
count = 0

for i in kali:
    if i == kata:
        count += 1

print("Banyak kata", kata, "yang terdapat pada kalimat diatas adalah", count)
