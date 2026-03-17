# from odoo import http


# class ManufacturingCustom(http.Controller):
#     @http.route('/manufacturing_custom/manufacturing_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufacturing_custom/manufacturing_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufacturing_custom.listing', {
#             'root': '/manufacturing_custom/manufacturing_custom',
#             'objects': http.request.env['manufacturing_custom.manufacturing_custom'].search([]),
#         })

#     @http.route('/manufacturing_custom/manufacturing_custom/objects/<model("manufacturing_custom.manufacturing_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufacturing_custom.object', {
#             'object': obj
#         })

