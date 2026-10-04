from openerp import models, api, fields
from openerp.api import Environment
import cStringIO
import base64
import os
class class1(models.TransientModel):
    b1 = 'extraschool.qrcodes_wizard'
    b2 = fields.Integer('Quantity to print')
    b3 = fields.Selection((('qrcode','Qr Code'),('b7','Logo'),),'Print Type', b9=True)
    b4 = fields.Integer('Last id')
    b5 = fields.Char('File Name', size=16, readonly=True)
    b6 = fields.Boolean('Print QrCode value')
    b7 = fields.Binary()
    b8 = fields.Selection([('extraschool.tpl_qrcodes_wizard_report', 'Standard'),
                             ('extraschool.tpl_qrcodes_precut_wizard_report', 'Precut')],
                            'Format', b9 = True, default='extraschool.tpl_qrcodes_wizard_report'
                            )
    b10 = fields.Selection([('init', 'Init'),
                             ('print_qrcodes', 'Print QRCodes')],
                            'State', b9 = True, default='init'
                            )
    b11 = fields.Many2one('extraschool.qrconfig', string='QR Config')
    @api.multi
    def fonk1(self):
        b12 = self.env['b12']._get_report_from_name('extraschool.tpl_qrcodes_wizard_report')
        b13 = self.env['extraschool.mainsettings'].browse([1])
        self.b4 = b13.b14 + 1
        b13.b14 = b13.b14 + self.b2
        b15 = {
        'ids': self.ids,
        'model': b12.model,
        }
        return {
               'type': 'ir.actions.b12.xml',
               'report_name': self.b8,
               'b15': b15,
               'report_type': 'qweb-pdf',
           }
class class2(models.TransientModel):
    b1 = 'extraschool.qrconfig'
    b5 = fields.Char('Name')
    b16 = fields.Char('Size of QR code b7', default="qrcode_img")
    b17 = fields.Char('Size of QR code b5', default='qr_child_name')