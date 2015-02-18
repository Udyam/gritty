'''
	Hashing utility functions
'''
import base64 

def gen_hash(username,event_name):
	val = 0
	HASH_BASE = 37
	string = username + event_name
	for a in string:
		val = val*HASH_BASE + ord(a)
	return base64.b64encode(str(val))
