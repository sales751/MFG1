from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vehicle_number = fields.Char(string="Vehicle Number")
    driver_name = fields.Char(string="Driver Name")
    driver_license = fields.Binary(string="Driver License")
    vehicle_puc = fields.Binary(string="Vehicle PUC")
    iso_verified = fields.Boolean(string="ISO Verified")
    gate_entry_time = fields.Datetime(string="Gate Entry Time")