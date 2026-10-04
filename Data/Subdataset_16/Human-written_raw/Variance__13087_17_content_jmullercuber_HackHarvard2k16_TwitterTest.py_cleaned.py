import json, httplib, urllib, string, base64, ast
b1 = 'kFxjNI3AlMiWGCVVIdg2mwLVf'
b2 = 'VbvyqLW2B0LB3BNCVZfJaSD7djvAbYuQgBvWnoz7oycoINqKoF'
a1 = 23424977
def fonk1(b1, b2):
    b3 = base64.b64encode(b1 + ':' + b2)
    b4 = {'Authorization': 'Basic ' + b3, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    b5 = httplib.HTTPSConnection('api.twitter.com')
    b5.request('POST', '/oauth2/token', 'b6 = client_credentials', b4)
    b7 = b5.getresponse()
    b8 = ast.literal_eval(b7.read())['access_token']
    return b8
def fonk2(b8, hashtag):
    b9 = '/1.1/search/tweets.json?q=%23' + hashtag + '&count=100'
    b4 = {'Authorization': 'Bearer ' + b8}
    b5 = httplib.HTTPSConnection('api.twitter.com')
    b5.request('GET', b9, '', b4)
    b7 = b5.getresponse().read()
    try:
        return json.loads( b7 )
    except:
        return {}
def fonk3(b8, woeid):
    b9 = '/1.1/b11/place.json?id=' + str(woeid)
    b4 = {'Authorization': 'Bearer ' + b8}
    b5 = httplib.HTTPSConnection('api.twitter.com')
    b5.request('GET', b9, '', b4)
    b7 = b5.getresponse().read()
    b10 = json.loads(b7)
    b11 = [
        (tag['name'], tag['query'], tag['tweet_volume'])
        for tag in b10[0]['b11']
    ]
    return b11
if b12 = = "__main__":
    b13 = fonk1(b1, b2)
    b11 = fonk3(b13, a1)
    print b11
    b14 = []
    for t in b11:
        print t
        print '\n'*22
        b15 = fonk2(b13, t[0])
        print b15
        try:
            json.loads( b15 )
        except:
            b14 += [t]
    print b14