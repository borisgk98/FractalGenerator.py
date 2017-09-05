from PIL import Image, ImageDraw
import math, colorsys
imgsz = 16384, 16384
scale = 4 / imgsz[0]
recursion_depth = 400

img = Image.new("RGB", imgsz)
d = ImageDraw.Draw(img)

pallete = [0] * (recursion_depth + 1)
pallete[0] = (0, 0, 0)  # black color
pallete[1] = (245, 0, 0) # first color

def color_function(palleteC):
	r, g, b = palleteC[0], palleteC[1], palleteC[2] 
	if r:
		r -= 35
		g += 35
	elif g:
		g -= 35
		b += 35
	else:
		b -= 35
		r += 35
	return (r, g, b)   

for i in range(2, len(pallete)):
    pallete[i] = color_function(pallete[i-1])

def fractal_f(z, c):
	return z**2 + c

def get_point_color(x, y):
    c = complex(x, y)
    it = 0
    z = complex(0, 0)
    for i in range(recursion_depth):
        if z.imag**2 + z.real**2 > 4:
            return it + 1
        z = fractal_f(z, c)
        it += 1
    return 0

for i in range(imgsz[0]):
    for j in range(imgsz[1]):
        y, x = scale * float(i) - 2.0, scale * float(j) - 2.0
        point_color = pallete[get_point_color(x, y)]
        d.point((j, i), fill = point_color)

img.save("big(16384x16384)colorMand.png")