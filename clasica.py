from func_globales import numero_valido, operador_valido, operacion


def UI_clasica(num1="", oper="", num2="", result="")->None:

    print(f"""
        Casio
        --- Calculadora CLASICA ---       
          {num1} {oper} {num2}              
                    = {result}

         |1| |2| |3|      |+| |-| 

         |4| |5| |6|      |x| |/|

         |7| |8| |9|      |=|  

         |.| |0|
    """)

#-----------------------------------------------------------------
#                          CALCULADORA
#-----------------------------------------------------------------

def Calculadora_Clasica():
    resultado=0
    UI_clasica()

    num1= input("Ingrese un numero: ")
    num1= numero_valido(num1)

    operador=input("Ingrese el operador: ")
    operador= operador_valido(operador)

    while operador != "=":

        num2= input("Ingrese el segundo numero: ")
        num2= numero_valido(num2)

        while num2==0 and operador=="/":
            print("Error, division por 0 \n")
            num2= input("Reingrese el segundo numero: ")
            num2= numero_valido(num2)

        resultado= operacion(num1, operador, num2)
        resultado=numero_valido(resultado)

        UI_clasica(num1, operador, num2, resultado)
        
        num1=resultado

        print(f"       Esta operando con el numero: {num1} \n")
        
        operador=input("Ingrese el operador: ")
        operador= operador_valido(operador)
    
    UI_clasica(num1, "", "", num1)
