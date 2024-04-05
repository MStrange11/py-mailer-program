import os

print()
for img in os.listdir("img"):
    print(img)
print()

img_name = ["img/"+input("enter image file name: ")]
print(img_name)