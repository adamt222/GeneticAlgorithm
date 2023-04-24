from GeneticSolver import GeneticSolverClass

size = 100
length = 10
mutationRate = 0.1
crossoverRate = 0.75
generations = 250
solver = GeneticSolverClass(size, length, mutationRate, crossoverRate, generations)
solver.begin()


