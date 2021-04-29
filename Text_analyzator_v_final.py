TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

uzivatele = {'USER': 'PASSWORD',
             'bob': '123',
             'ann': 'pass123',
             'mike': 'password123',
             'liz': 'pass123'
             }
oddelovac = "-" * 40

jmeno = input("Zadej jméno: ").lower()
heslo = input("Zadej heslo: ")
print(oddelovac)

uzivatele.get(jmeno, "You are not registered, bye.")
if jmeno in uzivatele.keys() and heslo == uzivatele.get(jmeno):
    print("Welcome to the app, ", jmeno, "\nWe have 3 texts to be analyzed.")
else:
    print("You are not registered, bye.")
    exit()
print(oddelovac)

c_text = int(input("Enter a number btw. 1 and 3 to select: "))
if c_text in list(range(1, 4)):
    print(oddelovac)
else:
    print("Sorry, wrong input, bye.")
    exit()


slovnik = {}
slovnik_4_graf = {}
text1 = TEXTS[0]
text2 = TEXTS[1]
text3 = TEXTS[2]

for i, text in enumerate((text1, text2, text3), 1):
    cista_slova = [slovo.strip(',."?!)(\n') for slovo in text.split(" ")]
    slovnik[f"text{i}"] = {"pocet_slov": sum(1 for slovo in cista_slova),
                           "titlecase": sum(1 for slovo in cista_slova if slovo.istitle()),
                           "uppercase": sum(1 for slovo in cista_slova if slovo.isalpha() and slovo.isupper()),
                           "lowercase": sum(1 for slovo in cista_slova if slovo.islower()),
                           "numeric": sum(1 for slovo in cista_slova if slovo.isdigit()),
                           "sum_numbers": sum(int(slovo) for slovo in cista_slova if slovo.isdigit())}

print(f"There are {slovnik[f'text{c_text}']['pocet_slov']} words in the selected text.")
print(f"There are {slovnik[f'text{c_text}']['titlecase']} titlecase words.")
print(f"There are {slovnik[f'text{c_text}']['uppercase']} uppercase words.")
print(f"There are {slovnik[f'text{c_text}']['lowercase']} lowercase words.")
print(f"There are {slovnik[f'text{c_text}']['numeric']} numeric words.")
print(f"The sum of all the numbers {slovnik[f'text{c_text}']['sum_numbers']}.")
print(oddelovac)

for i, text in enumerate((text1, text2, text3), 1):
    pocet_slov = [slovo.strip(',."?!)(\n') for slovo in text.split(" ")]
    pocet = [len(slovo) for slovo in pocet_slov]
    slovnik_4_graf[f"text{i}"] = {x: pocet.count(x) for x in pocet}

vysledek = list((slovnik_4_graf[f"text{c_text}"].items()))
vysledek.sort()


print(f"{'LEN'.format('left aligned')}| {'OCCURENCES'.center(28)} | {'NR.'.format('right aligned')}")
print(oddelovac)

for klic, hodnota in vysledek:
    if klic < 10:
        klic = "0" + str(klic)
        print(f"{klic.format('left aligned')} | {'*' * hodnota} {' ' * (27 - hodnota)} | {hodnota}")
    else:
        print(f"{str(klic).format('left aligned')} | {'*' * hodnota} {' ' * (27 - hodnota)} | {hodnota}")
