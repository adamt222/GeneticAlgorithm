import random

class GeneticSolverClass:

    def __init__(self, size=100, length=10, mutationRate=0.05, crossoverRate=0.75):
        self.population = []
        self.newPopulation = []
        self.size = size 
        self.length = length
        self.mutationRate = mutationRate
        self.crossoverRate = crossoverRate

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
            sample = list(self.population[sampleIndex])
            index = random.randint(0,self.length-1)
            if sample[index] == '1':
                sample[index] = '0'
            elif sample[index] == '0':
                sample[index] = '1'
            newString = ''.join(sample)
            self.population[sampleIndex] = newString

    def Crossover(self):
        crossoverNumber = self.size * self.crossoverRate
        weights = []
        for _ in range(crossoverNumber):
            parent1 = random.choice(self.population , weights = weights)
            parent2 = random.choice(self.population, weights = weights)
            offspring = self.onePointCrossover(parent1, parent2)

    def onePointCrossover(self, parent1, parent2):
        offspring = ''
        point = random.randint(1, self.length-1)
        while len(offspring) != self.length:
            if len(offspring) < point:
                offspring += parent1[len(offspring)]
            else:
                offspring += parent2[len(offspring)]
        return offspring



    def costFunction(self, individual):
        number = int(individual, 2)
        return number

    def printPopulation(self):
        print(self.population)