import os
import sys
import PIL
import time
from PIL import Image, ImageDraw


def recalculate_point(point_y, point_x, map_size):
    # bf2 maps coordinates are floats from center
    # we're using 2k images here while maps can be 1k, 2k, 4k
    """
    4k map, point 2048/2048 right top corner
            point 1024/1024 right top square mid => 512/512 => 1024+512 => 1024 + modifier*point
            
    4k map, point -2048/2048 left top corner => 0/0
            point -2048/-2048 left bottom corner => 0/2048
            point 2048/-2048 right bottom corner => 2048/2048
            point 0/0 center => 1024/1024
            point -1024/0 left => 1024/0
    """
    modifiers = {
        512 : 0.25,
        1024 : 0.5,
        2048 : 1,
        4096 : 2
        }
    offset = 1024.0*modifiers[map_size] # no idea but this worked
    point_y = (float(point_y) + offset)/modifiers[map_size]
    point_x = (float(point_x) + offset)/modifiers[map_size]
    return point_y, point_x

def main():
    original_minimap = 'ingamemap_ramiel.dds'
    map_size = 2048

    img = Image.open(original_minimap)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    print(img.size)
    
    
    points = []
    with open('area_points.txt') as ca_fo:
        for line in ca_fo:
            point_y, point_x = line.replace('\n', '').split(' ')[1].split('/')
            point_y, point_x = recalculate_point(point_y, point_x, map_size)
            points.append((float(point_y), float(point_x)))
            print((point_y, point_x))
        points.append(points[0])
    
    #im = Image.new('RGB', (2048, 2048))
    draw = ImageDraw.Draw(img)
    draw.line(points, fill='red', width=5) # outline='red', fill='blue'
    new_points = [
        (512, 512),
        (512, 512),
        ]
    #draw.line(new_points, fill='red', width=6) # outline='red', fill='blue'
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save(original_minimap.replace('.dds', '.png'))
    img.close()


if __name__ == '__main__':
    main()