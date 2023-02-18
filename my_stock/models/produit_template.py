import uuid

from odoo import fields, models, api


class ProduitTemplate(models.Model):
    _name = 'produit.template'
    _description = 'Articles (Produit Template)'
    # _rec_name = 'categ_id'

    name = fields.Char(string='Nom D\'artcile', required=True)
    categ_id = fields.Many2one('produit.categorie', string='Categorie')
    type = fields.Selection([
        ('consom', 'Consommable'),
        ('service', 'Service'),
        ('produit', 'Produit stockable')
    ], string='Product Type', default='product', required=True)
    description = fields.Text(string='Description')
    list_price = fields.Integer(string='prix de produit')
    prix_standard = fields.Integer(string='Prix standard')
    # qty_disponible = fields.Integer(string='Quantiter de produit')
    image = fields.Binary(string='Image')
    produit_id = fields.Char(string='Produit ID', default=lambda self: str(uuid.uuid4()))
    seller_ids = fields.One2many('produit.fournisseur', 'produit_tmpl_id', string='Fournisseur')
    # buyer_id = fields.Many2one('product.buyer', string='Buyer')

    # Électronique - Biens de consommation
    # Vêtements et accessoires
    # Jouets - Biens de consommation
    # Électroménagers - Biens de consommation
    # Meubles - Articles pour la maison
    # Produits de Beauté - Santé & Beauté
    # Équipement de sport - Articles de sport
    # Épicerie - Nourriture et boissons
    # Équipement de plein air - Articles de sport
    # Fournitures de bureau - Papeterie & fournitures de bureau
