from openerp.osv import osv, fields
from openerp import models
class ResRegion(osv.osv):
    _name = 'res.region'
    _columns = {
        'name': fields.char('Region'),
    }
class ResPartner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
        'region': fields.many2one('res.region', string='Region Client'),
    }