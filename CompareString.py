# coding=utf-8

import os


def LoadTxtFile(fileName):
    myList=[]
    myReader=open(fileName,'r')
    for eachline in myReader:
        myList.append(eachline)
    myReader.close()
    # print(myList)
    # print(len(myList))
    return myList

def WriteTxtFile(fileName,lineList):
    # if os.path.exists(fileName):
    #     print("%s already exists!\n")
    #     return False
    myWriter=open(fileName,'w')
    for eachline in lineList:
        myWriter.writelines(eachline)
    myWriter.close()
    return True

def CompareString(valList,trainList):
    for k in range(0,len(valList)):
        valList[k]=valList[k].strip()
    for i in valList:
        for j in trainList:
            if i in j:
                trainList.remove(j)
    # print(trainList)
    # print(len(trainList))
    return trainList

def ExtractString(valList):
    for k in range(0,len(valList)):
        valList[k]=valList[k].split(".jpg")[0]
        valList[k]=valList[k][-11:]+"\n"
    return valList

def AddString(myList):
    newList=[]
    for i in range(0,len(myList)):
        myList[i]=myList[i].strip()  # not .split() => type:list
    for j in range(0,len(myList)):
        # print(myList[j])
        # print(type(myList[i]))
        preLabel="VOC2012/JPEGImages/"+myList[j]+".jpg"
        postLabel="VOC2012/SegmentationClass/"+myList[j]+".png"
        newList.append(preLabel+"\t"+postLabel+"\n")
    return newList

def test():
    savePath = r"D:\JackGu\DataSet\benchmark\SBD\result.txt"
    valList = LoadTxtFile(r"D:\JackGu\DataSet\benchmark\SBD\SBDval.lst")
    # trainList = LoadTxtFile(r"D:\JackGu\DataSet\benchmark\SBD\trainsbd.lst")
    result = ExtractString(valList)
    WriteTxtFile(savePath, result)


def main():
    savePath=r"D:\JackGu\DataSet\benchmark\SBD\result.txt"
    valList=LoadTxtFile(r"D:\JackGu\DataSet\benchmark\SBD\VOCtrain.txt")
    trainList=LoadTxtFile(r"D:\JackGu\DataSet\benchmark\SBD\SBD_NoVal.lst")
    result=CompareString(valList,trainList)
    WriteTxtFile(savePath,result)
    # ####################################################################
    # txtPath=r"D:\JackGu\DataSet\benchmark\SBD\PureVal.txt"
    # myList=LoadTxtFile(txtPath)
    # newList=AddString(myList)
    # WriteTxtFile(savePath,newList)

if __name__=="__main__":
    main()
    # test()















