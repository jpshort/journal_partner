# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

#import logging

#_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    journal_id = fields.Many2one('account.journal', string='Diario venta', domain="[('type', '=', 'sale')]")

class AccountInvoice(models.Model):
    _inherit = "account.invoice"


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        super(AccountInvoice, self)._onchange_partner_id()

        if self.partner_id:
            if self.type in ('out_invoice', 'out_refund'):
                self.journal_id = self.partner_id.journal_id.id

    @api.model
    def create(self, vals):

        res = super(AccountInvoice, self).create(vals)
        
        if res.partner_id.sale_fiscal_type:
            res.sale_fiscal_type = res.partner_id.sale_fiscal_type
		
        if res.partner_id.journal_id:
            res.journal_id = res.partner_id.journal_id

        return res				
        	           
        	           
