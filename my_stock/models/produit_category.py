from odoo import fields, models, api


class StockCategory(models.Model):
    _name = 'produit.categorie'
    _description = 'Categorie de Produit'

    name = fields.Char(string='Category Name')
    parent_id = fields.Many2one('produit.categorie', string='Parent Categorie')
    # child_ids = fields.One2many('produit.categorie', 'parent_id', string='Child Categorie')
    produits_ids = fields.One2many('produit.template', 'categ_id', string='Produits IDS')
