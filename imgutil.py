import requests
import urllib.request
import os
from PIL import Image
def gethtml():
   htmlsource="htmlcontainer.txt"
   fhand=open(htmlsource,"w+")
   target=input("enter a word ")
   size=int(input("enter number of images(should be multiple of 20) : "))
   si=int(size)
   s=str(si/20)
   for i in range(s):
      sii=str(si)
      prelink='https://www.google.com/search?q='+target+'&rlz=1C1CHBF_enIN921IN921&sxsrf=ALiCzsbYqN1K3KDUBz0Fw3uc6FwdGDIWZQ:1654625709598&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjImaCN-Zv4AhXMDd4KHWVsBW4Q_AUoAXoECAIQAw&biw=1280&bih=648&start='+sii+'&dpr=1.5&sfr=gws&gbv=1&sei=DJafYpbeHrCMg8UPyPmV6A8'
      r=requests.get(prelink)
      fhand.write(r.text)
      si-=20
   return htmlsource


def create_img_links(source):
   import re
   fhand=open(source,"r+")
   imgsource="imglist.txt"
   fhan=open(imgsource,'w+')
   ilst1=[]
   for line in fhand:
      line=line.rstrip()
      words=line.split()
   for j in range(len(words)):
      if words[j] == 'class=\"yWs4tf\"':
         ilst1.append(words[j+2])
   for line in ilst1:
      line=line.lstrip("src=\"")
      line=line.rstrip(";s\"/></div></a></td></tr><tr><td><a")
      fhan.write(line+'\n')
   return imgsource


def save_image(source):
   fhand=open(source,'r+')
   name=input("enter the name of the file ")
   fi=os.makedirs(name)
   count=0
   lis=[]
   for line in fhand:
      lis.append(line)
   os.chdir('./'+name)
   for link in lis:
      imgname=name+(str(count)+'.jpeg')
      urllib.request.urlretrieve(link,imgname)
      img = Image.open(imgname)
      count+=1
   


if __name__=="__main__":
   html_text=gethtml()
   imgsource=create_img_links(html_text)
   save_image(imgsource)

      
       

            
            

