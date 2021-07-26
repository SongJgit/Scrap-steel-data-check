import pandas as pd
import os
'''
对收上来的数据进行检查
'''

#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   check.py
@Time    :   2021/05/09 11:20:02
@Author  :   SongJ
@Version :   1.0
@Contact :   songj95@outlook.com
'''


def checktable(path):
    '''
    检查table数据
    path:文件夹的路径,path中的文件夹要求,root_path/0001/0001.txt,root_path/0002/0002.txt....
    return:合格与不合格数据的list
    '''
    print('正在检查报表txt列数是否正确\n')
    file_list = os.listdir(path)
    qualified = []
    Unqualified = []
    for i in file_list:
        df = pd.DataFrame()
        try:
            df = pd.read_csv(os.path.join(path,i,i)+'.txt' ,header = None,dtype=float)
        except:
            print('{}存在空数据'.format(i))
        if df.shape[1] == 14 or df.shape[1]== 11:
            qualified.append([i+'.txt'])
        else:
            Unqualified.append([i+'.txt'])
            print("{},数据尺寸为:{}".format(i+'.txt',df.shape))
    print('\n报表检查完毕')
    return qualified,Unqualified


def checklength(path):
    '''检查每个labels和images是否对齐'''
    print('正在检查labels与images数量是否相同\n')
    print('正数:img多于labels；负数:labels多于img')
    rootfile_list = os.listdir(path)
    for i in rootfile_list:
        img_file_list = os.listdir(os.path.join(path,i,'images'))
        txt_file_list = os.listdir(os.path.join(path,i,'labels'))
        if len(img_file_list)==len(txt_file_list):
            pass
        else:
            print('{}images与labels数量不一致,缺失的数量为{}'.format(i,len(img_file_list)-len(txt_file_list)))
    print('\n数量检查完毕')


def checkxml(path):
    #检查是否有错误保存为txt的,找出来并删除
    print('正在检查labels内是否有错误的txt格式\n')
    rootfile_list = os.listdir(path)
    for i in rootfile_list:
        img_file_list = os.listdir(os.path.join(path,i,'images'))
        txt_file_list = os.listdir(os.path.join(path,i,'labels'))
        for txt_fi in txt_file_list:
            sep = os.path.splitext(txt_fi)
            if sep[1] == ".txt":
                os.remove(os.path.join(path,i,'labels',txt_fi))
                print('{}已删除'.format(os.path.join(path,i,'labels',txt_fi)))
    print('\nlabels格式检查完毕')


def checkname(path):
    # 检查每个labels和images名称是否对应
    print('正在检查labels与images命名是否匹配\n')
    rootfile_list = os.listdir(path)
    for i in rootfile_list:
        F = True
        img_file_list = os.listdir(os.path.join(path,i,'images'))
        txt_file_list = os.listdir(os.path.join(path,i,'labels'))
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
                print('{}的labels缺少数据：{}.xml'.format(i,img))
        for xml in xml_list:
            if xml in jpg_list:
                pass
            else:
                print('{}的images缺少数据：{}.jpg'.format(i,xml))
    print('\n命名检查完毕')
                


if __name__ == '__main__':
    path = 'unmeasuredata'
    #path = 'fulldata'
    print('\n-----------------\n')
    # 检查报表列是否合格
    checktable(path)

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