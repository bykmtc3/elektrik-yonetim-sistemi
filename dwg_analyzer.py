import ezdxf
import os
from config import Config

class DWGAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dwg = None
    
    def load_file(self):
        try:
            self.dwg = ezdxf.readfile(self.file_path)
            return True
        except Exception as e:
            print(f"Error loading DWG: {str(e)}")
            return False
    
    def extract_layers(self):
        if not self.dwg:
            return []
        
        layers = []
        for layer in self.dwg.layers:
            layers.append({
                'name': layer.dxf.name,
                'color': layer.dxf.color,
                'linetype': layer.dxf.linetype
            })
        return layers
    
    def extract_entities(self):
        if not self.dwg:
            return []
        
        entities = []
        for entity in self.dwg.modelspace():
            entities.append({
                'type': entity.dxftype(),
                'layer': entity.dxf.layer,
                'color': entity.dxf.color
            })
        return entities
    
    def extract_dimensions(self):
        if not self.dwg:
            return {}
        
        dimensions = {
            'lines': 0,
            'circles': 0,
            'texts': 0,
            'polylines': 0
        }
        
        for entity in self.dwg.modelspace():
            if entity.dxftype() == 'LINE':
                dimensions['lines'] += 1
            elif entity.dxftype() == 'CIRCLE':
                dimensions['circles'] += 1
            elif entity.dxftype() == 'TEXT':
                dimensions['texts'] += 1
            elif entity.dxftype() == 'LWPOLYLINE':
                dimensions['polylines'] += 1
        
        return dimensions
    
    def analyze(self):
        if not self.load_file():
            return None
        
        return {
            'layers': self.extract_layers(),
            'entities': self.extract_entities(),
            'dimensions': self.extract_dimensions()
        }