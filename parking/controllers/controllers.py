# -*- coding: utf-8 -*-
# from odoo import http


# class Parking(http.Controller):
#     @http.route('/parking/parking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parking/parking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parking.listing', {
#             'root': '/parking/parking',
#             'objects': http.request.env['parking.parking'].search([]),
#         })

#     @http.route('/parking/parking/objects/<model("parking.parking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parking.object', {
#             'object': obj
#         })
