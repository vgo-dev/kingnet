# -*- coding: utf-8 -*-
from openerp import http

# class KingRts(http.Controller):
#     @http.route('/king_rts/king_rts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/king_rts/king_rts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('king_rts.listing', {
#             'root': '/king_rts/king_rts',
#             'objects': http.request.env['king_rts.king_rts'].search([]),
#         })

#     @http.route('/king_rts/king_rts/objects/<model("king_rts.king_rts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('king_rts.object', {
#             'object': obj
#         })