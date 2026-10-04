from openerp.osv import osv,fields
from openerp import api, models
from openerp import tools
class class1(osv.osv):
    b1 = 'res.ville'
    b2 = {
        'name': fields.char('ville'),
    }
class class2(osv.osv):
    b3 = 'res.partner'
    b2 = {
        'ville': fields.many2one('res.ville',u"Ville client"),
    }