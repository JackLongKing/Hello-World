# coding=utf-8
import os

def WriteLabels(txtPath,filePath):
    f=open(txtPath,'a')
    for tempImg in os.listdir(filePath):
        f.write(tempImg+"\n")
    f.close()
    return 1

def WriteLabelsSpecial(txtPath,filePath):
    f=open(txtPath,'w')
    for tempImg in os.listdir(filePath):
        preLabel="../sbd/images/"+tempImg.split(".")[0]+".jpg"
        postLabel="../sbd/anns/"+tempImg
        f.write(preLabel+"\t"+postLabel+"\n")
    f.close()
    return 1


def main():
    WriteLabelsSpecial(r"D:\JackGu\DataSet\benchmark\PureValLabels.txt",r"D:\JackGu\DataSet\benchmark\ConvertSBD")

if __name__=="__main__":
    main()