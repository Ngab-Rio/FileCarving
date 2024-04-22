from PIL import Image

img = Image.open('secret_square.png')
in_pixels = list(img.getdata())
out_pixels = ""
#print(len(in_pixels))
for i in range(len(in_pixels)):
    a = in_pixels[i]
    r = in_pixels[i][0]
    g = in_pixels[i][1]
    b = in_pixels[i][2]
    out_pixels += chr(r+g+b)

print(out_pixels)
