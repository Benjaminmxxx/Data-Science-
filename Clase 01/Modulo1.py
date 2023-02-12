def NumeroBinario(numero=int):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Recibe y devuelve un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    bin=[],binario=[], lis2=[], p=''
    
    if numero<0 or type(numero)!=int:
        return None
    elif numero==0:
        return numero
     
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

def NumeroBinarioMejorado(numero=int):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria.
    '''
    bin=[]
    if numero<0 or type(numero)!=int:
        return None
    elif numero==0:
        return numero
    while numero>0: #Mi condicion irá bajando respecto al nuevo valor asiganado a la variable
                    #Derivado de hacer la primer iteración
        unocero=numero%2
        bin.append(str(unocero))
        numero=numero//2
    bin.reverse()#Reverse
    res=''.join(bin)   #Concatenar
    return int(res) #Imprimirlos en un entero


#print(NumeroBinarioMejorado(10))

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
def NumeroFracBinarioMejorado(fraccion):
    '''
    Está función resuelve una fracción a número binario
    '''
    numerobinario='0.'

    while(fraccion>0):
        if len(numerobinario)>=32:
            break
        fraccion*=2
        if fraccion>=1:
            numerobinario+='1'
            fraccion-=1
        else:
            numerobinario+='0'
    
    return float(numerobinario)

print(NumeroFracBinarioMejorado(1/2))

def CualquierNumBinario(numero):
    '''
    Está funcion resuelve cualquier numero con parte entera y decimal a binario
    '''
    parte_entera=int(numero)
    parte_frac=numero-parte_entera

    binario_entero= NumeroBinarioMejorado(parte_entera)
    binario_frac=NumeroFracBinarioMejorado(parte_frac)

    binario_final=binario_entero + binario_frac

    return binario_final

print(CualquierNumBinario(10.5))