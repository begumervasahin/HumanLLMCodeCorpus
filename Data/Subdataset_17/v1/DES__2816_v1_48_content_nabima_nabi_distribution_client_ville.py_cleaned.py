from openerp import models, fields
class ResVille(models.Model):
    _name = 'res.ville'
    _description = 'Ville'
    name = fields.Char(string='Ville', required=True)
class ResPartner(models.Model):
    _inherit = 'res.partner'
    ville_id = fields.Many2one('res.ville', string='Ville Client')