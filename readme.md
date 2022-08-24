# 用python实现的常用数学变换

## 介绍

一些作业题中使用到的数学变换，由于手工计算过于复杂且难以保证正确率。使用MATLAB虽然有封装好的函数但是懒得装。为了节约手算的时间和精力以及安装MATLAB所需的20GB空间，使用python NumPy实现了部分常用的数学变换。

## 使用方法

### 环境准备

仅需要使用anaconda执行下方命令即可

`conda env create -f environment.yaml`

### 运行

`python cal.py [c] [d]`

使用算法替代[c]，使用矩阵维数替代[d]

例如，执行二维DCT可用下方命令完成：

`python cal.py two_d_dct 2`

## 目前支持的算法

二维离散余弦变换

...

