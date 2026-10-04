from odoo import models, api, fields
class class1(models.TransientModel):
    b1 = 'extraschool.qrcodes_wizard'
    b2 = 'QR Codes Wizard'
    b3 = fields.Integer('Quantity to print')
    b4 = fields.Selection([
        ('qrcode', 'Qr Code'),
        ('b9', 'Logo')
    ], 'Print Type', b5 = True)
    b6 = fields.Integer('Last ID')
    b7 = fields.Char('File Name', size=16, readonly=True)
    b8 = fields.Boolean('Print QrCode value')
    b9 = fields.Binary('Logo')
    b10 = fields.Selection([
        ('extraschool.tpl_qrcodes_wizard_report', 'Standard'),
        ('extraschool.tpl_qrcodes_precut_wizard_report', 'Precut')
    ], 'Format', b5 = True, default='extraschool.tpl_qrcodes_wizard_report')
    b11 = fields.Selection([
        ('init', 'Init'),
        ('print_qrcodes', 'Print QRCodes')
    ], 'State', b5 = True, default='init')
    b12 = fields.Many2one('extraschool.qrconfig', string='QR Config')
    @api.multi
    def fonk1(self):
        b13 = self.env['ir.actions.b13']._get_report_from_name('extraschool.tpl_qrcodes_wizard_report')
        b14 = self.env['extraschool.mainsettings'].browse([1])
        self.b6 = b14.lastqrcodenbr + 1
        b14.lastqrcodenbr += self.b3
        b15 = {
            'ids': self.ids,
            'model': b13.model,
        }
        return {
            'type': 'ir.actions.b13',
            'report_name': self.b10,
            'b15': b15,
            'report_type': 'qweb-pdf',
        }
class class2(models.TransientModel):
    b1 = 'extraschool.qrconfig'
    b2 = 'QR Config'
    b7 = fields.Char('Name')
    b16 = fields.Char('Size of QR code b9', default='qrcode_img')
    b17 = fields.Char('Size of QR code b7', default='qr_child_name')