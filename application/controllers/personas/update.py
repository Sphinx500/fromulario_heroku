import web 
import app 

import application.models.personas as personas
model_personas = personas.Personas()
render=web.template.render('application/views/personas/')

class Update():

    def GET(self, matricula):
      try:
        result = model_personas.view(matricula)[0]
        #print(result)
        return render.update(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, matricula):
        try:
            form = web.input()
            matricula = form.matricula
            nombre = form.nombre
            pri_ap = form.pri_ap
            seg_ap = form.seg_ap
            age = form.age
            fdate = form.fdate
            gender = form.gender
            state = form.state
            model_personas.update(matricula,nombre,pri_ap,seg_ap,age,fdate,gender,state)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"
