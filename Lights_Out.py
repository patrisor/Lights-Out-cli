# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Lights_Out.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/07/28 06:02:05 by patrisor          #+#    #+#              #
#    Updated: 2019/07/28 07:23:10 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def die(reason):
    print(reason)
    return(-1)

# TODO: Update
def print_board(b):
    print("\ny  |  x     " + ''.join((str(l) + " ") for l in range(len(b))))
    print(("_" * 12) + ("_" * ((2 * len(b)) - 1)))
    for i in range(len(b)):
        print(str(i) + "  |        " + ''.join((str(j) + " ") for j in (b[i])))

# TODO: Fix bugs
def update_board(g, i):
    coord = i.split(",")
    r = int(coord[1])
    c = int(coord[0])
    g[r][c] = (1 if g[r][c] == 0 else 0)
    g[r - 1][c] = (1 if (g[r - 1][c] == 0 and (r - 1) != -1) else 0)
    g[r][c - 1] = (1 if (g[r][c - 1] == 0 and (c - 1) != -1) else 0)
    if c + 1 == len(g[r]) and r + 1 == len(g[r]):
        return -1
    if c + 1 == len(g[r]):
        g[r + 1][c] = (1 if g[r + 1][c] == 0 else 0)
        return 1
    if r + 1 == len(g[r]):
        g[r][c + 1] = (1 if g[r][c + 1] == 0 else 0)
        return 1
    g[r][c + 1] = (1 if g[r][c + 1] == 0 else 0)
    g[r + 1][c] = (1 if g[r + 1][c] == 0 else 0)
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit(die("usage: python3 Lights_Out.py [GRID_WIDTH] [GRID_HEIGHT]"))
    GRID = [[0 for x in range(int(sys.argv[1]))] for y in range(int(sys.argv[2]))]
    while True:
        print_board(GRID)
        inp = input("Where do you want to toggle your light? (X-coord,Y-coord)\n")
        if inp == "q":
            exit(die("Goodbye!"))
        update_board(GRID, inp)
