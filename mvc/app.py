import web
import * as sio from 'socket.io';

urls = (
    '/', 'mvc.controllers.personas.delete.Delete',
    '/', 'mvc.controllers.personas.index.Index',
    '/', 'mvc.controllers.personas.insert.Insert',
    '/', 'mvc.controllers.personas.list.List',
    '/', 'mvc.controllers.personas.update.Update',
    '/', 'mvc.controllers.personas.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('10.0.0.253', 8080))
    except:
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('10.0.0.253', 8080))

    s.listen(1)
    conn, addr = s.accept()
    app.run()