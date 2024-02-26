import generation
import random



def calculate_fitness(population,target):
    '''
    Calcola la fitness per ogni persona(solo se è False, cioè ancora da calcolare) sapendo il target
    '''
    for person in population:
        if person[-1]==False:
            equal=0
            diff=0
            for i in range(len(target)):
                if person[i]==target[i]:
                    equal+=1
                else:
                    diff+=abs(person[i]-target[i])
            person[-1]=(len(target)-equal,diff)
    population.sort(key=lambda x:x[-1])
    return population



def genetic(target,n_pop,mutation_rate,min,max):
    population=generation.first_gen(n_pop,len(target),min,max)
    population=calculate_fitness(population,target)
    n_gen=1
    while population[0][:-1]!=target:
        print(n_gen,"|fitness:",population[0][-1],"|persone:",len(population))
        population=generation.new_gen(population,mutation_rate,min,max)
        population=calculate_fitness(population,target)
        n_gen+=1
    print(n_gen,"|fitness:",population[0][-1],"|persone:",len(population))
    print(population[0][:-1])
    return n_gen



if __name__=="__main__":
    target=[random.randint(0,100) for i in range(50)]
    print(target)
    n_gen=genetic(target,500,10,0,100)
    print("Generazioni necessarie:", n_gen)






