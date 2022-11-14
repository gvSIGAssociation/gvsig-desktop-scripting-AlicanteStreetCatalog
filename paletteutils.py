# encoding: utf-8

import gvsig
from gvsig import getResource
import os

from java.io import File

from org.gvsig.andami import PluginsLocator
from org.gvsig.app import ApplicationLocator
from org.gvsig.scripting.app.extension import ScriptingExtension
from org.gvsig.tools.swing.api import ToolsSwingLocator

def agregar_paleta(nombre, icono, descripcion, grupo, filtro, titulo=None):
  application = ApplicationLocator.getManager()
  modulename = os.path.splitext(os.path.basename(__file__))[0]
  #
  # Registramos los iconos en el tema de iconos
  icon = File(getResource(__file__,"images",icono+".png")).toURI().toURL()
  iconTheme = ToolsSwingLocator.getIconThemeManager().getCurrent()
  iconTheme.registerDefault("scripting.AlicanteStreetCatalogExtension", "action", icono, None, icon)

  if titulo == None:
    titulo = nombre
  #
  # Creamos la accion 
  actionManager = PluginsLocator.getActionInfoManager()
  action = actionManager.createAction(
    ScriptingExtension, 
    nombre, # Action name
    titulo, # Text
    "%s.mostrar_paleta('%s')" % (modulename,nombre), # Action command
    icono, # Icon name
    None, # Accelerator
    999999999,# Position 
    descripcion # Tooltip
  )
  action.putValue("DropDownGroup", grupo)
  action.putValue("palette_tableName", "URBSIGNAGE_HORIZONTAL_PALETTES")
  action.putValue("palette_filter", filtro)
  action.putValue("palette_label", "model")
  action.putValue("palette_title", titulo)
  action = actionManager.registerAction(action)
  application.addTool(action, "Paletas de señalización urbana")

def mostrar_paleta(*args):
  actionManager = PluginsLocator.getActionInfoManager()
  action = actionManager.getAction(args[0])
  actionManager.getAction("tools-open-geometriespalette").execute([
    "--tableName=", action.getValue("palette_tableName"), 
    "--filter=",action.getValue("palette_filter"),
    "--label=", action.getValue("palette_label"),
    "--title=", action.getValue("palette_title")
  ])

