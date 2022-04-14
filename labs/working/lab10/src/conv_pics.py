from PIL import Image, ImageOps
import numpy

shoeOG = Image.open("shoe.jpg")
bagOG = Image.open("bag.jpg")
shirtOG = Image.open("shirt.jpg")

shoeInv = ImageOps.invert(shoeOG)
bagInv = ImageOps.invert(bagOG)
shirtInv = ImageOps.invert(shirtOG)

shoeResize = shoeInv.resize((28, 28))
bagResize = bagInv.resize((28, 28))
shirtResize = shirtInv.resize((28, 28))

shoeGS = shoeResize.convert(mode='L')
bagGS = bagResize.convert(mode='L')
shirtGS = shirtResize.convert(mode='L')


shoe_np = numpy.array(shoe)
bag_np = numpy.array(bag)
shirt_np = numpy.array(shirt)		
