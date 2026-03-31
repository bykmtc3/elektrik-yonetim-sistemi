class MaterialCalculator:
    MATERIALS = {
        'kablo_1_5mm': {'name': 'Kablo 1.5mm²', 'unit': 'metre', 'price': 2.5},
        'kablo_2_5mm': {'name': 'Kablo 2.5mm²', 'unit': 'metre', 'price': 3.5},
        'kablo_4mm': {'name': 'Kablo 4mm²', 'unit': 'metre', 'price': 5.0},
        'kablo_6mm': {'name': 'Kablo 6mm²', 'unit': 'metre', 'price': 7.0},
        'sigorta_10a': {'name': 'Sigorta 10A', 'unit': 'adet', 'price': 8.0},
        'sigorta_20a': {'name': 'Sigorta 20A', 'unit': 'adet', 'price': 10.0},
        'pano_63a': {'name': 'Pano 63A', 'unit': 'adet', 'price': 150.0},
        'pano_100a': {'name': 'Pano 100A', 'unit': 'adet', 'price': 250.0},
        'boru_16mm': {'name': 'Boru 16mm', 'unit': 'metre', 'price': 3.0},
        'boru_20mm': {'name': 'Boru 20mm', 'unit': 'metre', 'price': 4.0},
        'toprak': {'name': 'Topraklama', 'unit': 'metre', 'price': 1.5},
    }
    
    def __init__(self):
        self.materials = self.MATERIALS.copy()
    
    def calculate_cable_length(self, layers):
        """Calculate total cable length from DWG layers"""
        total_length = 0
        for layer in layers:
            if 'kablo' in layer.lower():
                total_length += 100  # Example calculation
        return total_length
    
    def calculate_material_needs(self, project_data):
        """Calculate material requirements"""
        needs = []
        
        # Cable calculation
        cable_length = self.calculate_cable_length(project_data.get('layers', []))
        if cable_length > 0:
            needs.append({
                'material': 'kablo_2_5mm',
                'quantity': cable_length,
                'unit': 'metre',
                'cost': cable_length * self.materials['kablo_2_5mm']['price']
            })
        
        # Panel and breaker
        needs.append({
            'material': 'pano_63a',
            'quantity': 1,
            'unit': 'adet',
            'cost': 150.0
        })
        
        needs.append({
            'material': 'sigorta_20a',
            'quantity': 4,
            'unit': 'adet',
            'cost': 40.0
        })
        
        return needs
    
    def calculate_total_cost(self, needs):
        """Calculate total project cost"""
        return sum(item['cost'] for item in needs)
    
    def generate_bom(self, needs):
        """Generate Bill of Materials"""
        bom = {
            'items': needs,
            'total_cost': self.calculate_total_cost(needs),
            'total_items': len(needs)
        }
        return bom