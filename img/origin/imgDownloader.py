#imgDownloader

import requests

url = 'https://miakoron.net/zerumea/image/'
for i in range(0,23):
    r = requests.get(url+str(i)+'.png', stream=True)

    path = r'C:\Users\50811073\Dropbox\Programming\my app by py\ゼルメアライター\img'
    with open(path +'\\'+str(i)+ '.jpg','wb')as f:
        f.write(r.content)