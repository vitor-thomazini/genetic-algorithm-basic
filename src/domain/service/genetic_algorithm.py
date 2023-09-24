from random import random
from ..model import IndividualModel

class GeneticAlgorithm:
    def __init__(self, population_size) -> None:
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = None
        self.solutions = []

    def init_population(self, spaces, values, space_limit):
        for _ in range(self.population_size):
            self.population.append(IndividualModel(spaces=spaces, values=values, space_limit=space_limit, chromosome=[]))
        self.best_solution = self.population[0]

    def sort_population(self):
        self.population = sorted(self.population, key= lambda population: population.evaluation, reverse=True)

    def best_individual(self, individual):
        if individual.evaluation > self.best_solution.evaluation:
            self.best_solution = individual

    def sum_evaluation(self):
        total = 0
        for individual in self.population:
            total += individual.evaluation
        return total
    
    def get_parent(self, total_evaluation):
        parent = -1
        selected_value = random() * total_evaluation
        value = 0
        idx = 0
        while idx < len(self.population) and value < selected_value:
            value += self.population[idx].evaluation
            idx += 1
            parent += 1
        return parent
    
    def log(self, individual):
        self.solutions.append(individual.evaluation);
        print("G: %s -> Value: %s; Space: %s; Chromosome: %s" % (individual.generation, 
                                                                 individual.evaluation, 
                                                                 individual.usage_space, 
                                                                 individual.chromosome))
        
    def run(self, mutation_probability, number_of_generations, spaces, values, space_limit):
        self.init_population(spaces=spaces, values=values, space_limit=space_limit)

        for individual in self.population:
            individual.calculate_evaluation()

        self.sort_population()
        self.log(individual=self.population[0])
        for _ in range(number_of_generations):
            new_population = []
            total_evaluation = self.sum_evaluation()

            for individual in range(0, self.population_size, 2):
                parent_one = self.get_parent(total_evaluation=total_evaluation)
                parent_two = self.get_parent(total_evaluation=total_evaluation)
                children = self.population[parent_one].crossover(self.population[parent_two])
                new_population.append(children[0].mutation(mutation_probability))
                new_population.append(children[1].mutation(mutation_probability))

            self.population = list(new_population)  

            for individual in self.population:
                individual.calculate_evaluation()

            self.sort_population()
            self.log(individual=self.population[0])
            self.best_individual(self.population[0])

        print("\n============ BEST SOLUTION =============")
        self.log(self.best_solution)
        return self.best_solution.chromosome
