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

    # Apply collisions
    for particle_value in ps[:]:
        if ps.count(particle_value) > 1:
            while particle_value in ps:
                index = ps.index(particle_value)
                del ps[index]
                del vs[index]
                del acs[index]


def main(inp):
    particles = []
    velocities = []
    accels = []
    for line in inp:
        particles.append(map(lambda x: int(x.strip("pav=<>")), line[0].split(",")))
        velocities.append(map(lambda x: int(x.strip("pav=<>")), line[1].split(",")))
        accels.append(map(lambda x: int(x.strip("pav=<>")), line[2].split(",")))

    prev_len_particles = None
    counter = 0
    # closest = None
    while True:
        prev_len_particles = len(particles)

        # Update coords and velocities
        update_particle_info(particles, velocities, accels)

        counter = 0 if len(particles) != prev_len_particles else (counter + 1)

        if counter > 1000:
            return len(particles)



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part), ", "))

    print "=== Real ==="
    print main(read_words("input.txt", ", "))
