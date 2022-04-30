#!/usr/bin/python3

codeHeader='''
#################################################################
title="Certificate Image Generator"
summary="Read Excel File for list of fields and Generate Image(Certificate) with respective fields using image overlay"
author=Ganeshiva
created=20220430
updated=20220430
cmdLine="python3 <thisScriptName> <configFile>"
dependancy="refer requirement.txt"
repository="https://github.com/ganeshiva/certImgGen"
license="(c)ganeshiva - freeToUse@yourOwnRisk - no Guaranty, check license info from dependancy lib"
#################################################################
'''

print(codeHeader)

import sys
sys.path.append("lib")

import os
import yaml
import glob, os
import pandas as pd 
import inspect

from copy import deepcopy
from imgWrappers import createText
from imgWrappers import overLayText
from imgWrappers import openImageObject

if __name__ == '__main__':

    argument = sys.argv
    print("Input Argument(s): " + str(argument))
    
    if len(argument) == 2 :
        # Strip \n \r Characters in the Command line
        argument = [str(i).strip("\r\n") for i in argument]
        configFile = argument[1]
        
        try:
            with open(configFile, "r", encoding='utf8') as ymlFile:
                print("Reading Config File: " + str(configFile))
                ymlConfig = yaml.safe_load(ymlFile)
        except Exception as e:
            print( "Unable to Process file: " + str(configFile))
            print( inspect.stack()[0][3] + " Exception: " + str(e))
            sys.exit(-1)
            
        imageTemplateFileName = str(ymlConfig['templateImageFile'])
        outputPath = ymlConfig['outputDirectory']
        nameListFile= ymlConfig['CertificateParameters']['inputExcelFile']
        
        df = pd.read_excel(nameListFile)
        
        imageFile = openImageObject(imageTemplateFileName)
        xDim, yDim = imageFile.size
        print("Reading Template Image: " + str(imageTemplateFileName) + " , with x*y Dimension: " + str(xDim) + "*" + str(yDim))
        
        outputPath = outputPath + os.sep 
        
        for index, row in df.iterrows():
            fileName = ""
            newImageFile = deepcopy(imageFile)
            for field in ymlConfig['CertificateParameters']['excelField']:
                try:
                    # Name of the Excel Column
                    name = str(field['name'])
                    # Attributes of the excel field 
                    xPosition = field['xPosition']
                    yPosition = field['yPosition']
                    fontFile = field['font']
                    fontSize = field['fontSize']
                    fontColor = field['fontColor']
                    txtPrefix = field['txtPrefix']
                    txtSuffix = field['txtSuffix']
                    txtValue = str(row[name]).strip()
                except Exception as e:
                    print( "Unable to Process field : " + str(name))
                    print( inspect.stack()[0][3] + " Exception: " + str(e))
                    sys.exit(-1)
                # Text Value of the Excel Column [name]
                txt = txtPrefix + txtValue + txtSuffix
                # Creating Text Object based on the size, font, color attributes
                textImg = createText(txt,fontFile,fontSize,255)
                textXDim, txtYDim = textImg.size
                # Positioning the text with center alignment 
                txtXPosition = xPosition - int(textXDim/2)
                txtYPosition = yPosition - int(txtYDim/2)
                
                if txtXPosition + textXDim > xDim or txtXPosition + textXDim < 0:
                    print("Change 'xPosition' value for " + name  + " , it exceeds image size")
                    sys.exit(-1)
                if txtYPosition + txtYDim > yDim  or txtYPosition + txtYDim < 0 :
                    print("Change 'yPosition' value for " + name  + " , it exceeds image size")
                    sys.exit(-1)
                    
                position = (txtXPosition, txtYPosition)
                newImageFile = overLayText(newImageFile,textImg, txt, fontColor, position)
                # Generating File name based on the field value
                fileName = fileName + "_" + txtValue

            # Generating file name only with first 120 characters
            imageFileName = fileName.strip("_")[:120] + ".jpg"
            
            filePath = outputPath+imageFileName
            
            try:
                # Converting Image into RGB, say if it is PNG they can be other Transperancy layer
                rgb_im = newImageFile.convert('RGB')
                # Saving the file 
                rgb_im.save(filePath)
            except Exception as e:
                print( "Unable to Process file: " + str(filePath))
                print( inspect.stack()[0][3] + " Exception: " + str(e))
            print("File Generated: '" + str(filePath) + "'")
            
        print(" The End of Program !")
        sys.exit(0)
    else:
        print("Supported Arguments: 1. <configFile.yml>")
                