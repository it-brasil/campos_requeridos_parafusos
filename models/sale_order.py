# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fiscal_position_id = fields.Many2one('account.fiscal.position', required=True, oldname='fiscal_position', string='Fiscal Position', readonly=True)