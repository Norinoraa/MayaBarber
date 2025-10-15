import maya.cmds as cmds
import os
import random

ASSET_PATH = "C:/Users/nadia/Documents/maya/2026/scripts/mayaBarber/Asset" 
PREVIEW_PATH = os.path.join(ASSET_PATH, "C:/Users/nadia/Documents/maya/2026/scripts/mayaBarber/Asset/Customer/custommer1.png") # <<< เปลี่ยนเป็นโฟลเดอร์รูปภาพ

def next_customer():

	if not os.path.exists(PREVIEW_PATH):
		print(f"Error: Preview folder not found at {PREVIEW_PATH}")
		return None

	customer_files = [f for f in os.listdir(PREVIEW_PATH) if f.lower().endswith(".png")]
	
	if not customer_files:
		print("ไม่เจอไฟล์รูปภาพลูกค้าในโฟลเดอร์ customer_previews!")
		return None

	chosen_customer_file = random.choice(customer_files)
	print(f"Selected customer image: {chosen_customer_file}")
	
	return chosen_customer_file