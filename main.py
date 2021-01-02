cislo = 0
delky = dict()
mala_pismena = 0
oddelovac = 60 * '°'
pocet_cisel = 0
pocet_slov = 0
pokusy = 3
registrovani_uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
soucet_cisel = 0
velka_pismena = 0
zacatek_velkym_pismenem = 0
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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
garpike and stingray are also present.'''
         ]

print(oddelovac)
print("Vítejte v aplikaci, přihlaste se prosím [máte 3 pokusy]:")
print(oddelovac)

while pokusy > 0:
    jmeno = input('Jméno: ')
    heslo = input('Heslo: ')
    if registrovani_uzivatele.get(jmeno) == heslo:
        print('Přístup povolen')
        break
    else:
        print('Nesprávné jméno, nebo heslo. Zkus to prosím znovu.')
        if pokusy == 1:
            exit()
    pokusy = pokusy - 1

print(oddelovac)
while True:
    vyber_cisla = input("Máme 3 texty k porovnání. Zadejte číslo v rozsahu 1 až 3: ")
    if not vyber_cisla.isnumeric():
        print('Zadaná hodnota není číslo.')
        continue
    else:
        vyber_cisla = int(vyber_cisla) - 1

    if 0 > vyber_cisla or vyber_cisla > 2:
        print('Číslo není v rozsahu 1-3')
    else:
        break
print(oddelovac)
vybrany_text = TEXTS[vyber_cisla].split()

pocet_slov = len(vybrany_text)

for slovo in vybrany_text:
    slovo = slovo.strip(',.')

    if slovo == slovo.upper() and not slovo.isnumeric():
        velka_pismena += 1

    if slovo == slovo.title() and not slovo.isnumeric():
        zacatek_velkym_pismenem += 1

    if slovo == slovo.lower() and not slovo.isnumeric():
        mala_pismena += 1

    if slovo.isnumeric():
        pocet_cisel += 1
        soucet_cisel += int(slovo)

    delka = len(slovo)
    if delka in delky.keys():
        delky[delka] = delky[delka] + 1
    else:
        delky[delka] = 1

print(oddelovac)

print(f'Ve vybraném textu je {pocet_slov} slov.')
print(f'Ve vybraném textu je {zacatek_velkym_pismenem} slov začínajících velkým písmem.')
print(f'Ve vybraném textu je {velka_pismena} slov psaných velkým písmem.')
print(f'Ve vybraném textu je {mala_pismena} slov psaných malým písmem.')
print(f'Ve vybraném textu je {pocet_cisel} čísel.')
print(oddelovac)

for delka in set(delky.keys()):
    print(delka, delky[delka] * '*', delky[delka])

print(oddelovac)

print(f'Pokud bychom sečetli všechna čísla v tomto textu, dostali bychom: {soucet_cisel}.')
print(oddelovac)

