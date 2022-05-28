#Calculadora
def menu():
    print(''' Bienvenido a tu calcualdora!!!
            Aqui estan nuestras opciones:
            1- Suma
            2- Multiplicar
        '''
        )

menu()
Opciones = int(input('Escogue la opcion que necesite: '))

while (Opciones >0 and Opciones <3):
    if(Opciones==1):
        #SUMA
        lista_de_Valores=[]
        valor=float(input("Ingresar valor (0 para finalizar):"))
        while True:
            lista_de_Valores.append(valor)
            valor=float(input("Ingresar valor (0 para finalizar):"))
            if valor == 0:
                break
        print(f'La suma de {lista_de_Valores} es: ')
        Suma_Valores = sum(lista_de_Valores)
        print(Suma_Valores)
        
        Mantener_Operacion = input('Deseas seguir con la oprecacion? ("s" para seguir, "n" para salir): ')
        
        if Mantener_Operacion == "s" or Mantener_Operacion == "S":
            print('Okay, seguimos!')
            Opciones = 1
        elif Mantener_Operacion ==  "n" or Mantener_Operacion == "N":
            Opciones = int(input('Escogue un valor: '))      
        else:
            print('Valor incorrecto, vuelva a intentar')
            menu()
 
    elif (Opciones == 2):
        primer_numero = float(input('Primer numero para multiplicar: '))
        segundo_numero = float(input('Segundo numero para multiplicar: '))
        resultado = primer_numero * segundo_numero
        print(resultado)
