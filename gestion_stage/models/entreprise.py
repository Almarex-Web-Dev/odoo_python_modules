from odoo import models, fields


class EntrepriseAccueil(models.Model):
    _name = 'entreprise.stage'
    _description = 'Modèle pour gérer les entreprises d\'accueil'

    name = fields.Char(string='Nom de l\'entreprise', required=True)
    adresse = fields.Char(string='Adresse')
    domaine_activite = fields.Char(string='Domaine d\'activité')
    website = fields.Char(string="Website")
    phone = fields.Char(string="Numero de Service client")
    # contacts = fields.One2many('contact', 'entreprise_id', string='Contacts')
    # stages = fields.One2many('gestion.stage.model', 'entreprise_id', string='Stages disponibles')
    tuteur = fields.Char(string='Nom de Tuteur')
    specialite = fields.Char(string='Specialite / role')

