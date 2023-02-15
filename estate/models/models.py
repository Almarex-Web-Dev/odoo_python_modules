# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class c:\users\owner\documents\workspaceodoo14\my_module\estate(models.Model):
#     _name = 'c:\users\owner\documents\workspaceodoo14\my_module\estate.c:\users\owner\documents\workspaceodoo14\my_module\estate'
#     _description = 'c:\users\owner\documents\workspaceodoo14\my_module\estate.c:\users\owner\documents\workspaceodoo14\my_module\estate'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
