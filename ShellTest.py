# coding=utf-8

import os

def LoadTxtFile(txtFilePath):
    txtList=[]
    myReader=open(txtFilePath,'r')
    for eachline in myReader:
        txtList.append(eachline)
    myReader.close()
    return txtList

def AddStringToTxtFile(txtFilePath,target):
    myWriter=open(txtFilePath,'a')
    myWriter.write(target+"\n")
    myWriter.close()
    return True

def GetFileContentList(contentPath):
    contentFileList=[]
    if os.path.isdir(contentPath):
        for tempFile in os.listdir(contentPath):
            if os.path.isfile(contentPath+"\\"+tempFile):
                contentFileList.append(tempFile)
    return contentFileList


def CompareString(fileList,txtList):
    target=None
    for i in range(0,len(fileList)):
        if fileList[i] in txtList:
            continue
        else:
            target=fileList[i]
    return target

def WriteFileLabels(contentPath,saveFilePath):
    if os.path.isdir(contentPath):
        fileList=GetFileContentList(contentPath)
        myWriter=open(saveFilePath,"w")
        for i in range(len(fileList)):
            myWriter.write(fileList[i]+"\n")
        myWriter.close()
        return True
    return False

def ModifyBashFile(bashFilePath,modelName):
    if os.path.isfile(bashFilePath):
        f=open(bashFilePath,'r+')
        allText=f.read()
        post=allText.split("params")[1]
        pre=allText.split("voc_rna")[0]
        fullName=pre+modelName+post
        f.write(fullName)
        f.close()

def ExecFile(filePath):
    exec(filePath)

def Test():
    # basePath = "/data/bo718.wang/ziyuan.guo/segment/ademxapp-master/output/0715/fixed_lr/val"
    basePath=r"D:\JackGu\Test"
    txtFilePath=basePath+"\\fileTxt.txt"
    contentPath=basePath+"\\img"
    bashFilePath="/data/bo718.wang/ziyuan.guo/segment/ademxapp-master/issegm/gzy_val.sh"
    txtList=LoadTxtFile(txtFilePath)
    # print(len(txtList))
    contentFileList=GetFileContentList(contentPath)
    # print(len(contentFileList))
    modelName=CompareString(contentFileList,txtList)
    # print(modelName)
    if modelName is not None:
        # ModifyBashFile(bashFilePath, modelName)
        AddStringToTxtFile(txtFilePath, modelName)
        # ExecFile(bashFilePath)

def InitTest():
    basePath="D:\\JackGu\\Test"
    contentPath=basePath+"\\img"
    saveFilePath=basePath+"\\fileTxt.txt"
    result=WriteFileLabels(contentPath,saveFilePath)

if __name__=="__main__":
    InitTest()
    # Test()
