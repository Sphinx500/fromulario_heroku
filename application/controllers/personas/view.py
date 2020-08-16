import web 
import app 

import application.models.personas as personas

model_personas = personas.Personas()

render=web.template.render('application/views/personas')

class View():

    def GET(self, matricula):
      try:
        result = model_personas.view(matricula)[0]
        return render.view(result)
      except Exception as e:
        return "Error" + str(e.args)
