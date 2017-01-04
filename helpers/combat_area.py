


with open('area_points.txt') as ca_fo:
    for line in ca_fo:
        newline = line.replace('CombatArea.addAreaPoint ', '(').replace('\n', '),')
        print(newline)