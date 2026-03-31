import pandas as pd
import os

class PriceListManager:
    def __init__(self, directory):
        self.directory = directory
        self.price_lists = {}

    def import_price_list(self, file_path):
        if file_path.endswith('.csv'):
            price_list = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            price_list = pd.read_excel(file_path)
        else:
            raise ValueError('Unsupported file format. Please use CSV or Excel. ')
        self.price_lists[os.path.basename(file_path)] = price_list
        return price_list

    def manage_version_control(self):
        # This method can be expanded with version control logic.
        pass

    def list_price_lists(self):
        return list(self.price_lists.keys())

    def get_price_list(self, name):
        return self.price_lists.get(name, 'Price list not found.')

# Example usage:
# manager = PriceListManager(directory='path_to_price_lists')
# manager.import_price_list('path_to_file.csv')