# test_project.py
import unittest
from organisation import Organisation
from project import Project
from contact import Contact



    # Step 4

        # Create an organization

        # Create a project associated with the organisation

        # # Check if project is associated with the correct organisation


    # Step 5
    # Add a test that test a contact can be created and
    # added to an organisation and can also be added to a project


    # Challenge test that you can add a contact to an organisation
    # and a project using the project class



class TestProject(unittest.TestCase):

    def test_project_associated_with_organisation(self):
        organisation = Organisation("DataBridge")
        project = Project("Website Redesign", organisation)
        self.assertEqual(project.organisation, organisation)

    def test_contact_added_to_organisation_and_project(self):
        organisation = Organisation("DataBridge")
        contact = Contact("Marcos", "Developer")
        project = Project("Website Redesign", organisation)
        organisation.add_contact(contact)
        project.add_contact(contact)
        self.assertIn(contact, organisation.contacts)
        self.assertIn(contact, project.contacts)

    def test_add_contact_to_project(self):
        organisation = Organisation("DataBridge")
        project = Project("Internal Tool", organisation)
        contact = Contact("Ana", "Engineer")
        organisation.add_contact(contact)
        project.add_contact(contact)
        self.assertIn(contact, project.contacts)
        self.assertIn(contact, organisation.contacts)