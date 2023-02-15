from odoo import models, fields, api

import datetime


class Fournisseur(models.Model):
    _name = 'produit.fournisseur'
    _description = 'Le Fournisseur de Produit'

    name = fields.Many2one('res.partner', string='Fournisseur', required=True)
    produit_tmpl_id = fields.Many2one('produit.template', string='Article de Produit ', required=True)
    produit_name = fields.Char(related='produit_tmpl_id.name', string='Nom D\'article', readonly=True)
    product_code = fields.Char(related='produit_tmpl_id.produit_id', string='Code de Produit')
    min_qty = fields.Integer(string='Quantite Minimal')
    price = fields.Float(string='Prix')
    monnaie_id = fields.Many2one('res.currency', string='Monnaie')
    retard = fields.Integer(compute='livraison', string='Delai de livraison (Semaine)', readonly=True)
    date_de_depart = fields.Date(string='date de depart')
    date_de_fin = fields.Date(string='Date de fin')

    # @api.onchange('date_de_depart', 'date_de_fin')
    def livraison(self):
        for delai in self:
            if delai.date_de_depart and delai.date_de_fin:
                depart = fields.Datetime.to_datetime(delai.date_de_depart).date()
                fin = fields.Datetime.to_datetime(delai.date_de_fin).date()
                self.retard = str(int((fin - depart).days / 7))
            else:
                self.retard = 'No date specified!'

    # help="Lead time in days between the confirmation of the "
# "purchase order and the receipt of the products in your "
#  "warehouse."


# PRODUCT BUYERfrom odoo import models, fields
#
# class ProductBuyer(models.Model):
#     _name = 'product.buyer'
#
#     name = fields.Char(string='Buyer Name', required=True)
#     email = fields.Char(string='Email')
#     phone = fields.Char(string='Phone')
#     product_ids = fields.One2many('product.template', 'buyer_id', string=
