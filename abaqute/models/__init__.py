from __future__ import absolute_import
from abaqute import settings

settings.update_sys_path()

class Modeller(object):
	def __init__(self):
		self.model=mdb.models['Model-1']
	
	def build(self):
		return self

def main():
	model_1=Modeller().build()

if __name__=='__main__':
	if settings.is_run_by_abaqus:
		print 'Running the script in Abaqus...'
		from abaqute.common.red_deflector import *
		
		main()
	else:
		settings.run_script(__file__)
	print 'Done.'
