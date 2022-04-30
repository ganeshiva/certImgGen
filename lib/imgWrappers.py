# Image Wrappers

from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageColor
import inspect
import sys

def openImageObject(imageFilename):
    imageFile = None
    try:
        imageFile = Image.open(imageFilename)
    except Exception as e:
        print( "Unable to Process file: " + str(imageFilename))
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        sys.exit(-1)
    return imageFile
    
def reSizeImage(imageFile,width,height):
    imageFile = imageFile.resize((width, height), Image.ANTIALIAS)
    return imageFile

def setFont(fontFile,size):
	font = ImageFont.truetype(fontFile, size)
	return font

def getImageColor(colorName):
    return ImageColor.getrgb(colorName)

def createText(text,fontFile,fontSize,fill):
    font = setFont(fontFile, fontSize)
    fontXDim, fontYDim = font.getsize(text)
    txt=Image.new('L', (fontXDim,fontYDim))
    txtImg = ImageDraw.Draw(txt)
    txtImg.text( (0, 0),text,font=font,fill=fill)
    rotatedTxtImg=txt.rotate(0,  expand=1)
    return rotatedTxtImg

def overLayText(imageFile, imgText, text,txtColor, position):
    xPosition, yPosition = position
    imageFile.paste( ImageOps.colorize(imgText, (0,0,0), txtColor), (xPosition, yPosition), imgText)
    return imageFile

def imageResize(imgFile,basewidth=350):
    img = Image.open(imgFile)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    return img


def imageThumbnail(imgFile,size=(120,120)):
    img = Image.open(imgFile)
    img = img.thumbnail(size)
    return img