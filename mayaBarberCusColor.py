from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui

class CustomColorPickerDialog(QtWidgets.QDialog):
	def __init__(self, initial_color=QtGui.QColor("brown"), parent=None):
		super().__init__(parent)

		self.setWindowTitle("Custom Color Picker 🎨✨")
		self.setMinimumSize(300, 250) # เพิ่มความสูงเล็กน้อย
		self.final_color = initial_color

		# --- สร้าง Layout หลัก ---
		self.main_layout = QtWidgets.QVBoxLayout(self)

		# --- 1. กำหนด Stylesheet ทั้งหมดในที่เดียว ---
		self.setStyleSheet("""
			QDialog {
				background-color: #DED9DE;
			}
			QLabel {
				color: #453F3C;
				font-size: 16px;
				font-family: Candara;
				font-weight: bold;
			}
			QPushButton {
				background-color: #7D715C;
				color: white; /* เพิ่มสีตัวอักษรให้ปุ่ม */
				border-radius: 10px;
				font-size: 16px;
				font-family: Candara;
				font-weight: bold;
				padding: 8px;
			}
			QPushButton:hover { background-color: #CCA066; }
			QPushButton:pressed { background-color: #3D382A; }
		""")

		# --- 2. สร้าง Widget ต่างๆ ---
		
		# ส่วนแสดงสีตัวอย่าง
		self.color_preview = QtWidgets.QLabel()
		self.color_preview.setMinimumHeight(80)
		self.color_preview.setAutoFillBackground(True)
		self.main_layout.addWidget(self.color_preview)

		# ส่วนของ Slider (ใช้ตัวแปร local)
		form_layout = QtWidgets.QFormLayout()
		self.red_slider = self._create_slider()
		self.green_slider = self._create_slider()
		self.blue_slider = self._create_slider()
		
		form_layout.addRow("Red:", self.red_slider)
		form_layout.addRow("Green:", self.green_slider)
		form_layout.addRow("Blue:", self.blue_slider)
		self.main_layout.addLayout(form_layout)
		
		# ส่วนของปุ่ม (ใช้ตัวแปร local)
		button_layout = QtWidgets.QHBoxLayout()
		self.ok_button = QtWidgets.QPushButton("OK")
		self.cancel_button = QtWidgets.QPushButton("Cancel")
		button_layout.addStretch()
		button_layout.addWidget(self.ok_button)
		button_layout.addWidget(self.cancel_button)
		self.main_layout.addLayout(button_layout)
		
		# --- 3. เชื่อมต่อ Signals ---
		self.red_slider.valueChanged.connect(self._update_color_preview)
		self.green_slider.valueChanged.connect(self._update_color_preview)
		self.blue_slider.valueChanged.connect(self._update_color_preview)
		
		self.ok_button.clicked.connect(self.accept)
		self.cancel_button.clicked.connect(self.reject) # ใช้ reject ดีกว่า close
		
		# --- 4. ตั้งค่าเริ่มต้น ---
		self.red_slider.setValue(initial_color.red())
		self.green_slider.setValue(initial_color.green())
		self.blue_slider.setValue(initial_color.blue())
		self._update_color_preview()


	def _create_slider(self):
		slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		slider.setRange(0, 255)
		return slider

	def _update_color_preview(self):
		r = self.red_slider.value()
		g = self.green_slider.value()
		b = self.blue_slider.value()
		
		self.final_color = QtGui.QColor(r, g, b)
		
		# แก้ไข: ใช้ f-string ที่ถูกต้อง (f นำหน้า ''')
		self.color_preview.setStyleSheet(f"""
			background-color: rgb({r}, {g}, {b});
			border-radius: 10px;
		""")
	
	@staticmethod
	def get_color(initial_color, parent=None):
		dialog = CustomColorPickerDialog(initial_color, parent)
		if dialog.exec():
			return dialog.final_color
		return None