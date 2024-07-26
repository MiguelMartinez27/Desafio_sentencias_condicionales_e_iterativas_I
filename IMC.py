#verificador de valores numéricos ingresados
def verificador(value):
    try:
        float(value)
        return True
    except(TypeError,ValueError):
        return False
#definición de la variable imc, con ciclos while para acciones condicionadas
def imc():
    while True:
        peso = input('Ingresa tu peso en [kg]: ')
        if verificador(peso) and peso>"0":
            w = float(peso)  #asignación de input a la variable w usada en la fórmula
            break
        else: 
            print('El peso debe ser un número positivo: ')

    while True:
        altura = float(input('Ingresa tu altura en [cm]: '))  #conversión de input a float para evitar typeError 
        if verificador(altura) and altura>0:  
            altura_en_metros=(altura*0.01)  #aqui se produce typeError si no se cambia el input de string a float, mas conversión de cm a metros
            h=float(altura_en_metros)
            break
        else:
            print('La altura debe ser un número positivo')

    while True:
        imcexacto = (w/(h**2))          #formula de imc
        imc = round(imcexacto,2)           #redondeo a dos decimales
        print(f'Tu imc es de {imc}.')
        if imc < 18.5:                  #clasificación de imc
            print('La clasificación OMS es Bajo peso')
        elif imc >= 18.5 and imc < 25:
            print('La clasificación OMS es Adecuado')
        elif imc >= 25 and imc < 30:
            print('La clasificación OMS es Sobrepeso')
        elif imc >= 30 and imc < 35:
            print('La clasificación OMS es Obesidad Grado I')
        elif imc >= 35 and imc <40:
            print('La clasificación OMS es Obesidad Grado II')
        elif imc >= 40:
            print('La clasificación OMS es Obesidad Grado III')
        break

while True:
    imc()
    break