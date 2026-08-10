# monkey-shakespeare

A Python implementation of a genetic algorithm that evolves a population of
random strings into a target phrase, proving once and for all that an
infinite number of monkeys on an infinite number of keyboards will eventually
stop mashing `qwerty` and produce something legible. This one just does it a
little faster.

Inspired by the Genetic Algorithms chapter of Daniel Shiffman's
*The Nature of Code* (Chapter 9: Evolutionary Computing), whose original
examples are written in Processing/JavaScript.

## How it works

1. **Population**: start with a population of random strings ("DNA"), each
   the same length as the target phrase. Mostly gibberish. Some real gems.
2. **Fitness**: each string is scored by how many characters match the
   target in the correct position. The gibberish gets no participation trophy.
3. **Selection**: fitter individuals get more chances to reproduce, via a
   weighted mating pool. Natural selection, minus the nature.
4. **Crossover**: two parents combine their genes at a random midpoint to
   produce a child, who is somehow still slightly wrong.
5. **Mutation**: each gene has a small chance to randomly mutate, keeping
   genetic diversity alive so the population doesn't get stuck in local
   mediocrity.
6. Repeat until a generation finally spells things correctly, unlike autocorrect.

## Usage

```bash
python main.py
```

Edit `TARGET`, `POPULATION_SIZE`, or `MUTATION_RATE` at the top of `main.py`
to experiment with different phrases or convergence speeds.

## Example output

![monkey-shakespeare demo](demo.gif?v=2)



## Credits

Concept and original implementation: Daniel Shiffman, *The Nature of Code*
(Chapter 9: Evolutionary Computing). https://natureofcode.com/

Inspired by the original example, "Genetic Algorithm, Evolving Shakespeare,"
written in Processing/JavaScript. No monkeys, Shakespeares, or typewriters
were harmed in the making of this repo.
