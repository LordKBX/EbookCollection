# This Python file uses the following encoding: utf-8
import os
import sys
from PyQt5.QtWidgets import *
import PyQt5.uic
from PyQt5.uic import *

from common.vars import *
from common.lang import *


class EmptyBookWindow(QDialog):
    def __init__(self, parent, bdd):
        super(EmptyBookWindow, self).__init__(parent, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        PyQt5.uic.loadUi(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'empty_book.ui'.replace('/', os.sep), self)  # Load the .ui file

        lng = Lang()
        self.BDD = bdd
        style = self.BDD.get_param('style')
        lng.set_lang(self.BDD.get_param('lang'))

        self.setStyleSheet(get_style_var(style, 'QDialog'))
        self.setWindowTitle(lng['Library/emptyBooks/WindowTitle'])

        self.number_label.setText(lng['Library/emptyBooks/Number'])
        self.authors_label.setText(lng['Library/emptyBooks/Authors'])
        self.serie_label.setText(lng['Library/emptyBooks/Series'])
        self.name_label.setText(lng['Library/emptyBooks/Name'])
        self.format_label.setText(lng['Library/emptyBooks/Format'])
        self.serie_volume_label.setText(lng['Library/emptyBooks/SeriesVolume'])

        self.number_spin_box.setValue(1)
        self.serie_volume_spin_box.setValue(1.0)
        self.authors_line_edit.setText("")
        self.serie_line_edit.setText("")
        self.name_line_edit.setText("")

        self.button_box.button(QDialogButtonBox.Ok).setText(lng['Editor/FilesWindow/btnOk'])
        self.button_box.button(QDialogButtonBox.Cancel).setText(lng['Editor/FilesWindow/btnCancel'])

        cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        self.button_box.button(QDialogButtonBox.Ok).setStyleSheet(get_style_var(style, 'fullAltButton'))
        self.button_box.button(QDialogButtonBox.Ok).setCursor(cursor)
        self.button_box.button(QDialogButtonBox.Cancel).setStyleSheet(get_style_var(style, 'fullAltButton'))
        self.button_box.button(QDialogButtonBox.Cancel).setCursor(cursor)

    def open_exec(self, file_formats: [str] = None):
        if file_formats is None:
            file_formats = ["EPUB"]
        # self.format_combobox = QComboBox()
        for file_type in file_formats:
            self.format_combobox.addItem(file_type, file_type)
        self.format_combobox.setCurrentIndex(0)

        ret = self.exec_()
        if ret == 1:
            data = {
                "number": self.number_spin_box.value(),
                "authors": self.authors_line_edit.text(),
                "series": self.serie_line_edit.text(),
                "vol": self.serie_volume_spin_box.value(),
                "name": self.name_line_edit.text(),
                "format": self.format_combobox.currentText()
            }
            return data
        else:
            return None
