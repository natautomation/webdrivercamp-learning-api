"""Send GET request exercise"""

import requests

def get_repos(url):
    # adding code
    """Send GET request function"""
    response = requests.get(url, params={'q' : 'webdrivercamp-learning-python'})

    print(f'Response status code: {response.status_code}')
    print(f'Total count of found items: {response.json()["total_count"]}')
    res_list = response.json()['items']
  
    return sorted(res_list, key=lambda x: x['owner']['login'])

if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"

    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)

#output
# Response status code: 200
# Total count of found items: 24
#
# Acteonis        webdrivercamp-learning-python-2
# Acteonis        webdrivercamp-learning-python
# AlinaKaty       webdrivercamp-learning-python
# IgorSuvorov     webdrivercamp-learning-python
# JuliaGood       webdrivercamp-learning-python
# PieVan          webdrivercamp-learning-python
# bakhtier23      webdrivercamp-learning-python-python_beginning
# bakhtier23      webdrivercamp-learning-python-python-selenium
# bakhtier23      webdrivercamp-learning-python-python-modules
# bakhtier23      webdrivercamp-learning-python-python-data-structures-continue
# bakhtier23      webdrivercamp-learning-python-python-loops-and-more
# bakhtier23      webdrivercamp-learning-python-python-errors-exceptions
# chekirovstas    webdrivercamp-learning-python
# dvlad7909       webdrivercamp-learning-python
# ehnat0n         webdrivercamp-learning-python
# eli-atlanta     webdrivercamp-learning-python
# emnyc1221       webdrivercamp-learning-python
# galiur          webdrivercamp-learning-python
# isimionica      webdrivercamp-learning-python
# natautomation   webdrivercamp-learning-python
# oleksrud        webdrivercamp-learning-python
# shaikin-s       webdrivercamp-learning-python
# silvervinoth9   webdrivercamp-learning-python
# vr8686          webdrivercamp-learning-python
#
# Process finished with exit code 0
