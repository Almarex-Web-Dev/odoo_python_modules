from odoo import models, fields, api
from odoo.exceptions import ValidationError


# import math


class EstateModel(models.Model):
    _name = "estate.property"
    _description = "Estate property model"
    _order = "id"
    _inherit = 'mail.thread'

    model_id = fields.Many2one("estate.property.type")
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Integer(string="Expected_price", required=True)
    selling_price = fields.Integer(string="Selling price", readonly=True)
    bedrooms = fields.Integer(string="Bedrooms", default="2")
    living_area = fields.Integer(string="Living area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([("east", "East"), ("north", "North"), ("south", "South"), ("west", "West")],
                                          required=True)

    state = fields.Selection([("new", "New"), ("offer received", "Offer Received"),
                              ("offer accepted", "Offer Accepted"),
                              ("sold", "Sold"), ('cancel', 'Cancelled')], default="new", string="state")

    status = fields.Selection([("new", "New"), ("cancel", "Cancelled")], string="Status", default="new")
    property_image = fields.Binary(string="Property Image")


    # Property Location
    # location = fields.Selection([('london', "London"), ('qatar', "Qatar"),('spain', "Spain"),
    #                             ('london', "London"),('london', "London")])
    
    
    # Delete an offer where the state of the offer is not equal to sold or offer accepted
    def unlink(self):
        print("Item is successfully deleted !!!")
        if self.state == 'sold' or self.state == 'offer accepted':
            raise ValidationError("You can only delete new or cancelled offers")
        return super(EstateModel, self).unlink()

    type = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    price = fields.Integer(string="Price")
    seller_id = fields.Many2one('res.users', string="Salesperson", index=True)
    # index = True, tracking = True, default = lambda self: self.env.user
    property_type_id = fields.Many2one('res.partner', string='Partner')
    tags_ids = fields.Many2many("estate.property.tags", string="Tags")
    offers_ids = fields.One2many("estate.property.offers", 'property_id')
    total_area = fields.Integer(compute='_calc_total_', string='Total Area (sqm)')
    user_id = fields.Many2one('res.users', string='user offers')
    best_price = fields.Integer(string="Best offer", readonly=True)
    
    country = fields.Many2one(comodel_name='res.country', string='Country',
                              help='Select Country', ondelete='restrict')
    
    # city_id = fields.Many2one('res.city', 'City',  ondelete='restrict')
    state_id = fields.Many2one('res.country.state', string='State', domain="[('country_id', '=?', country)]")
    city = fields.Char('City', required=True)
    zip = fields.Char('ZIP', required=True)
    street = fields.Char('Street')
    house_number_or_name = fields.Char('House Number Or Name', required=True)

    
    # country_id = fields.Many2one('res.country', string='Country', domain=[('code', 'in', ADYEN_AVAILABLE_COUNTRIES)], required=True)
    # country_code = fields.Char(related='country_id.code')
    # state_code = fields.Char(related='state_id.code')

    # get all the price of an offers
    @api.depends('offers_ids')
    @api.onchange('offers_ids')
    @api.constrains('offers_ids')
    def get_all_price(self):
        price_list = []
        for record in self:
            for rec in record.offers_ids:
                if rec.price:
                    price_list.append(rec.price)
                    self.best_price = max(price_list)
                else:
                    self.best_price = len(price_list)
                    self.state = 'new'

    @api.depends("garden_area", "living_area")
    def _calc_total_(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.onchange("garden", "garden_area", "garden_orientation")
    def _change_garden_(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = self.garden_area
            self.garden_orientation = self.garden_orientation

    def cancel(self):
        if self.status == "new" or self.state == 'offer received':
            self.status = "cancel"
            self.state = 'cancel'

    def sold(self):
        self.state = "sold"
        if self.status == "cancel":
            raise ValidationError("Cancelled properties can not be sold")

    def button_report_property(self):
        return self.env.ref('estate.report_estate_property').report_action(self)

# class EstateModeLine(models.Model):
#     _name = "estate.property.line"
#     _description = "Estate property line model"
#
#     name = fields.Char(string="Name", required=True)
#     description = fields.Text(string="Description")
#     property_id = fields.Many2one('estate.property', string='property')
