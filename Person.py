class Person:

    def __init__(self, attr, target):
        self.attr=attr
        self.fitness=self.set_fitness(target)


    def set_fitness(self, target):
        equal=0
        diff=0
        for i in range(len(target)):
            if self.attr[i]==target[i]:
                equal+=1
            else:
                diff+=abs(self.attr[i]-target[i])
        return (len(target)-equal,diff)