# encoding: utf-8

import gvsig

from addons.AlicanteStreetCatalog.paletteutils import agregar_paleta

def main(*args):
   registrar()   

#==========================================

def registrar():
  agregar_paleta(
      nombre=u"Figuras de horizontal",
      icono=u"paleta-figuras",
      descripcion=u"Muestra La paleta de figuras de horizontal",
      grupo=u"Figuras",
      filtro=""" grupo = 'Figuras' """
  )
