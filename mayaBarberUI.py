from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui
import os
import importlib

class MayaBarberDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(500, 600)
		self.setWindowTitle('Maya Barber ✂️✨')

		self.main_layout = QtWidgets.QVBoxLayout(self)
		self.setLayout(self.main_layout)
		self.setStyleSheet(
			'''
				QDialog{
					background-color: #DED9DE; 
				}
			'''
			)


		self.control_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.control_layout)

		self.exist_button = QtWidgets.QPushButton('Exist🚪')
		self.exist_button.clicked.connect(self.close)
		self.exist_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
					padding: 8px;

				}
				QPushButton:hover{
					background-color: #CCA066;
				}
				QPushButton:pressed{
					background-color: #3D382A;
			'''
			)

		self.main_layout.addStretch()
		self.control_layout.addWidget(self.exist_button)


		self.main_layout.addStretch()

		self.top_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.top_layout)
		self.cut_button = QtWidgets.QPushButton('Cut ✂️')
		self.cut_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
					padding: 8px;
				}
				QPushButton:hover{
					background-color: #CCA066;
				}
				QPushButton:pressed{
					background-color: #3D382A;
			'''
			)

		self.color_button = QtWidgets.QPushButton('Color 🎨')
		self.color_button.clicked.connect(self.color_pick)
		self.color_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
					padding: 8px;
				}
				QPushButton:hover{
					background-color: #CCA066;
				}
				QPushButton:pressed{
					background-color: #3D382A;
			'''
			)
		self.top_layout.addWidget(self.cut_button)
		self.top_layout.addWidget(self.color_button)

		self.middle_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.middle_layout)
		self.comb_button = QtWidgets.QPushButton('Comb 🪮')
		self.comb_button.clicked.connect(self.comb_menu)
		self.comb_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
					padding: 8px;
				}
				QPushButton:hover{
					background-color: #CCA066;
				}
				QPushButton:pressed{
					background-color: #3D382A;
			'''
			)

		self.reset_button = QtWidgets.QPushButton('Reset ✨')
		self.reset_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
					padding: 8px;
				}
				QPushButton:hover{
					background-color: #CCA066;
				}
				QPushButton:pressed{
					background-color: #3D382A;
			'''
			)

		self.middle_layout.addWidget(self.comb_button)
		self.middle_layout.addWidget(self.reset_button)

		self.bottom_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.bottom_layout)
		self.nextCustomer_button = QtWidgets.QPushButton('Next Customer 😊')
		self.nextCustomer_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
					padding: 8px;
				}
				QPushButton:hover{
					background-color: #CCA066;
				}
				QPushButton:pressed{
					background-color: #3D382A;
			'''
			)
		self.bottom_layout.addWidget(self.nextCustomer_button)

	def color_pick(self):
		color = QtWidgets.QColorDialog.getColor(QtGui.QColor("brown"), self, "Select Hair Color")

	def comb_menu(self):
		menu = QtWidgets.QMenu(self)
		menu.addAction("Straight Comb")
		menu.addAction("Curl Comb")
		menu.addAction("Volume Comb")
		menu.addAction("Detangle Comb")
		menu.exec_(QtGui.QCursor.pos())







def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MayaBarberDialog(parent=ptr)
	ui.show()