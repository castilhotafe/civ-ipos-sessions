# organisation.py
class Organisation:
    # TODO: Step1
    # TODO attributes for org: name
    def __init__(self, name):
        self.name = name
        self.contacts = []
    # pass

    # TODO Step 3 get & set contacts (add and retrieve)
    # TODO behaviours for org: addContact()
    def __str__(self):
        return f'{self.name}'


    def add_contact(self, contact):
        self.contacts.append(contact)


    def get_contacts(self):
        for contact in self.contacts:
            print(contact)

 
# many contacts
