# Importar las librerías por defecto. Se puede prescindir de algunas dependiendo de la finalidad del código

# Algunos significados
# clr es el Common Language Runtime de .NET. Permite ejecutar código desde varios lenguajes distintos
# sys es la biblioteca de python para cargar otras bibliotecas
# System es espacio de nombres del sistema en la raíz de .NET

# Referencias: Protogeometry, RevitNodes, RevitServices, Revit API, REvitAPIUI

import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import System
from System import Array
from System.Collections.Generic import *

# ProtoGeometry es la biblioteca para interactuar con la geometría de Dynamo
clr.AddReference('ProtoGeometry')   
from Autodesk.DesignScript.Geometry import *

# RevitNodes Carga los nodos de Dynamo, la bibliotecas de los elements de Revit en Dynamo y las conversiones geométricas
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# RevitServices permitirá manejar los cocumentos y modificarles a través del DocumentManager y el TransactionManager
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# RevitAPI Agrega clases que se encuentran en el archivo dll de la API de Revit
# RevitAPI Permite acceder a la interfaz de usuario desde la API
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# CurrentDBDocument - Identificador del documento actual de python
# CurrentUIApplication - Identificador de la interfaz de usuario del documento de Revit activo
# Identificador de la aplicación de Revit abierta actualmente
# Identificador de la interfez de usuario del documento abierto actualmente
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveDocument

# De aquí en adelante el código:

