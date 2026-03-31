class ProjectTemplateManager:
    def __init__(self):
        self.templates = {}

    def add_template(self, name, config):
        self.templates[name] = config

    def remove_template(self, name):
        if name in self.templates:
            del self.templates[name]

    def get_template(self, name):
        return self.templates.get(name, None)

    def create_project(self, name, template_name):
        template = self.get_template(template_name)
        if template is None:
            raise ValueError(f"Template '{template_name}' not found.")

        # Here, you would implement the logic to create a project using the template.
        project_config = {"name": name, "config": template}
        return project_config

# Example of defining templates
if __name__ == '__main__':
    manager = ProjectTemplateManager()
    manager.add_template('web_app', {'framework': 'Flask', 'database': 'SQLAlchemy'})
    manager.add_template('data_science', {'libraries': ['numpy', 'pandas', 'matplotlib']})
    
    # Create a new project
    project = manager.create_project('MyWebApp', 'web_app')
    print(project)