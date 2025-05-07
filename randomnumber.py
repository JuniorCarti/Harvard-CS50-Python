#random numbers
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# The random module provides various functions to generate random numbers, including:
# - random(): Returns a random float number between 0.0 and 1.0.
# - randrange(start, stop): Returns a random integer between the specified start and stop values (inclusive of start and exclusive of stop).
# - randint(start, stop): Returns a random integer between the specified start and stop values (inclusive of both start and stop).
# - choice(sequence): Returns a random element from the specified sequence (list, tuple, or string).
# - shuffle(sequence): Shuffles the elements of the specified sequence in place.
# - sample(sequence, k): Returns a list of k unique elements chosen from the specified sequence.
# - uniform(start, stop): Returns a random float number between the specified start and stop values.
# - seed(a=None): Initializes the random number generator with the specified seed value.
# - getstate(): Returns the current state of the random number generator.
# - setstate(state): Restores the state of the random number generator to the specified state.
# - random.seed(a=None): Initializes the random number generator with the specified seed value.
# - random.getstate(): Returns the current state of the random number generator.
# - random.setstate(state): Restores the state of the random number generator to the specified state.
# - random.randrange(start, stop[, step]): Returns a randomly selected element from range(start, stop[, step]).
# - random.randint(a, b): Returns a random integer N such that a <= N <= b.
# - random.choice(seq): Returns a randomly selected element from seq.
# - random.shuffle(x[, random]): Shuffles the sequence x in place.
# - random.sample(population, k): Returns a k length list of unique elements chosen from the population sequence.
# - random.uniform(a, b): Returns a random float number between the specified start and stop values.
# - random.triangular(low, high, mode): Returns a random float number between the specified low and high values, with the specified mode value.
# - random.betavariate(alpha, beta): Returns a random float number between 0 and 1, with the specified alpha and beta values.
# - random.expovariate(lambd): Returns a random float number between 0 and infinity, with the specified lambda value.
# - random.gammavariate(alpha, beta): Returns a random float number between 0 and infinity, with the specified alpha and beta values.
# - random.gauss(mu, sigma): Returns a random float number between negative infinity and positive infinity, with the specified mu and sigma values.
# - random.lognormvariate(mu, sigma): Returns a random float number between 0 and positive infinity, with the specified mu and sigma values.
# - random.normalvariate(mu, sigma): Returns a random float number between negative infinity and positive infinity, with the specified mu and sigma values.
# - random.vonmisesvariate(mu, kappa): Returns a random float number between negative pi and positive pi, with the specified mu and kappa values.
# - random.paretovariate(alpha): Returns a random float number between 0 and positive infinity, with the specified alpha value.
# - random.weibullvariate(alpha, beta): Returns a random float number between 0 and positive infinity, with the specified alpha and beta values.

import random

print(random.random()) # Returns a random float number between 0.0 and 1.0.
print(random.randrange(1, 10)) # Returns a random integer between the specified start and stop values (inclusive of start and exclusive of stop).
print(random.randint(1, 10)) # Returns a random integer between the specified start and stop values (inclusive of both start and stop).
print(random.choice(['apple', 'banana', 'cherry'])) # Returns a random element from the specified sequence (list, tuple, or string).
print(random.shuffle(['apple', 'banana', 'cherry'])) # Shuffles the elements of the specified sequence in place.
print(random.sample(['apple', 'banana', 'cherry'], 2)) # Returns a list of k unique elements chosen from the specified sequence.
print(random.uniform(1, 10)) # Returns a random float number between the specified start and stop values.
print(random.seed(10)) # Initializes the random number generator with the specified seed value.
print(random.getstate()) # Returns the current state of the random number generator.
print(random.setstate(random.getstate())) # Restores the state of the random number generator to the specified state.
print(random.randrange(1, 10, 2)) # Returns a randomly selected element from range(start, stop[, step]).
print(random.randint(1, 10)) # Returns a random integer N such that a <= N <= b.
print(random.choice(['apple', 'banana', 'cherry'])) # Returns a randomly selected element from seq.
print(random.shuffle(['apple', 'banana', 'cherry'])) # Shuffles the sequence x in place.
print(random.sample(['apple', 'banana', 'cherry'], 2)) # Returns a k length list of unique elements chosen from the population sequence.
print(random.uniform(1, 10)) # Returns a random float number between the specified start and stop values.