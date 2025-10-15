from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui
import os
import importlib
import maya.cmds as cmds

from . import mayaBarberUtill as mbarUtil
from . import mayaBarberCusColor as mbarCusCL

class MayaBarberDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(500, 650)
		self.setWindowTitle('Maya Barber ✂️✨')
		self.money = 0
		
		self.PREVIEW_IMAGE_PATH = "C:/Users/nadia/Documents/maya/2026/scripts/mayaBarber/Asset/Customer"
		self.HAIR_STYLES_PATH = "C:/Users/nadia/Documents/maya/2026/scripts/mayaBarber/Asset/Hair"

		self.main_layout = QtWidgets.QVBoxLayout(self)
		self.setLayout(self.main_layout)
		self.setStyleSheet(
			'''
				QDialog{ 
					background-color: #DED9DE;
					color: #453F3C;
					}
			'''
			)
		self.main_layout.setContentsMargins(10, 10, 10, 10)
		self.main_layout.setSpacing(15)

		control_layout = QtWidgets.QHBoxLayout()
		self.money_label = QtWidgets.QLabel(f"Money: ${self.money}")
		self.money_label.setStyleSheet(
			'''
				font-size: 18px;
				font-weight: bold;
				color: #4CAF50;
			'''
			)
		self.exist_button = QtWidgets.QPushButton('Exist🚪')
		self.exist_button.clicked.connect(self.close)
		
		control_layout.addWidget(self.money_label)
		control_layout.addStretch()
		control_layout.addWidget(self.exist_button)
		self.main_layout.addLayout(control_layout)

		self.scene = QtWidgets.QGraphicsScene()
		self.view = QtWidgets.QGraphicsView(self.scene)
		self.view.setMinimumSize(400, 300)
		self.view.setStyleSheet(
			'''
				background-color: #F0EBEF;
				border-radius: 15px;
				border: 2px dashed #BDB8BD;
			'''
			)
		
		customer_pixmap = QtGui.QPixmap(f"{self.PREVIEW_IMAGE_PATH}/custommer1.png")
		customer_pixmap = customer_pixmap.scaled(
			QtCore.QSize(400, 400),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.customer_base_item = QtWidgets.QGraphicsPixmapItem(customer_pixmap)


		hair_pixmap = QtGui.QPixmap(f"{self.HAIR_STYLES_PATH}/bob.png")
		hair_pixmap = hair_pixmap.scaled(
			QtCore.QSize(400, 400),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.hair_item = QtWidgets.QGraphicsPixmapItem(hair_pixmap)

		self.customer_base_item.setZValue(0)
		self.hair_item.setZValue(1)


		self.scene.addItem(self.customer_base_item)
		self.scene.addItem(self.hair_item)
		

		self.main_layout.addWidget(self.view)


		button_grid_layout = QtWidgets.QGridLayout()
		self.cut_button = QtWidgets.QPushButton('Cut ✂️')

		self.color_button = QtWidgets.QPushButton('Color 🎨')
		self.color_button.clicked.connect(self.colorPick)

		self.comb_button = QtWidgets.QPushButton('Comb 🪮')
		self.comb_button.clicked.connect(self.combMenu)

		self.reset_button = QtWidgets.QPushButton('Reset ✨')

		button_grid_layout.addWidget(self.cut_button, 0, 0)
		button_grid_layout.addWidget(self.color_button, 0, 1)
		button_grid_layout.addWidget(self.comb_button, 1, 0)
		button_grid_layout.addWidget(self.reset_button, 1, 1)
		self.main_layout.addLayout(button_grid_layout)


		self.nextCustomer_button = QtWidgets.QPushButton('Next Customer 😊')
		self.main_layout.addWidget(self.nextCustomer_button)


		button_style = '''
			QPushButton {
				background-color: #7D715C;
				border-radius: 10px;
				color: white;
				font-size: 20px;
				font-family: Candara;
				font-weight: bold;
				padding: 8px;
			}
			QPushButton:hover { background-color: #CCA066; }
			QPushButton:pressed { background-color: #3D382A; }
		'''
		all_buttons = [self.exist_button, self.cut_button, self.color_button, 
					   self.comb_button, self.reset_button, self.nextCustomer_button]
		for btn in all_buttons:
			btn.setStyleSheet(button_style)

	def colorPick(self):
		color = QtWidgets.QColorDialog.getColor()
		if color.isValid():
			colorize_effect = QtWidgets.QGraphicsColorizeEffect()
			colorize_effect.setColor(color)
			self.hair_item.setGraphicsEffect(colorize_effect)

	def combMenu(self):
		menu = QtWidgets.QMenu(self)
		menu.setStyleSheet(
			"""
				QMenu{ 
					background-color: #5D5443;
					border: 1px solid #7D715C;
					color: #E0D6C4;
					}
				QMenu::item{
					padding: 5px 25px;
					border-radius: 5px;
					}
				QMenu::item:selected{ 
					background-color: #7D715C;
					color: #FFFFFF;
					}
			"""
			)
		action_bob = menu.addAction("Blunt bob")
		
		action_ponytail = menu.addAction("Ponytail")
		
		action_bowl = menu.addAction("Bowl cut")

		action_bun = menu.addAction("Bun")

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