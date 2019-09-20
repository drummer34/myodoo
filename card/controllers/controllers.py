# -*- coding: utf-8 -*-
from odoo import http

# class Card(http.Controller):
#     @http.route('/card/card/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/card/card/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('card.listing', {
#             'root': '/card/card',
#             'objects': http.request.env['card.card'].search([]),
#         })

#     @http.route('/card/card/objects/<model("card.card"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('card.object', {
#             'object': obj
#         })