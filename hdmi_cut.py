import FreeCAD as App
import FreeCADGui as Gui
import Part
from BOPTools import BOPFeatures
import os

# -----------------------
# PARAMETERS (mm)
# -----------------------
WIDTH  = 14.5
HEIGHT = 7
DEPTH  = 7.0


def run():
    doc = App.ActiveDocument
    bp = BOPFeatures.BOPFeatures(doc)

    # -----------------------
    # GET USER SELECTION (NOW AFTER BUTTON CLICK)
    # -----------------------
    sel = Gui.Selection.getSelectionEx()
    if not sel:
        App.Console.PrintError("Select a face on the enclosure first.\n")
        return

    selEx = sel[0]

    if not selEx.SubObjects:
        App.Console.PrintError("Selection must be a face.\n")
        return

    base_obj = selEx.Object
    face = selEx.SubObjects[0]
    click_point = selEx.PickedPoints[0]

    # -----------------------
    # FACE NORMAL
    # -----------------------
    normal = face.normalAt(0.5, 0.5)
    normal.normalize()

    # -----------------------
    # CREATE CUT SHAPE
    # -----------------------
    shape = Part.makeBox(WIDTH, DEPTH, HEIGHT)

    # Rotate box depth (Y axis) to match face normal
    box_depth_axis = App.Vector(0, 1, 0)
    rotation = App.Rotation(box_depth_axis, normal)
    shape.Placement = App.Placement(App.Vector(0, 0, 0), rotation)

    # -----------------------
    # CENTER & INSET
    # -----------------------
    local_center_offset = App.Vector(
        -WIDTH / 2,
        0,
        -HEIGHT / 2
    )

    global_center_offset = rotation.multVec(local_center_offset)
    OUTSIDE_OVERLAP = 1.0  # mm sticking out
    INSET_DEPTH = DEPTH - OUTSIDE_OVERLAP

    inset_offset = normal.multiply(-INSET_DEPTH)
    shape.translate(
        click_point
        .add(global_center_offset)
        .add(inset_offset)
    )

    # -----------------------
    # SHOW AS DOCUMENT OBJECT
    # -----------------------
    cut_obj = doc.addObject("Part::Feature", "HDMI_Cut")
    cut_obj.Shape = shape
    doc.recompute()

    # -----------------------
    # BOOLEAN CUT
    # -----------------------
    bp.make_cut([base_obj.Name, cut_obj.Name])
    doc.recompute()

    Gui.SendMsgToActiveView("ViewFit")


class EnclosureMacro6_Command_Class:
    def GetResources(self):
        mod_dir = App.getUserAppDataDir()
        icon_path = os.path.join(
            mod_dir,
            "Mod",
            "ElectronicsEnclosures",
            "Resources",
            "icons",
            "hdmi.svg"
        )

        return {
            'Pixmap': icon_path,
            'MenuText': 'Cut HDMI hole',
            'ToolTip': 'Select a face, click a point, then press the button'
        }

    def Activated(self):
        run()

    def IsActive(self):
        return True


Gui.addCommand('hdmi_cut', EnclosureMacro6_Command_Class())
