from odoo import models, fields


class EtablissementStage(models.Model):
    _name = 'etablissement.stage'

    name = fields.Char(string="Nom")
    website = fields.Char(string="Website")
    address = fields.Text(string="Adresse")
    phone = fields.Char(string="Téléphone")
    email = fields.Char(string="Email")
    description = fields.Text(string="Description")
    # domaines_stage = fields.Many2many('domaine.stage', string='Domaines de stage')
    # offres_stage = fields.One2many('offre.stage', 'etablissement_stage_id', string='Offres de stage')
