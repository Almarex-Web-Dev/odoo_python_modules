from odoo import models, fields, api

from odoo.exceptions import ValidationError


class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Estate Property Tags"
    _order = "name"

    name = fields.Char(string="Name", widget="Many2many_fields")
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="color")

    @api.constrains("name")
    def is_unique(self):
        for rec in self:
            isExist = self.env['estate.property.tags'].search([("name", "=", rec.name), ("id", "!=", rec.id)])
            if isExist:
                raise ValidationError("Name %s must be unique" % rec.name)