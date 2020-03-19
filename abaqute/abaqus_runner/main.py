import time
from pathlib import Path
import os
import subprocess
from lgblkb_tools import Folder,logger
import numpy as np
from lgblkb_tools.pathify import get_name
from abaqute.abaqus_runner.modelling import Node,NodeSet,Model,Element
from abaqute.abaqus_runner.py_curve import get_py_curve,get_gap

# logger=logging.getLogger('abaqus_runner')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

project_dir=Path(__file__).parent
project_folder=Folder(__file__)
sim_folder=project_folder['sim_folder']
abaqus_cmd='C:\Windows\SysWOW64\cmd.exe /k'

def model_2():
	model=Model()
	
	node1=Node([0,0])
	node2=Node([5,0])
	
	elem1=Element(node1,node2)
	
	nodeset1=NodeSet('node1',node1)
	nodeset2=NodeSet('node2',node2)
	
	model.add_node(node1)
	model.add_node(node2)
	model.add_nodeset(nodeset1)
	model.add_nodeset(nodeset2)
	
	gap_values=get_py_curve(np.arange(-3000,3001,1000))[:1]
	model.add_element(elem1)
	model.add_gap(-0.5)
	model.add_py_curve(gap_values)
	model.add_friction(elastic_slip=2.54,myu=0.233)
	model.add_boundary(nodeset1,1,1)
	model.add_boundary(nodeset1,2,2)
	model.add_boundary(nodeset1,3,3)
	model.add_boundary(nodeset2,3,3)
	
	for i,(x,y) in enumerate(gap_values):
		step_data=f"""** ----------------------------------------------------------------
** 
** STEP: Step-1
** 
*Step, name=Step-{i+1}
*Static
1., 1., 1e-05, 1.
** 
** BOUNDARY CONDITIONS
** 
** Name: BC-2 Type: Displacement/Rotation
** 
*Boundary
node2, 1, 1, {-float(y)}
** OUTPUT REQUESTS
** 
*Restart, write, frequency=0
** 
** FIELD OUTPUT: F-Output-1
** 
*Output, field, variable=PRESELECT
** 
** HISTORY OUTPUT: H-Output-1
** 
*Output, history, variable=PRESELECT
*End Step"""
		model.add_raw_data(step_data)
	
	input_filepath=sim_folder['test.inp']
	model.write_to_file(input_filepath)
	run_abaqus_job(sim_folder,input_filepath)

def run_abaqus_job(sim_folder_,input_filepath):
	subprocess.run(f'abaqus job={get_name(input_filepath)}',
	               shell=True,cwd=sim_folder_)
	is_created=False
	while True:
		is_simdir_present=sim_folder_.glob_search('test.simdir')
		if is_created:
			if is_simdir_present:
				time.sleep(1)
			else:
				break
		else:
			if is_simdir_present:
				is_created=True
				logger.debug('simdir is created.')
			else:
				time.sleep(1)
	
	pass

def main():
	model_2()
	pass

if __name__=='__main__':
	main()
