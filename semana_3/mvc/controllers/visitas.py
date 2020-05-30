class Visitas:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'