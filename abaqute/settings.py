from __future__ import absolute_import
import sys
import os
import subprocess
from abaqute import configs

project_dir=os.path.split(__file__)[0]
abaqus_workdir=os.path.join(project_dir,'abaqus_workdir')

is_run_by_abaqus='ABQLMUSER' in os.environ

def run_script(script_path):
	cmd=r'{cae_exec_path} cae -script {:} -- {:}'.format(
		script_path,get_python_packages_path(),
		cae_exec_path=configs.abaqus_executable_path)
	print "Executing "+cmd
	subprocess.call(cmd.split(' '))

def get_splitted(path):
	outs=list()
	while True:
		rest,chunk=os.path.split(path)
		if not chunk: return [rest]+outs[::-1]
		outs.append(chunk)
		path=rest

def get_parent(path,depth=1):
	curr_path=path
	for i_depth in range(depth):
		curr_path=os.path.dirname(curr_path)
	return curr_path

def get_python_packages_path():
	python_packages_path=os.path.join(get_parent(sys.executable,2),'Lib','site-packages')
	print 'python_packages_path: ',python_packages_path
	return python_packages_path

def update_sys_path():
	sys.path.append(sys.argv[-1])
	sys.path.append(project_dir)

def main():
	# print os.path.join(*get_splitted(__file__))
	print get_parent(__file__,2)
	pass

if __name__=='__main__':
	main()
