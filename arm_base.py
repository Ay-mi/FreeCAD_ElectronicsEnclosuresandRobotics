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


    ActiveSketch = doc.getObject('Sketch')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000000))
    doc.getObject('Sketch').addGeometry(geoList,False)
    del geoList

    constraintList = []
    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',0,50.000000)) 
    doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))


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
    doc.getObject('Pad').Length = 20.000000
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
    #doc.purgeTouched()
    doc.recompute()
    # doc.resetEdit()
    doc.getObject('Sketch').Visibility = False
    # Gui.Selection.addSelection('Unnamed3','Body','Pad.Face3',-1.44927,-6.66247,20)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
    doc.getObject('Sketch001').AttachmentSupport = (doc.getObject('Pad'),['Face3',])
    doc.getObject('Sketch001').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    ### End command PartDesign_CompSketches
    ActiveSketch = doc.getObject('Sketch001')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-12.500000, -12.500000, 0.000000),App.Vector(12.500000, -12.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(12.500000, -12.500000, 0.000000),App.Vector(12.500000, 12.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(12.500000, 12.500000, 0.000000),App.Vector(-12.500000, 12.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-12.500000, 12.500000, 0.000000),App.Vector(-12.500000, -12.500000, 0.000000)))
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

    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,25.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,25.000000)) 
    doc.getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))


    # doc.resetEdit()
    App.ActiveDocument.recompute()

    doc.recompute()
    ### Begin command PartDesign_Pad
    doc.getObject('Body').newObject('PartDesign::Pad','Pad001')
    doc.getObject('Pad001').Profile = (doc.getObject('Sketch001'), ['',])
    doc.getObject('Pad001').Length = 10
    App.ActiveDocument.recompute()
    doc.getObject('Pad001').ReferenceAxis = (doc.getObject('Sketch001'),['N_Axis'])
    doc.getObject('Sketch001').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Pad
    # Gui.Selection.clearSelection()
    doc.getObject('Pad001').Length = 60.000000
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
    #doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad').Visibility = False
    # doc.resetEdit()
    doc.getObject('Sketch001').Visibility = False
    # Gui.Selection.addSelection('Unnamed3','Body','Pad001.Face8',-5.02347,-0.0967585,80)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
    doc.getObject('Sketch002').AttachmentSupport = (doc.getObject('Pad001'),['Face8',])
    doc.getObject('Sketch002').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    ### End command PartDesign_CompSketches
    ActiveSketch = doc.getObject('Sketch002')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.LineSegment(App.Vector(-12.671545, -12.500000, 0.000000),App.Vector(-2.671545, -12.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-2.671545, -12.500000, 0.000000),App.Vector(-2.671545, 12.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-2.671545, 12.500000, 0.000000),App.Vector(-12.671545, 12.500000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(-12.671545, 12.500000, 0.000000),App.Vector(-12.671545, -12.500000, 0.000000)))
    doc.getObject('Sketch002').addGeometry(geoList,False)
    del geoList

    constrGeoList = []
    constrGeoList.append(Part.Point(App.Vector(-7.671545, 0.000000, 0.000000)))
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

    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,10.000000)) 
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,25.000000)) 
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('PointOnObject', 4, 1, -1))

    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',-2,1,1,2.671545)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch002').setDatum(12,App.Units.Quantity('2.500000 mm'))
    App.ActiveDocument.recompute()

    ### Begin command PartDesign_Pad
    doc.getObject('Body').newObject('PartDesign::Pad','Pad002')
    doc.getObject('Pad002').Profile = (doc.getObject('Sketch002'), ['',])
    doc.getObject('Pad002').Length = 10
    App.ActiveDocument.recompute()
    doc.getObject('Pad002').ReferenceAxis = (doc.getObject('Sketch002'),['N_Axis'])
    doc.getObject('Sketch002').Visibility = False
    App.ActiveDocument.recompute()

    ### End command PartDesign_Pad
    # Gui.Selection.clearSelection()
    doc.getObject('Pad002').Length = 20.000000
    doc.getObject('Pad002').TaperAngle = 0.000000
    doc.getObject('Pad002').UseCustomVector = 0
    doc.getObject('Pad002').Direction = (0, 0, 1)
    doc.getObject('Pad002').ReferenceAxis = (doc.getObject('Sketch002'), ['N_Axis'])
    doc.getObject('Pad002').AlongSketchNormal = 1
    doc.getObject('Pad002').Type = 0
    doc.getObject('Pad002').UpToFace = None
    doc.getObject('Pad002').Reversed = 0
    doc.getObject('Pad002').Midplane = 0
    doc.getObject('Pad002').Offset = 0
    #doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad001').Visibility = False
    # doc.resetEdit()
    doc.getObject('Sketch002').Visibility = False
    # Gui.Selection.addSelection('Unnamed3','Body','Pad002.Face6',-2.5,1.68342,89.1901)
    ### Begin command PartDesign_CompSketches
    doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch003')
    doc.getObject('Sketch003').AttachmentSupport = (doc.getObject('Pad002'),['Face6',])
    doc.getObject('Sketch003').MapMode = 'FlatFace'
    App.ActiveDocument.recompute()

    ### End command PartDesign_CompSketches
    # Gui.Selection.clearSelection()
    # Gui.runCommand('Sketcher_CompCreateConic',0)
    ActiveSketch = doc.getObject('Sketch003')

    lastGeoId = len(ActiveSketch.Geometry)

    geoList = []
    geoList.append(Part.Circle(App.Vector(0.000000, 94.569893, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 2.500000))
    doc.getObject('Sketch003').addGeometry(geoList,False)
    del geoList

    constraintList = []
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Diameter',0,5.000000)) 
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('PointOnObject', 0, 3, -2))

    ### Begin command Sketcher_Dimension
    doc.getObject('Sketch003').addConstraint(Sketcher.Constraint('Distance',0,3,-1,94.569893)) 
    ### End command Sketcher_Dimension
    # Gui.Selection.clearSelection()
    doc.getObject('Sketch003').setDatum(2,App.Units.Quantity('94.500000 mm'))
    # doc.resetEdit()
    App.ActiveDocument.recompute()
    doc.recompute()
    ### Begin command PartDesign_Pocket
    doc.getObject('Body').newObject('PartDesign::Pocket','Pocket')
    doc.getObject('Pocket').Profile = (doc.getObject('Sketch003'), ['',])
    doc.getObject('Pocket').Length = 5
    App.ActiveDocument.recompute()
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch003'),['N_Axis'])
    doc.getObject('Sketch003').Visibility = False
    App.ActiveDocument.recompute()
    ### End command PartDesign_Pocket
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket').Length = 10.000000
    doc.getObject('Pocket').TaperAngle = 0.000000
    doc.getObject('Pocket').UseCustomVector = 0
    doc.getObject('Pocket').Direction = (-1, 0, 0)
    doc.getObject('Pocket').ReferenceAxis = (doc.getObject('Sketch003'), ['N_Axis'])
    doc.getObject('Pocket').AlongSketchNormal = 1
    doc.getObject('Pocket').Type = 0
    doc.getObject('Pocket').UpToFace = None
    doc.getObject('Pocket').Reversed = 0
    doc.getObject('Pocket').Midplane = 0
    doc.getObject('Pocket').Offset = 0
    #doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pad002').Visibility = False
    # doc.resetEdit()
    doc.getObject('Sketch003').Visibility = False
    ### Begin command PartDesign_Fillet
    doc.getObject('Body').newObject('PartDesign::Fillet','Fillet')
    doc.getObject('Fillet').Base = (doc.getObject('Pocket'),['Edge16',])
    # Gui.Selection.clearSelection()
    doc.getObject('Pocket').Visibility = False
    App.ActiveDocument.recompute()
    # Gui.Selection.clearSelection()
    ### End command PartDesign_Fillet
    # Gui.Selection.clearSelection()
    doc.getObject('Fillet').Radius = 11.000000
    doc.getObject('Fillet').Base = (doc.getObject('Pocket'),["Edge16",])
    #doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pocket').Visibility = False
    # Gui.Selection.clearSelection()
    doc.getObject('Fillet').Radius = 11.000000
    doc.getObject('Fillet').Base = (doc.getObject('Pocket'),["Edge16","Edge11",])
    #doc.purgeTouched()
    doc.recompute()
    doc.getObject('Pocket').Visibility = False
    # doc.resetEdit()

class EnclosureMacro11_Command_Class:
    def GetResources(self):
        mod_dir = App.getUserAppDataDir()
        icon_path = os.path.join(
            mod_dir,
            "Mod",
            "ElectronicsEnclosures",
            "Resources",
            "icons",
            "arm_base.svg"
        )

        # App.Console.PrintMessage("ICON PATH: {}\n".format(icon_path))
        # App.Console.PrintMessage("ICON EXISTS: {}\n".format(os.path.exists(icon_path)))

        return {
            'Pixmap': icon_path,
            'MenuText': 'Create Robot Arm Base',
            'ToolTip': 'Creates a base for a robot arm. Can be assembled with robot arm links.'
        }

    def Activated(self):
        run()

    def IsActive(self):
        return True

FreeCADGui.addCommand('arm_base', EnclosureMacro11_Command_Class())
