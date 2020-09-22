import datetime
name = input("Kāds ir Jūsu vārds?")
age = input(f"Prieks iepazīties {name}. Cik Jums ir gadu?")
age = int(age)
currentYear = datetime.datetime.now().year
print(f"Forši {name}. Jums būs 100 gadu {100-age+currentYear}.gadā :)")
