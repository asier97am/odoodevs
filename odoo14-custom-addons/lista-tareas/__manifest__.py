# -*- coding: utf-8 -*-
{
    'name': "lista-tareas",

    'summary': """
       Sencilla lista de tareas""",

    'description': """
       Sencilla lista de tareas utilizadas para crear un nuevo modulo
con un nuevo modelo de datos
    """,

    'author': "Asier Aranda, DAM2",
    'website': "https://github.com/asier97am",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # Vamos a utilizar la categoría Productivity
    'category': 'Productivity',
    'version': '0.1',
    # Indicamos lista de módulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del módulo "base"
    'depends': ['base'],
    # Esto siempre se carga
    'data': [
    #Este primero indica la politica de acceso del módulo
    'security/ir.model.access.csv',
    #Cargamos las vistas y las plantillas
    'views/views.xml',
    ],
}
