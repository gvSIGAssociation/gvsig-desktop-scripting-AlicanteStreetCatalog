# encoding: utf-8

import gvsig
from gvsig.libs.formpanel import FormPanel
import urllib
import json
from org.gvsig.utils import DefaultListModel
from org.gvsig.tools.util import LabeledValueImpl
from org.gvsig.fmap.geom import GeometryLocator
from gvsig import currentView
from java.awt.event import MouseEvent
import sys

class AlicanteStreetCatalog(FormPanel):
    def __init__(self):
        FormPanel.__init__(self,gvsig.getResource(__file__,"alicanteStreetCatalog.xml"))

    def lstAddress_mouseClick(self, event):
        if event.getClickCount()!=2:
          return
        if event.getID() != MouseEvent.MOUSE_CLICKED:
          return
        urlpetition = None
        address = None
        try:
          calle = self.lstAddress.getSelectedValue().getValue()
          urlpetition = "https://guiaurbana.alicante.es/callejero/servicios/direccion/%s/geojson" % calle
          petition = urllib.urlopen(urlpetition)
          address = petition.read()
          geomManager = GeometryLocator.getGeometryManager()
          geometry = geomManager.createFrom(address)
  
          if geometry == None:
             #print "geometry is null:", address
             #print "urlpetition:", urlpetition
             return
          currentView().getMapContext().zoomToEnvelope(geometry.getEnvelope())
        except:
          print "url:", urlpetition
          print "response:", address
          ex = sys.exc_info()[1]
          print "Error", ex.__class__.__name__, str(ex)

        

    def txtSearch_keyPressed(self, event):
        if event.keyChar == "\n":
          self.searchAddress()
          
    def btnSearch_click(self, *args):
        self.searchAddress()
        
    def searchAddress(self):
        #https://guiaurbana.alicante.es/callejero/servicios/direccion/?query=padre
        petition = None
        addresList = None
        try:
          petition = urllib.urlopen("https://guiaurbana.alicante.es/callejero/servicios/direccion/?query="+self.txtSearch.getText())
          addressList = petition.read()
          jAddressList = json.loads(addressList)
          suggestions = jAddressList["suggestions"]
          listModel = DefaultListModel()
          for suggestion in suggestions:
            n = LabeledValueImpl(suggestion["value"], suggestion["data"])
            listModel.addElement(n)
          self.lstAddress.setModel(listModel)
        except:
          print "url:", repr(petition)
          print "response:", repr(addresList)
          ex = sys.exc_info()[1]
          print "Error", ex.__class__.__name__, str(ex)
          
def showAlicanteStreetCatalog():
    l = AlicanteStreetCatalog()
    l.showTool(u"Catálogo calles de Alicante")
  
def main(*args):
    showAlicanteStreetCatalog()

    


    
      
    
    
    