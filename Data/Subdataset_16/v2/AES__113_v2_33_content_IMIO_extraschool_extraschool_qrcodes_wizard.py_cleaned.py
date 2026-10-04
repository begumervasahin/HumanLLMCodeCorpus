from odoo import models, api, fields
class class1(models.TransientModel):
    b1 = 'extraschool.qrcodes_wizard'
    b2 = 'QR Codes Wizard'
    b3 = fields.Integer(b5='Quantity to Print')
    b4 = fields.Selection(
        [
            ('qrcode', 'QR Code'),
            ('b10', 'Logo')
        ],
        b5 = 'Print Type',
        b6 = True
    )
    b7 = fields.Integer(b5='Last ID')
    b8 = fields.Char(b5='File Name', size=16, readonly=True)
    b9 = fields.Boolean(b5='Print QR Code Value')
    b10 = fields.Binary(b5='Logo')
    b11 = fields.Selection(
        [
            ('extraschool.tpl_qrcodes_wizard_report', 'Standard'),
            ('extraschool.tpl_qrcodes_precut_wizard_report', 'Precut')
        ],
        b5 = 'Format',
        b6 = True,
        b12 = 'extraschool.tpl_qrcodes_wizard_report'
    )
    b13 = fields.Selection(
        [
            ('init', 'Init'),
            ('print_qrcodes', 'Print QR Codes')
        ],
        b5 = 'State',
        b6 = True,
        b12 = 'init'
    )
    b14 = fields.Many2one('extraschool.qrconfig', b5='QR Config')
    @api.multi
    def fonk1(self):
        b15 = self.env['ir.actions.b15']._get_report_from_name('extraschool.tpl_qrcodes_wizard_report')
        b16 = self.env['extraschool.mainsettings'].browse([1])
        self.b7 = b16.lastqrcodenbr + 1
        b16.lastqrcodenbr += self.b3
        b17 = {
            'ids': self.ids,
            'model': b15.model,
        }
        return {
            'type': 'ir.actions.b15',
            'report_name': self.b11,
            'b17': b17,
            'report_type': 'qweb-pdf',
        }
class class2(models.TransientModel):
    b1 = 'extraschool.qrconfig'
    b2 = 'QR Config'
    b8 = fields.Char(b5='Name')
    b18 = fields.Char(b5='Size of QR Code Logo', b12='qrcode_img')
    b19 = fields.Char(b5='Size of QR Code Name', b12='qr_child_name')