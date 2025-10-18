from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui
import os
import importlib
import maya.cmds as cmds
import random

from . import mayaBarberUtill as mbarUtil
importlib.reload(mbarUtil)


class MayaBarberDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(500, 650)
		self.setWindowTitle('Maya Barber ✂️✨')
		self.money = 0
		self.is_first_customer = True
				
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
		
		self.customer_base_item = QtWidgets.QGraphicsPixmapItem()


		initial_hair_path = mbarUtil.get_hair_style_path("bob.png")
		if initial_hair_path:
			hair_pixmap = QtGui.QPixmap(initial_hair_path)
			hair_pixmap = hair_pixmap.scaled(
				QtCore.QSize(400, 400),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation
			)
			self.hair_item = QtWidgets.QGraphicsPixmapItem(hair_pixmap)
		else:
			self.hair_item = QtWidgets.QGraphicsPixmapItem()

		self.customer_base_item.setZValue(0)
		self.hair_item.setZValue(1)


		self.scene.addItem(self.customer_base_item)
		self.scene.addItem(self.hair_item)
		

		self.main_layout.addWidget(self.view)


		button_grid_layout = QtWidgets.QGridLayout()
		self.cut_button = QtWidgets.QPushButton('Cut ✂️')
		self.cut_button.clicked.connect(self.cut_hair)

		self.color_button = QtWidgets.QPushButton('Color 🎨')
		self.color_button.clicked.connect(self.colorPick)

		self.comb_button = QtWidgets.QPushButton('Comb 🪮')
		self.comb_button.clicked.connect(self.combMenu)

		self.reset_button = QtWidgets.QPushButton('Reset ✨')
		self.reset_button.clicked.connect(self.reset_hair)

		button_grid_layout.addWidget(self.cut_button, 0, 0)
		button_grid_layout.addWidget(self.color_button, 0, 1)
		button_grid_layout.addWidget(self.comb_button, 1, 0)
		button_grid_layout.addWidget(self.reset_button, 1, 1)
		self.main_layout.addLayout(button_grid_layout)


		self.nextCustomer_button = QtWidgets.QPushButton('Next Customer 😊')
		self.nextCustomer_button.clicked.connect(self.load_next_customer)
		self.main_layout.addWidget(self.nextCustomer_button)

		self.load_next_customer()


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

			hair_styles_map = mbarUtil.HAIR_STYLES_MAP

			for display_name, file_name in hair_styles_map.items():
				action = menu.addAction(display_name)
				action.triggered.connect(lambda checked=False, fn=file_name: self.change_hair_style(fn))
			
			menu.exec_(QtGui.QCursor.pos())

	def load_next_customer(self):
			if not self.is_first_customer:
				self.money += 500
				self.money_label.setText(f"Money: ${self.money}")
			image_path = mbarUtil.get_random_customer_path()

			if image_path:
				customer_pixmap = QtGui.QPixmap(image_path)
				customer_pixmap = customer_pixmap.scaled(
					QtCore.QSize(400, 400),
					QtCore.Qt.KeepAspectRatio,
					QtCore.Qt.SmoothTransformation
				)
				self.customer_base_item.setPixmap(customer_pixmap)

			self.is_first_customer = False

	def change_hair_style(self, hair_filename):
			image_path = mbarUtil.get_hair_style_path(hair_filename)

			if image_path:
				self.hair_item.show()
				
				hair_pixmap = QtGui.QPixmap(image_path)
				hair_pixmap = hair_pixmap.scaled(
					QtCore.QSize(400, 400),
					QtCore.Qt.KeepAspectRatio,
					QtCore.Qt.SmoothTransformation
				)
				self.hair_item.setPixmap(hair_pixmap)
				self.hair_item.setGraphicsEffect(None)

	def cut_hair(self):
		self.hair_item.hide()

	def reset_hair(self):
		self.change_hair_style("bob.png")
		
def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MayaBarberDialog(parent=ptr)
	ui.show()