from odoo import models, fields, api


class StockModel(models.Model):
    _name = 'stock.models'
    _description = 'My Stock'
    # _rec_name = 'quantite'

    product_id = fields.Many2one('produit.template', string='Product', required=True)
    fournisseur = fields.Many2one('produit.fournisseur', string='Fournisseur')
    quantite = fields.Integer(related='fournisseur.min_qty', required=True, readonly=True)
    minimum_stock_level = fields.Integer(string='Niveau de stock minimum', default=150)
    maximum_stock_level = fields.Integer(string='Niveau de stock maximum', default=175)
    reorder_level = fields.Integer(compute='_get_qtn', string='Niveau de réapprovisionnement')

    @api.depends('maximum_stock_level')
    def _get_qtn(self):
        for rec in self:
            rec.reorder_level = rec.maximum_stock_level * 2

