from __future__ import absolute_import,print_function
from abaqute import settings
import os
from abaqute.common.geom_utils import ThePoint2D,ThePoint3D
import collections
import functools

settings.update_sys_path()

class Modeller(object):
	
	def build(self):
		
		model_1=mdb.models['Model-1']
		model_1.rootAssembly.DatumCsysByDefault(CARTESIAN)
		sketch_filepath=r'C:\Users\lgblkb\Desktop\Tunnel/TunnelCrossSection.iges'
		mdb.openIges(sketch_filepath,msbo=0,scaleFromFile=OFF,topology=WIRE,trimCurve=DEFAULT,uniteWires=OFF)
		the_sketch=model_1.ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis,name='Tunnel_CrossSection',scale=1.0)
		sketch_profile=model_1.ConstrainedSketch(name='__profile__',sheetSize=10.0)
		sketch_profile.retrieveSketch(sketch=the_sketch)
		part_1=model_1.Part(dimensionality=THREE_D,name='Part-1',type=DEFORMABLE_BODY)
		part_1.BaseSolidExtrude(depth=12.0,sketch=sketch_profile)
		del model_1.sketches['__profile__']
		# return
		instances=list()
		for instance_i in range(4):
			instance=model_1.rootAssembly.Instance(dependent=OFF,name='Part-1-{}'.format(instance_i+1),part=part_1)
			model_1.rootAssembly.translate(instanceList=(instance.name,),vector=ThePoint3D(0,0,float(instance_i)*(12+1e-3)).tup)
			instances.append(instance)
		#
		int_prop=model_1.ContactProperty('IntProp-1')
		int_prop.NormalBehavior(allowSeparation=ON,constraintEnforcementMethod=DEFAULT,pressureOverclosure=HARD)
		int_prop.TangentialBehavior(dependencies=0,directionality=ISOTROPIC,elasticSlipStiffness=None,
		                            formulation=PENALTY,fraction=0.005,maximumElasticSlip=FRACTION,
		                            pressureDependency=OFF,shearStressLimit=None,slipRateDependency=OFF,
		                            table=((0.4,),),temperatureDependency=OFF)
		initial_step_name='Initial'
		interaction=model_1.ContactStd(createStepName=initial_step_name,name='Int-1')
		interaction.includedPairs.setValuesInStep(stepName=initial_step_name,useAllstar=ON)
		interaction.contactPropertyAssignments.appendInStep(assignments=((GLOBAL,SELF,int_prop.name),),stepName=initial_step_name)
		
		step_1=model_1.StaticStep(maxNumInc=500,name='Step-1',previous=initial_step_name)
		regions=functools.reduce(lambda a,b:a+b,[instance.cells.getSequenceFromMask(mask=('[#1 ]',),) for instance in instances])
		# regions=instances[0].cells.getSequenceFromMask(mask=('[#1 ]',),)
		# print('regions: ',regions)
		model_1.rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS,elemShape=HEX,regions=regions)
		print('Done setMeshControls')
		model_1.rootAssembly.seedPartInstance(deviationFactor=0.1,minSizeFactor=0.1,regions=tuple(instances),size=0.2)
		print('Done setMeshControls')
		model_1.rootAssembly.generateMesh(regions=regions)
		print('Done generateMesh')
		# return
		# model_1.rootAssembly.seedPartInstance(deviationFactor=0.1,minSizeFactor=0.1,regions=tuple(instances),size=0.2)
		# model_1.rootAssembly.generateMesh(regions=tuple(instances))
		# allNodes=model_1.rootAssembly.nodes
		# position=ThePoint3D(0,0,0)
		# expanded=ThePoint3D(20,20,10)
		# xmin,ymin,zmin=(position-expanded).tup
		# # print(xmin,ymin,zmin)
		# xmax,ymax,zmax=(position+expanded).tup
		# # print(xmax,ymax,zmax)
		# myNodes=allNodes.getByBoundingBox(xmin,ymin,zmin,xmax,ymax,zmax)
		# print('myNodes: ',myNodes)
		
		# instances[-1].Set('facename',faces=instances[-1].faces.findAt(((1,0,0),),))
		return
		
		print('Creating set 1')
		bottom_nodes=(27,28,57,58,59,60,61,62,63,82,87,88,89,90,91,
		              92,93,94,156,157,186,187,188,189,190,191,192,211,216,217,
		              218,219,220,221,222,223,285,286,315,316,317,318,319,320,321,
		              340,345,346,347,348,349,350,351,352,414,415,444,445,446,447,
		              448,449,450,469,474,475,476,477,478,479,480,481,543,544,573,
		              574,575,576,577,578,579,598,603,604,605,606,607,608,609,610,
		              672,673,702,703,704,705,706,707,708,727,732,733,734,735,736,
		              737,738,739,801,802,831,832,833,834,835,836,837,856,861,862,
		              863,864,865,866,867,868,930,931,960,961,962,963,964,965,966,
		              985,990,991,992,993,994,995,996,997,1059,1060,1089,1090,1091,
		              1092,1093,1094,1095,1114,1119,1120,1121,1122,1123,1124,1125,
		              1126,1188,1189,1218,1219,1220,1221,1222,1223,1224,1243,1248,
		              1249,1250,1251,1252,1253,1254,1255,1317,1318,1347,1348,1349,
		              1350,1351,1352,1353,1372,1377,1378,1379,1380,1381,1382,1383,
		              1384,1446,1447,1476,1477,1478,1479,1480,1481,1482,1501,1506,
		              1507,1508,1509,1510,1511,1512,1513,1575,1576,1605,1606,1607,
		              1608,1609,1610,1611,1630,1635,1636,1637,1638,1639,1640,1641,
		              1642,1704,1705,1734,1735,1736,1737,1738,1739,1740,1759,1764,
		              1765,1766,1767,1768,1769,1770,1771,1833,1834,1863,1864,1865,
		              1866,1867,1868,1869,1888,1893,1894,1895,1896,1897,1898,1899,
		              1900,1962,1963,1992,1993,1994,1995,1996,1997,1998,2017,2022,
		              2023,2024,2025,2026,2027,2028,2029,2091,2092,2121,2122,2123,
		              2124,2125,2126,2127,2146,2151,2152,2153,2154,2155,2156,2157,
		              2158,2220,2221,2250,2251,2252,2253,2254,2255,2256,2275,2280,
		              2281,2282,2283,2284,2285,2286,2287)
		bottom_nodes_set=model_1.rootAssembly.SetFromNodeLabels(
			name='Set-1',nodeLabels=tuple((instance.name,bottom_nodes) for instance in instances),unsorted=True)
		
		print('Creating fixed BC')
		fixed_bc=model_1.DisplacementBC(amplitude=UNSET,createStepName=initial_step_name,
		                                distributionType=UNIFORM,fieldName='',localCsys=None,name='BC-1',
		                                region=bottom_nodes_set,u1=SET,u2=SET,u3=SET,ur1=SET,ur2=SET,ur3=SET)
		# print('Creating radial surface nodes'
		# surface_nodes=(28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,
		#                43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,83,84,85,86,
		#                157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,
		#                172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,
		#                212,213,214,215,286,287,288,289,290,291,292,293,294,295,296,
		#                297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,
		#                312,313,314,315,341,342,343,344,415,416,417,418,419,420,421,
		#                422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,
		#                437,438,439,440,441,442,443,444,470,471,472,473,544,545,546,
		#                547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,
		#                562,563,564,565,566,567,568,569,570,571,572,573,599,600,601,
		#                602,673,674,675,676,677,678,679,680,681,682,683,684,685,686,
		#                687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,
		#                702,728,729,730,731,802,803,804,805,806,807,808,809,810,811,
		#                812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,
		#                827,828,829,830,831,857,858,859,860,931,932,933,934,935,936,
		#                937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,
		#                952,953,954,955,956,957,958,959,960,986,987,988,989,1060,
		#                1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,
		#                1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,
		#                1085,1086,1087,1088,1089,1115,1116,1117,1118,1189,1190,1191,
		#                1192,1193,1194,1195,1196,1197,1198,1199,1200,1201,1202,1203,
		#                1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,
		#                1216,1217,1218,1244,1245,1246,1247,1318,1319,1320,1321,1322,
		#                1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,
		#                1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,
		#                1347,1373,1374,1375,1376,1447,1448,1449,1450,1451,1452,1453,
		#                1454,1455,1456,1457,1458,1459,1460,1461,1462,1463,1464,1465,
		#                1466,1467,1468,1469,1470,1471,1472,1473,1474,1475,1476,1502,
		#                1503,1504,1505,1576,1577,1578,1579,1580,1581,1582,1583,1584,
		#                1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,1596,
		#                1597,1598,1599,1600,1601,1602,1603,1604,1605,1631,1632,1633,
		#                1634,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,
		#                1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,
		#                1728,1729,1730,1731,1732,1733,1734,1760,1761,1762,1763,1834,
		#                1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,
		#                1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,
		#                1859,1860,1861,1862,1863,1889,1890,1891,1892,1963,1964,1965,
		#                1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,
		#                1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,
		#                1990,1991,1992,2018,2019,2020,2021,2092,2093,2094,2095,2096,
		#                2097,2098,2099,2100,2101,2102,2103,2104,2105,2106,2107,2108,
		#                2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,
		#                2121,2147,2148,2149,2150,2221,2222,2223,2224,2225,2226,2227,
		#                2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,
		#                2240,2241,2242,2243,2244,2245,2246,2247,2248,2249,2250,2276,
		#                2277,2278,2279)
		# surface_nodes_set=model_1.rootAssembly.SetFromNodeLabels(
		# 	name='Set-2',nodeLabels=tuple((instance.name,surface_nodes) for instance in instances),unsorted=True)
		print('Creating surface')
		masks=dict()
		masks[3]=('[#54a170 #0 #85c00000 #152 #0 #54a1700 #0',
		          ' #5c000000 #1528 #0 #54a17000 #0 #c0000000 #15285',
		          ' #0 #4a170000 #5 #0 #15285c #0 #a1700000',
		          ' #54 #0 #15285c0 #0 #17000000 #54a #0',
		          ' #15285c00 #0 #70000000 #54a1 #0 #5285c000 #1',
		          ' #0 #54a17 #0 #285c0000 #15 #0 #54a170 ]',)
		masks[4]=('[#f0001c08 #0 #70200000 #3c000 #0 #1c080 #f',
		          ' #2000000 #3c0007 #0 #1c0800 #f0 #20000000 #3c00070',
		          ' #0 #1c08000 #f00 #0 #3c000702 #0 #1c080000',
		          ' #f000 #0 #c0007020 #3 #c0800000 #f0001 #0',
		          ' #70200 #3c #8000000 #f0001c #0 #702000 #3c0',
		          ' #80000000 #f0001c0 #0 #7020000 #3c00 #0 #f0001c08 ]',)
		masks[5]=('[#3aa0080 #2000 #20002e0 #80000ea8 #b800000 #3aa00800 #20000',
		          ' #20002e00 #ea80 #b8000008 #aa008000 #200003 #2e000 #ea802',
		          ' #80000080 #a008000b #200003a #2e0000 #ea8020 #800 #8000b8',
		          ' #200003aa #2e00000 #ea80200 #8000 #8000b80 #3aa0 #2e000002',
		          ' #ea802000 #80000 #8000b800 #3aa00 #e0000020 #a8020002 #80000e',
		          ' #b8000 #3aa008 #200 #8020002e #80000ea #b80000 #3aa0080',
		          ' #2000 #2e0 ]',)
		masks[6]=('[#c000200 #20000 #8000000 #3000 #8 #c0002000 #200000',
		          ' #80000000 #30000 #80 #20000 #200000c #0 #300008',
		          ' #800 #200000 #200000c0 #0 #3000080 #8000 #2000000',
		          ' #c00 #2 #30000800 #80000 #20000000 #c000 #20',
		          ' #8000 #800003 #0 #c0002 #200 #80000 #8000030',
		          ' #0 #c00020 #2000 #800000 #80000300 #0 #c000200',
		          ' #20000 ]',)
		
		surface_data=dict()
		for i in [3,4,5,6]:
			elements=list()
			for instance in instances:
				elements.append(instance.elements.getSequenceFromMask(mask=masks[i],))
			surface_data['face{}Elements'.format(i)]=functools.reduce(lambda x,y:x+y,elements)
		
		surface=model_1.rootAssembly.Surface(name='Surf-1',**surface_data)
		
		print('Creating pressure load')
		pressure_load=model_1.Pressure(amplitude=UNSET,createStepName='Step-1',distributionType=UNIFORM,field='',
		                               magnitude=2e6,name='Load-1',region=surface)
		
		material2=mdb.models['Model-1'].Material(name='Material-2')
		material2.Elastic(table=((36.43e9,0.19),))
		# cdp=material2.ConcreteDamagedPlasticity(table=((30.0,0,0,0.0,0.0),))
		#
		# cdp.ConcreteCompressionHardening(
		# 	table=((15000000.0,0.0),
		# 	       (20200000.0,7.5e-05),
		# 	       (30000000.0,9.9e-05),
		# 	       (40300000.0,0.000154),
		# 	       (50000000.0,0.000762),
		# 	       (40200000.0,0.002558),
		# 	       (20200000.0,0.005675)))
		# cdp.ConcreteTensionStiffening(
		# 	table=((2842000.0,0.0),
		# 	       (1869810.0,0.0001160481922),
		# 	       (862723.0,0.0002592867922),
		# 	       (226254.0,0.0006792229984)))
		
		model_1.HomogeneousSolidSection(material=material2.name,name='Section-1',thickness=None)
		part_1.SectionAssignment(offset=0.0,offsetField='',offsetType=MIDDLE_SURFACE,region=Region(
			cells=part_1.cells.getSequenceFromMask(mask=('[#1 ]',),)),sectionName='Section-1',thicknessAssignment=FROM_SECTION)
		model_1.rootAssembly.regenerate()
		job_1=mdb.Job(atTime=None,contactPrint=OFF,description='',echoPrint=OFF,
		              explicitPrecision=SINGLE,getMemoryFromAnalysis=True,historyPrint=OFF,
		              memory=90,memoryUnits=PERCENTAGE,model=model_1.name,modelPrint=OFF,
		              multiprocessingMode=MPI,name='Job-1',nodalOutputPrecision=SINGLE,
		              numCpus=8,numDomains=8,numGPUs=1,queue=None,resultsFormat=ODB,scratch='',
		              type=ANALYSIS,userSubroutine='',waitHours=0,waitMinutes=0)
		job_1.submit(consistencyChecking=OFF)
		return self

def main():
	model_1=Modeller().build()

if __name__=='__main__':
	if settings.is_run_by_abaqus:
		print('Running the script in Abaqus...')
		
		from abaqute.common.red_deflector import *
		
		main()
	else:
		savedir=os.curdir
		os.chdir(settings.abaqus_workdir)
		settings.run_script(__file__)
		os.chdir(savedir)
	print('Done.')
