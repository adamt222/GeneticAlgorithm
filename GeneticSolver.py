import random
import math
import matplotlib.pyplot as plt


class GeneticSolverClass:

    def __init__(self, size=100, length=10, mutationRate=0.05, crossoverRate=0.75, numberOfGenerations=500):
        self.population = []
        self.newPopulation = []
        self.size = size 
        self.length = length
        self.mutationRate = mutationRate
        self.crossoverRate = crossoverRate
        self.numberOfGenerations = numberOfGenerations

    def initialise(self):
        # Create a random initial population
        for _ in range(self.size):
            number = ""
            for _ in range(self.length):
                temp = str(random.randint(0,1))
                number += temp
            self.population.append(number)

    def mutate(self):
        # Mutate a portion of the population by flipping one bit
        mutationNumber = math.ceil(self.size * self.mutationRate)
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

    def crossover(self, newPopulation):
        # Create an offspring from parents from a portion of the population

        crossoverNumber = math.ceil(self.size * self.crossoverRate)
        weights = [self.objectiveFunction(x) for x in self.population]
        for _ in range(crossoverNumber):
            parent1 = random.choices(self.population , weights=weights, k=1)[0]
            parent2 = random.choices(self.population, weights=weights, k=1)[0]
            offspring = self.onePointCrossover(parent1, parent2)
            newPopulation.append(offspring)

    def bringOver(self, newPopulation):
        # Bring over a portion of the population to the new generation according to their fitness

        bringOverNumber = math.ceil(self.size * (1-self.crossoverRate))
        weights = [self.objectiveFunction(x) for x in self.population]
        for _ in range(bringOverNumber):
            individual = random.choices(self.population , weights=weights, k=1)[0]
            newPopulation.append(individual)

    def onePointCrossover(self, parent1, parent2):
        # Create offsrping with one point crossover

        offspring = ''
        point = random.randint(1, self.length-1)
        while len(offspring) != self.length:
            if len(offspring) < point:
                offspring += parent1[len(offspring)]
            else:
                offspring += parent2[len(offspring)]
        return offspring

    def objectiveFunction(self, individual):
        # Evaluate an individual with the objective function

        number = int(individual, 2)
        number = abs(number*math.sin(number) - math.log10(100*number+1))
        return int(number)

    def begin(self):
        # Start the genetic algorithm 

        self.initialise()
        generation = 0
        avgFitness = []
        while generation < self.numberOfGenerations:
            newPopulation = []
            #print("new size is ", len(newPopulation))
            self.crossover(newPopulation)
            #print("new size is ", len(newPopulation))
            self.bringOver(newPopulation)
            #print("new size is ", len(newPopulation))
            self.population = newPopulation
            #print("new size is ", len(newPopulation))
            self.mutate()
            generation += 1

            #print("Max fitness is ", max([self.costFunction(x) for x in self.population]))
            #print("Size of population is ", len(self.population))
            avgFitness.append((sum([self.objectiveFunction(x)  for x in self.population])/self.size))
        plt.plot([i for i in range(self.numberOfGenerations)], avgFitness)

        plt.xlim([0, self.numberOfGenerations+0.5])
        plt.ylim([0, max(avgFitness)+0.5])
        plt.xlabel("Generations")
        plt.ylabel("Average fitness")
        plt.show()

    def printPopulation(self):
        print(self.population)