from odoo import models, fields, api


class VehiculeType(models.Model):
    _name = 'parking.vehicule.type'
    _description = 'Parking Vehicule Type'
    _rec_name = 'type'

    type = fields.Char(string="Name", required=True)
    Montant = fields.Integer(string='Montant par type')