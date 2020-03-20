import numpy as np

class Params:
	
	def __init__(self,target_depth=7000):
		self.unit_weight=0.000018
		self.friction_angle=30
		self.soil_pile_angle=self.friction_angle-5
		self.k_lateral=0.5
		self.mu=self.k_lateral*np.tan(self.soil_pile_angle*np.pi/180)
		self.pile_dia=1000
		self.pile_dia_in=200
		self.k_stiffness=0.0244
		self.a_cyclic=0.88
		self.curve_c1=1.8705
		self.curve_c2=2.616
		self.curve_c3=29.65
		self.curve_pu_s=(
				                self.curve_c1*target_depth+self.curve_c2*self.pile_dia)*self.unit_weight*target_depth
		self.curve_pu_d=self.curve_c3*self.pile_dia*self.unit_weight*target_depth
		self.curve_pu_min=np.min([self.curve_pu_s,self.curve_pu_d],axis=0)
		self.sigma_h=self.k_lateral*self.unit_weight*target_depth

def get_stiffness(target_depth):
	params=Params(target_depth)
	y_gap=(np.arctanh((params.sigma_h*params.pile_dia)/(params.a_cyclic*params.curve_pu_min)))/(
			(params.k_stiffness*target_depth)/(params.a_cyclic*params.curve_pu_min))
	return params.sigma_h/y_gap

def get_gap(target_depth):
	params=Params(target_depth)
	y_gap=(np.arctanh((params.sigma_h*params.pile_dia)/(params.a_cyclic*params.curve_pu_min)))/(
			(params.k_stiffness*target_depth)/(params.a_cyclic*params.curve_pu_min))
	output=np.column_stack((params.sigma_h,y_gap))  #todo: OPASYAN
	output_as_tuple=tuple([tuple(x) for x in output])
	return output_as_tuple

def get_target_depth(coor,pile_length=6000,pile_part_offset=1000,pile_coor_offset=-3000):
	target_depth=pile_length-coor+pile_part_offset+pile_coor_offset
	return target_depth

def get_py_curve(coors,decimals=6):
	target_depths=get_target_depth(coors)
	py_curve=get_gap(target_depths)
	out=np.round(py_curve,decimals=decimals)
	# sorted_out = out[out[:, 0].argsort()]
	return out
