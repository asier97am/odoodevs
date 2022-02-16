# -*- coding: utf-8 -*-
# from odoo import http


# class EstoesunaPrueba(http.Controller):
#     @http.route('/estoesuna_prueba/estoesuna_prueba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estoesuna_prueba/estoesuna_prueba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estoesuna_prueba.listing', {
#             'root': '/estoesuna_prueba/estoesuna_prueba',
#             'objects': http.request.env['estoesuna_prueba.estoesuna_prueba'].search([]),
#         })

#     @http.route('/estoesuna_prueba/estoesuna_prueba/objects/<model("estoesuna_prueba.estoesuna_prueba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estoesuna_prueba.object', {
#             'object': obj
#         })
