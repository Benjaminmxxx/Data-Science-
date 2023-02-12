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

def NumeroFracBinarioMejorado(fraccion):
    '''
    Está función resuelve una fracción a número binario
    '''
    numerobinario='0.'

    while(fraccion>0):
        if len(numerobinario)>=32: #Tope por los decimales que tienen. 
            break 
        fraccion*=2
        if fraccion>=1:
            numerobinario+='1'
            fraccion-=1
        else:
            numerobinario+='0'
    
    return float(numerobinario)

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