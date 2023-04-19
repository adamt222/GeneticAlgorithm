from GeneticSolver import GeneticSolverClass

solver = GeneticSolverClass(100, 10, 0.05)
solver.initialise()
print(solver.onePointCrossover("1111111111", "0000000000"))
