import random

def new_gen(population,mutation_rate,min,max):
    '''
    Crea una nuova generazione eliminando la metà peggiore e ripopolandola creando ogni figlio
    con due genitori scelti casualmente.
    Ogni attributo del figlio è una mutazione con valore tra min e max con probabilità mutation_rate
    sennò viene ereditato con la stessa probabilità dal primo o secondo genitore
    '''
    size=len(population)
    population=population[0:round((size+1)/2)]
    for i in range(size-len(population)):
        par1=random.randint(0,round(size/2)-1)
        par2=random.randint(0,round(size/2)-1)
        son=[]
        for j in range(0,len(population[0])-1):
            rand_attr=random.randint(1,100)
            if rand_attr<=((100-mutation_rate)/2):
                son.append(population[par1][j])
            elif rand_attr<=(100-mutation_rate):
                son.append(population[par2][j])
            else:
                son.append(random.randint(min,max))
        son.append(False)
        population.append(son)
    return population



def first_gen(n_pop,n_attr,min,max):
    '''
    Crea una popolazione iniziale di numero start_pop con n_attr attributi ognuno
    con valori tra min e max e una fitness inizializzata a False
    '''
    population=[([random.randint(min,max) for j in range(n_attr)]+[False]) for i in range(n_pop)]
    return population