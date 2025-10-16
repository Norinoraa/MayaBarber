import maya.cmds as cmds
import os
import random

SCRIPT_DIRECTORY = os.path.dirname(__file__)
ASSET_PATH = os.path.join(SCRIPT_DIRECTORY, "Asset")
CUSTOMER_IMAGE_PATH = os.path.join(ASSET_PATH, "Customer")
HAIR_STYLES_PATH = os.path.join(ASSET_PATH, "Hair")


HAIR_STYLES_MAP = {
	"Blunt bob": "bob.png",
	"Ponytail": "ponytail.png",
	"Bowl cut": "bowlcut.png",
	"Bun": "bun.png"
}

def get_random_customer_path():
	try:
		customer_files = [f for f in os.listdir(CUSTOMER_IMAGE_PATH) if f.endswith('.png')]
		if not customer_files:
			cmds.warning("Could not find any customer images!")
			return None
			
		random_file = random.choice(customer_files)
		return os.path.join(CUSTOMER_IMAGE_PATH, random_file)
		
	except FileNotFoundError:
		cmds.warning(f"Customer directory not found: {CUSTOMER_IMAGE_PATH}")
		return None

def get_hair_style_path(hair_filename):
	path = os.path.join(HAIR_STYLES_PATH, hair_filename)
	if not os.path.exists(path):
		cmds.warning(f"Hair style file not found: {path}")
		return None
	return path