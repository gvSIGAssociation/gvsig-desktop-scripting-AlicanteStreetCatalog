# encoding: utf-8

import gvsig

from gvsig import getResource

from java.io import File
from org.gvsig.andami import PluginsLocator
from org.gvsig.app import ApplicationLocator
from org.gvsig.scripting.app.extension import ScriptingExtension
from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.swing.api import ToolsSwingLocator

from addons.AlicanteStreetCatalog.alicanteStreetCatalog import showAlicanteStreetCatalog

class AlicanteStreetCatalogExtension(ScriptingExtension):
  def __init__(self):
    pass

  def canQueryByAction(self):
    return True

  def isEnabled(self,action):
    return True

  def isVisible(self,action):
    return gvsig.currentView()!=None
    
  def execute(self,actionCommand, *args):
    actionCommand = actionCommand.lower()
    if actionCommand == "view-alicante-street-catalog":
      showAlicanteStreetCatalog()

def selfRegister():
  application = ApplicationLocator.getManager()

  #
  # Registramos las traducciones
  i18n = ToolsLocator.getI18nManager()
  i18n.addResourceFamily("text",File(getResource(__file__,"i18n")))

  #
  # Registramos los iconos en el tema de iconos
  icon = File(getResource(__file__,"images","view-alicante-street-catalog.png")).toURI().toURL()
  iconTheme = ToolsSwingLocator.getIconThemeManager().getCurrent()
  iconTheme.registerDefault("scripting.AlicanteStreetCatalogExtension", "action", "view-alicante-street-catalog", None, icon)

  #
  # Creamos la accion 
  extension = AlicanteStreetCatalogExtension()
  actionManager = PluginsLocator.getActionInfoManager()
  action = actionManager.createAction(
    extension, 
    "view-alicante-street-catalog", # Action name
    u"Catálogo calles de Alicante", # Text
    "view-alicante-street-catalog", # Action command
    "view-alicante-street-catalog", # Icon name
    None, # Accelerator
    650700601, # Position 
    u"Muestra el catálogo de calles de Alicante" # Tooltip
  )
  action = actionManager.registerAction(action)
  application.addMenu(action, u"tools/Catálogo calles de Alicante")

  application.addTool(action, "AlicanteStreetCatalog")
      
def main(*args):
   selfRegister()