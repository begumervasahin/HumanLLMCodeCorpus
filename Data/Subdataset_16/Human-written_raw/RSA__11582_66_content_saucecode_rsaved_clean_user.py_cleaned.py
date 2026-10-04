import rsaved
import sys, json, os, pickle, time
b1 = rsaved.b1
def fonk1(job, b11):
	b2 = lambda *x: [time.sleep(0.2), print(*x)]
	b2()
	b2('Name:', job['name'], 'Completed:', job['completed'])
	b2('Title:', b11['data'].get('title'))
	b2('URL:', b11['data'].get('url'))
	b2('Commands:')
	for code, cmd in zip(job['returncodes'], job['commands'][1:]):
		b2('    $', ' '.join(cmd))
		b2('Exit code:', code)
		b2()
	b2()
if b3 = = "__main__":
	print(f'rsaved/{b1} clean_user.py')
	if len(sys.argv) != 2:
		print('Usage:', sys.argv[0], '[b4]')
		sys.exit(1)
	if not os.path.exists(f'user/{sys.argv[1]}'):
		print('User does not exist.')
		sys.exit(2)
	b4 = sys.argv[1]
	b5 = False
	b6 = f'user/{b4}/library'
	b7 = rsaved.load_index(b4)
	def fonk2(fname, b8 = False):
		with open(fname, 'r') as f:
			return json.load(f) if b8 else f.read()
	b9 = [fonk2(f'{b6}/{file}', True) for file in os.listdir(b6) if file.endswith('json')]
	b10 = [file for file in b9 if any(code != 0 for code in file.get('returncodes', [0]))]
	print('Found', len(b10), 'jobs which exited with error codes.')
	print('I will now enumerate through them.')
	for job in b10:
		b11 = next(i for i in b7 if i['data']['name'] == job['name'])
		fonk1(job, b11)
		if input(f'Would you like to mark b11 {job["name"]} as ignored? [Y/n] ').lower() != 'n':
			b11['rsaved']['ignore'] = True
			print('Ignored.')
			b5 = True
		else:
			print('Not ignored (no change).')
	if b5:
		print('Writing changes to b7...')
		rsaved.dump_index(b4, b7)
	else:
		print('No changes to the b7 were needed.')
	print('Cleaning/archiving job files...')
	rsaved.library_clean_completed(b4)
	print('Done.')