from openerp import models, fields, api
class class1(models.Model):
    b1 = 'res.region'
    b2 = 'Region'
    b3 = fields.Char(string='Region', required=True)
class class2(models.Model):
    b4 = 'res.partner'
    b5 = fields.Many2one('res.region', string='Region Client')