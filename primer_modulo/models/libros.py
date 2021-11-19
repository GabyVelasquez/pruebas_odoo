from odoo import models, fields, api

# Creando un modelo (tabla de la BD) a partir de una clase
class Libros(models.Model):
    _name = 'libros'  # = nombre de la tabla en minúsculas
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Nombre del libroD', required=True, tracking=True)  # Nombre del campo de tabla = Nombre del campo en vista
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del autor")
    image = fields.Binary(string="Image")
    categoria_id=fields.Many2one(comodel_name="categoria_libro")
    state=fields.Selection([('draft','Borrador'),('published','Publicado')], default='draft')
    description = fields.Char(string="Descripción", compute="_compute_description") #, store=True - Para guardar en la BD

    #@api.depends('name','isbn') #Para que actualice el cambio sin presionar botón guardar
    def _compute_description(self):
        self.description = self.name + " | " + self.isbn + " | " + self.autor_id.name + " | " + self.categoria_id.name

    def boton_publicar(self):
        self.state = 'published'
        print("PRUEBA CLICK BOTON")
    def boton_borrador(self):
        self.state = 'draft'

    #EVITAR DATOS REPETIDOS: CONTRAINTS
    _sql_constraints = [("name_uniq","unique(name)","El nombre del libro ya existe")]
    #nombre del sql contraint, unique(los valores que no se duplicarán),mensaje de error



class CatergoriaLibro(models.Model):
    _name='categoria_libro'

    name = fields.Char(string="Nombre de la categoría")