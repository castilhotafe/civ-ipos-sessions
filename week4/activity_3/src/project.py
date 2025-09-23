# TODO Step 4 create a project
# project.py



class Project:
    def __init__(self, name, organisation):
        self.name = name
        self.organisation = organisation
        self.contacts = []
        # Challenge solution
 

    def __str__(self):
        return f'Procect: {self.name}'
    # TODO Step 5 add contacts
    # Challenge - For a contact to be added to a
    # project it must already exist in the organisation
    def add_contact(self, contact):
        if contact in self.organisation.contacts:
            self.contacts.append(contact)

