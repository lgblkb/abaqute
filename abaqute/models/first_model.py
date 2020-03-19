from __future__ import absolute_import
from abaqute.common.geom_utils import ThePoint2D
from abaqute import settings

settings.update_sys_path()

class Modeller(object):
	
	def build(self):
		model=mdb.models['Model-1']
		
		tunnel_center=ThePoint2D(0,0)
		tunnel_radius=6
		tunnel_length=12
		wall_thickness=1.1
		
		point_1=tunnel_center-(tunnel_radius,0)
		point_2=tunnel_center+(tunnel_radius,0)
		profile=model.ConstrainedSketch(name='tunnel_profile',sheetSize=200.0)
		
		tunnel_arc=profile.ArcByCenterEnds(center=tunnel_center(),direction=CLOCKWISE,point1=point_1(),point2=point_2())
		tunnel_base=profile.Line(point1=point_1(),point2=point_2())
		
		profile.offset(distance=wall_thickness,objectList=(tunnel_arc,tunnel_base),side=LEFT)
		
		tunnel_part=model.Part(dimensionality=THREE_D,name='tunnel_part',type=DEFORMABLE_BODY)
		tunnel_part.BaseSolidExtrude(depth=tunnel_length,sketch=profile)
		del profile
		
		rc_material=model.Material(name='rc-material')
		rc_material.Elastic(table=((210000000000.0,0.3),))
		
		section=model.HomogeneousSolidSection(material=rc_material.name,name='Section-1',thickness=None)
		model.rootAssembly.DatumCsysByDefault(CARTESIAN)
		assembly_instance=model.rootAssembly.Instance(dependent=OFF,name='tunnel_part-1',part=tunnel_part)
		model.StaticStep(description='some step description',initialInc=7.0,maxInc=7.0,minInc=7e-05,name='Step-1',
		                 previous='Initial',timePeriod=7.0)
		
		
		
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
