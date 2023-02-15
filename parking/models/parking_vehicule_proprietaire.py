from odoo import models, fields


class CarParkOwner(models.Model):
    _name = 'parking.vehicule.proprietaire'
    _description = 'Properitaire de vehicule'

    name = fields.Many2one('res.partner', 'Proprietaire')
    address = fields.Char(string='Address')
    numero_telephone = fields.Char(string="Numero de Telephone")
    Owner_ids = fields.One2many('parking.vehicule', 'owner_id', string='Owner Ids')
