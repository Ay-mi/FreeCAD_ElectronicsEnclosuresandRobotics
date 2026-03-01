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
    ### End command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch')
    doc.getObject('Sketch').AttachmentSupport = (doc.getObject('XY_Plane'),[''])
    doc.getObject('Sketch').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    ActiveSketch = doc.getObject('Sketch')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-37.500000, -20.000000, 0.000000),App.Vector(37.500000, -20.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(37.500000, -20.000000, 0.000000),App.Vector(37.500000, 20.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(37.500000, 20.000000, 0.000000),App.Vector(-37.500000, 20.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-37.500000, 20.000000, 0.000000),App.Vector(-37.500000, -20.000000, 0.000000)))
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

    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,75.000000)) 
    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,40.000000)) 
    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))


    App.ActiveDocument.recompute()

    ### Begin command PartDesign_Pad
    doc.getObject('Body').newObject('PartDesign::Pad','Pad')
    doc.getObject('Pad').Profile = (doc.getObject('Sketch'), ['',])
    doc.getObject('Pad').Length = 10
    App.ActiveDocument.recompute()
    doc.getObject('Pad').ReferenceAxis = (doc.getObject('Sketch'),['N_Axis'])
    doc.getObject('Sketch').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Pad
    # Gui.Selection.clearSelection()
    doc.getObject('Pad').Length = 17.000000
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
    doc.recompute()
    # doc.resetEdit()
    doc.getObject('Sketch').Visibility = False
    # Gui.Selection.addSelection('Unnamed3','Body','Pad.Face6',-17.3803,-10.5836,17)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
    doc.getObject('Sketch001').AttachmentSupport = (doc.getObject('Pad'),['Face6',])
    doc.getObject('Sketch001').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch001')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-35.000000, -17.500000, 0.000000),App.Vector(35.000000, -17.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(35.000000, -17.500000, 0.000000),App.Vector(35.000000, 17.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(35.000000, 17.500000, 0.000000),App.Vector(-35.000000, 17.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-35.000000, 17.500000, 0.000000),App.Vector(-35.000000, -17.500000, 0.000000)))
    doc.getObject('Sketch001').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(0.000000, 0.000000, 0.000000)))
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

    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,70.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,35.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))


    App.ActiveDocument.recompute()

    ### Begin command PartDesign_Pocket
    doc.getObject('Body').newObject('PartDesign::Pocket','Pocket')
    doc.getObject('Pocket').Profile = (doc.getObject('Sketch001'), ['',])
    doc.getObject('Pocket').Length = 5
    App.ActiveDocument.recompute()
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch001'),['N_Axis'])
    doc.getObject('Sketch001').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Pocket
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket').Length = 12.000000
    doc.getObject('Pocket').TaperAngle = 0.000000
    doc.getObject('Pocket').UseCustomVector = 0
    doc.getObject('Pocket').Direction = (0, 0, -1)
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch001'), ['N_Axis'])
    doc.getObject('Pocket').AlongSketchNormal = 1
    doc.getObject('Pocket').Type = 0
    doc.getObject('Pocket').UpToFace = None
    doc.getObject('Pocket').Reversed = 0
    doc.getObject('Pocket').Midplane = 0
    doc.getObject('Pocket').Offset = 0
    doc.recompute()
    doc.getObject('Pad').Visibility = False
    # doc.resetEdit()
    doc.getObject('Sketch001').Visibility = False
    # Gui.Selection.addSelection('Unnamed3','Body','Pocket.Edge15',-3.07436,17.5,17)
    ### Begin command PartDesign_Chamfer
    doc.getObject('Body').newObject('PartDesign::Chamfer','Chamfer')
    doc.getObject('Chamfer').Base = (doc.getObject('Pocket'),['Edge15',])
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Chamfer

    doc.getObject('Chamfer').Size = 2.000000
    doc.getObject('Chamfer').Base = (doc.getObject('Pocket'),["Edge15","Edge16","Edge13","Edge14",])
    doc.recompute()
    doc.getObject('Pocket').Visibility = False
    # doc.resetEdit()
    # Gui.Selection.addSelection('Unnamed3','Body','Chamfer.Face6',-21.7075,-20,5.45255)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
    doc.getObject('Sketch002').AttachmentSupport = (doc.getObject('Chamfer'),['Face6',])
    doc.getObject('Sketch002').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch002')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-30.440777, 3.806386, 0.000000),App.Vector(-17.440777, 3.806386, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-17.440777, 3.806386, 0.000000),App.Vector(-17.440777, 8.806386, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-17.440777, 8.806386, 0.000000),App.Vector(-30.440777, 8.806386, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-30.440777, 8.806386, 0.000000),App.Vector(-30.440777, 3.806386, 0.000000)))
    doc.getObject('Sketch002').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(-23.940777, 6.306386, 0.000000)))
    doc.getObject('Sketch002').addGeometry(constrGeoList,True)
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
    doc.getObject('Sketch002').addConstraint(constraintList)
    del constraintList

    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,13.000000)) 
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,5.000000)) 
    constraintList = []
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch002.Edge2',-17.4408,-20.008,5.31036,False)
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch002.V_Axis',0,-20.002,6.30639,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',-2,1,1,17.440777)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch002').setDatum(11,App.Units.Quantity('13.500000 mm'))
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch002.Edge1',-16.6698,-20.008,3.71686,False)
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch002.H_Axis',-11.8888,-20.002,-2.38419e-10,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',-1,1,0,3.716855)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch002').setDatum(12,App.Units.Quantity('6.500000 mm'))
    App.ActiveDocument.recompute()

    ### Begin command PartDesign_Pocket
    doc.getObject('Body').newObject('PartDesign::Pocket','Pocket001')
    doc.getObject('Pocket001').Profile = (doc.getObject('Sketch002'), ['',])
    doc.getObject('Pocket001').Length = 5
    App.ActiveDocument.recompute()
    doc.getObject('Pocket001').ReferenceAxis = (doc.getObject('Sketch002'),['N_Axis'])
    doc.getObject('Sketch002').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Pocket
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket001').Length = 5.000000
    doc.getObject('Pocket001').TaperAngle = 0.000000
    doc.getObject('Pocket001').UseCustomVector = 0
    doc.getObject('Pocket001').Direction = (0, 1, -0)
    doc.getObject('Pocket001').ReferenceAxis = (doc.getObject('Sketch002'), ['N_Axis'])
    doc.getObject('Pocket001').AlongSketchNormal = 1
    doc.getObject('Pocket001').Type = 0
    doc.getObject('Pocket001').UpToFace = None
    doc.getObject('Pocket001').Reversed = 0
    doc.getObject('Pocket001').Midplane = 0
    doc.getObject('Pocket001').Offset = 0
    doc.recompute()
    doc.getObject('Chamfer').Visibility = False
    # doc.resetEdit()
    doc.getObject('Sketch002').Visibility = False
    # Gui.Selection.addSelection('Unnamed3','Body','Pocket001.Face6',3.38886,-20,9.27162)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch003')
    doc.getObject('Sketch003').AttachmentSupport = (doc.getObject('Pocket001'),['Face6',])
    doc.getObject('Sketch003').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    

    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch003')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(11.250021, 5.103041, 0.000000),App.Vector(20.750021, 5.103041, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(20.750021, 5.103041, 0.000000),App.Vector(20.750021, 9.103041, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(20.750021, 9.103041, 0.000000),App.Vector(11.250021, 9.103041, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(11.250021, 9.103041, 0.000000),App.Vector(11.250021, 5.103041, 0.000000)))
    doc.getObject('Sketch003').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(16.000021, 7.103041, 0.000000)))
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

    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,9.500000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,4.000000)) 
    constraintList = []
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.Edge1',13.7092,-20.008,5.10304,False)
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.H_Axis',15.1036,-20.002,-2.38419e-10,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',-1,1,0,5.103041)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(11,App.Units.Quantity('6.500000 mm'))
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.Edge4',11.1981,-20.008,8.29827,False)
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.V_Axis',0,-20.002,14.7725,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',-2,1,3,11.198130)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(12,App.Units.Quantity('4.000000 mm'))
    # Gui.runCommand('Sketcher_CompCreateRectangles',1)
    ActiveSketch = doc.getObject('Sketch003')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(17.923410, 6.497479, 0.000000),App.Vector(27.423410, 6.497479, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(27.423410, 6.497479, 0.000000),App.Vector(27.423410, 10.497479, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(27.423410, 10.497479, 0.000000),App.Vector(17.923410, 10.497479, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(17.923410, 10.497479, 0.000000),App.Vector(17.923410, 6.497479, 0.000000)))
    doc.getObject('Sketch003').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(22.673410, 8.497479, 0.000000)))
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

    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',6,1,8,2,9.500000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',5,1,7,2,4.000000)) 
    constraintList = []
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.Edge6',20.1833,-20.008,6.49748,False)
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.H_Axis',35.1238,-20.002,-2.38419e-10,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',-1,1,5,6.497479)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(24,App.Units.Quantity('6.500000 mm'))
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.Edge9',17.9234,-20.008,8.69669,False)
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.V_Axis',0,-20.002,9.49351,False)
    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',-2,1,8,17.923410)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(25,App.Units.Quantity('16.800000 mm'))
    # doc.resetEdit()
    App.ActiveDocument.recompute()
    # ActiveSketch = doc.getObject('Sketch003')
    # tv = ActiveSketch.ViewObject.TempoVis
    # if tv:
    #   tv.restore()
    # ActiveSketch.ViewObject.TempoVis = None
    # del(tv)
    # del(ActiveSketch)
    # 
    # Gui.Selection.addSelection('Unnamed3','Body','Sketch003.')
    doc.recompute()
    ### Begin command PartDesign_Pocket
    doc.getObject('Body').newObject('PartDesign::Pocket','Pocket002')
    doc.getObject('Pocket002').Profile = (doc.getObject('Sketch003'), ['',])
    doc.getObject('Pocket002').Length = 5
    App.ActiveDocument.recompute()
    doc.getObject('Pocket002').ReferenceAxis = (doc.getObject('Sketch003'),['N_Axis'])
    doc.getObject('Sketch003').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Pocket
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket002').Length = 5.000000
    doc.getObject('Pocket002').TaperAngle = 0.000000
    doc.getObject('Pocket002').UseCustomVector = 0
    doc.getObject('Pocket002').Direction = (0, 1, -0)
    doc.getObject('Pocket002').ReferenceAxis = (doc.getObject('Sketch003'), ['N_Axis'])
    doc.getObject('Pocket002').AlongSketchNormal = 1
    doc.getObject('Pocket002').Type = 0
    doc.getObject('Pocket002').UpToFace = None
    doc.getObject('Pocket002').Reversed = 0
    doc.getObject('Pocket002').Midplane = 0
    doc.getObject('Pocket002').Offset = 0
    doc.recompute()
    doc.getObject('Pocket001').Visibility = False
    # doc.resetEdit()
    doc.getObject('Sketch003').Visibility = False


class EnclosureMacro8_Command_Class:
    def GetResources(self):
        mod_dir = App.getUserAppDataDir()
        icon_path = os.path.join(
            mod_dir,
            "Mod",
            "ElectronicsEnclosures",
            "Resources",
            "icons",
            "rpizero2_pink.svg"
        )

        # App.Console.PrintMessage("ICON PATH: {}\n".format(icon_path))
        # App.Console.PrintMessage("ICON EXISTS: {}\n".format(os.path.exists(icon_path)))

        return {
            'Pixmap': icon_path,
            'MenuText': 'Create Raspberry Pi Zero 2 Enclosure Box',
            'ToolTip': 'Creates enclosure box using the Part Design Workbench'
        }

    def Activated(self):
        run()

    def IsActive(self):
        return True

FreeCADGui.addCommand('RaspberryPiZero2_pd_wb', EnclosureMacro8_Command_Class())
