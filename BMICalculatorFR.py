import time

print("Bonjour Monsieur/Madame, Avez vous envie de connaître votre IMC(BMI) ? Introduisez vos données ci-dessous:")

weight = float(input("Quel est ton poids? (kg) : "))
height = float(input("Quelle est ta hauteur? (cm) : "))
bmi = float(weight / ((height * 0.01) * (height * 0.01)))

if bmi > 0:
    if bmi < 18.5:
        print("Vous etes Trop maigre!!!!")
    elif bmi < 25:
        print("Vous devez etre totalement satisfait abec votre poids!!!!")
    elif bmi < 30:
        print("Propablement vous avez quelques kilos en trop :D, mais ce n'est pas urgent")
    elif bmi < 40:
        print("Vous etes obèse!!!! Maigir pour votre Bonheur et Sante! ;) ")
    else:
        print("Vous avez obésité morbide!! C'est dangereux!! Pour votre Sante, Maigrir, S'il vous plait!")
    time.sleep(60)
# J'aime le programming et Le Python
