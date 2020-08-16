import web 
import app 

render=web.template.render('application/views/personas/')

class Formulario():

    def GET(self):
      try:
        return render.index()
      except Exception as e:
        return "Error" + str(e.args)
