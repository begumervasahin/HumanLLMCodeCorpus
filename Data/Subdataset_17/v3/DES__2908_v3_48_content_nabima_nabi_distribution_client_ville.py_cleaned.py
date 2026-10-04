from openerp import models, fields
class ResVille(models.Model):
    _name = 'res.ville'
    _description = 'City'
    name = fields.Char(string='City', required=True)
class ResPartner(models.Model):
    _inherit = 'res.partner'
    ville_id = fields.Many2one('res.ville', string='City Client')