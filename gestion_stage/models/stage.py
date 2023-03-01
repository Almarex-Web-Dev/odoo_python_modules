from odoo import models, fields


class Stage(models.Model):
    _name = 'gestion.stage.model'
    _description = 'Modèle pour gérer les stages'
    _rec_name = 'name'

    name = fields.Many2one('etudiant.stage', string='Nom de Stager', required=True)
    matricule_id = fields.Char(related='name.matricule', string='Matricule de Stager', required=True)
    description = fields.Text(string='Description du stage')
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    filiere_id = fields.Many2one(related='name.filiere', string='Filière')
    entreprise_id = fields.Many2one('entreprise.stage', string="Entreprise")
    encadreur_id = fields.Many2one('encadreur.stage', string="Encadreur")
    missions = fields.Text(string='Missions confiées')
    competences = fields.Text(string='Compétences développées')
