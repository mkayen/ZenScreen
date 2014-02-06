from zendesk import Zendesk, get_id_from_url
import config1

zendesk = Zendesk(config1.zendesksite, config1.email, config1.password)

pending = zendesk.list_tickets(view_id=config1.view1)
new = zendesk.list_tickets(view_id=config1.view2)

print config1.view1name
print "--------------------------------------"

for items in pending:
	requester = items['req_name']	
	ticket = items['nice_id']
	date = items['status_updated_at']
	assignee = items['assignee_name']
	print ticket, ' | ', date, ' | ', requester, ' | ', assignee 

print "--------------------------------------"
print config1.view2name
print "--------------------------------------"

for items in new:
	requester = items['req_name']	
	ticket = items['nice_id']
	date = items['status_updated_at']
	print ticket, ' | ', date, ' | ', requester
