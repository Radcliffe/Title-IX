import requests
from bs4 import BeautifulSoup
import csv

url = "http://projects.chronicle.com/titleix/case/%s"
header = ('CaseNumber',
          'InstitutionName',
          'InstitutionURL',
          'DetailsURL',
          'DateOpened',
          'Status',
          'OpenFor',
          'DateResolved')
       
with open('federal_title_ix_investigations.txt', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for case_no in range(1, 251):
        r = requests.get(url % case_no)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'lxml')
        case_page = soup.select('.case-page')
        if case_page:
            case_page = case_page[0]
            institution_name = case_page.select('h3')[0].text
            institution_url = case_page.select('a')[1].text
            row = [case_no, institution_name, institution_url, url % case_no]
            row.extend(['NA']*4)            
            info_table = soup.select("div.info-table")[0]
            i = 4
            for case_row in info_table.select("div.case-row"):
                value = case_row.select('span.value')[0].text.replace(u'\xa0', '')
                row[i] = value
                i += 1
            writer.writerow(row)
            print (row)