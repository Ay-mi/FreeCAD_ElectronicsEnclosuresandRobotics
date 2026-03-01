import FreeCAD
import FreeCADGui
import sys
import os

mod_dir = FreeCAD.getUserAppDataDir() + "Mod/ElectronicsEnclosures"
#macros_dir = os.path.join(mod_dir, "macros")

#if macros_dir not in sys.path:
#    sys.path.append(macros_dir)

class ElectronicsEnclosure(FreeCADGui.Workbench):
    MenuText = "Electronics Enclosures and Robotics"
    ToolTip = "Workbench for designing electronic enclosures and robots"
    Icon = os.path.join(
        FreeCAD.getUserAppDataDir(),
        "Mod",
        "ElectronicsEnclosures",
        "Resources",
        "icons",
        "electronics.svg"
)

    def Initialize(self):
        import enclosure_shell
        import RaspberryPi4_shell
        import RaspberryPi4_pd_wb
        import usbc_cut
        import usbb_cut
        import hdmi_cut
        import robot_base
        import RaspberryPiZero2_pd_wb
        import robot_arm
        import robot_arm_des2
        import arm_base


        self.appendToolbar("Enc and Robot Tools", ["enclosure_shell", "RaspberryPi4_shell_Command",  "usbc_cut", "usbb_cut", "hdmi_cut", "RaspberryPi4_pd_wb_Command", "RaspberryPiZero2_pd_wb", "robot_base", "robot_arm", "robot_arm_des2", "arm_base"])
        self.appendMenu("Electronics Enclosures and Robotics", ["enclosure_shell", "RaspberryPi4_shell_Command", "usbc_cut", "usbb_cut", "hdmi_cut","RaspberryPi4_pd_wb_Command", "RaspberryPiZero2_pd_wb", "robot_base", "robot_arm", "robot_arm_des2", "arm_base"])
    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list) # add commands to the context menu
        
    def GetClassName(self):
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(ElectronicsEnclosure())
