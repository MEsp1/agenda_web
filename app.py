import web
import sqlite3

urls = (
    "/", "Personas",
    "/detalle", "Detalle",
    "/editar", "Editar",
    "/borrar", "Borrar"
)

app = web.application(urls, globals())
render = web.template.render("views/")


class Personas:
    def GET(self):
        try:
            conection = sqlite3.connect("agenda.db")
            cursor = conection.cursor()
            result = cursor.execute("select * from personas")
            return render.personas(result)
        except Exception as e:
            print(f"Error001:{e}")
            return f"No se puedo conectar a la base de datos"

    def POST(self):
        form = web.input()
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        cursor.execute(
            "insert into personas(nombre,email) values (?, ?)",
            (form.nombre, form.email),
        )
        conection.commit()
        conection.close()
        raise web.seeother("/")


class Editar:
    def GET(self, id):
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        cursor.execute("select * from personas where id=?", (id,))
        persona = cursor.fetchone()
        conection.close()
        if persona:
            return render.editar(persona)
        else:
            return "Persona no encontrada"


if __name__ == "__main__":
    app.run()