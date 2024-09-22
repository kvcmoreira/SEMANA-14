import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear Frames
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Lista de Eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Campos de Entrada
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.cal = Calendar(self.frame_entrada, selectmode='day')
        self.cal.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.entry_hora = ttk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entry_desc = ttk.Entry(self.frame_entrada)
        self.entry_desc.grid(row=2, column=1)

        # Botones
        btn_agregar = ttk.Button(self.frame_entrada, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.grid(row=3, column=0, pady=5)

        btn_eliminar = ttk.Button(self.frame_entrada, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.grid(row=3, column=1, pady=5)

        btn_salir = ttk.Button(self.frame_entrada, text="Salir", command=self.salir_aplicacion)
        btn_salir.grid(row=4, columnspan=2, pady=5)

    def agregar_evento(self):
        fecha = self.cal.get_date()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_hora.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def salir_aplicacion(self):
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas salir?")
        if confirm:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()




