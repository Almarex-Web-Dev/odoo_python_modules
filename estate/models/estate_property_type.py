from odoo import fields, models, api

from odoo.exceptions import ValidationError, UserError


class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name"

    def aprt(self):
        nbre = self.env['estate.property'].search_count([('type', '=', "Apartment")])
        self.nombre_apartement = nbre

    def house(self):
        nbre = self.env['estate.property'].search_count([('type', '=', "House")])
        self.nombre_house = nbre

    nombre_apartement = fields.Integer(compute='aprt')
    nombre_house = fields.Integer(compute='house')
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("estate.property", "model_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            user_name = self.env["estate.property.type"].search([("name", "=", record.name),
                                                                 ("id", "!=", record.id)])
            if user_name:
                raise ValidationError(("Name %s must be unique. User already exists" % record.name))

    def offer_apartment(self):
        return {
            'name': 'Apartment',
            'res_model': 'estate.property',
            'view_mode': 'list,form',
            'context': {},
            'domain': [('type', '=', 'Apartment')],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }
        # context = self.env.context.copy()
        # for record in self:
        #     form_id = self.env.ref("estate.view_estate_property_tree").id
        #     return {
        #         'type': 'ir.actions.act_window',
        #         'name': ('Apartment'),
        #         'view_type': 'list',
        #         'view_mode': 'list',
        #         'res_model': 'estate.property',
        #         'views': [(form_id, 'list')],
        #         'domain': [('type', '=', 'Apartment')],
        #         'target': 'current',
        #         'context': context,
        #     }

    def offers_house(self):
        return {
            'name': 'House',
            'res_model': 'estate.property',
            'view_mode': 'list,form',
            'context': {},
            'domain': [('type', '=', 'House')],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }
