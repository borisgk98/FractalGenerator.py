from PIL import Image, ImageDraw
import math, colorsys
imgsz = 400, 400
scale = 4 / imgsz[0]
recursion_depth = 10

img = Image.new("RGB", imgsz)
d = ImageDraw.Draw(img)

pallete = [0] * (recursion_depth + 1)
pallete[0] = (0, 0, 0)
pallete[1] = (5, 0, 10)
for i in range(2, len(pallete)):
    pallete[i] = (pallete[i - 1][0] + 10, pallete[i-1][1], pallete[i-1][2])

def get_point_color(x, y):
    c = complex(x, y)
    it = 0
    z = complex(0, 0)
    for i in range(recursion_depth):
        if z.imag**2 + z.real**2 > 4:
            return it + 1
        z = z*z + c
        it+=1
    return 0

for i in range(imgsz[0]):
    for j in range(imgsz[1]):
        y, x = scale * float(i) - 2.0, scale * float(j) - 2.0
        point_color = pallete[get_point_color(x, y)]
        d.point((j, i), fill = point_color)

img.save("mand.png")