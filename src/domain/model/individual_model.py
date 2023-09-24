from random import random

class IndividualModel():
    def __init__(self, spaces, values, space_limit, chromosome, generation = 0):
        self.spaces = spaces
        self.values = values
        self.space_limit = space_limit
        self.usage_space = 0
        self.generation = generation
        self.evaluation = 0
        self.chromosome = chromosome

        if len(self.chromosome) == 0:
            for _ in range(len(self.spaces)):
                if random() < 0.5:
                    self.chromosome.append("0")
                else:
                    self.chromosome.append("1")

    def calculate_evaluation(self):
        evaluation = 0
        spaces_sum = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == "1":
                evaluation += self.values[i]
                spaces_sum += self.spaces[i]
            
        if spaces_sum > self.space_limit:
            evaluation = 1

        self.evaluation = evaluation
        self.usage_space = spaces_sum

    def crossover(self, other):
        split = round(random() * len(self.chromosome))

        child_one = other.chromosome[0:split] + self.chromosome[split::]
        child_two = self.chromosome[0:split] + other.chromosome[split::]
        
        return [
            IndividualModel(spaces=self.spaces, 
                            values=self.values, 
                            space_limit=self.space_limit, 
                            generation=self.generation +1,
                            chromosome=child_one),
            IndividualModel(spaces=self.spaces, 
                            values=self.values, 
                            space_limit=self.space_limit, 
                            generation=self.generation +1,
                            chromosome=child_two)
        ]
    
    def mutation(self, tax):
        for i in range(len(self.chromosome)):
            if random() < tax:
                if self.chromosome[i] == "1":
                    self.chromosome[i] = "0"
                else:
                    self.chromosome[i] = "1"
        return self
