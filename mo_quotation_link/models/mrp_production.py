from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_order_id = fields.Many2one(
        'sale.order',
        string="Linked Quotation",
        tracking=True,
    )

    sale_order_partner = fields.Many2one(
        'res.partner',
        string="Customer",
        related='sale_order_id.partner_id',
        store=False,
    )

    sale_order_amount = fields.Monetary(
        string="Quotation Amount",
        related='sale_order_id.amount_total',
        currency_field='sale_currency_id',
        store=False,
    )

    sale_currency_id = fields.Many2one(
        'res.currency',
        related='sale_order_id.currency_id',
        store=False,
    )

    sale_order_state = fields.Selection(
        related='sale_order_id.state',
        string="Quotation Status",
        store=False,
    )