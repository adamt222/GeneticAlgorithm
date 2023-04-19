from GeneticSolver import GeneticSolverClass

solver = GeneticSolverClass(100, 10, 0.05)
solver.initialise()
solver.printPopulation()
solver.mutate()
solver.printPopulation()
