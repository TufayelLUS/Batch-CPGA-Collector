import urllib, httplib
allData = {}
def getResult(std_id):
    data = urllib.urlencode({'action': 'get-result', 'student_id':str(std_id), 'birth_date':''})
    h = httplib.HTTPSConnection('www.lus.ac.bd')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    h.request('POST', '/wp-admin/admin-ajax.php', data, headers)
    r = h.getresponse()
    info = r.read()
    if info.split('success":')[1].split(',')[0] == 'false':
        return
    name = info.split('name":"')[1].split('"')[0]
    sid = info.split('id":"')[1].split('"')[0]
    cgpa = info.split('cgpa":')[1].split(',')[0]
    credit = info.split('credit":')[1].split(',')[0]
    grade = info.split('grade":"')[1].split('"')[0]
    #print name, sid, cgpa, credit, grade
    print 'Student:', name
    print 'ID:', sid
    print 'CGPA:', cgpa + ' (' + grade + ')'
    print 'Credits Completed:', credit

stdId = 1622020001
for i in range(stdId, 1622020035):
    getResult(i)
input('Press enter to exit ...')
