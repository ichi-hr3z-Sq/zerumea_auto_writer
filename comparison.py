#取得したスクリーンショットを分割して、決められた画像と比較
#類似度を計算し、対応する値を返す
#sShot comparison
#trimming 3*4 + 4*2 = 20pics & comparison


#-----------------------------------------------------------#


#取得するスクリーンショットは、sShot.pyによって[sShot.png]と名づけられている
#File name = sShot.png (named by- sShot.py)
from PIL import Image
im = Image.open("スクリーンショットのPath")

#撮ったスクリーンショットの大きさを補正する。
#デフォルトの画像サイズは[1280*720]で描かれている
#[1920*1080]のサイズでスクショした場合、[1280*720]と比べて1.5倍なので、cMog=1.5とする
#change capcher size [1280*720] to [1920*1080] = magnification 1.5
cMag=1.5

#マップ部分を3*4 = 12枚の画像に分割する
#map trimmng by 3*4
i = 0
for row in range(4):
    for column in range(3):
        move = [86.5*column*cMag, 86.5*row*cMag]
        span = 40*cMag
        sXY = [98*cMag, 264*cMag]
        nXY = [sXY[0]+move[0], sXY[1]+move[1]]
        box = (nXY[0]-span, nXY[1]-span, nXY[0]+span, nXY[1]+span)
        #トリミングした画像に0~11の番号を付けて.png形式で保存する
        savePath = "トリミングした画像を保存するファイルのpath" +'\\'+ str(i)+ '.png'
        i += 1
        im.crop(box).save(savePath)

#未探索ヒント部分を4*2 = 8枚の画像に分割する
#undifined trimmig by 4*2
i = 0
for row in range(2):
    for column in range(4):
        move = [48*column*cMag, 39*row*cMag]
        box = (84*cMag+move[0],572*cMag+move[1], 132*cMag+move[0],620*cMag+move[1])
        #トリミングした画像に0~7の番号を付けて.png形式で保存する
        savePath = "トリミングした画像を保存するファイルのpath" +'\\'+ str(i)+ '.png'
        i += 1
        im.crop(box).save(savePath)


#-----------------------------------------------------#

#画像の比較部分
#imagehashで点数をつけ、比較する
#類似度が閾値を超えたらアクションを起こす
# （本来なら一致した画像に対応する値を返す）
#comparison body
#import ImageHash - for comparison
from PIL import Image
import imagehash as ihash

#比較元となる画像のhashデータをimgBox[]に保存する
#比較元の画像は23枚あり、それぞれ0~22の番号が充てられていたので、range23、str(img)を用いて指定している
#comparison reference map
imgBox = []
for img in range(23):
    imgPath = "比較元となる画像のpath"+'\\'+str(img)+'.png'
    #print(imgPath)
    ohash = ihash.average_hash(Image.open(imgPath))
    imgBox.append(ohash)
    #print(imgBox[img])

#先に保存したマップ情報のhashデータをmapBox[]に保存する
#load trimming - map.png
mapBox = []
for i in range(12):
    ssPath = "先ほどトリミングしたマップ情報0~11のpath"+ '\\'+str(i) +'.png'
    shash = ihash.average_hash(Image.open(ssPath))
    #print('i='+str(i))
    mapBox.append(shash)
    #print(mapBox[i])

#同様に未探索画像0~7についてもhashを保存
#load trimming - undifined.png
undBox = []
for i in range(8):
    ssPath = "先ほどトリミングした未探索画像0~7のpath"+ '\\'+str(i) +'.png'
    shash = ihash.average_hash(Image.open(ssPath))
    #print('i='+str(i))
    undBox.append(shash)
    #print(mapBox[i])

#保存したデータの数が正常かチェック
print('len(imgBox=)'+str(len(imgBox)))
print('len(mapBox=)'+str(len(mapBox)))
print('len(undBox=)'+str(len(undBox)))

#printで要所に区切りを入れつつ、0~11の各マップデータと比較データ23個を比較
for map in range(12):
    #map.pngのカウント
    print('-------------------map['+str(map)+']')
    for img in range(2,23):
        #比較の結果、比較値が22を下回る（似ている）なら----saveで区切る
        if(int(mapBox[map]-imgBox[img]) < 22):
            print('----------save')
        print('img['+str(img)+']='+str(mapBox[map]-imgBox[img]))

#上記の未探索部分ver.
for und in range(8):
    print('-------------undifined['+str(und)+']')
    for img in range(2,23):
        print('img['+str(img)+']='+str(undBox[und]-imgBox[img]))

#動作の終了を宣言
#print('#success- comparison.py')