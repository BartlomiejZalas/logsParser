from FileLogParser import FileLogParser

print('Parser starts... please wait...')

logs = FileLogParser().parseFile('sesja.log')

print('File parsed')



print('***************************')
print("Requests from " + logs[0].date_time.strftime('%d/%b/%Y') + " to " + logs[len(logs)-1].date_time.strftime('%d/%b/%Y') + ':')
print(str(len(logs)) + ' requests')



print('***************************')
print("404 Errors in January 2016:")
counter = 0
for log in logs:
    if (log.date_time.month == 1 and log.date_time.year == 2016 and log.response_code == 404):
        counter = counter +1

print(str(counter) + " 404 errors")
print('***************************')