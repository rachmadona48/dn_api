# -*- coding: utf-8 -*-
from odoo import http

# class DnApi(http.Controller):
#     @http.route('/dn_api/dn_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dn_api/dn_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dn_api.listing', {
#             'root': '/dn_api/dn_api',
#             'objects': http.request.env['dn_api.dn_api'].search([]),
#         })

#     @http.route('/dn_api/dn_api/objects/<model("dn_api.dn_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dn_api.object', {
#             'object': obj
#         })