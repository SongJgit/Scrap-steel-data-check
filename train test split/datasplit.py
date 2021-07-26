
import os
import shutil
import argparse
from tqdm import tqdm 
import random

# 划分为验证集与训练集2:8比例
# 两个参数src和tar必须给出
# src为存放等待划分的数据集的文件夹 默认内部存放格式filename/images、filename/labels
# tar为存放划分结果的文件夹 默认结果filename/images、filename/labels
# 仅需要给出文件夹的名称
#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   datasplit.py
@Time    :   2021/05/09 11:18:31
@Author  :   SongJ
@Version :   1.0
@Contact :   songj95@outlook.com
'''

def imgdatasplit(src,tar):
    rootfile_list = os.listdir(src)
    length = len(rootfile_list)
    num_train = int(length * 0.8)
    random.shuffle(rootfile_list)
    print('正在划分图片数据集')
    for train in tqdm(rootfile_list[:num_train]):
        shutil.move(os.path.join(src,train),os.path.join(tar,'train'))
    for val in tqdm(rootfile_list[num_train:]):
        shutil.move(os.path.join(src,val),os.path.join(tar,'val'))


def txtdatasplit(src,tar,img):    
    # src：源，tar：目标，img：训练集的图片，确保标签数量与名称对齐
    # 获取train对应的图片名称，然后从标签文件里面提取对应的txt文件
    # val重复上述工作
    print('正在划分标签数据集')
    img_train_file_list = os.listdir(os.path.join(img,'train')) 
    for fi in tqdm(img_train_file_list):
        sep = os.path.splitext(fi)
        txt = sep[0]+'.txt'
        shutil.move(os.path.join(src,txt),os.path.join(tar,'train'))
    img_val_file_list = os.listdir(os.path.join(img,'val'))
    for fi in tqdm(img_val_file_list):
        sep = os.path.splitext(fi)
        txt = sep[0]+'.txt'
        shutil.move(os.path.join(src,txt),os.path.join(tar,'val'))

def main():
    if not os.path.exists(os.path.join(args.tarimg,'train')):
        # 如果目标的images和lables不存在则创建
        print('正在创建目标文件夹')
        os.makedirs(os.path.join(args.tarimg,'train'))
        os.makedirs(os.path.join(args.tarimg,'val'))
        os.makedirs(os.path.join(args.tarlab,'train'))
        os.makedirs(os.path.join(args.tarlab,'val'))
        print('目标文件夹创建完毕')
    #imgdatasplit('img','images') 
    # 先划分图片，然后根据图片的训练集划分label
    imgdatasplit(args.srcimg, args.tarimg)
    txtdatasplit(args.srclab,args.tarlab,args.tarimg) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--src', default=' ', type=str, help='img source directory')
    parser.add_argument('--tar', default=' ', type=str, help='img targets directory')
    args = parser.parse_args()

    args.srcimg = os.path.join(args.src,'images')
    args.srclab = os.path.join(args.src,'labels')

    args.tarimg = os.path.join(args.tar,'images')
    args.tarlab = os.path.join(args.tar,'labels')
    if args.src == ' ':
        print('未指定src参数')
    
    print(args)
    
    main()