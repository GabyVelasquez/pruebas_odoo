from odoo import models, fields

class ProductTemplate(models.Model):
    #_name = '' No se va crear un modelo (tabla) nuevo
    _inherit = 'product.template'#Name del modelo(tabla) que va heredar, es decir a la que se agregarán campos (BD: product_template)

    price2= fields.Monetary(string="Precio 2")
