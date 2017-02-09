from PIL import Image

Pics = []
GreenP = []
BlueP = []
RedP = []

Pics.append(Image.open("ana-project1/Ana/1."))
Pics.append(Image.open("ana-project1/Ana/2.png"))
Pics.append(Image.open("ana-project1/Ana/3.png"))
Pics.append(Image.open("ana-project1/Ana/4.png"))
Pics.append(Image.open("ana-project1/Ana/5.png"))
Pics.append(Image.open("ana-project1/Ana/6.png"))
Pics.append(Image.open("ana-project1/Ana/7.png"))
Pics.append(Image.open("ana-project1/Ana/8.png"))
Pics.append(Image.open("ana-project1/Ana/9.png"))

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
            
            
        FinalImage.putpixal((x,y),(NewRed, NewGreen, NewBlue))
        GreenP= []
        BlueP = []
        RedP = []
        
        
FinalImage.show()