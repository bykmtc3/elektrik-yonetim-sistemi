# Central Integration Manager

class IntegrationManager:
    def __init__(self):
        # Initialize all modules
        self.modules = {}

    def register_module(self, module_name, module):
        """ Registers a module to the integration manager. """
        self.modules[module_name] = module

    def communicate(self, module_name, message):
        """ Communicates a message to a specific module. """
        if module_name in self.modules:
            module = self.modules[module_name]
            module.receive_message(message)
        else:
            raise ValueError(f'Module {module_name} not found.')

    def broadcast(self, message):
        """ Broadcasts a message to all registered modules. """
        for module_name, module in self.modules.items():
            module.receive_message(message)

# Example usage:
# integration_manager = IntegrationManager()
# integration_manager.register_module('module1', Module1())
# integration_manager.communicate('module1', 'Hello!')