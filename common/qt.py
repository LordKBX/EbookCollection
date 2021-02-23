import os, sys
import enum
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from vars import *


class QtQIconEnum(enum.Enum):
    folder = env_vars['styles']['black']['icons']['folder']
    file = env_vars['styles']['black']['icons']['file']
    lock = env_vars['styles']['black']['icons']['lock']
    unlock = env_vars['styles']['black']['icons']['unlock']


def setQTreeItemIcon(item: QtWidgets.QTreeWidgetItem, iconRef: QtQIconEnum = QtQIconEnum.folder):
    icon = QtGui.QIcon()
    image = QtGui.QPixmap()
    image.load(iconRef.value)
    icon.addPixmap(image, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(0, icon)


def setQTreeItemFolderIcon(item: QtWidgets.QTreeWidgetItem):
    setQTreeItemIcon(item, QtQIconEnum.folder)


def setQTreeItemLockIcon(item: QtWidgets.QTreeWidgetItem):
    setQTreeItemIcon(item, QtQIconEnum.lock)
