import pymongo, csv
b1 = pymongo.MongoClient()
b2 = b1["projectOne"]
b3 = b2["Users"]
b4 = b2["Organizations"]
b5 = b2["Interests"]
b6 = b2["Projects"]
b7 = b2["Skill"]
def fonk1():
    b1 = pymongo.MongoClient()
    b2 = b1["projectOne"]
    b8 = b2["Users"]
    b4 = b2["Organizations"]
    b5 = b2["Interests"]
    b6 = b2["Projects"]
    b9 = b2["Skill"]
    while True:
        b10 = raw_input("\nWould you like to search for a b8 (y/n):  ")
        if b10 = = 'y':
            fonk2(b8, b4, b5, b9, b6)
        else:
            break
def fonk2(userID):
    if((b3.find({"User_id": str(userID)})).count() == 0):
        print "This b8 does not exist. Please try another userID."
    else:
        b11 = b3.find({"User_id": str(userID)})
        b12 = b4.find({"User_id": str(userID)})
        b13 = b5.find({"User_id": str(userID)})
        b14 = b7.find({"User_id": str(userID)})
        b15 = b6.find({"User_id": str(userID)})
        for u in b11:
            print("\tName: %s %s" %(u['First name'], u['First name']))
        for o in b12:
            print("\tWorks at: %s" %o["organization"])
        b16 = ""
	for i in b13:
		if isinstance(i["Interest"], list):
			for items in range(len(i["Interest"])):
				b16+= i["Interest"][items] + "(" + i["Interest level"][items] + "),"
		else:
			b16 = i["Interest"] + "(" + i["Interest level"] + ")"
	print("\tInterest: %s" %b16)
	b17 = ""
	for sk in b14:
		if isinstance(sk["Skill"], list):
		 	for items in range(len(sk["Skill"])):
		 		b17 += sk["Skill"][items] + "(" + sk["Skill level"][items] + "), "
		else:
			b17 = sk["Skill"] + "(" + sk["Skill level"] + ")"
	print("\tSkill: %s" %b17)
	b18 = ""
	for p in b15:
		if isinstance(p["Project"], list):
		 	for items in range(len(p["Project"])):
		 		b18 += p["Project"][items] + ", "
		else:
			b18 = p["Project"]
	print("\tWorks on: %s" %b18)
def fonk3(file_name):
    b19 = open(file_name)
    b20 = csv.reader(b19)
    b21 = next(b20)
    b22 = []
    b23 = {}
    a1 = 0
    b24 = []
    for key in b21:
        b22.append(key)
    a1 = len(b22)
    for rows in b20:
        for i in range(a1):
            b23[b22[i]] = rows[i]
        b24.append(b23)
        b23 = {}
    b19.close()
    return b24
def fonk4(collection_name, entries):
    print entries
    collection_name.create_index("User_id", b25 = True)
    for b26 in entries:
        collection_name.insert_one(b26)
def fonk5(csvfiles):
    fonk8(b3,fonk3(csvfiles[0]))
    fonk8(b4,fonk3(csvfiles[1]))
    fonk8(b6,fonk6(csvfiles[2],"project"))
    fonk8(b5,fonk6(csvfiles[3],"interest"))
    fonk8(b7,fonk6(csvfiles[4],"b9"))
def fonk6(file_name, b27):
	b19 = open(file_name, "r")
	b20 = csv.reader(b19)
	b21 = next(b20)
	b22 = b21
	b24 = []
	b5.create_index([("User_id", pymongo.ASCENDING), ("interest", pymongo.DESCENDING)], b25 = True)
	b7.create_index([("User_id", pymongo.ASCENDING), ("b9", pymongo.DESCENDING)], b25 = True)
	for rows in b20:
		b26 = {}
		for column in range(len(rows)):
			b26[b22[column]] = rows[column]
		if fonk7(b26, b24, b27):
			b24.append(b26)
	b19.close()
	return b24
def fonk7(info, arr, b27):
	if b27 = = "interest":
		for elements in arr:
			if elements["User_id"] == info["User_id"]:
				if not isinstance(elements["Interest"], list):
					elements["Interest"] = [elements["Interest"], info["Interest"]]
					elements["Interest level"] = [elements["Interest level"], info["Interest level"]]
				else:
					if info["Interest"] not in elements["Interest"]:
						elements["Interest"].append(info["Interest"])
						elements["Interest level"].append(info["Interest level"])
				return False
		return True
	elif b27 = = "b9":
		for elements in arr:
			if elements["User_id"] == info["User_id"]:
				if not isinstance(elements["Skill"], list):
					elements["Skill"] = [elements["Skill"], info["Skill"]]
					elements["Skill level"] = [elements["Skill level"], info["Skill level"]]
				else:
					if info["Skill"] not in elements['Skill']:
						elements["Skill"].append(info["Skill"])
						elements["Skill level"].append(info["Skill level"])
				return False
		return True
	elif b27 = = "project":
		for elements in arr:
			if elements["User_id"] == info["User_id"]:
				if not isinstance(elements["Project"], list):
					elements["Project"] = [elements["Project"], info["Project"]]
				else:
					if info["Project"] not in elements['Project']:
						elements["Project"].append(info["Project"])
				return False
		return True
def fonk8(collection_name, entries):
	if collection_name != b7 or collection_name != b5:
		collection_name.create_index("User_id", b25 = True)
	for b26 in entries:
		try:
			collection_name.insert_one(b26)
		except:
                    print b26
                    pass
def fonk9():
    b1.drop_database("projectOne")