import json

class TemplateManager:
    def __init__(self, template_file="message_templates.json"):
        self.template_file = template_file
        self.templates = self.load_templates()

    def load_templates(self):
        """Load templates from JSON file"""
        try:
            with open(self.template_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Template file not found.")
            return {}

    def get_template(self, template_name):
        """Retrieve a specific template"""
        return self.templates.get(template_name, None)

    def generate_message(self, template_name, data):
        """
        Replace placeholders with actual values.

        data example:
        {
            "name": "Rahul",
            "offer": "20% OFF on your next order",
            "due_amount": "500"
        }
        """
        template = self.get_template(template_name)

        if not template:
            return "Template not found."

        try:
            message = template.format(**data)
            return message
        except KeyError as e:
            return f"Missing placeholder value for {e}"