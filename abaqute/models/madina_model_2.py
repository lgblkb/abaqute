from __future__ import absolute_import,print_function

from abaqute import settings
import os
from abaqute.common.geom_utils import ThePoint2D,ThePoint3D
import collections
import functools

settings.update_sys_path()

class Modeller(object):
	
	def build(self):
		pass

def main():
	model_1=Modeller().build()

if __name__=='__main__':
	if settings.is_run_by_abaqus:
		print('Running the script in Abaqus...')
		
		from abaqute.common.red_deflector import *
		
		main()
	else:
		from abaqute.abaqus_runner.main import main
		
		savedir=os.curdir
		os.chdir(settings.abaqus_workdir)
		settings.run_script(__file__)
		os.chdir(savedir)
		main()
	print('Done.')
