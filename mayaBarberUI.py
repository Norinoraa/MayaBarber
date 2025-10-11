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

		self.resize(500, 600)
		self.setWindowTitle('Maya Barber ✂️✨')

		self.money = 0

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


		self.control_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.control_layout)

		self.money_label = QtWidgets.QLabel(f"Money: ${self.money}")
		self.money_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #4CAF50;")
		self.control_layout.addWidget(self.money_label)

		self.control_layout.addStretch()

		self.exist_button = QtWidgets.QPushButton('Exist🚪')
		self.exist_button.clicked.connect(self.close)
		self.control_layout.addStretch()
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

		self.model_preview_label = QtWidgets.QLabel("Loading Customer...")
		self.model_preview_label.setAlignment(QtCore.Qt.AlignCenter)
		self.model_preview_label.setMinimumSize(400, 400)
		self.model_preview_label.setStyleSheet(
			'''
				background-color: #F0EBEF;
				border-radius: 15px;
				border: 2px dashed #BDB8BD;

			'''
		)
		
		self.main_layout.addWidget(self.model_preview_label)

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
		self.color_button.clicked.connect(self.colorPick)
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
		self.comb_button.clicked.connect(self.combMenu)
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
		self.nextCustomer_button.clicked.connect(self.call_next_customer_and_update_preview)


	def colorPick(self):
		self.color = mbarCusCL.CustomColorPickerDialog.get_color(QtGui.QColor("brown"), self)
		if color and color.isValid():
			print(f"Color selected: {color.name()}")

	def combMenu(self):
		self.menu = QtWidgets.QMenu(self)

		self.menu.setStyleSheet(
			'''
				QMenu{
					background-color: #7D715C;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
				}
				QMenu:hover{
					background-color: #CCA066;
				}
				QMenu:pressed{
					background-color: #3D382A;
				}
				
			'''
			)

		self.menu.addAction("Blunt bob")
		self.menu.addAction("Ponytail")
		self.menu.addAction("Bowl cut")
		self.menu.addAction("Bun")
		self.menu.exec_(QtGui.QCursor.pos())




	def call_next_customer_and_update_preview(self):
		mbarUtil.next_customer()
		self.update_model_preview()
		
		self.money += 500
		self.update_money_display()

	def update_model_preview(self):
		QtWidgets.QApplication.processEvents()

		try:
			model_panel = cmds.getPanel(withLabel='Persp View')
			if not model_panel or "modelPanel" not in model_panel:
				 model_panel = cmds.getPanel(visiblePanels=True)[0]
		except Exception:
			model_panel = cmds.getPanel(withFocus=True)

		if "modelPanel" not in model_panel:
			print("Error: No valid model panel found for capturing.")
			return
		
		cmds.modelEditor(model_panel, edit=True, displayAppearance='smoothShaded', grid=False, headsUpDisplay=False)
		
		temp_path = os.path.join(cmds.internalVar(userTmpDir=True), 'maya_barber_preview.png')
		
		cmds.playblast(
			format='image', filename=temp_path, sequenceTime=0,
			clearCache=1, viewer=False, showOrnaments=False,
			framePadding=0, percent=100, compression="png",
			quality=100, widthHeight=[512, 512]
		)
		
		cmds.modelEditor(model_panel, edit=True, grid=True, headsUpDisplay=True)

		if os.path.exists(temp_path):
			pixmap = QtGui.QPixmap(temp_path)
			self.model_preview_label.setScaledContents(True)
			self.model_preview_label.setPixmap(pixmap)
		else:
			self.model_preview_label.setText("Failed to capture viewport.")

	def update_money_display(self):
		self.money_label.setText(f"Money: ${self.money}")
			
def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MayaBarberDialog(parent=ptr)
	ui.show()