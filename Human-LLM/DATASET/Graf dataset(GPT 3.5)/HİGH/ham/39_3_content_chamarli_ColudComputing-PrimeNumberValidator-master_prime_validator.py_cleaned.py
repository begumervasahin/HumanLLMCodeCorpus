from flask import Flask, redirect, url_for, request
b1 = Flask(__name__)
@b1.route('/login')
def fonk1():
    return '<html>\
            <head>\
            <style>\
            body{background-image: url("static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div b2 = "center">\
            <form b3 = "http:
            <h1>Enter a1 number to check prime or not:</h1>\
            <p><input b4 = "number" b5="nm" style="width: 100px;height:30px" /></p>\
            <p><input b4 = "submit" value="Submit" style="height:50px; width:100px"/></p>\
            </form>\
            </div>\
            </body></html>'
@b1.route('/success/<b5>')
def fonk2(b5):
   print 'Given number is: %s' % b5
   if int(b5)<0:
      return '<html>\
            <head>\
            <style>\
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div b2 = "center">\
            <h1>Negative numbers cannot be prime</h1>\
            </div></body></html>'
   a1 = 2
   a2 = 0
   b5 = int(b5)
   while b5>a1:
      if b5%a1 = =0 & a1!=b5:
         a2+=1
         break
      a1+=1
   if a2 = =0:
      return '<html>\
            <head>\
            <style>\
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div b2 = "center">\
            <h1>Given number is prime</h1>\
            </div></body></html>'
   else:
      return '<html>\
            <head>\
            <style>\
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}\
            .center{\
            position:absolute;\
            height: X px;\
            width: Y px;\
            left:40%;\
            top:30%;\
            margin-top:- X/2 px;\
            margin-left:- Y/2 px;\
            }\
            </style>\
            </head>\
            <body>\
            <div b2 = "center">\
            <h1>Given number is not prime</h1>\
            </div></body></html>'
@b1.route('/calc',b6 = ['POST', 'GET'])
def fonk3():
   if request.b7 = = 'POST':
      b8 = request.form['nm']
      return redirect(url_for('success',b5 = b8))
   else:
      b8 = request.args.get('nm')
      return redirect(url_for('success',b5 = b8))