from datetime import datetime
import timeago

class WeWorkParser:
    def __init__(self):
        pass
    
    def ParseResult(self, result):
        jobList = self.ExtractJobList(result)
        retval = self.ParseJobList(jobList)
        return retval
    
    def ExtractJobList(self, document):
        idx = document.find('id=job_list') + len('id=job_list')
        fin = document.find('<footer', idx)
        return document[idx:fin]
    
    def ParseJobList(self, jobList):
        retval = []
        idx = jobList.find('<li class=feature')
        while idx >= 0:
            idx = jobList.find('a href="/remote-jobs', idx)
            fin = jobList.find('</li>', idx)
            retval.append(self.ParseJob(jobList[idx:fin]))
            idx = jobList.find('<li class=feature', idx)

        return retval
    
    def ParseJob(self, job):
        idx = job.find('a href="') + len ('a href="')
        fin = job.find('">', idx)
        link = job[idx:fin]

        idx = job.find('class=company>', idx) + len('class=company>')
        fin = job.find('</span', idx)
        company = job[idx:fin]

        idx = job.find('class=title>', idx) + len('class=title>')
        fin = job.find('</span', idx)
        title = job[idx:fin]

        idx = job.find('datetime="', idx) + len('datetime="')
        if idx > 0:
            fin = job.find('"', idx)
            date = job[idx:fin][:10]
            try:
                time = timeago.format(date, datetime.now())
            except:
                time = ''
        else:
            time = ''

        return {'title': title, 'link': link, 'company': company, 'time': time, 'tags': [], 'salary': ''}
