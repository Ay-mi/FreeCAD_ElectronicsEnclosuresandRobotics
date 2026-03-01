import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui
import PartDesign
import Sketcher
import os
from BOPTools import BOPFeatures

def run():
    App.Console.PrintMessage("Running Enclosure Macro 1\n")

    doc = App.activeDocument()
    if doc is None:
        doc = App.newDocument()

    bp = BOPFeatures.BOPFeatures(doc)

    # ----------------------------
    # USER INPUT
    # ----------------------------
    length, ok = QtGui.QInputDialog.getDouble(
        None, "Enclosure Depth", "Enter length (mm) (x axis):", 100.0, 10.0, 1000.0, 1
    )
    if not ok:
        return
    
    width, ok = QtGui.QInputDialog.getDouble(
        None, "Enclosure Width", "Enter width (mm) (y axis):", 80.0, 10.0, 1000.0, 1
    )
    if not ok:
        return

    height, ok = QtGui.QInputDialog.getDouble(
        None, "Enclosure Height", "Enter height (mm) (z axis):", 30.0, 5.0, 500.0, 1
    )
    if not ok:
        return

    wall, ok = QtGui.QInputDialog.getDouble(
        None, "Wall Thickness", "Enter wall thickness (mm):", 2.5, 0.5, 20.0, 1
    )
    if not ok:
        return

    # ----------------------------
    # BOX FUNCTIONS
    # ----------------------------
    def makeBox(label, w, d, h, placement):
        box = doc.addObject("Part::Box", label)
        box.Width = w
        box.Length = d
        box.Height = h
        box.Placement.Base = placement
        doc.recompute()
        return box

    def cutBox(base, tool):
        result = bp.make_cut([base.Name, tool.Name])
        doc.recompute()
        return result

    # ----------------------------
    # CREATE ENCLOSURE
    # ----------------------------

    # OUTER BOX (derived from inner dimensions)
    outer = makeBox(
        "OuterBox",
        width + 2 * wall,
        length + 2 * wall,
        height + wall,           # open-top enclosure
        App.Vector(0, 0, 0)
    )

    # INNER BOX 
    inner = makeBox(
        "InnerBox",
        width,
        length,
        height,
        App.Vector(wall, wall, wall)
    )

    # Boolean cut
    enclosure = cutBox(outer, inner)

    Gui.SendMsgToActiveView("ViewFit")

    
class EnclosureMacro5_Command_Class:
    def GetResources(self):
        mod_dir = App.getUserAppDataDir()
        icon_path = os.path.join(
            mod_dir,
            "Mod",
            "ElectronicsEnclosures",
            "Resources",
            "icons",
            "custom.svg"
        )

        return {
            'Pixmap': icon_path,
            'MenuText': 'Create Enclosure Box',
            'ToolTip': 'Creates the outer and inner enclosure boxes'
        }

    def Activated(self):
        run()

    def IsActive(self):
        return True
Gui.addCommand('enclosure_shell', EnclosureMacro5_Command_Class())
