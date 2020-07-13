# -*- coding: utf-8 -*-
# from odoo import http


# class E-learning(http.Controller):
#     @http.route('/e-learning/e-learning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e-learning/e-learning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('e-learning.listing', {
#             'root': '/e-learning/e-learning',
#             'objects': http.request.env['e-learning.e-learning'].search([]),
#         })

#     @http.route('/e-learning/e-learning/objects/<model("e-learning.e-learning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e-learning.object', {
#             'object': obj
#         })
