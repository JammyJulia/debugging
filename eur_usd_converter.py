
# Mērķis: 
# iespēja konvertēt USD uz EUR un otrādi pēc 1.08 kursa

eur_to_usd_rate = 1.08

print("Choose command")
while True:
    print("=======")
    print("1 - convert EUR into USD")
    print("2 - convert USD into EUR")
    print("3 - exit")
    command = input("")

    if command == '1':
        eur = float(input("Enter USD:"))
        usd = eur / 1.08
        print(eur, "EUR equals USD", usd)
    elif command == '2':
        usd = float(input("Enter EUR:"))
        eur = usd * 1.08
        print(usd, "USD equals EUR", eur)
    else:
        break

# Kādas kļūdas izdevies atrast?
# While False means code is never reached, to make a loop changed it to True
# The exchange rate is supposed to be 1.08, not 1.09
# 'if' checks 'command' as if it was an integer, however 'input' returns a string
# usd is a string, and the program is trying to divide it
# the first commands varieables names are supposed to bo the other way around(doesnt actually cause an error tho)
# the first commands output is supposed to say "EUR equals USD"