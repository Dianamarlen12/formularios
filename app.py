import web

urls = (
    '/delete', 'mvc.controllers.personas.delete.Delete',
    '/insert', 'mvc.controllers.personas.index.Index',
    '/', 'mvc.controllers.personas.insert.Insert',
    '/list', 'mvc.controllers.personas.list.List',
    '/update', 'mvc.controllers.personas.update.Update',
    '/view', 'mvc.controllers.personas.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8090))
    app.run()