from rembg import remove
from PIL import Image

input = Image.open('hero-bg.jpg')
output = remove(input)
output.save('output.png')