# Zadanie lista zakupów

zakupy = {
    "piekarnia,": ["chleb", "bułki", "pączek", "rogalik"],
    "warzywniak": ["marchew", "seler", "rukola", "pomidor"]
}

# Tworzenie pętli
suma_produktów = 0
for sklep, produkty in zakupy .items():
    sklep_nazwa = sklep.title()
    produkty_nazwa = ', '.join([produkt.title() for produkt in produkty])
    print(f"Idę do {sklep_nazwa} kupuję am następujące rzeczy: {produkty_nazwa}.")
    suma_produktów += len(produkty)
    
# Suma produktów
print(f"W sumie kupuję {suma_produktów} produktów.")
