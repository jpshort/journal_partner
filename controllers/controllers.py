# -*- coding: utf-8 -*-
from odoo import http

# class journal_partner(http.Controller):
#     @http.route('/journal_partner/journal_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/journal_partner/journal_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('journal_partner.listing', {
#             'root': '/journal_partner/journal_partner',
#             'objects': http.request.env['journal_partner.journal_partner'].search([]),
#         })

#     @http.route('/journal_partner/journal_partner/objects/<model("journal_partner.journal_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('journal_partner.object', {
#             'object': obj
#         })