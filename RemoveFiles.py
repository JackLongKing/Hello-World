# coding=utf-8
import os

def LoadTxtFile(txtFilePath):
    myList=[]
    myReader=open(txtFilePath,'r')
    for eachline in myReader:
        myList.append(eachline)
    myReader.close()
    return myList

def WriteImgLabel(imgPath):
    imgList=[]
    for tempImg in os.listdir(imgPath):
        imgList.append(imgPath+"\\"+tempImg)
    return imgList

def CompareString(valStr,imgStr):
    if valStr in imgStr:
        return True
    else:
        return False

def JudgeRemove(valList,imgList):
    for i in range(0,len(valList)):
        for j in range(0,len(imgList)):
            if CompareString(valList[i],imgList[j]):
                os.remove(imgList[i])



def main():
    imgPath=r"D:\JackGu\Test\img"
    txtFilePath=r"D:\JackGu\Test\PureVal.txt"
    valList=LoadTxtFile(txtFilePath)
    imgList=WriteImgLabel(imgPath)
    JudgeRemove(valList,imgList)


if __name__=="__main__":
    main()