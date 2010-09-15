import os

def get_generate_secret_key(root, key_file_name='secret.key', length=50):
	key_path = os.path.join(root, key_file_name)
	try:
	    return open(key_path).read().strip()
	except IOError:
	    try:
	        from random import choice
	        secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(length)])
	        key_file = file(key_path, 'w')
	        key_file.write(secret_key)
	        key_file.close()
	    except IOError:
	        Exception('Could not generate a secret key file in %s. Please create it manually!' % key_path)
