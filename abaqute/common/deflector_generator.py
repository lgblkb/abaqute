from __future__ import absolute_import,print_function

template_code=r"""from __future__ import absolute_import,print_function

### This file is generated automatically.
### Any changes will be lost!!!
### Instead, modify deflector_generator.py

# noinspection PyUnresolvedReferences
from abaqute.common.abaqus_imports import {0}

{0}={0}
"""

import_names=[
	'mdb',
	'OFF',
	'ON',
	'THREE_D',
	'DEFORMABLE_BODY',
	'MIDDLE_SURFACE',
	'FROM_SECTION',
	'CARTESIAN',
	'SOLVER_DEFAULT',
	'STEP',
	'UNSET',
	'UNIFORM',
	'SINGLE',
	'PERCENTAGE',
	'DEFAULT',
	'DOMAIN',
	'ODB',
	'ANALYSIS',
	'RIGHT',
	'CLOCKWISE',
	'COUNTERCLOCKWISE',
	'LEFT',
	'WIRE',
	'GLOBAL',
	'HARD',
	'SELF',
	'ISOTROPIC',
	'PENALTY',
	'FRACTION',
	'SET',
	'Region',
	'MPI',
	'MEDIAL_AXIS',
	'HEX',
]

if __name__=='__main__':
	generated_code=template_code.format(','.join(import_names))
	filepath='red_deflector.py'
	with open(filepath,'w') as fh:
		fh.write(generated_code)
	print(filepath+' successfully generated.')
