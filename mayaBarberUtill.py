import maya.cmds as cmds
import os
import random

ASSET_PATH = "C:/Users/nadia/Documents/maya/2026/scripts/mayaBarber/Asset" 
CUSTOMER_PATH = os.path.join(ASSET_PATH, "customer")

def clear_scene():
	if cmds.objExists('barber_grp'):
		cmds.delete('barber_grp')

def next_customer():
	clear_scene()
	
	cmds.group(empty=True, name='barber_grp')
	
	customer_files = [f for f in os.listdir(CUSTOMER_PATH) if f.endswith(".ma")]
	if not customer_files:
		cmds.warning("can't not find model customer in folder assets/customers!")
		return

	chosen_customer_file = random.choice(customer_files)
	customer_file_path = os.path.join(CUSTOMER_PATH, chosen_customer_file)
	
	cmds.file(customer_file_path, i=True, groupName='barber_grp')
	print(f"Loaded customer: {chosen_customer_file}")

	cmds.viewFit(all=True)