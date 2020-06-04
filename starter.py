import time
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'f0cado3e1692kn0nb3g0l6mvd6'
target = 'https://juice-shop.herokuapp.com/#/'
target1 = 'https://juice-shop.herokuapp.com.*'
excludeURL= '(?!https://juice-shop.herokuapp.com).*'


zap = ZAPv2(apikey=apiKey)
#Create new context 
zap.context.new_context(contextname='KaiTest')
zap.context.remove_context(contextname = 'Default Context')
#Exclude from Proxy
zap.core.exclude_from_proxy(excludeURL)
#Add include target to scope
zap.context.include_in_context('KaiTest',target1)
zap.context.set_context_in_scope('KaiTest', True)
#Change Mode
#Sets the mode, which may be one of [safe, protect, standard, attack]
zap.core.set_mode('protect')


print(zap.core.alerts_summary())
print(zap.core.alerts(start= 0, count = 3))
print(zap.core.alerts(start= 0, count = 3, riskid='risk'))  # What is the riskid here????

with open('report.html', 'w') as f:f.write(zap.core.htmlreport())


#May be ran a PScan/aScan
#Get the results
#Shutdown Once Finished
zap.core.shutdown()

# TODO : explore the app (Spider, etc) before using the Passive Scan API, Refer the explore section for details
# scanID = zap.spider.scan(target)

# while int(zap.pscan.records_to_scan) > 0:
#     # Loop until the passive scan has finished
#     print('Records to passive scan : ' + zap.pscan.records_to_scan)
#     time.sleep(2)

# print('Passive Scan completed')
# print('target:1122 {}'.format(target))

# # Print Passive scan results/alerts
# print('Hosts: {}'.format(', '.join(zap.core.hosts)))
# print('Alerts: ')
# pprint(zap.core.alerts())