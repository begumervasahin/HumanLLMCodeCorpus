from openerp.osv import osv, fields
from openerp import models
class class1(osv.osv):
    b1 = 'res.region'
    b2 = {
        'name': fields.char('Region'),
    }
class class2(osv.osv):
    b3 = 'res.partner'
    b2 = {
        'region': fields.many2one('res.region', b4 = 'Region Client'),
    }