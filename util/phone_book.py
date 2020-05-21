class ContactList:
    def __init__(self):
        print("Lista de contatos de emergência")
        self.LIST = []

    def add_contact(self, contact_name, contact_number):
        contact = {
            'name': contact_name,
            'number': contact_number}

        self.LIST.append(contact)

    def remove_contact(self, contact, number):
        self.LIST.remove({
            'name': contact,
            'number': number})

    def set_list(self, list):
        self.LIST = list

    def get_list(self):
        return self.LIST
 