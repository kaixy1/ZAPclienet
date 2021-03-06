import time
from pprint import pprint
from zapv2 import ZAPv2
import subprocess
from config import*

apiKey = APIKEY
target = 'https://juice-shop.herokuapp.com/#/'
targetRegex = 'https://juice-shop.herokuapp.com.*'
excludeURL= '(?!https://juice-shop.herokuapp.com).*'

#start Burp
#subprocess.call(r'C:\Program Files\OWASP\Zed Attack Proxy\zap.bat)

#Change browser proxy setting
time.sleep(20)


zap = ZAPv2(apikey=apiKey)
#Create new context 
zap.context.new_context(contextname='KaiTest')
zap.context.remove_context(contextname = 'Default Context')
#Exclude from Proxy
zap.core.exclude_from_proxy(excludeURL)
#Add include target to scope
zap.context.include_in_context('KaiTest',targetRegex)
zap.context.set_context_in_scope('KaiTest', True)

#Sets the mode, which may be one of [safe, protect, standard, attack]
zap.core.set_mode('protect')
#?Wait till Functional test is done
#?Run a PScan/aScan


###Results 
summaryalert = zap.core.alerts_summary()
print(summaryalert['Medium'])

#print(zap.core.alerts(start= 0, count = summaryalert['Medium'], riskid='2')) # riskid = Severity

#Get all Medium risk into a file
with open('alerts1.txt','w') as f:
    for listitem in zap.core.alerts(start= 0, count = summaryalert['Medium'], riskid='2'):
        f.write('%s\n' % listitem)
#Create a Report 
with open('report.html', 'w') as f:f.write(zap.core.htmlreport())


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