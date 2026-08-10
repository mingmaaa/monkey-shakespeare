import random
import string

TARGET = "a wise man can code"
POPULATION_SIZE = 250
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

class Population:
    def __init__(self,target,mutation_rate,size):
        self.target = target
        self.mutation_rate = mutation_rate
        self.population = [DNA(len(target)) for _ in range(size)]
        self.generations = 0
        self.mating_pool = []
        self.best_phrase = ""

    def calc_fitness(self):
        for individual in self.population:
            individual.calc_fitness(self.target)

    def natural_selection(self):
        self.mating_pool=[]
        max_fitness = max(ind.fitness for ind in self.population) or 1
        for individual in self.population:
            n = int((individual.fitness/max_fitness)*100)
            self.mating_pool.extend([individual]*n)

    def generate(self):
        new_population =[]
        for _ in range(len(self.population)):
            if self.mating_pool:
                parent_a = random.choice(self.mating_pool)
                parent_b = random.choice(self.mating_pool)
            else:
                parent_a = random.choice(self.population)
                parent_b = random.choice(self.population)
            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            new_population.append(child)
        self.population = new_population
        self.generations+=1
    def get_best(self):
        best = max(self.population,key=lambda ind:ind.fitness)
        self.best_phrase = best.get_phrase()
        return best

    def evaluate(self):
        best = self.get_best()
        return best.get_phrase(),best.fitness

def run():
    population = Population(TARGET, MUTATION_RATE, POPULATION_SIZE)

    while True:
        population.calc_fitness()
        population.natural_selection()
        phrase, fitness = population.evaluate()
        print(f"Gen {population.generations:4d} | "
              f"Fitness {fitness:.4f} | Best: '{phrase}'")
        if phrase == TARGET:
            print(f"\nTarget matched in {population.generations} generations!")
            break
        population.generate()


if __name__ == "__main__":
    run()
    
