import random

class GeneticSolverClass:

    def __init__(self, size, length, mutationRate):
        self.population = []
        self.size = size 
        self.length = length
        self.mutationRate = mutationRate

    def initialise(self):
        for _ in range(self.size):
            number = ""
            for _ in range(self.length):
                temp = str(random.randint(0,1))
                number += temp
            self.population.append(number)

    def mutate(self):
        mutationNumber = int(self.size * self.mutationRate)
        for _ in range(mutationNumber):
            sampleIndex = random.randint(0,self.size-1)
            print("Index was ", sampleIndex)
            sample = list(self.population[sampleIndex])
            index = random.randint(0,self.length-1)
            if sample[index] == '1':
                sample[index] = '0'
            elif sample[index] == '0':
                sample[index] = '1'
            newString = ''.join(sample)
            self.population[sampleIndex] = newString
            

    def printPopulation(self):
        print(self.population)