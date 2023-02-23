# -*- coding: utf-8 -*-
# from odoo import http


# class GestionStage(http.Controller):
#     @http.route('/gestion_stage/gestion_stage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_stage/gestion_stage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_stage.listing', {
#             'root': '/gestion_stage/gestion_stage',
#             'objects': http.request.env['gestion_stage.gestion_stage'].search([]),
#         })

#     @http.route('/gestion_stage/gestion_stage/objects/<model("gestion_stage.gestion_stage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_stage.object', {
#             'object': obj
#         })
