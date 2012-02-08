class BaseBackend(object):

    def initialize(self, **kwargs):
        self.config = kwargs

    def push_contacts(self, contacts, **kwargs):
        raise NotImplemented('Create a subclass and use that')
