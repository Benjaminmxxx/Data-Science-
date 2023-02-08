def NumeroBinario(numero=int):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Recibe y devuelve un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    bin=[]
    binario=[]
    lis2=[]
    p=''
    if numero<0 or type(numero)!=int:
        return None

    while numero>0: #Mi condicion irá bajando respecto al nuevo valor asiganado a la variable
                    #Derivado de hacer la primer iteración

        if(numero%2==0):
            bin.append(0)
        else:
            bin.append(1)
        #print(numero) #Para pruebas
        numero=int(numero/2)

    for i in range (0,len(bin)): #Reverse
        binario.append(bin[-i-1])
    
    for j in binario: #Pasar a una lista donde unicamente datos sean tipo string
        if type(j)==int:
            lis2.append(str(j))

    for k in range (len(lis2)): #Concatenar los numeros de tipo string
        p+=lis2[k]   

    n=int(p) #Pasar los datos (numeros) concatenados a entero 

    return n #Imprimirlos en un entero

print(NumeroBinario(12))

def NumeroFracBinario(num):
    '''
    Esta función recibe una fracción y da como resultado su representación en numero
    binario, de acuerdo al metodo "Multiplicación Suseciva" 

    '''
    frac=str(num)
    lista2=[]
    lis3=[]
    p='0.'
    while num!=1.0:
            num=num*2
            #print(num)
            if num==1:
                lista2.append(1)
            if num<1:
                lista2.append(0)
            elif (num>1):
                #print('hola') #Me ayuda para saber como estaba funcionando el ciclo
                lista2.append(1)
                num=num-1
    for j in lista2:

        if type(j)==int:
            lis3.append(str(j))
    for k in range (len(lis3)):

        p+=lis3[k]
    
    return print ('Binario de la fracción', frac, 'es', p)

'''
NumeroFracBinario(1/2)
NumeroFracBinario(1/3)
NumeroFracBinario(1/4)
NumeroFracBinario(1/5)
NumeroFracBinario(1/6)
NumeroFracBinario(1/7)
NumeroFracBinario(1/8)
NumeroFracBinario(1/9)
'''
