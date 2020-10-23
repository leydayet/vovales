def leer():
    global palabra
    palabra=(input('ingrese una frase:'))
def contar():
    vocales=['a','e','i','o','u']
    consosnantes=['b','c','d','f','g','h','j','k','l','m','n','ñ','p','r','s','t','v','w','x','y','z']
    contador=0
    contadorcons=0
    for o in palabra:
        for v in vocales:
            if(o==v):
                contador+=1
        for c in consosnantes:
            if(o==c):
                contadorcons +=1
    print('el numero devovales es:',contador)
    print('el numero de consonantes es:',contadorcons)

leer()
contar()