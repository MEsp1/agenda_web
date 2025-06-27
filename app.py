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
        try:
            form = web.input()
            conection = sqlite3.connect("agenda.db")
            cursor = conection.cursor()
            cursor.execute("INSERT INTO personas (nombre, email) VALUES (?, ?)", (form.nombre, form.email))
            conection.commit()
            conection.close()
            raise web.seeother("/")
        except Exception as e:
            return f"Error: {str(e)}"

class Detalle:
    def GET(self, id_persona):
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        result = cursor.execute("SELECT * FROM personas WHERE id_persona = ?", (id_persona,))
        persona = result.fetchone()
        conection.close()
        if persona:
            return render.detalle(persona)
        return "Persona no encontrada"

class Editar:
    def GET(self, id_persona):
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        result = cursor.execute("SELECT * FROM personas WHERE id_persona = ?", (id_persona,))
        persona = result.fetchone()
        conection.close()
        if persona:
            return render.editar(persona)
        return "Persona no encontrada"

    def POST(self, id_persona):
        try:
            form = web.input()
            conection = sqlite3.connect("agenda.db")
            cursor = conection.cursor()
            cursor.execute("UPDATE personas SET nombre = ?, email = ? WHERE id_persona = ?", (form.nombre, form.email, id_persona))
            conection.commit()
            conection.close()
            raise web.seeother("/")
        except Exception as e:
            return f"Error: {str(e)}"

class Borrar:
    def GET(self, id_persona):
        conection = sqlite3.connect("agenda.db")
        cursor = conection.cursor()
        result = cursor.execute("SELECT * FROM personas WHERE id_persona = ?", (id_persona,))
        persona = result.fetchone()
        conection.close()
        if persona:
            return render.borrar(persona)
        return "Persona no encontrada"
    

    def POST(self, id_persona):
        try:
            conection = sqlite3.connect("agenda.db")
            cursor = conection.cursor()
            cursor.execute("DELETE FROM personas WHERE id_persona = ?", (id_persona,))
            conection.commit()
            conection.close()
            raise web.seeother("/")
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run()