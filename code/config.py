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

print 'First View Name'
view1 = raw_input()
f.write('view1name=\'' + view1name + '\'\n')

print 'View1 ID (ex. number at end of URL')
view1 = raw_input()
f.write('view1=\'' + view1 + '\'\n')

print 'First View Name'
view1 = raw_input()
f.write('view2name=\'' + view2name + '\'\n')

print 'View2 ID (ex. number at end of URL')
view1 = raw_input()
f.write('view2=\'' + view2 + '\'\n')
