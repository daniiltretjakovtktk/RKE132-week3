n = int(input("Sisesta täisarv: "))
if n % 2 == 0:
    print("Sisestatud arv on paaris.")
else:
    print("Sisestatud arv on paaritu.")

#print("Sisestatud arv on paaris." if n % 2 == 0 else "Sisestatud arv on paaritu.")

match n % 2:
    case 0:
        print("Sisestatud arv on paaris.")
    case 1:
        print("Sisestatud arv on paaritu.")
        