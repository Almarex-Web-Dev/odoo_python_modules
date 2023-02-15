from odoo import fields, api, models


class account(models.Model):
    _inherit = 'account.move'
    partners_id = fields.Many2one('estate.property', "partners")
