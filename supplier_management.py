# Supplier Management System

## Features
- Supplier Database Management
- Contact Information
- Pricing
- Contract Tracking

## Code Implementation

class Supplier:
    def __init__(self, name, contact_info, pricing, contract_details):
        self.name = name
        self.contact_info = contact_info
        self.pricing = pricing
        self.contract_details = contract_details

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info

    def update_pricing(self, new_pricing):
        self.pricing = new_pricing

    def track_contract(self, contract_status):
        self.contract_details['status'] = contract_status

class SupplierManagement:
    def __init__(self):
        self.suppliers = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def get_supplier_info(self, name):
        for supplier in self.suppliers:
            if supplier.name == name:
                return supplier
        return None

    def update_supplier(self, name, contact_info=None, pricing=None, contract_details=None):
        supplier = self.get_supplier_info(name)
        if supplier:
            if contact_info:
                supplier.update_contact_info(contact_info)
            if pricing:
                supplier.update_pricing(pricing)
            if contract_details:
                supplier.contract_details.update(contract_details)

# Example Usage
if __name__ == '__main__':
    supplier_management = SupplierManagement()
    supplier1 = Supplier('Supplier A', {'email': 'contact@supplierA.com', 'phone': '123-456-7890'}, {'product1': 100, 'product2': 150}, {'start_date': '2026-01-01', 'end_date': '2027-01-01', 'status': 'active'})
    supplier_management.add_supplier(supplier1)
    
    supplier_info = supplier_management.get_supplier_info('Supplier A')
    print(supplier_info.contact_info)   # Output: {'email': 'contact@supplierA.com', 'phone': '123-456-7890'}
    
    supplier_management.update_supplier('Supplier A', pricing={'product1': 110})
