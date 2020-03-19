# encoding: utf-8
# module docstringLookupTable
# from C:\SIMULIA\CAE\2019\win_b64\code\python2.7\lib\docstringLookupTable.pyc
# by generator 1.147
# no doc
# no imports

# no functions
# no classes
# variables with complex values

methodDocstringTable={
	'AVIOptions.setValues':(
		'<compressionMethod, compressionQuality, codecOptions, sizeDefinition, imageSize>',
		'This method modifies the AVIOptions object.',
	),
	'Abaqus.Mdb':(
		'<pathName>',
		'This constructor creates an empty \n Mdb\n object.\n ',
	),
	'Abaqus.importDxf':(
		'fileName',
		'This method creates a \n ConstrainedSketch\n object from a file containing dxf-format (AutoCAD) geometry. Only a limited number of entities are supported. This format should be used only if no other formats are available.\n ',
	),
	'Abaqus.openAcis':(
		'fileName <, scaleFromFile>',
		'This method creates an \n AcisFile\n object from a file containing ACIS-format geometry. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'Abaqus.openCatia':(
		'fileName <, topology, convertUnits, combineBodies>',
		'This method creates an \n AcisFile\n object from a file containing \n CATIA\n V4-format or V5&#8211;format geometry. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'Abaqus.openEnf':(
		'fileName, fileType <, topology, convertUnits>',
		'This method creates an\n AcisFile\n object from a file containing Elysium Neutral File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'Abaqus.openIges':(
		'fileName <, trimCurve, scaleFromFile, msbo, includedLayers, topology, uniteWires>',
		'This method creates an \n AcisFile\n object from a file containing IGES-format geometry. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'Abaqus.openMdb':(
		'pathName',
		'This method opens an existing model database file.',
	),
	'Abaqus.openParasolid':(
		'fileName <, topology>',
		'This method creates an\n AcisFile\n object from a file containing Parasolid-format geometry. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'Abaqus.openStep':(
		'fileName <, scale>',
		'This method creates an \n AcisFile\n object from a file containing STEP-format geometry. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'Abaqus.openVda':(
		'fileName',
		'This method creates an \n AcisFile\n object from a file containing VDA-FS-format geometry. This object is subsequently used by the \n PartFromGeometryFile\n method.\n ',
	),
	'AccelerationBC.setValues':(
		'',
		'',
	),
	'AccelerationBC.setValuesInStep':(
		'stepName <, a1, a2, a3, ar1, ar2, ar3, amplitude>',
		'This method modifies the propagating data for an existing AccelerationBC object in the specified step.',
	),
	'AccelerationBaseMotionBC.setValues':'<value is a self-reference, replaced by this string>',
	'AccelerationBaseMotionBC.setValuesInStep':(
		'stepName <, amplitude>',
		'This method modifies the propagating data for an existing AccelerationBaseMotionBC object in the specified step.',
	),
	'AcisFile.writeAcisFile':(
		'fileName <, version>',
		'This method exports the assembly to a named file in ACIS format.',
	),
	'AcousticImpedance.setValues':'<value is a self-reference, replaced by this string>',
	'AcousticImpedance.setValuesInStep':(
		'stepName <, interactionProperty>',
		'This method modifies the propagating data for an existing AcousticImpedance object in the specified step.',
	),
	'AcousticImpedanceProp.setValues':'<value is a self-reference, replaced by this string>',
	'AcousticInfiniteSection.setValues':'<value is a self-reference, replaced by this string>',
	'AcousticInterfaceSection.setValues':'<value is a self-reference, replaced by this string>',
	'AcousticMedium.setValues':'<value is a self-reference, replaced by this string>',
	'AcousticPressureBC.setValues':'<value is a self-reference, replaced by this string>',
	'AcousticPressureBC.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing AcousticPressureBC object in the specified step.',
	),
	'ActuatorAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'ActuatorSensor.setValues':'<value is a self-reference, replaced by this string>',
	'ActuatorSensorProp.setValues':'<value is a self-reference, replaced by this string>',
	'AdaptiveMeshConstraint.deactivate':(
		'stepName',
		'This method deactivates the adaptive mesh constraint in the specified step and all subsequent steps.',
	),
	'AdaptiveMeshConstraint.delete':(
		'indices',
		' This method allows you to delete existing adaptive mesh constraints.\n      ',
	),
	'AdaptiveMeshConstraint.move':(
		'fromStepName, toStepName',
		'This method moves the adaptive mesh constraint state from one step to a different step.',
	),
	'AdaptiveMeshConstraint.reset':(
		'stepName',
		'This method resets the adaptive mesh constraint state of the specified step to the state of the previous analysis step.',
	),
	'AdaptiveMeshConstraint.resume':(
		'',
		'This method resumes the adaptive mesh constraint that was previously suppressed.',
	),
	'AdaptiveMeshConstraint.suppress':(
		'',
		'This method suppresses the adaptive mesh constraint.',
	),
	'AdaptiveMeshControl.setValues':'<value is a self-reference, replaced by this string>',
	'AdaptiveMeshDomain.setValues':'<value is a self-reference, replaced by this string>',
	'AdaptivityIteration.RuleResult':(
		'name, indicatorResults, numElems, minSizeElemCount <, satisfiedVars>',
		'This method creates a RuleResult with data for a RemeshingRule for a given adaptivity iteration.',
	),
	'AdaptivityProcess.AdaptivityIteration':(
		'iteration, jobName, modelName, odbPath, remeshingErrors',
		'This method creates an AdaptivityIteration object.',
	),
	'AdaptivityProcess.setValues':'<value is a self-reference, replaced by this string>',
	'AdaptivityProcess.submit':(
		'<waitForCompletion, datacheckJob, continueJob>',
		'This method begins the process of analysis and adaptive remeshing.',
	),
	'AdjustPoints.setValues':'<value is a self-reference, replaced by this string>',
	'AnimationController.decrementFrame':(
		'',
		'This method decrements the animation frame.',
	),
	'AnimationController.incrementFrame':(
		'',
		'This method increments the animation frame.',
	),
	'AnimationController.play':(
		'<duration>',
		'This method begins the animation.',
	),
	'AnimationController.setValues':(
		'<animationType, viewports>',
		'This method modifies the AnimationController object.',
	),
	'AnimationController.showFirstFrame':(
		'',
		'This method renders the first frame of the animation.',
	),
	'AnimationController.showFrame':(
		'<frame, value>',
		'This method renders the specified frame of the animation.',
	),
	'AnimationController.showLastFrame':(
		'',
		'This method renders the last frame of the animation.',
	),
	'AnimationController.stop':(
		'',
		'This method stops the animation.',
	),
	'AnimationOptions.setValues':(
		'<mode, frameRate, frameCounter, relativeScaling, numScaleFactorFrames, timeHistoryMode, maxTime, maxTimeAutoCompute, minTime, minTimeAutoCompute, timeIncrement, xyUseHighlightMethod, xyShowLine, xyLineStyle, xyLineThickness, xyLineColor, xyShowSymbol, xySymbolMarker, xySymbolSize, xySymbolColor>',
		'This method modifies the AnimationOptions object.',
	),
	'AnnealStep.setValues':'<value is a self-reference, replaced by this string>',
	'AnnealTemperature.setValues':'<value is a self-reference, replaced by this string>',
	'Annotation.bringForward':(
		'',
		'This method brings the \n Annotation\n object one position up in the annotation stack.\n ',
	),
	'Annotation.bringToFront':(
		'',
		'This method brings the \n Annotation\n object to the top of the annotation stack.\n ',
	),
	'Annotation.moveAfter':(
		'name',
		'This method moves the \n Annotation\n object after another object in the same repository.\n ',
	),
	'Annotation.moveBefore':(
		'name',
		'This method moves the \n Annotation\n object before another object in the same repository.\n ',
	),
	'Annotation.sendBackward':(
		'',
		'This method sends the \n Annotation\n object one position down in the annotation stack.\n ',
	),
	'Annotation.sendToBack':(
		'',
		'This method sends the \n Annotation\n object to the bottom of the annotation stack.\n ',
	),
	'Annotation.translate':(
		'<x, y>',
		'This method translates the \n Annotation\n object on the viewport plane.\n ',
	),
	'AnnotationsToPlotArray.bringForward':(
		'index',
		'This method brings the \n Annotation\n object one position forward in the \n AnnotationsToPlotArray\n sequence.\n ',
	),
	'AnnotationsToPlotArray.bringToFront':(
		'index',
		'This method brings the \n Annotation\n object to the beginning of the \n AnnotationsToPlotArray\n sequence.\n ',
	),
	'AnnotationsToPlotArray.moveAfter':(
		'index, other',
		'This method moves the \n Annotation\n object after another object in the same \n AnnotationsToPlotArray\n sequence.\n ',
	),
	'AnnotationsToPlotArray.moveBefore':(
		'index, other',
		'This method moves the \n Annotation\n object before another object in the same \n AnnotationsToPlotArray\n sequence.\n ',
	),
	'AnnotationsToPlotArray.sendBackward':(
		'index',
		'This method sends the \n Annotation\n object one position backward in the \n AnnotationsToPlotArray\n sequence.\n ',
	),
	'AnnotationsToPlotArray.sendToBack':(
		'index',
		'This method sends the \n Annotation\n object to the end of the \n AnnotationsToPlotArray\n sequence.\n ',
	),
	'ArbitraryProfile.setValues':'<value is a self-reference, replaced by this string>',
	'Area.setValues':(
		'<area, style, border, positionMethod, alignment, sizeMethod, originOffset, widthScale, heightScale, inset, pl, pr, pt, pb>',
		'This method modifies the Area object.',
	),
	'AreaStyle.setValues':(
		'<color, fill, style>',
		'This method modifies the AreaStyle object.',
	),
	'Arrow.setValues':'<value is a self-reference, replaced by this string>',
	'Arrow.translateEndPoint':(
		'<x, y>',
		'This method translates the end point of the \n Arrow\n object on the viewport plane.\n ',
	),
	'Arrow.translateStartPoint':(
		'<x, y>',
		'This method translates the start point of the \n Arrow\n object on the viewport plane.\n ',
	),
	'AssembledFastener.setValues':'<value is a self-reference, replaced by this string>',
	'Assembly.AttachmentLines':(
		'name, points, sourceFaces, sourceElementFaces, targetFaces, targetElementFaces <, projectionMethod, projectionDirStartPt, projectionDirEndPt, sourceToTargetProjMethod, numProjections, projectionDistance, flipSourceToTargetDirection, setName>',
		'This method creates a Feature object by creating attachment lines between the given set of source and target faces. The given points are first projected onto the source faces using the specified projection method. The points are then projected normal to the source faces onto the target faces. The user can specify the number of projections or the length of projection vector for projection onto the target faces. The lines are then created between the source face and the closest target face. Subsequent lines are created between the target faces. ',
	),
	'Assembly.AttachmentPoints':(
		'name, points <, projectionMethod, projectOnFaces, projectOnElementFaces, projectionDirStartPt, projectionDirEndPt, setName>',
		'This method creates an attachment points Feature. Attachment points may be created using datum points, vertices, reference points, attachment points, interesting points, orphan mesh nodes or coordinates. Optionally, the attachment points can be projected on geometric faces or element faces.',
	),
	'Assembly.AttachmentPointsAlongDirection':(
		'name, startPoint, pointCreationMethod <, endPoint, direction, spacing, numPtsAlongDir, numPtsBetweenPts, createPtAtStartPt, createPtAtEndPt, projectionMethod, projectOnFaces, projectOnElementFaces, projectionDirStartPt, projectionDirEndPt, flipDirection, setName>',
		'This method creates a Feature object by creating attachment points along a direction or between two points. A Datum point, a Vertex, a Reference point, an Attachment point, an Interesting point, or an orphan mesh Node can be specified as the start or end point. The direction can be specified using a straight edge or a datum axis. ',
	),
	'Assembly.AttachmentPointsOffsetFromEdges':(
		'name, edges <, startPoint, flipDirection, pointCreationMethod, numberOfPoints, spacingBetweenPoints, offsetFromStartPoint, offsetFromEndPoint, spacingMethod, patterningMethod, referenceFace, startPointForPatternDirection, endPointForPatternDirection, offsetFromEdges, numberOfRows, spacingBetweenRows, projectionMethod, projectOnFaces, projectOnElementFaces, projectionDirStartPt, projectionDirEndPt, setName>',
		'This method creates a Feature object by creating attachment points along or offset from one or more connected edges. ',
	),
	'Assembly.Coaxial':(
		'movableAxis, fixedAxis, flip',
		'This method moves an instance so that its selected face is coaxial with the selected face of a fixed instance.',
	),
	'Assembly.CoincidentPoint':(
		'movablePoint, fixedPoint',
		'This method moves an instance so that a specified point is coincident with a specified point of a fixed instance.',
	),
	'Assembly.ConnectorOrientation':(
		'region <, localCsys1, axis1, angle1, orient2sameAs1, localCsys2, axis2, angle2>',
		'This method creates a ConnectorOrientation object.',
	),
	'Assembly.DatumAxisByCylFace':(
		'face',
		'This method creates a Feature object and a DatumAxis object along the axis of a cylinder or cone.',
	),
	'Assembly.DatumAxisByNormalToPlane':(
		'plane, point',
		'This method creates a Feature object and a DatumAxis object normal to the specified plane and passing through the specified point.',
	),
	'Assembly.DatumAxisByParToEdge':(
		'edge, point',
		'This method creates a Feature object and a DatumAxis object parallel to the specified edge and passing through the specified point.',
	),
	'Assembly.DatumAxisByPrincipalAxis':(
		'principalAxis',
		'This method creates a Feature object and a DatumAxis object along one of the three principal axes.',
	),
	'Assembly.DatumAxisByRotation':(
		'line, point, angle',
		'This method creates a Feature object and a DatumAxis object in a two-dimensional model by rotating a line about the specified point through the specified angle.',
	),
	'Assembly.DatumAxisByThreePoint':(
		'point1, point2, point3',
		'This method creates a Feature object and a DatumAxis object normal to the circle described by three points and through its center.',
	),
	'Assembly.DatumAxisByThruEdge':(
		'edge',
		'This method creates a Feature object and a DatumAxis object along the specified edge.',
	),
	'Assembly.DatumAxisByTwoPlane':(
		'plane1, plane2',
		'This method creates a Feature object and a DatumAxis object at the intersection of two planes.',
	),
	'Assembly.DatumAxisByTwoPoint':(
		'point1, point2',
		'This method creates a Feature object and a DatumAxis object along the line joining two points.',
	),
	'Assembly.DatumCsysByDefault':(
		'coordSysType <, name>',
		'This method creates a Feature object and a DatumCsys object from the specified default coordinate system at the origin.',
	),
	'Assembly.DatumCsysByOffset':(
		'coordSysType, datumCoordSys, vector, point <, name>',
		'This method creates a Feature object and a DatumCsys object by offsetting the origin of an existing datum coordinate system to a specified point.',
	),
	'Assembly.DatumCsysByThreePoints':(
		'coordSysType, origin, point1, point2, line1, line2 <, name>',
		'This method creates a Feature object and a DatumCsys object from three points.',
	),
	'Assembly.DatumCsysByTwoLines':(
		'coordSysType, line1, line2 <, name>',
		'This method creates a Feature object and a DatumCsys object from two orthogonal lines. The origin of the new datum coordinate system is placed at the intersection of the two lines.',
	),
	'Assembly.DatumPlaneByLinePoint':(
		'line, point',
		'This method creates a Feature object and a DatumPlane object that pass through the specified line and through the specified point that does not lie on the line.',
	),
	'Assembly.DatumPlaneByOffset':(
		'plane, point',
		'This method creates a Feature object and a DatumPlane object offset from an existing plane and passing through the specified point.',
	),
	'Assembly.DatumPlaneByPointNormal':(
		'point, normal',
		'This method creates a Feature object and a DatumPlane object normal to the specified line and running through the specified point.',
	),
	'Assembly.DatumPlaneByPrincipalPlane':(
		'principalPlane, offset',
		'This method creates a Feature object and a DatumPlane object through the origin along one of the three principal planes.',
	),
	'Assembly.DatumPlaneByRotation':(
		'plane, axis, angle',
		'This method creates a Feature object and a DatumPlane object by rotating a plane about the specified axis through the specified angle.',
	),
	'Assembly.DatumPlaneByThreePoints':(
		'point1, point2, point3',
		'This method creates a Feature object and a DatumPlane object defined by passing through three points.',
	),
	'Assembly.DatumPlaneByTwoPoint':(
		'point1, point2',
		'This method creates a Feature object and a DatumPlane object midway between two points and normal to the line connecting the points.',
	),
	'Assembly.DatumPointByCoordinate':(
		'coords',
		'This method creates a Feature object and a DatumPoint object at the point defined by the specified coordinates.',
	),
	'Assembly.DatumPointByEdgeParam':(
		'edge, parameter',
		'This method creates a Feature object and a DatumPoint object along an edge at a selected distance from one end of the edge.',
	),
	'Assembly.DatumPointByMidPoint':(
		'point1, point2',
		'This method creates a Feature object and a DatumPoint object midway between two points.',
	),
	'Assembly.DatumPointByOffset':(
		'point, vector',
		'This method creates a Feature object and a DatumPoint object offset from an existing point by a vector.',
	),
	'Assembly.DatumPointByOnFace':(
		'face, edge1, offset1, edge2, offset2',
		'This method creates a Feature object and a DatumPoint object on the specified face, offset from two edges.',
	),
	'Assembly.DatumPointByProjOnEdge':(
		'point, edge',
		'This method creates a Feature object and a DatumPoint object along an edge by projecting an existing point along the normal to the edge.',
	),
	'Assembly.DatumPointByProjOnFace':(
		'point, face',
		'This method creates a Feature object and a DatumPoint object on a specified face by projecting an existing point onto the face.',
	),
	'Assembly.DiscreteFieldByVolumeFraction':(
		'name, eulerianInstance, referenceInstance <, accuracy, materialLocation, description, scaleFactor>',
		'This method creates a DiscreteField object that represents the volume fraction of each element of an Eulerian Instance that is occupied by a reference instance.',
	),
	'Assembly.EdgeToEdge':(
		'movableAxis, fixedAxis, flip, clearance',
		'This method moves an instance so that its edge is parallel to an edge of a fixed instance.',
	),
	'Assembly.FaceToFace':(
		'movablePlane, fixedPlane, flip, clearance',
		'This method moves an instance so that its face is coincident with a face of a fixed instance.',
	),
	'Assembly.Instance':(
		'name, part <, autoOffset, dependent>',
		'This method creates a PartInstance object and puts it into the instances repository.',
	),
	'Assembly.InstanceFromBooleanCut':(
		'name, instanceToBeCut, cuttingInstances <, originalInstances>',
		'This method creates a PartInstance in the instances repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance.',
	),
	'Assembly.InstanceFromBooleanMerge':(
		'name, instances <, keepIntersections, originalInstances, domain, mergeNodes, nodeMergingTolerance, removeDuplicateElements>',
		'This method creates a PartInstance in the instances repository after merging two or more part instances.',
	),
	'Assembly.LinearInstancePattern':(
		'instanceList, number1, spacing1, number2, spacing2 <, direction1, direction2>',
		'This method creates multiple PartInstance objects in a linear pattern and puts them into the instances repository.',
	),
	'Assembly.MakeSketchTransform':(
		'sketchPlane <, origin, sketchOrientation, sketchPlaneSide, sketchUpEdge>',
		' This method creates a Transform object. A Transform object is a 4x3 matrix of Floats that represents the transformation from sketch coordinates to part coordinates.',
	),
	'Assembly.ParallelCsys':(
		'movableCsys, fixedCsys',
		'This method moves an instance so that its Datum coordinate system is parallel to a Datum coordinate system of a fixed instance.',
	),
	'Assembly.ParallelEdge':(
		'movableAxis, fixedAxis, flip',
		'This method moves an instance so that its edge is parallel to an edge of a fixed instance.',
	),
	'Assembly.ParallelFace':(
		'movablePlane, fixedPlane, flip',
		'This method moves an instance so that its face is parallel to a face of a fixed instance.',
	),
	'Assembly.PartFromBooleanCut':(
		'name, instanceToBeCut, cuttingInstances',
		'This method creates a Part in the parts repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance.',
	),
	'Assembly.PartFromBooleanMerge':(
		'name, instances <, keepIntersections, mergeNodes, nodeMergingTolerance, removeDuplicateElements, domain>',
		'This method creates a Part in the parts repository after merging two or more part instances. The part instances can be either Abaqus native parts or orphan mesh parts, but they cannot be a combination of both.',
	),
	'Assembly.PartFromInstanceMesh':(
		'name <, partInstances, copyPartSets, copyAssemblySets>',
		'This method creates a Part object containing the mesh found in the supplied PartInstance objects and places the new Part object in the parts repository.',
	),
	'Assembly.PartitionCellByDatumPlane':(
		'cells, datumPlane',
		'This method partitions one or more cells using the given datum plane.',
	),
	'Assembly.PartitionCellByExtendFace':(
		'cells, extendFace',
		'This method partitions one or more cells by extending the underlying geometry of a given face to partition the target cells.',
	),
	'Assembly.PartitionCellByExtrudeEdge':(
		'cells, edges, line, sense',
		'This method partitions one or more cells by extruding selected edges in the given direction.',
	),
	'Assembly.PartitionCellByPatchNCorners':(
		'cell, cornerPoints',
		'This method partitions a cell using an N-sided cutting patch defined by the given corner points.',
	),
	'Assembly.PartitionCellByPatchNEdges':(
		'cell, edges',
		'This method partitions a cell using an N-sided cutting patch defined by the given edges.',
	),
	'Assembly.PartitionCellByPlaneNormalToEdge':(
		'cells, edge, point',
		'This method partitions one or more cells using a plane normal to an edge at the given edge point.',
	),
	'Assembly.PartitionCellByPlanePointNormal':(
		'cells, point, normal',
		'This method partitions one or more cells using a plane defined by a point and a normal direction.',
	),
	'Assembly.PartitionCellByPlaneThreePoints':(
		'cells, point1, point2, point3',
		'This method partitions one or more cells using a plane defined by three points.',
	),
	'Assembly.PartitionCellBySweepEdge':(
		'cells, edges, sweepPath',
		'This method partitions one or more cells by sweeping selected edges along the given sweep path.',
	),
	'Assembly.PartitionEdgeByDatumPlane':(
		'edges, datumPlane',
		'This method partitions an edge where it intersects with a datum plane.',
	),
	'Assembly.PartitionEdgeByParam':(
		'edges, parameter',
		'This method partitions one or more edges at the given normalized edge parameter.',
	),
	'Assembly.PartitionEdgeByPoint':(
		'edge, point',
		'This method partitions an edge at the given point.',
	),
	'Assembly.PartitionFaceByAuto':(
		'face',
		'This method automatically partitions a target face into simple regions that can be meshed using a structured meshing technique.',
	),
	'Assembly.PartitionFaceByCurvedPathEdgeParams':(
		'face, edge1, parameter1, edge2, parameter2',
		'This method partitions a face normal to two edges, using a curved path between the two given edge points defined by the normalized edge parameters.',
	),
	'Assembly.PartitionFaceByCurvedPathEdgePoints':(
		'face, edge1, point1, edge2, point2',
		'This method partitions a face normal to two edges, using a curved path between the two given edge points.',
	),
	'Assembly.PartitionFaceByDatumPlane':(
		'faces, datumPlane',
		'This method partitions one or more faces using the given datum plane.',
	),
	'Assembly.PartitionFaceByExtendFace':(
		'faces, extendFace',
		'This method partitions one or more faces by extending the underlying geometry of another given face to partition the target faces.',
	),
	'Assembly.PartitionFaceByIntersectFace':(
		'faces, cuttingFaces',
		'This method partitions one or more faces using the given cutting faces to partition the target faces.',
	),
	'Assembly.PartitionFaceByProjectingEdges':(
		'faces, edges <, extendEdges>',
		'This method partitions one or more faces by projecting the given edges on the target faces.',
	),
	'Assembly.PartitionFaceByShortestPath':(
		'faces, point1, point2',
		'This method partitions one or more faces using a minimum distance path between the two given points.',
	),
	'Assembly.PartitionFaceBySketch':(
		'faces, sketch <, sketchUpEdge, sketchOrientation>',
		'This method partitions one or more planar faces by sketching on them.',
	),
	'Assembly.PartitionFaceBySketchDistance':(
		'faces, sketchPlane, sketchPlaneSide, sketchUpEdge, sketch, distance <, sketchOrientation>',
		'This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through the given distance.',
	),
	'Assembly.PartitionFaceBySketchRefPoint':(
		'faces, sketchPlane, sketchUpEdge, sketch, point <, sketchOrientation>',
		'This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through a distance governed by the reference point.',
	),
	'Assembly.PartitionFaceBySketchThruAll':(
		'faces, sketchPlane, sketchPlaneSide, sketchUpEdge, sketch <, sketchOrientation>',
		'This method partitions one or more faces by sketching on a sketch plane and then projecting toward the target faces through an infinite distance.',
	),
	'Assembly.RadialInstancePattern':(
		'instanceList, number, totalAngle <, point, axis>',
		'This method creates multiple PartInstance objects in a radial pattern and puts them into the instances repository.',
	),
	'Assembly.ReferencePoint':(
		'point <, nodeLabel, instanceName>',
		'This method creates a Feature object and a ReferencePoint object at the specified location.',
	),
	'Assembly.RemoveWireEdges':(
		'wireEdgeList',
		'This method removes wire edges.',
	),
	'Assembly.SectionAssignment':(
		'region, sectionName <, thicknessAssignment, offset, offsetType, offsetField>',
		'This method creates a SectionAssignment object.',
	),
	'Assembly.Set':(
		'name <, nodes, elements, region, vertices, edges, faces, cells, xVertices, xEdges, xFaces, referencePoints, skinFaces, skinEdges, stringerEdges>',
		'This method creates a set from a sequence of objects in a model database.',
	),
	'Assembly.SetByBoolean':(
		'name, sets <, operation>',
		'This method creates a set by performing a boolean operation on two or more input sets.',
	),
	'Assembly.SetFromElementLabels':(
		'name, elementLabels',
		'This method creates a set from a sequence of element labels in a model database.',
	),
	'Assembly.SetFromNodeLabels':(
		'name, nodeLabels',
		'This method creates a set from a sequence of node labels in a model database.',
	),
	'Assembly.Surface':(
		'name <, side1Elements, side2Elements, side12Elements, end1Elements, end2Elements, circumElements, face1Elements, face2Elements, face3Elements, face4Elements, face5Elements, face6Elements, side1Faces, side2Faces, side12Faces, side1Edges, side2Edges, end1Edges, end2Edges, circumEdges>',
		'This method creates a surface from a sequence of objects in a model database. The surface will apply to the sides specified by the arguments.',
	),
	'Assembly.SurfaceByBoolean':(
		'name, surfaces <, operation>',
		'This method creates a surface by performing a boolean operation on two or more input surfaces.',
	),
	'Assembly.SurfaceFromElsets':(
		'name, elementSetSeq',
		'This method creates a surface from a sequence of element sets in a model database.',
	),
	'Assembly.WirePolyLine':(
		'points <, mergeType, meshable>',
		'This method creates an additional Feature object by creating a series of wires joining points in pairs. When such a feature is created at the Part level, then each point can be either a datum point, a vertex, a reference point, an interesting point, an orphan mesh node, or the coordinates of a point. When such a feature is created at the Assembly level, then each point can only be a vertex, a reference point, or an orphan mesh node.',
	),
	'Assembly._generateDelTri':(
		'faceNumber',
		'This method computes the delaunay triangulation used in the first step of auto-partitioning and displays it. ',
	),
	'Assembly._generateMedialAxis':(
		'faceNumber',
		'This method computes the medial axis used in the second step of auto-partitioning and displays it.',
	),
	'Assembly._queryMesh':(
		'regions',
		'This method prints mesh and mesh attributes information for the given part instances or regions.',
	),
	'Assembly._removeMedialAxis':(
		'',
		'This method removes the display of the medial axis.',
	),
	'Assembly._seedPartInstanceBySolution':(
		'regions, size <, constraint, lowTemp, highTemp, highTempElementReduction, fileName>',
		'This method applies local edge seeds to the given part instances based on solution measures. The solution measures are the boundary curvature and the solution temperature, as read from an output database file.',
	),
	'Assembly.assignStackDirection':(
		'cells, referenceRegion',
		'This method assigns a stack direction to geometric cells. The stack direction will be used to orient the elements during mesh generation.',
	),
	'Assembly.associateMeshWithGeometry':(
		'geometricEntity <, elements, elemFaces, elemEdges, node>',
		'This method associates a geometric entity with mesh entities that are either orphan elements, bounds orphan elements, or were created using the bottom-up meshing technique.',
	),
	'Assembly.backup':(
		'',
		'This method makes a backup copy of the features in the assembly. The backup() method is used in conjunction with the restore() method.',
	),
	'Assembly.clashSets':(
		'arg1, arg2',
		'This command prints a message describing the relationship between the contents of two sets. Possible outcomes are: Both sets are the same.Set 2 is a subset of set 1.Set 2 is a superset of set 1.Set 2 intersects set 1.Set 2 touches set 1 (their boundaries intersect).Set 2 and set 1 are disjoint.This command accepts only positional arguments and has no keywords.',
	),
	'Assembly.clearGeometryCache':(
		'',
		'This method deletes the geometry cache. Deleting the geometry cache reduces the amount of memory being used.',
	),
	'Assembly.collapseMeshEdge':(
		'edge, collapseMethod',
		'This method collapses an edge of a quadrilateral or triangular element of a part instance.',
	),
	'Assembly.combineElement':(
		'elements',
		'This method combines two triangular elements of a part instance.',
	),
	'Assembly.createVirtualTopology':(
		'regions <, mergeShortEdges, shortEdgeThreshold, mergeSmallFaces, smallFaceAreaThreshold, mergeSliverFaces, faceAspectRatioThreshold, mergeSmallAngleFaces, smallFaceCornerAngleThreshold, mergeThinStairFaces, thinStairFaceThreshold, ignoreRedundantEntities, cornerAngleTolerance, applyBlendControls, blendSubtendedAngleTolerance, blendRadiusTolerance>',
		'This method creates a virtual topology feature by automatically merging faces and edges based on a set of geometric parameters. The edges and vertices that are being merged will be ignored during mesh generation.',
	),
	'Assembly.deleteAllFeatures':(
		'',
		'This method deletes all the features in the assembly.',
	),
	'Assembly.deleteBoundaryLayerControls':(
		'regions',
		'This method deletes the control parameters for boundary layer mesh for all the specified regions.',
	),
	'Assembly.deleteElement':(
		'elements <, deleteUnreferencedNodes>',
		'This method deletes the given elements from a part instance. The elements must have been generated using the bottom-up meshing technique.',
	),
	'Assembly.deleteFeatures':(
		'featureNames',
		'This method deletes specified features from the assembly.',
	),
	'Assembly.deleteMesh':(
		'regions',
		'This method deletes  a subset of the mesh that contains the native elements from the given part instances or regions.',
	),
	'Assembly.deleteMeshAssociationWithGeometry':(
		'geometricEntities <, addBoundingEntities>',
		'This method deletes the association of geometric entities with mesh entities.',
	),
	'Assembly.deletePreviewMesh':(
		'',
		'This method deletes all boundary meshes in the assembly. See the boundaryPreview argument of generateMesh for information about generating boundary meshes.',
	),
	'Assembly.deleteSeeds':(
		'regions',
		'This method deletes the global edge seeds from the given part instances or deletes the local edge seeds from the given edges.',
	),
	'Assembly.deleteSets':(
		'setNames',
		'This command deletes the given sets from the assembly.',
	),
	'Assembly.deleteSurfaces':(
		'surfaceNames',
		'This command deletes the given surfaces from the assembly.',
	),
	'Assembly.editNode':(
		'nodes <, coordinate1, coordinate2, coordinate3, coordinates, offset1, offset2, offset3, localCsys, projectToGeometry>',
		'This method changes the coordinates of the given nodes on a part instance.',
	),
	'Assembly.excludeFromSimulation':(
		'instances, exclude',
		'This method excludes the specified part instances from the analysis.',
	),
	'Assembly.featurelistInfo':(
		'',
		'This method prints the name and status of all the features in the feature lists.',
	),
	'Assembly.generateBottomUpExtrudedMesh':(
		'cell, numberOfLayers, extrudeVector <, geometrySourceSide, elemFacesSourceSide, elemSourceSide, depth, targetSide, biasRatio, extendElementSets>',
		'This method generates solid elements by extruding a 2D mesh along a vector, either on an orphan mesh or within a cell region using a bottom-up technique.',
	),
	'Assembly.generateBottomUpRevolvedMesh':(
		'cell, numberOfLayers, axisOfRevolution, angleOfRevolution <, geometrySourceSide, elemFacesSourceSide, elemSourceSide, extendElementSets>',
		'This method generates solid elements by revolving a 2D mesh around an axis, either on an orphan mesh or within a cell region using a bottom-up technique.',
	),
	'Assembly.generateBottomUpSweptMesh':(
		'cell <, geometrySourceSide, elemFacesSourceSide, elemSourceSide, geometryConnectingSides, elemFacesConnectingSides, elemConnectingSides, targetSide, numberOfLayers, extendElementSets>',
		'This method generates solid elements by sweeping a 2D mesh, either on an orphan mesh or within a cell region using a bottom-up technique.',
	),
	'Assembly.generateMesh':(
		'regions <, seedConstraintOverride, meshTechniqueOverride, boundaryPreview, boundaryMeshOverride>',
		'This method generates a mesh in the given part instances or regions.',
	),
	'Assembly.generateMeshByOffset':(
		'region, meshType, totalThickness, distanceBetweenLayers, numLayers <, offsetDirection, initialOffset, shareNodes, deleteBaseElements, constantThicknessCorners, extendElementSets>',
		'This method generates a solid or shell mesh from an orphan mesh surface by generating layers of elements that propagate out normal to the surface boundary.',
	),
	'Assembly.getAngle':(
		'plane1, plane2, line1, line2',
		'This method returns the angle between the specified entities.',
	),
	'Assembly.getCoordinates':(
		'entity',
		'This method returns the coordinates of a specified point. ',
	),
	'Assembly.getDistance':(
		'entity1, entity2 <, printResults>',
		'Depending on the arguments provided, this method returns one of the following: The distance between two points.The minimum distance between a point and an edge.The minimum distance between two edges.',
	),
	'Assembly.getEdgeSeeds':(
		'edge, attribute',
		'This method returns an edge seed parameter for a specified edge of an assembly.',
	),
	'Assembly.getElementType':(
		'region, elemShape',
		'This method returns the ElemType object of a given element shape assigned to a region of the assembly.',
	),
	'Assembly.getFacesAndVerticesOfAttachmentLines':(
		'edges',
		'Given an array of edge objects, this method returns a tuple of dictionary objects. Each object consists of five members including the attachment line and associated face and vertex objects.',
	),
	'Assembly.getIncompatibleMeshInterfaces':(
		'<cells>',
		'This method returns a sequence of face objects that are meshed with incompatible elements. ',
	),
	'Assembly.getMassProperties':(
		'<regions, relativeAccuracy, useMesh, specifyDensity, density, specifyThickness, thickness, miAboutCenterOfMass, miAboutPoint>',
		'This method returns the mass properties of the assembly, or instances or regions. Only beams, trusses, shells, solids, point, nonstructural mass, and rotary inertia elements are supported.',
	),
	'Assembly.getMeshControl':(
		'region, attribute',
		'This method returns a mesh control parameter for the specified region of the assembly.',
	),
	'Assembly.getMeshStats':(
		'regions',
		'This method returns the mesh statistics for the given part instances or regions.',
	),
	'Assembly.getPartSeeds':(
		'region, attribute',
		'This method returns a part seed parameter for the specified instance.',
	),
	'Assembly.getSurfaceSections':(
		'surface',
		'This method returns a list of the sections assigned to the regions encompassed by the specified surface.',
	),
	'Assembly.getUnmeshedRegions':(
		'',
		'This method returns all geometric regions in the assembly that require a mesh for submitting an analysis but are either unmeshed or are meshed incompletely.',
	),
	'Assembly.ignoreEntity':(
		'entities',
		'This method creates a virtual topology feature. Virtual topology allows unimportant entities to be ignored during mesh generation. You can combine two adjacent faces by specifying a common edge to ignore. Similarly, you can combine two adjacent edges by specifying a common vertex to ignore. ',
	),
	'Assembly.importCatiaV4File':(
		'filename <, ids>',
		'This method imports an assembly from a CATIA V4 file into the root assembly.',
	),
	'Assembly.importCatiaV5File':(
		'filename <, ids>',
		'This method imports an assembly from a CATIA V5 Elysium Neutral file into the root assembly.',
	),
	'Assembly.importEafFile':(
		'filename <, ids>',
		'This method imports an assembly from an EAF file into the root assembly.',
	),
	'Assembly.importEnfFile':(
		'filename <, ids>',
		'This method imports an assembly from an Elysium Neutral file created by Pro/ENGINEER, I-DEAS, or CATIA V5 into the root assembly.',
	),
	'Assembly.importIdeasFile':(
		'filename <, ids>',
		'This method imports an assembly from an I-DEAS Elysium Neutral file into the root assembly.',
	),
	'Assembly.importParasolidFile':(
		'filename <, ids>',
		'This method imports an assembly from the Parasolid file into the root assembly.',
	),
	'Assembly.importProEFile':(
		'filename <, ids>',
		'This method imports an assembly from a Pro/ENGINEER Elysium Neutral file into the root assembly.',
	),
	'Assembly.isSetInternal':(
		'setName',
		'This command returns a flag indicating whether the Set is Internal.',
	),
	'Assembly.isSurfaceInternal':(
		'surfaceName',
		'This command returns a flag indicating whether the Surface is Internal.',
	),
	'Assembly.lock':(
		'',
		'This method locks the assembly. Locking the assembly prevents any further changes to the assembly that can trigger regeneration of the assembly.',
	),
	'Assembly.makeDependent':(
		'instances',
		'This method converts the specified part instances from independent to dependent part instances.',
	),
	'Assembly.makeIndependent':(
		'instances',
		'This method converts the specified part instances from dependent to independent part instances.',
	),
	'Assembly.markSetInternal':(
		'setName, internalSet',
		'This command marks the given Set as internal or external.',
	),
	'Assembly.markSurfaceInternal':(
		'setName, internalSurface',
		'This command marks the given Surface as internal or external.',
	),
	'Assembly.mergeNodes':(
		'node1, node2 <, removeDuplicateElements>',
		'Merge two nodes of a part instance. At least one of the two nodes must have been generated using the bottom-up meshing technique.',
	),
	'Assembly.printAssignedSections':(
		'',
		'This method prints a summary of assigned connector sections.',
	),
	'Assembly.printConnectorOrientations':(
		'',
		'This method prints a summary of connector orientations.',
	),
	'Assembly.projectNode':(
		'nodes, projectionReference',
		'This method projects the given nodes of a part instance onto a mesh entity, geometric entity, or a datum object.',
	),
	'Assembly.projectReferencesOntoSketch':(
		'sketch <, filter, upToFeature, edges, vertices>',
		'This method projects the specified edges, vertices, and datum points from the assembly onto the specified ConstrainedSketch object. The edges, vertices, and datum points appear on the sketch as reference geometry.',
	),
	'Assembly.queryCachedStates':(
		'',
		'This method displays the position of geometric states relative to the sequence of features in the assembly cache. The output is displayed in the message area.',
	),
	'Assembly.redoMeshEdit':(
		'',
		'This method executes the edit mesh or the bottom-up meshing operation most recently undone by the undoMeshEdit method on an assembly. A redo action must be currently available for the assembly.  This implies that the user must have executed the undoMeshEdit method on the assembly and that the user has not subsequently executed any further edit mesh commands on the assembly. It also implies that the user provided a sufficient cache allowance to store the undo operation. ',
	),
	'Assembly.regenerate':(
		'',
		'This method regenerates the assembly and brings it up to date with the latest values of the assembly parameters. When you modify features of an assembly, it may be convenient to postpone regeneration until you make all your changes, since regeneration can be time consuming. In contrast, when you modify features of a part that is included in the assembly, you should use this command to regenerate the assembly. When you regenerate the assembly, it will reflect the changes that you made to the part.',
	),
	'Assembly.regenerationWarnings':(
		'',
		'This method prints any regeneration warnings associated with the features.',
	),
	'Assembly.restore':(
		'',
		'This method restores the parameters of all features in the assembly to the value they had before a failed regeneration. Use the restore method after a failed regeneration, followed by a regenerate command.',
	),
	'Assembly.restoreIgnoredEntity':(
		'entities',
		'This method restores vertices and edges that have been merged using a virtual topology feature.',
	),
	'Assembly.resumeAllFeatures':(
		'',
		'This method resumes all the suppressed features in the part or assembly.',
	),
	'Assembly.resumeFeatures':(
		'featureNames',
		'This method resumes the specified suppressed features in the assembly.',
	),
	'Assembly.resumeLastSetFeatures':(
		'',
		'This method resumes the last set of features to be suppressed in the assembly.',
	),
	'Assembly.rotate':(
		'instanceList, axisPoint, axisDirection, angle',
		'This method rotates given instances by the specified amount.',
	),
	'Assembly.saveGeometryCache':(
		'',
		'This method caches the current geometry, which improves regeneration performance.',
	),
	'Assembly.seedEdgeByBias':(
		'biasMethod, end1Edges, end2Edges, centerEdges, endEdges, ratio, number, minSize, maxSize <, constraint>',
		'This method seeds the given edges nonuniformly using the specified number of elements and bias ratio or the specified minimum and maximum element sizes.',
	),
	'Assembly.seedEdgeByNumber':(
		'edges, number <, constraint>',
		'This method seeds the given edges uniformly based on the number of elements along the edges. ',
	),
	'Assembly.seedEdgeBySize':(
		'edges, size <, deviationFactor, minSizeFactor, constraint>',
		'This method seeds the given edges either uniformly or following edge curvature distribution, based on the desired element size. ',
	),
	'Assembly.seedPartInstance':(
		'regions, size <, deviationFactor, minSizeFactor, constraint>',
		'This method assigns global edge seeds to the given part instances.',
	),
	'Assembly.setBoundaryLayerControls':(
		'regions, firstElemSize, growthFactor, numLayers <, inactiveFaces, setName>',
		'This method sets the control parameters for boundary layer mesh for the specified regions.',
	),
	'Assembly.setElementType':(
		'regions, elemTypes',
		'This method assigns element types to the specified regions.',
	),
	'Assembly.setLogicalCorners':(
		'region, corners',
		'This method sets the logical corners for a mappable face region.',
	),
	'Assembly.setMeshControls':(
		'regions <, elemShape, technique, algorithm, minTransition, sizeGrowth, allowMapped>',
		'This method sets the mesh control parameters for the specified regions.',
	),
	'Assembly.setMeshNumberingControl':(
		'instances <, startNodeLabel, startElemLabel>',
		'This method changes the start node and/or element labels on the specified independent part instances before or after Abaqus/CAE generates the meshes. For the meshed instances, Abaqus/CAE changes the node and/or element labels while preserving the original order and incrementation.',
	),
	'Assembly.setSweepPath':(
		'region, edge, sense',
		'This method sets the sweep path for a sweepable region or the revolve path for a revolvable region.',
	),
	'Assembly.setTolerance':(
		'linearTolerance, angularTolerance',
		'This method sets the linear and angular tolerance used by the system. The argument linearTolerance defines the smallest distance between two distinct points and determines if two positions in space are equal. The argument angularTolerance checks a number for equality with zero. angularTolerance checks for zero length or determines if vectors are parallel or perpendicular.The default settings when a session is started are:linearTolerance = 1E-06.angularTolerance = 1E-10.',
	),
	'Assembly.setValues':(
		'regenerateConstraintsTogether',
		'This method modifies the behavior associated with the specified assembly.',
	),
	'Assembly.splitElement':(
		'elements',
		'This method splits quadrilateral elements into triangular elements.',
	),
	'Assembly.splitMeshEdge':(
		'edge <, parameter>',
		'This method splits an edge of a quadrilateral or triangular element of a part instance.',
	),
	'Assembly.suppressFeatures':(
		'featureNames',
		'This method suppresses specified features.',
	),
	'Assembly.swapMeshEdge':(
		'edge',
		'This method swaps the diagonal of two adjacent triangular elements of a part instance.',
	),
	'Assembly.translate':(
		'instanceList, vector',
		'This method translates given instances by the specified amount.',
	),
	'Assembly.undoMeshEdit':(
		'',
		'This method undoes the most recent edit mesh or the bottom-up meshing operation on an assembly and restores the mesh on the affected part instance to its previous state. An edit mesh undo action must be available for the assembly.  This implies that prior to executing an edit mesh command on the assembly, the user enabled edit mesh undo with a sufficient cache allowance to store the edit mesh operation.',
	),
	'Assembly.unlinkInstances':(
		'instances',
		'This method converts the specified PartInstance objects from linked child instances to regular instances.  The parts associated with the selected instances will be converted to regular parts as well.',
	),
	'Assembly.unlock':(
		'',
		'This method unlocks the assembly. Unlocking the assembly allows it to be regenerated after any modifications to the assembly.',
	),
	'Assembly.verifyMeshQuality':(
		'criterion <, threshold, elemShape, regions>',
		'This method tests the quality of part instance meshes and returns poor-quality elements.',
	),
	'Assembly.writeAcisFile':'<value is a self-reference, replaced by this string>',
	'Assembly.writeCADParameters':(
		'paramFile <, modifiedParams, updatePaths>',
		'This method writes the parameters that were imported from the CAD system to a parameter file.',
	),
	'AssemblyDisplayOptions.setValues':(
		'<visibleInstances, step, renderStyle, mesh, loads, bcs, interactions, constraints, connectors, cnxEndPoints, cnxLocalAxes, cnxTypeLabels, cnxTagDisplay, predefinedFields, visibleDisplayGroups, engineeringFeatures, renderBeamProfiles, beamScaleFactor, optimizationTasks, geometricRestrictions, stopConditions>',
		'This method modifies the AssemblyDisplayOptions object.',
	),
	'AttributeColorMap.setDefaults':(
		'',
		'This method resets the \n AttributeColorMap \n object to its default state.\n ',
	),
	'AttributeColorMap.setValues':(
		'<overrides, defaultOverrides>',
		'This method modifies the \n AttributeColorMap \n object.\n ',
	),
	'AttributeColorMap.updateOverrides':(
		'<overrides, defaultOverrides>',
		'This method specifies additional overrides to be added to the current object definition.',
	),
	'AutoColors.setValues':(
		'colors',
		'This method changes the color palette.',
	),
	'Axis.setValues':(
		'<axis, labelFrequency, labelPlacement, labelStyle, lineStyle, placement, tickLength, tickPlacement, tickStyle, titleStyle>',
		'This method modifies the Axis object.',
	),
	'AxisData.setValues':(
		'<axisData, labelFormat, labelNumDigits, scale, dbReference, minAutoCompute, minValue, maxAutoCompute, maxValue, tickMode, tickIncrement, tickCount, minorTickCount, title, useSystemTitle>',
		'This method modifies the AxisData object.',
	),
	'BCDisplayOptions.setValues':(
		'<displacement, velocity, acceleration, symmetry, antiSymmetry, temperature, porePressure, fluidCavityPressure, acousticPressure, electricPotential, concentration, encastre, pinned>',
		'This method modifies the BCDisplayOptions object.',
	),
	'BaselineCorrection.setValues':'<value is a self-reference, replaced by this string>',
	'BasicOptions.setValues':(
		'<options, cameraCsysName, cameraMovesWithCsys, cameraFollowsRotation, averagingThreshold, quantityToPlot, curveRefinementLevel, noResultsColor, featureAngle, otherSymbolSize, renderBeamProfiles, beamScaleFactor, renderShellThickness, shellScaleFactor, accountForDeactivatedElems, bcDisplay, connectorDisplay, highlightConnectorPts, showConnectorAxes, showConnectorType, pointElements, referencePoints, massElements, springElements, spotWelds, tracerParticles, sweepArs, sweepElem, sweepStartAngleArs, sweepStartAngleElem, sweepEndAngleArs, sweepEndAngleElem, numSweepSegmentsArs, numSweepSegmentsElem, numericForm, complexAngle, sectionResults, envelopeCriteria, envelopeDataPosition, plyResultLocation, sectionPointScheme, sweepSectors, sectorSelectionType, selectedSectorNumbers, sweepSectorStartAngle, sweepSectorEndAngle, extrudeArs, extrudeArsDepthAutoCompute, extrudeElem, extrudeArsDepth, extrudeElemDepth, mirrorPatternOrder, mirrorCsysName, mirrorAboutXyPlane, mirrorAboutXzPlane, mirrorAboutYzPlane, mirrorDisplayBodies, patternCsysName, patternNumX, patternNumY, patternNumZ, patternOffsetX, patternOffsetY, patternOffsetZ, patternRotationAxis, patternTotalAngle, patternNumCircular, couplingDisplay, coordSystemDisplay, scratchCoordSystemDisplay, transformationType, datumCsys, rigidTransformPrimary, rigidTransformDeformed, transformOnDeformed, averageElementOutput, averageOnlyDisplayed, computeOutput, regionBoundaries, useRegionBoundaries, userRegions, includeFeatureBoundaries>',
		'This method modifies the BasicOptions object.',
	),
	'BeamSection.TransverseShearBeam':(
		'<k23, k13, slendernessCompensation>',
		'This method creates a TransverseShearBeam object.',
	),
	'BeamSection.setValues':'<value is a self-reference, replaced by this string>',
	'BiaxialTestData.setValues':'<value is a self-reference, replaced by this string>',
	'BodyCharge.setValues':'<value is a self-reference, replaced by this string>',
	'BodyCharge.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing BodyCharge object in the specified step.',
	),
	'BodyConcentrationFlux.setValues':'<value is a self-reference, replaced by this string>',
	'BodyConcentrationFlux.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing BodyConcentrationFlux object in the specified step.',
	),
	'BodyCurrent.setValues':'<value is a self-reference, replaced by this string>',
	'BodyCurrent.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing BodyCurrent object in the specified step.',
	),
	'BodyCurrentDensity.setValues':'<value is a self-reference, replaced by this string>',
	'BodyCurrentDensity.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing BodyCurrentDensity object in the specified step.',
	),
	'BodyForce.setValues':'<value is a self-reference, replaced by this string>',
	'BodyForce.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing BodyForce object in the specified step.',
	),
	'BodyHeatFlux.setValues':'<value is a self-reference, replaced by this string>',
	'BodyHeatFlux.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing BodyHeatFlux object in the specified step.',
	),
	'BoltLoad.setValues':'<value is a self-reference, replaced by this string>',
	'BoltLoad.setValuesInStep':(
		'stepName <, boltMethod, magnitude, amplitude>',
		'This method modifies the propagating data for an existing BoltLoad object in the specified step.',
	),
	'BondedContact.setValues':'<value is a self-reference, replaced by this string>',
	'BoundaryCondition.deactivate':(
		'stepName',
		'This method deactivates the boundary condition in the specified step and all subsequent steps.',
	),
	'BoundaryCondition.delete':(
		'indices',
		'This method allows you to delete existing boundary conditions.\n      ',
	),
	'BoundaryCondition.move':(
		'fromStepName, toStepName',
		'This method moves the boundary condition state from one step to a different step.',
	),
	'BoundaryCondition.reset':(
		'stepName',
		'This method resets the boundary condition state of the specified step to the state of the previous analysis step.',
	),
	'BoundaryCondition.resume':(
		'',
		'This method resumes the boundary condition that was previously suppressed.',
	),
	'BoundaryCondition.suppress':(
		'',
		'This method suppresses the boundary condition.',
	),
	'BoxProfile.setValues':'<value is a self-reference, replaced by this string>',
	'BrittleCracking.BrittleFailure':(
		'table <, temperatureDependency, dependencies, failureCriteria>',
		'This method creates a BrittleFailure object.',
	),
	'BrittleCracking.BrittleShear':(
		'table <, temperatureDependency, dependencies, type>',
		'This method creates a BrittleShear object.',
	),
	'BrittleCracking.setValues':'<value is a self-reference, replaced by this string>',
	'BrittleFailure.setValues':'<value is a self-reference, replaced by this string>',
	'BrittleShear.setValues':'<value is a self-reference, replaced by this string>',
	'BuckleStep.setValues':'<value is a self-reference, replaced by this string>',
	'ButterworthFilter.setValues':'<value is a self-reference, replaced by this string>',
	'CDCTerm.ConnectorOptions':(
		'<useBehRegSettings, regularize, defaultTolerance, regularization, defaultRateFactor, rateFactor, interpolation, useBehExtSettings, extrapolation>',
		'This method creates a connector options object to be used in conjunction with an allowable connector behavior option, derived component term, or connector section.',
	),
	'CDCTerm.setValues':'<value is a self-reference, replaced by this string>',
	'Calibration.Behavior':(
		'name, typeName',
		'This method creates a \n Behavior\n object.\n ',
	),
	'Calibration.DataSet':(
		'name, data <, type, form>',
		'This method creates a \n DataSet\n object.\n ',
	),
	'CapCreepCohesion.setValues':'<value is a self-reference, replaced by this string>',
	'CapCreepConsolidation.setValues':'<value is a self-reference, replaced by this string>',
	'CapHardening.setValues':'<value is a self-reference, replaced by this string>',
	'CapPlasticity.CapCreepCohesion':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a CapCreepCohesion object.',
	),
	'CapPlasticity.CapCreepConsolidation':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a CapCreepConsolidation object.',
	),
	'CapPlasticity.CapHardening':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a CapHardening object.',
	),
	'CapPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'CastIronCompressionHardening.setValues':'<value is a self-reference, replaced by this string>',
	'CastIronPlasticity.CastIronCompressionHardening':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a CastIronCompressionHardening object.',
	),
	'CastIronPlasticity.CastIronTensionHardening':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a CastIronTensionHardening object.',
	),
	'CastIronPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'CastIronTensionHardening.setValues':'<value is a self-reference, replaced by this string>',
	'CavityRadiation.setValues':'<value is a self-reference, replaced by this string>',
	'CavityRadiation.setValuesInStep':(
		'stepName <, blocking, blockingSurfaces, rangeOfView, surfaceReflection, viewfactorAccurTol>',
		'This method modifies the propagating data of an existing CavityRadiation object in the specified step.',
	),
	'CavityRadiationProp.setValues':'<value is a self-reference, replaced by this string>',
	'Cell.getAdjacentCells':(
		'',
		'This method returns an array of cell objects that share at least one face of the cell.',
	),
	'Cell.getEdges':(
		'',
		'This method returns a sequence consisting of the edge IDs of the edges on the cell.',
	),
	'Cell.getElements':(
		'',
		'This method returns an array of element objects that are associated with the cell.',
	),
	'Cell.getFaces':(
		'',
		'This method returns a sequence consisting of the face IDs of the faces which bound the cell.',
	),
	'Cell.getNodes':(
		'',
		'This method returns an array of node objects that are associated with the cell.',
	),
	'Cell.getSize':(
		'<printResults>',
		'This method returns a Float indicating the volume of the cell.',
	),
	'Cell.getVertices':(
		'',
		'This method returns a sequence consisting of the vertex IDs of the vertices on the cell.',
	),
	'Cell.index':(
		'keyword argument not implemented',
		'This method returns the index of a Cell in the CellArray.',
	),
	'CellArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the object or objects in the CellArray located at the given coordinates. \n findAt \n initially uses the ACIS tolerance of 1E-6. As a result, \n findAt \n returns any entity that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, \n findAt \n uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities). The arbitrary point must not be shared by a second cell. If two cells intersect or coincide at the arbitrary point, \n findAt \n chooses the first cell that it encounters, and you should not rely on the return value being consistent.\n findAt \n will always try to find objects among all the cells in the part or assembly instance and will not restrict itself to a subset even if the CellArray represents such subset.\n ',
	),
	'CellArray.getBoundingBox':(
		'',
		'This method returns a dictionary of two tuples representing minimum and maximum boundary\n values of the bounding box of the minimum size containing the cell sequence.',
	),
	'CellArray.getByBoundingBox':(
		'<xMin, yMin, zMin, xMax, yMax, zMax>',
		'This method returns an array of cell objects that lie within the specified bounding box.',
	),
	'CellArray.getByBoundingCylinder':(
		'center1, center2, radius',
		'This method returns an array of cell objects that lie within the specified bounding cylinder.',
	),
	'CellArray.getByBoundingSphere':(
		'center, radius',
		'This method returns an array of cell objects that lie within the specified bounding sphere.',
	),
	'CellArray.getSequenceFromMask':(
		'mask',
		'This method returns the object or objects in the CellArray identified using the specified \n mask. This command is generated when the \n JournalOptions \n are set to COMPRESSEDINDEX. When large number of objects are involved, this method is highly efficient.\n ',
	),
	'Chart.autoColor':(
		'<lines, symbols>',
		'This method distributes the colors on all curves displayed in the chart using the color palette defined by the xyColors object.',
	),
	'Chart.autoSymbol':(
		'',
		'This method distributes the symbols on all curves displayed in the chart.',
	),
	'Chart.fitCurves':(
		'',
		'This method resets the transform of the chart. It cancels any zoom or pan action.',
	),
	'Chart.getAxis1':(
		'curve, quantityType',
		'This method returns the Axis object used for displaying the Axis1 of the XYCurve specified by name or object or used for the given QuantityType object.',
	),
	'Chart.getAxis2':(
		'curve, quantityType',
		'This method returns the Axis object used for displaying the Axis2 of the XYCurve specified by name or object or used for the given QuantityType object.',
	),
	'Chart.moveAxisDown':(
		'axis',
		'This method moves the relative position of the given Axis object down in the axis sequence of the Chart.',
	),
	'Chart.moveAxisUp':(
		'axis',
		'This method moves the relative position of the given Axis object up in the axis sequence of the Chart.',
	),
	'Chart.removeCurve':(
		'curve',
		'This method removes the given XYCurve from the Chart.',
	),
	'Chart.setValues':(
		'<chart, curvesToPlot, aspectRatio, transform, view, useQuantityType>',
		'This method modifies the Chart object.',
	),
	'Chebyshev1Filter.setValues':'<value is a self-reference, replaced by this string>',
	'Chebyshev2Filter.setValues':'<value is a self-reference, replaced by this string>',
	'CircularProfile.setValues':'<value is a self-reference, replaced by this string>',
	'ClayHardening.setValues':'<value is a self-reference, replaced by this string>',
	'ClayPlasticity.ClayHardening':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a ClayHardening object.',
	),
	'ClayPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'Coexecution.kill':(
		'',
		'This method kills the analysis of a co-execution.',
	),
	'Coexecution.submit':(
		'<consistencyChecking, datacheckJob, continueJob>',
		'This method submits a co-execution for analysis.',
	),
	'Coexecution.waitForCompletion':(
		'',
		'This method interrupts the execution of the script until the end of all the analyses. If you call the waitForCompletion method and the status member is neither SUBMITTED nor RUNNING, Abaqus assumes the analysis has either completed or aborted and returns immediately. ',
	),
	'Coexecution.writeInput':(
		'<consistencyChecking>',
		'This method writes an input file for each analysis in the co-execution.',
	),
	'CohesiveBehavior.setValues':'<value is a self-reference, replaced by this string>',
	'CohesiveSection.setValues':'<value is a self-reference, replaced by this string>',
	'Color.setByRGB':(
		'rgb',
		'This method changes the RGB value of a user-defined color. However, users cannot define colors, and this method does not modify system-defined colors.',
	),
	'CombinedTermDesignResponse.setValues':'<value is a self-reference, replaced by this string>',
	'CombinedTestData.setValues':'<value is a self-reference, replaced by this string>',
	'CommonOptions.setValues':(
		'<options, renderStyle, visibleEdges, deformationScaling, uniformScaleFactor, nonuniformScaleFactor, edgeColorWireHide, edgeColorFillShade, edgeLineStyle, edgeLineThickness, fillColor, colorCodeOverride, labelFont, elemLabels, elemLabelColor, faceLabels, faceLabelColor, nodeLabels, nodeLabelColor, nodeSymbols, nodeSymbolType, nodeSymbolColor, nodeSymbolSize, elementShrink, elementShrinkFactor, coordinateScale, coordinateScaleFactors, normals, normalDisplay, faceNormalColor, beamN1Color, beamN2Color, beamTangentColor, normalArrowLength, normalLineThickness, normalArrowheadStyle, translucency, translucencyFactor>',
		'This method modifies the CommonOptions object.',
	),
	'ComplexFrequencyStep.setValues':'<value is a self-reference, replaced by this string>',
	'CompositeLayup.CompositePly':(
		'thickness, region, material <, orientationValue, orientationType, thicknessType, numIntPts, axis, angle, additionalRotationType, plyName, orientation, additionalRotationField>',
		'This method creates a CompositePly object.',
	),
	'CompositeLayup.CompositeShellSection':(
		'name, layup <, symmetric, thicknessType, preIntegrate, poissonDefinition, poisson, integrationRule, temperature, idealization, nTemp, thicknessModulus, useDensity, density, layupName, thicknessField, nodalThicknessField>',
		'This method creates a CompositeShellSection object.',
	),
	'CompositeLayup.HomogeneousShellSection':(
		'name, material <, thickness, numIntPts, thicknessType, preIntegrate, poissonDefinition, poisson, integrationRule, temperature, idealization, nTemp, thicknessModulus, useDensity, density, thicknessField, nodalThicknessField>',
		'This method creates a HomogeneousShellSection object.',
	),
	'CompositeLayup.ReferenceOrientation':(
		'<localCsys, axis, angle, stackDirection, fieldName, orientationType, additionalRotationField, additionalRotationType, normalAxisDirection, normalAxisDefinition, normalAxisRegion, normalAxisDatum, flipNormalDirection, normalAxisVector, primaryAxisDirection, primaryAxisDefinition, primaryAxisRegion, primaryAxisDatum, flipPrimaryDirection, primaryAxisVector>',
		'This method creates a \n MaterialOrientation \n object.\n ',
	),
	'CompositeLayup.Section':(
		'<nodalThicknessField, thicknessField, thicknessType, preIntegrate, poissonDefinition, poisson, integrationRule, temperature, nTemp, thicknessModulus, useDensity, density>',
		'This method creates a GeometryShellSection object.',
	),
	'CompositeLayup.deletePlies':(
		'',
		'This method deletes all of the plies from a composite layup.',
	),
	'CompositeLayup.resume':(
		'',
		'This method resumes a composite layup that was previously suppressed.',
	),
	'CompositeLayup.setValues':'<value is a self-reference, replaced by this string>',
	'CompositeLayup.suppress':(
		'',
		'This method suppresses a composite layup.',
	),
	'CompositeShellSection.setValues':'<value is a self-reference, replaced by this string>',
	'CompositeSolidSection.setValues':'<value is a self-reference, replaced by this string>',
	'ConcCharge.setValues':'<value is a self-reference, replaced by this string>',
	'ConcCharge.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ConcCharge object in the specified step.',
	),
	'ConcConcFlux.setValues':'<value is a self-reference, replaced by this string>',
	'ConcConcFlux.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ConcConcFlux object in the specified step.',
	),
	'ConcCurrent.setValues':'<value is a self-reference, replaced by this string>',
	'ConcCurrent.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ConcCurrent object in the specified step.',
	),
	'ConcPoreFluid.setValues':'<value is a self-reference, replaced by this string>',
	'ConcPoreFluid.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ConcPoreFluid object in the specified step.',
	),
	'ConcentratedFilmCondition.setValues':'<value is a self-reference, replaced by this string>',
	'ConcentratedFilmCondition.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data of an existing ConcentratedFilmCondition object in the specified step.',
	),
	'ConcentratedForce.setValues':'<value is a self-reference, replaced by this string>',
	'ConcentratedForce.setValuesInStep':(
		'stepName <, cf1, cf2, cf3, amplitude>',
		'This method modifies the propagating data for an existing ConcentratedForce object in the specified step.',
	),
	'ConcentratedHeatFlux.setValues':'<value is a self-reference, replaced by this string>',
	'ConcentratedHeatFlux.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ConcentratedHeatFlux object in the specified step.',
	),
	'ConcentratedRadiationToAmbient.setValues':'<value is a self-reference, replaced by this string>',
	'ConcentratedRadiationToAmbient.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data of an existing ConcentratedRadiationToAmbient object in the specified step.',
	),
	'Concentration.setValues':'<value is a self-reference, replaced by this string>',
	'ConcentrationBC.setValues':'<value is a self-reference, replaced by this string>',
	'ConcentrationBC.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ConcentrationBC object in the specified step.',
	),
	'Concrete.FailureRatios':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a FailureRatios object.',
	),
	'Concrete.ShearRetention':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a ShearRetention object.',
	),
	'Concrete.TensionStiffening':(
		'table <, type, temperatureDependency, dependencies>',
		'This method creates a TensionStiffening object.',
	),
	'Concrete.setValues':'<value is a self-reference, replaced by this string>',
	'ConcreteCompressionDamage.setValues':'<value is a self-reference, replaced by this string>',
	'ConcreteCompressionHardening.setValues':'<value is a self-reference, replaced by this string>',
	'ConcreteDamagedPlasticity.ConcreteCompressionDamage':(
		'table <, tensionRecovery, temperatureDependency, dependencies>',
		'This method creates a ConcreteCompressionDamage object.',
	),
	'ConcreteDamagedPlasticity.ConcreteCompressionHardening':(
		'table <, rate, temperatureDependency, dependencies>',
		'This method creates a ConcreteCompressionHardening object.',
	),
	'ConcreteDamagedPlasticity.ConcreteTensionDamage':(
		'table <, compressionRecovery, type, temperatureDependency, dependencies>',
		'This method creates a ConcreteTensionDamage object.',
	),
	'ConcreteDamagedPlasticity.ConcreteTensionStiffening':(
		'table <, rate, type, temperatureDependency, dependencies>',
		'This method creates a ConcreteTensionStiffening object.',
	),
	'ConcreteDamagedPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'ConcreteTensionDamage.setValues':'<value is a self-reference, replaced by this string>',
	'ConcreteTensionStiffening.setValues':'<value is a self-reference, replaced by this string>',
	'Conductivity.setValues':'<value is a self-reference, replaced by this string>',
	'ConnAccelerationBC.setValues':'<value is a self-reference, replaced by this string>',
	'ConnAccelerationBC.setValuesInStep':(
		'stepName <, a1, a2, a3, ar1, ar2, ar3, amplitude>',
		'This method modifies the propagating data for an existing ConnAccelerationBC object in the specified step.',
	),
	'ConnDisplacementBC.setValues':'<value is a self-reference, replaced by this string>',
	'ConnDisplacementBC.setValuesInStep':(
		'stepName <, u1, u2, u3, ur1, ur2, ur3, amplitude, buckleCase>',
		'This method modifies the propagating data for an existing ConnDisplacementBC object in the specified step.',
	),
	'ConnVelocityBC.setValues':'<value is a self-reference, replaced by this string>',
	'ConnVelocityBC.setValuesInStep':(
		'stepName <, v1, v2, v3, vr1, vr2, vr3, amplitude>',
		'This method modifies the propagating data for an existing ConnVelocityBC object in the specified step.',
	),
	'ConnectorDamage.ConnectorOptions':'<value is a self-reference, replaced by this string>',
	'ConnectorDamage.ConnectorPotential':(
		'<componentStyle, componentNumber, sign, scaleFactor, positiveExponent, shiftFactor, hFunction>',
		'This method creates\na connector potential object to be used in conjunction with an allowable connector\nbehavior option.',
	),
	'ConnectorDamage.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorDamping.ConnectorOptions':'<value is a self-reference, replaced by this string>',
	'ConnectorDamping.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorElasticity.ConnectorOptions':'<value is a self-reference, replaced by this string>',
	'ConnectorElasticity.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorFailure.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorForce.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorForce.setValuesInStep':(
		'stepName <, f1, f2, f3, amplitude>',
		'This method modifies the propagating data for an existing ConnectorForce object in the specified step.',
	),
	'ConnectorFriction.ConnectorOptions':'<value is a self-reference, replaced by this string>',
	'ConnectorFriction.ConnectorPotential':'<value is a self-reference, replaced by this string>',
	'ConnectorFriction.DerivedComponent':(
		'',
		'This method creates a DerivedComponent object.',
	),
	'ConnectorFriction.TangentialBehavior':(
		'<formulation, slipRateDependency, pressureDependency, temperatureDependency, dependencies, exponentialDecayDefinition, shearStressLimit, maximumElasticSlip, fraction, absoluteDistance, table>',
		'This method creates a TangentialBehavior object.',
	),
	'ConnectorFriction.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorLock.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorMoment.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorMoment.setValuesInStep':(
		'stepName <, m1, m2, m3, amplitude>',
		'This method modifies the propagating data for an existing ConnectorMoment object in the specified step.',
	),
	'ConnectorOptions.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorOrientation.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorPlasticity.ConnectorOptions':'<value is a self-reference, replaced by this string>',
	'ConnectorPlasticity.ConnectorPotential':'<value is a self-reference, replaced by this string>',
	'ConnectorPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorPotential.DerivedComponent':'<value is a self-reference, replaced by this string>',
	'ConnectorPotential.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorSection.ConnectorDamage':(
		'<coupling, criterion, initiationTemperature, initiationPotentialOperator, initiationPotentialExponent, initiationDependencies, evolution, evolutionType, softening, useAffected, degradation, evolutionTemperature, evolutionDependencies, evolutionPotentialOperator, evolutionPotentialExponent, initiationPotentials, evolutionPotentials, initiationTable, evolutionTable, affectedComponents, components>',
		'This method creates a connector damage behavior option for a ConnectorSection object.',
	),
	'ConnectorSection.ConnectorDamping':(
		'<behavior, coupling, dependencies, temperatureDependency, frequencyDependency, table, independentComponents, components>',
		'This method creates a connector damping behavior option for a ConnectorSection object.',
	),
	'ConnectorSection.ConnectorElasticity':(
		'<behavior, coupling, dependencies, temperatureDependency, frequencyDependency, table, independentComponents, components>',
		'This method creates a connector elasticity behavior option for a ConnectorSection object.',
	),
	'ConnectorSection.ConnectorFailure':(
		'<releaseComponent, minMotion, maxMotion, minForce, maxForce, components>',
		'This method creates a connector failure behavior option for a ConnectorSection object.',
	),
	'ConnectorSection.ConnectorFriction':(
		'<frictionModel, slipStyle, tangentDirection, stickStiffness, componentType, slipDependency, temperatureDependency, dependencies, useContactForceComponent, contactForceStyle, contactForceComponent, forcePotentialOperator, forcePotentialExponent, connectorPotentials, table, independentComponents>',
		'This method creates a connector friction behavior option for a ConnectorSection object.\n Depending upon the arguments provided, the friction behavior can be Coulomb-like or hysteretic in nature.',
	),
	'ConnectorSection.ConnectorLock':(
		'<lockingComponent, minMotion, maxMotion, minForce, maxForce, components>',
		'This method creates a connector lock behavior option for a ConnectorSection.',
	),
	'ConnectorSection.ConnectorPlasticity':(
		'<coupling, isotropic, isotropicType, isotropicTemperature, isotropicDependencies, kinematic, kinematicType, kinematicTemperature, kinematicDependencies, forcePotentialOperator, forcePotentialExponent, connectorPotentials, isotropicTable, kinematicTable, components>',
		'This method creates a connector plasticity behavior option for a ConnectorSection object.',
	),
	'ConnectorSection.ConnectorStop':(
		'<minMotion, maxMotion, components>',
		'This method creates a connector stop behavior option for a ConnectorSection object.',
	),
	'ConnectorSection.setValues':'<value is a self-reference, replaced by this string>',
	'ConnectorStop.setValues':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketch.AngularDimension':(
		'line1, line2, textPoint <, value, reference>',
		'This method constructs a \n ConstrainedSketchDimension\n object between two \n ConstrainedSketchGeometry\n objects, with the given angle between them.\n ',
	),
	'ConstrainedSketch.Arc3Points':(
		'point1, point2, point3',
		'This method constructs an arc using a two endpoints and an intermediate third point on the arc.',
	),
	'ConstrainedSketch.ArcByCenterEnds':(
		'center, point1, point2',
		'This method constructs an arc using a center point and two vertices. The Arc object is added to the geometry repository of the \n ConstrainedSketch\n object. The arc is created in a clockwise fashion from \n point1\n to \n point2.\n ',
	),
	'ConstrainedSketch.ArcByStartEndTangent':(
		'point1, point2, vector',
		'This method constructs an arc using two vertices. The Arc object is added to the geometry repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.CircleByCenterPerimeter':(
		'center, point1 <, type>',
		'This method constructs a circle using a center point and a point on the perimeter. The circle is added to the geometry repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.CoincidentConstraint':(
		'entity1, entity2',
		'This method creates a coincident constraint. This constraint applies to two vertices, to a vertex and a \n ConstrainedSketchGeometry\n object, or to two \n ConstrainedSketchGeometry\n objects of the same type and constrains them to be coincident.\n ',
	),
	'ConstrainedSketch.ConcentricConstraint':(
		'entity1, entity2',
		'This method creates a concentric constraint. This constraint applies to any combination of circles, arcs, ellipses, and points and constrains them to be concentric. A concentric constraint implies that the center of \n ConstrainedSketchGeometry\n objects coincide.\n ',
	),
	'ConstrainedSketch.ConstructionCircleByCenterPerimeter':(
		'center, point1 <, type>',
		'This method constructs a construction circle using a center point and a point on the perimeter. The circle is added to the geometry repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.ConstructionLine':(
		'point1, point2',
		'This method creates an oblique construction line that runs between two given points.',
	),
	'ConstrainedSketch.DistanceDimension':(
		'entity1, vertex2, textPoint <, value, reference>',
		'This method constructs a \n ConstrainedSketchDimension\n object between two \n ConstrainedSketchGeometry, or a\n ConstrainedSketchVertex\n and \n ConstrainedSketchGeometry\n object. A distance dimension specifies the shortest distance between two entities.\n ',
	),
	'ConstrainedSketch.EllipseByCenterPerimeter':(
		'center, axisPoint1, axisPoint2',
		'This method constructs an ellipse using a center point, a major axis point, and a minor axis point. The ellipse is added to the geometry repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.EqualDistanceConstraint':(
		'entity1, entity2, midpoint',
		'This method creates an equal distance constraint. This constraint can be applied between a midpoint \n Vertex\n object and any other two \n Vertex\n objects or between a midpoint \n Vertex\n object and two \n ConstrainedSketchGeometry\n objects that are lines. The equal distance constraint forces the midpoint vertex to remain at an equal distance from the two other vertices or lines.\n ',
	),
	'ConstrainedSketch.EqualLengthConstraint':(
		'entity1, entity2',
		'This method creates an equal length constraint. This constraint applies to lines and constrains them such that their lengths are equal.',
	),
	'ConstrainedSketch.EqualRadiusConstraint':(
		'entity1, entity2',
		'This method creates an equal radius constraint. This constraint applies to circles and arcs and constrains them such that their radii are equal.',
	),
	'ConstrainedSketch.FilletByRadius':(
		'radius, curve1, nearPoint1, curve2, nearPoint2',
		'This method constructs a fillet arc of a given radius between two curves. The fillet is added to the geometry repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.FixedConstraint':(
		'entity',
		'This method creates a fixed constraint. This constraint applies to a \n ConstrainedSketchGeometry\n object or a \n Vertex\n object and constrains them to be fixed in space. Both the location and the shape of the sketch geometry is fixed.\n ',
	),
	'ConstrainedSketch.HorizontalConstraint':(
		'entity',
		'This method creates a horizontal constraint. This constraint applies to a line and constrains it to be horizontal.',
	),
	'ConstrainedSketch.HorizontalDimension':(
		'vertex1, vertex2, textPoint <, value, reference>',
		'This method constructs a \n ConstrainedSketchDimension\n object between two vertices. A horizontal dimension indicates the horizontal distance along the \n X-axis between two vertices.\n ',
	),
	'ConstrainedSketch.Line':(
		'point1, point2',
		'This method creates a line between two given points.',
	),
	'ConstrainedSketch.ObliqueDimension':(
		'vertex1, vertex2, textPoint <, value, reference>',
		'This method constructs a \n ConstrainedSketchDimension\n object between two vertices. An oblique dimension indicates the distance between two vertices.\n ',
	),
	'ConstrainedSketch.ParallelConstraint':(
		'entity1, entity2',
		'This method creates a parallel constraint. This constraint applies to lines and constrains them to be parallel.',
	),
	'ConstrainedSketch.Parameter':(
		'name <, path, expression, previousParameter>',
		'This method creates a parameter and optionally associates a dimension with this parameter.',
	),
	'ConstrainedSketch.PerpendicularConstraint':(
		'entity1, entity2',
		'This method creates a perpendicular constraint. This constraint applies to different types of \n ConstrainedSketchGeometry\n objects and constrains them to be perpendicular to each other.\n ',
	),
	'ConstrainedSketch.RadialDimension':(
		'curve, textPoint <, value, reference, majorRadius, minorRadius>',
		'This method constructs a \n ConstrainedSketchDimension\n object on a circular or elliptical arc. A radial dimension indicates the radius of an arc or circle or the major or minor radius of an ellipse.\n ',
	),
	'ConstrainedSketch.Spline':(
		'points <, constrainPoints>',
		'This method creates a spline curve running through a sequence of points.',
	),
	'ConstrainedSketch.Spot':(
		'point',
		'This method creates a spot (construction point) located at the specified coordinates.',
	),
	'ConstrainedSketch.TangentConstraint':(
		'entity1, entity2',
		'This method creates a tangent constraint. This constraint applies to different types of \n ConstrainedSketchGeometry\n objects and constrains them to remain tangential.\n ',
	),
	'ConstrainedSketch.VerticalConstraint':(
		'entity',
		'This method creates a vertical constraint. This constraint applies to a line and constrains it to be vertical.',
	),
	'ConstrainedSketch.VerticalDimension':(
		'vertex1, vertex2, textPoint <, value, reference>',
		'This method constructs a \n ConstrainedSketchDimension\n between two vertices. A vertical dimension controls the vertical distance along the \n Y-axis between two vertices.\n ',
	),
	'ConstrainedSketch.assignCenterOfTwist':(
		'point',
		'This method indicates the isolated point that will be used as the center of twist when an extruded feature is created with twist.',
	),
	'ConstrainedSketch.assignCenterline':(
		'line',
		'This method indicates the construction line that will be used as a centerline for revolved features.',
	),
	'ConstrainedSketch.autoDimension':(
		'objectList',
		'This method applies dimensions to the selected \n ConstrainedSketchGeometry\n objects in an effort to make the \n ConstrainedSketch\n well defined.\n ',
	),
	'ConstrainedSketch.autoTrimCurve':(
		'curve1, point1, parameter1',
		'This method automatically trims a selected \n ConstrainedSketchGeometry\n object at the specified location. If the object does not intersect other \n ConstrainedSketchGeometry\n objects, the entire selected object will be deleted.\n ',
	),
	'ConstrainedSketch.breakCurve':(
		'curve1, point1, curve2, point2',
		'This method breaks a specified \n ConstrainedSketchGeometry\n object (\n curve1) using another specified \n ConstrainedSketchGeometry\n object (\n curve2). If the selected \n ConstrainedSketchGeometry\n objects intersect, then only \n curve1\n will be broken; \n curve2\n is not affected by the operation. The location for the break is determined by the specified point values.\n ',
	),
	'ConstrainedSketch.copyMirror':(
		'mirrorLine, objectList',
		'This method creates copies of the given \n ConstrainedSketchGeometry\n objects, mirrors them about a selected line, and inserts them into the appropriate repositories of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.copyMove':(
		'vector, objectList',
		'This method creates copies of the given \n ConstrainedSketchGeometry\n objects, moves them from their original position, and inserts them into the appropriate repositories of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.copyRotate':(
		'centerPoint, angle, objectList',
		'This method creates copies of the given \n ConstrainedSketchGeometry\n objects, rotates them, and inserts them into the appropriate repositories of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.copyScale':(
		'scaleValue, scaleCenter, objectList',
		'This method creates copies of the given \n ConstrainedSketchGeometry\n objects, scales them by the specified value about a selected point, and inserts them into the appropriate repositories of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.delete':(
		'objectList',
		'This method deletes the given \n ConstrainedSketchGeometry, \n ConstrainedSketchDimension, or \n ConstrainedSketchConstraint\n objects.\n ',
	),
	'ConstrainedSketch.deleteParameter':(
		'name',
		'The command deletes a specified parameter.',
	),
	'ConstrainedSketch.dragEntity':(
		'entity, points',
		'This method drags a specified \n ConstrainedSketchGeometry\n or \n ConstrainedSketchVertex\n object to a specific location.\n ',
	),
	'ConstrainedSketch.linearPattern':(
		'number1, spacing1, angle1 <, vertexList, geomList, number2, spacing2, angle2>',
		'This method copies \n ConstrainedSketchGeometry\n objects in a linear pattern along one or two directions. This method also copies any associated dimension or constraint objects that exist between the given objects.\n ',
	),
	'ConstrainedSketch.mergeVertices':(
		'value, vertexList',
		'This method merges the \n ConstrainedSketchVertex\n objects that lie within the specified distance of each other. If only one \n ConstrainedSketchVertex\n object is selected, it will merge all \n ConstrainedSketchVertex\n objects that lie within the specified distance of that vertex. If more than one vertex is selected, the search will be restricted to only the selected \n ConstrainedSketchVertex\n objects.\n ',
	),
	'ConstrainedSketch.move':(
		'vector, objectList',
		'This method translates the given \n ConstrainedSketchGeometry\n objects by the given vector.\n ',
	),
	'ConstrainedSketch.offset':(
		'distance, objectList, side <, filletCorners>',
		"This method creates copies of the selected \n ConstrainedSketchGeometry\n objects, offsets them by the specified distance in the specified direction, and inserts them into the \n ConstrainedSketch\n object's appropriate repositories. If connected objects are selected, trim or extend is carried out to complete the offset.\n ",
	),
	'ConstrainedSketch.print':(
		'',
		'This method prints the following statistics about a sketch:The sketch Id (a positive integer).The number of geometry curves (the number of \n    ConstrainedSketchGeometry\n    objects).\n    The number of dimensions (the number of \n    ConstrainedSketchDimension\n    objects).\n    The number of vertices (the number of \n    ConstrainedSketchVertex\n    objects).\n    ',
	),
	'ConstrainedSketch.radialPattern':(
		'number, totalAngle, centerPoint <, vertexList, geomList>',
		'This method copies \n ConstrainedSketchGeometry\n objects in a radial pattern about a specified center point.\n ',
	),
	'ConstrainedSketch.rectangle':(
		'point1, point2',
		'This method creates four lines that form a rectangle with diagonal corners defined by the given points and inserts them into the \n geometry\n repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketch.removeGapsAndOverlaps':(
		'tolerance, geomList',
		'This method removes gaps and overlaps between sketch geometries specified by the user. This method is particularly useful when cleaning up imported sketches',
	),
	'ConstrainedSketch.repairShortEdges':(
		'geomList <, tolerance>',
		'This method deletes the short edges specified, optionally selecting only those short edges whose lengths are smaller than the specified tolerance and healing the resultant gap in the sketch. This method is particularly useful in conjunction with \n removeGapsAndOverlap\n when cleaning up imported sketches.\n ',
	),
	'ConstrainedSketch.resetView':(
		'',
		'This method resets the view to be perpendicular to the sketching plane.',
	),
	'ConstrainedSketch.retrieveSketch':(
		'sketch',
		'This method copies all \n ConstrainedSketchGeometry, \n ConstrainedSketchDimension, \n ConstrainedSketchConstraint, and \n ConstrainedSketchParameter\n objects from the specified \n ConstrainedSketch\n object. The new objects are added to the existing objects (if any). The objects in the specified \n ConstrainedSketch\n object are not modified by the retrieve operation.\n ',
	),
	'ConstrainedSketch.rotate':(
		'centerPoint, angle, objectList',
		'This method rotates the given \n ConstrainedSketchGeometry\n objects by the given angle and about the given point.\n ',
	),
	'ConstrainedSketch.scale':(
		'scaleValue, scaleCenter, objectList',
		'This method scales the given \n ConstrainedSketchGeometry\n objects by the given scale factor and about the given point.\n ',
	),
	'ConstrainedSketch.setPrimaryObject':(
		'option',
		'This method makes the \n ConstrainedSketch\n object the primary object in the current viewport. The sketch remains the primary object in the current viewport until an \n unsetPrimaryobject\n command is issued.\n ',
	),
	'ConstrainedSketch.trimExtendCurve':(
		'curve1, point1, curve2, point2',
		'This method trims or extends a specified \n ConstrainedSketchGeometry\n object (\n curve1) using another specified \n ConstrainedSketchGeometry\n object (\n curve2). \n curve2\n is not affected by the operation. The location for the trim or extend is determined by the specified point values.\n ',
	),
	'ConstrainedSketch.undo':(
		'',
		'This method undoes the effects of the last \n ConstrainedSketch\n object method.\n ',
	),
	'ConstrainedSketch.unsetPrimaryObject':(
		'',
		'This method removes the \n ConstrainedSketch\n object from the current viewport, reversing the effects of the \n setPrimaryobject\n command. If the \n option\n argument was set to \n SUPERIMPOSE, the viewport will be returned to the view orientation that was in place when the \n setPrimaryobject\n command was issued. If the \n option\n argument was set to \n STANDALONE, the viewport will be left empty.\n ',
	),
	'ConstrainedSketch.writeAcisFile':(
		'fileName <, version>',
		'This method exports the geometry of the sketch to a named file in ACIS format.',
	),
	'ConstrainedSketch.writeIgesFile':(
		'filename <, flavor>',
		'This method exports the geometry of the sketch to a named file in IGES format.',
	),
	'ConstrainedSketchGeometry.getPointAtDistance':(
		'point, distance <, percentage>',
		'This method returns a point offset along the given \n ConstrainedSketchGeometry\n from the given end by a specified arc length distance or a percentage of the total length of the \n ConstrainedSketchGeometry\n object.\n ',
	),
	'ConstrainedSketchGeometry.getSize':(
		'',
		'This method returns the length of the given \n ConstrainedSketchGeometry\n object.\n ',
	),
	'ConstrainedSketchGeometry.getVertices':(
		'',
		'This method returns an list of \n ConstrainedSketchVertex\n objects which are a part of the given \n ConstrainedSketchGeometry\n object.\n ',
	),
	'ConstrainedSketchGeometryArray.Arc3Points':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.ArcByCenterEnds':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.ArcByStartEndTangent':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.CircleByCenterPerimeter':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.ConstructionCircleByCenterPerimeter':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.ConstructionLine':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.EllipseByCenterPerimeter':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.FilletByRadius':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.Line':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.Spline':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchGeometryArray.Spot':(
		'point',
		'This method creates a spot construction point located at the specified coordinates. The spot is added to the vertex repository of the \n ConstrainedSketch\n object.\n ',
	),
	'ConstrainedSketchGeometryArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the \n ConstrainedSketchGeometry\n object located at the given coordinates.\n ',
	),
	'ConstrainedSketchImageOptions.setValues':(
		'<imageName, showImage, origin, xScale, yScale, translucency>',
		'This method modifies the \n ConstrainedSketchOptions\n object.\n ',
	),
	'ConstrainedSketchOptions.setValues':(
		'<sheetSize, gridSpacing, grid, gridFrequency, dimensionTextHeight, decimalPlaces, constructionGeometry, gridSnap, preselection, sheetAuto, gridOrigin, gridAngle, viewStyle, addImpliedConstraints, maxCoplanarEntities, autoConstrainAngularTolerance, autoConstrainLinearTolerance, autoConstrainOptions, dragMethod, editMethod>',
		'This method modifies the \n ConstrainedSketchOptions\n object.\n ',
	),
	'ConstrainedSketchVertexArray.Spot':'<value is a self-reference, replaced by this string>',
	'ConstrainedSketchVertexArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the \n ConstrainedSketchVertex\n located at the given coordinates.\n ',
	),
	'ConstrainedSketcherOptions.setValues':(
		'<constructionGeometry, gridSnap, preselection, addImpliedConstraints, maxCoplanarEntities, autoConstrainAngularTolerance, autoConstrainLinearTolerance, autoConstrainOptions, dragMethod, editMethod>',
		'This method modifies the \n ConstrainedSketchOptions\n object.\n ',
	),
	'Constraint.delete':(
		'indices',
		' This method allows you to delete existing constraints.\n      ',
	),
	'Constraint.resume':(
		'',
		'This method resumes the constraint that was previously suppressed.',
	),
	'Constraint.suppress':(
		'',
		'This method suppresses the constraint.',
	),
	'ConstraintDisplayOptions.setValues':(
		'<constraintEquation, tieConstraint, rigidBodyConstraint, displayBodyConstraint, couplingConstrain>',
		'This method modifies the ConstraintDisplayOptions object.',
	),
	'ContactArea.setValues':'<value is a self-reference, replaced by this string>',
	'ContactDamage.setValues':'<value is a self-reference, replaced by this string>',
	'ContactDamping.setValues':'<value is a self-reference, replaced by this string>',
	'ContactProperty.CohesiveBehavior':(
		'<repeatedContacts, eligibility, defaultPenalties, coupling, temperatureDependency, dependencies, table>',
		'This method creates a CohesiveBehavior object.',
	),
	'ContactProperty.Damage':(
		'initTable <, criterion, initTempDep, initDependencies, useEvolution, evolutionType, softening, useMixedMode, mixedModeType, modeMixRatio, exponent, evolTempDep, evolDependencies, evolTable, useStabilization, viscosityCoef>',
		'This method creates a ContactDamage object.',
	),
	'ContactProperty.Damping':(
		'<definition, tangentFraction, clearanceDependence, table>',
		'This method creates a ContactDamping object.',
	),
	'ContactProperty.ElectricalConductance':(
		'<definition, clearanceDependency, temperatureDependency, dependencies, table>',
		'This method creates an ElectricalConductance object.',
	),
	'ContactProperty.FractureCriterion':(
		'initTable <, type, mixedModeBehavior, temperatureDependency, dependencies, tolerance>',
		'This method creates a FractureCriterion object.',
	),
	'ContactProperty.GapElectricalConductance':(
		'<definition, clearanceDependency, pressureDependency, temperatureDependencyC, dependenciesC, clearanceDepTable, temperatureDependencyP, dependenciesP, pressureDepTable>',
		'This method creates a GapElectricalConductance object.',
	),
	'ContactProperty.GeometricProperties':(
		'<contactArea, padThickness>',
		'This method creates a GeometricProperties object.',
	),
	'ContactProperty.HeatGeneration':(
		'<conversionFraction, slaveFraction>',
		'This method creates a GapHeatGeneration object.',
	),
	'ContactProperty.NormalBehavior':(
		'<contactStiffness, pressureOverclosure, allowSeparation, maxStiffness, table, constraintEnforcementMethod, overclosureFactor, overclosureMeasure, contactStiffnessScaleFactor, initialStiffnessScaleFactor, clearanceAtZeroContactPressure, stiffnessBehavior, stiffnessRatio, upperQuadraticFactor, lowerQuadraticRatio>',
		'This method creates a NormalBehavior object.',
	),
	'ContactProperty.Radiation':(
		'masterEmissivity, slaveEmissivity, table',
		'This method creates a Radiation object.',
	),
	'ContactProperty.TangentialBehavior':(
		'<formulation, directionality, slipRateDependency, pressureDependency, temperatureDependency, dependencies, exponentialDecayDefinition, table, shearStressLimit, maximumElasticSlip, fraction, absoluteDistance, elasticSlipStiffness, nStateDependentVars, useProperties>',
		'This method creates a ContactTangentialBehavior object.',
	),
	'ContactProperty.ThermalConductance':(
		'<definition, clearanceDependency, pressureDependency, temperatureDependencyC, massFlowRateDependencyC, dependenciesC, clearanceDepTable, temperatureDependencyP, massFlowRateDependencyP, dependenciesP, pressureDepTable>',
		'This method creates a ThermalConductance object.',
	),
	'ContactPropertyAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of contact property assignments to new domain pairs in a given step.',
	),
	'ContactPropertyAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of contact property assignments to domain pairs already defined in a given step.',
	),
	'ContactPropertyAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing contact property assignments.',
	),
	'ContactTangentialBehavior.setValues':'<value is a self-reference, replaced by this string>',
	'ContourIntegral.setValues':'<value is a self-reference, replaced by this string>',
	'ContourOptions.setValues':(
		'<options, contourType, contourMethod, tickmarkPlots, contourStyle, numIntervals, intervalType, intervalValues, maxAutoCompute, maxValue, minAutoCompute, minValue, animationAutoLimits, edgeColorLine, edgeColorBandedQuilt, spectrum, outsideLimitsMode, outsideLimitsAboveColor, outsideLimitsBelowColor, intervalLineAttributes, contourEdges, contourEdgeColor, contourEdgeStyle, contourEdgeThickness, tickmarkAxisLength, tickmarkBaseValue, tickmarkOrientation, tickmarkCurveColor, averagedOrientationDisplay, extrapolatedAveraging, showMaxLocation, showMinLocation>',
		'This method modifies the ContourOptions object.',
	),
	'Control.setValues':(
		'<allowPropagation, resetDefaultValues, discontinuous, constraints, lineSearch, timeIncrementation, directCyclic, concentrationField, displacementField, electricalPotentialField, globalField, hydrostaticFluidPressureField, poreFluidPressureField, rotationField, temperatureField>',
		'This method modifies the Control object.',
	),
	'CoriolisForce.setValues':'<value is a self-reference, replaced by this string>',
	'CoriolisForce.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing CoriolisForce object in the specified step.',
	),
	'CoupledTempDisplacementStep.setValues':'<value is a self-reference, replaced by this string>',
	'CoupledThermalElectricStep.setValues':'<value is a self-reference, replaced by this string>',
	'CoupledThermalElectricalStructuralStep.setValues':'<value is a self-reference, replaced by this string>',
	'Coupling.setValues':'<value is a self-reference, replaced by this string>',
	'Crack.resume':(
		'',
		'This method resumes the crack that was previously suppressed.',
	),
	'Crack.suppress':(
		'',
		'This method suppresses the crack.',
	),
	'Creep.Ornl':(
		'<a, h, reset>',
		'This method creates an Ornl object.',
	),
	'Creep.Potential':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a Potential object.',
	),
	'Creep.setValues':'<value is a self-reference, replaced by this string>',
	'CrushableFoam.CrushableFoamHardening':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a CrushableFoamHardening object.',
	),
	'CrushableFoam.RateDependent':(
		'table <, type, temperatureDependency, dependencies>',
		'This method creates a RateDependent object.',
	),
	'CrushableFoam.setValues':'<value is a self-reference, replaced by this string>',
	'CrushableFoamHardening.setValues':'<value is a self-reference, replaced by this string>',
	'CycledPlastic.setValues':'<value is a self-reference, replaced by this string>',
	'CyclicHardening.setValues':'<value is a self-reference, replaced by this string>',
	'CyclicSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'CyclicSymmetry.setValuesInStep':(
		'stepName <, extractedNodalDiameter, lowestNodalDiameter, highestNodalDiameter, excitationNodalDiameter>',
		'This method modifies the propagating data of an existing CyclicSymmetry object in the specified step.',
	),
	'CyclicSymmetry.swapSurfaces':(
		'',
		'This method switches the master and slave surfaces of a cyclic symmetry interaction. This command is valid only during the step in which the interaction is created.',
	),
	'DamageEvolution.setValues':'<value is a self-reference, replaced by this string>',
	'DamageInitiation.DamageEvolution':(
		'type, table <, degradation, temperatureDependency, dependencies, mixedModeBehavior, modeMixRatio, power, softening>',
		'This method creates an DamageEvolution object.',
	),
	'DamageInitiation.DamageStabilization':(
		'fiberTensileCoeff, fiberCompressiveCoeff, matrixTensileCoeff, matrixCompressiveCoeff',
		'This method creates a DamageStabilization object.',
	),
	'DamageInitiation.DamageStabilizationCohesive':(
		'<cohesiveCoeff>',
		'This method creates a DamageStabilizationCohesive object.',
	),
	'DamageInitiation.setValues':'<value is a self-reference, replaced by this string>',
	'DamageStabilization.setValues':'<value is a self-reference, replaced by this string>',
	'DamageStabilizationCohesive.setValues':'<value is a self-reference, replaced by this string>',
	'Damping.setValues':'<value is a self-reference, replaced by this string>',
	'DecayAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'DefaultChartOptions.setValues':(
		'<areaStyle, aspectRatio, defaultAxis1Options, defaultAxis2Options, gridArea, legend, majorAxis1GridStyle, majorAxis2GridStyle, minorAxis1GridStyle, minorAxis2GridStyle, tagAreaStyle, tagBorder, tagTextStyle, useQuantityType>',
		'This method modifies the DefaultChartOptions object.',
	),
	'DeformationPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'Density.setValues':'<value is a self-reference, replaced by this string>',
	'Depvar.setValues':'<value is a self-reference, replaced by this string>',
	'DerivedComponent.CDCTerm':(
		'intrinsicComponents, table <, termOperator, termSign, localDependency, indepCompType, indepComponents, tempDependency, fieldDependencies>',
		'This method creates a CDCTerm object.',
	),
	'DerivedComponent.setValues':'<value is a self-reference, replaced by this string>',
	'DesignDirection.setValues':'<value is a self-reference, replaced by this string>',
	'DetonationPoint.setValues':'<value is a self-reference, replaced by this string>',
	'DiagnosticPrint.setValues':'<value is a self-reference, replaced by this string>',
	'Dielectric.setValues':'<value is a self-reference, replaced by this string>',
	'Diffusivity.PressureEffect':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a PressureEffect object.',
	),
	'Diffusivity.SoretEffect':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a SoretEffect object.',
	),
	'Diffusivity.setValues':'<value is a self-reference, replaced by this string>',
	'DirectCyclicStep.setValues':'<value is a self-reference, replaced by this string>',
	'DiscreteFastener.setValues':'<value is a self-reference, replaced by this string>',
	'DiscreteField.setValues':'<value is a self-reference, replaced by this string>',
	'DisplacementAdaptiveMeshConstraint.setValues':'<value is a self-reference, replaced by this string>',
	'DisplacementAdaptiveMeshConstraint.setValuesInStep':(
		'stepName <, u1, u2, u3, ur1, ur2, ur3, amplitude>',
		'This method modifies the propagating data for an existing DisplacementAdaptiveMeshConstraint object in the specified step.',
	),
	'DisplacementBC.setValues':'<value is a self-reference, replaced by this string>',
	'DisplacementBC.setValuesInStep':(
		'stepName <, u1, u2, u3, ur1, ur2, ur3, amplitude, buckleCase>',
		'This method modifies the propagating data for an existing DisplacementBC object in the specified step.',
	),
	'DisplacementBaseMotionBC.setValues':'<value is a self-reference, replaced by this string>',
	'DisplacementBaseMotionBC.setValuesInStep':(
		'stepName <, amplitude>',
		'This method modifies the propagating data for an existing DisplacementBaseMotionBC object in the specified step.',
	),
	'DisplayBody.setValues':'<value is a self-reference, replaced by this string>',
	'DisplayBodyOptions.setValues':(
		'<options, visibleEdges, edgeColorWireHide, edgeColorFillShade, edgeLineStyle, edgeLineThickness, fillColor, colorCodeOverride, elementShrink, elementShrinkFactor, coordinateScale, coordinateScaleFactors, translucency, translucencyFactor>',
		'This method modifies the DisplayBodyOptions object.',
	),
	'DisplayGroup.add':(
		'leaf',
		'This method adds the specified items to the display group.',
	),
	'DisplayGroup.either':(
		'leaf',
		'This method redefines the display group to be only those items that are not shared by the leaf argument and by the display group.',
	),
	'DisplayGroup.intersect':(
		'leaf',
		'This method redefines the display group to be only those items that are shared by the leaf argument and the display group.',
	),
	'DisplayGroup.print':(
		'',
		'This method returns a String with a tree representation of the display group along with information about the display group.',
	),
	'DisplayGroup.redoLast':(
		'',
		'This method redoes the last undone operation on the display group.',
	),
	'DisplayGroup.remove':(
		'leaf',
		'This method removes the specified items from the display group.',
	),
	'DisplayGroup.replace':(
		'leaf',
		'This method replaces the contents of the display group with the specified items.',
	),
	'DisplayGroup.undoLast':(
		'',
		'This method undoes the last operation performed on the display group.',
	),
	'DisplayGroupInstance.elements':(
		'',
		'This method returns the list of elements present in the DisplayGroupInstance object. The elements method returns a Dictionary object that uses part instance names for the keys. The value of the items in the Dictionary object is a List of user element labels that belong to the part instance and are contained in the DisplayGroupInstance object. This method is available only for DisplayGroupInstance objects that are members of the DisplayGroupInstance repository member of the OdbDisplay object.',
	),
	'DisplayGroupInstance.nodes':(
		'',
		'This method is used to obtain the list of nodes present in the DisplayGroupInstance object. It returns a Dictionary object keyed by part instance names, the value of which is a list of user node labels belonging to the part instance and contained in the DisplayGroupInstance object. This method is available only for DisplayGroupInstance objects that are members of the DisplayGroupInstance repository member of OdbDisplay object.',
	),
	'DisplayGroupInstance.setValues':(
		'<lockOptions>',
		'This method modifies the DisplayGroupInstance object. The setValues method is available only for DisplayGroupInstance objects that are members of the DisplayGroupInstance repository member of the OdbDisplay object. ',
	),
	'DisplayGroupInstanceRepository.syncOptions':(
		'name <, updateInstances>',
		'This method synchronizes the display options stored on the OdbDisplay object with the display options stored on the DisplayGroupInstance object.',
	),
	'DisplayOptions.setValues':(
		'<options, plotState>',
		'This method modifies the DisplayOptions object.',
	),
	'Drawing.addArrayDraw':(
		'type, startIndex, numVertices <, polygonMode>',
		'This method adds a rendering command to the drawing and can be called multiple times to add additional rendering commands.  When the drawing is referenced by a \n Viewport, the drawing commands are used the render the \n Drawing.\n The rendering command constructs the specified type of geometric primitive using \n numVertices\n array elements starting at element index \n startIndex.\n ',
	),
	'Drawing.addIndexDraw':(
		'type, indices <, polygonMode>',
		'This method adds a rendering command to the drawing and can be called multiple times to add additional rendering commands.  When the drawing is referenced by a \n Viewport, the drawing commands are used the render the \n Drawing.\n The rendering command constructs the specified type of geometric primitive using \n numVertices\n array elements starting at element index \n startIndex.\n ',
	),
	'Drawing.setColors':(
		'colorDimension, colorData',
		'This method accepts the color data for each vertex. It defines in an array of colors with a length equal to the length of the \n colorData\n sequence divided by \n colorDimension.\n ',
	),
	'Drawing.setEdgeColor':(
		'edgeColor',
		'This method allows a separate, single color to be used when rendering the edges of the drawing. Once called, edges will be rendered using the specified color but facets will continue to use the colors specified in the \n setColors\n method. An empty sequence can be specified to resume using the colors arrays for edges.\n ',
	),
	'Drawing.setNormals':(
		'normalData',
		'This method accepts the normal data for each vertex. It defines in an array of normal vectors with a length equal to the length of the \n normalData\n sequence divided by 3.\n ',
	),
	'Drawing.setPointColor':(
		'pointColor',
		'This method allows a separate, single color to be used when rendering the points of the drawing. Once called, points will be rendered using the specified color but facets will continue to use the colors specified in the \n setColors\n method. An empty sequence can be specified to resume using the colors arrays for points.\n ',
	),
	'Drawing.setValues':(
		'<show, cullBackfaces, frontFaceOrder, smoothShade, edgesInShaded, translucency, lineSize, pointSize>',
		'This method modifies the rendering of the \n Drawing\n object.\n ',
	),
	'Drawing.setVertices':(
		'vertexDimension, vertexData',
		'This method accepts the vertex data that defines the \n Drawing\n object. It defines in an array of vertices with a length equal to the length of the \n vertexData\n sequence divided by \n vertexDimension.\n ',
	),
	'DrillControl.setValues':'<value is a self-reference, replaced by this string>',
	'DruckerPrager.DruckerPragerCreep':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a DruckerPragerCreep object.',
	),
	'DruckerPrager.DruckerPragerHardening':(
		'table <, type, rate, temperatureDependency, dependencies>',
		'This method creates a DruckerPragerHardening object.',
	),
	'DruckerPrager.RateDependent':'<value is a self-reference, replaced by this string>',
	'DruckerPrager.TriaxialTestData':(
		'table <, a, b, pt>',
		'This method creates a TriaxialTestData object.',
	),
	'DruckerPrager.setValues':'<value is a self-reference, replaced by this string>',
	'DruckerPragerCreep.setValues':'<value is a self-reference, replaced by this string>',
	'DruckerPragerHardening.setValues':'<value is a self-reference, replaced by this string>',
	'Edge.getAdjacentEdges':(
		'',
		'This method returns an array of edge objects that share at least one vertex of the edge.',
	),
	'Edge.getCurvature':(
		'parameter, point',
		'This method returns curvature information at a location on the edge.',
	),
	'Edge.getElements':(
		'',
		'This method returns an array of element objects that are associated with the edge.',
	),
	'Edge.getFaces':(
		'',
		'This method returns a sequence consisting of the face ids of the faces which share this edge.',
	),
	'Edge.getNodes':(
		'',
		'This method returns an array of node objects that are associated with the edge.',
	),
	'Edge.getRadius':(
		'',
		'This method returns the radius of circular edges.',
	),
	'Edge.getSize':(
		'<printResults>',
		'This method returns a Float indicating the length of the edge.',
	),
	'Edge.getVertices':(
		'',
		'This method returns a sequence of indices of the vertices that bound this edge. The first index refers to the vertex where the normalized curve parameter = 0.0, and the second index refers to the vertex where the normalized curve parameter = 1.0. If the edge is a closed curve, only one vertex index is returned.',
	),
	'Edge.index':(
		'keyword argument not implemented',
		'This method returns an Int indicating the index of an Edge object in the EdgeArray.',
	),
	'EdgeArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the object or objects in the EdgeArray located at the given coordinates.findAt \n initially uses the ACIS tolerance of 1E-6. As a result, \n findAt \n returns any edge that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, \n findAt \n uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities). The arbitrary point must not be shared by a second edge. If two edges intersect or coincide at the arbitrary point, \n findAt \n chooses the first edge that it encounters, and you should not rely on the return value being consistent.\n findAt \n will always try to find objects among all the edges in the part or assembly instance and will not restrict itself to a subset even if the EdgeArray represents such subset.\n ',
	),
	'EdgeArray.getBoundingBox':(
		'',
		'This method returns a dictionary of two tuples representing minimum and maximum boundary\n values of the bounding box of the minimum size containing the edge sequence.',
	),
	'EdgeArray.getByBoundingBox':(
		'<xMin, yMin, zMin, xMax, yMax, zMax>',
		'This method returns an array of edge objects that lie within the specified bounding box.',
	),
	'EdgeArray.getByBoundingCylinder':(
		'center1, center2, radius',
		'This method returns an array of edge objects that lie within the specified bounding cylinder.',
	),
	'EdgeArray.getByBoundingSphere':(
		'center, radius',
		'This method returns an array of edge objects that lie within the specified bounding sphere.',
	),
	'EdgeArray.getClosest':(
		'coordinates <, searchTolerance>',
		'This method returns an object or objects in the EdgeArray closest to the given set of points, where the given points need not lie on the edges in the EdgeArray.',
	),
	'EdgeArray.getSequenceFromMask':(
		'mask',
		'This method returns the object or objects in the EdgeArray identified using the specified \n mask. This command is generated when the \n JournalOptions \n are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.\n ',
	),
	'Elastic.FailStrain':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a FailStrain object.',
	),
	'Elastic.FailStress':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a FailStress object.',
	),
	'Elastic.setValues':'<value is a self-reference, replaced by this string>',
	'ElasticFoundation.setValues':'<value is a self-reference, replaced by this string>',
	'ElasticFoundation.setValuesInStep':(
		'stepName <, stiffness>',
		'This method modifies the propagating data of an existing ElasticFoundation object in the specified step.',
	),
	'ElectricPotentialBC.setValues':'<value is a self-reference, replaced by this string>',
	'ElectricPotentialBC.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ElectricPotentialBC object in the specified step.',
	),
	'ElectricalConductance.setValues':'<value is a self-reference, replaced by this string>',
	'ElectricalConductivity.setValues':'<value is a self-reference, replaced by this string>',
	'EmagTimeHarmonicStep.setValues':'<value is a self-reference, replaced by this string>',
	'EmbeddedRegion.setValues':'<value is a self-reference, replaced by this string>',
	'EngineeringFeature.AssembledFastener':(
		'name, region, templateModel, controlSet, templateSurfaces, assignedSurfaces, propertyPrefix <, orientMethod, localCsys, scriptName>',
		'This method creates an AssembledFastener object. Although the constructor is available both for parts and for the assembly, AssembledFastener objects are currently supported only under the assembly.',
	),
	'EngineeringFeature.ContourIntegral':(
		'name, crackFront, crackTip, extensionDirectionMethod <, symmetric, listOfRegions, crackFrontName, crackTipName, crackNormal, qVectors, midNodePosition, collapsedElementAtTip>',
		'This method creates a ContourIntegral object. Although the constructor is available both for parts and for the assembly, ContourIntegral objects are currently supported only under the assembly.',
	),
	'EngineeringFeature.DiscreteFastener':(
		'name, region, influenceRadius <, ur1, ur2, ur3, coupling, weightingMethod, localCsys>',
		'This method creates a DiscreteFastener object. Although the constructor is available both for parts and for the assembly, DiscreteFastener objects are currently supported only under the assembly.',
	),
	'EngineeringFeature.HeatCapacitance':(
		'name, region, table <, temperatureDependency, dependencies>',
		'This method creates a HeatCapacitance object.',
	),
	'EngineeringFeature.NonstructuralMass':(
		'name, region, units, magnitude <, distribution>',
		'This method creates a NonstructuralMass object.',
	),
	'EngineeringFeature.PointFastener':(
		'name, region, physicalRadius <, directionVector, targetSurfaces, ur1, ur2, ur3, attachmentMethod, influenceRadius, searchRadius, maximumLayers, coupling, weightingMethod, additionalMass, adjustOrientation, localCsys, connectionType, sectionName, connectorOrientationLocalCsys1, axis1, angle1, orient2SameAs1, connectorOrientationLocalCsys2, axis2, angle2, unsorted>',
		'This method creates a PointFastener object. Although the constructor is available both for parts and for the assembly, PointFastener objects are currently supported only under the assembly.',
	),
	'EngineeringFeature.PointMassInertia':(
		'name, region <, mass, mass1, mass2, mass3, i11, i22, i33, i12, i13, i23, localCsys, alpha, composite>',
		'This method creates a PointMassInertia object.',
	),
	'EngineeringFeature.SpringDashpotToGround':(
		'name, region, dof <, orientation, springBehavior, dashpotBehavior, springStiffness, dashpotCoefficient>',
		'This method creates a SpringDashpotToGround object.',
	),
	'EngineeringFeature.TwoPointSpringDashpot':(
		'name, regionPairs, axis <, dof1, dof2, orientation, springBehavior, dashpotBehavior, springStiffness, dashpotCoefficient>',
		'This method creates a TwoPointSpringDashpot object.',
	),
	'EngineeringFeature.XFEMCrack':(
		'name, crackDomain <, allowCrackGrowth, crackLocation, singularityCalcRadius, interactionProperty, elemId, nodeId, hasCrackFront, crackPlaneDist, crackFrontDist>',
		'This method creates a XFEMCrack object. Although the constructor is available both for parts and for the assembly, XFEMCrack objects are currently supported only under the assembly.',
	),
	'EngineeringFeature.assignSeam':(
		'regions',
		'This method creates a seam crack along an edge or a face.',
	),
	'EngineeringFeature.deleteSeam':(
		'regions',
		'This method deletes a seam crack.',
	),
	'EngineeringFeatureDisplayOptions.setValues':(
		'<pointMassInertia, nonstructuralMass, heatCapacitance, contourIntegral, springToGround, twoPointSpring>',
		'This method modifies the EngineeringFeatureDisplayOptions object.',
	),
	'Eos.DetonationPoint':(
		'table',
		'This method creates a DetonationPoint object.',
	),
	'Eos.EosCompaction':(
		'soundSpeed, porosity, pressure, compactionPressure',
		'This method creates a EosCompaction object.',
	),
	'Eos.setValues':'<value is a self-reference, replaced by this string>',
	'EosCompaction.setValues':'<value is a self-reference, replaced by this string>',
	'EpsOptions.setValues':(
		'<imageSize, units, resolution, fontType, imageFormat, shadingQuality>',
		'This method modifies the \n EpsOptions\n object.\n ',
	),
	'EquallySpacedAmplitude.BaselineCorrection':(
		'<intervals>',
		'This method creates a BaselineCorrection object.',
	),
	'EquallySpacedAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'Equation.setValues':'<value is a self-reference, replaced by this string>',
	'EulerianBC.setValues':(
		'<region, definition, inflowType, outflowType>',
		'This method modifies the data for an existing EulerianBC object in the step where it is created.',
	),
	'EulerianBC.setValuesInStep':(
		'stepName <, definition, inflowType, outflowType>',
		'This method modifies the propagating data for an existing EulerianBC object in the specified step.',
	),
	'EulerianMotionBC.setValues':(
		'<instanceName, followRegion, region, materialName, ctrPosition1, posPosition1, negPosition1, expansionRatio1, contractRatio1, ctrPosition2, posPosition2, negPosition2, expansionRatio2, contractRatio2, ctrPosition3, posPosition3, negPosition3, expansionRatio3, contractRatio3, allowContraction, aspectLimit, vmaxFactor, volThreshold, bufferSize>',
		'This method modifies the data for an existing EulerianMotionBC object in the step where it is created.',
	),
	'EulerianMotionBC.setValuesInStep':(
		'stepName <, ctrPosition1, posPosition1, negPosition1, expansionRatio1, contractRatio1, ctrPosition2, posPosition2, negPosition2, expansionRatio2, contractRatio2, ctrPosition3, posPosition3, negPosition3, expansionRatio3, contractRatio3, allowContraction, aspectLimit, vmaxFactor, volThreshold, bufferSize>',
		'This method modifies the propagating data for an existing EulerianMotionBC object in the specified step.',
	),
	'EulerianSection.setValues':'<value is a self-reference, replaced by this string>',
	'ExpContactControl.setValues':'<value is a self-reference, replaced by this string>',
	'Expansion.setValues':'<value is a self-reference, replaced by this string>',
	'ExplicitDynamicsStep.setValues':'<value is a self-reference, replaced by this string>',
	'ExpressionField.setValues':'<value is a self-reference, replaced by this string>',
	'Face.getAdjacentFaces':(
		'',
		'This method returns an array of face objects that share at least one edge of the face.',
	),
	'Face.getCells':(
		'',
		'This method returns a sequence consisting of the cell ids of the cells to which this face belongs.',
	),
	'Face.getCentroid':(
		'',
		'This method returns the centroid of a face.',
	),
	'Face.getCurvature':(
		'point, uParam, vParam',
		'This method returns information about the curvature at a location on the face.',
	),
	'Face.getEdges':(
		'',
		'This method returns a sequence consisting of the edge ids of the edges on the face.',
	),
	'Face.getElementFaces':(
		'<side>',
		'This method returns an array of mesh face objects. Each mesh face object contains the element label and the side of the element    that lies on the geometric face.',
	),
	'Face.getElements':(
		'',
		'This method returns an array of element objects that are associated with the face.',
	),
	'Face.getFacesByFaceAngle':(
		'angle',
		'This method returns an array of Face objects that are obtained by recursively finding adjacent faces that are at an angle of less than or equal to the specified angle.',
	),
	'Face.getNodes':(
		'<side>',
		'This method returns an array of mesh node objects. Each mesh node object contains the label of the node that lies on the geometric face.',
	),
	'Face.getNormal':(
		'<point>',
		'This method returns the normal to a face at the location specified by the \n pointOn \n member. The normal at a different location on the face can be obtained by specifying the optional \n point \n argument.\n ',
	),
	'Face.getSize':(
		'<printResults>',
		'This method returns a Float indicating the area of the face.',
	),
	'Face.getVertices':(
		'',
		'This method returns a sequence consisting of the vertex ids of the vertices of the face.',
	),
	'Face.index':(
		'keyword argument not implemented',
		'This method returns the index of a Face in the FaceArray.',
	),
	'Face.isNormalFlipped':(
		'',
		'This method determines whether the normal to the face is flipped from\n its default direction by the use of the \n FlipNormal \n method on a Part object.\n ',
	),
	'FaceArray.findAt':(
		'coordinates <, normal, printWarning>',
		'This method returns the object or objects in the FaceArray located at the given coordinates.findAt \n initially uses the ACIS tolerance of 1E-6. As a result, \n findAt \n returns any face that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, \n findAt \n uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities). The arbitrary point must not be shared by a second face. If two faces intersect or coincide at the arbitrary point, \n findAt \n chooses the first face that it encounters, and you should not rely on the return value being consistent.\n findAt \n will always try to find objects among all the faces in the part or assembly instance and will not restrict itself to a subset even if the FaceArray represents such subset.\n ',
	),
	'FaceArray.getBoundingBox':(
		'',
		'This method returns a dictionary of two tuples representing minimum and maximum boundary\n values of the bounding box of the minimum size containing the face sequence.',
	),
	'FaceArray.getByBoundingBox':(
		'<xMin, yMin, zMin, xMax, yMax, zMax>',
		'This method returns an array of face objects that lie within the specified bounding box.',
	),
	'FaceArray.getByBoundingCylinder':(
		'center1, center2, radius',
		'This method returns an array of face objects that lie within the specified bounding cylinder.',
	),
	'FaceArray.getByBoundingSphere':(
		'center, radius',
		'This method returns an array of face objects that lie within the specified bounding sphere.',
	),
	'FaceArray.getClosest':(
		'coordinates <, searchTolerance>',
		'This method returns an object or objects in the FaceArray closest to the given set of points, where the given points need not lie on the faces in the FaceArray.',
	),
	'FaceArray.getSequenceFromMask':(
		'mask',
		'This method returns the object or objects in the FaceArray identified using the specified \n mask. This command is generated when the \n JournalOptions \n are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.\n ',
	),
	'FailStrain.setValues':'<value is a self-reference, replaced by this string>',
	'FailStress.setValues':'<value is a self-reference, replaced by this string>',
	'FailureRatios.setValues':'<value is a self-reference, replaced by this string>',
	'Fastener.resume':(
		'',
		'This method resumes the fastener that was previously suppressed.',
	),
	'Fastener.suppress':(
		'',
		'This method suppresses the fastener.',
	),
	'Feature.isSuppressed':(
		'',
		'This method queries the suppressed state of the feature.',
	),
	'Feature.restore':(
		'',
		'This method restores the parameters of a feature to the value they had when the backup method was invoked on the part or assembly. Use the restore method after the backup method.',
	),
	'Feature.resume':(
		'',
		'This method resumes suppressed features. Resuming a feature fully restores it to the part or assembly. You can resume the last feature you suppressed, all suppressed features, or just selected features. When you resume a child feature, Abaqus/CAE also resumes the parent features automatically.',
	),
	'Feature.setValues':(
		'<parameter, parameter1, parameter2, sketch, distance>',
		'This method modifies the Feature object.',
	),
	'Feature.suppress':(
		'',
		'This method suppresses features. Suppressing a feature is equivalent to temporarily removing the feature from the part or assembly. Suppressed features remain suppressed when you regenerate a part or assembly. You cannot suppress the base feature. In addition, if you suppress a parent feature, all of its child features are also suppressed automatically. Suppressed features can be restored with the resume command.',
	),
	'FeatureOptions.setValues':(
		'<autoRegeneration, checkSelfIntersection, autoCaching, maxCachedStates>',
		'This method modifies the FeatureOptions object for the specified model.',
	),
	'FieldOutput.addData':(
		'position, set, data <, sectionPoint, conjugateData>',
		'This method adds data to a \n FieldOutput \n object.\n ',
	),
	'FieldOutput.getScalarField':(
		'componentLabel',
		'This method generates a scalar field containing the extracted component or calculated invariant values. The new field will hold values for the same nodes or elements as the parent field. Abaqus will perform this operation on only the real part of the \n FieldOutput \n object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).\n ',
	),
	'FieldOutput.getSubset':(
		'<elementType>',
		'A \n FieldOutput \n object with a subset of the field values.\n ',
	),
	'FieldOutput.getTransformedField':(
		'datumCsys <, deformationField, rotationField, projected22Axis, projectionTol>',
		'This method generates a new vector or tensor field containing the transformed component values of the parent field. The new field will hold values for the same nodes or elements as the parent field. Results will be transformed based on the orientations specified by the input \n DatumCsys \n object. Abaqus will perform this operation on only the real part of the \n FieldOutput \n object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).\n ',
	),
	'FieldOutputRequest.deactivate':(
		'stepName',
		'This method deactivates the field output request in the specified step and all its subsequent steps.',
	),
	'FieldOutputRequest.move':(
		'fromStepName, toStepName',
		'This method moves the field output request state object from one step to a different step.',
	),
	'FieldOutputRequest.reset':(
		'stepName',
		'This method resets the field output request state of the specified step to the state of the previous step.',
	),
	'FieldOutputRequest.resume':(
		'',
		'This method resumes the field output request that was previously suppressed.',
	),
	'FieldOutputRequest.setValues':'<value is a self-reference, replaced by this string>',
	'FieldOutputRequest.setValuesInStep':(
		'stepName <, variables, frequency, modes, timeInterval, numIntervals, timePoints, timeMarks>',
		'This method modifies the propagating data for an existing FieldOutputRequest object in the specified step.',
	),
	'FieldOutputRequest.suppress':(
		'',
		'This method suppresses the field output request.',
	),
	'FieldReportOptions.NumberFormat':(
		'<blankPad, format, numDigits, precision>',
		'This method creates a NumberFormat object.',
	),
	'FieldReportOptions.setValues':(
		'<numColumns, numberFormat, printXYData, printTotal, printMinMax, pageWidth, columnLayout, sort>',
		'This method modifies the FieldReportOptions object.',
	),
	'FilmCondition.setValues':'<value is a self-reference, replaced by this string>',
	'FilmCondition.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data of an existing FilmCondition object in the specified step.',
	),
	'FilmConditionProp.setValues':'<value is a self-reference, replaced by this string>',
	'FixedRegion.setValues':'<value is a self-reference, replaced by this string>',
	'FlowStep.setValues':'<value is a self-reference, replaced by this string>',
	'FluidCavity.setValues':'<value is a self-reference, replaced by this string>',
	'FluidCavityPressure.setValues':'<value is a self-reference, replaced by this string>',
	'FluidCavityPressureBC.setValues':'<value is a self-reference, replaced by this string>',
	'FluidCavityPressureBC.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing FluidCavityPressureBC object in the specified step.',
	),
	'FluidCavityProperty.setValues':'<value is a self-reference, replaced by this string>',
	'FluidDensity.setValues':'<value is a self-reference, replaced by this string>',
	'FluidExchange.setValues':'<value is a self-reference, replaced by this string>',
	'FluidExchangeProperty.setValues':'<value is a self-reference, replaced by this string>',
	'FluidInletOutletBC.setValues':'<value is a self-reference, replaced by this string>',
	'FluidInletOutletBC.setValuesInStep':(
		'stepName <, momentumType, pressure, v1, v2, v3, momentumAmplitude, temperature, temperatureAmplitude, kineticEnergy, kineticEnergyAmplitude, dissipationRate, dissipationRateAmplitude, eddyViscosity, eddyViscosityAmplitude>',
		'This method modifies the propagating data for an existing FluidInletOutletBC object in the specified step.',
	),
	'FluidLeakoff.setValues':'<value is a self-reference, replaced by this string>',
	'FluidThermalEnergy.setValues':'<value is a self-reference, replaced by this string>',
	'FluidTurbulence.setValues':'<value is a self-reference, replaced by this string>',
	'FluidVelocity.setValues':'<value is a self-reference, replaced by this string>',
	'FluidWallConditionBC.setValues':'<value is a self-reference, replaced by this string>',
	'FluidWallConditionBC.setValuesInStep':(
		'stepName <, type, v1, v2, v3, velocityAmplitude, thermalEnergyType, temperature, heatFlux, thermalEnergyAmplitude, kineticEnergy, kineticEnergyAmplitude, dissipationRate, dissipationRateAmplitude, eddyViscosity, eddyViscosityAmplitude>',
		'This method modifies the propagating data for an existing FluidWallConditionBC object in the specified step.',
	),
	'FractureCriterion.setValues':'<value is a self-reference, replaced by this string>',
	'FreeBodyOptions.setValues':(
		'<comp1ColorF, comp1ColorM, comp2ColorF, comp2ColorM, comp3ColorF, comp3ColorM, resultantColorF, resultantColorM, textColorF, textColorM, textFontF, textFontM, numberFormatF, numberFormatM, scaleModeF, scaleModeM, vectorDisplay, numDigitsF, numDigitsM, sizePercentageF, sizePercentageM, thresholdF, thresholdM, drawLabelF, drawLabelM, showComp1F, showComp1M, showComp2F, showComp2M, showComp3F, showComp3M, showForce, showMoment, constantLengthArrow>',
		'This method modifies the FreeBodyOptions object.',
	),
	'FreeBodyReportOptions.setValues':(
		'<numDigits, forceThreshold, momentThreshold, numberFormat, reportFormat, csysType>',
		'This method modifies the FreeBodyReportOptions object.',
	),
	'FrequencyStep.setValues':'<value is a self-reference, replaced by this string>',
	'FrozenArea.setValues':'<value is a self-reference, replaced by this string>',
	'GapElectricalConductance.setValues':'<value is a self-reference, replaced by this string>',
	'GapFlow.setValues':'<value is a self-reference, replaced by this string>',
	'GapHeatGeneration.setValues':'<value is a self-reference, replaced by this string>',
	'GasketMembraneElastic.setValues':'<value is a self-reference, replaced by this string>',
	'GasketSection.setValues':'<value is a self-reference, replaced by this string>',
	'GasketThicknessBehavior.ContactArea':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a ContactArea object.',
	),
	'GasketThicknessBehavior.setValues':'<value is a self-reference, replaced by this string>',
	'GasketTransverseShearElastic.setValues':'<value is a self-reference, replaced by this string>',
	'Gel.setValues':'<value is a self-reference, replaced by this string>',
	'GeneralField.move':(
		'fromStepName, toStepName',
		'This method moves the GeneralFieldState object from one step to a different step.',
	),
	'GeneralField.setValues':'<value is a self-reference, replaced by this string>',
	'GeneralField.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data for an existing GeneralField object in the specified step.',
	),
	'GeneralStiffnessSection.RebarLayers':(
		'rebarSpacing, layerTable',
		'This method creates a RebarLayers object.',
	),
	'GeneralStiffnessSection.setValues':'<value is a self-reference, replaced by this string>',
	'GeneralizedProfile.setValues':'<value is a self-reference, replaced by this string>',
	'GeometricProperties.setValues':'<value is a self-reference, replaced by this string>',
	'GeometricRestrictionDisplayOptions.setValues':(
		'<drillControl, fixedRegion, frozenArea, growth, penetrationCheck, shapeDemoldControl, designDirection, shapeMemberSize, shapePlanarSymmetry, shapePointSymmetry, shapeRotationalSymmetry, stampControl, slideRegionControl, topologyCyclicSymmetry, topologyDemoldControl, topologyOverhangControl, topologyMemberSize, topologyPlanarSymmetry, topologyPointSymmetry, topologyRotationalSymmetry, turnControl>',
		'This method modifies the GeometricRestrictionDisplayOptions object.',
	),
	'GeometryDisplayOptions.setValues':(
		'<geometryEdgesInShaded, geometryHiddenEdges, geometrySilhouetteEdges, datumAxes, datumCoordSystems, datumPlanes, referencePointLabels, referencePointSymbols, referenceRepresentation, referenceRepTranslucency>',
		'This method modifies the GeometryDisplayOptions object.',
	),
	'GeometryShellSection.RebarLayers':'<value is a self-reference, replaced by this string>',
	'GeostaticStep.setValues':'<value is a self-reference, replaced by this string>',
	'GraphicsOptions.setValues':(
		'<graphicsDriver, doubleBuffering, displayLists, highlightMethodHint, dragMode, antiAlias, autoFitAfterRotate, polygonOffsetConstant, polygonOffsetSlope, printPolygonOffsetConstant, printPolygonOffsetSlope, vertexArrays, vertexArraysInDisplayLists, viewManipDisplayListThreshold, directRendering, hardwareAcceleration, hardwareOverlay, textureMapping, printTextureMapping, backgroundStyle, backgroundColor, backgroundBottomColor, backgroundOverride, backfaceCulling, accelerateOffScreen, backingStore, shadersAvailable, translucencyMode, options, contourRangeTexturePrecision>',
		'This method modifies the \n GraphicsOptions \n object.\n ',
	),
	'Gravity.setValues':'<value is a self-reference, replaced by this string>',
	'Gravity.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing Gravity object in the specified step.',
	),
	'Growth.setValues':'<value is a self-reference, replaced by this string>',
	'HeatCapacitance.setValues':'<value is a self-reference, replaced by this string>',
	'HeatTransferStep.setValues':'<value is a self-reference, replaced by this string>',
	'HexagonalProfile.setValues':'<value is a self-reference, replaced by this string>',
	'HistoryOutput.addData':(
		'data',
		'This method adds data to the data member of the HistoryOutput object.',
	),
	'HistoryOutputRequest.deactivate':(
		'stepName',
		'This method deactivates the history output request in the specified step and all subsequent steps.',
	),
	'HistoryOutputRequest.move':(
		'fromStepName, toStepName',
		'This method moves the history output request state object from one step to a different step.',
	),
	'HistoryOutputRequest.reset':(
		'stepName',
		'This method resets the history output request state of the specified step to the state of the previous step.',
	),
	'HistoryOutputRequest.resume':(
		'',
		'This method resumes the history output request that was previously suppressed.',
	),
	'HistoryOutputRequest.setValues':'<value is a self-reference, replaced by this string>',
	'HistoryOutputRequest.setValuesInStep':(
		'stepName <, variables, frequency, modes, timeInterval, numIntervals, timePoints>',
		'This method modifies the propagating data for an existing HistoryOutputRequest object in the specified step.',
	),
	'HistoryOutputRequest.suppress':(
		'',
		'This method suppresses the history output request.',
	),
	'HistoryRegion.HistoryOutput':(
		'name, description, type <, validInvariants>',
		'This method creates a HistoryOutput object.',
	),
	'HistoryRegion.HistoryPoint':(
		'instance',
		'This method creates a HistoryPoint object for the OdbInstance object.',
	),
	'HistoryRegion.getSubset':(
		'start, end',
		'This method returns a subset of the data in the HistoryRegion object.',
	),
	'HomogeneousShellSection.setValues':'<value is a self-reference, replaced by this string>',
	'HomogeneousSolidSection.setValues':'<value is a self-reference, replaced by this string>',
	'HydrostaticFluidFlow.setValues':'<value is a self-reference, replaced by this string>',
	'HydrostaticFluidFlow.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing HydrostaticFluidFlow object in the specified step.',
	),
	'Hyperelastic.BiaxialTestData':(
		'table <, smoothing, lateralNominalStrain, temperatureDependency, dependencies>',
		'This method creates a BiaxialTestData object.',
	),
	'Hyperelastic.Hysteresis':(
		'table',
		'This method creates a Hysteresis object.',
	),
	'Hyperelastic.PlanarTestData':(
		'table <, smoothing, lateralNominalStrain, temperatureDependency, dependencies>',
		'This method creates a PlanarTestData object.',
	),
	'Hyperelastic.UniaxialTestData':(
		'table <, smoothing, lateralNominalStrain, temperatureDependency, dependencies>',
		'This method creates a UniaxialTestData object.',
	),
	'Hyperelastic.VolumetricTestData':(
		'table <, volinf, smoothing, temperatureDependency, dependencies>',
		'This method creates a VolumetricTestData object.',
	),
	'Hyperelastic.setValues':'<value is a self-reference, replaced by this string>',
	'Hyperfoam.BiaxialTestData':'<value is a self-reference, replaced by this string>',
	'Hyperfoam.PlanarTestData':'<value is a self-reference, replaced by this string>',
	'Hyperfoam.SimpleShearTestData':(
		'table',
		'This method creates a SimpleShearTestData object.',
	),
	'Hyperfoam.UniaxialTestData':'<value is a self-reference, replaced by this string>',
	'Hyperfoam.VolumetricTestData':'<value is a self-reference, replaced by this string>',
	'Hyperfoam.setValues':'<value is a self-reference, replaced by this string>',
	'Hypoelastic.setValues':'<value is a self-reference, replaced by this string>',
	'Hysteresis.setValues':'<value is a self-reference, replaced by this string>',
	'IProfile.setValues':'<value is a self-reference, replaced by this string>',
	'IgnoredEdge.getCurvature':(
		'parameter, point',
		'This method returns curvature information at a location on the \n IgnoredEdge \n object.\n ',
	),
	'IgnoredEdge.getRadius':(
		'',
		'This method returns the radius of a circular \n IgnoredEdge \n object.\n ',
	),
	'IgnoredEdge.getSize':'<value is a self-reference, replaced by this string>',
	'IgnoredEdge.index':(
		'keyword argument not implemented',
		'This method returns an Int indicating the index of an \n IgnoredEdge \n object in the IgnoredEdgeArray.\n ',
	),
	'IgnoredEdgeArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the object or objects in the IgnoredEdgeArray located at the given coordinates.findAt \n initially uses the ACIS tolerance of 1E-6. As a result, \n findAt \n returns any \n IgnoredEdge \n that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, \n findAt \n uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities). The arbitrary point must not be shared by a second \n IgnoredEdge. If two \n IgnoredEdge \n objects intersect or coincide at the arbitrary point, \n findAt \n chooses the first \n IgnoredEdge \n that it encounters, and you should not rely on the return value being consistent.\n findAt \n will always try to find objects among all the ignored edges in the part or assembly instance and will not restrict itself to a subset even if the IgnoredEdgeArray represents such subset.\n ',
	),
	'IgnoredEdgeArray.getClosest':(
		'coordinates <, searchTolerance>',
		'This method returns a object or objects in the IgnoredEdgeArray closest to the given set of points, where the given points need not lie on the edges in the IgnoredEdgeArray.',
	),
	'IgnoredEdgeArray.getSequenceFromMask':(
		'mask',
		'This method returns the object or objects in the IgnoredEdgeArray identified using the specified \n mask. This command is generated when the \n JournalOptions \n are set to COMPRESSEDINDEX. When large number of objects are involved, this method is highly efficient.\n ',
	),
	'IgnoredVertex.index':(
		'keyword argument not implemented',
		'This method returns the index of an IgnoredVertex in the IgnoredVertexArray.',
	),
	'IgnoredVertexArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the object or objects in the IgnoredVertexArray located at the given coordinates.findAt \n initially uses the ACIS tolerance of 1E-6. As a result, \n findAt \n returns any \n IgnoredVertex \n object that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, \n findAt \n uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities).\n findAt \n will always try to find objects among all the ignored vertices in the part or assembly instance and will not restrict itself to a subset even if the IgnoredVertexArray represents such subset.\n ',
	),
	'IgnoredVertexArray.getClosest':(
		'coordinates <, searchTolerance>',
		'This method returns a object or objects in the IgnoredVertexArray closest to the given set of points, where the given points need not lie on the vertices in the IgnoredVertexArray.',
	),
	'IgnoredVertexArray.getSequenceFromMask':(
		'mask',
		'This method returns the object or objects in the IgnoredVertexArray identified using the specified \n mask. This command is generated when the \n JournalOptions \n are set to COMPRESSEDINDEX. When large number of objects are involved, this method is highly efficient.\n ',
	),
	'Image.ImageFromMovie':(
		'name, movieName, frame, time',
		'This method creates an \n Image\n object from a given frame of an existing \n Movie\n object.\n ',
	),
	'ImageAnimation.close':(
		'',
		'This method closes the ImageAnimation object.',
	),
	'ImageAnimation.closed':(
		'',
		'This method indicates if the ImageAnimation is open or closed for writing animation frames.',
	),
	'ImageAnimation.writeFrame':(
		'<canvasObjects>',
		'This method adds a frame to the ImageAnimation object.',
	),
	'ImageAnimationOptions.setValues':(
		'<frameRate, timeScale, vpDecorations, vpBackground, compass>',
		'This method modifies the ImageAnimationOptions object.',
	),
	'ImageOptions.setValues':(
		'<imageName, showImage, positionMethod, fitMethod, alignment, xScale, yScale, origin, translucency, options>',
		'This method modifies the \n ImageOptions \n object.\n ',
	),
	'ImplicitDynamicsStep.setValues':'<value is a self-reference, replaced by this string>',
	'IncidentWave.WaveReflection':(
		'reflectionCoefficient, datumPlane',
		'This method creates a WaveReflection object.',
	),
	'IncidentWave.setValues':'<value is a self-reference, replaced by this string>',
	'IncidentWaveProperty.setValues':'<value is a self-reference, replaced by this string>',
	'InelasticHeatFraction.setValues':'<value is a self-reference, replaced by this string>',
	'Inertia.resume':(
		'',
		'This method resumes the inertia that was previously suppressed.',
	),
	'Inertia.suppress':(
		'',
		'This method suppresses the inertia.',
	),
	'InertiaRelief.setValues':'<value is a self-reference, replaced by this string>',
	'InertiaRelief.setValuesInStep':(
		'stepName <, u1, u2, u3, ur1, ur2, ur3, referencePoint, fixed>',
		'This method modifies the propagating data for an existing InertiaRelief object in the specified step.',
	),
	'InitialState.setValues':'<value is a self-reference, replaced by this string>',
	'InitializationAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of contact initialization assignments to new domain pairs in a given step.',
	),
	'InitializationAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of contact initialization assignments to domain pairs already defined in a given step.',
	),
	'InitializationAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing contact initialization assignments from a ContactStd object.',
	),
	'IntegratedOutputSection.setValues':'<value is a self-reference, replaced by this string>',
	'Interaction.deactivate':(
		'stepName',
		'This method deactivates the interaction in the specified step and all its subsequent steps.',
	),
	'Interaction.delete':(
		'indices',
		' This method allows you to delete existing interactions.\n      ',
	),
	'Interaction.move':(
		'fromStepName, toStepName',
		'This method moves an interaction from one step to another.',
	),
	'Interaction.reset':(
		'stepName',
		'This method reactivates an interaction that was deactivated previously. The reset method is available during the step in which the interaction was deactivated originally.',
	),
	'Interaction.resume':(
		'',
		'This method resumes an interaction that was previously suppressed.',
	),
	'Interaction.suppress':(
		'',
		'This method suppresses an interaction.',
	),
	'InteractionDisplayOptions.setValues':(
		'<surfaceContact, selfContact, elasticFoundation, actuatorSensor, radiationAmbient, filmCondition, concentratedRadiationToAmbient, concentratedFilmCondition>',
		'This method modifies the InteractionDisplayOptions object.',
	),
	'InwardVolAccel.setValues':'<value is a self-reference, replaced by this string>',
	'InwardVolAccel.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing InwardVolAccel object in the specified step.',
	),
	'Job._Message':(
		'',
		'This method creates a Message object.',
	),
	'Job.kill':(
		'',
		'This method kills the analysis of a job.',
	),
	'Job.submit':(
		'<consistencyChecking, datacheckJob, continueJob>',
		'This method submits a job for analysis.',
	),
	'Job.waitForCompletion':(
		'',
		'This method interrupts the execution of the script until the end of the analysis. If you call the waitForCompletion method and the status member is neither SUBMITTED nor RUNNING, Abaqus assumes the analysis has either completed or aborted and returns immediately. ',
	),
	'JobFromInputFile.setValues':'<value is a self-reference, replaced by this string>',
	'JouleHeatFraction.setValues':'<value is a self-reference, replaced by this string>',
	'JournalOptions.NumberFormat':'<value is a self-reference, replaced by this string>',
	'JournalOptions.setValues':(
		'<replayGeometry, recoverGeometry, defaultFormat, fieldReportFormat, geometryFormat>',
		'This method modifies the \n JournalOptions\n object.\n ',
	),
	'KeywordBlock.insert':(
		'position, text',
		'This method inserts a String at a specified position in the \n sieBlocks \n member.\n ',
	),
	'KeywordBlock.replace':(
		'position, text',
		'This method replaces a String at a specified position in the \n sieBlocks \n member.\n ',
	),
	'KeywordBlock.setValues':(
		'<edited>',
		'This method modifies the \n KeywordBlock \n object.\n ',
	),
	'KeywordBlock.synchVersions':(
		'storeNodesAndElements',
		'This method synchronizes, or merges,  the edits made in this object with those made in the model using other scripting commands or the user interface.  The \n synchVersions \n method updates the \n sieBlocks \n member. The \n sieBlocks \n member is empty prior to the first call to \n synchVersions. As a side effect, \n synchVersions \n sets \n lastSynchCount \n to the current value of the counter associated with the \n Mdb \n object, which is used to determine if synchronization is necessary.\n ',
	),
	'KinematicHardening.setValues':'<value is a self-reference, replaced by this string>',
	'LProfile.setValues':'<value is a self-reference, replaced by this string>',
	'LatentHeat.setValues':'<value is a self-reference, replaced by this string>',
	'Layer.moveAfter':(
		'name',
		'This method moves the layer object after another object in the layer repository.',
	),
	'Layer.moveBefore':(
		'name',
		'This method moves the layer object before another object in the layer repository.',
	),
	'Legend.setValues':(
		'<legend, show, showMinMax, title, numberFormat, numDigits, textStyle, titleStyle>',
		'This method modifies the Legend object.',
	),
	'Light.setValues':(
		'<enabled, type, latitude, longitude, diffuseColor, specularColor>',
		'This method modifies the \n Light \n object.\n ',
	),
	'LightOptions.setValues':(
		'<shading, viewpoint, ambientColor, materialShininess>',
		'This method modifies the \n LightOptions \n object.\n ',
	),
	'LineLoad.setValues':'<value is a self-reference, replaced by this string>',
	'LineLoad.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing LineLoad object in the specified step.',
	),
	'LineStyle.setValues':(
		'<color, show, style, thickness>',
		'This method modifies the LineStyle object.',
	),
	'Load.deactivate':(
		'stepName',
		'This method deactivates the load in the specified step and all its subsequent steps.',
	),
	'Load.delete':(
		'indices',
		' This method allows you to delete existing loads.\n      ',
	),
	'Load.move':(
		'fromStepName, toStepName',
		'This method moves the load state object from one step to a different step.',
	),
	'Load.reset':(
		'stepName',
		'This method resets the load state of the specified step to the state of the previous general analysis step.',
	),
	'Load.resume':(
		'',
		'This method resumes the load that was previously suppressed.',
	),
	'Load.suppress':(
		'',
		'This method suppresses the load.',
	),
	'LoadCase.resume':(
		'',
		'This method resumes the load case that was previously suppressed.',
	),
	'LoadCase.setValues':'<value is a self-reference, replaced by this string>',
	'LoadCase.suppress':(
		'',
		'This method suppresses the load case.',
	),
	'LoadDisplayOptions.setValues':(
		'<concentratedForce, moment, pressure, pipePressure, bodyForce, lineLoad, gravity, boltLoad, pegLoad, connectorForce, connectorMoment, inertiaRelief, rotationalIntertiaLoad, coriolisForce, bodyHeatFlux, surfaceHeatFlux, concentratedHeatFlux, concentratedPoreFluid, surfacePoreFluid, hydroFluidFlow, concentratedCharge, concentratedCurrent, surfaceCharge, surfaceCurrent, bodyCharge, bodyCurrent, inwardVolAccel, bodyConcentrationFlux, surfaceConcentrationFlux, concentratedConcentrationFlux>',
		'This method modifies the LoadDisplayOptions object.',
	),
	'LocalStopCondition.setValues':'<value is a self-reference, replaced by this string>',
	'LowDensityFoam.UniaxialTestData':'<value is a self-reference, replaced by this string>',
	'LowDensityFoam.setValues':'<value is a self-reference, replaced by this string>',
	'MagneticPermeability.setValues':'<value is a self-reference, replaced by this string>',
	'MagneticVectorPotentialBC.setValues':'<value is a self-reference, replaced by this string>',
	'MagneticVectorPotentialBC.setValuesInStep':(
		'stepName <, component1, component2, component3, amplitude>',
		'This method modifies the propagating data for an existing MagneticVectorPotentialBC object in the specified step.',
	),
	'MappedField.OdbMeshRegionData':(
		'odbFileName, variableLabel <, stepIndex, frameIndex, outputPosition, dataType, storageType, quantityToPlot, averageElementOutput, useRegionBoundaries, regionBoundaries, includeFeatureBoundaries, featureAngle, averageOnlyDisplayed, averagingThreshold, computeOrder, numericForm, complexAngle>',
		'This method creates an OdbMeshRegionData object.',
	),
	'MappedField.setValues':'<value is a self-reference, replaced by this string>',
	'MassDiffusionStep.setValues':'<value is a self-reference, replaced by this string>',
	'MassFlowRate.move':(
		'fromStepName, toStepName',
		'This method moves the MassFlowState object from one step to a different step.',
	),
	'MassFlowRate.setValues':'<value is a self-reference, replaced by this string>',
	'MassFlowRate.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data for an existing MassFlowRate object in the specified step. The arguments to setValuesInStep are the same as the arguments to the MassFlowRate method, except for the name, createStepName, and region. All arguments are optional. In addition the following argument is required.',
	),
	'MasterSlaveAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of master-slave assignments to new surface pairs in a given step.',
	),
	'MasterSlaveAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of master-slave assignments already defined on surface pairs in a given step.',
	),
	'MasterSlaveAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing master-slave assignments.',
	),
	'Material.AcousticMedium':(
		'<acousticVolumetricDrag, temperatureDependencyB, temperatureDependencyV, dependenciesB, dependenciesV, bulkTable, volumetricTable>',
		'This method creates an AcousticMedium object.',
	),
	'Material.BrittleCracking':(
		'table <, temperatureDependency, dependencies, type>',
		'This method creates an BrittleCracking object.',
	),
	'Material.CapPlasticity':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a CapPlasticity object.',
	),
	'Material.CastIronPlasticity':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a CastIronPlasticity object.',
	),
	'Material.ClayPlasticity':(
		'table <, intercept, hardening, temperatureDependency, dependencies>',
		'This method creates a ClayPlasticity object.',
	),
	'Material.Concrete':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a Concrete object.',
	),
	'Material.ConcreteDamagedPlasticity':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a ConcreteDamagedPlasticity object.',
	),
	'Material.Conductivity':(
		'table <, type, temperatureDependency, dependencies>',
		'This method creates a Conductivity object.',
	),
	'Material.Creep':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a Creep object.',
	),
	'Material.CrushableFoam':(
		'table <, hardening, temperatureDependency, dependencies>',
		'This method creates a CrushableFoam object.',
	),
	'Material.Damping':(
		'<alpha, beta, composite, structural>',
		'This method creates a Damping object.',
	),
	'Material.DeformationPlasticity':(
		'table <, temperatureDependency>',
		'This method creates a DeformationPlasticity object.',
	),
	'Material.Density':(
		'table <, temperatureDependency, dependencies, distributionType, fieldName>',
		'This method creates a Density object.',
	),
	'Material.Depvar':(
		'<deleteVar, n>',
		'This method creates a Depvar object.',
	),
	'Material.Dielectric':(
		'table <, type, frequencyDependency, temperatureDependency, dependencies>',
		'This method creates a Dielectric object.',
	),
	'Material.Diffusivity':(
		'table <, type, law, temperatureDependency, dependencies>',
		'This method creates a Diffusivity object.',
	),
	'Material.DruckerPrager':(
		'table <, shearCriterion, eccentricity, testData, temperatureDependency, dependencies>',
		'This method creates a DruckerPrager object.',
	),
	'Material.DuctileDamageInitiation':(
		'table <, definition, feq, fnn, fnt, frequency, ks, numberImperfections, temperatureDependency, dependencies, alpha, omega, tolerance, direction>',
		'This method creates a DamageInitiation object.',
	),
	'Material.Elastic':(
		'table <, type, noCompression, noTension, temperatureDependency, dependencies, moduli>',
		'This method creates an Elastic object.',
	),
	'Material.ElectricalConductivity':(
		'table <, type, frequencyDependency, temperatureDependency, dependencies>',
		'This method creates an ElectricalConductivity object.',
	),
	'Material.Eos':(
		'<type, temperatureDependency, dependencies, detonationEnergy, solidTable, gasTable, reactionTable, gasSpecificTable, table>',
		' This method creates an Eos object.\n    ',
	),
	'Material.Expansion':(
		'<type, userSubroutine, zero, temperatureDependency, dependencies, table>',
		'This method creates an Expansion object.',
	),
	'Material.FldDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.FlsdDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.FluidLeakoff':(
		'<temperatureDependency, dependencies, type, table>',
		'This method creates an FluidLeakoff object.',
	),
	'Material.GapFlow':(
		'table <, kmax, temperatureDependency, dependencies, type>',
		'This method creates an GapFlow object.',
	),
	'Material.GasketMembraneElastic':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a GasketMembraneElastic object.',
	),
	'Material.GasketThicknessBehavior':(
		'table <, temperatureDependency, dependencies, tensileStiffnessFactor, type, unloadingDependencies, unloadingTemperatureDependency, variableUnits, yieldOnset, yieldOnsetMethod, unloadingTable>',
		'This method creates a GasketThicknessBehavior object.',
	),
	'Material.GasketTransverseShearElastic':(
		'table <, variableUnits, temperatureDependency, dependencies>',
		'This method creates a GasketTransverseShearElastic object.',
	),
	'Material.Gel':(
		'table',
		'This method creates a Gel object.',
	),
	'Material.HashinDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.HeatGeneration':(
		'',
		'This method creates a HeatGeneration object.',
	),
	'Material.Hyperelastic':(
		'table <, type, moduliTimeScale, temperatureDependency, n, beta, testData, compressible, properties, deviatoricResponse, volumetricResponse, poissonRatio, materialType, anisotropicType, formulation, behaviorType, dependencies, localDirections>',
		'This method creates a Hyperelastic object.',
	),
	'Material.Hyperfoam':(
		'<testData, poisson, n, temperatureDependency, moduli, table>',
		'This method creates a Hyperfoam object.',
	),
	'Material.Hypoelastic':(
		'table <, user>',
		'This method creates a Hypoelastic object.',
	),
	'Material.InelasticHeatFraction':(
		'<fraction>',
		'This method creates an InelasticHeatFraction object.',
	),
	'Material.JohnsonCookDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.JouleHeatFraction':(
		'<fraction>',
		'This method creates a JouleHeatFraction object.',
	),
	'Material.LatentHeat':(
		'table',
		'This method creates a LatentHeat object.',
	),
	'Material.LowDensityFoam':(
		'<elementRemoval, maxAllowablePrincipalStress, extrapolateStressStrainCurve, strainRateType, mu0, mu1, alpha>',
		'This method creates a LowDensityFoam object.',
	),
	'Material.MagneticPermeability':(
		'table <, type, frequencyDependency, temperatureDependency, dependencies>',
		'This method creates an MagneticPermeability object.',
	),
	'Material.MaxeDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.MaxpeDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.MaxpsDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.MaxsDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.MkDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.MohrCoulombPlasticity':(
		'table <, deviatoricEccentricity, meridionalEccentricity, temperatureDependency, dependencies, useTensionCutoff>',
		'This method creates a MohrCoulombPlasticity object.',
	),
	'Material.MoistureSwelling':(
		'table',
		'This method creates a MoistureSwelling object.',
	),
	'Material.MsfldDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.Permeability':(
		'specificWeight, inertialDragCoefficient, table <, type, temperatureDependency, dependencies>',
		'This method creates a Permeability object.',
	),
	'Material.Piezoelectric':(
		'table <, type, temperatureDependency, dependencies>',
		'This method creates a Piezoelectric object.',
	),
	'Material.Plastic':(
		'table <, hardening, rate, dataType, strainRangeDependency, numBackstresses, temperatureDependency, dependencies>',
		'This method creates a Plastic object.',
	),
	'Material.PoreFluidExpansion':(
		'table <, zero, temperatureDependency, dependencies>',
		'This method creates a PoreFluidExpansion object.',
	),
	'Material.PorousBulkModuli':(
		'table <, temperatureDependency>',
		'This method creates a PorousBulkModuli object.',
	),
	'Material.PorousElastic':(
		'table <, shear, temperatureDependency, dependencies>',
		'This method creates a PorousElastic object.',
	),
	'Material.PorousMetalPlasticity':(
		'table <, relativeDensity, temperatureDependency, dependencies>',
		'This method creates a PorousMetalPlasticity object.',
	),
	'Material.QuadeDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.QuadsDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.Regularization':(
		'<rtol, strainRateRegularization>',
		'This method creates a Regularization object.',
	),
	'Material.Shear':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a Shear object.',
	),
	'Material.ShearDamageInitiation':'<value is a self-reference, replaced by this string>',
	'Material.Solubility':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a Solubility object.',
	),
	'Material.Sorption':(
		'absorptionTable <, lawAbsorption, exsorption, lawExsorption, scanning, exsorptionTable>',
		'This method creates a Sorption object.',
	),
	'Material.SpecificHeat':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a SpecificHeat object.',
	),
	'Material.Swelling':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a Swelling object.',
	),
	'Material.UserDefinedField':(
		'',
		'This method defines a UserDefinedField object.',
	),
	'Material.UserMaterial':(
		'<type, unsymm, mechanicalConstants, thermalConstants>',
		'This method creates a UserMaterial object.',
	),
	'Material.UserOutputVariables':(
		'<n>',
		'This method creates a UserOutputVariables object.',
	),
	'Material.Viscoelastic':(
		'domain, table <, frequency, type, preload, time, errtol, nmax, volumetricTable>',
		'This method creates a Viscoelastic object.',
	),
	'Material.Viscosity':(
		'table <, type, temperatureDependency, dependencies>',
		'This method creates a Viscosity object.',
	),
	'Material.Viscous':(
		'table <, law, temperatureDependency, dependencies>',
		'This method creates a Viscous object.',
	),
	'MaterialAssignment.setValues':'<value is a self-reference, replaced by this string>',
	'MaterialFlowBC.setValues':'<value is a self-reference, replaced by this string>',
	'MaterialFlowBC.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing MaterialFlowBC object in the specified step.',
	),
	'MaterialOrientation.setValues':'<value is a self-reference, replaced by this string>',
	'Mdb.AdaptivityProcess':(
		'name, job <, maxIterations, jobPrefix>',
		'This method creates an AdaptivityProcess object.',
	),
	'Mdb.Arrow':(
		'name <, startPoint, endPoint, startAnchor, endAnchor, startHeadStyle, endHeadStyle, startGap, endGap, color, lineStyle, lineThickness>',
		'This method creates an \n Arrow\n object.\n ',
	),
	'Mdb.Job':(
		'name, model <, description, type, queue, waitHours, waitMinutes, atTime, echoPrint, contactPrint, modelPrint, historyPrint, scratch, userSubroutine, numCpus, memory, memoryUnits, explicitPrecision, nodalOutputPrecision, parallelizationMethodExplicit, numDomains, activateLoadBalancing, multiprocessingMode>',
		'This method creates an analysis job using a model on a model database (MDB) for the model definition.',
	),
	'Mdb.JobFromInputFile':(
		'name, inputFileName <, type, queue, waitHours, waitMinutes, atTime, scratch, userSubroutine, numCpus, memory, memoryUnits, explicitPrecision, nodalOutputPrecision, parallelizationMethodExplicit, numDomains, activateLoadBalancing, multiprocessingMode>',
		'This method creates an analysis job using an input file for the model definition.',
	),
	'Mdb.Model':(
		'name <, description, stefanBoltzmann, absoluteZero, waveFormulation, modelType, universalGas>',
		'This method creates a Model object.',
	),
	'Mdb.ModelFromInputFile':(
		'name, inputFileName',
		'This method creates a Model object by reading the keywords in an input file and creating the corresponding Abaqus/CAE objects.',
	),
	'Mdb.ModelFromNastranFile':(
		'modelName, inputFileName <, sectionConsolidation, preIntegratedShell, weightMassScaling, loadCases, coupleBeamOffsets, cbar, cquad4, chexa, ctetra, keepTranslatedFiles>',
		'This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran input file and creating any corresponding Abaqus/CAE objects. The default values is discussed in following and can be defined alternatively in the Abaqus environment file as the one used for the translator from Nastran to Abaqus. For more information, see \n .\n ',
	),
	'Mdb.ModelFromOdbFile':(
		'name, odbFileName',
		'This method creates a Model object by reading an output database and creating any corresponding Abaqus/CAE objects.',
	),
	'Mdb.OptimizationProcess':(
		'name, model, task, prototypeJob <, description, maxDesignCycle>',
		'This method creates an OptimizationProcess object.',
	),
	'Mdb.Text':(
		'name <, text, offset, anchor, referencePoint, rotationAngle, color, font, backgroundStyle, backgroundColor, box, justification>',
		'This method creates a \n Text \n object.\n ',
	),
	'Mdb.close':(
		'',
		'This method closes an open \n Mdb \n object but does not save the \n Mdb \n object to disk. After closing the \n Mdb \n object, this method creates a new unnamed empty \n Mdb \n object.\n ',
	),
	'Mdb.closeAuxMdb':(
		'',
		'This method closes the auxiliary \n Mdb \n which had been opened earlier using the \n openAuxMdb \n command.\n ',
	),
	'Mdb.copyAuxMdbModel':(
		'fromName <, toName>',
		'This method copies a specified model from the auxiliary \n Mdb \n which had been opened earlier using the \n openAuxMdb \n command.\n ',
	),
	'Mdb.getAuxMdbModelNames':(
		'',
		'This method returns a list of model names present in the auxiliary \n Mdb \n which had been opened earlier using the \n openAuxMdb \n command.\n ',
	),
	'Mdb.openAcis':(
		'fileName <, scaleFromFile>',
		'This method creates an AcisFile object from a file containing ACIS-format geometry. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.openAuxMdb':(
		'pathName',
		'This method opens an auxiliary \n Mdb \n object on the disk at the specified location. This enables models from the auxiliary \n Mdb \n object to be copied into the current \n Mdb.\n ',
	),
	'Mdb.openCatia':(
		'fileName <, topology, convertUnits, combineBodies>',
		'This method creates an AcisFile object from a file containing CATIA V4-format or V5&#8211;format geometry. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.openEnf':(
		'fileName, fileType <, topology, convertUnits>',
		'This method creates an AcisFile object from a file containing Elysium Neutral File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.openIges':(
		'fileName <, trimCurve, scaleFromFile, msbo, includedLayers, topology, uniteWires>',
		'This method creates an AcisFile object from a file containing IGES-format geometry. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.openParasolid':(
		'fileName <, topology>',
		'This method creates an AcisFile object from a file containing Parasolid-format geometry. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.openStep':(
		'fileName <, scale>',
		'This method creates an AcisFile object from a file containing STEP-format geometry. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.openVda':(
		'fileName',
		'This method creates an AcisFile object from a file containing VDA-FS-format geometry. This object is subsequently used by the PartFromGeometryFile method.',
	),
	'Mdb.save':(
		'',
		'This method saves an \n Mdb \n object to disk at the location specified by \n pathName (pathName is a member of the \n Mdb \n object).\n ',
	),
	'Mdb.saveAs':(
		'pathName',
		'This method saves an \n Mdb \n object to disk at the specified location.\n ',
	),
	'MembraneSection.RebarLayers':'<value is a self-reference, replaced by this string>',
	'MembraneSection.setValues':'<value is a self-reference, replaced by this string>',
	'MemoryReductionOptions.setValues':(
		'<reducedMemoryMode, percentThreshold>',
		'This method modifies the \n MemoryReductionOptions\n object.\n ',
	),
	'MeshDisplayOptions.setValues':(
		'<nodeLabels, elementLabels, meshVisibleEdges, featureAngle, meshEdgesInShaded, meshTechnique, seeds>',
		'This method modifies the MeshDisplayOptions object.',
	),
	'MeshEdge.getElemFaces':(
		'',
		'This method returns a tuple of unique element faces that share the element edge.',
	),
	'MeshEdge.getElements':(
		'',
		'This method returns a tuple of elements that share the element edge.',
	),
	'MeshEdge.getNodes':(
		'',
		'This method returns a tuple of nodes on the element edge.',
	),
	'MeshEdgeArray.getSequenceFromMask':(
		'mask',
		'This method returns the objects in the MeshEdgeArray identified using the specified mask. When large number of objects are involved, this method is highly efficient.',
	),
	'MeshEditOptions.setValues':(
		'<maxUndoCacheElements, enableUndo, _suspendUndo>',
		'This method modifies the \n MeshEditOptions \n object.\n ',
	),
	'MeshElement.getAdjacentElements':(
		'',
		'This method returns an array of element objects adjacent to the mesh element.',
	),
	'MeshElement.getElemEdges':(
		'',
		'This method returns a tuple of unique element edge objects on the element.',
	),
	'MeshElement.getElemFaces':(
		'',
		'This method returns a tuple of unique element face objects on the element.',
	),
	'MeshElement.getNodes':(
		'',
		'This method returns a tuple of node objects of the element.',
	),
	'MeshElement.setValues':(
		'<label>',
		'This method modifies the MeshElement object.',
	),
	'MeshElementArray.getBoundingBox':(
		'',
		'This method returns a dictionary of two tuples representing minimum and maximum boundary \t\t\t\t\t\t values of the bounding box of the minimum size containing the element sequence. \t\t\t\t\t ',
	),
	'MeshElementArray.getByBoundingBox':(
		'<xMin, yMin, zMin, xMax, yMax, zMax>',
		'This method returns an array of element objects that lie within the specified bounding box.',
	),
	'MeshElementArray.getByBoundingCylinder':(
		'center1, center2, radius',
		'This method returns an array of element objects that lie within the specified bounding cylinder.',
	),
	'MeshElementArray.getByBoundingSphere':(
		'center, radius',
		'This method returns an array of element objects that lie within the specified bounding sphere.',
	),
	'MeshElementArray.getFromLabel':(
		'label',
		'This method returns the object in the MeshElementArray with the given label.',
	),
	'MeshElementArray.getSequenceFromMask':(
		'mask',
		'This method returns the objects in the MeshElementArray identified using the specified mask. This command is generated when the JournalOptions are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.',
	),
	'MeshElementArray.sequenceFromLabels':(
		'labels',
		'This method returns the objects in the MeshElementArray identified using the specified labels. ',
	),
	'MeshFace.getElemEdges':(
		'',
		'This method returns a tuple of unique element edges on the element face.',
	),
	'MeshFace.getElemFacesByFaceAngle':(
		'<angle>',
		'This method returns an array of mesh Element Face objects \n\t\t\t\t\t that are obtained by recursively finding adjacent element faces \n\t\t\t\t\t that are at an angle of less than or equal to the specified angle.',
	),
	'MeshFace.getElements':(
		'',
		'This method returns a tuple of elements that share the element face.',
	),
	'MeshFace.getElementsByFaceAngle':(
		'<angle>',
		'This method returns an array of mesh Element objects \n\t\t\t\t\t that are obtained by recursively finding adjacent element faces \n\t\t\t\t\t that are at an angle of less than or equal to the specified angle.',
	),
	'MeshFace.getNodes':(
		'',
		'This method returns a tuple of nodes on the element face.',
	),
	'MeshFace.getNodesByFaceAngle':(
		'<angle>',
		'This method returns an array of mesh Node objects \n\t\t\t\t\t that are obtained by recursively finding adjacent element faces \n\t\t\t\t\t that are at an angle of less than or equal to the specified angle.',
	),
	'MeshFaceArray.getSequenceFromMask':(
		'mask',
		'This method returns the objects in the MeshFaceArray identified using the specified mask. When large number of objects are involved, this method is highly efficient.',
	),
	'MeshNode.getElemEdges':(
		'',
		'This method returns a tuple of element edge objects that share the node.',
	),
	'MeshNode.getElemFaces':(
		'',
		'This method returns a tuple of element face objects that share the node.',
	),
	'MeshNode.getElements':(
		'',
		'This method returns a tuple of element objects that share the node.',
	),
	'MeshNode.setValues':(
		'<label>',
		'This method modifies the MeshNode object.',
	),
	'MeshNodeArray.getBoundingBox':(
		'',
		'This method returns a dictionary of two tuples representing minimum and maximum boundary values of the bounding box of the minimum size containing the node sequence.',
	),
	'MeshNodeArray.getByBoundingBox':(
		'<xMin, yMin, zMin, xMax, yMax, zMax>',
		'This method returns an array of nodes that lie within the specified bounding box.',
	),
	'MeshNodeArray.getByBoundingCylinder':(
		'center1, center2, radius',
		'This method returns an array of node objects that lie within the specified bounding cylinder.',
	),
	'MeshNodeArray.getByBoundingSphere':(
		'center, radius',
		'This method returns an array of node objects that lie within the specified bounding sphere.',
	),
	'MeshNodeArray.getFromLabel':(
		'label',
		'This method returns the object in the MeshNodeArray with the given label.',
	),
	'MeshNodeArray.getSequenceFromMask':(
		'mask',
		'This method returns the objects in the MeshNodeArray identified using the specified mask. This command is generated when the JournalOptions are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.',
	),
	'MeshNodeArray.sequenceFromLabels':(
		'labels',
		'This method returns the objects in the MeshNodeArray identified using the specified labels.',
	),
	'MesherOptions.setValues':(
		'<elemShape2D, elemShape3D, quadAlgorithm, allowMapped, minTransition>',
		'This method modifies the MesherOptions object.',
	),
	'ModalDynamicsStep.setValues':'<value is a self-reference, replaced by this string>',
	'Model.AccelerationBC':(
		'name, createStepName, region <, fieldName, a1, a2, a3, ar1, ar2, ar3, amplitude, localCsys, distributionType>',
		'This method creates an AccelerationBC object.',
	),
	'Model.AccelerationBaseMotionBC':(
		'name, createStepName, dof <, amplitudeScaleFactor, centerOfRotation, correlation, secondaryBase, useComplex, amplitude>',
		'This method creates a AccelerationBaseMotionBC object.',
	),
	'Model.AcousticImpedance':(
		'name, createStepName, surface <, definition, interactionProperty, nonreflectingType, radius, semimajorAxis, eccentricity, centerCoordinates, directionCosine>',
		'This method creates an AcousticImpedance object.',
	),
	'Model.AcousticImpedanceProp':(
		'name, tableType, table <, frequencyDependency>',
		'This method creates an AcousticImpedanceProp object.',
	),
	'Model.AcousticInfiniteSection':(
		'name, material <, thickness, order>',
		'This method creates an AcousticInfiniteSection object.',
	),
	'Model.AcousticInterfaceSection':(
		'name <, thickness>',
		'This method creates an AcousticInterfaceSection object.',
	),
	'Model.AcousticPressureBC':(
		'name, createStepName, region <, fieldName, magnitude, distributionType, amplitude, fixed>',
		'This method creates a AcousticPressureBC object.',
	),
	'Model.ActuatorAmplitude':(
		'name <, timeSpan>',
		'This method creates a ActuatorAmplitude object.',
	),
	'Model.ActuatorSensor':(
		'name, createStepName, point, interactionProperty, noCoordComponents, unsymm, noSolutionDepVar, userSubUel, dof, solutionDepVars',
		'This method creates an ActuatorSensor object.',
	),
	'Model.ActuatorSensorProp':(
		'name <, realProperties, integerProperties>',
		'This method creates an ActuatorSensorProp object.',
	),
	'Model.AdaptiveMeshControl':(
		'name <, remapping, smoothingAlgorithm, smoothingPriority, initialFeatureAngle, transitionFeatureAngle, momentumAdvection, meshingPredictor, curvatureRefinement, volumetricSmoothingWeight, laplacianSmoothingWeight, equipotentialSmoothingWeight, meshConstraintAngle, originalConfigurationProjectionWeight, standardVolumetricSmoothingWeight>',
		'This method creates an AdaptiveMeshControl object.',
	),
	'Model.AdjustPoints':(
		'name, surface, controlPoints',
		'This method creates an AdjustPoints object.',
	),
	'Model.AnnealStep':(
		'name, previous <, description, refTemp, _solverInput, maintainAttributes>',
		'This method creates an AnnealStep object. ',
	),
	'Model.ArbitraryProfile':(
		'name, table',
		'This method creates a ArbitraryProfile object.',
	),
	'Model.BeamSection':(
		'name, integration, profile <, poissonRatio, thermalExpansion, temperatureDependency, dependencies, density, referenceTemperature, temperatureVar, alphaDamping, betaDamping, compositeDamping, useFluidInertia, submerged, fluidMassDensity, crossSectionRadius, lateralMassCoef, axialMassCoef, massOffsetX, massOffsetY, beamShape, material, table, outputPts, centroid, shearCenter, profileEnd>',
		'This method creates a BeamSection object.',
	),
	'Model.BodyCharge':(
		'name, createStepName, region, magnitude <, amplitude, distributionType, field>',
		'This method creates a BodyCharge object.',
	),
	'Model.BodyConcentrationFlux':(
		'name, createStepName, region, magnitude <, field, distributionType, amplitude>',
		'This method creates a BodyConcentrationFlux object.',
	),
	'Model.BodyCurrent':(
		'name, createStepName, region, magnitude <, amplitude, distributionType, field>',
		'This method creates a BodyCurrent object.',
	),
	'Model.BodyCurrentDensity':(
		'name, createStepName, region, comp1, comp2, comp3 <, amplitude, distributionType>',
		'This method creates a BodyCurrentDensity object.',
	),
	'Model.BodyForce':(
		'name, createStepName, region <, field, distributionType, comp1, comp2, comp3, amplitude>',
		'This method creates a BodyForce object.',
	),
	'Model.BodyHeatFlux':(
		'name, createStepName, region, magnitude <, field, distributionType, amplitude>',
		'This method creates a BodyHeatFlux object.',
	),
	'Model.BoltLoad':(
		'name, createStepName, region, magnitude, datumAxis <, boltMethod, amplitude>',
		'This method creates a BoltLoad object.',
	),
	'Model.BondedContact':(
		'name, region, interactionName',
		"This method creates a BondedContact object.The Bonded Contact modeling paradigm is about as unclear as can be. For example, it's probably going to be called something like Crack Propagation. We may even just have the Interaction object in CAE and then make it internally initialize PredefinedField related data needed for the Solver.",
	),
	'Model.BoxProfile':(
		'name, a, b, uniformThickness, t1 <, t2, t3, t4>',
		'This method creates a BoxProfile object.',
	),
	'Model.BuckleStep':(
		'name, previous, numEigen <, description, eigensolver, minEigen, maxEigen, vectors, maxIterations, blockSize, maxBlocks, matrixStorage, _solverInput, maintainAttributes>',
		'This method creates a BuckleStep object.',
	),
	'Model.ButterworthFilter':(
		'name, cutoffFrequency <, order, operation, halt, limit, invariant>',
		'This method creates a ButterworthFilter object.',
	),
	'Model.Calibration':(
		'name',
		'This method creates a \n Calibration\n object.\n ',
	),
	'Model.CavityRadiation':(
		'name, createStepName, surfaces <, surfaceEmissivities, ambientTemp, blocking, blockingSurfaces, rangeOfView, surfaceReflection, viewfactorAccurTol, minInfinitesimalRatio, numPointsPerEdge, minLumpedAreaDS, cyclicSymmetry, cyclicImages, cyclicRotPt, cyclicRotEndPt, cyclicSymPt, periodicSymmetries, periodicImages_1, periodicImages_2, periodicImages_3, periodicSymAxis_1, periodicSymAxis_2, periodicSymPlane_1, periodicSymPlane_2, periodicSymPlane_3, periodicDistance_1, periodicDistance_2, periodicDistance_3, periodicSymZ, periodicDistZ, reflectionSymmetries, reflectionSymAxis_1, reflectionSymAxis_2, reflectionSymPlane_1, reflectionSymPlane_2, reflectionSymPlane_3, reflectionSymZ>',
		'This method creates a CavityRadiation object.',
	),
	'Model.CavityRadiationProp':(
		'name <, temperatureDependency, dependencies, property>',
		'This method creates a CavityRadiationProp object.',
	),
	'Model.Chebyshev1Filter':(
		'name, cutoffFrequency <, rippleFactor, order, operation, halt, limit, invariant>',
		'This method creates a Chebyshev1Filter object.',
	),
	'Model.Chebyshev2Filter':(
		'name, cutoffFrequency <, rippleFactor, order, operation, halt, limit, invariant>',
		'This method creates a Chebyshev2Filter object.',
	),
	'Model.CircularProfile':(
		'name, r',
		'This method creates a CircularProfile object.',
	),
	'Model.CohesiveSection':(
		'name, response, material <, initialThicknessType, initialThickness, outOfPlaneThickness>',
		'This method creates a CohesiveSection object.',
	),
	'Model.ComplexFrequencyStep':(
		'name, previous <, numEigen, description, shift, frictionDamping, matrixStorage, _solverInput, maintainAttributes, minEigen, maxEigen, propertyEvaluationFrequency>',
		'This method creates a ComplexFrequencyStep object. ',
	),
	'Model.CompositeShellSection':'<value is a self-reference, replaced by this string>',
	'Model.CompositeSolidSection':(
		'name, layup <, symmetric, layupName>',
		'This method creates a CompositeSolidSection object.',
	),
	'Model.ConcCharge':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a ConcCharge object.',
	),
	'Model.ConcConcFlux':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a ConcConcFlux object.',
	),
	'Model.ConcCurrent':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a ConcCurrent object.',
	),
	'Model.ConcPoreFluid':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a ConcPoreFluid object.',
	),
	'Model.ConcentratedFilmCondition':(
		'name, createStepName, region, definition <, nodalArea, explicitRegionType, interactionProperty, field, sinkTemperature, sinkAmplitude, filmCoeff, filmCoeffAmplitude, sinkFieldName, sinkDistributionType>',
		'This method creates a ConcentratedFilmCondition object.',
	),
	'Model.ConcentratedForce':(
		'name, createStepName, region <, distributionType, field, cf1, cf2, cf3, amplitude, follower, localCsys>',
		'This method creates a ConcentratedForce object.',
	),
	'Model.ConcentratedHeatFlux':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude, dof>',
		'This method creates a ConcentratedHeatFlux object.',
	),
	'Model.ConcentratedRadiationToAmbient':(
		'name, createStepName, region, ambientTemperature, ambientTemperatureAmp, emissivity <, nodalArea, explicitRegionType, field, distributionType>',
		'This method creates a ConcentratedRadiationToAmbient object.',
	),
	'Model.Concentration':(
		'name, region, magnitude',
		'This method creates a Concentration object.',
	),
	'Model.ConcentrationBC':(
		'name, createStepName, region <, fieldName, magnitude, distributionType, amplitude, fixed>',
		'This method creates a ConcentrationBC object.',
	),
	'Model.ConnAccelerationBC':(
		'name, createStepName <, region, fastenerName, fastenerSetName, a1, a2, a3, ar1, ar2, ar3, amplitude, distributionType>',
		'This method creates an ConnAccelerationBC object on a wire region.  Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.',
	),
	'Model.ConnDisplacementBC':(
		'name, createStepName <, region, fastenerName, fastenerSetName, u1, u2, u3, ur1, ur2, ur3, fixed, amplitude, distributionType, buckleCase>',
		'This method creates a ConnDisplacementBC object on a wire region.  Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.',
	),
	'Model.ConnVelocityBC':(
		'name, createStepName <, region, fastenerName, fastenerSetName, v1, v2, v3, vr1, vr2, vr3, amplitude, distributionType>',
		'This method creates a ConnVelocityBC object on a wire region.  Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.',
	),
	'Model.ConnectorForce':(
		'name, createStepName <, region, fastenerName, fastenerSetName, f1, f2, f3, amplitude>',
		'This method creates a ConnectorForce object on a wire region.  Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.',
	),
	'Model.ConnectorMoment':(
		'name, createStepName <, region, fastenerName, fastenerSetName, m1, m2, m3, amplitude>',
		'This method creates a ConnectorMoment object on a wire region.  Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.',
	),
	'Model.ConnectorSection':(
		'name <, assembledType, rotationalType, translationalType, integration, u1ReferenceLength, u2ReferenceLength, u3ReferenceLength, ur1ReferenceAngle, ur2ReferenceAngle, ur3ReferenceAngle, massPerLength, contactAngle, materialFlowFactor, regularize, defaultTolerance, regularization, extrapolation, behaviorOptions>',
		'This method creates a ConnectorSection object.',
	),
	'Model.ConstrainedSketch':(
		'name, objectToCopy',
		'This method copies one \n ConstrainedSketch\n object to a new \n ConstrainedSketch\n object.\n If the name of the sketch to be copied to is \n    __edit__, Abaqus creates an exact copy that contains both reference geometry and a non-identity transform matrix. Otherwise, the \n    Sketch\n    copy constructor strips the reference geometry from the copied sketch and sets the transform matrix to identity, creating a standalone copy.\n    ',
	),
	'Model.ConstrainedSketchFromGeometryFile':(
		'name, geometryFile',
		'This method creates a \n ConstrainedSketch\n object and places it in the \n sketches\n repository.\n ',
	),
	'Model.ContactExp':(
		'name, createStepName <, globalSmoothing, useAllstar, includedPairs, excludedPairs, contactPropertyAssignments, surfaceThicknessAssignments, surfaceOffsetAssignments, surfaceFeatureAssignments, smoothingAssignments, masterSlaveAssignments>',
		'This method creates a ContactExp object.',
	),
	'Model.ContactProperty':(
		'name',
		'This method creates a ContactProperty object.',
	),
	'Model.ContactStd':(
		'name, createStepName <, globalSmoothing, useAllstar, includedPairs, excludedPairs, contactPropertyAssignments, surfaceFeatureAssignments, surfaceThicknessAssignments, surfaceOffsetAssignments, masterSlaveAssignments, initializationAssignments, stabilizationAssignments, smoothingAssignments>',
		'This method creates a ContactStd object.',
	),
	'Model.CoriolisForce':(
		'name, createStepName, region, magnitude, point1, point2 <, amplitude, distributionType, field>',
		'This method creates a CoriolisForce object.',
	),
	'Model.CoupledTempDisplacementStep':(
		'name, previous <, description, response, timePeriod, nlgeom, stabilizationMethod, stabilizationMagnitude, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, deltmx, cetol, creepIntegration, solutionTechnique, matrixStorage, amplitude, extrapolation, _solverInput, maintainAttributes, convertSDI, adaptiveDampingRatio, continueDampingFactors>',
		'This method creates a CoupledTempDisplacementStep object.',
	),
	'Model.CoupledThermalElectricStep':(
		'name, previous <, description, response, timePeriod, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, end, deltmx, mxdem, solutionTechnique, matrixStorage, amplitude, extrapolation, _solverInput, maintainAttributes, convertSDI>',
		'This method creates a CoupledThermalElectricStep object. ',
	),
	'Model.CoupledThermalElectricalStructuralStep':(
		'name, previous <, description, response, timePeriod, nlgeom, stabilizationMethod, stabilizationMagnitude, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, deltmx, cetol, creepIntegration, matrixStorage, amplitude, extrapolation, _solverInput, maintainAttributes, convertSDI, adaptiveDampingRatio, continueDampingFactors>',
		'This method creates a CoupledThermalElectricalStructuralStep object.',
	),
	'Model.Coupling':(
		'name, surface, controlPoint, influenceRadius, couplingType <, adjust, localCsys, u1, u2, u3, ur1, ur2, ur3, weightingMethod>',
		'This method creates a Coupling object.',
	),
	'Model.CyclicSymmetry':(
		'name, createStepName, master, slave, repetitiveSectors, axisPoint1, axisPoint2 <, extractedNodalDiameter, lowestNodalDiameter, highestNodalDiameter, excitationNodalDiameter, adjustTie, positionTolerance, positionToleranceMethod>',
		'This method creates a CyclicSymmetry object.',
	),
	'Model.DecayAmplitude':(
		'name, initial, maximum, start, decayTime <, timeSpan>',
		'This method creates a DecayAmplitude object.',
	),
	'Model.DirectCyclicStep':(
		'name, previous <, description, timePeriod, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, maxNumIterations, initialTerms, maxTerms, termsIncrement, deltmx, cetol, timePoints, fatigue, continueAnalysis, minCycleInc, maxCycleInc, maxNumCycles, damageExtrapolationTolerance, matrixStorage, extrapolation, _solverInput, maintainAttributes, convertSDI>',
		'This method creates a DirectCyclicStep object.',
	),
	'Model.DiscreteField':(
		'name, defaultValues, fieldType <, location, dataWidth, data, description, orientationType, partLevelOrientation>',
		'This method creates a DiscreteField object.',
	),
	'Model.DiscreteFieldFromAnalytic':(
		'name, location, analyticFieldName, region',
		'This method creates a DiscreteField object from a AnalyticalField object.',
	),
	'Model.DisplacementAdaptiveMeshConstraint':(
		'name, createStepName, region <, u1, u2, u3, ur1, ur2, ur3, amplitude, motionType, localCsys>',
		'This method creates a DisplacementAdaptiveMeshConstraint object.',
	),
	'Model.DisplacementBC':(
		'name, createStepName, region <, fieldName, u1, u2, u3, ur1, ur2, ur3, fixed, amplitude, distributionType, localCsys, buckleCase>',
		'This method creates a DisplacementBC object.',
	),
	'Model.DisplacementBaseMotionBC':(
		'name, createStepName, dof <, amplitudeScaleFactor, centerOfRotation, correlation, secondaryBase, useComplex, amplitude>',
		'This method creates a DisplacementBaseMotionBC object.',
	),
	'Model.DisplayBody':(
		'name, instance, controlPoints',
		'This method creates a DisplayBody object.',
	),
	'Model.ElasticFoundation':(
		'name, createStepName, surface, stiffness',
		'This method creates an ElasticFoundation object.',
	),
	'Model.ElectricPotentialBC':(
		'name, createStepName, region <, fieldName, magnitude, distributionType, amplitude, fixed>',
		'This method creates an ElectricPotentialBC object.',
	),
	'Model.EmagTimeHarmonicStep':(
		'name, previous, frequencyRange <, description, factorization>',
		'This method creates a EmagTimeHarmonicStep object.',
	),
	'Model.EmbeddedRegion':(
		'name, embeddedRegion, hostRegion <, weightFactorTolerance, toleranceMethod, absoluteTolerance, fractionalTolerance>',
		'This method creates a EmbeddedRegion object.',
	),
	'Model.EncastreBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates an encastre TypeBC object.',
	),
	'Model.EquallySpacedAmplitude':(
		'name, fixedInterval, data <, begin, smooth, timeSpan>',
		'This method creates an EquallySpacedAmplitude object.',
	),
	'Model.Equation':(
		'name, terms',
		'This method creates an Equation object.',
	),
	'Model.EulerianBC':(
		'name, createStepName, region <, definition, inflowType, outflowType>',
		'This method creates a EulerianBC object.',
	),
	'Model.EulerianMotionBC':(
		'name, createStepName, instanceName <, followRegion, region, materialName, ctrPosition1, posPosition1, negPosition1, expansionRatio1, contractRatio1, ctrPosition2, posPosition2, negPosition2, expansionRatio2, contractRatio2, ctrPosition3, posPosition3, negPosition3, expansionRatio3, contractRatio3, allowContraction, aspectLimit, vmaxFactor, volThreshold, bufferSize>',
		'This method creates an EulerianMotionBC object.',
	),
	'Model.EulerianSection':(
		'name, data',
		'This method creates a EulerianSection object.',
	),
	'Model.ExpContactControl':(
		'name <, globTrkChoice, globTrkInc, fastLocalTrk, scalePenalty, warpCheckPeriod, warpCutoff>',
		'This method creates an ExpContactControl object.',
	),
	'Model.ExplicitDynamicsStep':(
		'name, previous <, description, timePeriod, nlgeom, adiabatic, timeIncrementationMethod, maxIncrement, scaleFactor, massScaling, linearBulkViscosity, quadBulkViscosity, userDefinedInc, _solverInput, maintainAttributes>',
		'This method creates an ExplicitDynamicsStep object.',
	),
	'Model.ExpressionField':(
		'name, expression <, localCsys, description>',
		'This method creates an ExpressionField object.',
	),
	'Model.FieldOutputRequest':(
		'name, createStepName <, region, variables, frequency, modes, timeInterval, numIntervals, timeMarks, boltLoad, sectionPoints, interactions, rebar, filter, directions, fasteners, assembledFastener, assembledFastenerSet, exteriorOnly, layupNames, layupLocationMethod, outputAtPlyTop, outputAtPlyMid, outputAtPlyBottom>',
		'This method creates a FieldOutputRequest object.',
	),
	'Model.FilmCondition':(
		'name, createStepName, surface, definition <, interactionProperty, sinkTemperature, sinkAmplitude, filmCoeff, filmCoeffAmplitude, field, sinkFieldName, sinkDistributionType>',
		'This method creates a FilmCondition object.',
	),
	'Model.FilmConditionProp':(
		'name <, temperatureDependency, dependencies, property>',
		'This method creates a FilmConditionProp object.',
	),
	'Model.FlowStep':(
		'name, previous <, description, timePeriod, energyEquation, incrementation, initialInc, divergenceTol, maximumCFL, incAdjustmentFreq, stepGrowthFactor, viscousFactor, boundaryFactor, advectionFactor, momOutputDiagnostics, momOutputConvergence, momIterationLimit, momCheckingFreq, momConvergenceLimit, pressureType, pressSolverType, pressSmootherType, pressPreSweeps, pressPostSweeps, pressOutputDiagnostics, pressOutputConvergence, pressIterationLimit, pressCheckingFreq, pressConvergenceLimit, transOutputDiagnostics, transOutputConvergence, transIterationLimit, transCheckingFreq, transConvergenceLimit, turbulenceModel, turbPrandtlNumber, turbCb1, turbCb2, turbCv1, turbCv2, turbCw1, turbCw2, turbCw3, turbSigma, turbKappa, turbCmu, turbCeps1, turbCeps2t, turbSigma_k, turbSigma_eps, turbBeta, turbLambda0>',
		'This method creates a FlowStep object.',
	),
	'Model.FluidCavity':(
		'name, createStepName, cavityPoint, cavitySurface, interactionProperty <, ambientPressure, thickness, useAdiabatic, checkNormals>',
		'This method creates an FluidCavity object.',
	),
	'Model.FluidCavityPressure':(
		'name, fluidCavity, fluidPressure',
		'This method creates a FluidCavityPressure object.',
	),
	'Model.FluidCavityPressureBC':(
		'name, createStepName, fluidCavity <, magnitude, amplitude, fixed>',
		'This method creates a FluidCavityPressureBC object.',
	),
	'Model.FluidCavityProperty':(
		'name <, definition, fluidDensity, molecularWeight, useExpansion, expansionTempDep, expansionDependencies, referenceTemperature, expansionTable, useBulkModulus, bulkModulusTempDep, bulkModulusDependencies, bulkModulusTable, useCapacity, capacityType, capacityTempDep, capacityDependencies, capacityTable>',
		'This method creates a FluidCavityProperty object.',
	),
	'Model.FluidDensity':(
		'name, createStepName, region <, density>',
		'This method creates a FluidDensity object.',
	),
	'Model.FluidExchange':(
		'name, createStepName, firstCavity, interactionProperty <, definition, secondCavity, exchangeArea>',
		'This method creates an FluidExchange object.',
	),
	'Model.FluidExchangeProperty':(
		'name, dataTable <, definition, pressureDependency, temperatureDependency, fieldDependencies>',
		'This method creates a FluidExchangeProperty object.',
	),
	'Model.FluidInletOutletBC':(
		'name, createStepName, region <, fieldName, distributionType, localCsys, momentumType, pressure, v1, v2, v3, momentumAmplitude, temperature, temperatureAmplitude, kineticEnergy, kineticEnergyAmplitude, dissipationRate, dissipationRateAmplitude, eddyViscosity, eddyViscosityAmplitude>',
		'This method creates a FluidInletOutletBC object.',
	),
	'Model.FluidThermalEnergy':(
		'name, createStepName, region <, temperature, distributionType>',
		'This method creates a FluidThermalEnergy object.',
	),
	'Model.FluidTurbulence':(
		'name, createStepName, region <, eddyViscosity, dissipationRate, kineticEnergy>',
		'This method creates a\n FluidTurbulence\n object.\n ',
	),
	'Model.FluidVelocity':(
		'name, createStepName, region <, velocity1, velocity2, velocity3>',
		'This method creates a FluidVelocity object.',
	),
	'Model.FluidWallConditionBC':(
		'name, createStepName, region <, fieldName, distributionType, localCsys, type, v1, v2, v3, velocityAmplitude, thermalEnergyType, temperature, heatFlux, thermalEnergyAmplitude, kineticEnergy, kineticEnergyAmplitude, dissipationRate, dissipationRateAmplitude, eddyViscosity, eddyViscosityAmplitude>',
		'This method creates a FluidWallConditionBC object.',
	),
	'Model.FrequencyStep':(
		'name, previous, eigensolver <, numEigen, description, shift, minEigen, maxEigen, vectors, maxIterations, blockSize, maxBlocks, _solverInput, normalization, propertyEvaluationFrequency, projectDamping, acousticCoupling, acousticRangeFactor, frictionDamping, matrixStorage, maintainAttributes, simLinearDynamics, residualModes, substructureCutoffMultiplier, firstCutoffMultiplier, secondCutoffMultiplier, residualModeRegion, residualModeDof, limitSavedEigenvectorRegion>',
		'This method creates a FrequencyStep object. ',
	),
	'Model.GasketSection':(
		'name, material <, crossSection, initialGap, initialThickness, initialVoid, stabilizationStiffness>',
		'This method creates a GasketSection object.',
	),
	'Model.GeneralField':(
		'name, createStepName, region <, distributionType, crossSectionDistribution, specifyVariableID, variableID, numberOfVariables, amplitude, fileName, beginStep, beginIncrement, endStep, endIncrement, midSide, magnitudes>',
		'This method creates a GeneralField object.',
	),
	'Model.GeneralStiffnessSection':(
		'name, stiffnessMatrix <, referenceTemperature, applyThermalStress, temperatureDependency, dependencies, poissonDefinition, poisson, useDensity, density, thermalStresses, scalingData>',
		'This method creates a GeneralStiffnessSection object.',
	),
	'Model.GeneralizedProfile':(
		'name, area, i11, i12, i22, j, gammaO, gammaW',
		'This method creates a GeneralizedProfile object.',
	),
	'Model.GeostaticStep':(
		'name, previous <, description, nlgeom, matrixSolver, matrixStorage, _solverInput, maintainAttributes, solutionTechnique, reformKernel, convertSDI, utol, timePeriod, timeIncrementationMethod, initialInc, minInc, maxInc>',
		'This method creates a GeostaticStep object.',
	),
	'Model.Gravity':(
		'name, createStepName <, distributionType, field, region, comp1, comp2, comp3, amplitude>',
		'This method creates a Gravity object.',
	),
	'Model.HeatTransferStep':(
		'name, previous <, description, response, timePeriod, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, end, deltmx, mxdem, amplitude, extrapolation, matrixSolver, matrixStorage, _solverInput, maintainAttributes, solutionTechnique, reformKernel, convertSDI>',
		'This method creates a HeatTransferStep object. ',
	),
	'Model.HexagonalProfile':(
		'name, r, t',
		'This method creates a HexagonalProfile object.',
	),
	'Model.HistoryOutputRequest':(
		'name, createStepName <, region, variables, frequency, modes, timeInterval, numIntervals, boltLoad, sectionPoints, stepName, interactions, contourIntegral, numberOfContours, stressInitializationStep, contourType, kFactorDirection, rebar, integratedOutputSection, springs, filter, fasteners, assembledFastener, assembledFastenerSet, sensor, useGlobal, layupNames, layupLocationMethod, outputAtPlyTop, outputAtPlyMid, outputAtPlyBottom>',
		'This method creates a HistoryOutputRequest object.',
	),
	'Model.HomogeneousShellSection':'<value is a self-reference, replaced by this string>',
	'Model.HomogeneousSolidSection':(
		'name, material <, thickness>',
		'This method creates a HomogeneousSolidSection object.',
	),
	'Model.HydrostaticFluidFlow':(
		'name, createStepName, region, magnitude <, amplitude>',
		'This method creates a HydrostaticFluidFlow object.',
	),
	'Model.IProfile':(
		'name, l, h, b1, b2, t1, t2, t3',
		'This method creates an IProfile object.',
	),
	'Model.ImplicitDynamicsStep':(
		'name, previous <, description, timePeriod, nlgeom, matrixStorage, application, adiabatic, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, hafTolMethod, haftol, halfIncScaleFactor, nohaf, amplitude, alpha, initialConditions, extrapolation, noStop, _solverInput, maintainAttributes, solutionTechnique, reformKernel, convertSDI>',
		'This method creates an ImplicitDynamicsStep object.',
	),
	'Model.IncidentWave':(
		'name, createStepName, sourcePoint, standoffPoint, surface, interactionProperty <, definition, amplitude, imaginaryAmplitude, surfaceNormal, initialDepth, referenceMagnitude, detonationTime, magnitudeFactor>',
		'This method creates an IncidentWave object.',
	),
	'Model.IncidentWaveProperty':(
		'name <, definition, propagationModel, soundSpeed, fluidDensity, specificHeatRatio, gravity, atmosphericPressure, dragCoefficient, dragExponent, waveEffects, chargeDensity, chargeMass, constantK1, constantK2, constantA, constantB, constantKc, duration, maximumSteps, relativeStepControl, absoluteStepControl, stepControlExponent, genDecayA, genDecayB, genDecayC, seedNumber, massTNT, massFactor, lengthFactor, timeFactor, pressureFactor>',
		'This method creates an IncidentWaveProperty object.',
	),
	'Model.InertiaRelief':(
		'name, createStepName <, u1, u2, u3, ur1, ur2, ur3, referencePoint, localCoordinates>',
		'This method creates an InertiaRelief object.',
	),
	'Model.InitialState':(
		'name, instances, fileName <, endStep, endIncrement, updateReferenceConfiguration>',
		'This method creates an InitialState predefined field object.',
	),
	'Model.Instance':(
		'name, objectToCopy',
		'This method copies a \n PartInstance \n object from the specified model and creates a new \n PartInstance \n object.\n ',
	),
	'Model.IntegratedOutputSection':(
		'name <, surface, refPoint, refPointAtCenter, refPointMotion, localCsys, projectOrientation>',
		'This method creates an IntegratedOutputSection object.',
	),
	'Model.InwardVolAccel':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a InwardVolAccel object.',
	),
	'Model.KinematicHardening':(
		'name, region <, numBackStress, equivPlasticStrain, backStress, sectPtNum, definition, rebarLayerNames, distributionType>',
		' This method creates a KinematicHardening object.  ',
	),
	'Model.LProfile':(
		'name, a, b, t1, t2',
		'This method creates a LProfile object.',
	),
	'Model.LineLoad':(
		'name, createStepName, region <, distributionType, field, comp1, comp2, comp3, amplitude, system>',
		'This method creates a LineLoad object.',
	),
	'Model.MPCSection':(
		'name, mpcType <, userMode, userType>',
		'This method creates a MPCSection object.',
	),
	'Model.MagneticVectorPotentialBC':(
		'name, createStepName, region <, component1, component2, component3, amplitude, distributionType, localCsys>',
		'This method creates a MagneticVectorPotentialBC object.',
	),
	'Model.MappedField':(
		'name <, regionType, partLevelData, pointDataFormat, gridPointPlane, defaultUnmappedValue, mappingAlgorithm, searchTolType, boundarySearchTol, neighborhoodSearchTol, negativeNormalSearchTol, positiveNormalSearchTol, scaleCoordinates, gridPointData, xyzPointData, coordinateScalingFactors, localCsys, description>',
		'This method creates an MappedField object.',
	),
	'Model.MassDiffusionStep':(
		'name, previous <, description, response, timePeriod, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, end, dcmax, amplitude, extrapolation, _solverInput, maintainAttributes, convertSDI>',
		'This method creates a MassDiffusionStep object. ',
	),
	'Model.MassFlowRate':(
		'name, createStepName, region <, v1, v2, v3, amplitude>',
		'This method creates a MassFlowRate object.',
	),
	'Model.Material':(
		'name <, description, materialIdentifier>',
		'This method creates a Material object.',
	),
	'Model.MaterialAssignment':(
		'name, instanceList <, useFields, assignmentList, fieldList, colorList>',
		'This method creates a MaterialAssignment predefined field object.',
	),
	'Model.MaterialFlowBC':(
		'name, createStepName, region <, fieldName, magnitude, distributionType, amplitude, fixed>',
		'This method creates a MaterialFlowBC object.',
	),
	'Model.MembraneSection':(
		'name, material <, thickness, thicknessType, poissonDefinition, poisson, thicknessField>',
		'This method creates a MembraneSection object.',
	),
	'Model.ModalDynamicsStep':(
		'name, previous <, description, continueAnalysis, timePeriod, incSize, directDamping, compositeDamping, rayleighDamping, amplitude, _solverInput, maintainAttributes, directDampingByFrequency, rayleighDampingByFrequency>',
		'This method creates a ModalDynamicsStep object. ',
	),
	'Model.ModelChange':(
		'name, createStepName <, isRestart, regionType, region, activeInStep, includeStrain>',
		'This method creates a ModelChange object.',
	),
	'Model.ModulatedAmplitude':(
		'name, initial, magnitude, start, frequency1, frequency2 <, timeSpan>',
		'This method creates a ModulatedAmplitude object.',
	),
	'Model.Moment':(
		'name, createStepName, region <, cm1, cm2, cm3, amplitude, follower, localCsys, distributionType, field>',
		'This method creates a Moment object.',
	),
	'Model.MultipointConstraint':(
		'name, surface, controlPoint, mpcType <, csys, userType, userMode>',
		'This method creates a MultipointConstraint object.',
	),
	'Model.OperatorFilter':(
		'name, cutoffFrequency <, order, operation, halt, limit, invariant>',
		'This method creates an OperatorFilter object.',
	),
	'Model.PEGLoad':(
		'name, createStepName, region <, distributionType, field, comp1, comp2, comp3, amplitude>',
		'This method creates a PEGLoad object.',
	),
	'Model.PEGSection':(
		'name, material <, thickness, wedgeAngle1, wedgeAngle2>',
		'This method creates a PEGSection object.',
	),
	'Model.Part':(
		'name, objectToCopy <, scale, mirrorPlane, compressFeatureList, separate>',
		'This method copies a Part object and places the copy in the parts repository.',
	),
	'Model.Part2DGeomFrom2DMesh':(
		'name, part, featureAngle <, splineCurvatureLimit, twist>',
		'This method creates a geometric Part object from the outline of an existing two-dimensional orphan mesh Part object and places it in the parts repository. If the Part2DGeomFrom2DMesh method cannot create a valid two-dimensional shell section from the two-dimensional mesh, the method fails and creates an empty geometry part with a failed base shell feature.',
	),
	'Model.PartFromExtrude2DMesh':(
		'name, part, depth, elementSize',
		'This method creates a Part object by extruding an existing two-dimensional orphan mesh Part object in the positive Z-direction and places it in the parts repository.',
	),
	'Model.PartFromGeometryFile':(
		'name, geometryFile, dimensionality, type <, bodyNum, combine, retainBoundary, stitchTolerance, twist, scale, convertToAnalytical, convertToPrecise>',
		'This method creates a Part object and places it in the parts repository.',
	),
	'Model.PartFromMeshMirror':(
		'name, part, point1, point2',
		'This method creates a Part object by mirroring an existing orphan mesh Part object about a specified plane and places it in the parts repository. The result is a union of the original and the mirrored copy. Contrast the PartFromMeshMirror method with the mirrorPlane argument of the Part copy constructor. The mirrorPlane argument creates only the second half of the part but does not unite the two halves.',
	),
	'Model.PartFromNodesAndElements':(
		'name, dimensionality, type, nodes, elements <, twist>',
		'This method creates a Part object from nodes and elements and places it in the parts repository.',
	),
	'Model.PartFromOdb':(
		'name, odb <, fileName, instance, elementSet, shape, step, frame, twist>',
		'This method creates an orphan mesh Part object by reading an output database. The new part is placed in the parts repository.',
	),
	'Model.PartFromSection3DMeshByPlane':(
		'name, part, point1, point2, point3',
		'This method creates a Part object by cutting an existing three-dimensional orphan mesh Part object by a plane and places it in the parts repository. This method is valid only for orphan mesh parts composed of 8-node brick elements. ',
	),
	'Model.PartFromSubstructure':(
		'name, substructureFile, odbFile',
		'This method creates a substructure Part object by reading a substructure sim file and places it in the   parts  repository.  ',
	),
	'Model.PeriodicAmplitude':(
		'name, frequency, start, a_0, data <, timeSpan>',
		'This method creates a PeriodicAmplitude object.',
	),
	'Model.PinnedBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a pinned TypeBC object.',
	),
	'Model.PipePressure':(
		'name, createStepName, region, magnitude, diameter, hZero, hReference <, field, amplitude, distributionType, side>',
		'This method creates a Pressure object.',
	),
	'Model.PipeProfile':(
		'name, r, t <, formulation>',
		'This method creates a PipeProfile object.',
	),
	'Model.PorDragBodyForce':(
		'name, createStepName, region, fieldName, distributionType, magnitude',
		'This method creates a PorDragBodyForce object.',
	),
	'Model.PorePressure':(
		'name, region <, distribution, magnitude1, verticalCoord1, magnitude2, verticalCoord2>',
		'This method creates a PorePressure object.',
	),
	'Model.PorePressureBC':(
		'name, createStepName, region <, fieldName, magnitude, distributionType, amplitude, fixed>',
		'This method creates a PorePressureBC object.',
	),
	'Model.Pressure':(
		'name, createStepName, region, magnitude, hZero, hReference <, field, refPoint, distributionType, amplitude>',
		'This method creates a Pressure object.',
	),
	'Model.PressurePenetration':(
		'name, createStepName, contactInteraction, masterPoints, slavePoints, penetrationPressure, criticalPressure <, amplitude, penetrationTime>',
		'This method creates a PressurePenetration object.',
	),
	'Model.PressureStress':(
		'name, createStepName, region <, distribution, magnitude, fileName, beginStep, beginIncrement, endStep, endIncrement, amplitude>',
		'This method creates a PressureStress object.',
	),
	'Model.PsdDefinition':(
		'name, data <, unitType, referenceGravityAcceleration, referenecePower, user, timeSpan, amplitude>',
		'This method creates a \n PsdDefinition\n object.\n ',
	),
	'Model.RadiationToAmbient':(
		'name, createStepName, surface, emissivity <, field, distributionType, radiationType, ambientTemperature, ambientTemperatureAmp>',
		'This method creates a RadiationToAmbient object.',
	),
	'Model.RandomResponseStep':(
		'name, previous, freq <, description, scale, directDamping, compositeDamping, rayleighDamping, structuralDamping, directDampingByFrequency, rayleighDampingByFrequency, structuralDampingByFrequency, _solverInput, maintainAttributes>',
		'This method creates a RandomResponseStep object.',
	),
	'Model.RectangularProfile':(
		'name, a, b',
		'This method creates a RectangularProfile object.',
	),
	'Model.ReferencePressure':(
		'name, createStepName, region, magnitude',
		'This method creates a ReferencePressure object.',
	),
	'Model.RelativeDensity':(
		'name, region, magnitude',
		'This method creates a RelativeDensity object.',
	),
	'Model.RemeshingRule':(
		'name, stepName, variables <, description, region, sizingMethod, errorTarget, maxSolutionErrorTarget, minSolutionErrorTarget, meshBias, minElementSize, maxElementSize, outputFrequency, specifyMinSize, specifyMaxSize, coarseningFactor, refinementFactor, elementCountLimit>',
		'This method creates a RemeshingRule object.',
	),
	'Model.ResponseSpectrumStep':(
		'name, previous, components <, description, comp, sum, directDamping, compositeDamping, rayleighDamping, directDampingByFrequency, rayleighDampingByFrequency, _solverInput, maintainAttributes>',
		'This method creates a ResponseSpectrumStep object. ',
	),
	'Model.RetainedNodalDofsBC':(
		'name, createStepName, region <, u1, u2, u3, ur1, ur2, ur3>',
		'This method creates a RetainedNodalDofsBC object.',
	),
	'Model.RigidBody':(
		'name, refPointRegion <, bodyRegion, tieRegion, pinRegion, surfaceRegion, refPointAtCOM, isothermal>',
		'This method creates a RigidBody object.',
	),
	'Model.RotationalBodyForce':(
		'name, createStepName, region, magnitude, point1, point2 <, distributionType, field, centrifugal, rotaryAcceleration, amplitude>',
		'This method creates a RotationalBodyForce object.',
	),
	'Model.SDV':(
		'name, region <, distribution, magnitudes>',
		'This method creates a SDV object.',
	),
	'Model.Saturation':(
		'name, region, magnitude',
		'This method creates a Saturation object.',
	),
	'Model.SecondaryBaseBC':(
		'name, createStepName, regions, dofs',
		'This method creates a SecondaryBaseBC object.',
	),
	'Model.SelfContactExp':(
		'name, createStepName, surface, interactionProperty <, mechanicalConstraint, contactControls>',
		'This method creates a SelfContactExp object.',
	),
	'Model.SelfContactStd':(
		'name, createStepName, surface, interactionProperty <, enforcement, thickness, smooth, contactControls>',
		'This method creates a SelfContactStd object.',
	),
	'Model.ShapeTask':(
		'name <, absoluteStepSizeControl, constrainedLaplacianConvergenceLevel, curvatureSmoothingEdgeLength, equalityConstraintTolerance, featureRecognitionAngle, filterExponent, filterMaxRadius, filterRadiusReduction, firstCycleDeletedVolumeTechnique, freezeBoundaryConditionRegions, frozenBoundaryConditionRegion, geometricRestrictionEvaluationFrequency, growthScaleFactor, haltUponViolation, layerReferenceRegion, meshSmoothingRegionMethod, meshSmoothingStrategy, midsideInterpolation, numFreeNodeLayers, numSmoothedElementLayers, presumeFeasibleBCRegionAtStart, quadMaxAngle, quadMinAngle, quadSkew, quadTaper, region, reportPoorQualityElements, reportQualityViolation, shrinkScaleFactor, smoothingRegion, targetMeshQuality, tetAspectRatio, tetMaxAspect, tetMinAspect, tetSkew, triMaxAngle, triMinAngle, updateShapeBasisVectors>',
		'This method creates a ShapeTask object.',
	),
	'Model.ShellEdgeLoad':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude, angle, axis, localCsys, userCsys, directionVector, follower, resultant, traction>',
		'This method creates a ShellEdgeLoad object.',
	),
	'Model.ShellSolidCoupling':(
		'name, shellEdge, solidFace <, positionToleranceMethod, positionTolerance, influenceDistanceMethod, influenceDistance>',
		'This method creates a ShellSolidCoupling object.',
	),
	'Model.SmoothStepAmplitude':(
		'name, data <, timeSpan>',
		'This method creates a SmoothStepAmplitude object.',
	),
	'Model.SoilsStep':(
		'name, previous <, description, response, timePeriod, nlgeom, stabilizationMethod, stabilizationMagnitude, creep, timeIncrementationMethod, initialInc, minInc, maxInc, maxNumInc, end, utol, cetol, amplitude, extrapolation, matrixSolver, matrixStorage, _solverInput, maintainAttributes, solutionTechnique, reformKernel, convertSDI, adaptiveDampingRatio, continueDampingFactors>',
		'This method creates a SoilsStep object.',
	),
	'Model.SolutionDependentAmplitude':(
		'name <, initial, minimum, maximum, timeSpan>',
		'This method creates a SolutionDependentAmplitude object.',
	),
	'Model.SpectrumAmplitude':(
		'name, method, data <, specificationUnits, eventUnits, solution, timeIncrement, gravity, criticalDamping, timeSpan, amplitude>',
		'This method creates a \n SpectrumAmplitude\n object.\n ',
	),
	'Model.SpudPreload':(
		'name, region, magnitude',
		'This method creates a SpudPreload object.',
	),
	'Model.StaticLinearPerturbationStep':(
		'name, previous <, description, matrixSolver, matrixStorage, _solverInput, maintainAttributes>',
		'This method creates a StaticLinearPerturbationStep object. ',
	),
	'Model.StaticRiksStep':(
		'name, previous <, description, nlgeom, adiabatic, maxLPF, nodeOn, maximumDisplacement, dof, region, timeIncrementationMethod, maxNumInc, totalArcLength, initialArcInc, minArcInc, maxArcInc, matrixStorage, extrapolation, fullyPlastic, noStop, _solverInput, maintainAttributes, useLongTermSolution, convertSDI>',
		'This method creates a StaticRiksStep object.',
	),
	'Model.StaticStep':(
		'name, previous <, description, timePeriod, nlgeom, stabilizationMethod, stabilizationMagnitude, adiabatic, timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, matrixSolver, matrixStorage, amplitude, extrapolation, fullyPlastic, noStop, _solverInput, maintainAttributes, useLongTermSolution, solutionTechnique, reformKernel, convertSDI, adaptiveDampingRatio, continueDampingFactors>',
		'This method creates a StaticStep object.',
	),
	'Model.StdContactControl':(
		'name <, stiffnessScaleFactor, penetrationTolChoice, relativePenetrationTolerance, absolutePenetrationTolerance, frictionOnset, automaticTolerances, maxchp, perrmx, uerrmx, stabilizeChoice, dampFactor, dampCoef, tangFraction, eosFraction, zeroDampingChoice, zeroDamping, enforceWithLagrangeMultipliers>',
		'This method creates an StdContactControl object.',
	),
	'Model.StdInitialization':(
		'name <, overclosureType, interferenceDistance, clearanceDistance, openingTolerance, overclosureTolerance>',
		'This method creates a StdInitialization object.',
	),
	'Model.StdStabilization':(
		'name <, zeroDistance, reductionFactor, scaleFactor, tangentialFactor, amplitude, reset>',
		'This method creates a StdStabilization object.',
	),
	'Model.StdXplCosimulation':(
		'name, createStepName, region <, incrementation, stepSize, stepSizeDefinition>',
		'This method creates a StdXplCosimulation object.',
	),
	'Model.SteadyStateDirectStep':(
		'name, previous, frequencyRange <, description, factorization, scale, matrixStorage, _solverInput, maintainAttributes, subdivideUsingEigenfrequencies, frictionDamping>',
		'This method creates a SteadyStateDirectStep object.',
	),
	'Model.SteadyStateModalStep':(
		'name, previous, frequencyRange <, description, scale, directDamping, compositeDamping, rayleighDamping, structuralDamping, directDampingByFrequency, rayleighDampingByFrequency, structuralDampingByFrequency, _solverInput, maintainAttributes, subdivideUsingEigenfrequencies>',
		'This method creates a SteadyStateModalStep object. ',
	),
	'Model.SteadyStateSubspaceStep':(
		'name, previous, frequencyRange <, description, factorization, scale, matrixStorage, _solverInput, maintainAttributes, subdivideUsingEigenfrequencies, projection, maxDampingChange, maxStiffnessChange, frictionDamping>',
		'This method creates a SteadyStateSubspaceStep object.',
	),
	'Model.Stress':(
		'name, region <, distribution, sectionType, stressTensor, magnitude1, verticalCoord1, magnitude2, verticalCoord2, lateralCoeff1, lateralCoeff2>',
		'This method creates a Stress object.',
	),
	'Model.SubmodelBC':(
		'name, createStepName, region, dof, globalStep, timeScale, shellThickness <, globalDrivingRegion, absoluteExteriorTolerance, exteriorTolerance, localCsys, globalIncrement, centerZoneSize>',
		'This method creates a SubmodelBC object.',
	),
	'Model.SubmodelSB':(
		'name, createStepName, region, globalStep <, globalDrivingRegion, absoluteExteriorTolerance, exteriorTolerance, globalIncrement>',
		'This method creates a SubmodelSB object.',
	),
	'Model.SubspaceDynamicsStep':(
		'name, previous <, description, timePeriod, vectors, nlgeom, maxNumInc, incSize, amplitude, _solverInput, maintainAttributes>',
		'This method creates a SubspaceDynamicsStep object.',
	),
	'Model.SubstructureGenerateStep':(
		'name, previous, substructureIdentifier <, description, recoveryMatrix, recoveryRegion, computeGravityLoadVectors, computeReducedMassMatrix, computeReducedStructuralDampingMatrix, computeReducedViscousDampingMatrix, evaluateFrequencyDependentProperties, frequency, retainedEigenmodesMethod, modeRange, frequencyRange, globalDampingField, alphaDampingRatio, betaDampingRatio, structuralDampingRatio, viscousDampingControl, structuralDampingControl>',
		'This method creates a SubstructureGenerateStep object.',
	),
	'Model.SubstructureLoad':(
		'name, createStepName, region, loadCaseNames, magnitude <, amplitude>',
		'This method creates a SubstructureLoad object.',
	),
	'Model.SurfaceCharge':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a SurfaceCharge object.',
	),
	'Model.SurfaceConcentrationFlux':(
		'name, createStepName, region, magnitude <, field, distributionType, amplitude>',
		'This method creates a SurfaceConcentrationFlux object.',
	),
	'Model.SurfaceCurrent':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude>',
		'This method creates a SurfaceCurrent object.',
	),
	'Model.SurfaceCurrentDensity':(
		'name, createStepName, region, comp1, comp2, comp3 <, distributionType, amplitude>',
		'This method creates a SurfaceCurrentDensity object.',
	),
	'Model.SurfaceHeatFlux':(
		'name, createStepName, region, magnitude <, field, distributionType, amplitude>',
		'This method creates a SurfaceHeatFlux object.',
	),
	'Model.SurfacePoreFluid':(
		'name, createStepName, region, magnitude <, field, distributionType, amplitude>',
		'This method creates a SurfacePoreFluid object.',
	),
	'Model.SurfaceSection':(
		'name <, useDensity, density>',
		'This method creates a SurfaceSection object.',
	),
	'Model.SurfaceToSurfaceContactExp':(
		'name, createStepName, master, slave, sliding, masterNoThick, slaveNoThick, interactionProperty <, mechanicalConstraint, weightingFactorType, weightingFactor, contactControls, initialClearance, halfThreadAngle, pitch, majorBoltDiameter, meanBoltDiameter, datumAxis, useReverseDatumAxis, clearanceRegion>',
		'This method creates a SurfaceToSurfaceContactExp object.',
	),
	'Model.SurfaceToSurfaceContactStd':(
		'name, createStepName, master, slave, sliding, interactionProperty <, interferenceType, overclosure, interferenceDirectionType, direction, amplitude, smooth, hcrit, extensionZone, adjustMethod, adjustTolerance, adjustSet, enforcement, thickness, contactControls, tied, initialClearance, halfThreadAngle, pitch, majorBoltDiameter, meanBoltDiameter, datumAxis, useReverseDatumAxis, clearanceRegion, surfaceSmoothing, bondingSet>',
		'This method creates a SurfaceToSurfaceContactStd object.',
	),
	'Model.SurfaceTraction':(
		'name, createStepName, region, magnitude <, distributionType, field, amplitude, angle, axis, localCsys, userCsys, directionVector, follower, resultant, traction>',
		'This method creates a SurfaceTraction object.',
	),
	'Model.TProfile':(
		'name, b, h, l, tf, tw',
		'This method creates a TProfile object.',
	),
	'Model.TabularAmplitude':(
		'name, data <, smooth, timeSpan>',
		'This method creates a TabularAmplitude object.',
	),
	'Model.TempDisplacementDynamicsStep':(
		'name, previous <, description, timePeriod, nlgeom, timeIncrementationMethod, maxIncrement, scaleFactor, userDefinedInc, massScaling, linearBulkViscosity, quadBulkViscosity, _solverInput, maintainAttributes>',
		'This method creates a TempDisplacementDynamicsStep object. ',
	),
	'Model.Temperature':(
		'name, createStepName, region <, distributionType, crossSectionDistribution, field, amplitude, fileName, beginStep, beginIncrement, endStep, endIncrement, interpolate, magnitudes, absoluteExteriorTolerance, exteriorTolerance>',
		'This method creates a Temperature object.',
	),
	'Model.TemperatureBC':(
		'name, createStepName, region <, fieldName, magnitude, dof, amplitude, distributionType, fixed>',
		'This method creates a TemperatureBC object.',
	),
	'Model.Tie':(
		'name, master, slave <, adjust, positionToleranceMethod, positionTolerance, tieRotations, constraintRatioMethod, constraintRatio, constraintEnforcement, thickness>',
		'This method creates a Tie object.',
	),
	'Model.TimePoint':(
		'name, points',
		'This method creates a TimePoint object.',
	),
	'Model.TopologyTask':(
		'name <, algorithm, densityMoveLimit, densityUpdateStrategy, elementDensityDeltaStopCriteria, filterRadius, firstCycleDeletedVolume, firstCycleDeletedVolumeTechnique, freezeBoundaryConditionRegions, freezeLoadRegions, frequencySpectrumWeight, initialDensity, materialInterpolationPenalty, materialInterpolationTechnique, maxDensity, minDensity, modeTrackingRegion, numDesignCycles, numFulfilledStopCriteria, numTrackedModes, objectiveFunctionDeltaStopCriteria, region, softDeletionMethod, softDeletionRadius, softDeletionRegion, softDeletionThreshold, stepSize, stiffnessMassDamping, stopCriteriaDesignCycle, structuralMassDamping, viscousMassDamping, viscousStiffnessDamping>',
		'This method creates a TopologyTask object.',
	),
	'Model.TrapezoidalProfile':(
		'name, a, b, c, d',
		'This method creates a TrapezoidalProfile object.',
	),
	'Model.TrussSection':(
		'name, material <, area>',
		'This method creates a TrussSection object.',
	),
	'Model.UserAmplitude':(
		'name, numVariables <, timeSpan>',
		'This method creates a UserAmplitude object.',
	),
	'Model.Velocity':(
		'name, region, velocity1, velocity2, velocity3, omega, axisBegin, axisEnd <, field, distributionType>',
		'This method creates a Velocity predefined field object.',
	),
	'Model.VelocityAdaptiveMeshConstraint':(
		'name, createStepName, region <, v1, v2, v3, vr1, vr2, vr3, amplitude, localCsys, motionType>',
		'This method creates a VelocityAdaptiveMeshConstraint object.',
	),
	'Model.VelocityBC':(
		'name, createStepName, region <, fieldName, v1, v2, v3, vr1, vr2, vr3, amplitude, localCsys, distributionType>',
		'This method creates a VelocityBC object.',
	),
	'Model.VelocityBaseMotionBC':(
		'name, createStepName, dof <, amplitudeScaleFactor, centerOfRotation, correlation, secondaryBase, useComplex, amplitude>',
		'This method creates a VelocityBaseMotionBC object.',
	),
	'Model.ViscoStep':(
		'name, previous <, description, timePeriod, nlgeom, stabilizationMethod, stabilizationMagnitude, timeIncrementationMethod, matrixSolver, matrixStorage, initialInc, maxNumInc, minInc, maxInc, integration, cetol, amplitude, extrapolation, _solverInput, maintainAttributes, solutionTechnique, reformKernel, convertSDI, adaptiveDampingRatio, continueDampingFactors>',
		'This method creates a ViscoStep object.',
	),
	'Model.VoidsRatio':(
		'name, region <, distribution, magnitude, verticalCoord1, magnitude2, verticalCoord2>',
		'This method creates a VoidsRatio object.',
	),
	'Model.XFEMCrackGrowth':(
		'name, createStepName, crackName <, allowGrowth>',
		'This method creates an XFEMCrackGrowth object.',
	),
	'Model.XasymmBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a TypeBC object that specifies antisymmetry about the X-axis.',
	),
	'Model.XsymmBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a TypeBC object that specifies symmetry about the X-axis.',
	),
	'Model.YasymmBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a TypeBC object that specifies antisymmetry about the Y-axis.',
	),
	'Model.YsymmBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a TypeBC object that specifies symmetry about the Y-axis.',
	),
	'Model.ZasymmBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a TypeBC object that specifies antisymmetry about the Z-axis.',
	),
	'Model.ZsymmBC':(
		'name, createStepName, region <, buckleCase, localCsys>',
		'This method creates a TypeBC object that specifies symmetry about the Z-axis.',
	),
	'Model.adaptiveRemesh':(
		'odb',
		'This method remeshes the model using the active remesh rules in the model and the error indicator results from a previous analysis.',
	),
	'Model.beamProfilesFromOdb':(
		'fileName',
		'This method creates Profile objects by reading an output database. The new profiles are placed in the profiles repository.',
	),
	'Model.contactDetection':(
		'<name, createStepName, searchDomain, defaultType, interactionProperty, separationTolerance, extendByAngle, mergeWithinAngle, searchSingleInstances, nameEachSurfaceFound, createUnionOfMasterSurfaces, createUnionOfSlaveSurfaces, createUnionOfMasterSlaveSurfaces, includePlanar, includeCylindricalSphericalToric, includeSplineBased, includeMeshSolid, includeMeshShell, includeMeshMembrane, includeOverclosed, includeNonOverlapping, meshedGeometrySearchTechnique, useShellThickness, surfaceSmoothing>',
		'This method uses contact detection to create \n SurfaceToSurfaceContactStd, \n SurfaceToSurfaceContactExp, and \n Tie\n objects.\n ',
	),
	'Model.convertAllSketches':(
		'<regenerate, convertReversedSketches>',
		'This method converts all sketches from Abaqus 6.5 or earlier to the equivalent \n ConstrainedSketch \n objects.\n ',
	),
	'Model.getVertices':(
		'',
		"This method returns a sequence consisting of tuples of coordinates of the connector's endpoints.",
	),
	'Model.linkInstances':(
		'instancesMap',
		'This method links the selected \n PartInstance \n objects to the corresponding \n PartInstance \n objects from the specified models.  If all instances of a Part are selected for linking, the Part will be linked as well.  If not, a new linked child Part object will be created and added to the repository.\n ',
	),
	'Model.materialsFromOdb':(
		'fileName',
		'This methods creates Material objects by reading an output database. The new materials are placed in the materials repository.',
	),
	'Model.sectionsFromOdb':(
		'fileName',
		'This method creates Section objects by reading an output database. The new sections are placed in the sections repository.',
	),
	'Model.setValues':(
		'<description, noPartsInputFile, absoluteZero, stefanBoltzmann, waveFormulation, universalGas, restartJob, restartStep, restartIncrement, endRestartStep, globalJob, shellToSolid>',
		'This method modifies the \n Model\n object.\n ',
	),
	'ModelChange.setValues':'<value is a self-reference, replaced by this string>',
	'ModelChange.setValuesInStep':(
		'stepName <, activeInStep, includeStrain>',
		'This method modifies the propagating data of an existing ModelChange object in the specified step.',
	),
	'ModelJob._writeJobKeywords':(
		'',
		'Generates an input file with only Job-related keywords.',
	),
	'ModelJob._writeModelKeywords':(
		'',
		'Generates an input file with all the keywords not output by writeJobKeywords',
	),
	'ModelJob.setValues':'<value is a self-reference, replaced by this string>',
	'ModelJob.writeInput':(
		'<consistencyChecking>',
		'This method writes an input file.',
	),
	'ModulatedAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'MohrCoulombHardening.setValues':'<value is a self-reference, replaced by this string>',
	'MohrCoulombPlasticity.MohrCoulombHardening':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a MohrCoulombHardening object.',
	),
	'MohrCoulombPlasticity.TensionCutOff':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a TensionCutOff object.',
	),
	'MohrCoulombPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'MoistureSwelling.Ratios':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a Ratios object.',
	),
	'MoistureSwelling.setValues':'<value is a self-reference, replaced by this string>',
	'Moment.setValues':'<value is a self-reference, replaced by this string>',
	'Moment.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing Moment object in the specified step.',
	),
	'Monitor.setValues':'<value is a self-reference, replaced by this string>',
	'MonitorMgr.addMessageCallback':(
		'jobName, messageType, callback <, userData>',
		'This method specifies a callback function that will be called when the specified message is received from the analysis product.For more information, see .',
	),
	'MonitorMgr.checkMonitorStatus':(
		'',
		'This method raises a MonitorError exception if the monitoring status is not ENABLED. ',
	),
	'MonitorMgr.removeMessageCallback':(
		'jobName, messageType, callback, userData',
		'This method removes a callback function. You specify the callback function to remove using the same arguments you used to add the callback.',
	),
	'Movie.setValues':(
		'<startFrame, endFrame, timelineStartFrame, timelineEndFrame, timelineStartTime, timelineEndTime>',
		'This method modifies the Movie object.',
	),
	'MovieOptions.setValues':(
		'<movieName, showMovie, positionMethod, fitMethod, alignment, xScale, yScale, origin, translucency, options>',
		'This method modifies the \n MovieOptions\n object.\n ',
	),
	'MullinsEffect.BiaxialTestData':'<value is a self-reference, replaced by this string>',
	'MullinsEffect.PlanarTestData':'<value is a self-reference, replaced by this string>',
	'MullinsEffect.UniaxialTestData':'<value is a self-reference, replaced by this string>',
	'MultipointConstraint.setValues':'<value is a self-reference, replaced by this string>',
	'NetworkDatabaseConnector.setValues':'<value is a self-reference, replaced by this string>',
	'NetworkDatabaseConnector.start':(
		'<serverPort, serverTimeout>',
		'This method starts the remote network database connector server on the remote host.',
	),
	'NetworkDatabaseConnector.stop':(
		'',
		'This method stops the remote network database connector server on the remote host.',
	),
	'NonstructuralMass.setValues':'<value is a self-reference, replaced by this string>',
	'NormalBehavior.setValues':'<value is a self-reference, replaced by this string>',
	'ObjectiveFunction.setValues':'<value is a self-reference, replaced by this string>',
	'Odb.AcousticInfiniteSection':'<value is a self-reference, replaced by this string>',
	'Odb.AcousticInterfaceSection':'<value is a self-reference, replaced by this string>',
	'Odb.ActuatorAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.ArbitraryProfile':'<value is a self-reference, replaced by this string>',
	'Odb.BeamSection':'<value is a self-reference, replaced by this string>',
	'Odb.BoxProfile':'<value is a self-reference, replaced by this string>',
	'Odb.ButterworthFilter':'<value is a self-reference, replaced by this string>',
	'Odb.Chebyshev1Filter':'<value is a self-reference, replaced by this string>',
	'Odb.Chebyshev2Filter':'<value is a self-reference, replaced by this string>',
	'Odb.CircularProfile':'<value is a self-reference, replaced by this string>',
	'Odb.CohesiveSection':'<value is a self-reference, replaced by this string>',
	'Odb.CompositeShellSection':'<value is a self-reference, replaced by this string>',
	'Odb.CompositeSolidSection':'<value is a self-reference, replaced by this string>',
	'Odb.ConnectorSection':'<value is a self-reference, replaced by this string>',
	'Odb.DecayAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.EquallySpacedAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.EulerianSection':'<value is a self-reference, replaced by this string>',
	'Odb.GasketSection':'<value is a self-reference, replaced by this string>',
	'Odb.GeneralStiffnessSection':'<value is a self-reference, replaced by this string>',
	'Odb.GeneralizedProfile':'<value is a self-reference, replaced by this string>',
	'Odb.HexagonalProfile':'<value is a self-reference, replaced by this string>',
	'Odb.HomogeneousShellSection':'<value is a self-reference, replaced by this string>',
	'Odb.HomogeneousSolidSection':'<value is a self-reference, replaced by this string>',
	'Odb.IProfile':'<value is a self-reference, replaced by this string>',
	'Odb.LProfile':'<value is a self-reference, replaced by this string>',
	'Odb.MPCSection':'<value is a self-reference, replaced by this string>',
	'Odb.Material':'<value is a self-reference, replaced by this string>',
	'Odb.MembraneSection':'<value is a self-reference, replaced by this string>',
	'Odb.ModulatedAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.OperatorFilter':'<value is a self-reference, replaced by this string>',
	'Odb.PEGSection':'<value is a self-reference, replaced by this string>',
	'Odb.Part':(
		'name, embeddedSpace, type',
		'This method creates an \n OdbPart\n object. Nodes and elements are added to this object at a later stage.\n ',
	),
	'Odb.PeriodicAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.PipeProfile':'<value is a self-reference, replaced by this string>',
	'Odb.PsdDefinition':'<value is a self-reference, replaced by this string>',
	'Odb.RectangularProfile':'<value is a self-reference, replaced by this string>',
	'Odb.SectionCategory':(
		'name, description',
		'This method creates a SectionCategory object.',
	),
	'Odb.SmoothStepAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.SolutionDependentAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.SpectrumAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.Step':(
		'name, description, domain <, timePeriod, previousStepName, procedure, totalTime>',
		'This method creates an OdbStep object.',
	),
	'Odb.SurfaceSection':'<value is a self-reference, replaced by this string>',
	'Odb.SurfaceToSurfaceContactExp':'<value is a self-reference, replaced by this string>',
	'Odb.SurfaceToSurfaceContactStd':'<value is a self-reference, replaced by this string>',
	'Odb.TProfile':'<value is a self-reference, replaced by this string>',
	'Odb.TabularAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.TrapezoidalProfile':'<value is a self-reference, replaced by this string>',
	'Odb.TrussSection':'<value is a self-reference, replaced by this string>',
	'Odb.UserAmplitude':'<value is a self-reference, replaced by this string>',
	'Odb.close':(
		'',
		'This method closes an output database.',
	),
	'Odb.getFrame':(
		'frameValue <, match>',
		'This method returns the frame at the specified time, frequency, or mode. It will not interpolate values between frames. The method is not applicable to an \n Odb\n object containing steps with different domains or to an \n Odb\n object containing a step with load case specific data.\n ',
	),
	'Odb.getVertices':'<value is a self-reference, replaced by this string>',
	'Odb.hasSectorDefinition':(
		'',
		'This method checks whether or not a valid \n SectorDefinition\n object, indicating a cyclic symmetry model, is present.\n ',
	),
	'Odb.save':(
		'',
		'This method saves output to an output database (\n .odb\n ) file.\n ',
	),
	'Odb.update':(
		'',
		'This method is used to update an \n Odb\n object in memory while an Abaqus analysis writes data to the associated output database. \n update\n checks if additional steps and frames have been written to the output database since it was opened or last updated. If additional steps and frames have been written to the output database, \n update\n adds them to the \n Odb\n object.\n ',
	),
	'OdbAssembly.ConnectorOrientation':(
		'region <, localCsys1, axis1, angle1, orient2sameAs1, localCsys2, axis2, angle2>',
		'This method assigns a connector orientation to a connector region.',
	),
	'OdbAssembly.DatumCsys':(
		'name, datumCsys',
		'This method copies oneOdbDatumCsys object to a new OdbDatumCsys object.',
	),
	'OdbAssembly.DatumCsysBy6dofNode':(
		'name, coordSysType, origin',
		'A datum coordinate system created with this method results in a system that follows the position of a node. The node location defines the origin of the datum coordinate system. The rotational displacement (UR1, UR2, UR3) of the node defines the orientation of the coordinate system axes. Results, such as those for displacement, are resolved into the orientation of the datum coordinate system without regard to the position of its origin. The last argument is given in the form of an OdbMeshNode object.',
	),
	'OdbAssembly.DatumCsysByThreeCircNodes':(
		'name, coordSysType, node1Arc, node2Arc, node3Arc',
		'This method is convenient to use where there are no nodes along the axis of a hollow cylinder or at the center of a hollow sphere. The three nodes that you provide as arguments determine a circle in space. The center of the circle is the origin of the datum coordinate system. The normal to the circle is parallel to the $z$-axis of a cylindrical coordinate system or to the $\\phi$-axis of a spherical coordinate system. The line from the origin to the first node defines the $r$-axis.',
	),
	'OdbAssembly.DatumCsysByThreeNodes':(
		'name, coordSysType, origin, point1, point2',
		'This method creates an OdbDatumCsys object using the coordinates of three OdbMeshNode objects. A datum coordinate system created with this method results in a system that follows the position of the three nodes. Results, such as those for displacement, are resolved into the orientation of the datum coordinate system without regard to the position of its origin. The last three arguments are given in the form of an OdbMeshNode object.',
	),
	'OdbAssembly.DatumCsysByThreePoints':(
		'name, coordSysType, origin, point1, point2',
		'This method creates an OdbDatumCsys object using three points. A datum coordinate system created with this method results in a fixed system. ',
	),
	'OdbAssembly.ElementSet':(
		'name, instanceNames, elementLabels',
		'This method creates an element set.',
	),
	'OdbAssembly.ElementSetFromElementLabels':(
		'name, elementLabels',
		'This method creates an element set from a sequence of element labels.',
	),
	'OdbAssembly.Instance':(
		'name, object <, localCoordSystem>',
		'This method creates an \n OdbInstance\n object from an \n OdbPart\n object.\n ',
	),
	'OdbAssembly.MeshSurface':(
		'name, meshSurfaces',
		'This method creates a surface from the element and side identifiers for the assembly.',
	),
	'OdbAssembly.MeshSurfaceFromElsets':(
		'name, elementSetSeq',
		'This method creates a mesh surface from a sequence of element sets.',
	),
	'OdbAssembly.MeshSurfaceFromLabels':(
		'name, surfaceLabels',
		'This method creates a mesh surface from a sequence of surface labels.',
	),
	'OdbAssembly.NodeSet':(
		'name, instanceNames, nodeLabels',
		'This method creates a node set.',
	),
	'OdbAssembly.NodeSetFromNodeLabels':(
		'name, nodeLabels',
		'This method creates a node set from a sequence of node labels.',
	),
	'OdbAssembly.RigidBody':(
		'referenceNode <, position, isothermal, elements, tieNodes, pinNodes, analyticSurface>',
		'This method creates a OdbRigidBody object.',
	),
	'OdbAssembly.SectionAssignment':(
		'region, section',
		'This method is used to assign a section to a region on an instance.  Only connector sections can be assigned at the assembly level.',
	),
	'OdbAssembly.Surface':(
		'name, instanceNames, elementLabels, faces',
		'This method creates a surface set.',
	),
	'OdbAssembly.addElements':(
		'labels, connectivity, instanceNames, type <, elementSetName, sectionCategory>',
		'This method is used to define elements using nodes defined at the \n OdbAssembly\n and/or \n OdbInstance\n level. For connector elements connected to ground, specify the lone node in the connectivity. The position of the ground node cannot be specified. This is a limitation.\n ',
	),
	'OdbAssembly.addNodes':(
		'labels, coordinates <, nodeSetName>',
		'This method adds nodes to the \n OdbAssembly\n object using node labels and coordinates.\n Adding nodes not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.',
	),
	'OdbAssembly.sectionAssignments':(
		'index',
		'This method is used to retrieve a section assignment.',
	),
	'OdbData.setValues':(
		'<activeFrames, stepPeriods>',
		'This method modifies the OdbData object.',
	),
	'OdbDataFrame.setValues':(
		'activateFrame <, update>',
		'This method modifies the OdbDataFrame object.',
	),
	'OdbDataStep.setValues':(
		'activateFrames <, update>',
		'This method modifies the OdbDataStep object.',
	),
	'OdbDisplay.ViewCut':(
		'name, shape, origin, normal, axis2, csysName, cylinderAxis <, followDeformation, overrideAveraging, overrideRgnBoundaryAvg, referenceFrame>',
		'This method creates a ViewCut object.',
	),
	'OdbDisplay.moveCameraToCsys':(
		'',
		'This method specifies a new position for the camera. It is available only when movieMode=ON (in the View object). The new camera position is the origin of the coordinate system specified by the cameraCsysName member of the BasicOptions object.',
	),
	'OdbDisplay.setDeformedVariable':(
		'variableLabel, field',
		'This method specifies the field output variable or FieldOutput object to be used when displaying the deformed shape of the model.',
	),
	'OdbDisplay.setFrame':(
		'frame',
		'This method specifies the frame for the OdbDisplay object.',
	),
	'OdbDisplay.setPrimarySectionPoint':(
		'sectionPoint, activePly',
		'This method specifies the section point for the current primary, symbol and status variables.',
	),
	'OdbDisplay.setPrimaryVariable':(
		'variableLabel, field, outputPosition <, refinement, sectionPoint>',
		'This method specifies the field output variable for which to obtain results.',
	),
	'OdbDisplay.setStatusVariable':(
		'variableLabel, field, outputPosition <, refinement, sectionPoint, statusMinimum, statusMaximum, statusInsideRange, useStatus, applyStatusToUndeformed>',
		'This method specifies the field output variable for filtering element display based on a status criteria.',
	),
	'OdbDisplay.setStreamVariable':(
		'variableLabel',
		'This method specifies the field output variable for which to obtain results used for stream plots. This variable must be in the form of nodal vector data.',
	),
	'OdbDisplay.setSymbolVariable':(
		'variableLabel, field, outputPosition <, refinement, sectionPoint, tensorQuantity, vectorQuantity>',
		'This method specifies the field output variable for which to obtain results used for symbol plots. This variable must be in the form of vector or tensor data.  The output quantity can also be specified with this command to control the display of resultants, or components.',
	),
	'OdbDisplay.setValues':(
		'<visibleDisplayGroups, viewCut, viewCutNames>',
		'This method specifies member values for the OdbDisplay object.',
	),
	'OdbFrame.FieldOutput':(
		'field <, name, description>',
		'This method creates a \n FieldOutput\n object from an existing \n FieldOutput\n object.\n ',
	),
	'OdbFrame.MatrixOutput':(
		'name, description, rows, cols',
		'This method creates a \n FieldOutput\n object.\n ',
	),
	'OdbFrame.SymmetricMatrixOutput':(
		'name, description, dim',
		'This method creates a \n FieldOutput\n object.\n ',
	),
	'OdbFrame.VectorOutput':(
		'name, description, width',
		'This method creates a \n FieldOutput\n object.\n ',
	),
	'OdbInstance.AnalyticRigidSurf2DPlanar':(
		'name, profile <, filletRadius>',
		'This method is used to define a two-dimensional \n AnalyticSurface\n object on the instance.\n ',
	),
	'OdbInstance.AnalyticRigidSurfExtrude':(
		'name, profile <, filletRadius, localCoordData>',
		'This method is used to define a three-dimensional cylindrical \n AnalyticSurface\n on the instance.\n ',
	),
	'OdbInstance.AnalyticRigidSurfRevolve':(
		'name, profile <, filletRadius, localCoordData>',
		'This method is used to define a three-dimensional \n AnalyticSurface\n of revolution on the instance.\n ',
	),
	'OdbInstance.ElementSet':'<value is a self-reference, replaced by this string>',
	'OdbInstance.ElementSetFromElementLabels':'<value is a self-reference, replaced by this string>',
	'OdbInstance.MeshSurface':'<value is a self-reference, replaced by this string>',
	'OdbInstance.MeshSurfaceFromElsets':'<value is a self-reference, replaced by this string>',
	'OdbInstance.MeshSurfaceFromLabels':'<value is a self-reference, replaced by this string>',
	'OdbInstance.NodeSet':'<value is a self-reference, replaced by this string>',
	'OdbInstance.NodeSetFromNodeLabels':'<value is a self-reference, replaced by this string>',
	'OdbInstance.RigidBody':'<value is a self-reference, replaced by this string>',
	'OdbInstance.Surface':'<value is a self-reference, replaced by this string>',
	'OdbInstance.assignBeamOrientation':(
		'region, method, vector',
		'This method assigns a beam section orientation to a region of a part instance.',
	),
	'OdbInstance.assignMaterialOrientation':(
		'region, localCsys <, axis, angle, stackDirection>',
		'This method assigns a material orientation to a region of a part instance.',
	),
	'OdbInstance.assignRebarOrientation':(
		'region, localCsys <, axis, angle>',
		'This method assigns a rebar reference orientation to a region of a part instance.',
	),
	'OdbInstance.assignSection':(
		'region, section',
		'This method is used to assign a section to a region on an instance.',
	),
	'OdbInstance.getElementFromLabel':(
		'label',
		'This method is used to retrieved an element with a specific label from an instance object.',
	),
	'OdbInstance.getNodeFromLabel':(
		'label',
		'This method is used to retrieved a node with a specific label from an instance object.',
	),
	'OdbInstance.nodesLabelsFromNodeTypeFace':(
		'elementNodeLabels, elementType, elementFace',
		'Given a sequence of integers defining an element connectivity, this method is used to retrieve the sequence of nodes attached to a specified face of the element based on element type.',
	),
	'OdbMeshRegionData.setValues':'<value is a self-reference, replaced by this string>',
	'OdbPart.AnalyticRigidSurf2DPlanar':(
		'name, profile <, filletRadius>',
		'This method is used to define a two-dimensional \n AnalyticSurface\n object on the part object.\n ',
	),
	'OdbPart.AnalyticRigidSurfExtrude':(
		'name, profile <, filletRadius>',
		'This method is used to define a three-dimensional cylindrical \n AnalyticSurface\n on the part object.\n ',
	),
	'OdbPart.AnalyticRigidSurfRevolve':(
		'name, profile <, filletRadius>',
		'This method is used to define a three-dimensional \n AnalyticSurface\n of revolution on the part object.\n ',
	),
	'OdbPart.ElementSet':'<value is a self-reference, replaced by this string>',
	'OdbPart.ElementSetFromElementLabels':'<value is a self-reference, replaced by this string>',
	'OdbPart.MeshSurface':'<value is a self-reference, replaced by this string>',
	'OdbPart.MeshSurfaceFromElsets':'<value is a self-reference, replaced by this string>',
	'OdbPart.MeshSurfaceFromLabels':'<value is a self-reference, replaced by this string>',
	'OdbPart.NodeSet':'<value is a self-reference, replaced by this string>',
	'OdbPart.NodeSetFromNodeLabels':'<value is a self-reference, replaced by this string>',
	'OdbPart.RigidBody':(
		'referenceNode <, position, isothermal, elset, pinNodes, tieNodes>',
		'This method defines an \n OdbRigidBody\n on the part object.\n ',
	),
	'OdbPart.Surface':'<value is a self-reference, replaced by this string>',
	'OdbPart.addElements':(
		'elementData, type <, elementSetName, sectionCategory>',
		'This method adds elements to an \n OdbPart\n object using a sequence of element labels and nodal connectivity.\n ',
	),
	'OdbPart.addNodes':(
		'nodeData <, nodeSetName>',
		'This method adds nodes to an \n OdbPart\n object using a sequence of node labels and coordinates.\n Adding nodes not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.',
	),
	'OdbPart.assignBeamOrientation':'<value is a self-reference, replaced by this string>',
	'OdbPart.assignMaterialOrientation':(
		'region, localCSys <, axis, angle, stackDirection>',
		'This method assigns a material orientation to a region of a part instance.',
	),
	'OdbPart.assignRebarOrientation':'<value is a self-reference, replaced by this string>',
	'OdbPart.getElementFromLabel':(
		'label',
		'This method is used to retrieved an element with a specific label from a part object.',
	),
	'OdbPart.getNodeFromLabel':(
		'label',
		'This method is used to retrieved a node with a specific label from a part object.',
	),
	'OdbSequenceAnalyticSurfaceSegment.Circle':(
		'center, endPoint',
		'This method adds a AnalyticSurfaceSegment describing a circular segment of the surface profile.',
	),
	'OdbSequenceAnalyticSurfaceSegment.Line':(
		'endPoint',
		'This method adds a AnalyticSurfaceSegment describing the line segment of the surface profile.',
	),
	'OdbSequenceAnalyticSurfaceSegment.Parabola':(
		'middlePoint, endPoint',
		'This method adds a AnalyticSurfaceSegment describing a parabolic segment of the surface profile.',
	),
	'OdbSequenceAnalyticSurfaceSegment.Start':(
		'origin',
		'This method adds a AnalyticSurfaceSegment describing the first segment of the surface profile.',
	),
	'OdbStep.Frame':(
		'loadCase <, description, frequency>',
		'This constructor creates an OdbFrame object for a specific load case and appends it to the frame sequence. ',
	),
	'OdbStep.HistoryRegion':(
		'name, description, point <, loadCase>',
		'This method creates a HistoryRegion object.',
	),
	'OdbStep.LoadCase':(
		'name',
		'This method creates an OdbLoadCase object.',
	),
	'OdbStep.getFrame':(
		'loadCase, frameValue <, match>',
		'This method retrieves an OdbFrame object associated with a given load case and frame value.',
	),
	'OdbStep.getHistoryRegion':(
		'point <, loadCase>',
		'This method retrieves a HistoryRegion object associated with a HistoryPoint in the model.',
	),
	'OdbStep.setDefaultDeformedField':(
		'field',
		'This method sets the default deformed field variable in a step.',
	),
	'OdbStep.setDefaultField':(
		'field',
		'This method sets the default field variable in a step.',
	),
	'OperatorFilter.setValues':'<value is a self-reference, replaced by this string>',
	'OptimizationConstraint.setValues':'<value is a self-reference, replaced by this string>',
	'OptimizationProcess.extract':(
		'outputFileName, designCycle <, isoValue, smoothCycles, reductionPercent, reductionAngle, targetVolume, extractFormat, resultFiltering>',
		'This method extracts a surface mesh from the optimized model.',
	),
	'OptimizationProcess.setValues':'<value is a self-reference, replaced by this string>',
	'OptimizationProcess.submit':(
		'<validate>',
		'This method submits an optimization process.',
	),
	'OptimizationProcess.waitForCompletion':(
		'',
		'This method interrupts the execution of the script until the end of all the analyses. If you call the waitForCompletion method and the status member is neither SUBMITTED nor RUNNING, Abaqus assumes the analysis has either completed or aborted and returns immediately.\n ',
	),
	'OptimizationTask.CombinedTermDesignResponse':(
		'name, terms <, filterMaxRadius, filterExponent, filterRadiusReduction, highCutOff, lowCutOff, method, weights>',
		'This method creates a CombinedTermDesignResponse object.',
	),
	'OptimizationTask.DesignDirection':(
		'name, region <, csys, masterPoint, masterPointDetermination, movementRestriction, presumeFeasibleRegionAtStart, u1, u2, u3>',
		'This method creates a DesignDirection object.',
	),
	'OptimizationTask.DrillControl':(
		'name, clientDirection, region <, csys, drawAngle, masterPoint, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3, undercutTolerance>',
		'This method creates a DrillControl object.',
	),
	'OptimizationTask.FixedRegion':(
		'name, region <, csys, presumeFeasibleRegionAtStart, u1, u2, u3>',
		'This method creates a FixedRegion object.',
	),
	'OptimizationTask.FrozenArea':(
		'name <, region>',
		'This method creates a FrozenArea object.',
	),
	'OptimizationTask.Growth':(
		'name, region <, growth, presumeFeasibleRegionAtStart, shrink>',
		'This method creates a Growth object.',
	),
	'OptimizationTask.LocalStopCondition':(
		'name, referenceFactor <, comparisonOperation, identifier, identifierOperation, referenceDesignCycle, referenceOperation, region>',
		'This method creates a LocalStopCondition object.',
	),
	'OptimizationTask.ObjectiveFunction':(
		'name, objectives <, target>',
		'This method creates an ObjectiveFunction object.',
	),
	'OptimizationTask.OptimizationConstraint':(
		'name, designResponse, restrictionValue <, restrictionMethod>',
		'This method creates an OptimizationConstraint object.',
	),
	'OptimizationTask.PenetrationCheck':(
		'name, penetrationCheckRegion, region <, presumeFeasibleRegionAtStart>',
		'This method creates a PenetrationCheck object.',
	),
	'OptimizationTask.ShapeDemoldControl':(
		'name, pullDirection, region <, collisionCheckRegion, csys, drawAngle, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3, undercutTolerance>',
		'This method creates a ShapeDemoldControl object.',
	),
	'OptimizationTask.ShapeMemberSize':(
		'name, region <, maxThickness, minThickness, sizeRestriction>',
		'This method creates a ShapeMemberSize object.',
	),
	'OptimizationTask.ShapePlanarSymmetry':(
		'name, clientDirection, region <, csys, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3>',
		'This method creates a ShapePlanarSymmetry object.',
	),
	'OptimizationTask.ShapePointSymmetry':(
		'name, region <, csys, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3>',
		'This method creates a ShapePointSymmetry object.',
	),
	'OptimizationTask.ShapeRotationalSymmetry':(
		'name, clientDirection, region <, angle, csys, masterPoint, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3>',
		'This method creates a ShapeRotationalSymmetry object.',
	),
	'OptimizationTask.SingleTermDesignResponse':(
		'name, identifier <, csys, drivingRegion, operation, region, shellLayer, stepOperation, stepOptions>',
		'This method creates a SingleTermDesignResponse object.',
	),
	'OptimizationTask.SlideRegionControl':(
		'name, clientDirection, region <, approach, csys, freeFormRegion, presumeFeasibleRegionAtStart, revolvedRegion, tolerance1, tolerance2, tolerance3>',
		'This method creates a SlideRegionControl object.',
	),
	'OptimizationTask.StampControl':(
		'name, clientDirection, region <, csys, drawAngle, masterPoint, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3, undercutTolerance>',
		'This method creates a StampControl object.',
	),
	'OptimizationTask.TopologyCyclicSymmetry':(
		'name, region, translation <, axis, csys, ignoreFrozenArea>',
		'This method creates a TopologyCyclicSymmetry object.',
	),
	'OptimizationTask.TopologyDemoldControl':(
		'name, region <, csys, draftAngle, collisionCheckRegion, pointRegion, pullDirection, technique>',
		'This method creates a TopologyDemoldControl object.',
	),
	'OptimizationTask.TopologyMemberSize':(
		'name, region <, maxThickness, minThickness, separation, sizeRestriction>',
		'This method creates a TopologyMemberSize object.',
	),
	'OptimizationTask.TopologyOverhangControl':(
		'name, region <, csys, draftAngle, collisionCheckRegion, pointRegion, pullDirection, radius>',
		'This method creates a TopologyOverhangControl object.',
	),
	'OptimizationTask.TopologyPlanarSymmetry':(
		'name, region <, axis, csys, ignoreFrozenArea>',
		'This method creates a TopologyPlanarSymmetry object.',
	),
	'OptimizationTask.TopologyPointSymmetry':(
		'name, region <, csys, ignoreFrozenArea>',
		'This method creates a TopologyPointSymmetry object.',
	),
	'OptimizationTask.TopologyRotationalSymmetry':(
		'name, angle, region <, axis, csys, ignoreFrozenArea>',
		'This method creates a TopologyRotationalSymmetry object.',
	),
	'OptimizationTask.TurnControl':(
		'name, clientDirection, region <, csys, masterPoint, masterPointDetermination, presumeFeasibleRegionAtStart, tolerance1, tolerance2, tolerance3>',
		'This method creates a TurnControl object.',
	),
	'OptimizationTaskDisplayOptions.setValues':(
		'<topologyTask, shapeTask>',
		'This method modifies the OptimizationTaskDisplayOptions object.',
	),
	'OrientationOptions.setValues':(
		'<options, axis1Color, showAxis1, axis2Color, showAxis2, axis3Color, showAxis3, symbolSize, lineThickness, arrowheadStyle, scaleMode>',
		'This method modifies the OrientationOptions object.',
	),
	'Ornl.setValues':'<value is a self-reference, replaced by this string>',
	'PEGLoad.setValues':'<value is a self-reference, replaced by this string>',
	'PEGLoad.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing PEGLoad object in the specified step.',
	),
	'PEGSection.setValues':'<value is a self-reference, replaced by this string>',
	'PageSetupOptions.setValues':(
		'<imageSize, units, quality, topMargin, bottomMargin, leftMargin, rightMargin, orientation, logo, date>',
		'This method modifies the \n PageSetupOptions\n object.\n ',
	),
	'Part.AddCells':(
		'faceList <, flipped>',
		'This method tries to convert a shell entity to a solid entity. The conversion is not always successful.',
	),
	'Part.AnalyticRigidSurf2DPlanar':(
		'sketch',
		'This method creates a first Feature object for an analytical rigid surface by creating a planar wire from the given ConstrainedSketch object.',
	),
	'Part.AnalyticRigidSurfExtrude':(
		'sketch <, depth>',
		'This method creates a first Feature object for an analytical rigid surface by extruding the given ConstrainedSketch object by the given depth, creating a surface.',
	),
	'Part.AnalyticRigidSurfRevolve':(
		'sketch',
		'This method creates a first Feature object for an analytical rigid surface by revolving the given ConstrainedSketch object by 360&#176; about the Y-axis.',
	),
	'Part.AssignMidsurfaceRegion':(
		'cellList',
		'This method assign a mid-surface property to sequence of Cell objects. If a reference representation of the part does not exist, it creates one. It also copies the cells to the reference representation and deletes the cells from the active representation of the part.',
	),
	'Part.AttachmentPoints':'<value is a self-reference, replaced by this string>',
	'Part.AttachmentPointsAlongDirection':'<value is a self-reference, replaced by this string>',
	'Part.AttachmentPointsOffsetFromEdges':'<value is a self-reference, replaced by this string>',
	'Part.AutoRepair':(
		'',
		'This method carries out a sequence of geometry repair operations if it contains invalid entities.  It is expected to improve the geometry, but it does not guarantee that the number of invalid entities will decrease.  In some cases, it can also increase the number of invalid entities.  Since a number of geometry repair operations and validity checks are performed, it could be a slow operation depending on the complexity of the geometry.',
	),
	'Part.BaseShell':(
		'sketch',
		'This method creates a first Feature object by creating a planar shell from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.',
	),
	'Part.BaseShellExtrude':(
		'sketch, depth <, draftAngle, pitch>',
		'This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell. The ConstrainedSketch object can define either an open or closed profile.',
	),
	'Part.BaseShellRevolve':(
		'sketch, angle <, pitch, flipRevolveDirection, flipPitchDirection, moveSketchNormalToPath>',
		'This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell. The ConstrainedSketch object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line.',
	),
	'Part.BaseShellSweep':(
		'sketch, path',
		'This method creates a first Feature object by sweeping the given section ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a shell. The ConstrainedSketch object can define either an open or closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self-intersection.',
	),
	'Part.BaseSolidExtrude':(
		'sketch, depth <, draftAngle, pitch>',
		'This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid. The ConstrainedSketch object must define a closed profile.',
	),
	'Part.BaseSolidRevolve':(
		'sketch, angle <, pitch, flipRevolveDirection, flipPitchDirection, moveSketchNormalToPath>',
		'This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid. The ConstrainedSketch object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.',
	),
	'Part.BaseSolidSweep':(
		'sketch, path',
		'This method creates a first Feature object by sweeping the given profile ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a solid. The profile ConstrainedSketch object must define a closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self-intersection.',
	),
	'Part.BaseWire':(
		'sketch',
		'This method creates a first Feature object by creating a planar wire from the given ConstrainedSketch object.',
	),
	'Part.BlendFaces':(
		'side1, side2 <, method, path>',
		'This method creates a Feature object by creating new faces that blends two sets of faces.',
	),
	'Part.Chamfer':(
		'length, edgeList',
		'This method creates an additional Feature object by chamfering the given list of edges with a given length.',
	),
	'Part.CompositeLayup':(
		'name <, description, offsetType, offsetField, offsetValues, elementType>',
		'This method creates a CompositeLayup object.',
	),
	'Part.ConvertToAnalytical':(
		'',
		'This method attempts to change entities into a simpler form that will speed up processing and make entities available during feature operations.',
	),
	'Part.ConvertToPrecise':(
		'<method>',
		'This method attempts to change imprecise entities so that the geometry becomes precise. ',
	),
	'Part.CoverEdges':(
		'edgeList <, tryAnalytical>',
		"This method generates a face using the given edges as the face's boundaries. The CoverEdges method generates a face by creating the geometry consisting of the underlying surface, associated edges, and vertices.",
	),
	'Part.Cut':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch <, sketchOrientation>',
		'This method creates an additional Feature object by cutting a hole using the given ConstrainedSketch object.',
	),
	'Part.CutExtrude':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketchOrientation, sketch <, depth, upToFace, draftAngle, pitch, flipExtrudeDirection>',
		'This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth and cutting away material in the solid and shell regions of the part. The ConstrainedSketch object must define a closed profile. The CutExtrude method creates a blind cut (using depth), an up-to-face cut (using upToFace), or a through-all cut (if depth and upToFace are not specified).',
	),
	'Part.CutLoft':(
		'loftsections <, startCondition, endCondition, startTangent, startMagnitude, endTangent, endMagnitude, globalSmoothing>',
		'This method creates an additional Feature object by lofting between the given sections and cutting away material from the part. You define the sections using a sequence of edges from the part or an EdgeArray.',
	),
	'Part.CutRevolve':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketchOrientation, sketch, angle <, pitch, flipRevolveDirection, flipPitchDirection, moveSketchNormalToPath>',
		'This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle and cutting away material from the part. The ConstrainedSketch object must define a closed profile and an axis of revolution.',
	),
	'Part.CutSweep':(
		'path, profile <, pathPlane, pathUpEdge, pathOrientation, sketchPlane, sketchUpEdge, sketchOrientation, draftAngle, pitch, profileNormal, flipSweepDirection>',
		'This method creates an additional Feature object by sweeping the given ConstrainedSketch object along a path which may be a ConstrainedSketch or a sequence of Edge objects and cutting away material from the part. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.',
	),
	'Part.DatumAxisByCylFace':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByNormalToPlane':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByParToEdge':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByPrincipalAxis':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByRotation':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByThreePoint':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByThruEdge':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByTwoPlane':'<value is a self-reference, replaced by this string>',
	'Part.DatumAxisByTwoPoint':'<value is a self-reference, replaced by this string>',
	'Part.DatumCsysByDefault':'<value is a self-reference, replaced by this string>',
	'Part.DatumCsysByOffset':'<value is a self-reference, replaced by this string>',
	'Part.DatumCsysByThreePoints':'<value is a self-reference, replaced by this string>',
	'Part.DatumCsysByTwoLines':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByLinePoint':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByOffset':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByPointNormal':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByPrincipalPlane':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByRotation':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByThreePoints':'<value is a self-reference, replaced by this string>',
	'Part.DatumPlaneByTwoPoint':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByCoordinate':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByEdgeParam':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByMidPoint':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByOffset':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByOnFace':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByProjOnEdge':'<value is a self-reference, replaced by this string>',
	'Part.DatumPointByProjOnFace':'<value is a self-reference, replaced by this string>',
	'Part.EditSkin':(
		'name <, faces, edges, elementFaces, elementEdges>',
		'This method modifies underlying entities of the selected skin. At least one of the optional arguments needs to be specified.',
	),
	'Part.EditStringer':(
		'name <, edges, elementEdges>',
		'This method modifies underlying entities of the selected stringer. At least one of the optional arguments needs to be specified.',
	),
	'Part.Element':(
		'nodes, elemShape <, label>',
		'This method creates an element on an orphan mesh part from a sequence of nodes.',
	),
	'Part.ExtendFaces':(
		'<faces, extendAlong, distance, upToFaces, trimToExtendedTargetSurfaces, upToReferenceRep>',
		'This method extends faces along its free edges by offsetting the external edges along the surfaces. One of distance, upToReferenceRep, or upToFaces must be used to specify how far the faces need to be extended.',
	),
	'Part.FaceFromElementFaces':(
		'elementFaces',
		'This method creates a geometry face from a collection of orphan element faces.',
	),
	'Part.HoleBlindFromEdges':(
		'plane, planeSide, diameter, edge1, distance1, edge2, distance2, depth',
		'This method creates an additional Feature object by creating a circular blind hole of the given diameter and depth and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.',
	),
	'Part.HoleFromEdges':(
		'diameter, edge1, distance1, edge2, distance2',
		'This method creates an additional Feature object by creating a circular hole of the given diameter in a 2D planar part and cutting away material in the shell and wire regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.',
	),
	'Part.HoleThruAllFromEdges':(
		'plane, planeSide, diameter, edge1, distance1, edge2, distance2',
		'This method creates an additional Feature object by creating a circular through hole of the given diameter and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.',
	),
	'Part.InterestingPoint':(
		'edge, rule',
		'This method creates an interesting point along an edge. An InterestingPoint is a temporary object.',
	),
	'Part.Lock':(
		'',
		'This method locks the part. Locking the part prevents any further changes to the part that can trigger regeneration of the part.',
	),
	'Part.LockForUpgrade':(
		'',
		'This method locks the part for upgrade. Locking the part prevents any further changes to the part that can trigger regeneration of the part. When the part is unlocked, all the parts are upgraded and regenrated.',
	),
	'Part.MakeSketchTransform':'<value is a self-reference, replaced by this string>',
	'Part.MapSetsFromOdb':(
		'odbPath, odbSets <, partSets, method>',
		'This method creates sets based on mapping sets from element centroid locations in an Odb.',
	),
	'Part.MaterialOrientation':(
		'<region, localCsys, axis, angle, stackDirection, fieldName, orientationType, normalAxisDirection, normalAxisDefinition, normalAxisRegion, normalAxisDatum, flipNormalDirection, normalAxisVector, primaryAxisDirection, primaryAxisDefinition, primaryAxisRegion, primaryAxisDatum, flipPrimaryDirection, primaryAxisVector>',
		'This method creates a \n MaterialOrientation \n object.\n ',
	),
	'Part.MergeEdges':(
		'<edgeList, extendSelection>',
		'This method merges edges either by extending the user selection or using only the selected edges.',
	),
	'Part.Node':(
		'coordinates <, localCsys, label>',
		'This method creates a node on an orphan mesh part.',
	),
	'Part.OffsetFaces':(
		'faceList <, distance, targetFaces, targetFacesMethod, fractionDistance, trimToReferenceRep>',
		'This method creates new faces by offsetting existing faces.',
	),
	'Part.PartFromMesh':(
		'name <, copySets>',
		'This method creates a Part object containing the mesh found in the part and places the new Part object in the parts repository.',
	),
	'Part.PartitionCellByDatumPlane':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByExtendFace':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByExtrudeEdge':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByPatchNCorners':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByPatchNEdges':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByPlaneNormalToEdge':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByPlanePointNormal':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellByPlaneThreePoints':'<value is a self-reference, replaced by this string>',
	'Part.PartitionCellBySweepEdge':'<value is a self-reference, replaced by this string>',
	'Part.PartitionEdgeByDatumPlane':'<value is a self-reference, replaced by this string>',
	'Part.PartitionEdgeByParam':'<value is a self-reference, replaced by this string>',
	'Part.PartitionEdgeByPoint':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByAuto':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByCurvedPathEdgeParams':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByCurvedPathEdgePoints':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByDatumPlane':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByExtendFace':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByIntersectFace':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByProjectingEdges':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceByShortestPath':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceBySketch':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceBySketchDistance':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceBySketchRefPoint':'<value is a self-reference, replaced by this string>',
	'Part.PartitionFaceBySketchThruAll':'<value is a self-reference, replaced by this string>',
	'Part.ReferencePoint':'<value is a self-reference, replaced by this string>',
	'Part.RemoveCells':(
		'cellList',
		'This method converts a solid entity to a shell entity.',
	),
	'Part.RemoveFaces':(
		'faceList <, deleteCells>',
		'This method removes faces from a solid entity or from a shell entity.',
	),
	'Part.RemoveFacesAndStitch':(
		'faceList',
		'This method removes faces from a solid entity and attempts to close the resulting gap by extending the neighboring faces of the solid.',
	),
	'Part.RemoveRedundantEntities':(
		'<vertexList, edgeList, removeEdgeVertices>',
		'This method removes redundant edges and vertices from a solid or a shell entity. One of the two arguments is required.',
	),
	'Part.RemoveWireEdges':'<value is a self-reference, replaced by this string>',
	'Part.RepairFaceNormals':(
		'<faceList>',
		"This method works on the entire part or a sequence of shell faces.  When the entire part is selected, it aligns all the shell face normals, and inverts all of the solid faces' normals if the solid was originally inside out.  When a few shell faces are selected, it inverts the normals of the selected faces.",
	),
	'Part.RepairInvalidEdges':(
		'edgeList',
		'This method repairs invalid edges. It will always attempt to improve edges even if none of selected edges are initially invalid and may leave behind invalid edges that could not be repaired.',
	),
	'Part.RepairSliver':(
		'face, point1, point2 <, toleranceChecks>',
		'This method repairs the selected sliver from the selected face. The sliver area is specified using two points. A face partition is carried out at the specified points and the smaller of the two faces is removed.',
	),
	'Part.RepairSmallEdges':(
		'edgeList <, toleranceChecks>',
		'This method repairs small edges. This method will attempt to replace selected small edges with vertices and extend the adjacent faces and edges. This method might leave behind some small edges that cannot be removed.',
	),
	'Part.RepairSmallFaces':(
		'faceList <, toleranceChecks>',
		'This method repairs small faces. It will attempt to replace the selected small faces with edges or vertices  and extend the adjacent faces. This method might leave behind some small faces that cannot be removed.',
	),
	'Part.ReplaceFaces':(
		'faceList <, stitch>',
		'This method replaces the selected faces with a single face. If one single face is selected, that alone is replaced with a new face.',
	),
	'Part.Round':(
		'radius, edgeList, vertexList',
		'This method creates an additional Feature object by rounding (filleting) the given list of entities with the given radius.',
	),
	'Part.SectionAssignment':'<value is a self-reference, replaced by this string>',
	'Part.Set':'<value is a self-reference, replaced by this string>',
	'Part.SetByBoolean':'<value is a self-reference, replaced by this string>',
	'Part.SetFromColor':(
		'name, color',
		'This method creates a set containing faces of the part marked with a specified color attribute. Third-party applications can assign color attributes to faces, and the color attribute can be imported into Abaqus from an ACIS file. You can use this method to create sets only on parts; however, you can access the sets from instances of the parts in the assembly.',
	),
	'Part.SetFromElementLabels':'<value is a self-reference, replaced by this string>',
	'Part.SetFromNodeLabels':'<value is a self-reference, replaced by this string>',
	'Part.Shell':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch <, sketchOrientation>',
		'This method creates an additional Feature object by creating a planar shell from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.',
	),
	'Part.ShellExtrude':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch <, depth, upToFace, sketchOrientation, draftAngle, pitch, flipExtrudeDirection, keepInternalBoundaries>',
		'This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell protrusion. The ConstrainedSketch object can define either an open or closed profile.',
	),
	'Part.ShellLoft':(
		'loftsections <, startCondition, endCondition, startTangent, startMagnitude, endTangent, endMagnitude, paths, globalSmoothing, keepInternalBoundaries>',
		'This method creates an additional Feature object by lofting between the given sections and adding shell faces to the part. You define the sections using a sequence of edges from the part or an EdgeArray.',
	),
	'Part.ShellRevolve':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch, angle <, sketchOrientation, pitch, flipRevolveDirection, flipPitchDirection, moveSketchNormalToPath, keepInternalBoundaries>',
		'This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell protrusion. The ConstrainedSketch object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line. For a description of the plane positioning arguments, see SolidExtrude.',
	),
	'Part.ShellSweep':(
		'path, profile <, pathPlane, pathUpEdge, pathOrientation, sketchPlane, sketchUpEdge, sketchOrientation, draftAngle, pitch, profileNormal, flipSweepDirection, keepInternalBoundaries>',
		'This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a sequence of Edge objects along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a shell swept protrusion. The section can be an open or a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.',
	),
	'Part.Skin':(
		'name <, faces, edges, elementFaces, elementEdges>',
		'This method creates a skin from a sequence of objects in a model database. At least one of the optional arguments needs to be specified.',
	),
	'Part.SolidExtrude':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch <, depth, upToFace, sketchOrientation, draftAngle, pitch, flipExtrudeDirection, keepInternalBoundaries>',
		'This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid protrusion. The ConstrainedSketch object must define a closed profile.',
	),
	'Part.SolidLoft':(
		'loftsections <, startCondition, endCondition, startTangent, startMagnitude, endTangent, endMagnitude, paths, globalSmoothing, keepInternalBoundaries>',
		'This method creates an additional Feature object by lofting between the given sections and adding material to the part. You define the sections using a sequence of edges from the part or an EdgeArray.',
	),
	'Part.SolidRevolve':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch, angle <, sketchOrientation, pitch, flipRevolveDirection, flipPitchDirection, moveSketchNormalToPath, keepInternalBoundaries>',
		'This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid protrusion. The ConstrainedSketch object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.',
	),
	'Part.SolidSweep':(
		'path, profile <, pathPlane, pathUpEdge, pathOrientation, sketchPlane, sketchUpEdge, sketchOrientation, draftAngle, pitch, profileNormal, flipSweepDirection, keepInternalBoundaries>',
		'This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a Face object along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a solid swept protrusion. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.  ',
	),
	'Part.Stitch':(
		'<edgeList, stitchTolerance>',
		'This method attempts to create a valid part by binding together free and imprecise edges of all the faces of a part. If edgeList is not given, a global stitch will be performed. If stitchTolerance is not specified, a value of 1.0 will be used.',
	),
	'Part.Stringer':(
		'name <, edges, elementEdges>',
		'This method creates a stringer from a sequence of objects in a model database. At least one of the optional arguments needs to be specified.',
	),
	'Part.Surface':'<value is a self-reference, replaced by this string>',
	'Part.SurfaceByBoolean':'<value is a self-reference, replaced by this string>',
	'Part.Unlock':(
		'',
		'This method unlocks the part. Unlocking the part allows it to be regenerated after any modifications to the part.',
	),
	'Part.Wire':(
		'sketchPlane, sketchPlaneSide, sketchUpEdge, sketch <, sketchOrientation>',
		'This method creates an additional Feature object by creating a planar wire from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.',
	),
	'Part.WireFromEdge':(
		'edgeList',
		'This method creates an additional Feature object by creating a Wire by selecting one or more Edge objects of a Solid or Shell part.',
	),
	'Part.WirePolyLine':'<value is a self-reference, replaced by this string>',
	'Part.WireSpline':(
		'points <, mergeType, smoothClosedSpline>',
		'This method creates an additional Feature object by creating a spline wire that passes through a sequence of given points. Each point can be either a datum point, a vertex, an interesting point, or a tuple.',
	),
	'Part._generateDelTri':'<value is a self-reference, replaced by this string>',
	'Part._generateMedialAxis':'<value is a self-reference, replaced by this string>',
	'Part._queryMesh':'<value is a self-reference, replaced by this string>',
	'Part._removeMedialAxis':'<value is a self-reference, replaced by this string>',
	'Part._seedPartInstanceBySolution':(
		'regions, size <, constraint, lowTemp, highTemp, highTempElementReduction, fileName>',
		'This method applies local edge seeds to the given parts based on solution measures. The solution measures are the boundary curvature and the solution temperature, as read from an output database file.',
	),
	'Part._setTriToTetOptions':(
		'<useNonDefaultMesher, propagationCoef>',
		'This method sets options for generating an orphan tet mesh from a triangular shell mesh.',
	),
	'Part.addGeomToSketch':(
		'sketch',
		'This method converts a part into a sketch by projecting all of the edges of the part onto the X-Y plane of the sketch. You can use addGeomToSketch with a part of any modeling space.',
	),
	'Part.adjustMidsideNode':(
		'cornerNodes, parameter',
		'This method is used to adjust the midside node of second-order elements of an orphan mesh part.',
	),
	'Part.assignStackDirection':'<value is a self-reference, replaced by this string>',
	'Part.assignThickness':(
		'faces <, thickness, topFaces, bottomFaces>',
		'This method assigns thickness data to shell faces. The thickness can be used while assigning shell and membrane sections to faces.',
	),
	'Part.associateMeshWithGeometry':'<value is a self-reference, replaced by this string>',
	'Part.backup':(
		'',
		"This method makes a backup copy of the features in the part. Use the restore method to retrieve the part's features from the backup.",
	),
	'Part.checkGeometry':(
		'<detailed, reportFacetErrors, level>',
		'This method checks the validity of the geometry of the part and prints a count of all topological entities on the part (faces, edges, vertices, etc.).',
	),
	'Part.clashSets':'<value is a self-reference, replaced by this string>',
	'Part.cleanMesh':(
		'mergeTolerance <, growEdges, elements, refEdge, thicknessDir, moveLayers>',
		'This method is used to collapse short element edges and delete collapsed elements, or grow short element edges, on an orphan mesh part composed of linear elements.',
	),
	'Part.clearGeometryCache':(
		'',
		'This method clears the geometry cache. Clearing the geometry cache reduces the amount of memory being used to cache part features.',
	),
	'Part.collapseMeshEdge':(
		'edge, collapseMethod',
		'This method collapses an edge of a quadrilateral or triangular element of an orphan mesh part or part instance.',
	),
	'Part.combineElement':(
		'elements',
		'This method combines two triangular elements of an orphan mesh part or an Abaqus native mesh.',
	),
	'Part.convertSolidMeshToShell':(
		'',
		'This method removes all solid elements from an orphan mesh part and creates triangular or quadrilateral shell elements along their outer faces.',
	),
	'Part.createVirtualTopology':(
		'<regions, mergeShortEdges, shortEdgeThreshold, mergeSmallFaces, smallFaceAreaThreshold, mergeSliverFaces, faceAspectRatioThreshold, mergeSmallAngleFaces, smallFaceCornerAngleThreshold, mergeThinStairFaces, thinStairFaceThreshold, ignoreRedundantEntities, cornerAngleTolerance, applyBlendControls, blendSubtendedAngleTolerance, blendRadiusTolerance>',
		'This method creates a virtual topology feature by automatically merging faces and edges based on a set of geometric parameters. The edges and vertices that are being merged will be ignored during mesh generation.',
	),
	'Part.deleteAllFeatures':(
		'',
		'This method deletes all the features in the part.',
	),
	'Part.deleteBoundaryLayerControls':'<value is a self-reference, replaced by this string>',
	'Part.deleteElement':(
		'elements <, deleteUnreferencedNodes>',
		'This method deletes the given elements from an orphan mesh part or an Abaqus native mesh. If the elements belong to an Abaqus native mesh then the elements must have been generated using the bottom-up meshing technique.',
	),
	'Part.deleteFeatures':(
		'featureNames',
		'This method deletes the given features.',
	),
	'Part.deleteMesh':(
		'regions',
		'This method deletes a subset of the mesh that contains the native elements from the given parts or regions.',
	),
	'Part.deleteMeshAssociationWithGeometry':'<value is a self-reference, replaced by this string>',
	'Part.deleteNode':(
		'nodes <, deleteUnreferencedNodes>',
		'This method deletes the given nodes from an orphan mesh part.',
	),
	'Part.deletePreviewMesh':(
		'',
		'This method deletes all boundary meshes in the parts. See the boundaryPreview argument of generateMesh for information about generating boundary meshes.',
	),
	'Part.deleteSeeds':(
		'regions',
		'This method deletes the global edge seeds from the given parts or deletes the local edge seeds from the given edges.',
	),
	'Part.deleteSets':(
		'setNames',
		'This command deletes the given sets from the part.',
	),
	'Part.deleteSurfaces':(
		'surfaceNames',
		'This command deletes the given surfaces from the part.',
	),
	'Part.editNode':(
		'nodes <, coordinate1, coordinate2, coordinate3, coordinates, offset1, offset2, offset3, localCsys, projectToGeometry>',
		'This method changes the coordinates of the given nodes on an orphan mesh part or on an Abaqus native mesh.',
	),
	'Part.generateBottomUpExtrudedMesh':'<value is a self-reference, replaced by this string>',
	'Part.generateBottomUpRevolvedMesh':'<value is a self-reference, replaced by this string>',
	'Part.generateBottomUpSweptMesh':'<value is a self-reference, replaced by this string>',
	'Part.generateMesh':(
		'regions <, seedConstraintOverride, meshTechniqueOverride, boundaryPreview, boundaryMeshOverride>',
		'This method generates a mesh in the given parts or regions.',
	),
	'Part.generateMeshByOffset':'<value is a self-reference, replaced by this string>',
	'Part.getAngle':'<value is a self-reference, replaced by this string>',
	'Part.getArea':(
		'faces <, relativeAccuracy>',
		'This method returns the total surface area of a given face or group of faces.',
	),
	'Part.getAssociatedCADPaths':(
		'',
		'This method returns the paths to the associated CAD part and root file. These are only available if the part was imported from one of the supported CAD softwares using the Associative Import capability. The root file can be the assembly file or the part file, depending on what which one was imported.',
	),
	'Part.getCADParameters':(
		'',
		'This method returns the names and values of the CAD parameters associated with the part. These are only available if the part was imported from one of the supported CAD softwares using the Associative Import capability, and if the parameter names defined in that CAD software are prefixed with the string ABQ.  ',
	),
	'Part.getCentroid':(
		'faces, cells <, relativeAccuracy>',
		'Depending on the arguments provided, this method returns the following:The location of the centroid of a given face or group of faces.The location of the centroid of a given cell or group of cells.',
	),
	'Part.getCoordinates':(
		'entity',
		'This method returns the coordinates of specified point. ',
	),
	'Part.getCurvature':(
		'edges <, samplePoints>',
		'This method returns the maximum curvature of a given edge or group of edges. For an arc, the curvature is constant over the entire edge, and equal to the inverse of the radius. For a straight line, the curvature is constant and equal to 0. For a spline edge, the curvature varies over a range, and this methods computes the maximum.',
	),
	'Part.getDistance':(
		'entity1, entity2',
		'Depending on the arguments provided, this method returns one of the following:The distance between two points.The minimum distance between a point and an edge.The minimum distance between two edges.',
	),
	'Part.getEdgeSeeds':(
		'edge, attribute',
		'This method returns an edge seed parameter for a specified edge of a part.',
	),
	'Part.getElementType':(
		'region, elemShape',
		'This method returns the ElemType object of a given element shape assigned to a region of a part.',
	),
	'Part.getIncompatibleMeshInterfaces':'<value is a self-reference, replaced by this string>',
	'Part.getLength':(
		'edges',
		'This method returns the length of a given edge or group of edges.',
	),
	'Part.getMassProperties':(
		'<regions, relativeAccuracy, useMesh, specifyDensity, density, specifyThickness, thickness, miAboutCenterOfMass, miAboutPoint>',
		'This method returns the mass properties of a part or region. Only beams, trusses, shells, solids, point, nonstructural mass, and rotary inertia elements are supported.',
	),
	'Part.getMeshControl':(
		'region, attribute',
		'This method returns a mesh control parameter for the specified region of a part.',
	),
	'Part.getMeshStats':(
		'regions',
		'This method returns the mesh statistics for the given regions.',
	),
	'Part.getPartSeeds':(
		'attribute',
		'This method returns a part seed parameter for the part.',
	),
	'Part.getPerimeter':(
		'faces',
		'This method returns the total perimeter of a given face or group of faces. All faces need to be on the same part. If the specified faces have shared edges, these edges are excluded from the computation,  thus providing the length of the outer perimeter of the specified faces.',
	),
	'Part.getUnmeshedRegions':(
		'',
		'This method returns all geometric regions in the part that require a mesh for submitting an analysis but are either unmeshed or are meshed incompletely.',
	),
	'Part.getVolume':(
		'cells <, relativeAccuracy>',
		'This method returns the volume area of a given cell or group of cells.',
	),
	'Part.ignoreEntity':'<value is a self-reference, replaced by this string>',
	'Part.isAlignedWithSketch':(
		'',
		'This method checks if the normal of an analytical rigid surface part is aligned with that of its sketch.',
	),
	'Part.mergeElement':(
		'edge, elements',
		'Merge a selection of elements arranged in layers on an orphan mesh part into a single layer.',
	),
	'Part.mergeNodes':(
		'node1, node2 <, removeDuplicateElements, keepHighLabels>',
		'Merge two nodes of an orphan mesh part or an Abaqus native mesh. If the nodes belong to an Abaqus native mesh then at least one of the two nodes must have been generated using the bottom-up meshing technique.',
	),
	'Part.orientElements':(
		'pickedElements, referenceRegion',
		'This method orients the stack direction of elements in a continuum shell or gasket mesh.',
	),
	'Part.printAssignedSections':(
		'',
		'This method prints information on each section that has been assigned to a region of the part.',
	),
	'Part.projectEdgesOntoSketch':(
		'sketch, edges <, constrainToBackground>',
		'This method projects the selected edges of a part onto the specified ConstrainedSketch object. The edges appear as sketch geometry after projection. If the plane of projection is not parallel to the specified edge, the resultant sketch geometry may be of a different type. For example, a circular edge can be projected as an ellipse or a line depending on the angle of the plane of projection. By default, the projected edge will be constrained to the background geometry. You can remove this constraint by setting constrainToBackground to False.',
	),
	'Part.projectNode':(
		'nodes, projectionReference',
		'This method projects the given nodes onto a mesh entity, geometric entity, or a datum object. The nodes may belong to an orphan mesh part or to an Abaqus native mesh.',
	),
	'Part.projectReferencesOntoSketch':(
		'sketch <, filter, upToFeature, edges, vertices>',
		'This method projects the vertices of specified edges, and datum points from the part onto the specified ConstrainedSketch object. The vertices and datum points appear on the sketch as reference geometry. ',
	),
	'Part.queryAttributes':(
		'<printResults>',
		'This method prints the following information about a part:the name, modeling space, and analysis type; andwhether twist is included (only available when the modeling space is axisymmetric and the analysis type is deformable); andthe number of vertices, edges, faces and cells if applicable.',
	),
	'Part.queryCachedStates':(
		'',
		'This method displays the position of geometric states relative to the sequence of features in the part cache. The output is displayed in the message area.',
	),
	'Part.queryDisjointPlyRegions':(
		'',
		'This method provides a list of all composite plys in the current part which have disjoint regions.',
	),
	'Part.queryGeometry':(
		'<relativeAccuracy, printResults>',
		"This method prints the following information about a part:the name, modeling space, and analysis type;whether twist is included (only available when the modeling space is axisymmetric and the analysis type is deformable);a 3D point representing the minimum of the part's bounding box;a 3D point representing the maximum of the part's bounding box;a 3D point representing the part's centroid (only on 3D solid parts); andthe volume (only on 3D solid parts).",
	),
	'Part.queryRegionsMissingSections':(
		'',
		'This method returns all regions in the part that do not have a section assignment but require one for analysis.',
	),
	'Part.redoMeshEdit':(
		'',
		'This method executes the edit mesh or the bottom-up meshing operation most recently undone by the undoMeshEdit method on an part. A redo action must be currently available for the part.  This implies that the user must have executed the undoMeshEdit method on the part and that the user has not subsequently executed any further edit mesh commands on the assembly. It also implies that the user provided a sufficient cache allowance to store the undo operation. ',
	),
	'Part.regenerate':(
		'',
		'This method regenerates a part. When you modify features, it may be convenient to postpone regeneration until you make all your changes, since regeneration can be time consuming.',
	),
	'Part.regenerationWarnings':'<value is a self-reference, replaced by this string>',
	'Part.removeElementSize':(
		'',
		'This method removes the global element size from an orphan mesh part.',
	),
	'Part.removeInvalidGeometry':(
		'',
		'Removes all invalid entities from the part, leaving a valid part. This is not recorded as a feature in the feature list, therefore it should be used on parts that have a single feature (such as an imported part).This may remove valid entities that are connected to invalid ones. You can identify invalid entities using the query toolset before using this command.',
	),
	'Part.renumberElement':(
		'<elements, startLabel, increment, offset, labels>',
		'This method assigns new labels to orphan mesh elements.',
	),
	'Part.renumberNode':(
		'<nodes, startLabel, increment, offset, labels>',
		'This method assigns new labels to orphan mesh nodes.',
	),
	'Part.restore':'<value is a self-reference, replaced by this string>',
	'Part.restoreIgnoredEntity':'<value is a self-reference, replaced by this string>',
	'Part.resumeAllFeatures':(
		'',
		'This method resumes all the suppressed features in the part.',
	),
	'Part.resumeFeatures':(
		'featureNames',
		'This method resumes the specified suppressed features in the part.',
	),
	'Part.resumeLastSetFeatures':(
		'',
		'This method resumes the last set of features to be suppressed in the part.',
	),
	'Part.saveGeometryCache':(
		'',
		'This method caches the current geometry. Caching the current geometry improves regeneration performance.',
	),
	'Part.seedEdgeByBias':'<value is a self-reference, replaced by this string>',
	'Part.seedEdgeByNumber':'<value is a self-reference, replaced by this string>',
	'Part.seedEdgeBySize':'<value is a self-reference, replaced by this string>',
	'Part.seedPart':(
		'regions, size <, deviationFactor, minSizeFactor, constraint>',
		'This method assigns global edge seeds to the given parts.',
	),
	'Part.setAssociatedCADPaths':(
		'<partFile, rootFile>',
		'This method sets the paths to the associated CAD part and root file. This method is only available if the part was imported from one of the supported CAD softwares using the Associative Import capability. The root file can be the assembly file or the part file, depending on the one that was imported. This method can be used to specify the new paths when the CAD data is moved to a different directory.',
	),
	'Part.setBoundaryLayerControls':'<value is a self-reference, replaced by this string>',
	'Part.setElementSize':(
		'size',
		'This method sets the global element size for an orphan mesh part.',
	),
	'Part.setElementType':'<value is a self-reference, replaced by this string>',
	'Part.setLogicalCorners':'<value is a self-reference, replaced by this string>',
	'Part.setMeshControls':'<value is a self-reference, replaced by this string>',
	'Part.setSweepPath':'<value is a self-reference, replaced by this string>',
	'Part.setValues':(
		'<geometryRefinement, startNodeLabel, startElemLabel>',
		'This method modifies the Part object.',
	),
	'Part.splitElement':(
		'elements',
		'This method splits quadrilateral elements of an orphan mesh part or a Abaqus native mesh into triangular elements.',
	),
	'Part.splitMeshEdge':(
		'edge <, parameter>',
		'This method splits an edge of a quadrilateral or triangular element of an orphan mesh part or an Abaqus native mesh.',
	),
	'Part.subdivideElement':(
		'<elements, divisionNumber, face, edge>',
		'Subdivide a selection of elements on an orphan mesh part in one or more directions.',
	),
	'Part.suppressFeatures':(
		'featureNames',
		'This method suppresses the given features.',
	),
	'Part.swapMeshEdge':(
		'edge',
		'This method swaps the diagonal of two adjacent triangular elements of an orphan mesh part or an Abaqus native mesh.',
	),
	'Part.undoMeshEdit':(
		'',
		'This method undoes the most recent edit mesh or the bottom-up meshing operation on a part and restores the mesh to its previous state. An edit mesh undo action must be available for the part. This implies that prior to executing an edit mesh command on the part, the user enabled edit mesh undo with a sufficient cache allowance to store the edit mesh operation.',
	),
	'Part.verifyMeshQuality':(
		'criterion <, threshold, elemShape, regions>',
		'This method tests the mesh quality of a part and returns poor-quality elements.',
	),
	'Part.wrapMesh':(
		'radius',
		'This method wraps a planar orphan mesh part about the Z-axis.',
	),
	'Part.writeAcisFile':(
		'fileName <, version>',
		'This method exports the geometry of the part to a named file in ACIS format.',
	),
	'Part.writeCADParameters':'<value is a self-reference, replaced by this string>',
	'Part.writeHealedPart':(
		'fileName',
		'This function exports the geometry of the part to a named file in ACIS format.',
	),
	'Part.writeIgesFile':(
		'fileName, flavor',
		'This method exports the geometry of the part to a named file in IGES format.',
	),
	'Part.writeStepFile':(
		'fileName',
		'This method exports the geometry of the part to a named file in STEP format.',
	),
	'Part.writeVdaFile':(
		'fileName',
		'This method exports the geometry of the part to a named file in VDA-FS format.',
	),
	'PartDisplayOptions.setValues':(
		'<renderStyle, visibleDisplayGroups, engineeringFeatures, renderBeamProfiles, beamScaleFactor>',
		'This method modifies the PartDisplayOptions object.',
	),
	'PartInstance.Contact':(
		'movableList, fixedList, direction, clearance <, isFaceEdges>',
		'This method translates an instance along the specified direction until it is in contact with a fixed instance.',
	),
	'PartInstance.ConvertConstraints':(
		'',
		'This method converts the position constraints of an instance to absolute positions. The method deletes the constraint features on the instance but preserves the position in space.',
	),
	'PartInstance.InterestingPoint':'<value is a self-reference, replaced by this string>',
	'PartInstance.checkGeometry':(
		'<detailed, level>',
		'This method checks the validity of the geometry of the part instance and prints a count of all topological entities on the part instance (faces, edges, vertices, etc.).',
	),
	'PartInstance.getPosition':(
		'',
		'This method prints the sum of the translations and rotations applied to the PartInstance object.',
	),
	'PartInstance.getRotation':(
		'',
		'This method returns a tuple including the point of rotation, axis of rotation, and rotation angle (in degrees).',
	),
	'PartInstance.getTranslation':(
		'',
		'This method returns a tuple of three Floats representing translation in the X-, Y-, and Z-directions.',
	),
	'PartInstance.replace':(
		'instanceOf <, applyConstraints>',
		'This method replaces one instance with an instance of another part.',
	),
	'PartInstance.rotateAboutAxis':(
		'axisPoint, axisDirection, angle',
		'This method translates an instance by the specified amount.',
	),
	'PartInstance.translate':(
		'vector',
		'This method translates an instance by the specified amount.',
	),
	'PartInstance.translateTo':(
		'movableList, fixedList, direction, clearance <, vector>',
		'This method translates an instance along the specified direction until it is in contact with a fixed instance.',
	),
	'PenetrationCheck.setValues':'<value is a self-reference, replaced by this string>',
	'PeriodicAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'Permeability.SaturationDependence':(
		'table',
		'This method creates a SaturationDependence object.',
	),
	'Permeability.VelocityDependence':(
		'table',
		'This method creates a VelocityDependence object.',
	),
	'Permeability.setValues':'<value is a self-reference, replaced by this string>',
	'Piezoelectric.setValues':'<value is a self-reference, replaced by this string>',
	'PipePressure.setValues':'<value is a self-reference, replaced by this string>',
	'PipePressure.setValuesInStep':(
		'stepName <, magnitude, hZero, hReference, amplitude>',
		'This method modifies the propagating data for an existing PipePressure object in the specified step.',
	),
	'PipeProfile.setValues':'<value is a self-reference, replaced by this string>',
	'PlanarTestData.setValues':'<value is a self-reference, replaced by this string>',
	'Plastic.AnnealTemperature':(
		'table <, dependencies>',
		'This method creates an AnnealTemperature object.',
	),
	'Plastic.CycledPlastic':(
		'table <, temperatureDependency>',
		'This method creates a CycledPlastic object.',
	),
	'Plastic.CyclicHardening':(
		'table <, temperatureDependency, dependencies, parameters>',
		'This method creates a CyclicHardening object.',
	),
	'Plastic.Ornl':'<value is a self-reference, replaced by this string>',
	'Plastic.Potential':'<value is a self-reference, replaced by this string>',
	'Plastic.RateDependent':'<value is a self-reference, replaced by this string>',
	'Plastic.setValues':'<value is a self-reference, replaced by this string>',
	'PlyStackPlotOptions.setValues':(
		'<renderStyle, showEdges, edgeStyle, edgeThickness, plyDisplay, startLayer, numLayers, evenNumPlyColor, oddNumPlyColor, showFibers, fiberColor, fiberStyle, fiberThickness, fiberSpacing, showReferencePlane, referenceSurfaceColor, translucency, translucencyFactor, translucencySort, showReferenceOutline, referenceOutlineColor, referenceOutlineStyle, referenceOutlineThickness, allLabelsFont, showMaterialNames, materialNamesColor, showOrientationNames, orientationNamesColor, showStateBlock, stateBlockColor, showPlyNames, plyNamesColor, showThicknessLabels, thicknessLabelsColor, showIntPoints, intPointsColor, sizeX, sizeY, sizeZ>',
		'This method modifies the PlyStackPlotOptions object.',
	),
	'PngOptions.setValues':(
		'<imageSize>',
		'This method modifies the \n PngOptions\n object.\n ',
	),
	'PointFastener.setValues':'<value is a self-reference, replaced by this string>',
	'PointMassInertia.setValues':'<value is a self-reference, replaced by this string>',
	'PorDragBodyForce.setValues':'<value is a self-reference, replaced by this string>',
	'PorDragBodyForce.setValuesInStep':(
		'stepName <, magnitude>',
		'This method modifies the propagating data for an existing PorDragBodyForce object in the specified step.',
	),
	'PoreFluidExpansion.setValues':'<value is a self-reference, replaced by this string>',
	'PorePressure.setValues':'<value is a self-reference, replaced by this string>',
	'PorePressureBC.setValues':'<value is a self-reference, replaced by this string>',
	'PorePressureBC.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing PorePressureBC object in the specified step.',
	),
	'PorousBulkModuli.setValues':'<value is a self-reference, replaced by this string>',
	'PorousElastic.setValues':'<value is a self-reference, replaced by this string>',
	'PorousFailureCriteria.setValues':'<value is a self-reference, replaced by this string>',
	'PorousMetalPlasticity.PorousFailureCriteria':(
		'<fraction, criticalFraction>',
		'This method creates a PorousFailureCriteria object.',
	),
	'PorousMetalPlasticity.VoidNucleation':(
		'table <, temperatureDependency, dependencies>',
		'This method creates a VoidNucleation object.',
	),
	'PorousMetalPlasticity.setValues':'<value is a self-reference, replaced by this string>',
	'Potential.setValues':'<value is a self-reference, replaced by this string>',
	'PredefinedField.delete':(
		'indices',
		' This method allows you to delete existing fields.\n      ',
	),
	'PredefinedField.move':(
		'fromStepName, toStepName',
		'This method moves a specific PredefinedFieldState object from one step to a different step.',
	),
	'PredefinedField.resume':(
		'',
		'This method resumes the predefined field that was previously suppressed.',
	),
	'PredefinedField.suppress':(
		'',
		'This method suppresses the predefined field.',
	),
	'PredefinedFieldDisplayOptions.setValues':(
		'<temperatureField, velocityField, generalField, stressField, hardeningField>',
		'This method modifies the PredefinedFieldDisplayOptions object.',
	),
	'Pressure.setValues':'<value is a self-reference, replaced by this string>',
	'Pressure.setValuesInStep':(
		'stepName <, magnitude, hZero, hReference, amplitude>',
		'This method modifies the propagating data for an existing Pressure object in the specified step.',
	),
	'PressureEffect.setValues':'<value is a self-reference, replaced by this string>',
	'PressurePenetration.setValues':'<value is a self-reference, replaced by this string>',
	'PressurePenetration.setValuesInStep':(
		'stepName <, penetrationPressure, criticalPressure, amplitude, penetrationTime>',
		'This method modifies the propagating data for an existing PressurePenetration object in the specified step.',
	),
	'PressureStress.move':(
		'fromStepName, toStepName',
		'This method moves the PressureStressState object from one step to a different step.',
	),
	'PressureStress.setValues':'<value is a self-reference, replaced by this string>',
	'PressureStress.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data for an existing PressureStress object in the specified step.',
	),
	'PrintOptions.setValues':(
		'<rendition, vpDecorations, vpBackground, compass, printCommand, deleteTemporaryFiles, reduceColors>',
		'This method modifies the \n PrintOptions\n object.\n ',
	),
	'ProbeOptions.setValues':(
		'<options, probeEntity, probeOutputPosition, partInstance, elementID, elementType, elementConnectivity, elementFieldResults, nodeId, baseCoordinates, deformedCoordinates, attachedElements, nodeFieldResults, legend, xValue, yValue, sequenceID, interpolateXy>',
		'This method modifies the settings on the ProbeOptions object.',
	),
	'ProbeReport.setValues':(
		'<options, numColumns, numDigits, numFormat, pageWidth, printTotal, printMinMax>',
		'This method modifies the ProbeReport object.',
	),
	'PsOptions.setValues':(
		'<paperSize, topMargin, bottomMargin, leftMargin, rightMargin, orientation, logo, date, resolution, fontType, imageFormat, shadingQuality>',
		'This method modifies the \n PsOptions\n object.\n ',
	),
	'PsdDefinition.setValues':'<value is a self-reference, replaced by this string>',
	'QuantityType.setValues':(
		'<type, label>',
		'This method modifies the QuantityType object.',
	),
	'QuickTimeOptions.setValues':(
		'<compressionMethod, sizeDefinition, imageSize>',
		'This method modifies the QuickTimeOptions object.',
	),
	'Radiation.setValues':'<value is a self-reference, replaced by this string>',
	'RadiationToAmbient.setValues':'<value is a self-reference, replaced by this string>',
	'RadiationToAmbient.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data of an existing RadiationToAmbient object in the specified step.',
	),
	'RandomResponseStep.setValues':'<value is a self-reference, replaced by this string>',
	'RateDependent.setValues':'<value is a self-reference, replaced by this string>',
	'Ratios.setValues':'<value is a self-reference, replaced by this string>',
	'RebarLayers.setValues':'<value is a self-reference, replaced by this string>',
	'RectangularProfile.setValues':'<value is a self-reference, replaced by this string>',
	'ReferencePressure.setValues':'<value is a self-reference, replaced by this string>',
	'ReferencePressure.setValuesInStep':(
		'stepName <, magnitude>',
		'This method modifies the propagating data for an existing ReferencePressure object in the specified step.',
	),
	'RegionPairs.setValuesInStep':(
		'stepName <, useAllstar, addPairs, removePairs>',
		'This method allows addition and removal of domain pairs in a given step.',
	),
	'RegisteredDictionary.Methods':(
		'',
		'The RegisteredDictionary object supports the same methods as a Python dictionary. In addition, the RegisteredDictionary object supports the \n changeKey \n method.\n ',
	),
	'RegisteredDictionary.changeKey':(
		'fromName, toName',
		'This method changes the name of a key in the dictionary.',
	),
	'RegisteredList.Methods':(
		'',
		'The RegisteredList object supports the same methods as a standard Python list object.',
	),
	'RegisteredTuple.Methods':(
		'',
		'The RegisteredTuple object supports the same methods as a standard Python list object.',
	),
	'Regularization.setValues':'<value is a self-reference, replaced by this string>',
	'RelativeDensity.setValues':'<value is a self-reference, replaced by this string>',
	'RemeshingRule.resume':(
		'',
		'This method resumes the remeshing rule that was previously suppressed.',
	),
	'RemeshingRule.setValues':'<value is a self-reference, replaced by this string>',
	'RemeshingRule.suppress':(
		'',
		'This method suppresses the remeshing rule. Abaqus will not remesh regions where the rules are suppressed.',
	),
	'RepositorySupport.Repository':(
		'name, constructors',
		'This method installs a repository on the class. The repository is an instance of a \n RegisteredDictionary \n class. Refer to \n RegisteredDictionary \n for details on its methods.\n The objects stored in the repository are assumed to have an attribute called \n name \n that stores the key used to access the object in the repository. The name attribute will be modified by the \n changeKey \n method.\n ',
	),
	'ResponseSpectrumStep.setValues':'<value is a self-reference, replaced by this string>',
	'Restart.setValues':'<value is a self-reference, replaced by this string>',
	'RetainedNodalDofsBC.setValues':'<value is a self-reference, replaced by this string>',
	'RetainedNodalDofsBC.setValuesInStep':(
		'stepName <, u1, u2, u3, ur1, ur2, ur3>',
		'This method modifies the propagating data for an existing RetainedNodalDofsBC object in the specified step.',
	),
	'RigidBody.setValues':'<value is a self-reference, replaced by this string>',
	'RotationalBodyForce.setValues':'<value is a self-reference, replaced by this string>',
	'RotationalBodyForce.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing RotationalBodyForce object in the specified step.',
	),
	'RuleResult.ErrorIndicatorResult':(
		'name, results',
		'This method creates an ErrorIndicatorResult with data for an error indicator variable in a RemeshingRule for a given adaptivity iteration.',
	),
	'SDV.setValues':'<value is a self-reference, replaced by this string>',
	'Saturation.setValues':'<value is a self-reference, replaced by this string>',
	'SaturationDependence.setValues':'<value is a self-reference, replaced by this string>',
	'SecondaryBaseBC.setValues':'<value is a self-reference, replaced by this string>',
	'SecondaryBaseBC.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data for an existing SecondaryBaseBC object in the specified step.',
	),
	'SectionAssignment.resume':(
		'',
		'This method resumes the section assignment that was previously suppressed.',
	),
	'SectionAssignment.setValues':'<value is a self-reference, replaced by this string>',
	'SectionAssignment.suppress':(
		'',
		'This method suppresses the section assignment.',
	),
	'SectionCategory.SectionPoint':(
		'number, description',
		'This method creates a SectionPoint object.',
	),
	'SelfContactExp.setValues':'<value is a self-reference, replaced by this string>',
	'SelfContactExp.setValuesInStep':(
		'stepName <, interactionProperty, contactControls>',
		'This method modifies the propagating data for an existing SelfContactExp object in the specified step.',
	),
	'SelfContactStd.setValues':'<value is a self-reference, replaced by this string>',
	'SelfContactStd.setValuesInStep':(
		'stepName <, interactionProperty, contactControls>',
		'This method modifies the propagating data of an existing SelfContactStd object in the specified step.',
	),
	'Session.AreaStyle':(
		'<color, fill, style>',
		'This method creates an AreaStyle.',
	),
	'Session.Curve':(
		'name, data',
		'This method creates an XYCurve object from an XYData object.',
	),
	'Session.DisplayGroup':(
		'name, leaf',
		'This method creates a DisplayGroup object.',
	),
	'Session.Drawing':(
		'name',
		'This method creates an empty \n Drawing\n object.\n ',
	),
	'Session.FreeBodyFromEdges':(
		'name, edges <, summationLoc, summationPoint, componentResolution, csysName>',
		'This method creates a FreeBody object and places it in the freeBodies repository.',
	),
	'Session.FreeBodyFromFaces':(
		'name, faces <, summationLoc, summationPoint, componentResolution, csysName>',
		'This method creates a FreeBody object and places it in the freeBodies repository.',
	),
	'Session.FreeBodyFromNodesElements':(
		'name, elements, nodes <, summationLoc, summationPoint, componentResolution, csysName>',
		'This method creates a FreeBody object and places it in the freeBodies repository.',
	),
	'Session.Image':(
		'name, fileName',
		'This method creates an \n Image\n object from the contents of the specified file.\n ',
	),
	'Session.ImageAnimation':(
		'fileName, format',
		'This method creates an ImageAnimation object from the specified filename and format.',
	),
	'Session.LineStyle':(
		'<color, show, style, thickness>',
		'This method creates a LineStyle.',
	),
	'Session.Movie':(
		'name, fileName <, startFrame, endFrame, timelineStartFrame, timelineEndFrame, timelineStartTime, timelineEndTime>',
		'This method creates a Movie object from the contents of the specified file.',
	),
	'Session.NetworkDatabaseConnector':(
		'name, hostName, directory <, remoteAbaqusDriverName, remoteLoginMechanism, sshPath, serverPort, connectionPort, serverTimeout, allowAutomaticStartup>',
		'This method creates a \n NetworkDatabaseConnector\n object that you can use to access a remote output database. You can create a network database connector from any platform: Windows, UNIX, or Linux. However, the network database connector server must reside on a UNIX or Linux platform; you cannot access an output database that resides on a remote Windows system. You can access only a remote output database; you cannot access a remote model database.\n ',
	),
	'Session.Odb':(
		'name <, analysisTitle, description, path>',
		'This method creates a new \n Odb\n object.\n ',
	),
	'Session.Path':(
		'name, type, expression, circleDefinition, numSegments, startAngle, endAngle, radius, radialAngle, startRadius, endRadius',
		'This method creates a Path object.',
	),
	'Session.QuantityType':(
		'type <, label>',
		'This method creates a QuantityType object.',
	),
	'Session.Queue':(
		'name, queueName <, hostName, fileCopy, directory, driver, localPlatform, remotePlatform, filesToCopy, description>',
		'This method creates a Queue object. Remote queues are available only on UNIX platforms.',
	),
	'Session.ScratchOdb':(
		'odb',
		'This method creates a new ScratchOdb object.',
	),
	'Session.Spectrum':(
		'name, colors',
		'This method creates a Spectrum object and places it in the spectrums repository.',
	),
	'Session.Stream':(
		'name, numPointsOnRake <, pointA, pointB, path>',
		'This method creates a\n Stream\n object and places it in the streams repository.\n ',
	),
	'Session.SymbolStyle':(
		'<color, show, marker, size>',
		'This method creates a SymbolStyle object.',
	),
	'Session.TextStyle':(
		'<color, show, font, rotationAngle>',
		'This method creates a TextStyle.',
	),
	'Session.View':(
		'name, fieldOfViewAngle, nearPlane, farPlaneMode, farPlane, width, height, projection, cameraPosition, cameraUpVector, cameraTarget, viewOffsetX, viewOffsetY, autoFit <, movieMode>',
		'This method creates a \n View\n object.\n All dimensions and coordinates are specified in the model coordinate system.This method cannot be used to create a \n    View\n    for a \n    Layer\n    object.\n    ',
	),
	'Session.Viewport':(
		'name <, origin, width, height, border, titleBar, titleStyle, customTitleString>',
		'This method creates a \n Viewport\n object with the specified origin and dimensions.\n ',
	),
	'Session.XYData':(
		'objectToCopy',
		'This method creates an XYData object by copying an existing XYData object.',
	),
	'Session.XYDataFromFile':(
		'fileName <, name, sourceDescription, contentDescription, positionDescription, legendLabel, xValuesLabel, yValuesLabel, axis1QuantityType, axis2QuantityType, xField, yField, skipFrequency>',
		'This method creates an XYData object from data in an ASCII file.',
	),
	'Session.XYDataFromFreeBody':(
		'odb, force, moment, resultant, comp1, comp2, comp3',
		'This method creates a list of XYData objects by compputing free body data from an Odb object.',
	),
	'Session.XYDataFromHistory':(
		'odb, outputVariableName, steps <, name, sourceDescription, contentDescription, positionDescription, legendLabel, skipFrequency, numericForm, complexAngle, stepTuple>',
		'This method creates an XYData object by reading history data from an Odb object.',
	),
	'Session.XYDataFromPath':(
		'path, includeIntersections, shape, pathStyle, numIntervals, labelType <, name, viewport, step, frame, variable, deformedMag, numericForm, complexAngle>',
		'This method creates an XYData object from path information.',
	),
	'Session.XYPlot':(
		'name',
		'This method creates an empty XYPlot object.',
	),
	'Session.disableCADConnection':(
		'CADName',
		'This method disables an associative import CAD connection that was enabled.',
	),
	'Session.disableParameterUpdate':(
		'CADName',
		'This method disables an associative CAD connection using parameters.',
	),
	'Session.enableCADConnection':(
		'CADName <, portNum>',
		'This method enables an associative import CAD connection for the specified \n CADName.\n ',
	),
	'Session.enableParameterUpdate':(
		'CADName, CADVersion <, CADPort>',
		'This method enables an associative import CAD connection with parameters for the specified \n CADName.\n ',
	),
	'Session.getPathTolerance':(
		'',
		'This method is used to get the \n tolerance \n used when creating \n XYData \n objects by extracting results along \n Path \n objects.\n ',
	),
	'Session.linearizeStress':(
		'name, path, startPoint, endPoint, modelShape, components, xyMembraneComps, xyBendingComps <, invariantBendingComps, intervals, radiusOfCurvature, oopRadiusOfCurvature, curvatureCorrection, curvatureCsys, useCurvatureCsysForOrient, saveXy, writeReport, reportFile, appendToFile, saveToPath>',
		'This method is used to perform stress linearization along a defined stress line.',
	),
	'Session.printToFile':(
		'fileName <, format, canvasObjects, compression>',
		'This method prints canvas objects to a file using the attributes stored in the \n PrintOptions \n object and the appropriate format options object.\n ',
	),
	'Session.printToPrinter':(
		'<printCommand, numCopies, canvasObjects>',
		'This method prints canvas objects to a Windows printer or to a PostScript printer. The attributes used for printing to a Windows printer are stored in the \n PrintOptions \n object and the \n PageSetupOptions \n object; the attributes used for printing to a PostScript printer are stored in the \n PrintOptions \n object and the \n PsOptions \n object.\n ',
	),
	'Session.saveOptions':(
		'directory',
		'This method saves your customized display settings.',
	),
	'Session.setCADPortNumber':(
		'CADName, Port',
		'For the given CAD system, this method saves the port number in Abaqus/CAE. This port number is used to send the parameter information to the CAD system.',
	),
	'Session.setPathTolerance':(
		'<tolerance>',
		'This method is used to set the \n tolerance \n to be used when creating \n XYData \n objects by extracting results along \n Path \n objects. This command should be exercised with caution since setting a value too low or too high may result in getting no results or unpredictable results.\n ',
	),
	'Session.setValues':(
		'<kernelMemoryLimit>',
		'This method modifies the \n Session \n object.\n ',
	),
	'Session.updateCADParameters':(
		'modelName, CADName, parameterFile <, CADPartName, CADPartFile>',
		'This method updates the parameters for the specified model using the specified parameter file.',
	),
	'Session.write3DXMLFile':(
		'fileName <, format, canvasObjects>',
		'This method exports the current viewport objects to a file.',
	),
	'Session.writeImageAnimation':(
		'fileName, format <, canvasObjects>',
		'This method writes the animations present in the list of canvas objects to a file. It generates an animation file using the given file name and file format and uses the values in the appropriate options object.',
	),
	'Session.writeOBJFile':(
		'fileName <, canvasObjects>',
		'This method exports the current viewport objects to a file.',
	),
	'Session.writeVrmlFile':'<value is a self-reference, replaced by this string>',
	'Session.xyDataListFromField':(
		'odb, outputPosition, variable <, elementSets, elementLabels, nodeSets, nodeLabels, numericForm, complexAngle>',
		'This method creates a list of XYData objects by reading field data from an Odb object.',
	),
	'ShapeDemoldControl.setValues':'<value is a self-reference, replaced by this string>',
	'ShapeMemberSize.setValues':'<value is a self-reference, replaced by this string>',
	'ShapePlanarSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'ShapePointSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'ShapeRotationalSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'ShapeTask.setValues':'<value is a self-reference, replaced by this string>',
	'Shear.setValues':'<value is a self-reference, replaced by this string>',
	'ShearRetention.setValues':'<value is a self-reference, replaced by this string>',
	'ShearTestData.setValues':'<value is a self-reference, replaced by this string>',
	'ShellEdgeLoad.setValues':'<value is a self-reference, replaced by this string>',
	'ShellEdgeLoad.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing ShellEdgeLoad object in the specified step.',
	),
	'ShellSection.TransverseShearShell':(
		'k11, k22, k12',
		'This method creates a TransverseShearShell object.',
	),
	'ShellSolidCoupling.setValues':'<value is a self-reference, replaced by this string>',
	'SimpleShearTestData.setValues':'<value is a self-reference, replaced by this string>',
	'SingleTermDesignResponse.setValues':'<value is a self-reference, replaced by this string>',
	'SlideRegionControl.setValues':'<value is a self-reference, replaced by this string>',
	'SmoothStepAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'SmoothingAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of surface smoothing assignments to new surfaces in a given step.',
	),
	'SmoothingAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of surface smoothing assignments already defined on surfaces in a given step.',
	),
	'SmoothingAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing surface smoothing assignments from ContactExp and ContactStd objects.',
	),
	'SoilsStep.setValues':'<value is a self-reference, replaced by this string>',
	'Solubility.setValues':'<value is a self-reference, replaced by this string>',
	'SolutionDependentAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'SolverControl.setValues':(
		'<allowPropagation, resetDefaultValues, relativeTolerance, maxIterations, fillInLevel>',
		'This method modifies the SolverControl object.',
	),
	'SoretEffect.setValues':'<value is a self-reference, replaced by this string>',
	'Sorption.setValues':'<value is a self-reference, replaced by this string>',
	'SpecificHeat.setValues':'<value is a self-reference, replaced by this string>',
	'SpectrumAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'SpringDashpot.resume':(
		'',
		'This method resumes the spring/dashpot that was previously suppressed.',
	),
	'SpringDashpot.suppress':(
		'',
		'This method suppresses the spring/dashpot.',
	),
	'SpringDashpotToGround.setValues':'<value is a self-reference, replaced by this string>',
	'SpudPreload.setValues':'<value is a self-reference, replaced by this string>',
	'StabilizationAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of contact stabilization assignments to new domain pairs in a given step.',
	),
	'StabilizationAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of contact stabilization assignments to domain pairs already defined in a given step.',
	),
	'StabilizationAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing contact stabilization assignments from a ContactStd object.',
	),
	'StampControl.setValues':'<value is a self-reference, replaced by this string>',
	'StaticLinearPerturbationStep.setValues':'<value is a self-reference, replaced by this string>',
	'StaticRiksStep.setValues':'<value is a self-reference, replaced by this string>',
	'StaticStep.setValues':'<value is a self-reference, replaced by this string>',
	'StdContactControl.setValues':'<value is a self-reference, replaced by this string>',
	'StdInitialization.setValues':'<value is a self-reference, replaced by this string>',
	'StdStabilization.setValues':'<value is a self-reference, replaced by this string>',
	'StdXplCosimulation.setValues':'<value is a self-reference, replaced by this string>',
	'SteadyStateDirectStep.setValues':'<value is a self-reference, replaced by this string>',
	'SteadyStateModalStep.setValues':'<value is a self-reference, replaced by this string>',
	'SteadyStateSubspaceStep.setValues':'<value is a self-reference, replaced by this string>',
	'Step.AdaptiveMeshDomain':(
		'region <, controls, frequency, initialMeshSweeps, meshSweeps>',
		'This method creates an AdaptiveMeshDomain object.',
	),
	'Step.DiagnosticPrint':(
		'<allke, criticalElement, dmass, etotal, contact, modelChange, plasticity, residual, frequency, solve, mass>',
		'This method creates a DiagnosticPrint object.',
	),
	'Step.LoadCase':(
		'name <, boundaryConditions, predefinedFields, loads, includeActiveBaseStateBC>',
		'This method creates a load case in a step.',
	),
	'Step.Monitor':(
		'node, dof, frequency',
		'This method creates a request for a degree of freedom to be monitored in a general or modal procedure.',
	),
	'Step.Restart':(
		'<numberIntervals, timeMarks, overlay, frequency>',
		'This method creates a restart request.',
	),
	'Step.resume':(
		'',
		'This method resumes the step that was previously suppressed.',
	),
	'Step.suppress':(
		'',
		'This method suppresses the step.',
	),
	'StopConditionDisplayOptions.setValues':(
		'<localStopCondition>',
		'This method modifies the StopConditionDisplayOptions object.',
	),
	'StreamOptions.setValues':(
		'<colorMethod, uniformColor, lineThickness, showArrow, numArrows>',
		'This method modifies the StreamOptions object.',
	),
	'Stress.setValues':'<value is a self-reference, replaced by this string>',
	'SubmodelBC.setValues':'<value is a self-reference, replaced by this string>',
	'SubmodelBC.setValuesInStep':(
		'stepName <, fixed, dof, globalStep, globalIncrement, centerZoneSize>',
		'This method modifies the propagating data for an existing SubmodelBC object in the specified step.',
	),
	'SubmodelSB.setValues':'<value is a self-reference, replaced by this string>',
	'SubmodelSB.setValuesInStep':(
		'stepName <, fixed, globalStep, globalIncrement>',
		'This method modifies the propagating data for an existing SubmodelSB object in the specified step.',
	),
	'SubspaceDynamicsStep.setValues':'<value is a self-reference, replaced by this string>',
	'SubstructureGenerateStep.setValues':'<value is a self-reference, replaced by this string>',
	'SubstructureLoad.setValues':'<value is a self-reference, replaced by this string>',
	'SubstructureLoad.setValuesInStep':(
		'stepName <, loadCaseNames, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SubstructureLoad object in the specified step.',
	),
	'SuperimposeOptions.setValues':(
		'<options, renderStyle, visibleEdges, edgeColorWireHide, edgeColorFillShade, edgeLineStyle, edgeLineThickness, colorCodeOverride, fillColor, labelFont, elemLabels, elemLabelColor, faceLabels, faceLabelColor, nodeLabels, nodeLabelColor, nodeSymbols, nodeSymbolType, nodeSymbolColor, nodeSymbolSize, elementShrink, elementShrinkFactor, coordinateScale, coordinateScaleFactors, normals, normalDisplay, faceNormalColor, beamN1Color, beamN2Color, beamTangentColor, normalArrowLength, normalLineThickness, normalArrowheadStyle, translucency, translucencyFactor, deformedOffsetMode, uniformOffset, nonuniformOffset>',
		'This method modifies the SuperimposeOptions object.',
	),
	'SurfaceCharge.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceCharge.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SurfaceCharge object in the specified step.',
	),
	'SurfaceConcentrationFlux.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceConcentrationFlux.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SurfaceConcentrationFlux object in the specified step.',
	),
	'SurfaceCurrent.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceCurrent.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SurfaceCurrent object in the specified step.',
	),
	'SurfaceCurrentDensity.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceCurrentDensity.setValuesInStep':(
		'stepName <, comp1, comp2, comp3, amplitude>',
		'This method modifies the propagating data for an existing SurfaceCurrentDensity object in the specified step.',
	),
	'SurfaceFeatureAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of surface feature angle assignments to new surfaces in a given step.',
	),
	'SurfaceFeatureAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of surface feature angle assignments already defined on surfaces in a given step.',
	),
	'SurfaceFeatureAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing surface feature angle assignments from a ContactExp object.',
	),
	'SurfaceHeatFlux.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceHeatFlux.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SurfaceHeatFlux object in the specified step.',
	),
	'SurfaceOffsetAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of surface offset fraction assignments to new surfaces in a given step.',
	),
	'SurfaceOffsetAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of surface offset fraction assignments already defined on surfaces in a given step.',
	),
	'SurfaceOffsetAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing surface offset fraction assignments.',
	),
	'SurfacePoreFluid.setValues':'<value is a self-reference, replaced by this string>',
	'SurfacePoreFluid.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SurfacePoreFluid object in the specified step.',
	),
	'SurfaceSection.RebarLayers':'<value is a self-reference, replaced by this string>',
	'SurfaceThicknessAssignment.appendInStep':(
		'stepName, assignments',
		'This method allows addition of surface thickness assignments to new surfaces in a given step.',
	),
	'SurfaceThicknessAssignment.changeValuesInStep':(
		'stepName, index, value',
		'This method allows modification of surface thickness assignments already defined on surfaces in a given step.',
	),
	'SurfaceThicknessAssignment.delete':(
		'indices',
		'The delete method allows you to delete existing surface thickness assignments.',
	),
	'SurfaceToSurfaceContactExp.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceToSurfaceContactExp.setValuesInStep':(
		'stepName <, interactionProperty, contactControls>',
		'This method modifies the propagating data for an existing SurfaceToSurfaceContactExp object in the specified step.',
	),
	'SurfaceToSurfaceContactExp.swapSurfaces':(
		'',
		'This method switches the master and slave surfaces of a surface-to-surface contact pair. This command is valid only during the step in which the interaction is created.',
	),
	'SurfaceToSurfaceContactStd.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceToSurfaceContactStd.setValuesInStep':(
		'stepName <, interactionProperty, interferenceType, overclosure, interferenceDirectionType, direction, amplitude, contactControls>',
		'This method modifies the propagating data for an existing SurfaceToSurfaceContactStd object in the specified step.',
	),
	'SurfaceToSurfaceContactStd.swapSurfaces':(
		'',
		'This method switches the master and slave surfaces of a surface-to-surface contact pair. This command is valid only for the step in which the interaction is created.',
	),
	'SurfaceTraction.setValues':'<value is a self-reference, replaced by this string>',
	'SurfaceTraction.setValuesInStep':(
		'stepName <, magnitude, amplitude>',
		'This method modifies the propagating data for an existing SurfaceTraction object in the specified step.',
	),
	'SvgOptions.setValues':(
		'<imageSize>',
		'This method modifies the \n SvgOptions\n object.\n ',
	),
	'Swelling.Ratios':'<value is a self-reference, replaced by this string>',
	'Swelling.setValues':'<value is a self-reference, replaced by this string>',
	'SymbolDisplayOptions.setValues':(
		'<otherSymbolSize, arrowSymbolSize, faceSymbolDensity, edgeSymbolDensity, meshSymbolFraction, showFields>',
		'This method modifies the SymbolDisplayOptions object.',
	),
	'SymbolOptions.setValues':(
		'<options, vectorQuantity, vectorLineThickness, vectorArrowheadStyle, vectorColor, vectorColorMethod, vectorColorSpectrum, vectorIntervalNumber, symbolDensity, constantLengthArrows, tensorColorMethod, tensorColorSpectrum, tensorIntervalNumber, vectorMaxValueAutoCompute, vectorMaxValue, vectorMinValueAutoCompute, vectorMinValue, tensorQuantity, arrowSymbolSize, tensorMaxPrinColor, tensorMinPrinColor, tensorMidPrinColor, tensorSelectedPrinColor, tensorLineThickness, tensorArrowheadStyle, tensorMaxValueAutoCompute, tensorMaxValue, tensorMinValueAutoCompute, tensorMinValue>',
		'This method modifies the SymbolOptions object.',
	),
	'SymbolStyle.setValues':(
		'<color, show, marker, size>',
		'This method modifies the SymbolStyle object.',
	),
	'TProfile.setValues':'<value is a self-reference, replaced by this string>',
	'TabularAmplitude.BaselineCorrection':'<value is a self-reference, replaced by this string>',
	'TabularAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'TangentialBehavior.setValues':'<value is a self-reference, replaced by this string>',
	'TempDisplacementDynamicsStep.setValues':'<value is a self-reference, replaced by this string>',
	'Temperature.move':(
		'fromStepName, toStepName',
		'This method moves the TemperatureState object from one step to a different step.',
	),
	'Temperature.setValues':'<value is a self-reference, replaced by this string>',
	'Temperature.setValuesInStep':(
		'stepName',
		'This method modifies the propagating data for an existing Temperature object in the specified step.',
	),
	'TemperatureBC.setValues':'<value is a self-reference, replaced by this string>',
	'TemperatureBC.setValuesInStep':(
		'stepName <, magnitude, dof, amplitude>',
		'This method modifies the propagating data for an existing TemperatureBC object in the specified step.',
	),
	'TensionCutOff.setValues':'<value is a self-reference, replaced by this string>',
	'TensionStiffening.setValues':'<value is a self-reference, replaced by this string>',
	'Text.setValues':'<value is a self-reference, replaced by this string>',
	'TextStyle.setValues':(
		'<color, show, font, rotationAngle>',
		'This method modifies the TextStyle object.',
	),
	'ThermalConductance.setValues':'<value is a self-reference, replaced by this string>',
	'Tie.setValues':'<value is a self-reference, replaced by this string>',
	'Tie.swapSurfaces':(
		'',
		'This method switches the master and slave surfaces of a tied constraint. This command is valid only during the step in which the interaction is created.',
	),
	'TiffOptions.setValues':(
		'<imageSize>',
		'This method modifies the \n TiffOptions\n object.\n ',
	),
	'TimePoint.setValues':'<value is a self-reference, replaced by this string>',
	'Title.setValues':(
		'<title, text, area, useDefault, titleStyle>',
		'This method modifies the Title object.',
	),
	'TopologyCyclicSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyDemoldControl.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyMemberSize.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyOverhangControl.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyPlanarSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyPointSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyRotationalSymmetry.setValues':'<value is a self-reference, replaced by this string>',
	'TopologyTask.setValues':'<value is a self-reference, replaced by this string>',
	'Transform.matrix':(
		'',
		'This method returns the transformation matrix as a tuple of 12 Floats.',
	),
	'TransverseShearBeam.setValues':'<value is a self-reference, replaced by this string>',
	'TransverseShearShell.setValues':'<value is a self-reference, replaced by this string>',
	'TrapezoidalProfile.setValues':'<value is a self-reference, replaced by this string>',
	'TriaxialTestData.setValues':'<value is a self-reference, replaced by this string>',
	'Trs.setValues':'<value is a self-reference, replaced by this string>',
	'TrussSection.setValues':'<value is a self-reference, replaced by this string>',
	'TurnControl.setValues':'<value is a self-reference, replaced by this string>',
	'TwoPointSpringDashpot.setValues':'<value is a self-reference, replaced by this string>',
	'TypeBC.setValues':(
		'<region, typeName, buckleCase, localCsys>',
		'This method modifies the data for an existing TypeBC object in the step where it is created.',
	),
	'TypeBC.setValuesInStep':(
		'stepName <, typeName>',
		'This method always returns a value error for a TypeBC; it is inherited from the BoundaryCondition object.',
	),
	'UniaxialTestData.setValues':'<value is a self-reference, replaced by this string>',
	'UserAmplitude.setValues':'<value is a self-reference, replaced by this string>',
	'UserData.Arrow':'<value is a self-reference, replaced by this string>',
	'UserData.Text':'<value is a self-reference, replaced by this string>',
	'UserData.XYData':'<value is a self-reference, replaced by this string>',
	'UserMaterial.setValues':'<value is a self-reference, replaced by this string>',
	'UserOutputVariables.setValues':'<value is a self-reference, replaced by this string>',
	'UserXYData.addData':(
		'data',
		'This method replaces the contents of the data member of the XYData object.',
	),
	'UserXYData.getData':(
		'',
		'Returns the contents of the data member of the XYData object.',
	),
	'Velocity.setValues':'<value is a self-reference, replaced by this string>',
	'VelocityAdaptiveMeshConstraint.setValues':'<value is a self-reference, replaced by this string>',
	'VelocityAdaptiveMeshConstraint.setValuesInStep':(
		'stepName <, v1, v2, v3, vr1, vr2, vr3, amplitude>',
		'This method modifies the propagating data for an existing VelocityAdaptiveMeshConstraint object in the specified step.',
	),
	'VelocityBC.setValues':'<value is a self-reference, replaced by this string>',
	'VelocityBC.setValuesInStep':(
		'stepName <, v1, v2, v3, vr1, vr2, vr3, amplitude>',
		'This method modifies the propagating data for an existing VelocityBC object in the specified step.',
	),
	'VelocityBaseMotionBC.setValues':'<value is a self-reference, replaced by this string>',
	'VelocityBaseMotionBC.setValuesInStep':(
		'stepName <, amplitude>',
		'This method modifies the propagating data for an existing VelocityBaseMotionBC object in the specified step.',
	),
	'VelocityDependence.setValues':'<value is a self-reference, replaced by this string>',
	'Vertex.getEdges':(
		'',
		'This method returns a sequence consisting of the edge ids of the edges which share this vertex.',
	),
	'Vertex.getElements':(
		'',
		'This method returns an array of element objects that are associated with the vertex.',
	),
	'Vertex.getNodes':(
		'',
		'This method returns an array of node objects that are associated with the vertex.',
	),
	'Vertex.index':(
		'keyword argument not implemented',
		'This method returns the index of a Vertex in the VertexArray.',
	),
	'VertexArray.findAt':(
		'coordinates <, printWarning>',
		'This method returns the object or objects in the VertexArray located at the given coordinates.findAt \n initially uses the ACIS tolerance of 1E-6. As a result, \n findAt \n returns any \n Vertex \n object that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, \n findAt \n uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities).\n findAt \n will always try to find objects among all the vertices in the part or assembly instance and will not restrict itself to a subset even if the VertexArray represents such subset.\n ',
	),
	'VertexArray.getBoundingBox':(
		'',
		'This method returns a dictionary of two tuples representing minimum and maximum boundary\n values of the bounding box of the minimum size containing the vertex sequence.',
	),
	'VertexArray.getByBoundingBox':(
		'<xMin, yMin, zMin, xMax, yMax, zMax>',
		'This method returns an array of vertex objects that lie within the specified bounding box.',
	),
	'VertexArray.getByBoundingCylinder':(
		'center1, center2, radius',
		'This method returns an array of vertex objects that lie within the specified bounding cylinder.',
	),
	'VertexArray.getByBoundingSphere':(
		'center, radius',
		'This method returns an array of vertex objects that lie within the specified bounding sphere.',
	),
	'VertexArray.getClosest':(
		'coordinates <, searchTolerance>',
		'This method returns a object or objects in the VertexArray closest to the given set of points, where the given points need not lie on \n Vertex \n objects in the VertexArray.\n ',
	),
	'VertexArray.getSequenceFromMask':(
		'mask',
		'This method returns the object or objects in the VertexArray identified using the specified \n mask. This command is generated when the \n JournalOptions \n are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.\n ',
	),
	'View.fitView':(
		'<drawImmediately>',
		'This method scales the displayable object (such as a part, the assembly, or an X&#8211;Y plot) to fit the viewport.',
	),
	'View.next':(
		'<drawImmediately>',
		'This method restores the view in the viewport to the next view setting in the list. (There is a list of eight views stored for each viewport.) If there is no next view, no action is taken.\n This method is not available for a \n    LayerView.\n    ',
	),
	'View.pan':(
		'<xFraction, yFraction, asMovie, drawImmediately>',
		'This method pans the view in the viewport using absolute, not relative, mode.',
	),
	'View.previous':(
		'<drawImmediately>',
		'This method restores the view in the viewport to the previous view setting in the list. (There is a list of eight views stored for each viewport.) If there is no previous view, no action is taken. \n This method is not available for a \n    LayerView.\n    ',
	),
	'View.rotate':(
		'<xAngle, yAngle, zAngle, mode, asMovie, drawImmediately>',
		'This method rotates the view in the viewport.  If a center of rotation has been previously specified and \n asMovie\n is \n OFF\n then this method will honor that rotation center.\n ',
	),
	'View.setLayerTransform':(
		'<layerTransform, options, drawImmediately>',
		'This method modifies the transformation used to position a \n Layer.\n This method is not available for \n    Session\n    and \n    ViewportViews.\n    ',
	),
	'View.setProjection':(
		'projection <, drawImmediately>',
		'This method modifies the appearance of three-dimensional models in the viewport. Choosing \n PERSPECTIVE\n makes a model appear more realistic by decreasing the apparent size of features that are farther away from the viewing point.\n This method is not available for a \n    LayerView.\n    ',
	),
	'View.setRotationCenter':(
		'rotationCenter',
		'This method sets the center of rotation to the specified location.',
	),
	'View.setValues':(
		'<options, drawImmediately>',
		'This method modifies the \n View\n object.\n This method is not available for a \n    LayerView.\n    ',
	),
	'View.setViewpoint':(
		'viewVector <, cameraUpVector, drawImmediately>',
		"This method sets the camera's position in the viewport.\n This method is not available for a \n    LayerView.\n    ",
	),
	'View.zoom':(
		'zoomFactor <, mode, asMovie, drawImmediately>',
		'This method magnifies the view in the viewport.',
	),
	'View.zoomRectangle':(
		'point1, point2 <, drawImmediately>',
		'This method fills the viewport with the graphics located within the given rectangle.',
	),
	'ViewCut.setValues':(
		'<angle, motion, position, radius, rotationAxis, value, showModelAboveCut, showModelOnCut, showModelBelowCut, showFreeBodyCut, csysName, origin, normal, axis2, cylinderAxis, followDeformation, overrideAveraging, overrideRgnBoundaryAvg, referenceFrame>',
		'This method modifies the ViewCut object.',
	),
	'ViewCut.updateVariable':(
		'',
		'This method updates the field associated with an isosurface cut to be consistent with the current primary variable.',
	),
	'ViewCutOptions.setValues':(
		'<options, belowOptions, useBelowOptions, onOptions, useOnOptions, aboveOptions, useAboveOptions, freeBodyCutThru, freeBodyStepThru, numCutFreeBody, displaySlicing, slicingAtPathNodes, freeBodySumOnPath, cutFreeBodyMin, cutFreeBodyMax, showHeatFlowRate, summationLoc, componentResolution, csysName, pathName, summationPoint, yAxis>',
		'This method modifies the ViewCutOptions object.',
	),
	'ViewerOptions.setValues':(
		'<primaryVariableCaching, deformedVariableCaching, cutVariableCaching, odbUpdateChecking, odbUpdateCheckInterval>',
		'This method modifies the ViewerOptions object.',
	),
	'Viewport.Layer':(
		'name',
		'This method creates a Layer object in the Layer repository.',
	),
	'Viewport.addDrawings':(
		'<names>',
		'This method identifies the names of \n Drawing\n objects to be rendered in the \n Viewport.\n ',
	),
	'Viewport.bringToFront':(
		'',
		'This method moves the \n Viewport\n object to the front.\n ',
	),
	'Viewport.disableColorCodeUpdates':(
		'',
		'This method disables \n Viewport\n updates and internal computations triggered because of color coding.  Performance improvement will be significant when color coding is ON and repeating operations are performed using a script each of which requires color code updates.  No benefit will be had when color coding is OFF.\n ',
	),
	'Viewport.disableMultipleColors':(
		'',
		'This method disables applying multiple color mappings that was enabled using \n enableMultipleColors',
	),
	'Viewport.disableRefresh':(
		'',
		'This method disables \n Viewport\n refresh. Some methods that require the \n Viewport\n to be up-to-date will override this setting. It is advisable to use this method sparingly.\n ',
	),
	'Viewport.enableColorCodeUpdates':(
		'',
		'This method enables \n Viewport\n color code updates disabled using \n disableColorCodeUpdates.\n ',
	),
	'Viewport.enableMultipleColors':(
		'',
		'This method enables multiple color mappings to be applied at the same time. It also ensures that the \n Viewport\n is updated correctly when \n initialColor\n is set.\n ',
	),
	'Viewport.enableRefresh':(
		'',
		'This method enables \n Viewport\n refresh disabled using \n disableRefresh.\n ',
	),
	'Viewport.forceRefresh':(
		'',
		'This method causes the \n Viewport\n to refresh immediately. It is provided to allow scripts to refresh the \n Viewport\n before the script terminates.  Normally, there would only be a single cumulative refresh that takes place immediately after the script completes.\n ',
	),
	'Viewport.getActiveElementLabels':(
		'<useCut, printResults>',
		'This method returns the element labels currently active in the viewport based on the current display group and optionally based on any active cut if \n useCut\n is \n True. The labels will optionally be printed to the replay file if \n printResults\n is \n True. The \n getActiveElementLabels\n method has the following arguments:\n ',
	),
	'Viewport.getActiveNodeLabels':(
		'<useCut, printResults>',
		'This method returns the node labels currently active in the viewport based on the current display group and optionally based on any active cut if \n useCut\n is  \n True.  The labels will optionally be printed to the replay file if\n printResults\n is \n True. The \n getActiveNodeLabels\n method has the following arguments:\n ',
	),
	'Viewport.getPrimVarMinMaxLoc':(
		'',
		'This method returns a dictionary containing the minimum, maximum and their location for the current primary variable. A contour plot should be displayed in the current viewport or else the method will return \n None.\n ',
	),
	'Viewport.makeCurrent':(
		'',
		'This method makes the\n Viewport\n object the current viewport.\n ',
	),
	'Viewport.maximize':(
		'',
		'This method maximizes the \n Viewport\n object to fill the drawing area.\n ',
	),
	'Viewport.minimize':(
		'',
		'This method minimizes the \n Viewport\n object to appear as an abbreviated title bar.\n ',
	),
	'Viewport.offset':(
		'<deltaX, deltaY>',
		'This method modifies the current  \n X-\n Y \n location of the viewport by the specified distance.\n ',
	),
	'Viewport.plotAnnotation':(
		'annotation <, index>',
		'This method plots an \n Annotation \n object in a\n Viewport.\n ',
	),
	'Viewport.removeDrawings':(
		'<names>',
		'This method identifies the names of \n Drawing\n objects to no longer be rendered in the \n Viewport.\n ',
	),
	'Viewport.restore':(
		'',
		'This method restores a maximized or minimized \n Viewport\n object to its previous size and location.\n ',
	),
	'Viewport.sendToBack':(
		'',
		'This method moves the \n Viewport\n object to the back.\n ',
	),
	'Viewport.setColor':(
		'leaf <, edgeColorWireHide, edgeColorFillShade, fillColor, nodeSymbolColor, nodeSymbolType, nodeSymbolSize>',
		'This method specifies the color of a \n Leaf\n object.\n ',
	),
	'Viewport.setValues':(
		'<displayedObject, displayMode, visibleLayers, viewManipLayers, currentLayer, layerOffset>',
		'This method modifies the \n Viewport\n object. The arguments to \n setValues\n are the same as the arguments to the \n Viewport\n method, except for the \n name\n argument. In addition, the \n setValues\n method has the following arguments:\n ',
	),
	'Viewport.showCell':(
		'',
		'Need arguments',
	),
	'Viewport.showDatum':'<value is a self-reference, replaced by this string>',
	'Viewport.showEdge':'<value is a self-reference, replaced by this string>',
	'Viewport.showElemEdge':'<value is a self-reference, replaced by this string>',
	'Viewport.showElement':'<value is a self-reference, replaced by this string>',
	'Viewport.showElemface':'<value is a self-reference, replaced by this string>',
	'Viewport.showFace':'<value is a self-reference, replaced by this string>',
	'Viewport.showIP':'<value is a self-reference, replaced by this string>',
	'Viewport.showNode':'<value is a self-reference, replaced by this string>',
	'Viewport.showSet':'<value is a self-reference, replaced by this string>',
	'Viewport.showVertex':'<value is a self-reference, replaced by this string>',
	'Viewport.timeDisplay':(
		'<numFrames, numSeconds, degreesPerFrame>',
		'This method refreshes the \n Viewport\n display \n numFrames\n times and then checks to see if \n numSeconds\n seconds have elapsed. If not, it will continue refreshing the \n Viewport\n until the time has elapsed.  At completion, the actual number of refreshes (frames) rendered and elapsed time will be reported along with the calculated frames-per-second (fps).\n ',
	),
	'ViewportAnnotationOptions.setValues':(
		'<triad, triadPosition, triadColor, triadLabels, triadFont, triadSize, legend, legendMinMax, legendBox, legendDecimalPlaces, legendPosition, legendFont, legendTextColor, legendBackgroundStyle, legendBackgroundColor, title, titleBox, titlePosition, titleFont, titleTextColor, titleBackgroundStyle, titleBackgroundColor, state, stateBox, statePosition, stateFont, stateTextColor, stateBackgroundStyle, stateBackgroundColor, compass, compassScale, compassPrivilegedPlane>',
		'This method modifies the \n ViewportAnnotationOptions \n object.\n ',
	),
	'ViscoStep.setValues':'<value is a self-reference, replaced by this string>',
	'Viscoelastic.CombinedTestData':(
		'table <, volinf, shrinf>',
		'This method creates a CombinedTestData object.',
	),
	'Viscoelastic.ShearTestData':(
		'table <, shrinf>',
		'This method creates a ShearTestData object.',
	),
	'Viscoelastic.Trs':(
		'<definition, table>',
		'This method creates a Trs object.',
	),
	'Viscoelastic.VolumetricTestData':'<value is a self-reference, replaced by this string>',
	'Viscoelastic.setValues':'<value is a self-reference, replaced by this string>',
	'Viscosity.Trs':'<value is a self-reference, replaced by this string>',
	'Viscosity.setValues':'<value is a self-reference, replaced by this string>',
	'Viscous.Potential':'<value is a self-reference, replaced by this string>',
	'Viscous.setValues':'<value is a self-reference, replaced by this string>',
	'VoidNucleation.setValues':'<value is a self-reference, replaced by this string>',
	'VoidsRatio.setValues':'<value is a self-reference, replaced by this string>',
	'VolumetricTestData.setValues':'<value is a self-reference, replaced by this string>',
	'WaveReflection.setValues':'<value is a self-reference, replaced by this string>',
	'XFEMCrack.setValues':'<value is a self-reference, replaced by this string>',
	'XFEMCrackGrowth.setValues':'<value is a self-reference, replaced by this string>',
	'XFEMCrackGrowth.setValuesInStep':(
		'stepName <, allowGrowth>',
		'This method modifies the propagating data for an existing XFEMCrackGrowth object in the specified step.',
	),
	'XYCurve.setValues':(
		'<displayTypes, legendLabel, symbolFrequency, useDefault>',
		'This method modifies the XYCurve object.',
	),
	'XYData.save':(
		'',
		'This method saves a temporary XYData. The name of the XYData is changed to "XYData-#".  If the XYData is already saved, nothing is done.',
	),
	'XYData.setValues':'<value is a self-reference, replaced by this string>',
	'XYPlot.autoColor':(
		'<lines, symbols>',
		'This method distributes the colors on all curves displayed in the XYPlot using the color palette defined by the xyColors AutoColors object.',
	),
	'XYPlot.autoSymbol':(
		'',
		'This method distributes the symbols on all curves displayed in the XYPlot.',
	),
	'XYPlot.fitCurves':(
		'',
		'This method resets the transform of all the charts of the XYPlot object. It cancels any zoom or pan action.',
	),
	'XYPlot.next':(
		'<drawImmediately>',
		'This method restores the transform member of the active Chart object to the next setting in the transform list. (There is a list of eight transforms stored for each chart.) If there is no next transform, no action is taken. ',
	),
	'XYPlot.previous':(
		'<drawImmediately>',
		'This method restores the transform member of the active Chart object to the previous setting in the transform list. (There is a list of eight transforms stored for each chart.) If there is no next transform, no action is taken. ',
	),
	'XYPlot.setValues':(
		'<title, transform>',
		'This method modifies the XYPlot object.',
	),
	'XYReportOptions.setValues':(
		'<pageWidth, numDigits, interpolation, xyData, totals, minMax, pageWidthLimited, numberFormat, layout>',
		'This method modifies the XYReportOptions object.',
	),
	"sys.modules['customKernel'].CommandRegister":(
		'',
		'This class allows you to derive a general class that can be queried from the GUI and is capable of notifying the GUI when the contents of the class change.',
	),
	"sys.modules['customKernel'].RegisteredDictionary":(
		'',
		'This method creates a RegisteredDictionary object.',
	),
	"sys.modules['customKernel'].RegisteredList":(
		'',
		'This method creates a RegisteredList object.',
	),
	"sys.modules['customKernel'].RegisteredTuple":(
		'tuple',
		'This method creates a RegisteredTuple object.',
	),
	"sys.modules['customKernel'].RepositorySupport":(
		'',
		'This method creates a RepositorySupport object.',
	),
	"sys.modules['displayGroupMdbToolset'].Leaf":(
		'leafType',
		'This method creates a Leaf object.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromDatums":(
		'datumSeq',
		' This method creates a Leaf object from a sequence of datum objects. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromDisplayGroup":(
		'displayGroup',
		'This method creates a Leaf object from a sequence of Display Group objects.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromGeometry":(
		'<edgeSeq, faceSeq, cellSeq>',
		'This method creates a Leaf object from a sequence of edge, face and cell geometry objects. Any combination of edge, face or cell arguments is allowed however the arguments must specify at least one object--it is not permissible to create an empty leaf.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromInstance":(
		'instances',
		'This method creates a Leaf object from a sequence of part instance objects.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromInstanceElementLabels":(
		'elementLabels',
		' This method creates a Leaf object from a sequence of Strings specifying the element labels. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromInstanceNodeLabels":(
		'nodeLabels',
		' This method creates a Leaf object from a sequence of Strings specifying the node labels. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromMeshElementLabels":(
		'elementSeq',
		' This method creates a Leaf object from a sequence of mesh element objects. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromMeshNodeLabels":(
		'nodeSeq',
		' This method creates a Leaf object from a sequence of mesh node objects. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromMeshSurfaceSets":(
		'surfaceSets',
		'This method creates a Leaf object from a sequence of surface sets.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromPartElementLabels":(
		'part, elementLabels',
		' This method creates a Leaf object from a sequence of Strings specifying element labels. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromPartNodeLabels":(
		'part, nodeLabels',
		' This method creates a Leaf object from a sequence of Strings specifying node labels. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromReferencePoint":(
		'refPtSeq',
		'This method creates a Leaf object from a sequence of ReferencePoint objects.',
	),
	"sys.modules['displayGroupMdbToolset'].LeafFromSets":(
		'sets',
		'This method creates a Leaf object from a sequence of Set objects.',
	),
	"sys.modules['displayGroupOdbToolset'].Leaf":'<value is a self-reference, replaced by this string>',
	"sys.modules['displayGroupOdbToolset'].LeafFromDisplayGroup":'<value is a self-reference, replaced by this string>',
	"sys.modules['displayGroupOdbToolset'].LeafFromElementLabels":(
		'partInstanceName, elementLabels',
		'This method creates a Leaf object from a sequence of element labels that belong to a single part instance.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromElementSets":(
		'elementSets',
		'This method creates a Leaf object from a sequence of element sets.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromElementVarRange":(
		'<minimumRange, maximumRange, insideRange>',
		'This method creates a Leaf object from elements with values lying in a variable range. ',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromModelElemLabels":(
		'elementLabels',
		'This method creates a Leaf object from a sequence of element labels spanning several part instances. ',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromModelNodeLabels":(
		'nodeLabels',
		'This method creates a Leaf object from a sequence of node labels spanning several part instances. ',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromNodeLabels":(
		'partInstanceName, nodeLabels',
		'This method creates a Leaf object from a sequence of node labels that belong to a single part instance.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromNodeSets":(
		'nodeSets',
		'This method creates a Leaf object from a sequence of node sets.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromNodeVarRange":(
		'<minimumRange, maximumRange, insideRange>',
		'This method creates a Leaf object from nodes with values lying in a variable range. ',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbElementLayups":(
		'elementLayups',
		' This method creates a Leaf object from a sequence of Strings specifying layup names. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbElementMaterials":(
		'elementMaterials',
		' This method creates a Leaf object from a sequence of Strings specifying material names. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbElementPick":(
		'elementPick',
		' This method creates a Leaf object from a tuple containing machine readable, compact strings defining the elements picked for each part instance. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbElementPlies":(
		'elementPlies',
		' This method creates a Leaf object from a sequence of Strings specifying ply names. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbElementSections":(
		'elementSections',
		' This method creates a Leaf object from a sequence of Strings specifying section names. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbElementTypes":(
		'elementTypes',
		' This method creates a Leaf object from a sequence of Strings specifying element names. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromOdbNodePick":(
		'nodePick',
		' This method creates a Leaf object from a tuple containing machine readable, compact strings defining the nodes picked for each part instance. Leaf objects specify the items in a display group.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromPartInstance":(
		'partInstanceName',
		'This method creates a Leaf object from a list of part instance names.',
	),
	"sys.modules['displayGroupOdbToolset'].LeafFromSurfaceSets":'<value is a self-reference, replaced by this string>',
	"sys.modules['displayGroupOdbToolset'].LeafFromSurfaceVarRange":(
		'<minimumRange, maximumRange, insideRange>',
		'This method creates a Leaf object from surfaces with values lying in a variable range. ',
	),
	"sys.modules['mesh'].ElemType":(
		'elemCode <, elemLibrary, hourglassStiffness, bendingHourglass, drillingHourglass, kinematicSplit, distortionControl, lengthRatio, secondOrderAccuracy, hourglassControl, weightFactor, displacementHourglass, rotationalHourglass, outOfPlaneDisplacementHourglass, elemDeletion, particleConversion, particleConversionThreshold, particleConversionPPD, particleConversionKernel, maxDegradation, viscosity, linearBulkViscosity, quadraticBulkViscosity>',
		'This method creates an ElemType object.',
	),
	"sys.modules['mesh'].MeshEdgeArray":(
		'edges',
		'This method creates a MeshEdgeArray object.',
	),
	"sys.modules['mesh'].MeshElementArray":(
		'elements',
		'This method creates a MeshElementArray object.',
	),
	"sys.modules['mesh'].MeshFaceArray":(
		'faces',
		'This method creates a MeshFaceArray object.',
	),
	"sys.modules['mesh'].MeshNodeArray":(
		'nodes',
		'This method creates a MeshNodeArray object.',
	),
	"sys.modules['odbAccess'].AnalyticSurfaceProfile":(
		'',
		'This method creates a OdbSequenceAnalyticSurfaceSegment object.',
	),
	"sys.modules['odbAccess'].AnalyticSurfaceSegment":(
		'type, data',
		'This method creates an AnalyticSurfaceSegment object.',
	),
	"sys.modules['odbAccess'].HistoryPoint":(
		'node',
		'This method creates a HistoryPoint object for a node.',
	),
	"sys.modules['odbSection'].LayerProperties":(
		'barArea, orientationAngle, layerName, material <, barSpacing, layerPosition, spacingAngle, extensionRatio, radius>',
		'This method creates a LayerProperties object.',
	),
	"sys.modules['odbSection'].SectionLayer":(
		'thickness, material <, orientAngle, numIntPts, axis, angle, additionalRotationType, thicknessType, plyName, orientation, additionalRotationField, thicknessField>',
		'This method creates a SectionLayer object.',
	),
	"sys.modules['regionToolset'].Region":(
		'<side1Faces, side2Faces, side12Faces, side1Edges, side2Edges, end1Edges, end2Edges, circumEdges, face1Elements, face2Elements, face3Elements, face4Elements, face5Elements, face6Elements, side1Elements, side2Elements, side12Elements, end1Elements, end2Elements, circumElements>',
		'This command creates a surface-like region. For example, myRegion = regionToolset.Region(side1Faces=f[12:14])The arguments are the same as the arguments to the Surface method, except for the name argument.',
	),
	"sys.modules['section'].LayerProperties":'<value is a self-reference, replaced by this string>',
	"sys.modules['section'].MdbPlyStackPlot":(
		'part, region',
		'This method creates a PlyStackPlot object from a region of a part that contains a composite shell layup.',
	),
	"sys.modules['section'].SectionLayer":'<value is a self-reference, replaced by this string>',
	"sys.modules['visualization'].OdbPlyStackPlot":(
		'odb, sectionName <, offset>',
		'This method creates a PlyStackPlot object from a composite shell section of an Odb object.',
	),
	"sys.modules['visualization'].OptionArg":(
		'<renderStyle, visibleEdges, edgeColorWireHide, edgeColorFillShade, edgeLineStyle, edgeLineThickness, colorCodeOverride, fillColor, translucency, translucencyFactor>',
		'This method creates an OptionArg object.',
	),
	"sys.modules['xyPlot'].AreaStyle":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].LineStyle":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].QuantityType":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].SymbolStyle":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].TextStyle":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].XYData":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].XYDataFromFile":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].XYDataFromFreeBody":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].XYDataFromHistory":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].XYDataFromPath":'<value is a self-reference, replaced by this string>',
	"sys.modules['xyPlot'].XYDataFromShellThickness":(
		'odb, outputPosition, variable <, elementSets, elementLabels, nodeSets, nodeLabels, numericForm, complexAngle>',
		'This method creates a list of XYData objects by reading through the thickness field data from an Odb object.',
	),
	"sys.modules['xyPlot'].xyDataListFromField":'<value is a self-reference, replaced by this string>',
}

objectDocstringTable={
	'AVIOptions':'The AVIOptions object is used to store values and attributes to be used in generating AVI animation. The AVIOptions object has no constructor. Abaqus creates the aviOptions member when the animation module is imported.',
	'Abaqus':'',
	'AccelerationBC':'The AccelerationBC object stores the data for an acceleration boundary condition.',
	'AccelerationBCState':'The AccelerationBCState object stores the propagating data of an acceleration boundary condition in a step. One instance of this object is created internally by the AccelerationBC object for each step. The instance is also deleted internally by the AccelerationBC object.The AccelerationBCState object has no constructor or methods.',
	'AccelerationBaseMotionBC':'The AccelerationBaseMotionBC object stores the data for an acceleration base motion boundary condition.',
	'AccelerationBaseMotionBCState':'The AccelerationBaseMotionBCState object stores the propagating data for a velocity base motion boundary condition in a step. One instance of this object is created internally by the AccelerationBaseMotionBC object for each step. The instance is also deleted internally by the AccelerationBaseMotionBC object.The AccelerationBaseMotionBCState object has no constructor or methods.',
	'AcisFile':'The AcisFile object is a file object used to open ACIS-, STEP-, and IGES-format files.',
	'AcousticImpedance':'The AcousticImpedance object defines surface impedance information or nonreflecting boundaries for acoustic and coupled acoustic-structural analyses.',
	'AcousticImpedanceProp':'The AcousticImpedanceProp object is an interaction property that defines the properties referred to by an AcousticImpedance object.',
	'AcousticImpedanceState':'The AcousticImpedanceState object stores the propagating data of an AcousticImpedance object in a step. One instance of this object is created internally by the AcousticImpedance object for each step. The instance is also deleted internally by the AcousticImpedance object.The AcousticImpedanceState object has no constructor or methods.',
	'AcousticInfiniteSection':'The AcousticInfiniteSection object defines the properties of an acoustic section.',
	'AcousticInterfaceSection':'The AcousticInterfaceSection object defines the properties of an acoustic section.',
	'AcousticMedium':'The AcousticMedium object specifies the acoustic properties of a material.',
	'AcousticPressureBC':'The AcousticPressureBC object stores the data for an acoustic pressure boundary condition.',
	'AcousticPressureBCState':'The AcousticPressureBCState object stores the propagating data for an acoustic pressure boundary condition in a step. One instance of this object is created internally by the AcousticPressureBC object for each step. The instance is also deleted internally by the AcousticPressureBC object.The AcousticPressureBCState object has no constructor or methods.',
	'ActuatorAmplitude':'The ActuatorAmplitude object defines an actuator amplitude curve.',
	'ActuatorSensor':'The ActuatorSensor object defines a single point actuator where the actuation is determined by a user subroutine (UEL). The subroutine senses the data at the same point as the actuator.',
	'ActuatorSensorProp':'The ActuatorSensorProp object is an interaction property that defines the properties referred to by an ActuatorSensor object.',
	'ActuatorSensorState':'The ActuatorSensorState object stores the propagating data of an actuator sensor in a step. One instance of this object is created internally by the ActuatorSensor object for each step. The instance is also deleted internally by the ActuatorSensor object.The ActuatorSensorState object has no constructor, methods, or members.',
	'AdaptiveMeshConstraint':'The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. The AdaptiveMeshConstraint object has no explicit constructor. The methods and members of the AdaptiveMeshConstraint object are common to all objects derived from the AdaptiveMeshConstraint object.',
	'AdaptiveMeshConstraintState':'The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary Lagrangian Eularian (ALE) style AdaptiveMeshConstraintState objects. The AdaptiveMeshConstraintState object has no explicit constructor or methods. The members of the AdaptiveMeshConstraintState object are common to all objects derived from the AdaptiveMeshConstraintState object.',
	'AdaptiveMeshControl':'The AdaptiveMeshControl object is used to control various aspects of Arbitrary Lagrangian Eularian (ALE) style adaptive smoothing and advection algorithms applied to an ALE adaptive mesh domain.',
	'AdaptiveMeshDomain':'The AdaptiveMeshDomain object defines the region and controls that govern an Arbitrary Lagrangian Eularian (ALE) style adaptive smoothing mesh domain.Note that the adaptive mesh domain commands will change in a later version for consistency with the style used for loads. This style is implemented temporarily due to time constraints.',
	'AdaptivityIteration':' The AdaptivityIteration object contains information about a given iteration of the varying topology adaptivity process (adaptive remeshing).',
	'AdaptivityProcess':'The AdaptivityProcess object defines a series of jobs that will be submitted for analysis. Abaqus performs adaptive remeshing between each job.',
	'AdjustPoints':'The AdjustPoints constraint object is used to adjust points (nodes) to a surface.',
	'Amplitude':'The Amplitude object is the abstract base type for other Amplitude objects. The Amplitude object has no explicit constructor. The methods and members of the Amplitude object are common to all objects derived from the Amplitude.',
	'AnalysisStep':'The AnalysisStep object is the abstract base type for other Step objects, except the InitialStep object. It has no explicit constructor, no methods, and has only inherited members.',
	'AnalyticSurface':'The AnalyticSurface object is a geometric surface that can be described with straight and/or curved line segments.',
	'AnalyticSurfaceSegment':'An individual segment of the analytic surface.',
	'AnalyticalField':'The AnalyticalField object is the abstract base type for other AnalyticalField objects. The AnalyticalField object has no explicit constructor. The methods and members of the AnalyticalField object are common to all objects derived from the AnalyticalField.',
	'AnimationController':'The AnimationController object controls all object-based animation to be displayed in the viewports. The AnimationController object has no constructor. Abaqus creates the animationController member when it creates the Session object.',
	'AnimationOptions':'The AnimationOptions object is used to store values and attributes associated with an AnimationController object. The AnimationOptions object has no constructor command. Abaqus creates the animationOptions member when it creates the AnimationController object.',
	'AnnealStep':'The AnnealStep object anneals a structure by setting the velocities and all appropriate state variables to zero.',
	'AnnealTemperature':'The AnnealTemperature object specifies the material annealing temperature.',
	'Annotation':'The \n      Annotation\n      object is the abstract base type for other \n      Annotation\n      objects. The \n      Annotation\n      object has no explicit constructor. The methods and members of the \n      Annotation\n      object are common to all objects derived from \n      Annotation.\n   ',
	'AnnotationsToPlotArray':'The \n      AnnotationsToPlotArray\n      object is a sequence that stores references to plotted annotations. By adding annotations to and removing annotations from this sequence, you can control which annotations are displayed in a particular viewport.\n   ',
	'ArbitraryProfile':'The ArbitraryProfile object defines the properties of an arbitrary profile.',
	'Area':'The Area object is used to display a rectangular area in an XYPlot. The Area object has no constructor. Area objects are automatically created whenever a XYPlot, Chart, PlotTitle, or Legend objects are created.',
	'AreaStyle':'The AreaStyle object is used to define how areas are to be filled when drawing XY-plot objects.AreaStyle objects are automatically created whenever an Area object is created.  AreaStyle objects can be created using the methods described below. ',
	'Arrow':'The \n      Arrow\n      object stores the visual settings and location of an arrow annotation.\n   ',
	'AssembledFastener':'The AssembledFastener object defines an assembled fastener.',
	'Assembly':'An Assembly object is a container for instances of parts. The Assembly object has no constructor command. Abaqus creates the rootAssembly member when a Model object is created.',
	'AssemblyDisplayOptions':'The AssemblyDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport. The AssemblyDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'AttributeColorMap':'The \n      AttributeColorMap \n      object is used to store values and attributes associated with AttributeColorMap type objects. \n      AttributeColorMap \n      objects can be modified using the methods described below. The methods accessed via the \n      Viewport \n      object cause the AttributeColorMap object to be updated in the session.viewports[name].colorMappings repository.\n   ',
	'AutoColors':'The \n      AutoColors\n      object defines a color palette.\n   ',
	'Axis':'The Axis object is used to store the display attributes of axes. Axes objects are automatically created when adding XYCurve objects to a Chart object.',
	'AxisData':'The AxisData object is used to store the data attributes of axes. An AxisData object is automatically created when creating an Axis object.',
	'BCDisplayOptions':'The BCDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.bcs=ONThe BCDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'BaselineCorrection':'The BaselineCorrection object modifies an acceleration history to minimize the overall drift of the displacement obtained from the time integration of the given acceleration.',
	'BasicOptions':'The BasicOptions object stores values and attributes associated with an OdbDisplay object. The BasicOptions object has no constructor command. Abaqus creates the defaultOdbDisplay.basicOptions member when you import the Visualization module. Abaqus creates a basicOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.basicOptions. Abaqus creates the odbDisplay member when a viewport is created, using the attributes from the previous active viewport. The previous active viewport contains the attributes from the defaultOdbDisplay object for the session. The attributes from the defaultOdbDisplay object are copied from the previous active viewport to create the new viewport.BasicOptions objects are accessed in one of two ways:The default basic options. These settings are used as defaults when other basicOptions members are created. These settings can be set to customize user preferences.The basic options associated with a particular viewport.',
	'BeamOrientation':'The BeamOrientation object represents the direction of the first beam section axis $\x08f{n}_1$. Specifying the beam orientation using an additional node in the element connectivity list is not supported.',
	'BeamSection':'The BeamSection object defines the properties of a beam section.',
	'Behavior':'The \n      Behavior\n      object specifies the method used for calibrating a material.\n   ',
	'BiaxialTestData':'The BiaxialTestData object provides equibiaxial test data (compression and/or tension).',
	'BodyCharge':'The BodyCharge object stores the data for a body charge.',
	'BodyChargeState':'The BodyChargeState object stores the propagating data of a body charge in a step. One instance of this object is created internally by the BodyCharge object for each step. The instance is also deleted internally by the BodyCharge object.The BodyChargeState object has no constructor or methods.',
	'BodyConcentrationFlux':'The BodyConcentrationFlux object defines body concentration flux from a region or into a region.',
	'BodyConcentrationFluxState':'The BodyConcentrationFluxState object stores the propagating data for a BodyConcentrationFlux object in a step. One instance of this object is created internally by the BodyConcentrationFlux object for each step. The instance is also deleted internally by the BodyConcentrationFlux object.The BodyConcentrationFluxState object has no constructor or methods.',
	'BodyCurrent':'The BodyCurrent object stores the data for a body current.',
	'BodyCurrentDensity':'The BodyCurrentDensity object stores the data for a body current.',
	'BodyCurrentState':'The BodyCurrentState object stores the propagating data of a body current in a step. One instance of this object is created internally by the BodyCurrent object for each step. The instance is also deleted internally by the BodyCurrent object.The BodyCurrentState object has no constructor or methods.',
	'BodyForce':'The BodyForce object defines a distributed load.',
	'BodyForceState':'The BodyForceState object stores the propagating data of a body force in a step. One instance of this object is created internally by the BodyForce object for each step. The instance is also deleted internally by the BodyForce object.The BodyForceState object has no constructor or methods.',
	'BodyHeatFlux':'The BodyHeatFlux object defines body heat flux from a region or into a region.',
	'BodyHeatFluxState':'The BodyHeatFluxState object stores the propagating data for a Body BodyHeatFlux object in a step. One instance of this object is created internally by the BodyHeatFlux object for each step. The instance is also deleted internally by the BodyHeatFlux object.The BodyHeatFluxState object has no constructor or methods.',
	'BoltLoad':'The BoltLoad object defines a bolt load.',
	'BoltLoadState':'The BoltLoadState object stores the propagating data of a bolt load in a step. One instance of this object is created internally by the BoltLoad object for each step. The instance is also deleted internally by the BoltLoad object.The BoltLoadState object has no constructor or methods.',
	'BondedContact':'The BondedContact object stores the data for a stress.',
	'BoundaryCondition':'The BoundaryCondition object is the abstract base type for other BoundaryCondition objects. The BoundaryCondition object has no explicit constructor. The methods and members of the BoundaryCondition object are common to all objects derived from the BoundaryCondition.',
	'BoundaryConditionState':'The BoundaryConditionState object is the abstract base type for other BoundaryConditionState objects. The BoundaryConditionState object has no explicit constructor or methods. The members of the BoundaryConditionState object are common to all objects derived from the BoundaryConditionState object.',
	'BoxProfile':'The BoxProfile object defines the properties of a box profile.',
	'BrittleCracking':'The BrittleCracking object specifies cracking and postcracking properties for the brittle cracking material model.',
	'BrittleFailure':'The BrittleFailure object specifies the brittle failure of the material.',
	'BrittleShear':'The BrittleShear object specifies the postcracking shear behavior of a material used in a brittle cracking model.',
	'BuckleStep':'The BuckleStep object controls eigenvalue buckling estimation.',
	'ButterworthFilter':'The ButterworthFilter object defines a Butterworth type filter.',
	'CDCTerm':'The CDCTerm object is used to create contributing terms for a DerivedComponent object.  \t ',
	'Calibration':'A \n      Calibration\n      object is the object used to specify a material calibration. The \n      Calibration\n      object stores the data that is used for specifying materials from test data.\n   ',
	'CapCreepCohesion':'The CapCreepCohesion object specifies a cap creep model and material properties.',
	'CapCreepConsolidation':'The CapCreepConsolidation object specifies a cap creep model and material properties.',
	'CapHardening':'The CapHardening object specifies Drucker-Prager/Cap plasticity hardening.',
	'CapPlasticity':'The CapPlasticity object specifies the modified Drucker-Prager/Cap plasticity model.',
	'CastIronCompressionHardening':'The CastIronCompressionHardening object specifies hardening for the Cast- Iron plasticity model.',
	'CastIronPlasticity':'The CastIronPlasticity object specifies the Cast Iron plasticity model.',
	'CastIronTensionHardening':'The CastIronTensionHardening object specifies hardening for the Cast- Iron plasticity model.',
	'CavityRadiation':'The CavityRadiation object defines cavities for thermal radiation heat transfer and controls the calculation of viewfactors.',
	'CavityRadiationProp':'The CavityRadiationProp object is an interaction property that defines emissivity as a function of temperature and field variables.',
	'CavityRadiationState':'The CavityRadiationState object stores the propagating data for a CavityRadiation object. One instance of this object is created internally by the CavityRadiation object for each step. The instance is also deleted internally by the CavityRadiation object.The CavityRadiationState object has no constructor or methods.',
	'Cell':'Cells are volumetric regions of geometry.',
	'CellArray':'The CellArray is a sequence of \n      Cell \n      objects.\n   ',
	'Chart':'The Chart object is used to display XYCurve objects. A Chart object is automatically created when creating an XYPlot object',
	'Chebyshev1Filter':'The Chebyshev1Filter object defines a Chebyshev type 1 filter.',
	'Chebyshev2Filter':'The Chebyshev2Filter object defines a Chebyshev type 2 filter.',
	'CircularProfile':'The CircularProfile object defines the properties of a solid circular profile.',
	'ClayHardening':'The ClayHardening object specifies hardening for the clay plasticity model.',
	'ClayPlasticity':'The ClayPlasticity object specifies the extended Cam-clay plasticity model.',
	'Coexecution':'The Coexecution object contains a set of jobs as associated parameters to define a co-simulation analysis.',
	'CohesiveBehavior':'The CohesiveBehavior object specifies cohesive behavior for a contact interaction property.',
	'CohesiveSection':'The CohesiveSection object defines the properties of a cohesive section.',
	'Color':'The \n      Color\n      object contains the RGB definition of a system color.\n   ',
	'CombinedTermDesignResponse':'The CombinedTermDesignResponse object defines a combined-term design response.',
	'CombinedTestData':'The CombinedTestData object specifies simultaneously the normalized shear and bulk compliances or relaxation moduli as functions of time.',
	'CommandRegister':'This class allows you to derive a general class that can be queried from the GUI and is capable of notifying the GUI when the contents of the class change.',
	'CommonOptions':'The CommonOptions object stores values and attributes that are common to all plot states. The CommonOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.commonOptions member when you import the Visualization module. Abaqus creates a commonOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.commonOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.CommonOptions objects are accessed in one of two ways:    The default common options. These settings are used as defaults when other commonOptions members are created. These settings can be set to customize user preferences.The common options associated with a particular viewport.',
	'ComplexFrequencyStep':'The ComplexFrequencyStep object is used to perform eigenvalue extraction to calculate the complex eigenvalues and corresponding complex mode shapes of a system.',
	'CompositeDamping':'A CompositeDamping object contains composite modal damping parameters.',
	'CompositeDampingComponent':'A CompositeDampingComponent object is used to define composite damping over a range of modes.',
	'CompositeLayup':'The CompositeLayup object is used to specify a composite layup on a part.',
	'CompositePly':'The CompositePly object defines the material layers in a composite layup.',
	'CompositeShellSection':'The CompositeShellSection object defines the properties of a composite shell section.',
	'CompositeSolidSection':'The CompositeSolidSection object defines the properties of a composite solid section.',
	'ConcCharge':'The ConcCharge object stores the data for a concentrated charge.',
	'ConcConcFlux':'The ConcConcFlux object stores the data for a concentrated concentration flux.',
	'ConcCurrent':'The ConcCurrent object stores the data for a concentrated current.',
	'ConcCurrentState':'The ConcCurrentState object stores the propagating data of a concentrated current in a step. One instance of this object is created internally by the ConcCurrent object for each step. The instance is also deleted internally by the ConcCurrent object.The ConcCurrentState object has no constructor or methods.',
	'ConcPoreFluid':'The ConcPoreFluid object stores the data for a concentrated pore fluid flow load.',
	'ConcentratedChargeState':'The ConcentratedChargeState object stores the propagating data of a concentrated charge in a step. One instance of this object is created internally by the ConcCharge object for each step. The instance is also deleted internally by the ConcCharge object.The ConcentratedChargeState object has no constructor or methods.',
	'ConcentratedConcentrationFluxState':'The ConcentratedConcentrationFluxState object stores the propagating data of a concentrated concentration flux in a step. One instance of this object is created internally by the ConcConcFlux object for each step. The instance is also deleted internally by the ConcConcFlux object.The ConcentratedConcentrationFluxState object has no constructor or methods.',
	'ConcentratedFilmCondition':'The ConcentratedFilmCondition object defines concentrated film coefficients and associated sink temperatures.',
	'ConcentratedFilmConditionState':'The ConcentratedFilmConditionState object stores the propagating data for a ConcentratedFilmCondition object. One instance of this object is created internally by the ConcentratedFilmCondition object for each step. The instance is also deleted internally by the ConcentratedFilmCondition object.The ConcentratedFilmConditionState object has no constructor or methods.',
	'ConcentratedForce':'The ConcentratedForce object defines a concentrated force.',
	'ConcentratedForceState':'The ConcentratedForceState object stores the propagating data for a concentrated force in a step. One instance of this object is created internally by the ConcentratedForce object for each step. The instance is also deleted internally by the ConcentratedForce object.The ConcentratedForceState object has no constructor or methods.',
	'ConcentratedHeatFlux':'The ConcentratedHeatFlux object stores the data for a concentrated heat flux load.',
	'ConcentratedHeatFluxState':'The ConcentratedHeatFluxState object stores the propagating data of a concentrated heat flux load in a step. One instance of this object is created internally by the ConcentratedHeatFlux object for each step. The instance is also deleted internally by the ConcentratedHeatFlux object.The ConcentratedHeatFluxState object has no constructor or methods.',
	'ConcentratedPoreFluidState':'The ConcentratedPoreFluidState object stores the propagating data of a concentrated pore fluid flow load in a step. One instance of this object is created internally by the ConcPoreFluid object for each step. The instance is also deleted internally by the ConcPoreFluid object.The ConcentratedPoreFluidState object has no constructor or methods.',
	'ConcentratedRadiationToAmbient':'The ConcentratedRadiationToAmbient object defines radiant heat transfer between a point and its nonreflecting environment.',
	'ConcentratedRadiationToAmbientState':'The ConcentratedRadiationToAmbientState object stores the propagating data for a ConcentratedRadiationToAmbient object. One instance of this object is created internally by the ConcentratedRadiationToAmbient object for each step. The instance is also deleted internally by the ConcentratedRadiationToAmbient object.The ConcentratedRadiationToAmbientState object has no constructor or methods.',
	'Concentration':'The Concentration object stores the initial normalized concentration.',
	'ConcentrationBC':'The ConcentrationBC object stores the data for a concentration boundary condition.',
	'ConcentrationBCState':'The ConcentrationBCState object stores the propagating data for a concentration boundary condition in a step. One instance of this object is created internally by the ConcentrationBC object for each step. The instance is also deleted internally by the ConcentrationBC object.The ConcentrationBCState object has no constructor or methods.',
	'Concrete':'The Concrete object defines concrete properties beyond the elastic range.',
	'ConcreteCompressionDamage':'The ConcreteCompressionDamage object specifies hardening for the concrete damaged plasticity model.',
	'ConcreteCompressionHardening':'The ConcreteCompressionHardening object specifies hardening for the concrete damaged plasticity model.',
	'ConcreteDamagedPlasticity':'The ConcreteDamagedPlasticity object specifies the concrete damaged plasticity model.',
	'ConcreteTensionDamage':'The ConcreteTensionDamage object specifies hardening for the concrete damaged plasticity model.',
	'ConcreteTensionStiffening':'The ConcreteTensionStiffening object specifies hardening for the concrete damaged plasticity model.',
	'Conductivity':'The Conductivity object specifies thermal conductivity.',
	'ConnAccelerationBC':'The ConnAccelerationBC object stores the data for a connector acceleration boundary condition.',
	'ConnAccelerationBCState':'The ConnAccelerationBCState object stores the propagating data of a connector acceleration boundary condition in a step. One instance of this object is created internally by the ConnAccelerationBC object for each step. The instance is also deleted internally by the ConnAccelerationBC object.The ConnAccelerationBCState object has no constructor or methods.',
	'ConnDisplacementBC':'The ConnDisplacementBC object stores the data for a connector displacement/rotation boundary condition.',
	'ConnDisplacementBCState':'The ConnDisplacementBCState object stores the propagating data for a connector displacement/rotation boundary condition in a step. One instance of this object is created internally by the ConnDisplacementBC object for each step. The instance is also deleted internally by the ConnDisplacementBC object.The ConnDisplacementBCState object has no constructor or methods.',
	'ConnVelocityBC':'The ConnVelocityBC object stores the data for a connector velocity boundary condition.',
	'ConnVelocityBCState':'The ConnVelocityBCState object stores the propagating data for a velocity boundary condition in a step. One instance of this object is created internally by the ConnVelocityBC object for each step. The instance is also deleted internally by the ConnVelocityBC object.The ConnVelocityBCState object has no constructor or methods.',
	'ConnectorBehaviorOption':'The ConnectorBehaviorOption object is the abstract base type for other ConnectorBehaviorOption objects. The ConnectorBehaviorOption object has no explicit constructor. The members of the ConnectorBehaviorOption object are common to all objects derived from the ConnectorBehaviorOption.',
	'ConnectorDamage':"The ConnectorDamage object defines damage behavior for one or more components of a connector's relative motion.",
	'ConnectorDamping':"The ConnectorDamping object defines damping behavior for one or more components of a connector's relative motion.",
	'ConnectorElasticity':"The ConnectorElasticity object defines elastic behavior for one or more components of a connector's relative motion.",
	'ConnectorFailure':"The ConnectorFailure object defines failure criteria for one or more components of a connector's relative motion.",
	'ConnectorForce':'The ConnectorForce object defines a connector force.',
	'ConnectorForceState':'The ConnectorForceState object stores the propagating data for a connector force in a step. One instance of this object is created internally by the ConnectorForce object for each step. The instance is also deleted internally by the ConnectorForce object.The ConnectorForceState object has no constructor or methods.',
	'ConnectorFriction':"The ConnectorFriction object\ndefines Coulomb-like or hysteretic friction behavior for one or more components\nof a connector's relative motion.",
	'ConnectorLock':"The ConnectorLock object defines locking criteria for one or more available components of a connector's relative motion.",
	'ConnectorMoment':'The ConnectorMoment object stores the data for a connector moment.',
	'ConnectorMomentState':'The ConnectorMomentState object stores the propagating data for a connector moment in a step. One instance of this object is created internally by the ConnectorMoment object for each step. The instance is also deleted internally by the ConnectorMoment object.The ConnectorMomentState object has no constructor or methods.',
	'ConnectorOptions':'The ConnectorOptions object is used to define various options for connector behaviors. It can be used only in conjunction with CDCTerm, ConnectorDamage, ConnectorDamping, ConnectorElasticity, ConnectorFriction, and ConnectorPlasticity objects. Because the ConnectorDamage object contains two separate ConnectorOptions repositories (one for damage initiation and one for damage evolution), there are two ConnectorOptions constructors associated with that behavior&#8212;initiationOptions and evolutionOptions. The ConnectorPlasticity object also contains two separate ConnectorOptions repositories (one for isotropic hardening and one for kinematic hardening), so there are two ConnectorOptions constructors associated with that behavior&#8212;isotropicOptions and kinematicOptions.',
	'ConnectorOrientation':'The ConnectorOrientation object is used to assign a connector orientation to a connector.',
	'ConnectorPlasticity':"The ConnectorPlasticity object defines plastic behavior for one or more components of a connector's relative motion.",
	'ConnectorPotential':'The ConnectorPotential object\nis used to define a restricted set of mathematical functions to represent\nyield or limiting surfaces in the space spanned by connector available components.\nIt can be used only in conjunction with ConnectorDamage, ConnectorFriction,\nand ConnectorPlasticity objects. Because the ConnectorDamage object\ncontains two separate ConnectorPotential repositories (one for\ndamage initiation and one for damage evolution), there are two ConnectorPotential constructors\nassociated with that behavior&#8212;IniPotential and EvoPotential.',
	'ConnectorSection':'A ConnectorSection object describes the connection type and the behavior of a connector.',
	'ConnectorStop':"The ConnectorStop object defines connector stops for one or more components of a connector's relative motion.",
	'ConstrainedSketch':'A \n      ConstrainedSketch\n      object contains the entities that are used to create a sketch. The objects include \n      ConstrainedSketchGeometry\n      objects contained in the Geometry Repository, such as Line, Arc, and Spline. Vertex, Dimension, Constraint, and Parameter objects are contained in their respective repositories.\n   ',
	'ConstrainedSketchConstraint':'The \n      ConstrainedSketchConstraint\n      object stores the constraints associated with a sketch.\n   The Constraint IDs are not sequential.',
	'ConstrainedSketchDimension':'The \n      ConstrainedSketchDimension\n      object stores the dimensions associated with a sketch.\n   The dimension IDs are not sequential.',
	'ConstrainedSketchGeometry':'The \n      ConstrainedSketchGeometry\n      object stores the geometry of a sketch, such as lines, circles, arcs, and construction lines.\n   The geometry IDs are not sequential.',
	'ConstrainedSketchGeometryArray':'The \n      ConstrainedSketchGeometryArray\n      is a sequence of \n      ConstrainedSketchGeometry\n      objects.\n   The geometryIDs are not sequential.',
	'ConstrainedSketchImageOptions':'The \n      ConstrainedSketchImageOptions\n      object is used to store values and attributes associated with the background image for a particular sketch. The \n      ConstrainedSketchImageOptions\n      object has no constructor.\n   ',
	'ConstrainedSketchOptions':'The \n      ConstrainedSketchOptions\n      object is used to store values and attributes associated with a particular sketch. The \n      ConstrainedSketchOptions\n      object has no constructor.\n   ',
	'ConstrainedSketchParameter':'The \n      ConstrainedSketchParameter\n      object stores the definition of a parameter in the sketch.\n   The parameter IDs are not sequential.',
	'ConstrainedSketchVertex':'The \n      ConstrainedSketchVertex\n      object stores the vertex position.\n   The vertexIDs are not sequential.',
	'ConstrainedSketchVertexArray':'The \n      ConstrainedSketchVertexArray\n      is a sequence of \n      ConstrainedSketchVertex\n      objects.\n   The vertexIDs are not sequential.',
	'ConstrainedSketcherOptions':'The \n      ConstrainedSketcherOptions\n      object is used to store values and attributes which will be applied to all sketches used in the current session. The \n      ConstrainedSketcherOptions\n      object has no constructor.\n   ',
	'Constraint':'The Constraint object is the abstract base type for other Constraint objects. The Constraint object has no explicit constructor. The members of the Constraint object are common to all objects derived from the Constraint.',
	'ConstraintDisplayOptions':'The ConstraintDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.constraints=ONThe ConstraintDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'ContactArea':'A ContactArea object specifies a suboption of gasket thickness behavior when variableUnits=FORCE on the GasketThicknessBehavior object. The ContactArea object defines the contact area or contact width versus closure curves to output an average pressure through variable CS11.',
	'ContactControl':'The ContactControl object is the abstract base type for other ContactControl objects. The ContactControl object has no explicit constructor, members, or methods.',
	'ContactDamage':'The ContactDamage object specifies damage options for a contact interaction property.',
	'ContactDamping':'The ContactDamping object specifies damping for a contact interaction property.',
	'ContactExp':'The ContactExp object defines the contact domain and associated properties during contact in an Abaqus/Explicit analysis.',
	'ContactInitialization':'The ContactInitialization object is the abstract base type for other ContactInitialization objects. The ContactInitialization object has no explicit constructor, members, or methods.',
	'ContactProperty':'The ContactProperty object defines a contact interaction property.',
	'ContactPropertyAssignment':'The ContactPropertyAssignment object stores the contact property assignment definition for domain pairs in ContactExp and ContactStd objects. The ContactPropertyAssignment object has no constructor or members.',
	'ContactStabilization':'The ContactStabilization object is the abstract base type for other ContactStabilization objects. The ContactStabilization object has no explicit constructor, members, or methods.',
	'ContactStd':'The ContactStd object defines the contact domain and associated properties during contact in an Abaqus/Standard analysis.',
	'ContactTangentialBehavior':'The ContactTangentialBehavior object specifies tangential behavior for a contact interaction property.',
	'ContourIntegral':'The ContourIntegral object defines contour integral objects on an region. Currently only assembly regions are supported.',
	'ContourOptions':'The ContourOptions object stores values and attributes associated with a contour plot. The ContourOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.contourOptions member when you import the Visualization module. Abaqus creates a contourOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.contourOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.ContourOptions objects are accessed in one of two ways:The default contour options. These settings are used as defaults when other contourOptions members are created. These settings can be set to customize user preferences.The contour options associated with a particular viewport.',
	'Control':'The Control object is used to provide additional optional general solution controls.Note that controls are unavailable in Explicit Dynamics and Static, Linear Perturbation steps.',
	'CoriolisForce':'The CoriolisForce object stores the data for a coriolis force.',
	'CoriolisForceState':'The CoriolisForceState object stores the propagating data of a coriolis force in a step. One instance of this object is created internally by the CoriolisForce object for each step. The instance is also deleted internally by the CoriolisForce object.The CoriolisForceState object has no constructor or methods.',
	'Correlation':'A Correlation is an object used to define the cross-correlation as part of the definition of random loading.',
	'CoupledTempDisplacementStep':'The CoupledTempDisplacementStep object is used to analyze problems where the simultaneous solution of the temperature and stress/displacement fields is necessary.',
	'CoupledThermalElectricStep':'The CoupledThermalElectricStep object is used to analyze problems where the electrical potential and temperature fields must be solved simultaneously.',
	'CoupledThermalElectricalStructuralStep':'The CoupledThermalElectricalStructuralStep object is used to analyze problems where the simultaneous solution of the temperature, stress/displacement and electrical fields is necessary.',
	'Coupling':'The Coupling object defines a constraint between a group of coupling nodes located on a region and a reference point.',
	'Crack':'The Crack object is the abstract base type for ContourIntegral and future crack objects.',
	'Creep':'The Creep object defines a creep law.',
	'CrushableFoam':'The CrushableFoam object specifies the crushable foam plasticity model.',
	'CrushableFoamHardening':'The CrushableFoamHardening object specifies hardening for the crushable foam plasticity model.',
	'CurrentProbeValues':'The CurrentProbeValues object has no constructor. The CurrentProbeValues object is created when you import the Visualization module.',
	'CycledPlastic':'The CycledPlastic object specifies cycled yield stress data for the ORNL constitutive model.',
	'CyclicHardening':'The CyclicHardening object defines the evolution of the elastic domain for the nonlinear isotropic/kinematic hardening model.',
	'CyclicSymmetry':'The CyclicSymmetry object defines a cyclic symmetry analysis.',
	'CyclicSymmetryState':'The CyclicSymmetryState object stores the propagating data for a CyclicSymmetry object. One instance of this object is created internally by the CyclicSymmetry object for each step. The instance is also deleted internally by the CyclicSymmetry object.The CyclicSymmetryState object has no constructor or methods.',
	'DGCommonOptions':'The DGCommonOptions object stores values and attributes that are common to all plot states. The DGCommonOptions object has no constructor command. Abaqus creates an odbDisplayOptions.commonOptions member when a display group instance is created, using values from odbDisplay.commonOptions.',
	'DGContourOptions':'The DGContourOptions object stores values and attributes associated with a contour plot. The DGContourOptions object has no constructor command. Abaqus creates an odbDisplayOptions.contourOptions member when a display group instance is created, using values from odbDisplay.contourOptions.',
	'DGDisplayBodyOptions':'The DGDisplayBodyOptions object stores values and attributes applied to display bodies. The DGDisplayBodyOptions object has no constructor command. Abaqus creates an odbDisplayOptions.displayBodyOptions member when a display group instance is created, using values from odbDisplay.displayBodyOptions.',
	'DGOrientationOptions':'The DGOrientationOptions object stores values and attributes associated with a material orientation plot. The DGOrientationOptions object has no constructor command. Abaqus creates an odbDisplayOptions.materialOrientationOptions member when a display group instance is created, using values from odbDisplay.materialOrientationOptions.',
	'DGSuperimposeOptions':'The DGSuperimposeOptions object stores values and attributes associated with the undeformed shape when the display contains both the deformed shape and the undeformed shape. The DGSuperimposeOptions object has no constructor command. Abaqus creates an odbDisplayOptions.superimposeOptions member when a display group instance is created, using values from odbDisplay.superimposeOptions.',
	'DGSymbolOptions':'The DGSymbolOptions object stores values and attributes associated with a symbol plot. The DGSymbolOptions object has no constructor command. Abaqus creates an odbDisplayOptions.symbolOptions member when a display group instance is created, using values from odbDisplay.symbolOptions.',
	'DamageEvolution':'The DamageEvolution object specifies material properties to define the evolution of damage.',
	'DamageInitiation':'The DamageInitiation object specifies material properties to define the initiation of damage.',
	'DamageStabilization':'The DamageStabilization object specifies the viscosity coefficients for the damage model for fiber-reinforced materials.',
	'DamageStabilizationCohesive':'The DamageStabilizationCohesive object specifies the viscosity coefficients for the damage model for surface-based cohesive behavior or enriched cohesive behavior.',
	'Damping':'The Damping object specifies material damping.',
	'DataObject':'An instance of the DataObject object is passed to each callback. The DataObject object has no methods. The members of a DataObject object depend on the type of the object. All DataObject instances have the following members, regardless of type:clientHostclientNamephaseprocessIdthreadIdtimeStampThe possible DataObject types and the additional members for each type are as follows: ABORTEDmessageCOMPLETEDmessageEND_STEPstepIdERRORmessageHEADINGheadingMONITOR_DATAdofnodensetproceduretimevalueODB_FILEfileSTARTEDNo additional members.STATUSattemptsequilibriumincrementiterationsseverestepstepTimetimeIncrementtotalTimeSTEPstepIdstepNameWARNINGmessage',
	'DataSet':'The \n      DataSet\n      object specifies material test data.\n   ',
	'DataTable':'A DataTable is an object used to define the domain and data for a DiscreteField.\n   ',
	'Datum':'The Datum object is the abstract base type for other Datum objects. The Datum object has no explicit constructor. The methods and members of the Datum object are common to all objects derived from the Datum.',
	'DatumAxis':'The DatumAxis object has no direct constructor; it is created when a Feature object is created. For example, the DatumAxisByCylFace method creates a Feature object that creates a DatumAxis object. ',
	'DatumCsys':'The DatumCsys object has no direct constructor; it is created when a Feature object is created. For example, the DatumCsysByOffset method creates a Feature object that creates a DatumCsys object. ',
	'DatumPlane':'The DatumPlane object has no direct constructor; it is created when a Feature object is created. For example, the DatumPlaneByPrincipalPlane method creates a Feature object that creates a DatumPlane object.',
	'DatumPoint':'The DatumPoint object has no direct constructor; it is created when a Feature object is created. For example, the DatumPointByCoordinate method creates a Feature object that creates a DatumPoint object.',
	'DecayAmplitude':'The DecayAmplitude object defines an amplitude curve using an exponential decay.',
	'DefaultChartOptions':'The DefaultChartOptions object is used to hold on default chart and axis attributes. The DefaultChartOptions object attributes are used whenever Chart or Axis are created. A DefaultChartOptions object is automatically created when opening a session.',
	'DefaultOdbDisplay':'The DefaultOdbDisplay object is a limited-functionality version of the OdbDisplay object.',
	'DefaultPlot':'The DefaultPlot object is used to hold on default plot attributes. The DefaultPlot object attributes are used whenever an XYPlot object is created. A DefaultPlot object is automatically created when opening a session.',
	'DeformationPlasticity':'The DeformationPlasticity object specifies the deformation plasticity model.',
	'Density':'The Density object specifies the material density.',
	'Depvar':'The Depvar object specifies solution-dependent state variables.',
	'DerivedComponent':'A DerivedComponent object describes user-customized components for use in defining ConnectorFriction and Potential objects.',
	'DesignDirection':'The DesignDirection object defines a design direction geometric restriction.',
	'DesignResponse':'The DesignResponse object is the abstract base type for other DesignResponse objects. The DesponseResponse object has no explicit constructor. The methods and members of the DesignResponse object are common to all objects derived from DesignResponse.',
	'DetailPlotOptions':'The DetailPlotOptions object stores values and attributes associated with a Viewport object. The DetailPlotOptions object has no constructor command. Abaqus creates the detailPlotOptions member whenever a Viewport is created.',
	'DetonationPoint':'A DetonationPoint object specifies a suboption of the Eos object. The DetonationPoint object defines either isotropic linear elastic shear or linear viscous shear behavior for a hydrodynamic material.',
	'DiagnosticPrint':'The DiagnosticPrint object is used to request detailed diagnostic output or to disable specific diagnostic checks.',
	'Dielectric':'The Dielectric object specifies dielectric material properties.',
	'Diffusivity':'The Diffusivity object specifies mass diffusivity.',
	'DirectCyclicStep':'The DirectCyclicStep object is used to provide a direct cyclic procedure for nonlinear, non-isothermal quasi-static analysis. It can also be used to predict progressive damage and failure for ductile bulk materials and/or to predict delamination/debonding growth at the interfaces in laminated composites in a low-cycle fatigue analysis.',
	'DirectDamping':'A DirectDamping object contains direct modal damping parameters.',
	'DirectDampingByFrequency':'A DirectDampingByFrequency object contains direct damping parameters.',
	'DirectDampingByFrequencyComponent':'A DirectDampingByFrequencyComponent object is used to define direct damping over a range of frequencies.',
	'DirectDampingComponent':'A DirectDampingComponent object is used to define direct damping over a range of modes.',
	'DiscreteFastener':'The DiscreteFastener object defines a discrete fastener.',
	'DiscreteField':'The DiscreteField object defines a varying field whose values correspond to distinct points within a domain.',
	'DisplacementAdaptiveMeshConstraint':'The DisplacementAdaptiveMeshConstraint object stores the data for an Arbitrary Lagrangian Eularian (ALE) style displacement/rotation adaptive mesh constraint.',
	'DisplacementAdaptiveMeshConstraintState':'The DisplacementAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary Lagrangian Eularian (ALE) style displacement/rotation adaptive mesh constraint in a step. One instance of this object is created internally by the DisplacementAdaptiveMeshConstraint object for each step. The instance is also deleted internally by the DisplacementAdaptiveMeshConstraint object.The DisplacementAdaptiveMeshConstraintState object has no constructor or methods.',
	'DisplacementBC':'The DisplacementBC object stores the data for a displacement/rotation boundary condition.',
	'DisplacementBCState':'The DisplacementBCState object stores the propagating data for a displacement/rotation boundary condition in a step. One instance of this object is created internally by the DisplacementBC object for each step. The instance is also deleted internally by the DisplacementBC object.The DisplacementBCState object has no constructor or methods.',
	'DisplacementBaseMotionBC':'The DisplacementBaseMotionBC object stores the data for a displacement base motion boundary condition.',
	'DisplacementBaseMotionBCState':'The DisplacementBaseMotionBCState object stores the propagating data for a velocity base motion boundary condition in a step. One instance of this object is created internally by the DisplacementBaseMotionBC object for each step. The instance is also deleted internally by the DisplacementBaseMotionBC object.The DisplacementBaseMotionBCState object has no constructor or methods.',
	'DisplayBody':'The DisplayBody object defines a constraint such that the specified instance is used for display only and does not take part in the analysis. However it will still be visible during postprocessing and its position at any frame will be defined by the translation and rotation of the specified control points.',
	'DisplayBodyOptions':'The DisplayBodyOptions object stores values and attributes that are common to all plot states. The DisplayBodyOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.displayBodyOptions member when you import the Visualization module. Abaqus creates a displayBodyOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.displayBodyOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.DisplayBodyOptions objects are accessed in one of two ways:    The default display body options. These settings are used as defaults when other displayBodyOptions members are created. These settings can be set to customize user preferences.The display body options associated with a particular viewport.',
	'DisplayGroup':'DisplayGroup objects are used to select a subset of the entities displayed in the viewport. ',
	'DisplayGroupInstance':'A DisplayGroupInstance object stores the IDs of the entities displayed in a viewport. The DisplayGroupInstance object has no constructor. When you set a display group to be plotted in a viewport, Abaqus/CAE creates a DisplayGroupInstance object for each display group and places it in the DisplayGroupInstanceRepository object.',
	'DisplayGroupInstanceRepository':'The DisplayGroupInstanceRepository object stores DisplayGroupInstance objects. In addition to all the standard Python repository methods, the DisplayGroupInstance repository defines additional methods as described below.',
	'DisplayOptions':'The DisplayOptions object stores a plot state.',
	'Displayable':'',
	'Drawing':'A drawing is the container for a geometric object. The \n      Drawing\n      object stores the vertex data and various settings that determine how the drawing will be displayed.\n   ',
	'DrawingArea':'The \n      DrawingArea \n      object specifies the location and size of the drawing area used for placement of viewports.\n      ',
	'DrillControl':'The DrillControl object defines a drill control geometric restriction.',
	'DruckerPrager':'The DruckerPrager object specifies the extended Drucker-Prager plasticity model.',
	'DruckerPragerCreep':'The DruckerPragerCreep object specifies creep for Drucker-Prager plasticity models.',
	'DruckerPragerHardening':'The DruckerPragerHardening object specifies hardening for Drucker-Prager plasticity models.',
	'Edge':'Edges are one-dimensional regions of geometry.',
	'EdgeArray':'The EdgeArray is a sequence of \n      Edge \n      objects.\n   ',
	'Elastic':'The Elastic object specifies elastic material properties.',
	'ElasticFoundation':'The ElasticFoundation object defines a mechanical foundation.',
	'ElasticFoundationState':'The ElasticFoundationState object stores the propagating data for an ElasticFoundation object. One instance of this object is created internally by the ElasticFoundation object for each step. The instance is also deleted internally by the ElasticFoundation object.The ElasticFoundationState object has no constructor or methods.',
	'ElectricPotentialBC':'The ElectricPotentialBC object stores the data for an electrical potential boundary condition.',
	'ElectricPotentialBCState':'The ElectricPotentialBCState object stores the propagating data for a electrical potential boundary condition in a step. One instance of this object is created internally by the ElectricPotentialBC object for each step. The instance is also deleted internally by the ElectricPotentialBC object.The ElectricPotentialBCState object has no constructor or methods.',
	'ElectricalConductance':'The ElectricalConductance object specifies electrical conductance for a contact interaction property.',
	'ElectricalConductivity':'The ElectricalConductivity object specifies electrical conductivity.',
	'ElemType':'The ElemType object is an argument object used as an argument in the setElementType command.',
	'EmagTimeHarmonicFrequency':'A EmagTimeHarmonicFrequency is an object used to define frequency over range of modes.',
	'EmagTimeHarmonicStep':'The EmagTimeHarmonicStep object is used to calculate the electromagnetic response of the system to harmonic excitation of the model. ',
	'EmbeddedRegion':'The EmbeddedRegion object allows you to embed a region of the model within a &#8220;host&#8221; region of the model or within the whole model.',
	'EngineeringFeature':'The EngineeringFeature object is a container for various specific engineering feature repositories. The EngineeringFeature object has no explicit constructor or methods.',
	'EngineeringFeatureDisplayOptions':'The EngineeringFeatureDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport whensession.viewports[name].assemblyDisplay.engineeringFeatures=ONThe EngineeringFeatureDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'Eos':' The Eos object specifies an equation of state model.\n    ',
	'EosCompaction':'The EosCompaction object specifies material eos compaction.',
	'EpsOptions':'The EpsOptions object stores the settings that Abaqus uses when printing using Encapsulated PostScript format. The \n      EpsOptions\n      object has no constructor. Abaqus creates the \n      epsOptions\n      member when a session is started.\n   ',
	'EquallySpacedAmplitude':'The EquallySpacedAmplitude object defines a list of amplitude values at fixed time intervals beginning at a specified value of time.',
	'Equation':'The Equation object defines a linear multi-point constraint between a set of degrees of freedom.',
	'ErrorIndicatorResult':'The ErrorIndicatorResult object contains result information corresponding to an error indicator variable in a RemeshingRule object for an adaptivity iteration.',
	'EulerianBC':'The EulerianBC object stores the data for an Eulerian boundary condition.',
	'EulerianBCState':'The EulerianBCState object stores the propagating data for an Eulerian boundary condition in a step. One instance of this object is created internally by the EulerianBC object for each step. The instance is also deleted internally by the EulerianBC object.The EulerianBCState object has no constructor or methods.',
	'EulerianMotionBC':'The EulerianMotionBC object stores the data for an Eulerian mesh motion boundary condition.',
	'EulerianMotionBCState':'The EulerianMotionBCState object stores the propagating data for an Eulerian mesh motion boundary condition in a step. One instance of this object is created internally by the EulerianMotionBC object for each step. The instance is also deleted internally by the EulerianMotionBC object.The EulerianMotionBCState object has no constructor or methods.',
	'EulerianSection':'The EulerianSection object defines the properties of a Eulerian section.',
	'ExpContactControl':'The ExpContactControl object is used in Abaqus/Explicit analyses to specify optional solution controls for problems involving contact between bodies.',
	'Expansion':'The Expansion object specifies thermal expansion.',
	'ExplicitDynamicsStep':'The ExplicitDynamicsStep object is used to perform a dynamic stress/displacement analysis using explicit integration in Abaqus/Explicit.',
	'ExpressionField':'The ExpressionField object defines a spatially varying field whose value is calculated from a user-supplied mathematical expression.',
	'Face':'Faces are two-dimensional regions of geometry.',
	'FaceArray':'The FaceArray is a sequence of \n      Face \n      objects.\n   ',
	'FailStrain':'The FailStrain object defines parameters for strain-based failure measures.',
	'FailStress':'The FailStress object defines parameters for stress-based failure measures.',
	'FailureRatios':'The FailureRatios object specifies the shape of the failure surface for a Concrete model.',
	'Fastener':'The Fastener object is the abstract base type for PointFastener, DiscreteFastener, and AssembledFastener.',
	'Feature':'Abaqus/CAE is a feature-based modeling system, and features are stored in the Feature object. The user defines the parameters of the feature, and Abaqus/CAE modifies the model based on the value of the parameters. This evaluation of the parameters is called regeneration of the feature. Feature objects contain both the parameters and the resulting model modification. ',
	'FeatureOptions':'The FeatureOptions object stores the options that control the behavior of feature regeneration for all features in a model.',
	'Field':'The Field object is the abstract base type for other Field objects. The Field object has no explicit constructor. The methods and members of the Field object are common to all objects derived from the Field.',
	'FieldBulkData':'The \n      FieldBulkData \n      object represents the entire field data for a class of elements or nodes. All elements in a class correspond to the same element type and material.\n   ',
	'FieldLocation':'The FieldLocation object specifies locations for which data are available in the field. For example, a displacement field will have a FieldLocation object with a position member value of NODAL. The FieldLocation object has no constructor; it is created automatically as an element of the location member of a FieldOutput object by the addData method of a FieldOutput object.',
	'FieldOutput':'A \n      FieldOutput\n      object contains field data for a specific output variable.\n   ',
	'FieldOutputRequest':'The FieldOutputRequest object defines a field output request.',
	'FieldOutputRequestState':'The FieldOutputRequestState object stores the propagating data of a field output request current in a step. One instance of this object is created internally by the FieldOutputRequest object for each step. The instance is also deleted internally by the FieldOutputRequest object.The FieldOutputRequestState object has no constructor or methods.',
	'FieldReportOptions':'The FieldReportOptions object stores settings used by the writeFieldReport method when you write a FieldOutput object to an ASCII file. The FieldReportOptions object has no constructor. Abaqus creates the fieldReportOptions member when you import the Visualization module.The FieldReportOptions object is accessed in two ways:The default field report options. These settings are used as defaults when you create a FieldReportOptions object. These settings can be set to customize user preferences.The field report options used by the writeFieldReport method.',
	'FieldValue':'The FieldValue object represents the field data at a point. The FieldValue object has no constructor; it is created by the Odb object when data are added to the FieldOutput object using the addData method. For faster, bulk-data access, see .',
	'FilmCondition':'The FilmCondition object defines film coefficients and associated sink temperatures for coupled temperature-displacement analyses.',
	'FilmConditionProp':'The FilmConditionProp object is an interaction property that defines a film coefficient as a function of temperature and field variables.',
	'FilmConditionState':'The FilmConditionState object stores the propagating data for a FilmCondition object. One instance of this object is created internally by the FilmCondition object for each step. The instance is also deleted internally by the FilmCondition object.The FilmConditionState object has no constructor or methods.',
	'Filter':'The Filter object is the abstract base type for other Filter objects. The Filter object has no explicit constructor. The methods and members of the Filter object are common to all objects derived from the Filter.',
	'FixedRegion':'The FixedRegion object defines a fixed region geometric restriction.',
	'FlowStep':'The FlowStep object is used to create an analysis step for use in a CFD analysis.',
	'FluidCavity':'The FluidCavity object defines a surface-based cavity.',
	'FluidCavityPressure':'The FluidCavityPressure object stores the data for initial fluid cavity pressures.  The base classregion argument can not be specifed with this object.',
	'FluidCavityPressureBC':'The FluidCavityPressureBC object stores the data for a fluid cavity pressure boundary condition.',
	'FluidCavityPressureBCState':'The FluidCavityPressureBCState object stores the propagating data for a fluid cavity pressure boundary condition in a step. One instance of this object is created internally by the FluidCavityPressureBC object for each step. The instance is also deleted internally by the FluidCavityPressureBC object.The FluidCavityPressureBCState object has no constructor or methods.',
	'FluidCavityProperty':'The FluidCavityProperty object is an interaction property that defines the fluid behavior for a surface-based fluid cavity.',
	'FluidCavityState':'The FluidCavityState object stores the propagating data for an FluidCavity object. One instance of this object is created internally by the FluidCavity object for each step. The instance is also deleted internally by the FluidCavity object.The FluidCavityState object has no constructor or methods.',
	'FluidDensity':'The FluidDensity object stores the data for fluid density predefined fields.',
	'FluidExchange':'The FluidExchange object is used to define fluid exchange between two fluid cavities or between a fluid cavity and its environment.',
	'FluidExchangeProperty':'The FluidExchangeProperty object is an interaction property that defines the fluid exchange property for a flow between two fluid cavities or between a fluid cavity and its environment.',
	'FluidExchangeState':'The FluidExchangeState object stores the propagating data for an FluidExchange object. One instance of this object is created internally by the FluidExchange object for each step. The instance is also deleted internally by the FluidExchange object.The FluidExchangeState object has no constructor or methods.',
	'FluidInletOutletBC':'The FluidInletOutletBC object stores the data for a fluid inlet/outlet boundary condition.',
	'FluidInletOutletBCState':'The FluidInletOutletBCState object stores the propagating data of a fluid inlet/outlet boundary condition in a step. One instance of this object is created internally by the FluidInletOutletBC object for each step. The instance is also deleted internally by the FluidInletOutletBC object.The FluidInletOutletBCState object has no constructor or methods.',
	'FluidLeakoff':'The FluidLeakoff object specifies leak-off coefficients for pore pressure cohesive elements.',
	'FluidThermalEnergy':'The FluidThermalEnergy object stores the data for fluid thermal energy predefined fields. This predefined field is applicable only when an energy equation has been selected in a flow step.',
	'FluidTurbulence':'The FluidTurbulence object stores the data for fluid turbulence predefined fields. This predefined field is applicable only when a turbulence model has been selected in a flow step.',
	'FluidVelocity':'The FluidVelocity object stores the data for fluid velocity Predefined fields.',
	'FluidWallConditionBC':'The FluidWallConditionBC object stores the data for a fluid wall condition boundary condition.',
	'FluidWallConditionBCState':'The FluidWallConditionBCState object stores the propagating data of a fluid wall condition boundary condition in a step. One instance of this object is created internally by the FluidWallConditionBC object for each step. The instance is also deleted internally by the FluidWallConditionBC object.The FluidWallConditionBCState object has no constructor or methods.',
	'FractureCriterion':' The FractureCriterion object specifies fractureCriterion options for a contact interaction property.',
	'FreeBody':'The FreeBody object defines a section across which resultant forces and moments are computed.',
	'FreeBodyOptions':'The FreeBodyOptions object stores values and attributes associated with a free body plot. The FreeBodyOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.freeBodyOptions member when you import the Visualization module. Abaqus creates a FreeBodyOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.freeBodyOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.FreeBodyOptions objects are accessed in one of two ways:The default free body options. These settings are used as defaults when other freeBodyOptions members are created. These settings can be set to customize user preferences.The free body options associated with a particular viewport.',
	'FreeBodyReportOptions':'The FreeBodyReportOptions object stores settings used by the writeFreeBodyReport method when you write free body computational results to an ASCII file. The FreeBodyReportOptions object has no constructor. Abaqus creates the freeBodyReportOptions member when you import the Visualization module.The FreeBodyReportOptions object is accessed in two ways:The default free body report options. These settings are used as defaults when you create a FreeBodyReportOptions object. These settings can be set to customize user preferences.The free body report options used by the writeFreeBodyReport method.',
	'FrequencyStep':'The FrequencyStep object is used to perform eigenvalue extraction to calculate the natural frequencies and corresponding mode shapes of a system.',
	'FrozenArea':'The FrozenArea object defines a frozen area geometric restriction.',
	'GapElectricalConductance':'The GapElectricalConductance object specifies electrical conductance for a contact interaction property.',
	'GapFlow':'The GapFlow object specifies tangential flow constitutive parameters for pore pressure cohesive elements.',
	'GapHeatGeneration':'The GapHeatGeneration object specifies heat generation for a contact interaction property.',
	'GasketMembraneElastic':'The GasketMembraneElastic object defines the elastic parameters for the membrane shear behavior of a gasket.',
	'GasketSection':'The GasketSection object defines the properties of a gasket section.',
	'GasketThicknessBehavior':'The GasketThicknessBehavior object defines the behavior in the thickness direction for a gasket.',
	'GasketTransverseShearElastic':'The GasketTransverseShearElastic object defines the elastic parameters for the transverse shear behavior of a gasket.',
	'Gel':'The Gel object defines a swelling gel.',
	'GeneralField':'The GeneralField object stores a general predefined field.',
	'GeneralFieldState':'The GeneralFieldState object stores the propagating data of a GeneralField in a step. One instance of this object is created internally by the GeneralField object for each step. The instance is also deleted internally by the GeneralField object.The GeneralFieldState object has no constructor or methods.',
	'GeneralStiffnessSection':'The GeneralStiffnessSection object defines the properties of a shell section via the stiffness matrix.',
	'GeneralizedProfile':'The GeneralizedProfile object defines the properties of a profile via its area, moment of inertia, etc.',
	'GeometricProperties':'The GeometricProperties object specifies surface interaction properties.',
	'GeometricRestriction':'The GeometricRestriction object is the abstract base type for other GeometricRestriction objects. The GeometricRestriction object has no explicit constructor. The methods and members of the GeometricRestriction object are common to all objects derived from GeometricRestriction.',
	'GeometricRestrictionDisplayOptions':'The GeometricRestrictionDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.geometricRestrictions=ONThe GeometricRestrictionDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'GeometryDisplayOptions':'The GeometryDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport. The GeometryDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'GeometryShellSection':'The GeometryShellSection object defines the properties of a geometry shell section. The GeometryShellSection object has no explicit constructor and no methods. The GeometryShellSection object is an abstract base type.',
	'GeostaticStep':'The GeostaticStep object is used to verify that the geostatic stress field is in equilibrium with the applied loads and boundary conditions on the model and to iterate, if needed, to obtain equilibrium.',
	'GraphicsInfo':'The \n      GraphicsInfo \n      object stores information about the graphics adapter installed in your system. The \n      GraphicsInfo \n      object has no constructor or methods; Abaqus creates the \n      GraphicsInfo \n      member when a session is started.\n   If you execute Abaqus/CAE on a remote system and display the main window locally, the \n      glx server \n      is your local machine and the \n      glx client \n      is the remote machine. This definition of client and server follows the X11 naming convention. If you execute and display Abaqus/CAE on the same machine, you will typically see identical values for both the name of the server and the name of the client.\n   The members are all read-only.',
	'GraphicsOptions':'The \n      GraphicsOptions \n      object stores settings that control how objects are rendered in all viewports. \n      GraphicsOptions \n      objects are accessed in one of two ways:\n      The default graphics options. These settings are used as defaults when you start a session and by the \n    Defaults \n    button on the \n    Graphics Options \n    dialog box.\n The current graphics options.The \n      GraphicsOptions \n      object has no constructor; Abaqus creates both the \n      defaultGraphicsOptions \n      and the \n      graphicsOptions \n      members when a session is started.\n   When you start a session, Abaqus detects the graphics hardware installed on your system and uses the \n      setValues \n      method in the environment file (\n      abaqus_v6.env\n      ) to modify the members of the \n      GraphicsOptions \n      object. If your graphics hardware is not supported by Abaqus/CAE, or if you wish to override the default graphics options, you can modify settings in the environment file. For more information, see \n      .\n   ',
	'Gravity':'The Gravity object stores the data of a gravity load.',
	'GravityState':'The GravityState object stores the propagating data for a gravity load in a step. One instance of this object is created internally by the Gravity object for each step. The instance is also deleted internally by the Gravity object.The GravityState object has no constructor or methods.',
	'Growth':'The Growth object defines a growth geometric restriction.',
	'HeatCapacitance':'The HeatCapacitance object defines point heat capacitance on a part or an assembly region.',
	'HeatGeneration':'The HeatGeneration object includes volumetric heat generation in heat transfer analyses.',
	'HeatTransferStep':'The HeatTransferStep object is used to control uncoupled heat transfer for either transient or steady-state response.',
	'HexagonalProfile':'The HexagonalProfile object defines the properties of a hexagonal profile.',
	'HistoryOutput':'The HistoryOutput object contains the history output at a point for the specified variable.',
	'HistoryOutputRequest':'The HistoryOutputRequest object defines a history output request.',
	'HistoryOutputRequestState':'The HistoryOutputRequestState object stores the propagating data of a History output request current in a step. One instance of this object is created internally by the HistoryOutputRequest object for each step. The instance is also deleted internally by the HistoryOutputRequest object.The HistoryOutputRequestState object has no constructor or methods.',
	'HistoryPoint':'The HistoryPoint object specifies the point at which history data will be collected. The HistoryPoint object is a temporary object used as an argument to the HistoryRegion method.',
	'HistoryRegion':'The HistoryRegion object contains history data for a single location in the model.',
	'HistoryVariable':'The HistoryVariable object stores history data.',
	'HomogeneousShellSection':'The HomogeneousShellSection object defines the properties of a shell section.',
	'HomogeneousSolidSection':'The HomogeneousSolidSection object defines the properties of a solid section.',
	'HydrostaticFluidFlow':'The HydrostaticFluidFlow object defines a change in the amount of fluid in a fluid-filled cavity modeled with hydrostatic fluid elements.',
	'HydrostaticFluidFlowState':'The HydrostaticFluidFlowState object stores the propagating data for a concentrated HydrostaticFluidFlow object in a step. One instance of this object is created internally by the HydrostaticFluidFlow object for each step. The instance is also deleted internally by the HydrostaticFluidFlow object.The HydrostaticFluidFlowState object has no constructor or methods.',
	'Hyperelastic':'The Hyperelastic object specifies elastic properties for approximately incompressible elastomers.',
	'Hyperfoam':'The Hyperfoam object specifies elastic properties for a hyperelastic foam.',
	'Hypoelastic':'The Hypoelastic object specifies hypoelastic material properties.',
	'Hysteresis':'The Hysteresis object specifies the creep part of the material model for the hysteretic behavior of elastomers.',
	'IMAField':'A IMAField is an object used to define material instance name volume fractions for the MaterialAssignment predefined field.',
	'IMARegion':'A IMARegion is an object used to define material instance name volume fractions for the MaterialAssignment predefined field.',
	'IProfile':'The IProfile object defines the properties of an I profile.',
	'IgnoredEdge':'An IgnoredEdge object is a one-dimensional region of geometry that has been abstracted away by a virtual topology feature.',
	'IgnoredEdgeArray':'The IgnoredEdgeArray is a sequence of \n      IgnoredEdge \n      objects.\n   ',
	'IgnoredVertex':'An IgnoredVertex object is a point region of the geometry that was abstracted away by a virtual topology feature.',
	'IgnoredVertexArray':'The IgnoredVertexArray is a sequence of \n      IgnoredVertex \n      objects.\n   ',
	'Image':'The \n      Image\n      object is used to store color values and attributes associated with a raster file. Upon creation, the \n      Image\n      object is added to the \n      session.images\n      repository.\n   ',
	'ImageAnimation':'The ImageAnimation object is used to build frame by frame animation.',
	'ImageAnimationOptions':'The ImageAnimationOptions object is used to store values and attributes associated with saving viewport animations. The ImageAnimationOptions object has no constructor. Abaqus creates the imageAnimationOptions member when the animation module is imported.',
	'ImageOptions':'The \n      ImageOptions \n      object stores settings that control  how an image is rendered in a particular viewport. \n      ImageOptions \n      objects are accessed from the image options associated with a particular viewport.\n   The \n      ImageOptions \n      object has no constructor; Abaqus creates the \n      imageOptions \n      member for a viewport when the viewport is created using the values in the \n      imageOptions \n      member of the current viewport.\n   ',
	'ImplicitDynamicsStep':'The ImplicitDynamicsStep object is used to provide direct integration of a dynamic stress/displacement response in Abaqus/Standard analyses and is generally used for nonlinear cases.',
	'IncidentWave':'The IncidentWave object defines incident wave interactions for acoustic and coupled acoustic-structural analyses.',
	'IncidentWaveProperty':'The IncidentWaveProperty object is an interaction property that defines the properties referred to by an IncidentWave object.',
	'IncidentWaveState':'The IncidentWaveState object stores the propagating data of an IncidentWave object in a step. One instance of this object is created internally by the IncidentWave object for each step. The instance is also deleted internally by the IncidentWave object.The IncidentWaveState object has no constructor or methods.',
	'InelasticHeatFraction':'The InelasticHeatFraction object defines the fraction of the rate of inelastic dissipation that appears as a heat source.',
	'Inertia':'The Inertia object is the abstract base type for HeatCapacitance, NonstructuralMass, and PointMassInertia.',
	'InertiaRelief':'The InertiaRelief object defines an inertia relief load.',
	'InertiaReliefState':'The InertiaReliefState object stores the propagating data for an inertia relief load in a step. One instance of this object is created internally by the InertiaRelief object for each step. The instance is also deleted internally by the InertiaRelief object.The InertiaReliefState object has no constructor or methods.',
	'InitialState':'The InitialState object stores the data for an initial state predefined field.',
	'InitialStep':'The InitialStep object is a placeholder that you cannot create, delete, or modify. The InitialStep object exists in every model by default and is used to allow the preexisting boundary conditions and interactions to be defined in the model.',
	'InitializationAssignment':'The InitializationAssignment object stores the contact initialization assignment definition for domain pairs in a ContactStd object. The InitializationAssignment object has no constructor or members.',
	'IntegratedOutputSection':'The IntegratedOutputSection object specifies parameters used for integrated output.',
	'Interaction':'The Interaction object is the abstract base type for other Interaction objects. The Interaction object has no explicit constructor. Each of the Interaction objects has the following methods:deactivatemoveresetresumesuppressdeleteThe methods are described below.',
	'InteractionDisplayOptions':'The InteractionDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport whensession.viewports[name].assemblyDisplay.interactions=ONThe InteractionDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'InteractionProperty':'The InteractionProperty object is the abstract base type for other InteractionProperty objects. The InteractionProperty object has no explicit constructor, members, or methods.',
	'InteractionState':'The InteractionState object is the abstract base type for other InteractionState objects. The InteractionState object has no explicit constructor. The members of the InteractionState object are common to all objects derived from InteractionState.',
	'InterestingPoint':'Interesting points can be located at the following:\n      The middle of an edge.The middle of an arc.The center of an arc.\n      An \n      InterestingPoint \n      object is a temporary object and cannot be accessed from the \n      Mdb \n      object.\n   ',
	'InwardVolAccel':'The InwardVolAccel object stores the data for an inward volume acceleration acoustic load.',
	'InwardVolAccelState':'The InwardVolAccelState object stores the propagating data of an inward volume acceleration acoustic load in a step. One instance of this object is created internally by the InwardVolAccel object for each step. The instance is also deleted internally by the InwardVolAccel object.The InwardVolAccelState object has no constructor or methods.',
	'Job':'The Job object is the abstract base type for other Job objects. The Job object has no explicit constructor. The methods and members of the Job object are common to all objects derived from Job.',
	'JobData':'The \n      JobData\n      object describes the context in which the analysis was run.\n   ',
	'JobFromInputFile':'The JobFromInputFile object defines a Job object which analyzes a model contained in an input file.',
	'JouleHeatFraction':'The JouleHeatFraction object defines the fraction of electric energy released as heat.',
	'JournalOptions':'A \n      JournalOptions\n      object specifies how to record selection of geometry in the journal and replay files. \n      journalOptions\n      can also be used to set the numeric formatting options for field report output, geometry commands output, and a default format for other numeric output. The \n      JournalOptions\n      object has no constructor. Abaqus creates the \n      journalOptions\n      member when a session is started.\n   ',
	'KeywordBlock':'The \n      KeywordBlock \n      object contains a representation of its model in the Abaqus  input file format. You may edit the contents of the \n      KeywordBlock \n      to add solver functionality that is not supported by Abaqus/CAE. As a general rule, edits to the \n      KeywordBlock \n      object should be made as the last step prior to writing the actual Abaqus  input file, thus avoiding possible conflicts with changes made using other MDB commands. The \n      KeywordBlock \n      object has no constructor. A \n      KeywordBlock \n      object is created when you create a model object. A model object contains only one \n      KeywordBlock \n      object.\n   ',
	'KinematicHardening':' The KinematicHardening object stores the data for initial equivalent plastic strains and, if relevant, the initial backstress tensor.     ',
	'LProfile':'The LProfile object defines the properties of a L profile.',
	'LatentHeat':"The LatentHeat object specifies a material's latent heat.",
	'Layer':'Objects can be superimposed by displaying them in different layers of a viewport.',
	'LayerProperties':'The LayerProperties object defines the properties of a layer of reinforcement for membrane, shell, and surface sections.',
	'Leaf':'Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands. Leaf objects have similarities to Set objects; however, Leaf objects are evaluated when the DisplayGroup expression is evaluated, and they can have SymbolicConstant values (which are also evaluated when the DisplayGroup expression is evaluated).',
	'LeafFromDatums':'The LeafFromDatums object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromDisplayGroup':'The LeafFromDisplayGroup object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromElementLabels':'The LeafFromElementLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromElementSets':'The LeafFromElementSets object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromElementVarRange':'The LeafFromElementVarRange object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromGeometry':'The LeafFromGeometry object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromInstance':'The LeafFromInstance object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromInstanceElementLabels':'The LeafFromInstanceElementLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromInstanceNodeLabels':'The LeafFromInstanceNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromMeshElementLabels':'The LeafFromMeshElementLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromMeshNodeLabels':'The LeafFromMeshNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromMeshSurfaceSets':'The LeafFromMeshSurfaceSets object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromModelElemLabels':'The LeafFromModelElemLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands. ',
	'LeafFromModelNodeLabels':'The LeafFromModelNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromNodeLabels':'The LeafFromNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromNodeSets':'The LeafFromNodeSets object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromNodeVarRange':'The LeafFromNodeVarRange object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbElementLayups':'The LeafFromOdbElementLayups object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbElementMaterials':'The LeafFromOdbElementMaterials object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbElementPick':'The LeafFromOdbElementPick object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbElementPlies':'The LeafFromOdbElementPlies object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbElementSections':'The LeafFromOdbElementSections object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbElementTypes':'The LeafFromOdbElementTypes object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromOdbNodePick':'The LeafFromOdbNodePick object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromPartElementLabels':'The LeafFromPartElementLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromPartInstance':'The LeafFromPartInstance object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromPartNodeLabels':'The LeafFromPartNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromReferencePoint':'The LeafFromReferencePoint object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromSets':'The LeafFromSets object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromSurfaceSets':'The LeafFromSurfaceSets object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'LeafFromSurfaceVarRange':'The LeafFromSurfaceVarRange object can be used whenever a Leaf object is expected as an argument. Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to DisplayGroup commands.',
	'Legend':'The Legend object is used to store the display attributes of the chart legend. A legend object is automatically created when creating a Chart object.',
	'Light':'The \n      Light \n      object stores settings that control how objects are lit when the \n      renderStyle \n      is set to \n      SHADED.\n   The \n      Light \n      object has no constructor; Abaqus creates them as part of the \n      defaultLightOptions \n      and the \n      lightOptions \n      objects when a session is started.\n   ',
	'LightOptions':'The \n      LightOptions \n      object stores settings that control how objects are lit when the \n      renderStyle \n      is set to \n      SHADED. \n      LightOptions \n      objects are accessed in one of two ways:\n      The default light options. These settings are used as defaults when you start a session and by the \n    Defaults \n    button on the \n    Light Options \n    dialog box.\n The light options associated with a particular viewport.The \n      LightOptions \n      object has no constructor; Abaqus creates the \n      defaultLightOptions \n      member when a session is started.\n      When a new viewport is created, the \n      lightOptions \n      member is copied from the current viewport.\n   ',
	'LineLoad':'The LineLoad object stores the data of an applied line load.',
	'LineLoadState':'The LineLoadState object stores the propagating data of a line load in a step. One instance of this object is created internally by the LineLoad object for each step. The instance is also deleted internally by the LineLoad object.The LineLoadState object has no constructor or methods.',
	'LineStyle':'The LineStyle object is used to define the line style to be used for drawing XY-Plot objects.LineStyle objects can be created using the methods described below. ',
	'Load':'The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.',
	'LoadCase':'The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.Note that load cases are only available for Steady Steady Dynamics, Direct and Static, Linear Perturbation steps.',
	'LoadDisplayOptions':'The LoadDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.loads=ONThe LoadDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'LoadState':'The LoadState object is the abstract base type for other LoadState objects. The LoadState object has no explicit constructor or methods. The members of the LoadState object are common to all objects derived from LoadState.',
	'LocalStopCondition':'The LocalStopCondition object defines a local stop condition.',
	'LowDensityFoam':'The LowDensityFoam object specifies properties for low-density foam.',
	'MPCSection':'The MPCSection object defines the properties of a multi-point constraint section.',
	'MagneticPermeability':'The MagneticPermeability object specifies magnetic permeability.',
	'MagneticVectorPotentialBC':'The MagneticVectorPotentialBC object stores the data for a magnetic vector potential boundary condition.',
	'MappedField':'The MappedField object defines a spatially varying field whose value is calculated from an external source data.',
	'MassDiffusionStep':'The MassDiffusionStep object is used to control uncoupled transient or steady-state mass diffusion analysis.',
	'MassFlowRate':'The MassFlowRate object stores the data for mass flow rate.',
	'MassFlowRateState':'The MassFlowRateState object stores the propagating data of a MassFlowRate in a step. One instance of this object is created internally by the MassFlowRate object for each step. The instance is also deleted internally by the MassFlowRate object.The MassFlowRateState object has no constructor or methods.',
	'MassScaling':'A MassScaling object defines the region and controls that govern mass scaling.',
	'MasterSlaveAssignment':'The MasterSlaveAssignment object stores the master-slave assignment definition for surfaces in ContactExp and ContactStd objects. The MasterSlaveAssignment object has no constructor or members.',
	'Material':'A Material object is the object used to specify a material. The Material object stores the various settings that determine how a material behaves.A material is created by combining one or more individual material options and sub options. A particular material   option is associated with the Material object through a member. For example:  the acousticMedium member may contain an AcousticMedium object.   The alternative of having a MaterialOption abstract base class and a container of MaterialOptions was rejected because it   would make it more difficult to enforce the fact that one Material object cannot contain two AcousticMedium objects, for example.',
	'MaterialAssignment':'The MaterialAssignment object stores the data for an initial material assignment predefined field, for use with an Eulerian analysis.',
	'MaterialFlowBC':'The MaterialFlowBC object stores the data for a connector material flow boundary condition.',
	'MaterialFlowBCState':'The MaterialFlowBCState object stores the propagating data for a connector material flow boundary condition in a step. One instance of this object is created internally by the MaterialFlowBC object for each step. The instance is also deleted internally by the MaterialFlowBC object.The MaterialFlowBCState object has no constructor or methods.',
	'MaterialOrientation':'The \n      MaterialOrientation \n      object represents the orientation of the material properties and composite layups.\n   ',
	'Mdb':'The \n      Mdb \n      object is the high-level Abaqus model database. A model database stores models and analysis controls.\n   ',
	'MdbData':'The MdbData object has no constructor. Abaqus creates an MdbData object when a cae file is opened or a new model is created. There is one MdbData for each model in session. MdbData is updated when it is displayed in a viewport.',
	'MdbDataFrame':'The MdbDataFrame object. There is one and only MdbDataFrame in a MdbDataStep.',
	'MdbDataInstance':'The MdbDataInstance object instance data. It corresponds to same named part instance with a mesh in the cae model.',
	'MdbDataStep':'The MdbDataStep object.It corresponds to same named step in the cae model.',
	'MembraneSection':'The MembraneSection object defines the properties of a membrane section.',
	'MemoryReductionOptions':'The \n      MemoryReductionOptions\n      object controls the default settings that Abaqus/CAE uses for running in reduced memory mode. The \n      MemoryReductionOptions\n      object has no constructor. Abaqus creates the \n      MemoryReductionOptions\n      member when a session is started.\n   ',
	'MeshDisplayOptions':'The MeshDisplayOptions object stores settings that specify how the assembly is displayed in a particular viewport when session.viewports[name].assemblyDisplay.mesh=ONThe MeshDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'MeshEdge':'The MeshEdge object refers to an element edge. It has no constructor or members. A MeshEdge object can be accessed via a MeshEdgeArray or a repository on a part or part instance.',
	'MeshEdgeArray':'The MeshEdgeArray is a sequence of MeshEdge objects.',
	'MeshEditOptions':'The \n      MeshEditOptions \n      object stores settings that specify the behavior when editing meshes on parts or part instances.\n   The \n      MeshEditOptions \n      object has no constructor. Abaqus creates the \n      MeshEditOptions \n      member when a session is started.\n   ',
	'MeshElement':'The MeshElement object refers to an element of a native mesh or an orphan mesh. A MeshElement object can be accessed via a part or part instance using an index that refers to the internal numbering of the element repository. The index does not refer to the element label.',
	'MeshElementArray':'The MeshElementArray is a sequence of MeshElement objects.',
	'MeshFace':'The MeshFace object refers to an element face. It has no constructor or members. A MeshFace object can be accessed via a MeshFaceArray or a repository on a part or part instance.',
	'MeshFaceArray':'The MeshFaceArray is a sequence of MeshFace objects.',
	'MeshNode':'The MeshNode object refers to a node of a native mesh or an orphan mesh. A MeshNode object can be accessed via a part or part instance using an index that refers to the internal numbering of the node repository. The index does not refer to the node label.',
	'MeshNodeArray':'The MeshNodeArray is a sequence of MeshNode objects.',
	'MeshStats':'The MeshStats object is a query object for holding mesh statistics and is returned by the getMeshStats command. The object does not have any methods.',
	'MesherOptions':'The MesherOptions object controls the default settings that Abaqus uses for all meshing methods. The MesherOptions object has no constructor. Abaqus creates the MesherOptions member when a session is started.MesherOptions commands are intended for use at the beginning of scripts and in the abaqus_env file only; they should not be used during an Abaqus/CAE session.',
	'Message':'The Message object contains information about a given phase of the simulation. Job messages are not returned if a script is run without the Abaqus/CAE GUI (using the noGUI option).',
	'ModalDynamicsStep':'The ModalDynamicsStep object is used to provide dynamic time history response as a linear perturbation procedure using modal superposition.',
	'Model':'Abaqus creates a \n      Model\n      object named \n      Model-1\n      when a session is started.\n   ',
	'ModelChange':'The ModelChange object defines model change interactions for element removal and reactivation.',
	'ModelDot':'The \n      ModelDot \n      object can be used to access an actual \n      MeshNode, \n      ReferencePoint, or \n      Vertex \n      object.\n   ',
	'ModelJob':'The ModelJob object defines a Job object which analyzes a model on a model database (MDB).',
	'ModulatedAmplitude':'The ModulatedAmplitude object defines a modulated amplitude curve.',
	'MohrCoulombHardening':'The MohrCoulombHardening object specifies hardening for the Mohr-Coulomb plasticity model.',
	'MohrCoulombPlasticity':'The MohrCoulombPlasticity object specifies the extended Mohr-Coulomb plasticity model.',
	'MoistureSwelling':'The MoistureSwelling object defines moisture-driven swelling.',
	'Moment':'The Moment object stores the data for a moment.',
	'MomentState':'The MomentState object stores the propagating data for a moment in a step. One instance of this object is created internally by the Moment object for each step. The instance is also deleted internally by the Moment object.The MomentState object has no constructor or methods.',
	'Monitor':'The Monitor object defines a degree of freedom to monitor.',
	'MonitorMgr':'An instance of the MonitorMgr object is created when you import the abaqus module. No other instance of the MonitorMgr object is required. (This MonitorMgr object is not to be confused with the degree of freedom (DOF) monitor that is constructed from the Step object.)',
	'Movie':'The Movie object is used to store values and attributes associated with a movie file. Upon creation, the Movie object is added to the session.movies repository.',
	'MovieOptions':'The \n      MovieOptions \n      object stores settings that control how the movie background for an animation is rendered in a particular viewport. \n      MovieOptions \n      objects are accessed from the movie options associated with a particular viewport.\n   The \n      MovieOptions \n      object has no constructor; Abaqus creates the \n      movieOptions \n      member for a viewport when the viewport is created using the values in the \n      movieOptions \n      member of the current viewport.\n   ',
	'MullinsEffect':'The MullinsEffect specifies properties for mullins data.',
	'MultipointConstraint':'The MultipointConstraint object defines a constraint between a group of MultipointConstraint nodes located on a region and a reference point.',
	'NetworkDatabaseConnector':'The \n      NetworkDatabaseConnector\n      object allows you to access an output database on a remote system.\n   ',
	'NodalDofs':'The NodalDofs object represents the degrees of freedom that are retained or eliminated in a substructure generate analysis.',
	'NodeQuery':'The NodeQuery object specifies nodes and their coordinates in a path. The NodeQuery object has no constructor or methods. Abaqus creates the nodeQuery member when you import the visualization module.',
	'NonstructuralMass':'The NonstructuralMass object defines the mass contribution from nonstructural features into the model.',
	'NormalBehavior':'The NormalBehavior object specifies normal behavior for a contact interaction property.',
	'NumberFormat':'The \n      NumberFormat\n      object is a formatting template used to define formatting options for certain numeric output.\n   ',
	'ObjectiveFunction':'The ObjectiveFunction object defines the objective of the optimization.',
	'Odb':'The \n      Odb\n      object is the in-memory representation of an output database (ODB) file.\n   ',
	'OdbAssembly':'The \n      OdbAssembly\n      object has no constructor; it is created automatically when an \n      Odb\n      object is created. Abaqus creates the \n      rootAssembly\n      member when an \n      Odb\n      object is created.\n   ',
	'OdbData':'The OdbData object stores non persistent values and attributes associated with an open odb for the given session. The OdbData object has no constructor. Abaqus creates the odbData repository when you import the Visualization module.  Abaqus creates a OdbData object when an odb is opened.',
	'OdbDataDatumCsys':'The OdbDataDatumCsys object stores coordinate system data.',
	'OdbDataElementSet':'The OdbDataElementSet object stores element set data.',
	'OdbDataFrame':'The OdbDataFrame object.',
	'OdbDataInstance':'The OdbDataInstance object instance data.',
	'OdbDataMaterial':'The OdbDataMaterial object stores material data.',
	'OdbDataNodeSet':'The OdbDataNodeSet object stores node set data.',
	'OdbDataSection':'The OdbDataSection object stores section data.',
	'OdbDataStep':'The OdbDataStep object.',
	'OdbDataSurfaceSet':'The OdbDataSurfaceSet object stores surface set data.',
	'OdbDatumCsys':'The OdbDatumCsys object contains a coordinate system that can be stored in an output database. You can create the datum coordinate system in the Visualization module during an Abaqus/CAE session and save the datum coordinate system to the output database before you exit Abaqus/CAE. Alternatively, the analysis code can write the datum coordinate system to the output database. ',
	'OdbDisplay':'The OdbDisplay object stores the context of an output database for a viewport. The OdbDisplay object has no constructor. Abaqus creates the defaultOdbDisplay member when you import the Visualization module. Abaqus creates the odbDisplay member when a viewport is created, using the attributes from the previous active viewport. The previous active viewport contains the attributes from the defaultOdbDisplay object for the session. The attributes from the defaultOdbDisplay object are copied from the previous active viewport to create the new viewport.OdbDisplay objects are accessed in one of two ways: The default output database display options. These settings are used as defaults when other odbDisplay members are created and can be set to customize user preferences.The output database display options associated with a particular viewport.',
	'OdbDisplayOptions':'The OdbDisplayOptions object stores the display options associated with an OdbInstance object. This object does not have a constructor. Abaqus creates the OdbDisplayOptions object when an OdbInstance object is created using the display options associated with the current viewport at the time of creation.',
	'OdbFieldVarList':'The read-only OdbFieldVarList object is a sequence listing all variables available for the current step and frame. Each item in the sequence is itself a sequence fully describing the given variable.',
	'OdbFrame':'The domain of the OdbFrame object is taken from the parent step.',
	'OdbInstance':'A part instance is the usage of a part within an assembly.',
	'OdbLoadCase':'The OdbLoadCase object describes a load case.',
	'OdbMeshElement':'OdbMeshElement\n      objects are created with the \n      part.addElements\n      or \n      rootAssembly.addElements\n      methods.\n   ',
	'OdbMeshNode':'OdbMeshNode objects are created with the part.addNodes method.',
	'OdbMeshRegionData':'The OdbMeshRegionData object defines the external source data of MappedField from an ODB file.',
	'OdbModelFieldVarList':'The read-only OdbModelFieldVarList object lists all variables available for the model in the current OdbDisplay object.',
	'OdbPart':'The \n      OdbPart\n      object is similar to the kernel Part object and contains nodes and elements, but not geometry.\n   ',
	'OdbPretensionSection':'The pretension section object is used to define an assembly load. It associates a pretension node with a pretension section.',
	'OdbRigidBody':'The Rigid body object is used to bind a set of elements and/or a set of nodes and/or an analytical surface with a reference node.',
	'OdbSequenceAnalyticSurfaceSegment':'A sequence of AnalyticSurfaceSegment describing an analytic surface profile.',
	'OdbSet':'The set objects are used to identify regions of a model.',
	'OdbStep':'An output database contains the same steps of the model database that originated it.',
	'OperatorFilter':'The OperatorFilter object defines an operator filter.',
	'OptimizationConstraint':'The OptimizationConstraint object constrains an optimization from making changes to the topology of the model.',
	'OptimizationObjective':'An OptimizationObjective is an object used to define objectives in an objective function.',
	'OptimizationProcess':'The OptimizationProcess object defines a process to perform an optimization of a model defined using an optimization task.',
	'OptimizationTask':'The OptimizationTask object is the abstract base type for other OptimizationTask objects. The OptimizationTask object has no explicit constructor. The methods and members of the OptimizationTask object are common to all objects derived from OptimizationTask.',
	'OptimizationTaskDisplayOptions':'The OptimizationTaskDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.optimizationTasks=ON The OptimizationTaskDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'OptionArg':'The OptionArg object is used to store values and attributes as a temporary object to be associated with a viewCutOptions object. The OptionArg object has only a constructor command. ',
	'OrientationOptions':'The OrientationOptions object stores values and attributes associated with a material orientation plot. The OrientationOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.materialOrientationOptions member when you import the Visualization module. Abaqus creates a materialOrientationOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.materialOrientationOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.OrientationOptions objects are accessed in one of two ways:The default material orientation options. These settings are used as defaults when other materialOrientationOptions members are created. These settings can be set to customize user preferences.The material orientation options associated with a particular viewport.',
	'Ornl':'The Ornl object specifies the constitutive model developed by Oak Ridge National Laboratory.',
	'PEGLoad':'The PEGLoad object stores the data for a PEG load.',
	'PEGLoadState':'The PEGLoadState object stores the propagating data for a concentrated force in a step. One instance of this object is created internally by the PEGLoad object for each step. The instance is also deleted internally by the PEGLoad object.The PEGLoadState object has no constructor or methods.',
	'PEGSection':'The PEGSection object defines the properties of a solid section.',
	'PageSetupOptions':'The \n      PageSetupOptions\n      object stores the settings that Abaqus uses when printing using a Windows printer. The \n      PageSetupOptions\n      object has no constructor. Abaqus creates the \n      pageSetupOptions\n      member when a session is started.\n   ',
	'Part':'The Part object defines the physical attributes of a structure. Parts are instanced into the assembly and positioned before an analysis.',
	'PartDisplayOptions':'The PartDisplayOptions object stores settings that specify how parts are to be displayed in a particular viewport. The PartDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'PartInstance':'A PartInstance object is an instance of a Part object.',
	'Path':'The Path object defines a line through your model by specifying a series of nodes or points.',
	'PenetrationCheck':'The PenetrationCheck object defines a penetration check geometric restriction.',
	'PeriodicAmplitude':'The PeriodicAmplitude object defines an amplitude curve using a Fourier series.',
	'Permeability':'The Permeability object defines permeability for pore fluid flow.',
	'Piezoelectric':'The Piezoelectric object specifies piezoelectric material properties.',
	'PipePressure':'The PipePressure object stores the data for a pressure applied to pipe or elbow elements.',
	'PipePressureState':'The PipePressureState object stores the propagating data for a pipe pressure in a step. One instance of this object is created internally by the PipePressure object for each step. The instance is also deleted internally by the PipePressure object.The PipePressureState object has no constructor or methods.',
	'PipeProfile':'The PipeProfile object defines the properties of a circular pipe profile.',
	'PlanarTestData':'The PlanarTestData object specifies planar test (or pure shear) data (compression and/or tension).',
	'Plastic':'The Plastic object specifies a metal plasticity model.',
	'PlyStackPlot':'The PlyStackPlot object is used to plot the stacking of plies in a composite layup or in a composite shell section. ',
	'PlyStackPlotOptions':'The PlyStackPlotOptions object stores values and attributes associated with aViewport object. The PlyStackPlotOptions object has no constructor command. Abaqus creates the detailPlotOptions.plyStackPlotPlotOptions member whenever a Viewport is created.',
	'PngOptions':'The PngOptions object stores the settings that Abaqus uses when printing in PNG format. The \n      PngOptions\n      object has no constructor. Abaqus creates the \n      pngOptions\n      member when a session is started.\n   ',
	'PointFastener':'The PointFastener object defines a point fastener.',
	'PointMassInertia':'The PointMassInertia object defines point masses and point rotary inertia on a part or an assembly region.',
	'PointSection':'',
	'PorDragBodyForce':'The PorDragBodyForce object stores the data for a fluid pore drag body force load.',
	'PorDragBodyForceState':'The PorDragBodyForceState object stores the propagating data for a Body PorDragBodyForce object in a step. One instance of this object is created internally by the PorDragBodyForce object for each step. The instance is also deleted internally by the PorDragBodyForce object.The PorDragBodyForceState object has no constructor or methods.',
	'PoreFluidExpansion':'The PoreFluidExpansion object specifies the thermal expansion coefficient for a hydraulic fluid.',
	'PorePressure':'The PorePressure object stores the data for initial pore fluid pressures.',
	'PorePressureBC':'The PorePressureBC object stores the data for a pore pressure boundary condition.',
	'PorePressureBCState':'The PorePressureBCState object stores the propagating data for a pore pressure boundary condition in a step. One instance of this object is created internally by the PorePressureBC object for each step. The instance is also deleted internally by the PorePressureBC object.The PorePressureBCState object has no constructor or methods.',
	'PorousBulkModuli':'The PorousBulkModuli object defines bulk moduli for soils and rocks.',
	'PorousElastic':'The PorousElastic object specifies elastic material properties for porous materials.',
	'PorousFailureCriteria':'The PorousFailureCriteria object specifies the material failure criteria for a porous metal.',
	'PorousMetalPlasticity':'The PorousMetalPlasticity object specifies a porous metal plasticity model.',
	'Potential':'The Potential object defines an anisotropic yield/creep model.',
	'PredefinedField':'The PredefinedField object is the base object for the objects in the predefined field repository. The methods and members of the PredefinedField object are common to all objects derived from PredefinedField.An instance of any PredefinedField object can be obtained through the predefined field repository of the Model object. An instance of any PredefinedFieldState object can be obtained through the predefined field repository of the Step object.',
	'PredefinedFieldDisplayOptions':'The PredefinedFieldDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.predefinedFields=ONThe PredefinedFieldDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'PredefinedFieldState':'The PredefinedFieldState object is the base object for the objects in the predefinedFieldState repository of the Step object. The members of the PredefinedFieldState object are common to all objects derived from PredefinedFieldState.The PredefinedFieldState object has no constructor or methods.',
	'Pressure':'The Pressure object defines a pressure load.',
	'PressureEffect':'The PressureEffect object defines equivalent pressure stress driven mass diffusion.',
	'PressurePenetration':'The PressurePenetration object defines pressure penetration loading simulated with surface-to-surface contact.',
	'PressurePenetrationState':'The PressurePenetrationState object stores the propagating data of a PressurePenetration object in a step. One instance of this object is created internally by the PressurePenetration object for each step. The instance is also deleted internally by the PressurePenetration object.The PressurePenetrationState object has no constructor or methods.',
	'PressureState':'The PressureState object stores the propagating data for a pressure in a step. One instance of this object is created internally by the Pressure object for each step. The instance is also deleted internally by the Pressure object.The PressureState object has no constructor or methods.',
	'PressureStress':'The PressureStress object stores the data for presure stresses in a mass diffusion analysis.',
	'PressureStressState':'The PressureStressState object stores the propagating data of a PressureStress in a step. One instance of this object is created internally by the PressureStress object for each step. The instance is also deleted internally by the PressureStress object.The PressureStressState object has no constructor or methods.',
	'PrintOptions':'The PrintOptions object stores the common settings that Abaqus uses for all print methods. The \n      PrintOptions\n      object has no constructor. Abaqus creates the \n      printOptions\n      member when a session is started.\n   ',
	'ProbeOptions':'The ProbeOptions object is used to store settings associated with probing a model or an X&#8211;Y plot. The ProbeOptions object has no constructor. Abaqus creates the defaultProbeOptions and the probeOptions members when you import the Visualization module. When probing is initiated for the first time, the values in the probeOptions member are initialized using the values from the defaultProbeOptions member.',
	'ProbeReport':'The ProbeReport object is used to store settings associated with tabular reports of probe data. The ProbeReport object has no constructor. Abaqus creates the defaultProbeReport and the probeReport members when you import the Visualization module. When probing is initiated for the first time, the values in the probeReport member are initialized using the values from the defaultProbeReport member.',
	'Profile':'The Profile object defines the geometrical properties of a beam cross-section. Profile is an abstract base type.',
	'PsOptions':'The PsOptions object stores the settings that Abaqus uses when printing using PostScript format. The \n      PsOptions\n      object has no constructor. Abaqus creates the \n      psOptions\n      member when a session is started.\n   ',
	'PsdDefinition':'The \n      PsdDefinition\n      object defines the cross-spectral density frequency function for random response loading.\n   ',
	'QuantityType':'The QuantityType object is used to store attributes defining the physical dimension and label of the quantity type to be associated with an XYData or an AxisData object.QuantityType objects are automatically created when creating XYData objects from the odb. QuantityType objects can be created using the methods described below. ',
	'Queue':'A Queue object tells the job where and how to submit a job remotely. A Queue object can be used as the queue argument to the Job method.',
	'QuickTimeOptions':'The QuickTimeOptions object is used to store values and attributes to be used in generating QuickTime animation. The QuickTimeOptions object has no constructor. Abaqus creates the quickTimeOptions member when the animation module is imported.',
	'Radiation':'The Radiation object specifies radiation for a contact interaction property.',
	'RadiationToAmbient':'The RadiationToAmbient object defines radiant heat transfer between a surface and its environment.',
	'RadiationToAmbientState':'The RadiationToAmbientState object stores the propagating data for a RadiationToAmbient object. One instance of this object is created internally by the RadiationToAmbient object for each step. The instance is also deleted internally by the RadiationToAmbient object.The RadiationToAmbientState object has no constructor or methods.',
	'RandomResponseFrequency':'A RandomResponseFrequency is an object used to define frequency over a range of modes.',
	'RandomResponseStep':'The RandomResponseStep object is used to give the linearized response of a model to random excitation.',
	'RateDependent':'The RateDependent object defines a rate-dependent viscoplastic model.',\
	'Ratios':'The Ratios object specifies ratios that define anisotropic swelling.',
	'RayleighDamping':'A RayleighDamping object contains Rayleigh Damping parameters.',
	'RayleighDampingByFrequency':'A RayleighDampingByFrequency object contains Rayleigh Damping parameters.',
	'RayleighDampingByFrequencyComponent':'A RayleighDampingByFrequencyComponent object is used to define Rayleigh damping over a range of frequencies.',
	'RayleighDampingComponent':'A RayleighDampingComponent object is used to define Rayleigh damping over a range of modes.',
	'RebarLayers':'The RebarLayers object defines the rebar properties of a section.',
	'RebarOrientation':'The RebarOrientation object represents the orientation of the rebar reference.',
	'RectangularProfile':'The RectangularProfile object defines the properties of a solid rectangular profile.',
	'ReferencePoint':'The \n      ReferencePoint \n      object has no direct constructor; it is created when a \n      Feature \n      object is created. The \n      ReferencePoint \n      method creates a \n      Feature \n      object that creates a \n      ReferencePoint \n      object.\n   ',\
	'ReferencePressure':'The ReferencePressure object stores the data for a fluid reference pressure load.',
	'Region':'The purpose of the Region object is to provide a link between an attribute and the geometric or discrete entities to which the attribute is applied. An attribute (Load, BC, IC, etc.) is applied to one or more Region objects; each Region object in turn is associated with a picked Set or Surface or with a named Set or Surface. The Region object provides a unified interface (or "fa&#231;ade") to data and functionality located at the Set or Surface.A script that applies an attribute to a picked Set or Surface requires the explicit creation of a Region object and will implicitly create a matching internal Set or Surface. Conversely, a script that applies an attribute to a named Set or Surface requires the explicit creation of that Set or Surface (see 39.4) and will implicitly create a region object.The reference between Region and Set/Surface is by name (user-provided or internal.) If the Set/Surface is suppressed, deleted, or renamed, the Region object will not be able to find the associated Set/Surface, and will communicate that to the attribute, but will not be affected otherwise. If a Set/Surface with the same name becomes available (only possible with user-provided names) the Region object will re-establish the connection. Another way of correcting this problem is to re-apply the attribute.Wherever a particular Load, BC, IC, etc. command accepts a named set or a named surface, that command will also accept a Region object. For example, myRegion = regionToolset.Region(edges=edges1)\nmdb.models[\'Model-1\'].DisplacementBC(name=\'BC-1\',\n createStepName=\'Initial\', region=myRegion, u1=SET,\n u2=SET)\nmyRegion = regionToolset.Region(elements=e[1:100])\np = mdb.models[\'mirror\'].parts[\'COLLAR_MIRROR-1\']\np.SectionAssignment(region=myRegion, sectionName=\'Section-1\')Abaqus does not provide a regions repository; as an alternative, you should assign a variable to a Region object and refer to the variable. The life cycle of a Region object is similar to the life cycle of a Leaf object used by display groups; as a result, you should use a Region object immediately after you create it. The contents of a Region object are not intended to survive regeneration. If you use an out-of-date Region object, the script is unlikely to function correctly. Querying an attribute\'s Region will return a Region tuple.     The contents of the tuple are the set name followed by the owners of the set and three flags expressed as integers.  The flags indicate the region space, the type of region and the whether the region is an internal set.',
	'RegionPairs':'The RegionPairs object stores the domain pair definition for ContactExp and ContactStd objects. The RegionPairs object has no constructor or members.',
	'RegisteredDictionary':'This class allows you to create a dictionary that can be queried from the GUI and is capable of notifying the GUI when the contents of the dictionary change. The keys to a RegisteredDictionary must be either strings or integers.',
	'RegisteredList':'This class allows you to create a list that can be queried from the GUI and is capable of notifying the GUI when the contents of the list change.',
	'RegisteredTuple':"This class allows you to create a tuple that can be queried from the GUI and is capable of notifying the GUI when the contents of any of the tuple's members change.",
	'Regularization':'The Regularization object defines the tolerance to be used for regularizing material data.',
	'RelativeDensity':'The RelativeDensity object stores the data for initial relative density values for materials defined with the POROUS METAL PLASTICITY option.',
	'RemeshingRule':'The RemeshingRule object controls the adaptive remeshing resizing and the error indicators written to the output database for a specified region of the model.',
	'RepositorySupport':'The \n      RepositorySupport \n      is a base class from which you can derive your own classes that are designed to contain custom repositories. Instances of this class can be queried from the GUI and are capable of notifying the GUI when the contents of the instance change.\n   ',
	'ResponseSpectrumComponent':'A ResponseSpectrumComponent is an element of the ResponseSpectrumComponentArray.',
	'ResponseSpectrumStep':'The ResponseSpectrumStep object is used to calculate estimates of peak values of displacements and stresses based on user-supplied response spectra and on the natural modes of the system.',
	'Restart':'The Restart object defines a restart request.Adaptive Mesh Domain objects are also attached\nto the step that is referenced in the same way. Adaptive Mesh Controls objects\nare not attached to the step, but belong to the model. This is a temporary\nimplementation due to a time constraint for alpha-5 support and will only\napply to Explicit Dynamic steps. In a later version both of these objects\nwill belong to the model and can be used with other types of steps.',
	'RetainedNodalDofsBC':'The RetainedNodalDofsBC object stores the data for a retained nodal dofs boundary condition.',
	'RigidBody':'The RigidBody object constrains all the degrees of freedom on the specified regions to the degree of freedom of its associated reference point.',
	'RotationalBodyForce':'The RotationalBodyForce object stores the data for a rotational body force.',
	'RotationalBodyForceState':'The RotationalBodyForceState object stores the propagating data of a rotational body force in a step. One instance of this object is created internally by the RotationalBodyForce object for each step. The instance is also deleted internally by the RotationalBodyForce object.The RotationalBodyForceState object has no constructor or methods.',
	'RuleResult':'The RuleResult object contains result information corresponding to a RemeshingRule object for an adaptivity iteration.',
	'SDV':'The SDV object stores the data for initial values of solution-dependent state variables.',
	'Saturation':'The Saturation object stores the data for initial saturation values for the analysis of flow through a porous medium.',
	'SaturationDependence':'The SaturationDependence object specifies the dependence of the permeability of a material on the saturation of the wetting liquid.',
	'ScratchOdb':'A scratch output database is associated with an open output database and is used to store session-related, non-persistent objects, such as Step, Frame and FieldOutput objects. Abaqus creates a scratch output database when needed for these non-persistent objects during an Abaqus/CAE session. Abaqus deletes the scratch output database when the associated output database is closed.',
	'SecondaryBaseBC':'The SecondaryBaseBC object stores the data for a secondary base boundary condition.',
	'SecondaryBaseBCState':'The SecondaryBaseBCState object stores the propagating data for a secondary base boundary condition in a step. One instance of this object is created internally by the SecondaryBaseBC object for each step. The instance is also deleted internally by the SecondaryBaseBC object.The SecondaryBaseBCState object has no constructor or methods.',
	'Section':'The Section object defines the properties of a section. The Section object is the abstract base type for other Section objects. The Section object has no explicit constructor. The methods and members of the Section object are common to all objects derived from the Section.',
	'SectionAssignment':'The SectionAssignment object is used to specify a section assignment on an assembly, part or part instance. Section assignments on the assembly are limited to connector elements only.',
	'SectionCategory':'The SectionCategory object is used to group regions of the model with like sections. Section definitions that contain the same number of section points or integration points are grouped together.To access data for a particular section definition, use the individual Section objects in the output database. For more information, see ,&#8221; and .&#8221;',
	'SectionLayer':'The SectionLayer object defines the material layer in a composite shell.',
	'SectionPoint':'The SectionPoint object describes the location of a section point within a section category.',
	'SectorDefinition':'The SectorDefinition object describes the number of symmetry sectors and axis of symmetry for a cyclic symmetry model.',
	'SelectedProbeValues':'The SelectedProbeValues object has no constructor. The SelectedProbeValues object is created when you import the Visualization module.',
	'SelfContactExp':'The SelfContactExp object defines self-contact during an Abaqus/Explicit analysis.',
	'SelfContactExpState':'The SelfContactExpState object stores the propagating data for a SelfContactExp object. One instance of this object is created internally by the SelfContactExp object for each step. The instance is also deleted internally by the SelfContactExp object.The SelfContactExpState object has no constructor or methods.',
	'SelfContactStd':'The SelfContactStd object defines self-contact during an Abaqus/Standard analysis.',
	'SelfContactStdState':'The SelfContactStdState object stores the propagating data for a SelfContactStd object. One instance of this object is created internally by the SelfContactStd object for each step. The instance is also deleted internally by the SelfContactStd object.The SelfContactStdState object has no constructor or methods.',
	'Session':'The Session object has no constructor. Abaqus creates the\n      session\n      member when a session is started.\n   ',
	'Set':"If a set spans more than one part instance, the vertex, edge, face, \n cell, element, and node members return a sequence of sequences for each part instance. \n Each sequence contains entities from a single instance. For example:\n assembly=mdb.models['Transmission'].assembly\n clutchElements=assembly.instances['Clutch'].elements \n clutchSet=clutchElements[16:18]+clutchElements[78:80] \n housingElements=assembly.instances['Housing'].elements \n housingSet=housingElements[45:48] \n transmissionSet=assembly.Set(name='TransmissionSet',     elements=(clutchSet, housingSet))\n len(transmissionSet.element)=2 \n transmissionSet.elements[0]=16,17,78,79 \n transmissionSet.elements[1]=45,46,47",
	'ShapeDemoldControl':'The ShapeDemoldControl object defines a shape demold control geometric restriction.',
	'ShapeMemberSize':'The ShapeMemberSize object defines a shape member size geometric restriction.',
	'ShapePlanarSymmetry':'The ShapePlanarSymmetry object defines a shape planar symmetry geometric restriction.',
	'ShapePointSymmetry':'The ShapePointSymmetry object defines a shape point symmetry geometric restriction.',
	'ShapeRotationalSymmetry':'The ShapeRotationalSymmetry object defines a shape rotational symmetry geometric restriction.',
	'ShapeTask':'The ShapeTask object defines a shape task.',
	'Shear':'The Shear object specifies elastic shear.',
	'ShearRetention':'The ShearRetention object defines the reduction of the shear modulus associated with crack surfaces in a Concrete model as a function of the tensile strain across the crack.',
	'ShearTestData':'The ShearTestData object specifies the normalized shear creep compliance or relaxation modulus as a function of time.',
	'ShellEdgeLoad':'The ShellEdgeLoad object defines shell edge loads on a region.',
	'ShellEdgeLoadState':'The ShellEdgeLoadState object stores the propagating data for a ShellEdgeLoad object in a step. One instance of this object is created internally by the ShellEdgeLoad object for each step. The instance is also deleted internally by the ShellEdgeLoad object.The ShellEdgeLoadState object has no constructor or methods.',
	'ShellSection':'The ShellSection object defines the properties of a shell section. The ShellSection object is derived from the Section object. The ShellSection object has no explicit constructor and no methods or members.',
	'ShellSolidCoupling':'The ShellSolidCoupling object defines two surfaces to be tied together for the duration of a simulation.',
	'SimpleShearTestData':'The SimpleShearTestData object provides simple shear test data.',
	'SingleTermDesignResponse':'The SingleTermDesignResponse object defines a single-term design response.',
	'Skin':'The Skin object stores information on skin reinforcements created on entities.',
	'SlideRegionControl':'The SlideRegionControl object defines a slide region control geometric restriction.',
	'SmoothStepAmplitude':'The SmoothStepAmplitude object defines an amplitude that ramps up or down smoothly from one data point to another.',
	'SmoothingAssignment':'The SmoothingAssignment object stores the surface smoothing assignment definition for surfaces in ContactExp and ContactStd objects. The SmoothingAssignment object has no constructor or members.',
	'SoilsStep':'The SoilsStep object is used to specify transient (consolidation) or steady-state response analysis of partially or fully saturated fluid-filled porous media.',
	'SolidSection':'The SolidSection object defines the properties of a solid section. The SolidSection object has no explicit constructor, no members, and no methods. The SolidSection object is an abstract base type.',
	'Solubility':'The Solubility object specifies solubility.',
	'SolutionDependentAmplitude':'The SolutionDependentAmplitude object defines a solution-dependent amplitude for superplastic forming analysis.',
	'SolverControl':'The SolverControl object is used to provide additional optional solver controls.Note that solver controls are only available in Static, General and Static, Linear Perturbation steps.',
	'SoretEffect':'The SoretEffect object defines temperature gradient driven mass diffusion.',
	'Sorption':'The Sorption object defines absorption and exsorption behaviors of a partially saturated porous medium in the analysis of coupled wetting liquid flow and porous medium stress.',
	'SpecificHeat':"The SpecificHeat object specifies a material's specific heat.",
	'Spectrum':'The Spectrum object defines a color spectrum for the contour display.',
	'SpectrumAmplitude':'The \n      SpectrumAmplitude\n      object defines the spectrum of responses for displacement, velocity, or acceleration to be used in a response spectrum analysis.\n   ',
	'SpringDashpot':'The SpringDashpot object is the abstract base type for the SpringDashpotToGround and TwoPointSpringDashpot objects.',
	'SpringDashpotToGround':'The SpringDashpotToGround object defines springs and/or dashpots between points and ground on a part or an assembly region.',
	'SpudPreload':'The SpudPreload object stores the data for initial preload value for a spud can.',
	'StabilizationAssignment':'The StabilizationAssignment object stores the contact stabilization assignment definition for domain pairs in a ContactStd object. The StabilizationAssignment object has no constructor or members.',
	'StampControl':'The StampControl object defines a stamp control geometric restriction.',
	'StaticLinearPerturbationStep':'The StaticLinearPerturbationStep object is used to indicate that the static step should be analyzed as a linear perturbation load step.',
	'StaticRiksStep':'The StaticRiksStep object is used to indicate that the step should be analyzed as a static load step using the modified Riks method for proportional loading cases.',
	'StaticStep':'The StaticStep object is used to indicate that the step should be analyzed as a static load step.',
	'StdContactControl':'The StdContactControl object is used in Abaqus/Standard analyses to specify optional solution controls for problems involving contact between bodies.',
	'StdInitialization':'The StdInitialization object is used in conjunction with ContactStd in Abaqus/Standard analyses to specify contact initialization data.',
	'StdStabilization':'The StdStabilization object is used in conjunction with ContactStd in Abaqus/Standard analyses to specify contact stabilization.',
	'StdXplCosimulation':'The StdXplCosimulation object defines co-simulation behavior between Abaqus/Standard and Abaqus/Explicit.',
	'StdXplCosimulationState':'The StdXplCosimulationState object stores the propagating data for a StdXplCosimulation object. One instance of this object is created internally by the StdXplCosimulation object for each step. The instance is also deleted internally by the StdXplCosimulation object.The StdXplCosimulationState object has no constructor or methods.',
	'SteadyStateDirectFrequency':'A SteadyStateDirectFrequency is an object used to define frequency over range of modes.',
	'SteadyStateDirectStep':'The SteadyStateDirectStep object is used to calculate the linearized steady-state response of the system to harmonic excitation in terms of the physical degrees of freedom of the model. ',
	'SteadyStateModalFrequency':'A SteadyStateModalFrequency is an object used to define frequency over a range of modes.',
	'SteadyStateModalStep':'The SteadyStateModalStep object is used to calculate the linearized steady-state response of the system to harmonic excitation. ',
	'SteadyStateSubspaceFrequency':'A SteadyStateSubspaceFrequency is an object used to define frequency over range of modes.',
	'SteadyStateSubspaceStep':'The SteadyStateSubspaceStep object is used to calculate the linearized steady-state response of the system to harmonic excitation on the basis of the subspace projection method.',
	'Step':'The Step object stores the parameters that determine the context of the step. The Step object is the abstract base type for other Step objects. The Step object has no explicit constructor. The methods and members of the Step object are common to all objects derived from the Step. ',
	'StepOption':'A StepOption is an object used to define step options in a design response.',
	'StopCondition':'The StopCondition object is the abstract base type for other StopCondition objects. The StopCondition object has no explicit constructor. The methods and members of the StopCondition object are common to all objects derived from StopCondition.',
	'StopConditionDisplayOptions':'The StopConditionDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when session.viewports[name].assemblyDisplay.stopConditions=ONThe StopConditionDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'Stream':'The\n      Stream\n      object defines a set of streamlines in fluid mechanics.\n   ',
	'StreamOptions':'The StreamOptions object stores values and attributes associated with a stream plot. The StreamOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.streamOptions member when you import the Visualization module. Abaqus creates a StreamOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.streamOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.StreamOptions objects are accessed in one of two ways:The default stream options. These settings are used as defaults when other streamOptions members are created. These settings can be set to customize user preferences.The stream options associated with a particular viewport.',
	'Stress':'The Stress object stores the data for an initial stress predefined field.',
	'Stringer':'The Stringer object stores information on stringer reinforcements created on entities.',
	'StructuralDamping':'A StructuralDamping object contains structural damping parameters.',
	'StructuralDampingByFrequency':'A StructuralDampingByFrequency object contains structural damping parameters.',
	'StructuralDampingByFrequencyComponent':'A StructuralDampingByFrequencyComponent object is used to define structural damping over a range of frequencies.',
	'StructuralDampingComponent':'A StructuralDampingComponent object is used to define structural damping over a range of modes.',
	'SubmodelBC':'The SubmodelBC object stores the data for a submodel boundary condition.',
	'SubmodelBCState':'The SubmodelBCState object stores the propagating data for a Submodel boundary condition in a step. One instance of this object is created internally by the SubmodelBC object for each step. The instance is also deleted internally by the SubmodelBC object.The SubmodelBCState object has no constructor or methods.',
	'SubmodelSB':'The SubmodelSB object stores the data for a submodel surface based load.',
	'SubmodelSBState':'The SubmodelSBState object stores the propagating data for a Submodel load in a step. One instance of this object is created internally by the SubmodelSB object for each step. The instance is also deleted internally by the SubmodelSB object.The SubmodelSBState object has no constructor or methods.',
	'SubspaceDynamicsStep':'The SubspaceDynamicsStep object is used to calculate the linearized steady-state response of the system to harmonic excitation on the basis of the subspace projection method.',
	'SubstructureGenerateFrequency':'A \n      SubstructureGenerateFrequency\n      object is used to define the modes to be used in a modal dynamic analysis. These modes are selected from the specified frequency range including the frequency boundary.\n   ',
	'SubstructureGenerateModes':'A \n      SubstructureGenerateModes\n      object is used to define the modes to be used in a modal dynamic analysis.\n   ',
	'SubstructureGenerateStep':'The\n      SubstructureGenerateStep\n      object is used to generate a substructure.\n   ',
	'SubstructureLoad':'The SubstructureLoad object defines a substructure load.',
	'SubstructureLoadState':'The SubstructureLoadState object stores the propagating data for a substructure load in a step. One instance of this object is created internally by the SubstructureLoad object for each step. The instance is also deleted internally by the SubstructureLoad object.The SubstructureLoadState object has no constructor or methods.',
	'SuperimposeOptions':'The SuperimposeOptions object stores values and attributes associated with the undeformed shape when the display contains both the deformed shape and the undeformed shape. The SuperimposeOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.superimposeOptions member when you import the Visualization module. Abaqus creates a superimposeOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.superimposeOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.SuperimposeOptions objects are accessed in one of two ways:    The default superimpose options. These settings are used as defaults when other superimposeOptions members are created. These settings can be set to customize user preferences.The superimpose options associated with a particular viewport.',
	'Surface':'The Surface object stores surfaces selected from the assembly. A surface is comprised of geometric or discrete entities but not both. An instance of a Surface object is available from the surface member of the Assembly object.',
	'SurfaceCharge':'The SurfaceCharge object stores the data for a surface charge.',
	'SurfaceChargeState':'The SurfaceChargeState object stores the propagating data of a surface charge in a step. One instance of this object is created internally by the SurfaceCharge object for each step. The instance is also deleted internally by the SurfaceCharge object.The SurfaceChargeState object has no constructor or methods.',
	'SurfaceConcentrationFlux':'The SurfaceConcentrationFlux object defines surface concentration flux from a region or into a region.',
	'SurfaceConcentrationFluxState':'The SurfaceConcentrationFluxState object stores the propagating data for a SurfaceConcentrationFlux object in a step. One instance of this object is created internally by the SurfaceConcentrationFlux object for each step. The instance is also deleted internally by the SurfaceConcentrationFlux object.The SurfaceConcentrationFluxState object has no constructor or methods.',
	'SurfaceCurrent':'The SurfaceCurrent object stores the data for a surface current.',
	'SurfaceCurrentDensity':'The SurfaceCurrentDensity object stores the data for a surface current.',
	'SurfaceCurrentState':'The SurfaceCurrentState object stores the propagating data of a surface current in a step. One instance of this object is created internally by the SurfaceCurrent object for each step. The instance is also deleted internally by the SurfaceCurrent object.The SurfaceCurrentState object has no constructor or methods.',
	'SurfaceFeatureAssignment':'The SurfaceFeatureAssignment object stores the surface feature angle assignment definition for surfaces in ContactExp  or ContactStd objects. The SurfaceFeatureAssignment object has no constructor or members.',
	'SurfaceHeatFlux':'The SurfaceHeatFlux object defines surface heat flux from a region or into a region.',
	'SurfaceHeatFluxState':'The SurfaceHeatFluxState object stores the propagating data for a surface SurfaceHeatFlux object in a step. One instance of this object is created internally by the SurfaceHeatFlux object for each step. The instance is also deleted internally by the SurfaceHeatFlux object.The SurfaceHeatFluxState object has no constructor or methods.',
	'SurfaceOffsetAssignment':'The SurfaceOffsetAssignment object stores the surface offset fraction assignment definition for surfaces in ContactExp and ContactStd objects. The SurfaceOffsetAssignment object has no constructor or members.',
	'SurfacePoreFluid':'The SurfacePoreFluid object defines surface pore fluid flow from a region or into a region.',
	'SurfacePoreFluidState':'The SurfacePoreFluidState object stores the propagating data for a SurfacePoreFluid object in a step. One instance of this object is created internally by the SurfacePoreFluid object for each step. The instance is also deleted internally by the SurfacePoreFluid object.The SurfacePoreFluidState object has no constructor or methods.',
	'SurfaceSection':'The SurfaceSection object defines the properties of a surface section.',
	'SurfaceThicknessAssignment':'The SurfaceThicknessAssignment object stores the surface thickness assignment definition for surfaces in ContactExp and ContactStd objects. The SurfaceThicknessAssignment object has no constructor or members.',
	'SurfaceToSurfaceContactExp':'The SurfaceToSurfaceContactExp object defines surface-to-surface contact during an Abaqus/Explicit analysis.',
	'SurfaceToSurfaceContactStd':'The SurfaceToSurfaceContactStd object defines surface-to-surface contact during an Abaqus/Standard analysis.',
	'SurfaceToSurfaceExpState':'The SurfaceToSurfaceExpState object stores the propagating data for a SurfaceToSurfaceContactExp object. One instance of this object is created internally by the SurfaceToSurfaceContactExp object for each step. The instance is also deleted internally by the SurfaceToSurfaceContactExp object.The SurfaceToSurfaceExpState object has no constructor or methods.',
	'SurfaceToSurfaceStdState':'The SurfaceToSurfaceStdState object stores the propagating data for a SurfaceToSurfaceContactStd object. One instance of this object is created internally by the SurfaceToSurfaceContactStd object for each step. The instance is also deleted internally by the SurfaceToSurfaceContactStd object.The SurfaceToSurfaceStdState object has no constructor or methods.',
	'SurfaceTraction':'The SurfaceTraction object defines surface traction on a region.',
	'SurfaceTractionState':'The SurfaceTractionState object stores the propagating data for a SurfaceTraction object in a step. One instance of this object is created internally by the SurfaceTraction object for each step. The instance is also deleted internally by the SurfaceTraction object.The SurfaceTractionState object has no constructor or methods.',
	'SvgOptions':'The SvgOptions object stores the settings that Abaqus uses when printing in SVG format. The \n      SvgOptions\n      object has no constructor. Abaqus creates the \n      svgOptions\n      member when a session is started.\n   ',
	'Swelling':'The Swelling object specifies time-dependent volumetric swelling for a material.',
	'SymbolDisplayOptions':'The SymbolDisplayOptions object stores settings that specify how the assembly is displayed in a particular viewport. The SymbolDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.',
	'SymbolOptions':'The SymbolOptions object stores values and attributes associated with a symbol plot. The SymbolOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.symbolOptions member when you import the Visualization module. Abaqus creates a symbolOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.symbolOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.SymbolOptions objects are accessed in one of two ways: The default symbol options. These settings are used as defaults when other symbolOptions members are created. These settings can be set to customize user preferences.The symbol options associated with a particular viewport.',
	'SymbolStyle':'The SymbolStyle object is used to define the marker properties to be used when drawing curves.SymbolStyle objects can be created using the methods described below. ',
	'TProfile':'The TProfile object defines the properties of a T profile.',
	'TabularAmplitude':'The TabularAmplitude object defines an amplitude curve as a table of values at convenient points on the time scale.',
	'TangentialBehavior':'The TangentialBehavior object specifies tangential behavior for a connector friction behavior option.',
	'TempDisplacementDynamicsStep':'The TempDisplacementDynamicsStep object is used to perform a dynamic coupled thermal-stress analysis using explicit integration.',
	'Temperature':'The Temperature object stores the data for temperature predefined fields.',
	'TemperatureBC':'The TemperatureBC object stores the data for a temperature boundary condition.',
	'TemperatureBCState':'The TemperatureBCState object stores the propagating data for a temperature boundary condition in a step. One instance of this object is created internally by the TemperatureBC object for each step. The instance is also deleted internally by the TemperatureBC object.The TemperatureBCState object has no constructor or methods.',
	'TemperatureState':'The TemperatureState object stores the propagating data of a temperature in a step. One instance of this object is created internally by the Temperature object for each step.The TemperatureState object has no constructor or methods.',
	'TensionCutOff':'The TensionCutOff object specifies tension cutoff for different material models for example the Mohr-Coulomb plasticity model.',
	'TensionStiffening':'The TensionStiffening object defines the retained tensile stress normal to a crack in a Concrete model.',
	'Text':'The \n      Text \n      object stores the text settings and location of a text annotation.\n   ',
	'TextStyle':'The TextStyle object is used to store the text properties to be used for drawing XY-plot text objects.TextStyle objects are automatically created when creating a chart or can be created with methods described below. ',
	'ThermalConductance':'The ThermalConductance object specifies thermal conductance for a contact interaction property.',
	'Tie':'The Tie object defines two surfaces to be tied together for the duration of a simulation.',
	'TiffOptions':'The TiffOptions object stores the settings that Abaqus uses when printing in \n      TIFF\n      format. The \n      TiffOptions\n      object has no constructor. Abaqus creates the \n      tiffOptions\n      member when a session is started.\n   ',
	'TimePoint':'The TimePoint object defines time points at which\ndata are written to the output database or restart files.',
	'Title':'The Title object is used to store the display attributes of the XYPlot title. An Title object is automatically created when creating a XYPlot object.',
	'TopologyCyclicSymmetry':'The TopologyCyclicSymmetry object defines a topology cyclic symmetry geometric restriction.',
	'TopologyDemoldControl':'The TopologyDemoldControl object defines a topology demold control geometric restriction.',
	'TopologyMemberSize':'The TopologyMemberSize object defines a topology member size geometric restriction.',
	'TopologyOverhangControl':'The TopologyOverhangControl object defines a topology overhang control geometric restriction.',
	'TopologyPlanarSymmetry':'The TopologyPlanarSymmetry object defines a topology planar symmetry geometric restriction.',
	'TopologyPointSymmetry':'The TopologyPointSymmetry object defines a topology point symmetry geometric restriction.',
	'TopologyRotationalSymmetry':'The TopologyRotationalSymmetry object defines a topology rotational symmetry geometric restriction.',
	'TopologyTask':'The TopologyTask object defines a topology task.',
	'Transform':'The \n      MakeSketchTransform \n      method creates a \n      Transform \n      object. The \n      Transform \n      object has no direct constructor. A \n      Transform \n      object is a 4&#215;3 matrix of Floats that represents the transformation from sketch coordinates to assembly coordinates or to part coordinates.\n   ',
	'TransverseShearBeam':'The TransverseShearBeam object defines the transverse shear stiffness properties of a beam section.',
	'TransverseShearShell':'The TransverseShearShell object defines the transverse shear stiffness properties of a shell section.',
	'TrapezoidalProfile':'The TrapezoidalProfile object defines the properties of a trapezoidal profile.',
	'TriaxialTestData':'The TriaxialTestData object provides triaxial test data.',
	'Trs':'The Trs object defines the temperature-time shift for time history viscoelastic analysis.',
	'TrussSection':'The TrussSection object defines the properties of a truss section.',
	'TurnControl':'The TurnControl object defines a turn control geometric restriction.',
	'TwoPointSpringDashpot':'The TwoPointSpringDashpot object defines springs and/or dashpots between two points on a part or an assembly.',
	'TypeBC':'The TypeBC object stores the data for several types of predefined boundary conditions that are commonly used in stress/displacement analyses.',
	'TypeBCState':'The TypeBCState object stores the propagating data for a predefined boundary condition in a step. One instance of this object is created internally by the TypeBC object for each step. The instance is also deleted internally by the TypeBC object.The TypeBCState object has no constructor or methods.',
	'UniaxialTestData':'The UniaxialTestData object provides uniaxial test data (compression and/or tension).',
	'UserAmplitude':'The UserAmplitude object defines an amplitude curve using the UAMP or VUAMP user subroutine.',
	'UserData':'The UserData object contains user-defined XY data. The UserData object has no constructor; it is created automatically when an Odb object is created. ',
	'UserDefinedField':'The UserDefinedField object redefines field variables at a material point.',
	'UserMaterial':'The UserMaterial object defines material constants for use in subroutines UMAT, UMATHT, or VUMAT.',
	'UserOutputVariables':'The UserOutputVariables object specifies the number of user-defined output variables.',
	'UserXYData':'The UserXYData object stores a sequence of pairs and information about the axes.',
	'Velocity':'The Velocity object stores the data for an initial velocity predefined field.',
	'VelocityAdaptiveMeshConstraint':'The VelocityAdaptiveMeshConstraint object stores the data for an Arbitrary Lagrangian Eularian (ALE) style velocity adaptive mesh constraint.',
	'VelocityAdaptiveMeshConstraintState':'The VelocityAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary Lagrangian Eularian (ALE) style velocity adaptive mesh constraint in a step. One instance of this object is created internally by the VelocityAdaptiveMeshConstraint object for each step. The instance is also deleted internally by the VelocityAdaptiveMeshConstraint object.The VelocityAdaptiveMeshConstraintState object has no constructor or methods.',
	'VelocityBC':'The VelocityBC object stores the data for a velocity boundary condition.',
	'VelocityBCState':'The VelocityBCState object stores the propagating data for a velocity boundary condition in a step. One instance of this object is created internally by the VelocityBC object for each step. The instance is also deleted internally by the VelocityBC object.The VelocityBCState object has no constructor or methods.',
	'VelocityBaseMotionBC':'The VelocityBaseMotionBC object stores the data for a velocity base motion boundary condition.',
	'VelocityBaseMotionBCState':'The VelocityBaseMotionBCState object stores the propagating data for a velocity base motion boundary condition in a step. One instance of this object is created internally by the VelocityBaseMotionBC object for each step. The instance is also deleted internally by the VelocityBaseMotionBC object.The VelocityBaseMotionBCState object has no constructor or methods.',
	'VelocityDependence':'The VelocityDependence object specifies the dependence of the permeability of a material on the velocity of fluid flow.',
	'Vertex':'Vertices are point regions of geometry.',
	'VertexArray':'The VertexArray is a sequence of \n      Vertex \n      objects.\n   ',
	'View':'The \n      Session\n      and \n      ViewportView\n      objects store view settings for custom (both predefined and user-defined) views. The paradigm used to define a view is based on a camera analogy. Similar to taking a photograph with a camera, features such as camera position, view direction, orientation, depth of field, and projection are specified to transform three-dimensional views to the screen.\n   The \n      LayerView\n      objects store a transformation matrix used to position the contents of the \n      Layer\n      within a viewport.\n   ',
	'ViewCut':'The ViewCut object is used to store values and attributes associate with ViewCut type objects. ViewCut objects can be created using the methods described below. The methods accessed via the OdbDisplay object cause the ViewCut object to be added to the session.viewports[name].odbDisplay.viewCuts repository.',
	'ViewCutOptions':'The ViewCutOptions object stores values and attributes associated with a view cut plot. The ViewCutOptions object has no constructor command. Abaqus creates a defaultOdbDisplay.viewCutOptions member when you import the Visualization module. Abaqus creates an viewCutOptions member when it creates the OdbDisplay object, using the values from defaultOdbDisplay.viewCutOptions. Abaqus creates the odbDisplay member when a viewport is created, using the values from defaultOdbDisplay.ViewCutOptions objects are accessed in one of two ways:The default view cut options. These settings are used as defaults when other viewCutOptions members are created. These settings can be set to customize user preferences.The view cut options associated with a particular viewport.',
	'ViewerOptions':'The ViewerOptions object specifies options to set the result caching parameters. The ViewerOptions object has no constructor. Abaqus creates the viewerOptions member when a session is started.',
	'Viewport':'A viewport is the container for the graphics generated by the application. The\n      Viewport\n      object stores the various settings that determine how objects are displayed within that viewport.\n   ',
	'ViewportAnnotationOptions':'The \n      ViewportAnnotationOptions \n      object stores settings that control how annotations are rendered in a particular viewport. \n      ViewportAnnotationOptions \n      objects are accessed in one of two ways:\n      The default viewport annotations. These settings are used as defaults when other \n    viewportAnnotationOptions \n    members are created and can be set to customize user preferences.\n The viewport annotations associated with a particular viewport.The \n      ViewportAnnotationOptions \n      object has no constructor; Abaqus creates the \n      defaultViewportAnnotationOptions \n      member when a session is started. When a new viewport is created, the settings are copied from the current viewport.\n   ',
	'ViscoStep':'The ViscoStep object is used to obtain a transient static response in an analysis with time-dependent material behavior (creep, swelling, and viscoelasticity). ',
	'Viscoelastic':'The Viscoelastic object specifies dissipative behavior for use with elasticity.',
	'Viscosity':'The Viscosity object specifies mechanical viscosity.',
	'Viscous':'The Viscous object specifies the viscous properties for a two-layer viscoplastic material model.',
	'VoidNucleation':'The VoidNucleation object defines the nucleation of voids in a porous material.',
	'VoidsRatio':'The VoidsRatio object stores the data for initial void ratios.',
	'VolumetricTestData':'The VolumetricTestData object provides volumetric test data.',
	'WaveReflection':'The WaveReflection object\nis used to define a reflected incident wave field.\nIt can be used only in conjunction with IncidentWave objects.',
	'XFEMCrack':'The XFEMCrack object defines the parameters needed to model crack initiation or crack growth using XFEM technology. Currently only assembly regions are supported.',
	'XFEMCrackGrowth':'The XFEMCrackGrowth object defines the enrichment activation state for an XFEMCrack.',
	'XFEMCrackGrowthState':'The XFEMCrackGrowthState object stores the propagating data of an XFEMCrackGrowth object in a step. One instance of this object is created internally by the XFEMCrackGrowth object for each step. The instance is also deleted internally by the XFEMCrackGrowth object.The XFEMCrackGrowthState object has no constructor or methods.',
	'XYCurve':'The XYCurve object is used to plot X&#8211;Y data and to store its display attributes. ',
	'XYData':'The XYData object is used to store values and attributes associated with XYData type objects.XYData objects can be created using the methods described below. The methods accessed via the Session object cause the XYData object to be added to the session.xyData repository.  Temporary XYData objects will be created if no name is supplied. Temporary XYData objects will be added to the session.xyData repository but automatically deleted when they are not used anymore. Temporary XYData objects are also created as a result of math operations found in the abaqusMath module.',
	'XYPlot':'The XYPlot object is used to display Chart objects.',
	'XYReportOptions':'The XYReportOptions object stores settings used by the writeXYReport method when you write an XYData object to an ASCII file. The XYReportOptions object has no constructor. Abaqus creates the xyReportOptions member when you import the Visualization module.',
}

print_function=None  # (!) real value is "_Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 65536)"

x=None  # (!) real value is "ImportError('No module named docstringLookupGeneratedTable',)"
