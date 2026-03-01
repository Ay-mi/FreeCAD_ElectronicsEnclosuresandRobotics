import FreeCAD as App
import FreeCADGui
import FreeCADGui as Gui
from PySide import QtGui
import PartDesign
import Sketcher
import Part
import os
from BOPTools import BOPFeatures
import PartDesignGui

def run():
    doc = App.ActiveDocument
    if doc is None:
        doc = App.newDocument()

    ### Begin command PartDesign_CompSketches
    doc.addObject('PartDesign::Body','Body')
    # Gui.getDocument('Unnamed4').ActiveView.setActiveObject('pdbody',doc.getObject('Body'),'')
    ### End command PartDesign_CompSketches
    # Gui.Selection.addSelection('Unnamed4','Body','Origin.XY_Plane.')
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch')
    doc.getObject('Sketch').AttachmentSupport = (doc.getObject('XY_Plane'),[''])
    doc.getObject('Sketch').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-15.000000, -15.000000, 0.000000),App.Vector(15.000000, -15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(15.000000, -15.000000, 0.000000),App.Vector(15.000000, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(15.000000, 15.000000, 0.000000),App.Vector(-15.000000, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-15.000000, 15.000000, 0.000000),App.Vector(-15.000000, -15.000000, 0.000000)))
    doc.getObject('Sketch').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(0.000000, 0.000000, 0.000000)))
    doc.getObject('Sketch').addGeometry(constrGeoList,True)
    del constrGeoList

    constraintList = []
    constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
    constraintList.append(Sketcher.Constraint('Horizontal', 0))
    constraintList.append(Sketcher.Constraint('Horizontal', 2))
    constraintList.append(Sketcher.Constraint('Vertical', 1))
    constraintList.append(Sketcher.Constraint('Vertical', 3))
    constraintList.append(Sketcher.Constraint('Symmetric', 2, 1, 0, 1, 4, 1))
    doc.getObject('Sketch').addConstraint(constraintList)
    del constraintList

    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,30.000000)) 
    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,30.000000)) 
    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))


    # Gui.getDocument('Unnamed1').resetEdit()
    App.ActiveDocument.recompute()
    # ActiveSketch = doc.getObject('Sketch')
    # tv = ActiveSketch.ViewObject.TempoVis
    # if tv:
    #   tv.restore()
    # ActiveSketch.ViewObject.TempoVis = None
    # del(tv)
    # del(ActiveSketch)
    # 
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch.')
    doc.recompute()
    ### Begin command PartDesign_Pad
    doc.getObject('Body').newObject('PartDesign::Pad','Pad')
    doc.getObject('Pad').Profile = (doc.getObject('Sketch'), ['',])
    doc.getObject('Pad').Length = 10
    App.ActiveDocument.recompute()
    doc.getObject('Pad').ReferenceAxis = (doc.getObject('Sketch'),['N_Axis'])
    doc.getObject('Sketch').Visibility = False
    App.ActiveDocument.recompute()
    # doc.getObject('Pad').ViewObject.ShapeAppearance=getattr(doc.getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',doc.getObject('Pad').ViewObject.ShapeAppearance)
    # doc.getObject('Pad').ViewObject.LineColor=getattr(doc.getObject('Body').getLinkedObject(True).ViewObject,'LineColor',doc.getObject('Pad').ViewObject.LineColor)
    # doc.getObject('Pad').ViewObject.PointColor=getattr(doc.getObject('Body').getLinkedObject(True).ViewObject,'PointColor',doc.getObject('Pad').ViewObject.PointColor)
    # doc.getObject('Pad').ViewObject.Transparency=getattr(doc.getObject('Body').getLinkedObject(True).ViewObject,'Transparency',doc.getObject('Pad').ViewObject.Transparency)
    # doc.getObject('Pad').ViewObject.DisplayMode=getattr(doc.getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',doc.getObject('Pad').ViewObject.DisplayMode)
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Pad.')
    # Gui.Selection.clearSelection()
    ### End command PartDesign_Pad
    # Gui.Selection.clearSelection()
    doc.getObject('Pad').Length = 50.000000
    doc.getObject('Pad').TaperAngle = 0.000000
    doc.getObject('Pad').UseCustomVector = 0
    doc.getObject('Pad').Direction = (0, 0, 1)
    doc.getObject('Pad').ReferenceAxis = (doc.getObject('Sketch'), ['N_Axis'])
    doc.getObject('Pad').AlongSketchNormal = 1
    doc.getObject('Pad').Type = 0
    doc.getObject('Pad').UpToFace = None
    doc.getObject('Pad').Reversed = 0
    doc.getObject('Pad').Midplane = 0
    doc.getObject('Pad').Offset = 0
    ###doc.purgeTouched()
    doc.recompute()
    # Gui.getDocument('Unnamed1').resetEdit()
    doc.getObject('Sketch').Visibility = False
    # Gui.Selection.addSelection('Unnamed1','Body','Pad.Face6',1.90952,-0.134225,50)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
    doc.getObject('Sketch001').AttachmentSupport = (doc.getObject('Pad'),['Face6',])
    doc.getObject('Sketch001').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Sketch001.')
    # ActiveSketch = doc.getObject('Sketch001')
    # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
    # ActiveSketch.ViewObject.TempoVis = tv
    # if ActiveSketch.ViewObject.EditingWorkbench:
    #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
    # if ActiveSketch.ViewObject.HideDependent:
    #   tv.hide(tv.get_all_dependent(doc.getObject('Body'), 'Sketch001.'))
    # if ActiveSketch.ViewObject.ShowSupport:
    #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
    # if ActiveSketch.ViewObject.ShowLinks:
    #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
    # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
    # tv.hide(ActiveSketch)
    # del(tv)
    # del(ActiveSketch)
    # 
    # ActiveSketch = doc.getObject('Sketch001')
    # if ActiveSketch.ViewObject.RestoreCamera:
    #   ActiveSketch.ViewObject.TempoVis.saveCamera()
    #   if ActiveSketch.ViewObject.ForceOrtho:
    #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
    # 
    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch001')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-11.449354, -15.000000, 0.000000),App.Vector(-6.449354, -15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-6.449354, -15.000000, 0.000000),App.Vector(-6.449354, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-6.449354, 15.000000, 0.000000),App.Vector(-11.449354, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-11.449354, 15.000000, 0.000000),App.Vector(-11.449354, -15.000000, 0.000000)))
    doc.getObject('Sketch001').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(-8.949354, 0.000000, 0.000000)))
    doc.getObject('Sketch001').addGeometry(constrGeoList,True)
    del constrGeoList

    constraintList = []
    constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
    constraintList.append(Sketcher.Constraint('Horizontal', 0))
    constraintList.append(Sketcher.Constraint('Horizontal', 2))
    constraintList.append(Sketcher.Constraint('Vertical', 1))
    constraintList.append(Sketcher.Constraint('Vertical', 3))
    constraintList.append(Sketcher.Constraint('Symmetric', 2, 1, 0, 1, 4, 1))
    doc.getObject('Sketch001').addConstraint(constraintList)
    del constraintList

    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,5.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,30.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('PointOnObject', 4, 1, -1))


    # Gui.Selection.addSelection('Unnamed1','Body','Sketch001.Edge2',-6.44935,7.88408,50.008,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch001.V_Axis',0,7.88408,50.002,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',-2,1,1,6.449354)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch001').setDatum(12,App.Units.Quantity('10.000000 mm'))
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch001')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(3.391637, -15.000000, 0.000000),App.Vector(8.391637, -15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(8.391637, -15.000000, 0.000000),App.Vector(8.391637, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(8.391637, 15.000000, 0.000000),App.Vector(3.391637, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(3.391637, 15.000000, 0.000000),App.Vector(3.391637, -15.000000, 0.000000)))
    doc.getObject('Sketch001').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(5.891637, 0.000000, 0.000000)))
    doc.getObject('Sketch001').addGeometry(constrGeoList,True)
    del constrGeoList

    constraintList = []
    constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 6, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 6, 2, 7, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 8, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 8, 2, 5, 1))
    constraintList.append(Sketcher.Constraint('Horizontal', 5))
    constraintList.append(Sketcher.Constraint('Horizontal', 7))
    constraintList.append(Sketcher.Constraint('Vertical', 6))
    constraintList.append(Sketcher.Constraint('Vertical', 8))
    constraintList.append(Sketcher.Constraint('Symmetric', 7, 1, 5, 1, 9, 1))
    doc.getObject('Sketch001').addConstraint(constraintList)
    del constraintList

    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',6,1,8,2,5.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',5,1,7,2,30.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('PointOnObject', 9, 1, -1))


    # Gui.Selection.addSelection('Unnamed1','Body','Sketch001.Edge9',3.39164,9.82754,50.008,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch001.V_Axis',0,12.301,50.002,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',-2,1,8,3.391637)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch001').setDatum(25,App.Units.Quantity('10.000000 mm'))
    # Gui.getDocument('Unnamed1').resetEdit()
    App.ActiveDocument.recompute()
    # ActiveSketch = doc.getObject('Sketch001')
    # tv = ActiveSketch.ViewObject.TempoVis
    # if tv:
    #   tv.restore()
    # ActiveSketch.ViewObject.TempoVis = None
    # del(tv)
    # del(ActiveSketch)
    # 
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch001.')
    doc.recompute()
    ### Begin command PartDesign_Pad
    doc.getObject('Body').newObject('PartDesign::Pad','Pad001')
    doc.getObject('Pad001').Profile = (doc.getObject('Sketch001'), ['',])
    doc.getObject('Pad001').Length = 10
    App.ActiveDocument.recompute()
    doc.getObject('Pad001').ReferenceAxis = (doc.getObject('Sketch001'),['N_Axis'])
    doc.getObject('Sketch001').Visibility = False
    App.ActiveDocument.recompute()
    # doc.getObject('Pad001').ViewObject.ShapeAppearance=getattr(doc.getObject('Pad').getLinkedObject(True).ViewObject,'ShapeAppearance',doc.getObject('Pad001').ViewObject.ShapeAppearance)
    # doc.getObject('Pad001').ViewObject.LineColor=getattr(doc.getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',doc.getObject('Pad001').ViewObject.LineColor)
    # doc.getObject('Pad001').ViewObject.PointColor=getattr(doc.getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',doc.getObject('Pad001').ViewObject.PointColor)
    # doc.getObject('Pad001').ViewObject.Transparency=getattr(doc.getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',doc.getObject('Pad001').ViewObject.Transparency)
    # doc.getObject('Pad001').ViewObject.DisplayMode=getattr(doc.getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',doc.getObject('Pad001').ViewObject.DisplayMode)
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Pad001.')
    # Gui.Selection.clearSelection()
    ### End command PartDesign_Pad
    # Gui.Selection.clearSelection()
    doc.getObject('Pad001').Length = 20.000000
    doc.getObject('Pad001').TaperAngle = 0.000000
    doc.getObject('Pad001').UseCustomVector = 0
    doc.getObject('Pad001').Direction = (0, 0, 1)
    doc.getObject('Pad001').ReferenceAxis = (doc.getObject('Sketch001'), ['N_Axis'])
    doc.getObject('Pad001').AlongSketchNormal = 1
    doc.getObject('Pad001').Type = 0
    doc.getObject('Pad001').UpToFace = None
    doc.getObject('Pad001').Reversed = 0
    doc.getObject('Pad001').Midplane = 0
    doc.getObject('Pad001').Offset = 0
    ###doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad').Visibility = False
    # Gui.getDocument('Unnamed1').resetEdit()
    doc.getObject('Sketch001').Visibility = False
    # Gui.Selection.addSelection('Unnamed1','Body','Pad001.Face9',15,7.12198,53.4067)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
    doc.getObject('Sketch002').AttachmentSupport = (doc.getObject('Pad001'),['Face9',])
    doc.getObject('Sketch002').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Sketch002.')
    # ActiveSketch = doc.getObject('Sketch002')
    # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
    # ActiveSketch.ViewObject.TempoVis = tv
    # if ActiveSketch.ViewObject.EditingWorkbench:
    #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
    # if ActiveSketch.ViewObject.HideDependent:
    #   tv.hide(tv.get_all_dependent(doc.getObject('Body'), 'Sketch002.'))
    # if ActiveSketch.ViewObject.ShowSupport:
    #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
    # if ActiveSketch.ViewObject.ShowLinks:
    #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
    # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
    # tv.hide(ActiveSketch)
    # del(tv)
    # del(ActiveSketch)
    # 
    # ActiveSketch = doc.getObject('Sketch002')
    # if ActiveSketch.ViewObject.RestoreCamera:
    #   ActiveSketch.ViewObject.TempoVis.saveCamera()
    #   if ActiveSketch.ViewObject.ForceOrtho:
    #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
    # 
    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateConic',0)
    ActiveSketch = doc.getObject('Sketch002')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.Circle(App.Vector(0.000000, 60.386612, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 2.500000))
    doc.getObject('Sketch002').addGeometry(geoList,False)
    del geoList

    constraintList = []
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Diameter',0,5.000000)) 
    constraintList = []
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch002.Vertex1',15.014,0,60.3866,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch002.H_Axis',15.002,22.3751,0,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,3,-1,60.386612)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch002').setDatum(1,App.Units.Quantity('60.000000 mm'))
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch002.Vertex1',15.014,0,60,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch002.V_Axis',15.002,0,63.7293,False)
    ### Begin command Sketcher_ConstrainCoincidentUnified
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2))
    ### End command Sketcher_ConstrainCoincidentUnified
    # Gui.Selection.clearSelection()
    # Gui.getDocument('Unnamed1').resetEdit()
    App.ActiveDocument.recompute()
    # ActiveSketch = doc.getObject('Sketch002')
    # tv = ActiveSketch.ViewObject.TempoVis
    # if tv:
    #   tv.restore()
    # ActiveSketch.ViewObject.TempoVis = None
    # del(tv)
    # del(ActiveSketch)
    # 
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch002.')
    doc.recompute()
    ### Begin command PartDesign_Pocket
    doc.getObject('Body').newObject('PartDesign::Pocket','Pocket')
    doc.getObject('Pocket').Profile = (doc.getObject('Sketch002'), ['',])
    doc.getObject('Pocket').Length = 5
    App.ActiveDocument.recompute()
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch002'),['N_Axis'])
    doc.getObject('Sketch002').Visibility = False
    App.ActiveDocument.recompute()
    # doc.getObject('Pocket').ViewObject.ShapeAppearance=getattr(doc.getObject('Pad001').getLinkedObject(True).ViewObject,'ShapeAppearance',doc.getObject('Pocket').ViewObject.ShapeAppearance)
    # doc.getObject('Pocket').ViewObject.LineColor=getattr(doc.getObject('Pad001').getLinkedObject(True).ViewObject,'LineColor',doc.getObject('Pocket').ViewObject.LineColor)
    # doc.getObject('Pocket').ViewObject.PointColor=getattr(doc.getObject('Pad001').getLinkedObject(True).ViewObject,'PointColor',doc.getObject('Pocket').ViewObject.PointColor)
    # doc.getObject('Pocket').ViewObject.Transparency=getattr(doc.getObject('Pad001').getLinkedObject(True).ViewObject,'Transparency',doc.getObject('Pocket').ViewObject.Transparency)
    # doc.getObject('Pocket').ViewObject.DisplayMode=getattr(doc.getObject('Pad001').getLinkedObject(True).ViewObject,'DisplayMode',doc.getObject('Pocket').ViewObject.DisplayMode)
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Pocket.')
    # Gui.Selection.clearSelection()
    ### End command PartDesign_Pocket
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket').Length = 20.000000
    doc.getObject('Pocket').TaperAngle = 0.000000
    doc.getObject('Pocket').UseCustomVector = 0
    doc.getObject('Pocket').Direction = (-1, 0, 0)
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch002'), ['N_Axis'])
    doc.getObject('Pocket').AlongSketchNormal = 1
    doc.getObject('Pocket').Type = 0
    doc.getObject('Pocket').UpToFace = None
    doc.getObject('Pocket').Reversed = 0
    doc.getObject('Pocket').Midplane = 0
    doc.getObject('Pocket').Offset = 0
    ###doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad001').Visibility = False
    # Gui.getDocument('Unnamed1').resetEdit()
    doc.getObject('Sketch002').Visibility = False
    # Gui.Selection.addSelection('Unnamed1','Body','Pocket.')
    # Gui.ActiveDocument.setEdit(doc.getObject('Pocket'), 0)
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket').Length = 35.000000
    doc.getObject('Pocket').TaperAngle = 0.000000
    doc.getObject('Pocket').UseCustomVector = 0
    doc.getObject('Pocket').Direction = (-1, 0, 0)
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch002'), ['N_Axis'])
    doc.getObject('Pocket').AlongSketchNormal = 1
    doc.getObject('Pocket').Type = 0
    doc.getObject('Pocket').UpToFace = None
    doc.getObject('Pocket').Reversed = 0
    doc.getObject('Pocket').Midplane = 0
    doc.getObject('Pocket').Offset = 0
    ###doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad001').Visibility = False
    # Gui.getDocument('Unnamed1').resetEdit()
    doc.getObject('Sketch002').Visibility = False

    # Gui.Selection.addSelection('Unnamed1','Body','Pocket.Face1',5.57631,4.69781,0)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch003')
    doc.getObject('Sketch003').AttachmentSupport = (doc.getObject('Pocket'),['Face1',])
    doc.getObject('Sketch003').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Sketch003.')
    # ActiveSketch = doc.getObject('Sketch003')
    # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
    # ActiveSketch.ViewObject.TempoVis = tv
    # if ActiveSketch.ViewObject.EditingWorkbench:
    #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
    # if ActiveSketch.ViewObject.HideDependent:
    #   tv.hide(tv.get_all_dependent(doc.getObject('Body'), 'Sketch003.'))
    # if ActiveSketch.ViewObject.ShowSupport:
    #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
    # if ActiveSketch.ViewObject.ShowLinks:
    #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
    # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
    # tv.hide(ActiveSketch)
    # del(tv)
    # del(ActiveSketch)
    # 
    # ActiveSketch = doc.getObject('Sketch003')
    # if ActiveSketch.ViewObject.RestoreCamera:
    #   ActiveSketch.ViewObject.TempoVis.saveCamera()
    #   if ActiveSketch.ViewObject.ForceOrtho:
    #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
    # 
    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch003')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-8.862247, -15.000000, 0.000000),App.Vector(-6.362247, -15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-6.362247, -15.000000, 0.000000),App.Vector(-6.362247, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-6.362247, 15.000000, 0.000000),App.Vector(-8.862247, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-8.862247, 15.000000, 0.000000),App.Vector(-8.862247, -15.000000, 0.000000)))
    doc.getObject('Sketch003').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(-7.612247, 0.000000, 0.000000)))
    doc.getObject('Sketch003').addGeometry(constrGeoList,True)
    del constrGeoList

    constraintList = []
    constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
    constraintList.append(Sketcher.Constraint('Horizontal', 0))
    constraintList.append(Sketcher.Constraint('Horizontal', 2))
    constraintList.append(Sketcher.Constraint('Vertical', 1))
    constraintList.append(Sketcher.Constraint('Vertical', 3))
    constraintList.append(Sketcher.Constraint('Symmetric', 2, 1, 0, 1, 4, 1))
    doc.getObject('Sketch003').addConstraint(constraintList)
    del constraintList

    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,2.500000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,30.000000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('PointOnObject', 4, 1, -1))


    # Gui.Selection.addSelection('Unnamed1','Body','Sketch003.Edge2',-6.36225,-9.52797,-0.008,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch003.V_Axis',0,-7.93786,-0.002,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',-2,1,1,6.362247)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(12,App.Units.Quantity('6.000000 mm'))
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch003')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(8.982269, -15.000000, 0.000000),App.Vector(11.482269, -15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(11.482269, -15.000000, 0.000000),App.Vector(11.482269, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(11.482269, 15.000000, 0.000000),App.Vector(8.982269, 15.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(8.982269, 15.000000, 0.000000),App.Vector(8.982269, -15.000000, 0.000000)))
    doc.getObject('Sketch003').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(10.232269, 0.000000, 0.000000)))
    doc.getObject('Sketch003').addGeometry(constrGeoList,True)
    del constrGeoList

    constraintList = []
    constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 6, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 6, 2, 7, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 8, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 8, 2, 5, 1))
    constraintList.append(Sketcher.Constraint('Horizontal', 5))
    constraintList.append(Sketcher.Constraint('Horizontal', 7))
    constraintList.append(Sketcher.Constraint('Vertical', 6))
    constraintList.append(Sketcher.Constraint('Vertical', 8))
    constraintList.append(Sketcher.Constraint('Symmetric', 7, 1, 5, 1, 9, 1))
    doc.getObject('Sketch003').addConstraint(constraintList)
    del constraintList

    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',6,1,8,2,2.500000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',5,1,7,2,30.000000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('PointOnObject', 9, 1, -1))


    # Gui.Selection.addSelection('Unnamed1','Body','Sketch003.Edge9',8.98227,-7.23115,-0.008,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch003.V_Axis',0,-9.17461,-0.002,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',-2,1,8,8.982269)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(25,App.Units.Quantity('6.000000 mm'))
    # Gui.getDocument('Unnamed1').resetEdit()
    App.ActiveDocument.recompute()
    # ActiveSketch = doc.getObject('Sketch003')
    # tv = ActiveSketch.ViewObject.TempoVis
    # if tv:
    #   tv.restore()
    # ActiveSketch.ViewObject.TempoVis = None
    # del(tv)
    # del(ActiveSketch)
    # 
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch003.')
    doc.recompute()
    ### Begin command PartDesign_Pad
    doc.getObject('Body').newObject('PartDesign::Pad','Pad002')
    doc.getObject('Pad002').Profile = (doc.getObject('Sketch003'), ['',])
    doc.getObject('Pad002').Length = 10
    App.ActiveDocument.recompute()
    doc.getObject('Pad002').ReferenceAxis = (doc.getObject('Sketch003'),['N_Axis'])
    doc.getObject('Sketch003').Visibility = False
    App.ActiveDocument.recompute()
    # doc.getObject('Pad002').ViewObject.ShapeAppearance=getattr(doc.getObject('Pocket').getLinkedObject(True).ViewObject,'ShapeAppearance',doc.getObject('Pad002').ViewObject.ShapeAppearance)
    # doc.getObject('Pad002').ViewObject.LineColor=getattr(doc.getObject('Pocket').getLinkedObject(True).ViewObject,'LineColor',doc.getObject('Pad002').ViewObject.LineColor)
    # doc.getObject('Pad002').ViewObject.PointColor=getattr(doc.getObject('Pocket').getLinkedObject(True).ViewObject,'PointColor',doc.getObject('Pad002').ViewObject.PointColor)
    # doc.getObject('Pad002').ViewObject.Transparency=getattr(doc.getObject('Pocket').getLinkedObject(True).ViewObject,'Transparency',doc.getObject('Pad002').ViewObject.Transparency)
    # doc.getObject('Pad002').ViewObject.DisplayMode=getattr(doc.getObject('Pocket').getLinkedObject(True).ViewObject,'DisplayMode',doc.getObject('Pad002').ViewObject.DisplayMode)
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Pad002.')
    # Gui.Selection.clearSelection()
    ### End command PartDesign_Pad
    # Gui.Selection.clearSelection()
    doc.getObject('Pad002').Length = 20.000000
    doc.getObject('Pad002').TaperAngle = 0.000000
    doc.getObject('Pad002').UseCustomVector = 0
    doc.getObject('Pad002').Direction = (0, 0, -1)
    doc.getObject('Pad002').ReferenceAxis = (doc.getObject('Sketch003'), ['N_Axis'])
    doc.getObject('Pad002').AlongSketchNormal = 1
    doc.getObject('Pad002').Type = 0
    doc.getObject('Pad002').UpToFace = None
    doc.getObject('Pad002').Reversed = 0
    doc.getObject('Pad002').Midplane = 0
    doc.getObject('Pad002').Offset = 0
    ##doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pocket').Visibility = False
    # Gui.getDocument('Unnamed1').resetEdit()
    doc.getObject('Sketch003').Visibility = False
    # Gui.Selection.addSelection('Unnamed1','Body','Pad002.Edge43',8.5,-4.34135,-20)
    # Gui.Selection.clearSelection()
    # Gui.Selection.addSelection('Unnamed1','Body','Pad002.Face14',8.5,6.59543,-4.52361)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch004')
    doc.getObject('Sketch004').AttachmentSupport = (doc.getObject('Pad002'),['Face14',])
    doc.getObject('Sketch004').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    # Gui.getDocument('Unnamed1').setEdit(doc.getObject('Body'), 0, 'Sketch004.')
    # ActiveSketch = doc.getObject('Sketch004')
    # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
    # ActiveSketch.ViewObject.TempoVis = tv
    # if ActiveSketch.ViewObject.EditingWorkbench:
    #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
    # if ActiveSketch.ViewObject.HideDependent:
    #   tv.hide(tv.get_all_dependent(doc.getObject('Body'), 'Sketch004.'))
    # if ActiveSketch.ViewObject.ShowSupport:
    #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
    # if ActiveSketch.ViewObject.ShowLinks:
    #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
    # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
    # tv.hide(ActiveSketch)
    # del(tv)
    # del(ActiveSketch)
    # 
    # ActiveSketch = doc.getObject('Sketch004')
    # if ActiveSketch.ViewObject.RestoreCamera:
    #   ActiveSketch.ViewObject.TempoVis.saveCamera()
    #   if ActiveSketch.ViewObject.ForceOrtho:
    #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
    # 
    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateConic',0)
    ActiveSketch = doc.getObject('Sketch004')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.Circle(App.Vector(0.000000, -12.798752, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 2.750000))
    doc.getObject('Sketch004').addGeometry(geoList,False)
    del geoList

    constraintList = []
    doc.getObject('Sketch004').addConstraint(Sketcher.Constraint('Diameter',0,5.500000)) 
    constraintList = []
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch004.Vertex1',8.514,0,-12.7988,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch004.H_Axis',8.502,7.96929,0,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch004').addConstraint(Sketcher.Constraint('Distance',0,3,-1,12.798752)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch004').setDatum(1,App.Units.Quantity('14.500000 mm'))
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch004.Vertex1',8.514,0,-14.5,False)
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch004.V_Axis',8.502,0,-9.43714,False)
    ### Begin command Sketcher_ConstrainCoincidentUnified
    doc.getObject('Sketch004').addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2))
    ### End command Sketcher_ConstrainCoincidentUnified
    # Gui.Selection.clearSelection()
    # Gui.getDocument('Unnamed1').resetEdit()
    App.ActiveDocument.recompute()
    # ActiveSketch = doc.getObject('Sketch004')
    # tv = ActiveSketch.ViewObject.TempoVis
    # if tv:
    #   tv.restore()
    # ActiveSketch.ViewObject.TempoVis = None
    # del(tv)
    # del(ActiveSketch)
    # 
    # Gui.Selection.addSelection('Unnamed1','Body','Sketch004.')
    doc.recompute()
    ### Begin command PartDesign_Pocket
    doc.getObject('Body').newObject('PartDesign::Pocket','Pocket001')
    doc.getObject('Pocket001').Profile = (doc.getObject('Sketch004'), ['',])
    doc.getObject('Pocket001').Length = 5
    App.ActiveDocument.recompute()
    doc.getObject('Pocket001').ReferenceAxis = (doc.getObject('Sketch004'),['N_Axis'])
    doc.getObject('Sketch004').Visibility = False
    App.ActiveDocument.recompute()
    ### End command PartDesign_Pocket
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket001').Length = 35.000000
    doc.getObject('Pocket001').TaperAngle = 0.000000
    doc.getObject('Pocket001').UseCustomVector = 0
    doc.getObject('Pocket001').Direction = (-1, 0, 0)
    doc.getObject('Pocket001').ReferenceAxis = (doc.getObject('Sketch004'), ['N_Axis'])
    doc.getObject('Pocket001').AlongSketchNormal = 1
    doc.getObject('Pocket001').Type = 0
    doc.getObject('Pocket001').UpToFace = None
    doc.getObject('Pocket001').Reversed = 0
    doc.getObject('Pocket001').Midplane = 0
    doc.getObject('Pocket001').Offset = 0
    ##doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad002').Visibility = False
    # Gui.getDocument('Unnamed1').resetEdit()
    doc.getObject('Sketch004').Visibility = False


    ### Begin command PartDesign_Fillet
    doc.getObject('Body').newObject('PartDesign::Fillet','Fillet')
    doc.getObject('Fillet').Base = (doc.getObject('Pocket001'),['Edge12',])
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket001').Visibility = False
    App.ActiveDocument.recompute()
    ### End command PartDesign_Fillet
    doc.getObject('Fillet').Radius = 11.000000
    doc.getObject('Fillet').Base = (doc.getObject('Pocket001'),["Edge12",])
    ##doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pocket001').Visibility = False

    doc.getObject('Fillet').Radius = 11.000000
    doc.getObject('Fillet').Base = (doc.getObject('Pocket001'),["Edge12","Edge26","Edge30","Edge8","Edge34","Edge19","Edge15","Edge23",])
    ##doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pocket001').Visibility = False


class EnclosureMacro9_Command_Class:
    def GetResources(self):
        mod_dir = App.getUserAppDataDir()
        icon_path = os.path.join(
            mod_dir,
            "Mod",
            "ElectronicsEnclosures",
            "Resources",
            "icons",
            "arm_linkv1.svg"
        )

        # App.Console.PrintMessage("ICON PATH: {}\n".format(icon_path))
        # App.Console.PrintMessage("ICON EXISTS: {}\n".format(os.path.exists(icon_path)))

        return {
            'Pixmap': icon_path,
            'MenuText': 'Create Robot Arm Link Type 1',
            'ToolTip': 'Creates a robot arm link that can be assembled with the arm base.'
        }

    def Activated(self):
        run()

    def IsActive(self):
        return True

FreeCADGui.addCommand('robot_arm', EnclosureMacro9_Command_Class())
