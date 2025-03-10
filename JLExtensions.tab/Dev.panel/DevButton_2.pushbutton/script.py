# -*- coding: utf-8 -*-
__title__   = "Read Elements"
__doc__     = """Version = 1.0
Date    = 20.12.2024
________________________________________________________________
Description:
Examples on How to Read Properties and Methods of Selected Elements.
________________________________________________________________
Author: Jessie Love Elarde"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
from Autodesk.Revit.DB import  *
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

rvt_year = int(app.VersionNumber)
selection = uidoc.Selection #type: Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝

#==================================================
# Pick an Object
ref_pick_object = selection.PickObject(ObjectType.Element)
elem  = doc.GetElement(ref_pick_object)

# Check Type of element to be selected
if type(elem) != Room:
    print('This is not a Room Selected. Please try Again!')
    import sys
    sys.exit()

# Room Variables
level_id = elem.LevelId
level = doc.GetElement(level_id)
group = "None" if elem.GroupId == ElementId(-1) else elem.GroupId
#👆 Same as 👇
# if elem.GroupId == ElementId(-1):
#     group = "None"
# else:
#     group = elem.GroupId

# Print statements

print(elem.Category.Name)
print('ElementId: {}'.format(elem.Id))
print('GroupID: {}'.format(elem.GroupId))
print(type(elem.GroupId))
print('Category: {}'.format(elem.Category.Name))
print('BuiltInCategory: {}'.format(elem.Category.BuiltInCategory))
print('Level: {}'.format(level.Name))
print('XYZ: {}'.format(elem.Location.Point))
print('Area: {}'.format(elem.Area))
print('Number: {}'.format(elem.Number))
print('Perimeter: {}'.format(elem.Perimeter))

def convert_internal_units(length, get_internal = True ):
    """

    """
    if rvt_year >= 2021:
        # New Method


    else:

        # Old Method









