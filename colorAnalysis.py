import glob
from PIL import Image
from collections import Counter


def berechne():                                                                          #color analysing function

    listMostUsed = []

    for file in glob.glob("*.jpg"):
        img_file = Image.open(file)
        #img = img_file.convert('P', palette=Image.ADAPTIVE, colors=100)
        img = img_file.resize((300,300))

        rgb_img = img.convert('RGB')

        [xs, ys] = img.size

        for x in range(0, xs):
            for y in range(0, ys):
                r, g, b = rgb_img.getpixel((x,y))
                r = reduceColor(r)
                g = reduceColor(g)
                b = reduceColor(b)
                #if 2*r != g+b:
                a = '#%02x%02x%02x' % (r, g, b)
                #listMostUsed.append((r,g,b))
                if 2*g != r+b:								#deletes grey tones as they supress all other colors, implement on and of!
                    listMostUsed.append((a))
                if 2*b != r+g:
                    listMostUsed.append((a))

    b = Counter(listMostUsed).most_common(125)
    return b                                                                         	#returned list

def howmany():                                                                       	#counts how many files will be processed
    counter = 0
    for file in glob.glob("*.jpg"):
        counter += 1

    return str(counter) + " images were analysed."

def reduceColor(a):                                                                     #color reducing and rounding function
    a /= 255
    a = round(a, 2)
    a /= (0.2)
    a = round(a)
    a = (a * 51)
    return a

def readListOne(a, list):                                                       	#split list into tuples with color and count values
    return list[a]                                                              	#return tuple on position a

def getColor(a):                                                                	#return color values of tuple
    color, number = (a)
    return color

def getNumber(a):                                                               	#returns count value of tuple
    color, number = (a)
    return number

def readList(a):
    return getColor(readListOne(a, berechne()))

