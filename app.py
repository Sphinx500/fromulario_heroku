import web

urls = (
    '/', 'application.controllers.personas.fields.Formulario',
    '/delete/(.*)', 'application.controllers.personas.delete.Delete',
    '/insert', 'application.controllers.personas.insert.Insert',
    '/list', 'application.controllers.personas.list.List',
    '/update/(.*)', 'application.controllers.personas.update.Update',
    '/view/(.*)', 'application.controllers.personas.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()