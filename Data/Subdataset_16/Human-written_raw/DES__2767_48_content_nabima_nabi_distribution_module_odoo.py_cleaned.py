from openerp.osv import fields, osv
from openerp.tools import float_compare, float_round
from openerp.tools.translate import _
from openerp import SUPERUSER_ID, api
import logging
b1 = logging.getLogger(__name__)
class class1(osv.osv):
    b2 = "stock.inventory"
    b3 = {
        '': fields.char("name"),
    }