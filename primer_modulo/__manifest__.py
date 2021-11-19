# -*- coding: utf-8 -*-
{
    'name': "Curso de programacion Odoo 14",
    'summary':"""
        Curso de programacion Odoo 14, funcionalidades
    """,
    'author':'Gaby',
    'category':'General',
    'version':'1.0.0',
    'depends':['mail'],
    'data':[
        'views/menu_view.xml',
        'views/libros_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv'
    ],
    'license': 'LGPL-3',
}