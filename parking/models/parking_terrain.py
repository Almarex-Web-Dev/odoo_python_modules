from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ParkingTerrain(models.Model):
    _name = 'parking.terrain'
    _description = 'Terrain de Parking'
    _rec_name = 'numero_de_plaque'

    # name = fields.Char(string='Name', required=True)
    # address = fields.Char(string='Address', required=True)
    espace_total = fields.Integer(compute='_compute_total_spaces', string="Espace Total", readonly=True)
    espace_disponible = fields.Integer(compute='_compute_available_spaces', string="Espace disponible", readonly=True)
    Espace_id = fields.Many2one('parking.espace', 'Espace Id')
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('occuper', 'Occuper'),
        ('reserver', 'Reserver'),
    ], string='State', required=True, tracking=True)
    numero_de_plaque = fields.Many2one('parking.vehicule', string="numero de plaque", required=True)
    marque_id = fields.Char(related='numero_de_plaque.marque', string="Marque de Vehicule", required=True)
    model = fields.Char(related='numero_de_plaque.model', required=True)
    vehicule_type = fields.Many2one('parking.vehicule.type', string="type de vehicule")
    # related = 'numero_de_plaque.vehicule_type'
    proprietaire = fields.Many2one(related='numero_de_plaque.owner_id', string='Proprietaire')
    montant = fields.Integer(related='vehicule_type.Montant', require=True, readonly=True)
    image = fields.Binary(string='Image de Voiture')
    heure_arriver = fields.Date(string="L'heure d'arriver")
    heure_de_départ = fields.Datetime(string='Heure de départ')

    # @api.depends('Espace_id')
    # @api.onchange('Espace_id')
    def _compute_total_spaces(self):
        self.espace_total = self.env['parking.espace'].search_count([])

    # CHANGE THE FIELDS BASE ON THE ESPACE IDS VALUE

    @api.onchange('Espace_id')
    def _get_state_value(self):
        if self.Espace_id:
            if self.Espace_id.espace_state:
                self.state = self.Espace_id.espace_state
        else:
            self.state = ''

    @api.depends("espace_total")
    @api.onchange("espace_total")
    def _compute_available_spaces(self):
        self.espace_disponible = self.espace_total - self.env['parking.terrain'].search_count([])

    # creer un enregistrement et checker si le id de enregistrement existe deja
    @api.model
    def create(self, vals):
        print(vals)
        records = vals['Espace_id']
        existe = self.env['parking.terrain'].search([])
        for item in existe:
            # print(item.Espace_id.espace_id)
            if records == item.Espace_id.id:
                raise ValidationError("L'espace est deja occuper")
            else:
                pass
        return super(ParkingTerrain, self).create(vals)

    def button_parking_report(self):
        return self.env.ref('parking.parking_terrain_report').report_action(self)

    # remove this
    # parking_ids = fields.One2many('parking.espace', 'parking_id', string='Espaces')

    # @api.multi
    # def action_occupy(self):
    #     for lot in self:
    #         lot.spaces.action_occupy()
    #
    # @api.multi
    # def action_vacate(self):
    #     for lot in self:
    #         lot.spaces.action_vacate()

# class ParkingLot(models.Model):
#     _name = 'parking.lot'
#
#     name = fields.Char(string='Name', required=True)
#     address = fields.Char(string='Address', required=True)
#     total_spaces = fields.Integer(string='Total Spaces', required=True)
#     available_spaces = fields.Integer(string='Available Spaces', compute='_compute_available_spaces')
#
#     @api.depends('total_spaces', 'parking_space_ids.state')
#     def _compute_available_spaces(self):
#         for lot in self:
#             occupied_spaces = sum(space.state == 'occupied' for space in lot.parking_space_ids)
#             lot.available_spaces = lot.total_spaces - occupied_spaces


# class ParkingSpace(models.Model):
#     _name = 'parking.space'
#
#     name = fields.Char(string='Space Number', required=True)
#
#     type = fields.Selection([
#         ('compact', 'Compact'),
#         ('standard', 'Standard'),
#         ('handicap', 'Handicap'),
#     ], string='Type', required=True)
#     state = fields.Selection([
#         ('available', 'Available'),
#         ('occupied', 'Occupied'),
#         ('reserved', 'Reserved'),
#     ], string='State', default='available')
#     lot_id = fields.Many2one('parking.lot', string='Parking Lot')


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


# class ParkingPricing(models.Model):
#     _name = 'parking.pricing'
#
#     type = fields.Selection([
#         ('compact', 'Compact'),
#         ('standard', 'Standard'),
#         ('handicap', 'Handicap'),
#     ], string='Type', required=True)
#     time_of_day = fields.Selection([
#         ('morning', 'Morning'),
#         ('afternoon', 'Afternoon'),
#         ('evening', 'Evening'),
#     ], string='Time of Day', required=True)
#     duration = fields.Float(string='Duration (Hours)', required=True)
#     price = fields.Float(string='Price (USD)', required=True)


# class ParkingInvoice(models.Model):
#     _name = 'parking.invoice'
#
#     reservation_id = fields.Many2one
