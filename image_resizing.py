
import PIL
from PIL import Image
basewidth = 500

numberOfImages = input()
i=1
while (i<=24): 
    con = "J" + str(i)
    img = Image.open(con + '.jpg')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(str(i)+'.jpg')
    i=i+1
