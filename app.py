import web
import sqlite3

urls = (
    "/", "Personas",
    "/detalle/(.*)", "Detalle",
    "/editar/(.*)", "Editar",
    "/borrar/(.*)", "Borrar"
)

app = web.application(urls, globals())
render = web.template.render("views/")

class Personas:
    def GET(self):
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        result = cursor.execute("SELECT * FROM personas")
        return render.personas(result)

    def POST(self):
        form = web.input()
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        cursor.execute("INSERT INTO personas (nombre, email) VALUES (?, ?)", (form.nombre, form.email))
        conection.commit()
        conection.close()
        raise web.seeother("/")

if __name__ == "__main__":
    app.run()
