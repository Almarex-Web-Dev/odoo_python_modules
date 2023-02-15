from odoo import models, fields


class ProduitClient(models.Model):
    # _name = 'produit.client'
    _inherit = 'res.partner'

    customer = fields.Boolean(string='Is a Customer', default=True)
    street = fields.Char(string='Street', required=True)
    street2 = fields.Char(string='Street2')
    zip = fields.Char(change_default=True, size=24)
    city = fields.Char(string='City')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    fax = fields.Char(string='Fax')
    website = fields.Char(string='Website')