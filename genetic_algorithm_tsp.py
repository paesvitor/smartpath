from settings import MAX_TIME, SPEED, POPULATION_SIZE, GENERATIONS, CXPB, MUTPB
from create_distance_matrix import create_distance_matrix
from deap import base, creator, tools, algorithms
import random
from evaluate import evaluate

def genetic_algorithm_tsp(points, garage_idx, office_idx, toolbox):
    distance_matrix = create_distance_matrix(points)
    
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate, distance_matrix=distance_matrix,
                   start_idx=garage_idx, end_idx=office_idx)
    
    pop = toolbox.population(n=POPULATION_SIZE)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    for gen in range(GENERATIONS):
        offspring = algorithms.varAnd(pop, toolbox, cxpb=CXPB, mutpb=MUTPB)
        
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        pop = toolbox.select(offspring + pop, k=len(pop))
    
    return tools.selBest(pop, k=1)[0]