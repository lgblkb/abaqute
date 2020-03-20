from __future__ import absolute_import,print_function

from abaqute import settings
import os
import numpy as np
from abaqute.common.geom_utils import ThePoint2D,ThePoint3D
import collections
import functools
import csv

settings.update_sys_path()

class Modeller(object):
	def __init__(self):
		self.model=mdb.models['Model-1']
	
	def create_sketch(self,d_inner,d_outer):
		self.model.ConstrainedSketch(name='__profile__',sheetSize=8000.0)
		self.model.sketches['__profile__'].sketchOptions.setValues(viewStyle=AXISYM)
		self.model.sketches['__profile__'].ConstructionLine(point1=(0.0,-4000.0),point2=(0.0,4000.0))
		self.model.sketches['__profile__'].FixedConstraint(entity=self.model.sketches['__profile__'].geometry[2])
		corner_1=(d_inner,-3000.0)
		corner_2=(d_outer,-3000.0)
		corner_3=(d_outer,3000.0)
		corner_4=(d_inner,3000.0)
		self.model.sketches['__profile__'].Spot(point=corner_1)
		self.model.sketches['__profile__'].Spot(point=corner_2)
		self.model.sketches['__profile__'].Spot(point=corner_3)
		self.model.sketches['__profile__'].Spot(point=corner_4)
		self.model.sketches['__profile__'].Line(point1=corner_4,point2=corner_3)
		self.model.sketches['__profile__'].Line(point1=corner_3,point2=corner_2)
		self.model.sketches['__profile__'].Line(point1=corner_2,point2=corner_1)
		self.model.sketches['__profile__'].Line(point1=corner_1,point2=corner_4)
		# model.sketches['__profile__'].geometry.findAt((300.0,3000.0))
		# model.sketches['__profile__'].geometry.findAt((300.0,3000.0))
		# model.sketches['__profile__'].HorizontalConstraint(addUndoState=False,entity=model.sketches['__profile__'].geometry[3])
		
		# model.sketches['__profile__'].geometry.findAt((500.0,0.0))
		# model.sketches['__profile__'].geometry.findAt((500.0,0.0))
		# model.sketches['__profile__'].VerticalConstraint(addUndoState=
		#                                                  False,entity=
		#                                                  model.sketches[
		# 	                                                 '__profile__'].geometry[
		# 	                                                 4])
		# model.sketches['__profile__'].geometry.findAt((300.0,3000.0))
		# model.sketches['__profile__'].geometry.findAt((500.0,0.0))
		# model.sketches['__profile__'].geometry.findAt((300.0,3000.0))
		# model.sketches['__profile__'].geometry.findAt((500.0,0.0))
		# model.sketches['__profile__'].PerpendicularConstraint(
		# 	addUndoState=False,entity1=
		# 	model.sketches['__profile__'].geometry[3],entity2=
		# 	model.sketches['__profile__'].geometry[4])
		
		# model.sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		# model.sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		# model.sketches['__profile__'].HorizontalConstraint(
		# 	addUndoState=False,entity=
		# 	model.sketches['__profile__'].geometry[5])
		# model.sketches['__profile__'].geometry.findAt((500.0,0.0))
		# model.sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		# model.sketches['__profile__'].geometry.findAt((500.0,0.0))
		# model.sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		# model.sketches['__profile__'].PerpendicularConstraint(
		# 	addUndoState=False,entity1=
		# 	model.sketches['__profile__'].geometry[4],entity2=
		# 	model.sketches['__profile__'].geometry[5])
		
		# model.sketches['__profile__'].geometry.findAt((100.0,0.0))
		# model.sketches['__profile__'].geometry.findAt((100.0,0.0))
		# model.sketches['__profile__'].VerticalConstraint(addUndoState=
		#                                                  False,entity=
		#                                                  model.sketches[
		# 	                                                 '__profile__'].geometry[
		# 	                                                 6])
		# model.sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		# model.sketches['__profile__'].geometry.findAt((100.0,0.0))
		# model.sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		# model.sketches['__profile__'].geometry.findAt((100.0,0.0))
		# model.sketches['__profile__'].PerpendicularConstraint(
		# 	addUndoState=False,entity1=
		# 	model.sketches['__profile__'].geometry[5],entity2=
		# 	model.sketches['__profile__'].geometry[6])
		
		pass
	
	def create_bottom_springs(self,mesh_size,):
		model=self.model
		conn_sect=model.ConnectorSection(name='ConnSect-1',translationalType=CARTESIAN)
		conn_sect.setValues(behaviorOptions=(
			ConnectorPlasticity(isotropic=OFF,kinematic=ON,isotropicTable=((0.0,0.0,
			                                                                0.0),),
			                    kinematicTable=((4.091917,2.0),
			                                    (8.18394,13.0),
			                                    (12.27591,42.0),
			                                    (14.73109,73.0),
			                                    (16.36788,100.0)),
			                    components=(1,)),))
		
		# Save by Madina on 2020_03_17-23.06.21; build 6.14-2 2014_08_22-20.00.46 134497
		d_inner=100.0
		d_outer=500.0
		points_count=int((d_outer-d_inner)/mesh_size+1)
		# points=list()
		
		for i in range(points_count):
			x_coor=d_inner+i*mesh_size
			point1=np.array((x_coor,-3000.0,0.0))
			point2=np.array((x_coor,-3010.0,0.0))
			ref_point_1=model.rootAssembly.ReferencePoint(point=tuple(point1))
			ref_point_2=model.rootAssembly.ReferencePoint(point=tuple(point2))
			mid_point_coor=tuple((point1+point2)/2)
			# points.append((rp1,rp2))
			model.rootAssembly.WirePolyLine(mergeType=IMPRINT,meshable=OFF,
			                                points=((model.rootAssembly.referencePoints[ref_point_1.id],
			                                         model.rootAssembly.referencePoints[ref_point_2.id],),))
			# print('Wire polyline created.')
			wire_set=mdb.models['Model-1'].rootAssembly.Set(
				edges=mdb.models['Model-1'].rootAssembly.edges.findAt((mid_point_coor,)),
				name='Wire-{}-Set-1'.format(i))
			# print('Wire set created.')
			model.rootAssembly.SectionAssignment(region=wire_set,sectionName='ConnSect-1')
	
	def build(self):
		# -*- coding: mbcs -*-
		model=self.model
		self.create_sketch(100,500)
		
		part=model.Part(dimensionality=AXISYMMETRIC,name='Part-1',type=DEFORMABLE_BODY)
		part.BaseShell(sketch=model.sketches['__profile__'])
		del model.sketches['__profile__']
		
		mat=model.Material(name='Material-1')
		mat.Elastic(table=((20000.0,0.2),))
		mat.Conductivity(table=((2.0,),))
		mat.SpecificHeat(table=((940.0,),))
		
		model.HomogeneousSolidSection(material='Material-1',name='Section-1',thickness=None)
		global_set=part.Set(faces=part.faces.getSequenceFromMask(mask=('[#1 ]',),),name='Set-1')
		part.SectionAssignment(offset=0.0,
		                       offsetField='',offsetType=MIDDLE_SURFACE,region=global_set,
		                       sectionName='Section-1',thicknessAssignment=FROM_SECTION)
		
		model.rootAssembly.DatumCsysByThreePoints(coordSysType=CYLINDRICAL,origin=(0.0,0.0,0.0),
		                                          point1=(1.0,0.0,0.0),
		                                          point2=(0.0,0.0,-1.0))
		instance1=model.rootAssembly.Instance(dependent=ON,name='Part-1-1',part=part)
		model.StaticStep(name='Step-1',previous='Initial')
		mesh_size=10.0
		part.seedEdgeByBias(biasMethod=SINGLE,constraint=FINER,
		                    end2Edges=model.parts[
			                    'Part-1'].edges.getSequenceFromMask(
			                    ('[#2 ]',
			                     ),),maxSize=mesh_size,minSize=mesh_size)
		part.generateMesh()
		# Save by Madina on 2020_03_17-22.36.08; build 6.14-2 2014_08_22-20.00.46 134497
		model.rootAssembly.regenerate()
		
		self.create_bottom_springs(mesh_size)
		
		job_1=mdb.Job(atTime=None,contactPrint=OFF,description='',echoPrint=OFF,
		              explicitPrecision=SINGLE,getMemoryFromAnalysis=True,historyPrint=OFF,
		              memory=90,memoryUnits=PERCENTAGE,model='Model-1',modelPrint=OFF,
		              multiprocessingMode=DEFAULT,name='Job-1',nodalOutputPrecision=SINGLE,
		              numCpus=1,numGPUs=0,queue=None,resultsFormat=ODB,scratch='',type=
		              ANALYSIS,userSubroutine='',waitHours=0,waitMinutes=0)
		
		job_1.writeInput()
		input_filepath=os.path.join(settings.abaqus_workdir,job_1.name+'.inp')
		print(input_filepath)
		# target_nodes=list()
		# for node in global_set.nodes:
		# 	if node.coordinates[0]==500:
		# 		target_nodes.append(node)
		# print('len(target_nodes)',len(target_nodes))
		
		with open(os.path.join(settings.abaqus_workdir,'nodes_data.csv'),mode='w') as file:
			writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
			for node in global_set.nodes:
				writer.writerow([node.label]+list(node.coordinates))
				
		return self

def main():
	modeller=Modeller()
	modeller.build()

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
	print('Done.')
