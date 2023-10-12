import numpy
import random

from deap import algorithms, base, creator, tools

class GenericAlgorithmDeap():
    def __init__(self, spaces, values, space_limit, mutation_probability = 0.01, crossover_probability = 1.0):
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.spaces = spaces
        self.values = values
        self.space_limit = space_limit

        self.toolbox = base.Toolbox()

        creator.create("FitnessMax", base.Fitness, weights=(1.0, ))
        creator.create("Individual", list, fitness=creator.FitnessMax)
        
        self.toolbox.register("attr_bool", random.randint, 0, 1)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_bool, n=len(spaces))
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", self.calculate_evaluation)
        self.toolbox.register("mate", tools.cxOnePoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb = mutation_probability)
        self.toolbox.register("select", tools.selRoulette)

    def calculate_evaluation(self, individual):
        evaluation = 0
        sum_spaces = 0
        sum_values = 0
        for i in range(len(individual)):
            if individual[i] == 1:
                evaluation += self.values[i]
                sum_spaces += self.spaces[i]
            sum_values += self.values[i]
        if sum_spaces > self.space_limit:
            evaluation = 1
        return evaluation / sum_values, 

    def run(self, number_of_generations, population_size):
        population = self.toolbox.population(n=population_size)

        statistics = tools.Statistics(key=lambda individual: individual.fitness.values)
        statistics.register("max", numpy.max)
        statistics.register("min", numpy.min)
        statistics.register("mean", numpy.mean)
        statistics.register("std", numpy.std)
        
        result_population, info = algorithms.eaSimple(population,
                                                    self.toolbox, 
                                                    self.crossover_probability, 
                                                    self.mutation_probability,
                                                    number_of_generations, 
                                                    statistics)
        
        return tools.selBest(result_population, 1)[0], info
        