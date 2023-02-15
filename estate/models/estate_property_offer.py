from odoo import models, fields, api

from odoo.exceptions import ValidationError


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offers'
    _description = "Estate property offers"
    _order = "price desc"

    price = fields.Integer(string="Price")
    status = fields.Selection([('refuse', 'Refused'), ('accept', 'Accepted')], string="status")
    partner_ids = fields.Many2one("res.partner", "Partner")
    property_id = fields.Many2one("estate.property", "Estate")
    # property_type_id = fields.Char(related="property_id")
    validity = fields.Integer(string="Validity", default="7")
    date_deadline = fields.Date(string="Deadline")

    # add functionality to the selling and expected price
    @api.onchange("property_id.price", "property_id.selling_price", "property.buyer_id")
    @api.depends("status")
    def accept(self):
        estate_percentage = self.price / self.property_id.expected_price
        format_price = int('{:.0%}'.format(estate_percentage).rstrip("%"))
        MY__PERCENTAGE = int("{:.0%}".format(0.9).rstrip("%"))
        self.status = "accept"
        if self.status == "accept":
            self.property_id.state = "offer accepted"
            self.property_id.buyer_id = self.partner_ids
            self.property_id.price = self.price
            if format_price >= MY__PERCENTAGE:
                self.property_id.selling_price = self.price
            else:
                raise ValidationError('''The Selling price must be at least 90% of the expected price. You must reduce
                the expected price if you want to accept this offer''')
        elif self.status != "accept":
            self.property_id.buyer_id = ''
            self.property_id.price = 0
            self.property_id.selling_price = 0

    @api.depends("status")
    def refuse(self):
        self.status = "refuse"
        # if self.status == 'refuse':
        #     self.property_id.state = 'new'

    # Raise a validation error when a buyer provides a negative number value
    @api.constrains("price")
    def is_positive(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Negative %s is not valid" % record.price)

    # When an offer is created, the state should switch to offer received
    # @api.depends('property_id')
    # @api.constrains('property_id')
    @api.model
    def create(self, vals):
        current_price = vals['price']
        prop_offer = self.env['estate.property'].browse(vals['property_id'])
        # check if current price is less than existing
        print(prop_offer.best_price)
        if current_price <= prop_offer.best_price:
            # if the price is less, raise a validation error
            raise ValidationError(f'Current price must be greater than existing price which is {prop_offer.best_price}')
        else:
            prop_offer.state = 'offer received'
        return super(EstatePropertyOffer, self).create(vals)
