class StackOverflowParser:
    def __init__(self):
        self.jobs_footer = '<div class="jobsfooter'
        self.list_results = '<div class="listResults"'
        self.job_tag = '-item -job'
        self.company_tag = '-company'
    
    def ParseResult(self, result):
        result = self.ExtractJobList(result)
        retval = []

        jobsNo = result.count(self.job_tag)
        index = result.find(self.job_tag)
        for i in range(jobsNo):
            retval.append(self.ParseJobElement(result, index))
            index = result.find(self.job_tag, index + 1)
        return retval

    def ExtractJobList(self, result):
        result = result.replace('\r\n', '')
        result = result.replace('    ', '')
        head = result.find(self.list_results)
        tail = result.find(self.jobs_footer)
        return result[head : tail]
    
    def ParseJobElement(self, result, index):
        idx = index
        idx = result.find('job-details', idx)
        idx = result.find('a href="', idx) + len('a href="')
        endLink = result.find('"', idx)
        link = result[idx : endLink]
        link = 'https://stackoverflow.com' + link

        title = result.find('title="', idx) + len('title="')
        endTitle = result.find('"', title)
        jobTitle = result[title : endTitle]

        idx = result.find('<span class="', endTitle)
        idx = result.find('">', idx) + len('">')
        endTime = result.find('</span', idx)
        jobTime = result[idx : endTime]

        idx = result.find(self.company_tag, endTime)
        idx = result.find('<span>', idx) + len('<span>')
        endCompany = result.find('</span', idx)
        company = result[idx : endCompany]

        idx = result.find('-perks', idx)
        endPerks = result.find('</div', idx)
        perkTxt = result[idx : endPerks]
        salary = ''
        if '-salary' in perkTxt:
            spx = perkTxt.find('-salary')
            spx = perkTxt.find('">', spx) + len('">')
            endSalary = perkTxt.find('</span')
            salary = perkTxt[spx : endSalary]

        idx = result.find('-tags', idx)
        endTags = result.find('</div', idx)
        tagTxt = result[idx : endTags]
        tagCount = tagTxt.count('post-tag')
        tags = []
        tgx = 0
        for i in range(tagCount):
            tgx = tagTxt.find('post-tag', tgx)
            tgx = tagTxt.find('">', tgx) + len('">')
            endTag = tagTxt.find('</a', tgx)
            tags.append(tagTxt[tgx : endTag])

        return {'title': jobTitle, 'time': jobTime, 'company': company, 'link': link, 'tags': tags, 'salary': salary}
