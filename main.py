import random
import string

TARGET = "to be or not to be"
POPULATION_SIZE = 200
MUTATION_RATE = 0.01
VALID_CHARS = string.ascii_lowercase + " "


class DNA:
    def __init__(self,length):
        self.genes = [random.choice(VALID_CHARS) for _ in range(length)]
        self.fitness = 0

    def get_phrase(self):
        return "".join(self.genes)

    def calc_fitness(self,target):
        matches = sum(1 for g,t in zip(self.genes,target) if g==t)
        self.fitness = (matches/len((target)))**2

    def crossover(self,partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0,len(self.genes)-1)
        for i in range(len(self.genes)):
            child.genes[i] = self.genes[i] if i< midpoint else partner.genes[i]
        return child

    def mutate(self,mutation_rate):
        for i in range(len(self.genes)):
            if random.random()< mutation_rate:
                self.genes[i] = random.choice(VALID_CHARS)


