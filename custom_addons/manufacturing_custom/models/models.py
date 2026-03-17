# from odoo import models, fields, api


# class manufacturing_custom(models.Model):
#     _name = 'manufacturing_custom.manufacturing_custom'
#     _description = 'manufacturing_custom.manufacturing_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

