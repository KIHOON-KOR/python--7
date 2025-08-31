pi = 3.141592
def triangle_extent(base, height):
    return 0.5 * base * height

def circle_extent(radius):
    return pi * radius ** 2

def cuboid_extent(length, width, height):
    return 2 * (length * width + width * height + height * length)