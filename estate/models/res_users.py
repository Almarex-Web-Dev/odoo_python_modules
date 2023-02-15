from odoo import fields, models, api


# from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'user_id')


