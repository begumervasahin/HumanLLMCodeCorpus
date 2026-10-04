from openerp.osv import osv,fields
from openerp import api, models
from openerp import tools
class class1(osv.osv):
    b1 = 'res.region'
    b2 = {
        'name': fields.char('region'),
    }
class class2(osv.osv):
    b3 = 'res.partner'
    b2 = {
        'region': fields.many2one('res.region',u"Region client"),
    }