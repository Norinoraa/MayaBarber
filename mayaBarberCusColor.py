from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui

class CustomColorPickerDialog(QtWidgets.QDialog):
	def __init__(self, initial_color=QtGui.QColor("brown"), parent=None):
		super().__init__(parent)

		self.setWindowTitle("Custom Color Picker🎨✨")
		self.setMinimumSize(300, 200)
		self.final_color = initial_color

		self.main_layout = QtWidgets.QVBoxLayout(self)

		self.setStyleSheet(
			'''
				QDialog{
					color: #DED9DE;
					border-radius: 10px;
					font-size: 20px;
					font-family: Candara;
					font-weight: bold;
				}
			'''
			)
		self.color_preview = QtWidgets.QLabel()
		self.color_preview.setMinimumHeight(80)
		self.color_preview.setAutoFillBackground(True)
		self.main_layout.addWidget(self.color_preview)

		self.form_layout = QtWidgets.QFormLayout()
		self.red_slider = self._create_slider()
		self.green_slider = self._create_slider()
		self.blue_slider = self._create_slider()
		
		self.form_layout.addRow("Red:", self.red_slider)
		self.form_layout.addRow("Green:", self.green_slider)
		self.form_layout.addRow("Blue:", self.blue_slider)
		self.main_layout.addLayout(form_layout)
		
		self.button_layout = QtWidgets.QHBoxLayout()
		self.ok_button = QtWidgets.QPushButton("OK")
		self.ok_button.clicked.connect(self.accept)
		self.ok_button.setStyleSheet(
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
					}
			'''
			)
		

		self.cancel_button = QtWidgets.QPushButton("Cancel")
		self.cancel_button.clicked.connect(self.close)
		self.cancel_button.setStyleSheet(
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
					}
			'''
			)

		self.button_layout.addStretch()
		self.button_layout.addWidget(self.ok_button)
		self.button_layout.addWidget(self.cancel_button)

		self.main_layout.addLayout(button_layout)
		
		self.red_slider.valueChanged.connect(self._update_color_preview)
		self.green_slider.valueChanged.connect(self._update_color_preview)
		self.blue_slider.valueChanged.connect(self._update_color_preview)
		
		self.red_slider.setValue(initial_color.red())
		self.green_slider.setValue(initial_color.green())
		self.blue_slider.setValue(initial_color.blue())
		self._update_color_preview()


	def _create_slider(self):
		self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.slider.setRange(0, 255)
		return slider

	def _update_color_preview(self):
		r = self.red_slider.value()
		g = self.green_slider.value()
		b = self.blue_slider.value()
		
		self.final_color = QtGui.QColor(r, g, b)
		self.color_preview.setStyleSheet(
			'''
				background-color: rgb({r}, {g}, {b});
				border-radius: 10px;
			'''
			)
	
	@staticmethod
	def get_color(initial_color, parent=None):

		dialog = CustomColorPickerDialog(initial_color, parent)
		
		if dialog.exec():
			return dialog.final_color
		return None