from odoo import models, fields, api


class ParkingSpace(models.Model):
    _name = 'parking.espace'
    _description = 'Espace de Parking'
    _rec_name = 'espace_id'

    espace_id = fields.Char(string="Espace Id", required=True)
    espace_state = fields.Selection([
        ('disponible', 'Disponible'),
        ('occuper', 'Occuper'),
        ('reserver', 'Reserver'),
    ], string='Espace State', default='disponible')

    # @api.multi
    # def action_occupy(self):
    #     for espace in self:
    #         espace.est_occuper = True
    #
    # @api.multi
    # def action_vacate(self):
    #     for espace in self:
    #         espace.est_occuper = False
    #         espace.occuper_par = False
