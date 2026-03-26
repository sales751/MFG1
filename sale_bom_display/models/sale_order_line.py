from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    bom_component_ids = fields.Many2many(
    'mrp.bom.line',
    string="BoM Lines",        # ← "BoM Components" se badla
    compute='_compute_bom_lines',
    store=False,
    )

    bom_components_text = fields.Char(
        string="BoM Summary",      # ← "BoM Components" se badla
        compute='_compute_bom_components_text',
        store=False,
    )

    @api.depends('product_id')
    def _compute_bom_lines(self):
        for line in self:
            if not line.product_id:
                line.bom_component_ids = [(5, 0, 0)]
                continue

            bom = self.env['mrp.bom'].search([
                '|',
                ('product_id', '=', line.product_id.id),
                ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id),
            ], limit=1)

            if bom:
                line.bom_component_ids = [(6, 0, bom.bom_line_ids.ids)]
            else:
                line.bom_component_ids = [(5, 0, 0)]

    @api.depends('product_id')
    def _compute_bom_components_text(self):
        for line in self:
            if not line.product_id:
                line.bom_components_text = 'No BoM'
                continue

            bom = self.env['mrp.bom'].search([
                '|',
                ('product_id', '=', line.product_id.id),
                ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id),
            ], limit=1)

            if bom and bom.bom_line_ids:
                parts = []
                for comp in bom.bom_line_ids:
                    parts.append(f"{comp.product_id.name} x{comp.product_qty}")
                line.bom_components_text = ' | '.join(parts)
            else:
                line.bom_components_text = 'No BoM found'