import os
import sys
import PIL
import time
from PIL import Image, ImageDraw


def recalculate_point(point_y, point_x):
    point_y = float(point_y) + 1024.0
    point_x = float(point_x) + 1024.0
    return point_y, point_x

original_minimap = 'ingamemap_ramiel.tga'
points = []

with open('area_points.txt') as ca_fo:
    for line in ca_fo:
        point_y, point_x = line.replace('\n', '').split(' ')[1].split('/')
        point_y, point_x = recalculate_point(point_y, point_x)
        points.append((float(point_y), float(point_x)))
        print((point_y, point_x))
    points.append(points[0])

def main():
    img = Image.open(original_minimap)
    print(img.size)
    
    #im = Image.new('RGB', (2048, 2048))
    draw = ImageDraw.Draw(img)
    draw.line(points, fill='red', width=6) # outline='red', fill='blue'
    img.save('dod.jpg')
    img.close()


if __name__ == '__main__':
    main()