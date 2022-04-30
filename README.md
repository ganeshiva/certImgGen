# Certificate Image Generator
Certificate Image Generator - Generate Images based on excel file fields

## Summary

Read Excel File for list of fields and Generate Image(Certificate) with respective fields using image overlay

## Dependancy

Language: install python3+
Follow https://www.python.org/downloads/

Library: Refer requirements.txt

```
pip3 install -r requirements.txt
```
## Input

'input/CertificateInputList.xls' - Input Excel file with name or attributes List 

Enter Fields parameters of  xls file in 'config/config.yml'

Text Attributes will be generated based on the size, font, color attributes provided in 'config/config.yml'

## Output
```
output/*.jpg
```
Generated Certificate jpg files will be available in 'output' directory

## Run 
```
generateCert.sh (UNIX/LINUX)
generateCert.bat (Windows)
```
After configurations are completed in 'config/config.yml' , start generatCert.sh or generateCert.bat based on your Operating System
