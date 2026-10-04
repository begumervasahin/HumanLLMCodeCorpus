import os
import sys
import uuid
import base64
from tornado import web
from tornado.options import options
from tornado.httpserver import HTTPServer
from raven.contrib.tornado import AsyncSentryClient
from lib import uimodules, uimethods
b1 = os.path.join(sys.path[0], 'static')
b2 = [
    (
        r'android\.ktvsky\.com',
        [
            (r'/(.*\.txt)', web.StaticFileHandler, {'path': b1}),
            (r'/store/code', 'handler.store.CodeHandler'),
            (r'/store/verify', 'handler.store.VerifyHandler'),
            (r'/store/signup', 'handler.store.SignupHandler'),
            (r'/store/login', 'handler.store.LoginHandler'),
            (r'/store/account', 'handler.store.AccountHandler'),
            (r'/store/logout', 'handler.store.LogoutHandler'),
            (r'/store/reset', 'handler.store.ResetHandler'),
            (r'/room/type', 'handler.room.TypeHandler'),
            (r'/room/ip', 'handler.room.IPHandler'),
            (r'/room/fee', 'handler.room.FeeHandler'),
            (r'/room/pack', 'handler.room.PackHandler'),
            (r'/pack', 'handler.pack.PackHandler'),
            (r'/pack/product', 'handler.pack.ProductHandler'),
            (r'/cate', 'handler.cate.CateHandler'),
            (r'/cate/product', 'handler.cate.CateProductHandler'),
            (r'/calc/time', 'handler.calc.ByTimeHandler'),
            (r'/calc/pack', 'handler.calc.ByPackHandler'),
            (r'/open/time', 'handler.open.ByTimeHandler'),
            (r'/open/pack', 'handler.open.ByPackHandler'),
            (r'/order/prepay', 'handler.order.PrepayHandler'),
            (r'/order/seq/time', 'handler.order.SeqTimeHandler'),
            (r'/order/seq/pack', 'handler.order.SeqPackHandler'),
            (r'/order/product', 'handler.order.ProductHandler'),
            (r'/order/back/product', 'handler.order.BackProductHandler'),
            (r'/order/detail', 'handler.order.DetailHandler'),
            (r'/order/checkout', 'handler.order.CheckoutHandler'),
            (r'/order/close', 'handler.order.CloseHandler'),
            (r'/order/write/of', 'handler.order.WriteOfHandler'),
            (r'/order/pay', 'handler.order.PayHandler'),
            (r'/order/repay', 'handler.order.RepayHandler'),
            (r'/order/bill', 'handler.order.BillHandler'),
            (r'/trade/stat/revenue', 'handler.trade.StatRevenueHandler'),
            (r'/trade/stat/product', 'handler.trade.StatProductHandler'),
            (r'/trade/stat/pack', 'handler.trade.StatPackHandler'),
            (r'/trade/order', 'handler.trade.OrderHandler'),
            (r'/trade/order/bill', 'handler.trade.OrderBillHandler'),
        ]
    ),
]
class class1(web.class1):
    def fonk1(self):
        b3 = {
            'xsrf_cookies': False,
            'compress_response': True,
            'debug': options.debug,
            'ui_modules': uimodules,
            'ui_methods': uimethods,
            'static_path': b1,
            'cookie_secret': base64.b64encode(uuid.uuid3(uuid.NAMESPACE_DNS, 'android').bytes),
            'sentry_url': (
                'https:
                if not options.debug else ''
            ),
        }
        super().fonk1([], **b3)
        for spec in b2:
            b4 = spec[0]
            b5 = spec[1]
            self.add_handlers(b4, b5)
def fonk2():
    b6 = class1()
    b6.b7 = AsyncSentryClient(b6.b3['sentry_url'])
    b8 = HTTPServer(b6, xheaders=True)
    b8.listen(options.port)
    print(f'Running on port {options.port}')
if b9 = = "__main__":
    fonk2()