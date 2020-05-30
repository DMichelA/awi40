import web
from datetime import date
from datetime import datetime
  

class Visitas:
    def GET(self, nombre):
      try:
        cookie = web.cookies()
        visitas = "0"
        fecha = date.today()
        hora = datetime.now()
        format = hora.strftime("Hora visita: %H, Minutos: %M, Segundos: %S")
        print(cookie)

        if nombre:
          web.setcookie("nombre",nombre,expires="", domain=None)
        else:
          nombre = "Anonimo"
          web.setcookie("nombre",nombre,expires="", domain=None)

        if cookie.get("visitas"):
          visitas = int(cookie.get("visitas"))
          visitas += 1
          web.setcookie("visitas", str(visitas),expires="", domain=None)
        else:
          web.setcookie("visitas", str(1),expires="", domain=None)
          visitas = "1"
        
        if cookie.get("fecha"):
          web.setcookie("fecha", fecha, expires="", domain=None)
        else:
          web.setcookie("fecha", fecha, expires="", domain=None)

        if cookie.get("hora"):
          web.setcookie("hora", format, expires="", domain=None)
        else: 
          web.setcookie("hora", format, expires="", domain=None)


        return "Visitas " + str(visitas) + " Nombre " + nombre + "\nFecha visita: " + str(fecha) + "\n" + str(format)
      except Exception as e:
          return "Error " + str(e.args)

