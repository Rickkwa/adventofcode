import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def update_particle_info(ps, vs, acs):
    for i in range(len(ps)):
        # Apply accel
        vs[i] = map(lambda t: sum(t), zip(vs[i], acs[i]))
        # Apply vel
        ps[i] = map(lambda t: sum(t), zip(ps[i], vs[i]))


def main(inp):
    particles = []
    velocities = []
    accels = []
    for line in inp:
        particles.append(map(lambda x: int(x.strip("pav=<>")), line[0].split(",")))
        velocities.append(map(lambda x: int(x.strip("pav=<>")), line[1].split(",")))
        accels.append(map(lambda x: int(x.strip("pav=<>")), line[2].split(",")))

    prev_closest = 0
    counter = 0
    closest = None
    while True:
        prev_closest = closest
        closest = 0
        closest_dist = abs(particles[closest][0]) + abs(particles[closest][1]) + abs(particles[closest][2])
        # Get closest particle
        for i in range(len(particles)):
            p = particles[i]
            # calculate value, and check if < closest_dist and update closest=i if it is
            dist = abs(p[0]) + abs(p[1]) + abs(p[2])
            if dist < closest_dist:
                closest_dist = dist
                closest = i

        counter = 0 if closest != prev_closest else (counter + 1)

        # If counter > X, then return `closest` since it hasn't changed in a while
        if counter > 1000:
            return closest

        # Update coords and velocities
        update_particle_info(particles, velocities, accels)


if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    # print main(read_words("sample{0}.txt".format(part), ", "))

    print "=== Real ==="
    print main(read_words("input.txt", ", "))
