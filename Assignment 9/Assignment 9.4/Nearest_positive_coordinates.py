# Assignment 9.4 - Nearest positive coordinates

#        This is problem to convert all the negative coordinates to a positive coordinates;
#        The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
#        We can add or delete any number from the coordinates ; however graph should not be changed;

#        Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
#        Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]



coordinates = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
max_x = max_y = 0

for x, y in coordinates:
    if x < 0:
        max_x = max(max_x, abs(x))
    if y < 0:
        max_y = max(max_y, abs(y))

new_coordinates = [(x+max_x, y+max_y) for x, y in coordinates]

print(new_coordinates)
