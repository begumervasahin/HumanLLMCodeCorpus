import json, httplib, time
b1 = {
	'Content-Type': 'application/json',
	'Ocp-Apim-Subscription-Key': 'b3f5d9f8d81046598dedc07a7541e2c9',
}
def fonk1(docs):
	b2 = { 'documents': [
		{
			'id': str(i),
			'text': docs[i],
		}
		for i in range(len(docs))
		if docs[i] != ""
	]}
	global b1
	b3 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	b3.request("POST", "/text/analytics/v2.0/sentiment", json.dumps(b2), b1)
	b4 = b3.getresponse()
	b5 = b4.read()
	b3.close()
	b6 = {'body': b2, 'result': json.loads(b5)}
	return b6
def fonk2(docs):
	b2 = {
		'stop_words': [],
		'topicsToExclude': [],
		'documents': [
			{
				'id': str(i),
				'text': docs[i],
			}
			for i in range(len(docs))
		],
	}
	b3 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	b3.request("POST", "/text/analytics/v2.0/topics", json.dumps(b2), b1)
	b4 = b3.getresponse()
	b7 = b4.getheader('operation-location')
	print(b4.getheaders())
	print(b7)
	b7 = b7[b7.index('.com') + 4 :]
	print(b7)
	b6 = {'body': b2}
	while True:
		time.sleep(5)
		b8 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		b8.request("GET", b7, '', b1)
		b4 = b8.getresponse()
		b5 = b4.read()
		b5 = json.loads(b5)
		if 'status' in b5:
			print(b5['status'])
			if b5['status'] == 'Succeeded':
				b6['result'] = b5
				break
		b8.close()
	b3.close()
	return b6