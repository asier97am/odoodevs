# -*- coding: utf-8 -*-
# from odoo import http


# class Lista-tareas(http.Controller):
#     @http.route('/lista-tareas/lista-tareas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lista-tareas/lista-tareas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lista-tareas.listing', {
#             'root': '/lista-tareas/lista-tareas',
#             'objects': http.request.env['lista-tareas.lista-tareas'].search([]),
#         })

#     @http.route('/lista-tareas/lista-tareas/objects/<model("lista-tareas.lista-tareas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lista-tareas.object', {
#             'object': obj
#         })
