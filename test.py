varian = 3
campo1 = "hola1"
campo2 = ""
campo3 = "hola3"

if campo1 == "":
     0

while varian > 0:
    if len(campo3)>1:
        varian =3
        campo = campo3
        campo3=""
    elif len(campo2)>1:
        varian =2
        campo = campo2
        campo2=""
    elif len(campo1)>1:
        varian =0
        campo = campo1
        campo1=""


    print(campo)