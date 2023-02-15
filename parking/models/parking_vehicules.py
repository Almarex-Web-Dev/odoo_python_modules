from odoo import models, fields, api


class CarPark(models.Model):
    _name = 'parking.vehicule'
    _description = 'Parking de Vehicule'
    _rec_name = 'numero_de_plaque'

    # vehicule_name = fields.Char(string='Name', required=True)
    marque = fields.Char(string='Marque du véhicule', required=True)
    model = fields.Char(string='Model', required=True)
    vehicule_type = fields.Many2one("parking.vehicule.type", string="type de vehicule")
    numero_de_plaque = fields.Char(string='Numero de plaque', required=True)
    owner_id = fields.Many2one('parking.vehicule.proprietaire', string='Owner')
