# -*- coding: utf-8 -*-
__title__ = "SelectByUser"
__doc__ = """Version = 1.0
Date    = 15.07.2024
_____________________________________________________________________
Description: 
_____________________________________________________________________
Author: JL Elarde"""

from collections import defaultdict

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==================================================
# Regular + Autodesk
from Autodesk.Revit.DB import *

# pyRevit
from pyrevit import revit, forms

# .NET Imports (You often need List import)
import clr
clr.AddReference("System")
from System.Collections.Generic import List

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==================================================
from Autodesk.Revit.UI import UIDocument
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application               # Application

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝
#==================================================

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==================================================
# 📦 Create Default Dict Container
from collections import defaultdict
dict_elements_by_user = defaultdict(list)

#1️⃣ Get 3D Elements in The Project
elements = FilteredElementCollector(doc).WhereElementIsNotElementType().WhereElementIsViewIndependent().ToElements()



#2️⃣ Who Did this?
# elements = list(elements)[:30]
for elem in elements:
    wti = WorksharingUtils.GetWorksharingTooltipInfo(doc,elem.Id)
    changed_by = wti.LastChangedBy

    #owner       = wti.Owner
    #creator     = wti.Creator

    #3️⃣ Sort Elements By User
    dict_elements_by_user[changed_by].append(elem)

for k,v in dict_elements_by_user.items():
    print('User: {} has modified {} Elements'.format(k, len(v)))

#4️⃣ Select User
from pyrevit import forms

selected_user       = forms.SelectFromList.show(dict_elements_by_user.keys(), button_name='Select Item')

if not selected_user:
    forms.alert('No User Was Selected. Please Try Again',exitscript=True)

selected_elements   = dict_elements_by_user[selected_user]

# print('_'* 50)
# print('Selected {} Elements by {}'.format(len(selected_elements),selected_user))

#5️⃣ Modify User Selection
selected_el_ids      = [e.Id for e in selected_elements]
List_selected_el_ids = List[ElementId](selected_el_ids)
uidoc.Selection.SetElementIds(List_selected_el_ids )













