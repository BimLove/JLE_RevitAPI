# -*- coding: utf-8 -*-
__title__   = "Selection"
__doc__     = """Version = 1.0
Date    = 18.12.2024
________________________________________________________________
Description:
Example
________________________________________________________________
Author: Jessie Love Elarde"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import Room
from Autodesk.Revit.UI.Selection import ObjectType,PickBoxStyle, Selection
#.NET Imports
import clr
# from Samples.ViewsSheets import new_name
# from Samples.ViewsSheets import selection

clr.AddReference('System')
from System.Collections.Generic import List


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document

selection = uidoc.Selection #type: Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

#==================================================

#🔷 1. Get Selected Elements
# selected_element_ids = uidoc.Selection.GetElementIds("Select Elements")
# for e_id in selected_element_ids:
#     e = doc.GetElement(e_id)
#     print(e_id, e)
#
#     if type(e) == Room:
#         print("it's a room")
#     elif type(e) == Wall:
#         print("It's a wall")


#🔷 2. Pick Elements by Rectangle
# selected_elements = selection.PickElementsByRectangle("Select Elements")
# print(selected_elements)

#🔷 3.Pick Object

# ref_pick_object = selection.PickObject(ObjectType.Element)
# pick_object  = doc.GetElement(ref_pick_object)
# print(pick_object)

#🔷 4.Pick Objects

# ref_pick_objects = selection.PickObjects(ObjectType.Element)
# pick_objects  = [doc.GetElement(ref) for ref in ref_pick_objects]   # this will generate list
# for el in pick_objects:
#     print(el)
# print(pick_objects)


#🔷 5.Pick Point
# select_point = selection.PickPoint()
# print(select_point)

#🔷 6.Pick Box
# pick_box = selection.PickBox(PickBoxStyle.Directional,"Draw pick box")
# print(pick_box)

#🔷 7.Set Selection in Revit UI
# new_selection = List[ElementId]()
# new_selection.Add(ElementId(352530))
# new_selection.Add(ElementId(352519))
# new_selection.Add(ElementId(352518))
# new_selection.Add(ElementId(352531))
# selection.SetElementIds(new_selection)

# ╔═╗╔═╗╔╦╗╔═╗╦  ╔═╗  ╔═╗╦═╗╔═╗╔╦╗  ╔═╗╔╦╗╦ ╦╔═╗╦═╗
# ╚═╗╠═╣║║║╠═╝║  ║╣   ╠╣ ╠╦╝║ ║║║║  ║ ║ ║ ╠═╣║╣ ╠╦╝
# ╚═╝╩ ╩╩ ╩╩  ╩═╝╚═╝  ╚  ╩╚═╚═╝╩ ╩  ╚═╝ ╩ ╩ ╩╚═╝╩╚═

# selected_elements = selection.PickElementsByRectangle('Select Some Elements...!!!!')
# for elm in selected_elements:
#     print (elm.Category.Name)