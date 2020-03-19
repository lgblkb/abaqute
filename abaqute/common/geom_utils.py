import numpy as np

class ThePoint2D(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.v=np.array([self.x,self.y])
		self._tuple=None
	
	# @property
	# def v(self):
	# 	if self._v is None: self._v=np.array([self.x,self.y])
	# 	return self._v
	
	@property
	def tup(self):
		if self._tuple is None: self._tuple=tuple(self.v)
		return self._tuple
	
	def _make_operation(self,other,oper_func):
		if isinstance(other,ThePoint2D):
			other_coors=other.v
		elif type(other) is tuple:
			other_coors=other
		else:
			raise NotImplementedError()
		args=[oper_func(*x) for x in zip(self.v,other_coors)]
		return self.__class__(*args)
	
	def __add__(self,other):
		return self._make_operation(other,lambda x,y:x+y)
	
	def __radd__(self,other):
		return self._make_operation(other,lambda x,y:x+y)
	
	def __sub__(self,other):
		return self._make_operation(other,lambda x,y:x-y)
	
	def __rsub__(self,other):
		return self._make_operation(other,lambda x,y:y-x)
	
	def __str__(self):
		return self.tup
	
	def __repr__(self):
		return self.tup

class ThePoint3D(ThePoint2D):
	def __init__(self,x,y,z):
		super(ThePoint3D,self).__init__(x,y,)
		self.z=z
		self.v=np.array([self.x,self.y,self.z])
