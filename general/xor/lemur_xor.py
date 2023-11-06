from PIL import Image, ImageChops
# Po co ta libka?
# plik PNG nie dosc ze jest skompresowany, to jeszcze posiada naglowek oraz sume kontrolna
# domyslam sie, ze operacje xor trzeba bedzie wykonac na raw data obrazka, dlatego potrzebna jest libka, ktora umie to wyciągnąć
def lemur_xor():
    im1 = Image.open("general/xor/lemur.png", mode="r")
    im2 = Image.open("general/xor/flag.png", mode="r")

    final = ImageChops.difference(im1,im2)

    final.save("general/xor/final.png")