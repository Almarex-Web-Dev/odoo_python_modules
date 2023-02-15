# from odoo import models, api, fields
#
#
# class ParkingReservation(models.Model):
#     _name = 'parking.reservation'
#
#     start_time = fields.Datetime(string='Start Time', required=True)
#     end_time = fields.Datetime(string='End Time', required=True)
#     customer_id = fields.Many2one('res.partner', string='Customer', required=True)
#     space_id = fields.Many2one('parking.space', string='Parking Space', required=True)
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('confirmed', 'Confirmed'),
#         ('cancelled', 'Cancelled'),
#     ], string='State', default='draft')
