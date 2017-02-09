from PIL import Image
#import os
#import os.getenv('PORT','8080')
#import os.getenv('IP','0.0.0.0')

Pics = []
GreenP = []
BlueP = []
RedP = []

Pics.append(Image.open("/home/ubuntu/workspace/Ana/1.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/2.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/3.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/4.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/5.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/6.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/7.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/8.png"))
Pics.append(Image.open("/home/ubuntu/workspace/Ana/9.png"))

width,height= Pics[0].size

FinalImage= Image.new("RGB", (width, height), "white")

def median(thelist):
    sorted_list = sorted(thelist)
    length = len(sorted_list)
    center = length // 2

    if length == 1:
        return sorted_list[0]

    elif length % 2 == 0:
        return sum(sorted_list[center - 1: center + 1]) / 2.0

    else:
        return sorted_list[center]

for x in range (0,width):
    for y in range (0, height):
        for z in Pics:
            
            Red, Green, Blue = z.getpixel((x,y))
            
            GreenP.append(Green)
            BlueP.append(Blue)
            RedP.append(Red)
            
        NewGreen= median(GreenP)
        NewBlue = median(BlueP)
        NewRed = median (RedP)
            
            
        FinalImage.putpixel((x,y),(NewRed, NewGreen, NewBlue))
        GreenP= []
        BlueP = []
        RedP = []
        
        
FinalImage.save("/home/ubuntu/workspace/Ana/final.png")