#! /usr/bin/env python

"""Implement the Sieve of Eratosthenes without using bounds"""
import itertools
import sys
from typing import Generator

# In this code an integer generator is either a generator or a chain of
# list[int] with a generator
IntGenerator = (
    Generator[int, None, None] | itertools.chain[list[int], Generator[int, None, None]]
)


def peek(generator: IntGenerator) -> tuple[int, IntGenerator]:
    """
    Non-destructively extract the first element of a generator

    Args:
        generator: A generator that produces integers

    Returns:
        A tuple containing the first element yielded by the generator together
        with a chain that simulates the original generator
    """
    first = next(generator)
    return (first, itertools.chain([first], generator))


def multiples(n: int) -> IntGenerator:
    """
    Given a number n, return all integer multiples of it

    Args:
        n: an integer

    Returns:
        A generator for all multiples of n
    """
    current = n
    while True:
        current += n
        yield current


def get_minimum(generators: list[IntGenerator]) -> tuple[int, list[IntGenerator]]:
    """
    Given a list of generators check which one has the lowest "next" value then
    pop that and leave the others alone

    Args:
        generators: A list of generators of integers

    Returns:
        A tuple containing the minimum value among all generators plus the list
        of generators. Only the generator containing the minimum value is
        altered.
    """
    # Non-destructively peek at the first elements of each generator
    firsts, generators = zip(*map(peek, generators))
    # This is equivalent to numpy.argmin
    position_of_minimum = min(range(len(firsts)), key=lambda idx: firsts[idx])
    # Ensure that we pop the value from the appropriate generator
    value_of_minimum = next(generators[position_of_minimum])
    return (value_of_minimum, list(generators))


if __name__ == "__main__":
    # Allow the user to set a maximum number of primes to generate
    # If this is not set than the program will not terminate
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None

    # Initialise:
    # - primes and generator lists with 2
    # - initial candidate to 3
    # - next_composite to 0 (needs to be lower than candidate)
    generator_list = [multiples(2)]
    primes = [2]
    candidate = 3
    next_composite = 0

    # Generate primes, stopping when the limit (if any) is reached
    while True:
        # Get the next composite number greater than or equal to the candidate.
        # As each composite appears once for each of its distinct prime factors and
        # each entry is greater than the last, this will terminate
        while next_composite < candidate:
            next_composite, generator_list = get_minimum(generator_list)

        # If the next composite number is larger than the candidate then it is prime
        if next_composite > candidate:
            print(f"Found a prime number: {candidate}")
            primes.append(candidate)
            generator_list.append(multiples(candidate))

        # Increment the candidate
        candidate += 1

        if limit and len(primes) >= limit:
            break

    print("Last prime found", primes[-1])
    sys.exit(0)
