# coding=utf-8
import scipy.io as sio
from skimage import io
import os
import cPickle
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def LoadAllFiles(path):
    allFiles=[]
    for tempFile in os.listdir(path):
        # print(tempFile)
        tempFile=path+"\\"+tempFile
        allFiles.append(tempFile)
    return allFiles

def ConvertMatFileSaveAsPng(matFile,savePath=r"D:\JackGu\DataSet\benchmark\ConvertSBD"):
    matData=sio.loadmat(matFile)
    GTcls=matData["GTcls"]
    Segmentation=GTcls["Segmentation"]
    val=Segmentation[0,0]
    temp=matFile.split(".")[0]
    temp=temp[-11:]
    # print(temp)
    dstFile=savePath+"\\"+temp+".png"
    # print(dstFile)
    io.imsave(dstFile,val)

def ConvertMatFileSaveAsPngWithBoundary(matFile,savePath):
    tempList=[]
    tempBoundaries=[]
    matData=sio.loadmat(matFile)
    GTcls=matData["GTcls"]
    Segmentation=GTcls["Segmentation"]
    valS=Segmentation[0,0]
    Boundaries=GTcls["Boundaries"]
    valB=Boundaries[0,0]
    for i in range(1,21):
        if i in valS:
            tempList.append(i)
    for j in tempList:
        valB = valB[j-1][0]*255
        tempBoundaries.append(valB)
    for k in range(0,len(tempBoundaries)):
        valS=valS+tempBoundaries[k]
    # plt.imshow(valS)
    # plt.show()
    temp = matFile.split(".")[0]
    temp = temp[-11:]
    # print(temp)
    dstFile = savePath + "\\" + temp + ".png"
    # print(dstFile)
    io.imsave(dstFile, valS)

def ConvertPngWithColorMap(pngFile,cmapFilePath):
    with open(cmapFilePath) as f:
        cmap=cPickle.load(f)
    img=Image.open(pngFile)
    if cmap is not None:
        img.putpalette(cmap.ravel())
        img.save(pngFile)



def main():
    # filePath=r"D:\JackGu\DataSet\benchmark\dataset\cls"
    filePath=r"D:\JackGu\DataSet\benchmark\test"
    cmapFilePath=r"D:\JackGu\PyCharm\SBD\cmap.pkl"
    # savePath=r"D:\JackGu\DataSet\benchmark\ConvertSBD"
    savePath=r"D:\JackGu\DataSet\benchmark\testpng"
    allFiles=LoadAllFiles(savePath)
    # print(allFiles)
    for tempFile in allFiles:
        print(tempFile)
        # ConvertMatFileSaveAsPngWithBoundary(tempFile,savePath)
        # ConvertPngWithColorMap(tempFile,cmapFilePath)

if __name__=="__main__":
    main()












