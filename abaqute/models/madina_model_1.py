from __future__ import absolute_import,print_function

from abaqute import settings
import os
from abaqute.common.geom_utils import ThePoint2D,ThePoint3D
import collections
import functools

settings.update_sys_path()

class Modeller(object):
	
	def build(self):
		# -*- coding: mbcs -*-
		
		mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=8000.0)
		mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
			viewStyle=AXISYM)
		mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0,
		                                                                       -4000.0),point2=(0.0,4000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
		                                                              mdb.models['Model-1'].sketches[
			                                                              '__profile__'].geometry[2])
		mdb.models['Model-1'].sketches['__profile__'].Spot(point=(100.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].Spot(point=(500.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].Spot(point=(500.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].Spot(point=(100.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].Line(point1=(100.0,3000.0),
		                                                   point2=(500.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
			addUndoState=False,entity=
			mdb.models['Model-1'].sketches['__profile__'].geometry[3])
		mdb.models['Model-1'].sketches['__profile__'].Line(point1=(500.0,3000.0),
		                                                   point2=(500.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((500.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((500.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
		                                                                 False,entity=
		                                                                 mdb.models['Model-1'].sketches[
			                                                                 '__profile__'].geometry[
			                                                                 4])
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((500.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((500.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
			addUndoState=False,entity1=
			mdb.models['Model-1'].sketches['__profile__'].geometry[3],entity2=
			mdb.models['Model-1'].sketches['__profile__'].geometry[4])
		mdb.models['Model-1'].sketches['__profile__'].Line(point1=(500.0,-3000.0),
		                                                   point2=(100.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
			addUndoState=False,entity=
			mdb.models['Model-1'].sketches['__profile__'].geometry[5])
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((500.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((500.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
			addUndoState=False,entity1=
			mdb.models['Model-1'].sketches['__profile__'].geometry[4],entity2=
			mdb.models['Model-1'].sketches['__profile__'].geometry[5])
		mdb.models['Model-1'].sketches['__profile__'].Line(point1=(100.0,-3000.0),
		                                                   point2=(100.0,3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((100.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((100.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
		                                                                 False,entity=
		                                                                 mdb.models['Model-1'].sketches[
			                                                                 '__profile__'].geometry[
			                                                                 6])
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((100.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((300.0,-3000.0))
		mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((100.0,0.0))
		mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
			addUndoState=False,entity1=
			mdb.models['Model-1'].sketches['__profile__'].geometry[5],entity2=
			mdb.models['Model-1'].sketches['__profile__'].geometry[6])
		mdb.models['Model-1'].Part(dimensionality=AXISYMMETRIC,name='Part-1',type=
		DEFORMABLE_BODY)
		mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
		                                                mdb.models['Model-1'].sketches['__profile__'])
		del mdb.models['Model-1'].sketches['__profile__']
		mdb.models['Model-1'].Material(name='Material-1')
		mdb.models['Model-1'].materials['Material-1'].Elastic(table=((20000.0,0.2),))
		mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1',name=
		'Section-1',thickness=None)
		mdb.models['Model-1'].parts['Part-1'].Set(faces=
		mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(mask=(
			'[#1 ]',),),name='Set-1')
		mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0,
		                                                        offsetField='',offsetType=MIDDLE_SURFACE,region=
		                                                        mdb.models['Model-1'].parts['Part-1'].sets['Set-1'],
		                                                        sectionName=
		                                                        'Section-1',thicknessAssignment=FROM_SECTION)
		mdb.models['Model-1'].rootAssembly.DatumCsysByThreePoints(coordSysType=
		                                                          CYLINDRICAL,origin=(0.0,0.0,0.0),
		                                                          point1=(1.0,0.0,0.0),
		                                                          point2=(0.0,
		                                                                  0.0,-1.0))
		mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,name='Part-1-1',
		                                            part=mdb.models['Model-1'].parts['Part-1'])
		mdb.models['Model-1'].StaticStep(name='Step-1',previous='Initial')
		mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(biasMethod=SINGLE,
		                                                     constraint=FINER,end2Edges=
		                                                     mdb.models['Model-1'].parts[
			                                                     'Part-1'].edges.getSequenceFromMask(
			                                                     ('[#2 ]',
			                                                      ),),maxSize=10.0,minSize=10.0)
		mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(biasMethod=SINGLE,
		                                                     constraint=FINER,end2Edges=
		                                                     mdb.models['Model-1'].parts[
			                                                     'Part-1'].edges.getSequenceFromMask(
			                                                     ('[#2 ]',
			                                                      ),),maxSize=10.0,minSize=10.0)
		mdb.models['Model-1'].parts['Part-1'].generateMesh()
		# Save by Madina on 2020_03_17-22.36.08; build 6.14-2 2014_08_22-20.00.46 134497
		
		mdb.models['Model-1'].rootAssembly.regenerate()
		the_job=mdb.Job(atTime=None,contactPrint=OFF,description='',echoPrint=OFF,
		                explicitPrecision=SINGLE,getMemoryFromAnalysis=True,historyPrint=OFF,
		                memory=90,memoryUnits=PERCENTAGE,model='Model-1',modelPrint=OFF,
		                multiprocessingMode=DEFAULT,name='Job-1',nodalOutputPrecision=SINGLE,
		                numCpus=1,numGPUs=0,queue=None,resultsFormat=ODB,scratch='',type=
		                ANALYSIS,userSubroutine='',waitHours=0,waitMinutes=0)
		# Save by Madina on 2020_03_17-23.06.21; build 6.14-2 2014_08_22-20.00.46 134497
		
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(100.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(100.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(110.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(110.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(120.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(120.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(130.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(130.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(140.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(140.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(150.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(150.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(160.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(160.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(170.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(170.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(180.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(180.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(190.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(190.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(200.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(200.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(210.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(210.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(220.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(220.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(230.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(230.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(240.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(240.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(250.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(250.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(260.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(260.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(270.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(270.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(280.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(280.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(290.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(290.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(300.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(300.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(310.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(310.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(320.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(320.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(330.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(330.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(340.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(340.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(350.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(350.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(360.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(360.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(370.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(370.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(380.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(380.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(390.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(390.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(400.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(400.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(410.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(410.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(420.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(420.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(430.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(430.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(440.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(440.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(450.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(450.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(460.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(460.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(470.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(470.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(480.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(480.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(490.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(490.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(500.0,-3000.0,0.0))
		mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(500.0,-3010.0,0.0))
		mdb.models['Model-1'].rootAssembly.WirePolyLine(mergeType=IMPRINT,meshable=OFF
		                                                ,
		                                                points=((mdb.models['Model-1'].rootAssembly.referencePoints[4],
		                                                         mdb.models['Model-1'].rootAssembly.referencePoints[5]),
		                                                        (
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        6],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        7]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        8],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        9]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        10],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        11]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        12],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        13]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        14],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        15]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        16],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        17]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        18],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        19]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        20],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        21]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        22],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        23]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        24],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        25]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        26],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        27]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        28],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        29]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        30],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        31]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        32],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        33]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        34],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        35]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        36],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        37]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        38],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        39]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        40],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        41]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        42],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        43]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        44],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        45]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        46],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        47]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        48],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        49]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        50],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        51]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        52],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        53]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        54],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        55]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        56],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        57]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        58],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        59]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        60],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        61]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        62],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        63]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        64],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        65]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        66],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        67]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        68],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        69]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        70],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        71]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        72],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        73]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        74],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        75]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        76],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        77]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        78],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        79]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        80],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        81]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        82],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        83]),(
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        84],
			                                                        mdb.models['Model-1'].rootAssembly.referencePoints[
				                                                        85])))
		mdb.models['Model-1'].ConnectorSection(name='ConnSect-1',translationalType=
		CARTESIAN)
		mdb.models['Model-1'].sections['ConnSect-1'].setValues(behaviorOptions=(
			ConnectorElasticity(behavior=NONLINEAR,table=((0.0,0.0),(16.36788,0.0),
			                                              (4.09197,2.0),(8.18394,13.0),(12.27591,42.0),
			                                              (14.73109,73.0),
			                                              (
				                                              16.36788,100.0)),independentComponents=(),
			                    components=(1,)),))
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#0 #100 ]',
			 ),),name='Set-1')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-1'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#0 #80 ]',
			 ),),name='Set-2')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-2'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#0 #40 ]',
			 ),),name='Set-3')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-3'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#0 #20 ]',
			 ),),name='Set-4')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-4'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#0 #10 ]',
			 ),),name='Set-5')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-5'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#0 #8 ]',
		                                                                                                     ),),
		                                       name='Set-6')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-6'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#0 #4 ]',
		                                                                                                     ),),
		                                       name='Set-7')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-7'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#0 #2 ]',
		                                                                                                     ),),
		                                       name='Set-8')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-8'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#0 #1 ]',
		                                                                                                     ),),
		                                       name='Set-9')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-9'],
		                                                     sectionName='ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#80000000 ]',),),name='Set-10')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-10'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#40000000 ]',),),name='Set-11')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-11'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#20000000 ]',),),name='Set-12')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-12'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#10000000 ]',),),name='Set-13')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-13'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#8000000 ]',),),name='Set-14')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-14'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#4000000 ]',),),name='Set-15')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-15'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#2000000 ]',),),name='Set-16')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-16'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask((
			'[#1000000 ]',),),name='Set-17')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-17'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#800000 ]',
			 ),),
			name='Set-18')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-18'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#400000 ]',
			 ),),
			name='Set-19')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-19'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#200000 ]',
			 ),),
			name='Set-20')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-20'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#100000 ]',
			 ),),
			name='Set-21')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-21'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#80000 ]',
			 ),),
			name='Set-22')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-22'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#40000 ]',
			 ),),
			name='Set-23')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-23'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#20000 ]',
			 ),),
			name='Set-24')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-24'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#10000 ]',
			 ),),
			name='Set-25')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-25'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#8000 ]',
		                                                                                                     ),),
		                                       name='Set-26')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-26'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#4000 ]',
		                                                                                                     ),),
		                                       name='Set-27')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-27'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#2000 ]',
		                                                                                                     ),),
		                                       name='Set-28')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-28'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#1000 ]',
		                                                                                                     ),),
		                                       name='Set-29')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-29'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#800 ]',),
		),name='Set-30')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-30'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#400 ]',),
		),name='Set-31')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-31'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#200 ]',),
		),name='Set-32')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-32'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#100 ]',),
		),name='Set-33')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-33'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#80 ]',),
		                                                                                                    ),
		                                       name='Set-34')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-34'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#40 ]',),
		                                                                                                    ),
		                                       name='Set-35')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-35'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#20 ]',),
		                                                                                                    ),
		                                       name='Set-36')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-36'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		                                       mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(('[#10 ]',),
		                                                                                                    ),
		                                       name='Set-37')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-37'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#8 ]',),)
			,name='Set-38')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-38'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#4 ]',),)
			,name='Set-39')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-39'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#2 ]',),)
			,name='Set-40')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-40'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		mdb.models['Model-1'].rootAssembly.Set(edges=
		mdb.models['Model-1'].rootAssembly.edges.getSequenceFromMask(
			('[#1 ]',),)
			,name='Set-41')
		mdb.models['Model-1'].rootAssembly.SectionAssignment(region=
		                                                     mdb.models['Model-1'].rootAssembly.sets['Set-41'],
		                                                     sectionName=
		                                                     'ConnSect-1')
		# Save by Madina on 2020_03_18-00.33.11; build 6.14-2 2014_08_22-20.00.46 134497
		
		mdb.models['Model-1'].sections['ConnSect-1'].setValues(behaviorOptions=(
			ConnectorPlasticity(isotropic=OFF,kinematic=ON,isotropicTable=((0.0,0.0,
			                                                                0.0),),
			                    kinematicTable=((4.091917,2.0),(8.18394,13.0),(12.27591,
			                                                                   42.0),(14.73109,73.0),
			                                    (16.36788,100.0)),
			                    components=(1,)),))
		# Save by Madina on 2020_03_18-16.59.08; build 6.14-2 2014_08_22-20.00.46 134497
		
		mdb.models['Model-1'].materials['Material-1'].Conductivity(table=((2.0,),))
		mdb.models['Model-1'].materials['Material-1'].HeatGeneration()
		mdb.models['Model-1'].materials['Material-1'].SpecificHeat(table=((940.0,),))
		# Save by Madina on 2020_03_18-17.06.32; build 6.14-2 2014_08_22-20.00.46 134497
		the_job.writeInput()
		input_filepath=os.path.join(settings.abaqus_workdir,the_job.name+'.inp')
		print(input_filepath)
		
		return self

def main():
	model_1=Modeller().build()

if __name__=='__main__':
	if settings.is_run_by_abaqus:
		print('Running the script in Abaqus...')
		
		from abaqute.common.red_deflector import *
		
		main()
	else:
		from abaqute.abaqus_runner.main import model_2
		savedir=os.curdir
		os.chdir(settings.abaqus_workdir)
		settings.run_script(__file__)
		os.chdir(savedir)
		model_2()
		
	print('Done.')
