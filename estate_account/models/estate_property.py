from odoo import fields, models, api, _

from odoo.exceptions import ValidationError


class estateProperty(models.Model):
    _inherit = 'estate.property'
    invoice_ids = fields.One2many('account.move', 'partners_id', string="Factures")

    def sold(self):
        context = self._context.copy()
        context.update({
            'partners_id': self.id,
        })
        invoice_obj = self.env['account.move']
        # On va verifier si on est dans le context de location
        if context:
            # on va comparer les éléments
            loca = invoice_obj.search([
                ('partner_id', '=', self.buyer_id.id),
                ('partners_id', '=', self.id)
            ])
            if loca:
                raise ValidationError(_("La facture de ce client pour ce vehicule a été dejà crée ."))
            else:
                self.state = "sold"
                # Création de la facture
                invoice_values = {
                    'move_type': 'out_invoice',
                    'currency_id': self.env.user.company_id.currency_id.id,
                    'partner_id': self.buyer_id.id,
                    'partners_id': self.id,
                    'invoice_line_ids': [(0, 0, {
                        'name': "LOCATION " + str(self.name),
                        'price_unit': self.price,
                        'quantity': 1.0,
                    })],
                }

                # invoice_obj = self.env['account.move']
                invoice = invoice_obj.create(invoice_values)
                res = self.sudo().env.ref('account.action_move_out_invoice_type')
                res = res.read()[0]
                res.update({
                    'domain': str([('partners_id', '=', self.id)]),
                })
                return res

        # print("*************It is working****************")
        return super(estateProperty, self).sold()
