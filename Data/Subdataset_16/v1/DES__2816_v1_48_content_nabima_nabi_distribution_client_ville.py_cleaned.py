from openerp import models, fields
class class1(models.Model):
    b1 = 'res.ville'
    b2 = 'Ville'
    b3 = fields.Char(string='Ville', required=True)
class class2(models.Model):
    b4 = 'res.partner'
    b5 = fields.Many2one('res.ville', string='Ville Client')