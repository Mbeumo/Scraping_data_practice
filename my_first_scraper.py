from bs4 import BeautifullSoup
import csv
def request_github_trending(url:str)->str:


def extract(page:str)->str:
    soup=BeautifullSoup(page.content,'html.parser')
    rows=soup.find_all(class_='Box-row')
    return rows


def transform(html_repos:[str])->[str]:



def format(repositories_data:[str]):
    csv_file =','.join(repositories_data[0].keys())+ '\n'
    for user in repositories_data:
        line = ','.join(user.values())+'\n'
        csv_file += line
    return csv_file