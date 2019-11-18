import os
import sys
import json
import pyimgur
from os import walk

class Sync:

	def __init__(self):
		self.path = "/home/akii/Pictures/"
		self.uploaded = {}
		self.CLIENT_ID = "your_client_id"
		self.config = {
			"album_id": "your_album_id",
			"access_token" : "your_access_token",
			"refresh_token" : "your_refresh_token"
		}

	def start(self):
		im = pyimgur.Imgur(self.CLIENT_ID, client_secret=None, access_token=self.config['access_token'], refresh_token=self.config['refresh_token'])
		history_file = self.path + "history.json"

		if os.path.exists(history_file):
			f = open(history_file, 'r')
			self.uploaded = json.loads(f.read())
			f.close()

		files = self.list_files()
		for f in files:
			if f in self.uploaded:
				continue
				
			print("uploading...", f)
			try:
				uploaded_image = im.upload_image(self.path+f, title=f, album=self.config['album_id'])
				self.uploaded[f] = uploaded_image.id
				print("uploaded")
				f = open(history_file, 'w')
				f.write(json.dumps(self.uploaded))
				f.close()
			except Exception as e:
				print(e)
				sys.exit()
	
	def list_files(self):
	    for (dirpath, dirnames, filenames) in walk(self.path):
	        return (f for f in filenames if f.endswith('.png'))

sync = Sync()
sync.start()