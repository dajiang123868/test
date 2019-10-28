#_*_coding:utf-8_*_
"""
创建虚拟环境的两种方式
虚拟环境原理介绍：
虚拟环境相当于一个抽屉，
在这个抽屉中安装的任何软件包都不会影响到其他抽屉。
并且在项目中，我可以指定这个项目的虚拟环境来配合我的项目。
比如我们现在有一个项目是基于Django 1.10.x版本，又有一个项目是基于Django 0.9.x的版本，
那么这时候就可以创建两个虚拟环境，在这两个虚拟环境中分别安装Django 1.10.x和Django 0.9.x来适配我们的项目。
"""

"""
第一种:virtualenv安装方式
virtualenv 是用来创建虚拟环境的软件工具，我们可以通过pip或者pip3来安装：
pip install virtualenv
pip3 install virtualenv
创建虚拟环境：
    1> virtualenv [虚拟环境的名字]
    2> virtualenv -p C:\Python36\python.exe [virutalenv name] # 指定创建环境的python版本
进入虚拟环境：
    1> windows进入虚拟环境：进入到虚拟环境的Scripts文件夹中，然后执行activate。
    2> *nix进入虚拟环境：source /path/to/virtualenv/bin/activate
    一旦你进入到了这个虚拟环境中，你安装包，卸载包都是在这个虚拟环境中，不会影响到外面的环境。
退出虚拟环境：
退出虚拟环境很简单，通过一个命令就可以完成：deactivate

"""
"""
第二种：virtualenvwrapper：
virtualenvwrapper这个软件包可以让我们管理虚拟环境变得更加简单。
不用再跑到某个目录下通过virtualenv来创建虚拟环境，并且激活的时候也要跑到具体的目录下去激活。
安装virtualenvwrapper：
    1> *nix：pip install virtualenvwrapper。
    2> windows：pip install virtualenvwrapper-win。
virtualenvwrapper基本使用：
1.创建虚拟环境
    mkvirtualenv -p python版本  my_env
2.切换到某个虚拟环境
    workon my_env
3.退出当前虚拟环境：
    deactivate
4.删除某个虚拟环境：
    rmvirtualenv my_env
5.列出所有虚拟环境：
    lsvirtualenv
6. 进入到虚拟环境所在的目录：
    cdvirtualenv
"""


