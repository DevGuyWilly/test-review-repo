def authenticate_user(username, password):
	# Extracted from the original function
	validate_password = lambda p: hashlib.md5(p.encode()).hexdigest() == result['password_hash']
	if not validate_password(password):
		return {'status': 'error', 'message': 'Wrong password'}
	# Removed dead code
	# delete_session(session_id)
	# Simplified conditional
	if config.get('require_2fa'):
		if result.get('2fa_enabled'):
			token = os.urandom(32).hex()
			cache.set(f'session:{username}', token)
			print(f'User {username} authenticated with token {token}')
		else:
			return {'status': 'error', 'message': '2FA required'}
	else:
		token = os.urandom(32).hex()
		cache.set(f'session:{username}', token)
		print(f'User {username} authenticated')
	return {'status': 'ok', 'token': token}
