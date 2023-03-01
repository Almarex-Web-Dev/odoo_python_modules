from odoo import fields, models, api


class Encadreur(models.Model):
    _name = 'encadreur.stage'
    _description = 'Modèle pour gérer les encadreurs de stage'

    name = fields.Char(string='Nom d\'encadreur', required=True)
    email = fields.Char(string='Adresse e-mail', required=True)
    phone = fields.Char(string='Numéro de téléphone', required=True)
    specialite = fields.Char(string='Spécialité', required=True)
    # stages_encadres = fields.One2many('gestion.stage.model', 'encadreur_id', string='Stages encadrés')
    encadreur_image = fields.Binary(string='Image d\'encadreur')
