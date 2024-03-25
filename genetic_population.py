import generation
import random
import math



def genetic(target,n_pop,mutation_rate,min,max):
    print("Target:",target)
    max_not_exact=int(math.log(len(target),10))
    max_difference=int(math.log((max-min)*len(target),10))
    population=generation.first_gen(n_pop,len(target),min,max,target)
    n_gen=1
    while population[0].attr!=target:
        print('{0: >7}'.format(n_gen),"|fitness:",'{0: <{width}}'.format(population[0].fitness[0],width=max_not_exact),'{0: >{width}}'.format(population[0].fitness[1],width=max_difference),"|attributi:",len(target),"|persone:",len(population))
        population=generation.new_gen(population,mutation_rate,min,max,target)
        n_gen+=1
    print('{0: >7}'.format(n_gen),"|fitness:",'{0: <{width}}'.format(population[0].fitness[0],width=max_not_exact),'{0: >{width}}'.format(population[0].fitness[1],width=max_difference),"|attributi:",len(target),"|persone:",len(population))
    print("Generazioni necessarie:", n_gen)


if __name__=="__main__":
    n_population=500
    mutation_rate=10
    min=0
    max=100
    n_attribute=100
    target=[random.randint(min,max) for i in range(n_attribute)]
    genetic(target,n_population,mutation_rate,min,max)
    






