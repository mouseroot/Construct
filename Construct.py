"""Construct

"""
class Construct(object):
    """Creates a construct
    """

    def __init__(self, name):
        self.name = name
        self.lifetime = -1
        self.cycles = 0
        self.exists = 1
        self.programming = []
        self.links = []

    def link(self, link):
        """Creates a link to another thing

        Args:
            linkTo: What to link to
        """
        self.links.append(link)

    def program(self, code):
        """Adds code to the construct

        Args:
            code: the programming to add to the Construct
        """
        self.programming.append(code)

    def run(self):
        """Executes the programming of the construct
        """

        for code in self.programming:
            #Energy = new Energy.Netrual
            #Energy.setProgram(code)
            #Energy.ExecuteAndBind()
            print code
