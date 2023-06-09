
for i in range(1000):
    img1=input("What is the pathway to the first image? ")
    img2=input("What is the pathway to the second image? ")

    img1=img1.replace("\\","/")
    img2=img2.replace("\\","/")
    img1=img1.replace('"',"'")
    img2=img2.replace('"',"'")

    #read images
    print(img1)
    print(img2)
    decesion=input("Do you want to keep this tab open? (Y/N)")
    if(decesion=='Y'):
        continue
    else:
        break
    
