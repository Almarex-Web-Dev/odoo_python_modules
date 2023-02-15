# -*- coding: utf-8 -*-
# from odoo import http


# class MyStock(http.Controller):
#     @http.route('/my_stock/my_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_stock/my_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_stock.listing', {
#             'root': '/my_stock/my_stock',
#             'objects': http.request.env['my_stock.my_stock'].search([]),
#         })

#     @http.route('/my_stock/my_stock/objects/<model("my_stock.my_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_stock.object', {
#             'object': obj
#         })
