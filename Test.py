# coding=utf-8
import scipy.io as sio
from skimage import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# matData=sio.loadmat(r"D:\JackGu\DataSet\benchmark\2008_000033.mat")
# print(type(matData))
#print(matData)
#print(matData.keys())
#print(type(matData["GTcls"]))
# GTcls=matData["GTcls"]
# print(GTcls)
# print(GTcls.shape)
# Segmentation=GTcls["Segmentation"]
# print(Segmentation)
# print(Segmentation.shape)
# val=Segmentation[0,0]
# print(val)

# print(type(Segmentation))
# plt.imshow(val)
# plt.show()

#io.imsave(r"D:\JackGu\DataSet\benchmark\1.png",val)


# pngImg=io.imread(r"D:\JackGu\DataSet\benchmark\2008_000033.png")
# print(type(pngImg))
# #print(pngImg)
# print(pngImg.max())
# pngData=pngImg.shape

# pngImg=Image.open(r"D:\JackGu\DataSet\benchmark\ConvertSBD\2008_000002.png")
# img=np.array(pngImg,np.uint8)
# print(img)


# temp=r"D:\JackGu\DataSet\benchmark\2008_000033.mat"
# dstFile=temp.split(".")[0]+".png"
# dstFile1=temp.split(".")[0]
# dstFile1=dstFile1[-11:-1]
# print(dstFile1)

# testImg=io.imread(r"D:\JackGu\DataSet\benchmark\SBD\ConvertSBD\2008_000043.png")
# plt.imshow(testImg)
# plt.show()

# matData=sio.loadmat(r"D:\JackGu\DataSet\benchmark\2008_000002.mat")
# GTcls=matData["GTcls"]
# Segmentation=GTcls["Segmentation"]
# valS=Segmentation[0,0]
# # print(valS)
# Boundaries=GTcls["Boundaries"]
# # print(Boundaries)
# # print(Boundaries.shape)
# valB=Boundaries[0,0]
# valB=valB[19][0]
# # print(valB)
# valB=valB*255
# val=valB+valS
# print(valB.shape)
# plt.imshow(val)
# plt.show()






