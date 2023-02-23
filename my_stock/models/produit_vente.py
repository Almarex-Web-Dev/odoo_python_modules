from odoo import fields, models, api
import uuid


class SaleOrder(models.Model):
    _name = 'sale.order'
    _description = 'Sale Order Models'
    _rec_name = 'ref_commande'

    name = fields.Char(string='Sale')
    ref_commande = fields.Char(string='Référence de commande de Client',
                               default=lambda self: str(uuid.uuid4()).split('-')[-1])
    partner_id = fields.Many2one('res.partner', string='Customer')
    order_line_ids = fields.One2many('sale.order.line', 'order_id', string='Order Lines')
    date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sale Order'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', widget="statusbar")
    # track_visibility='onchange'
    currency_id = fields.Many2one('res.currency', string='Monnaie')

    # total general
    total = fields.Monetary(string='Total General', compute='_compute_total', currency_field='currency_id',
                            readonly=True)

    @api.depends('order_line_ids')
    def _compute_total(self):
        for rec in self:
            amount_total = 0
            if rec.order_line_ids:
                rec.state = 'sale'
                for line in rec.order_line_ids:
                    if line.price_subtotal:
                        amount_total += line.price_subtotal
                    else:
                        amount_total += amount_total
            rec.total = amount_total

    def MTR(self):
        MTR = 0
        for item in self.order_line_ids:
            MTR += 1
            item.SN = MTR
        return

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sale.order')
        res = super(SaleOrder, self).create(vals)
        res.MTR()
        return res

    def write(self, values):
        # print(values)
        # print("************ Print values here ************")
        res = super(SaleOrder, self).write(values)
        self.MTR()
        return res

    # def button_report_property(self):
    #     return self.env.ref('my_stock.custom_report_order').report_action(self)


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _description = 'Sale Order Line'
    _rec_name = 'order_id'

    SN = fields.Integer(string="MTR")
    order_id = fields.Many2one('sale.order', string="Order ID")
    ref_achat = fields.Char(string="Order ID", default=lambda self: str(uuid.uuid4()).split('-')[-1], required=True)
    product_id = fields.Many2one('produit.template', string='Product')
    description = fields.Text(related='product_id.description', string='Description', required=True)
    product_uom_qty = fields.Integer(string='Quantity', default=1.0)
    # product_uom = fields.Many2one('uom.uom', string='Unit of Measure', required=True)
    price_unit = fields.Integer(related='product_id.list_price', string='Unit Price', digits=(8, 4))
    currency_id = fields.Many2one('res.currency', string="Monnaie")
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_price_subtotal',
                                     currency_field="currency_id", store=True)

    # total_achat = fields.Integer(string='Total General', compute='_total_general')

    @api.depends('product_uom_qty', 'price_unit')
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.product_uom_qty * line.price_unit


# class OrderReport(models.AbstractModel):
#     _name = 'report.order_report.order_report_template'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         order = self.env['sale.order'].browse(docids)
#         order_lines = order.order_line_ids
#
#         lines_data = order_lines.mapped(lambda line: {
#             'SN': line.SN,
#             'ref_achat': line.ref_achat,
#             'product_id': line.product_id.name,
#             'description': line.product_id.description,
#             'quantity': line.product_uom_qty,
#             'price_unit': line.price_unit,
#             'currency_id': line.currency_id,
#             'subtotal': line.price_subtotal,
#         })
#
#         report_data = {
#             'order': order,
#             'lines_data': lines_data,
#         }
#
#         return {
#             'doc_ids': docids, # 'order_line_ids'
#             'doc_model': 'sale.order',
#             'data': data,
#             'docs': order,
#             'lines_data': lines_data,
#         }
