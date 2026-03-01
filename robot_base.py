import FreeCAD as App
import FreeCADGui
import FreeCADGui as Gui
from PySide import QtGui
import PartDesign
import Part
import Sketcher
import os
from BOPTools import BOPFeatures

def make_grid_plate():
    """Grid plate with user input dialog - using your working PySide import"""
    
    # Get user input - using QtGui (PySide)
    width, ok1 = QtGui.QInputDialog.getDouble(
        None, 
        "Grid Plate Dimensions", 
        "Enter width (mm):", 
        150.0, 50.0, 500.0, 1
    )
    
    if not ok1:
        return None
    
    height, ok2 = QtGui.QInputDialog.getDouble(
        None,
        "Grid Plate Dimensions",
        "Enter height (mm):",
        100.0, 50.0, 500.0, 1
    )
    
    if not ok2:
        return None
    
    thickness, ok3 = QtGui.QInputDialog.getDouble(
        None,
        "Grid Plate Dimensions",
        "Enter thickness (mm):",
        6.0, 2.0, 30.0,1
    )
    
    if not ok3:
        return None
    
    # Optional: Ask for grid parameters too
    spacing, ok4 = QtGui.QInputDialog.getDouble(
        None,
        "Grid Parameters",
        "Hole spacing (mm):",
        20.0, 5.0, 50.0, 1
    )
    
    if not ok4:
        spacing = 20.0  # Default if cancelled
    
    hole_dia, ok5 = QtGui.QInputDialog.getDouble(
        None,
        "Grid Parameters",
        "Hole diameter (mm) - M3 = 3.3mm:",
        3.3, 2.0, 10.0, 1
    )
    
    if not ok5:
        hole_dia = 3.3  # Default for M3 screws
    
    margin, ok6 = QtGui.QInputDialog.getDouble(
        None,
        "Grid Parameters",
        "Edge margin (mm):",
        10.0, 5.0, 30.0, 1
    )
    
    if not ok6:
        margin = 10.0
    
    # Create or get document
    doc = App.ActiveDocument if App.ActiveDocument else App.newDocument()
    
    # Make base box
    box = Part.makeBox(width, height, thickness)
    
    # Calculate holes
    holes_x = int((width - 2 * margin) / spacing) + 1
    holes_y = int((height - 2 * margin) / spacing) + 1
    
    # Cut holes
    for i in range(holes_x):
        for j in range(holes_y):
            x = margin + i * spacing
            y = margin + j * spacing
            hole = Part.makeCylinder(hole_dia/2, thickness+2, App.Vector(x, y, -1))
            box = box.cut(hole)
    
    # Add to document
    obj = doc.addObject("Part::Feature", "GridPlate")
    obj.Shape = box
    obj.Label = f"GridPlate_{width}x{height}x{thickness}"
    
    # Make it pretty
    obj.ViewObject.ShapeColor = (0.8, 0.9, 1.0)  # Light blue
    obj.ViewObject.LineColor = (0.0, 0.0, 0.5)    # Dark blue edges
    
    # Add custom properties so users can see parameters
    obj.addProperty("App::PropertyLength", "Width", "Dimensions")
    obj.Width = width
    obj.addProperty("App::PropertyLength", "Height", "Dimensions")
    obj.Height = height
    obj.addProperty("App::PropertyLength", "Thickness", "Dimensions")
    obj.Thickness = thickness
    obj.addProperty("App::PropertyLength", "HoleSpacing", "Grid")
    obj.HoleSpacing = spacing
    obj.addProperty("App::PropertyLength", "HoleDiameter", "Grid")
    obj.HoleDiameter = hole_dia
    obj.addProperty("App::PropertyInteger", "HolesX", "Grid")
    obj.HolesX = holes_x
    obj.addProperty("App::PropertyInteger", "HolesY", "Grid")
    obj.HolesY = holes_y
    
    doc.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    
    # Print summary
    print("="*50)
    print("GRID PLATE CREATED SUCCESSFULLY!")
    print(f"Dimensions: {width} x {height} x {thickness} mm")
    print(f"Hole pattern: {holes_x} x {holes_y} holes")
    print(f"Hole spacing: {spacing} mm")
    print(f"Hole diameter: {hole_dia} mm (for M3 screws)")
    print("="*50)
    
    return obj

    
class EnclosureMacro7_Command_Class:
    def GetResources(self):
        mod_dir = App.getUserAppDataDir()
        icon_path = os.path.join(
            mod_dir,
            "Mod",
            "ElectronicsEnclosures",
            "Resources",
            "icons",
            "electronics.svg"
        )

        # App.Console.PrintMessage("ICON PATH: {}\n".format(icon_path))
        # App.Console.PrintMessage("ICON EXISTS: {}\n".format(os.path.exists(icon_path)))

        return {
            'Pixmap': icon_path,
            'MenuText': 'Create Robot Base',
            'ToolTip': 'Creates a base for the robot with a grid of mounting holes'
        }

    def Activated(self):
        make_grid_plate()

    def IsActive(self):
        return True
Gui.addCommand('robot_base', EnclosureMacro7_Command_Class())
