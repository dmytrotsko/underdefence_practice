import sys
from bs4 import BeautifulSoup
import requests
import re
from prettytable import PrettyTable


def output_table_1(table):
    table_th = []
    table_td = []
    result_th = []
    result_td = []
    temp = []
    result_table = PrettyTable(['CVSS Scores &', 'Vulnerability Types' ])
    for row in table.findAll('tr'):
        for td in row.findAll('td'):
            temp.append(td.text)
        for th in row.findAll('th'):
            table_th.append(th.text)
        for td in row.findAll('td'):
            for span in td.findAll('span'):
                table_td.append(span.text)
            for div in td.findAll('div'):
                table_td.append(div.text)
    reg_exp = r'\([^\)]+\)'
    for k in table_th:
        string = re.sub(reg_exp, '', k)
        if len(string) != 0:
            result_th.append(k)
    print('\n\n')
    for v in table_td:
        string = re.sub(reg_exp, '', v)
        if len(string) != 0:
            result_td.append(v)
    result_td[-2] = result_td[-2] + ', ' + result_td[-1]
    result_td[-1] = temp[-1]

    i = 0
    while i < len(result_th):
        result_table.add_row([str(result_th[i]), str(result_td[i])])
        i += 1
    print(result_table)


def output_table_2(table):
    table_th = []
    table_td = []
    for row in table.findAll("tr"):
        for th in table.findAll("th"):
            if len(th) == 0:
                th = 'Empty string'
                table_th.append(th)
            else:
                table_th.append(th.text)
        for td in row.findAll("td"):
            table_td.append(td.text.replace("\t", ""))
    i = 0
    while i < len(table_td):
        print(table_th[i] + " :" + table_td[i].replace('\n', ' '))
        i += 1


def parse(*cve_id):
    for cveID in cve_id:
        target_page_request = requests.get('https://www.cvedetails.com/cve/' + cveID + '/')
        soup = BeautifulSoup(target_page_request.content, 'html.parser')
        table1 = soup.find('table', attrs={'id': 'cvssscorestable'})
        table2 = soup.find('table', attrs={'id': 'vulnprodstable'})
        output_table_1(table1)
        print('\n\n\n')
        print("Products Affected By " + cveID)
        output_table_2(table2)


def main():
    for el in sys.argv[1:]:
        tempstr = ''.join(el)
        parse(tempstr)


if __name__ == '__main__':
    main()