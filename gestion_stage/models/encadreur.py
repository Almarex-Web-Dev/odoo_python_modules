from odoo import fields, models, api


class Encadreur(models.Model):
    _name = 'encadreur.stage'
    _description = 'Modèle pour gérer les encadreurs de stage'

    name = fields.Char(string='Nom d\'encadreur', required=True)
    email = fields.Char(string='Adresse e-mail', required=True)
    telephone = fields.Char(string='Numéro de téléphone', required=True)

