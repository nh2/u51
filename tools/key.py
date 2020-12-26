import errno
import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

def get_generate_secret_key(root, key_file_name='secrets/secret.key'):
	key_path = os.path.join(root, key_file_name)
	try:
		return Path(key_path).read_text().strip()
	except IOError as ioe:
		if ioe.errno not in [errno.ENOENT]:
			raise
		secret_key = get_random_secret_key()
		try:
			Path(key_path).write_text(secret_key)
		except IOError as e:
			detail_exception = Exception('Could not generate a secret key file in %s. Please create it manually!' % key_path)
			raise detail_exception from e
		return secret_key
