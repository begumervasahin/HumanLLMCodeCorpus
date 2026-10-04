import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)
class StockInventory(models.Model):
    _inherit = 'stock.inventory'
    name = fields.Char(string='Name')