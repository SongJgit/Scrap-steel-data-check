import pandas as pd
import os
'''
对收上来的数据进行检查
'''

#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   measurecheack.py
@Time    :   2021/05/09 11:21:18
@Author  :   SongJ
@Version :   1.0
@Contact :   songj95@outlook.com
'''




def checklength(path):
    '''检查每个labels和images是否对齐'''
    print('正在检查labels与images数量是否相同\n')
    print('正数:img多于labels；负数:labels多于img')

    img_file_list = os.listdir(os.path.join(path,'images'))
    txt_file_list = os.listdir(os.path.join(path,'labels'))
    if len(img_file_list)==len(txt_file_list):
        pass
    else:
        print('images与labels数量不一致,缺失的数量为{}'.format(len(img_file_list)-len(txt_file_list)))
    print('\n数量检查完毕')


def checkxml(path):
    #检查是否有错误保存为txt的,找出来并删除
    print('正在检查labels内是否有错误的txt格式\n')
    
    img_file_list = os.listdir(os.path.join(path,'images'))
    txt_file_list = os.listdir(os.path.join(path,'labels'))
    for txt_fi in txt_file_list:
        sep = os.path.splitext(txt_fi)
        if sep[1] == ".txt":
            os.remove(os.path.join(path,i,'labels',txt_fi))
            print('{}已删除'.format(os.path.join(path,i,'labels',txt_fi)))
    print('\nlabels格式检查完毕')


def checkname(path):
    # 检查每个labels和images名称是否对应
    print('正在检查labels与images命名是否匹配\n')
    img_file_list = os.listdir(os.path.join(path,'images'))
    txt_file_list = os.listdir(os.path.join(path,'labels'))
    F = True
    jpg_list = []
    xml_list = []

    for fi in img_file_list:
        sep = os.path.splitext(fi)
        jpg_list.append(int(sep[0]))
    for fi1 in txt_file_list:
        sep1 = os.path.splitext(fi1)
        xml_list.append(int(sep1[0]))

    for img in jpg_list:
        if img in xml_list:
            pass
        else:
            print('labels缺少数据：{}.xml'.format(img))
    for xml in xml_list:
        if xml in jpg_list:
            pass
        else:
            print('images中缺少数据：{}.jpg'.format(xml))
    print('\n命名检查完毕')
                


if __name__ == '__main__':
    path = 'measuredata'
    print('\n-----------------\n')
    # 检查报表列是否合格
    #checktable(path)

    # 检查labels和xml数量是否一致，即是否有漏标
    print('\n-----------------\n')
    checklength(path)

    # 检查是否有错误保存为txt，找出来并删除
    print('\n-----------------\n')
    checkxml(path)

    # 检查名称是否正确
    print('\n-----------------\n')
    checkname(path)

    print('\n-----------------\n')
    print('全部检查完成')