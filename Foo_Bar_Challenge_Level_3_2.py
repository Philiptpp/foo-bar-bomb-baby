"""
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.
"""
import math


def true_result(M, F):
    m, f = int(M), int(F)
    generations = 0
    while (m > 1) or (f > 1):
        if m > f:
            m = m - f
            generations += 1
        elif f > m:
            f = f - m
            generations += 1
        else:
            break
        if (m == 0) or (f == 0):
            break
    if f == m == 1:
        return '%d' % generations
    else:
        return 'impossible'


def answer(M, F):
    m, f = int(M), int(F)
    generations = 0
    while (m > 1) and (f > 1):
        if f > m:
            div = int(math.floor(f / m))
            f = f - (m * div)
            generations += div
        elif m > f:
            div = int(math.floor(m / f))
            m = m - (f * div)
            generations += div
        else:
            return 'impossible'
    if (m <=0) or (f <=0):
        return 'impossible'
    else:
        if m == 1:
            generations += (f - 1)
        elif f == 1:
            generations += (m - 1)
        return '%d' % generations

if __name__ == '__main__':
    import random
    import progressbar
    bar = progressbar.ProgressBar()
    for _ in bar(range(1000)):
        m = random.randint(1, 10**50)
        f = random.randint(1, 10**50)
        #print('Testing %d %d' % (m, f))
        if not answer(m, f) == true_result(m, f):
            print('*** TEST FAILED for %d %d ***' % (m, f))
