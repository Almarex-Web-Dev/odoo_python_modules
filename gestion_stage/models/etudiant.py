from odoo import models, fields, api
import uuid


class Etudiant(models.Model):
    _name = 'etudiant.stage'
    _description = 'Modèle pour gérer les étudiants'
    _rec_name = 'name'

    name = fields.Char(string='Nom', required=True)
    matricule = fields.Char(string="Matricule", default=lambda self: str('STG') + str(uuid.uuid4()).split('-')[-1].upper())
    email = fields.Char(string='Adresse e-mail')
    date_naissance = fields.Date()
    adresse = fields.Char()
    code_postal = fields.Char()
    state = fields.Many2one("res.country.state", string='Ville', ondelete='restrict')
    country = fields.Many2one('res.country', string='Country', ondelete='restrict')
    statut = fields.Selection([('active', 'Active'), ('conger', 'Conger')])
    phone = fields.Char(string='Numéro de téléphone')
    niveau_etude = fields.Selection([('bachelor', 'Bachelor'), ('master', 'Master'), ('doctorat', 'Doctorat')],
                                    string='Niveau d\'études')
    filiere = fields.Many2one('filiere.stage', string="Filiere")
    image = fields.Binary(string='Image d\'etudiant ')

    # @api.onchange('name', 'matricule')
    # def concatenate(self):
    #     for rec in self:
    #         concate_name = rec.name.join(rec.matricule)
    #         self.name = concate_name
    #         print(concate_name)
