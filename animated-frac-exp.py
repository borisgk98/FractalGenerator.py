# libs
from PIL import Image, ImageDraw
import os, sys, math
import imageio

# constants
imgsz = 400, 400
scale = 4 / imgsz[0]
gif_duration = 0.05
number_of_mutations = 40

# generate color pallete
pallete = [0] * 2
pallete[0] = (0, 0, 0)  # black color
pallete[1] = (245, 0, 0)  # first color


def color_function(palleteC):
    r, g, b = palleteC[0], palleteC[1], palleteC[2]
    if r and b == 0:
        r -= 35
        g += 35
    elif g:
        g -= 35
        b += 35
    else:
        b -= 35
        r += 35
    return (r, g, b)

next_c = color_function(pallete[1])
while pallete[1] != next_c:
    pallete.append(next_c)
    next_c = color_function(next_c)
recursion_depth = len(pallete) - 1

# fractal function
def fractal_f(z, c, k):
    return z ** k + c


# color function
def get_point_color(x, y, k):

    c = complex(x, y)
    it = 0
    z = complex(0, 0)
    for i in range(recursion_depth):
        if z.imag ** 2 + z.real ** 2 > 4:
            return it + 1
        z = fractal_f(z, c, k)
        it += 1
    return 0


# main part
work_dir_name = "work_dir_for_img"
try:
    os.mkdir(work_dir_name)
except FileExistsError:
    print("Please, remove or delete directory \"" + work_dir_name + "\"")
    sys.exit(0)
images_arr = []

for iteration in range(number_of_mutations):
    img = Image.new("RGB", imgsz)
    d = ImageDraw.Draw(img)

    for i in range(imgsz[0]):
        for j in range(imgsz[1]):
            y, x = scale * float(i) - 2.0, scale * float(j) - 2.0
            point_color = pallete[get_point_color(x, y, iteration / 40 + 2)]
            d.point((j, i), fill=point_color)

    filename = work_dir_name + "\\" + str(iteration) + ".png"
    img.save(filename)
    images_arr.append(imageio.imread(filename))

# create gif
imageio.mimsave("animated_frac.gif", images_arr, duration=gif_duration)
try:
    os.remove(work_dir_name)
except PermissionError:
    print("PermissionError (Access to \"" + work_dir_name + "\")")
