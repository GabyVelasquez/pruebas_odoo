from odoo import models, fields

# Creando un modelo (tabla de la BD) a partir de una clase
class Autor(models.Model):
    _name = 'autor'  # = nombre de la tabla (modelo) en minúsculas
    #_rec_name = 'last_name' #Campo a retornar en una relación ManytoOne al seleccionar

    name = fields.Char(string='Nombre del autorD', required=True)  # Nombre del campo de tabla = Nombre del campo en vista
    last_name = fields.Char(string="Apellido")
