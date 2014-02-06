print 'Use Your Zendesk Credentials to set up your config file.'

print 'Zendesk site name (ex. the xyz in https://xyz.zendesk.com)'
zendesksite = raw_input()
f = open('config1.py','w')
f.write('zendesksite=\'' + 'https://' + zendesksite + '.zendesk.com' + '\'\n')

print 'Email address (ex. john.doe@smith.com)'
email = raw_input()
f.write('email=\'' + email + '\'\n')

print 'Zendesk password'
password = raw_input()
f.write('password=\'' + password + '\'\n')

