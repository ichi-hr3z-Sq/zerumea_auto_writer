#sShot comparison
#trimming 3*4 + 4*2 = 20pics & comparison
#-----------------------------------------------------------#


#File name = sShot.png (named by- sShot.py)
from PIL import Image
im = Image.open(r'C:\Users\50811073\Dropbox\Programming\myAppByPy\ゼルメアライター\check\sShotPng\sShot.png')

#change capcher size [1280*720] to [1920*1080] = magnification 1.5
cMag=1.5

#map trimmng by 3*4
i = 0
for row in range(4):
    for column in range(3):
        move = [86.5*column*cMag, 86.5*row*cMag]
        span = 40*cMag
        sXY = [98*cMag, 264*cMag]
        nXY = [sXY[0]+move[0], sXY[1]+move[1]]
        box = (nXY[0]-span, nXY[1]-span, nXY[0]+span, nXY[1]+span)
        savePath = r'C:\Users\50811073\Dropbox\Programming\myAppByPy\ゼルメアライター\check\sShotPng\trimmed\map' +'\\'+ str(i)+ '.png'
        i += 1
        im.crop(box).save(savePath)

#undifined trimmig by 4*2
i = 0
for row in range(2):
    for column in range(4):
        move = [48*column*cMag, 39*row*cMag]
        box = (84*cMag+move[0],572*cMag+move[1], 132*cMag+move[0],620*cMag+move[1])
        savePath = r'C:\Users\50811073\Dropbox\Programming\myAppByPy\ゼルメアライター\check\sShotPng\trimmed\undifined' +'\\'+ str(i)+ '.png'
        i += 1
        im.crop(box).save(savePath)


#-----------------------------------------------------#


#comparison body
#import ImageHash - for comparison
from PIL import Image
import imagehash as ihash

#comparison main map
#load img.jpg
imgBox = []
for img in range(23):
    imgPath = r'C:\Users\50811073\Dropbox\Programming\myAppByPy\ゼルメアライター\img'+'\\'+str(img)+'.png'
    #print(imgPath)
    ohash = ihash.average_hash(Image.open(imgPath))
    imgBox.append(ohash)
    #print(imgBox[img])

#load trimming - map.png
mapBox = []
for i in range(12):
    ssPath = r'C:\Users\50811073\Dropbox\Programming\myAppByPy\ゼルメアライター\check\sShotPng\trimmed\map'+ '\\'+str(i) +'.png'
    shash = ihash.average_hash(Image.open(ssPath))
    #print('i='+str(i))
    mapBox.append(shash)
    #print(mapBox[i])

#load trimming - undifined.png
undBox = []
for i in range(8):
    ssPath = r'C:\Users\50811073\Dropbox\Programming\myAppByPy\ゼルメアライター\check\sShotPng\trimmed\undifined'+ '\\'+str(i) +'.png'
    shash = ihash.average_hash(Image.open(ssPath))
    #print('i='+str(i))
    undBox.append(shash)
    #print(mapBox[i])

print('len(imgBox=)'+str(len(imgBox)))
print('len(mapBox=)'+str(len(mapBox)))
print('len(undBox=)'+str(len(undBox)))

for map in range(12):
    print('-------------------map['+str(map)+']')
    for img in range(2,23):
        if(int(mapBox[map]-imgBox[img]) < 22):
            print('----------save')
        print('img['+str(img)+']='+str(mapBox[map]-imgBox[img]))

for und in range(8):
    print('-------------undifined['+str(und)+']')
    for img in range(2,23):
        print('img['+str(img)+']='+str(undBox[und]-imgBox[img]))


print('#success- comparison.py')