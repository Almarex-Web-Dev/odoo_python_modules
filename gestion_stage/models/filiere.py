from odoo import models, fields


class FiliereStage(models.Model):
    _name = 'filiere.stage'
    _description = 'Modèle pour gérer les filières de stage'

    name = fields.Char(string='Nom de la filière', required=True)
    description = fields.Char(string='Description de la filière')
    # stages = fields.One2many('gestion.stage.model', 'filiere_id', string='Stages disponibles')
