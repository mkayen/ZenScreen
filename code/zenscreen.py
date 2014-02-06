from zendesk import Zendesk, get_id_from_url
import config1

zendesk = Zendesk(config1.zendesksite, config1.email, config1.password)

pending = zendesk.list_tickets(view_id=29012404)
new = zendesk.list_tickets(view_id=30131640)

print "ETP Pending Tickets"
print "(ticket #, date, requester id)"
print "--------------------------------------"

for items in pending:
	requester = items['req_name']	
	ticket = items['nice_id']
	date = items['status_updated_at']
	assignee = items['assignee_name']
	print ticket, ' | ', date, ' | ', requester, ' | ', assignee 

print "--------------------------------------"
print "New Tickets"
print "(ticket #, date, requester id)"
print "--------------------------------------"

for items in new:
	requester = items['req_name']	
	ticket = items['nice_id']
	date = items['status_updated_at']
	print ticket, ' | ', date, ' | ', requester
