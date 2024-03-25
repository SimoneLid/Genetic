import random
import Person



def first_gen(n_pop,n_attr,min,max,target):
    '''
    Crea una popolazione iniziale di numero start_pop con n_attr attributi ognuno
    con valori tra min e max e una fitness inizializzata a False
    '''
    population=[Person.Person([random.randint(min,max) for j in range(n_attr)],target) for i in range(n_pop)]
    population.sort(key= lambda x:x.fitness)
    return population


def new_gen(population,mutation_rate,min,max,target):
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
        son_attr=[]
        for j in range(0,len(population[0].attr)):
            rand_attr=random.randint(1,100)
            if rand_attr<=((100-mutation_rate)/2):
                son_attr.append(population[par1].attr[j])
            elif rand_attr<=(100-mutation_rate):
                son_attr.append(population[par2].attr[j])
            else:
                son_attr.append(random.randint(min,max))
        son=Person.Person(son_attr,target)
        population.append(son)
    population.sort(key= lambda x:x.fitness)
    return population