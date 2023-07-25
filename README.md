# sieve
Implementing Sieve of Eratosthenes

## Algorithm

1. Start with a list of primes (initially `[2]`) and a candidate for primeness (initially `3`).
2. For each prime generate the infinite list of multiples of that prime (initially this is `[[2, 4, 6, ...]]`).
3. This list of infinite lists (eventually) contains all composite numbers
4. Keep taking the lowest composite number until this is no longer smaller than the candidate.
   - If the candidate is smaller than this number it must be prime:
     - add it to the list of primes and add its multiples to the list of multiples.
   - If the candidate is equal to the number it must be composite.
5. In either case, increment the candidate by 1 and continue.
