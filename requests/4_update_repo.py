"""Send PATCH request to update"""

import requests

def update_repo(url_):
    """PATCH function"""
    # adding code here
  
    header_content = {'Authorization': 'token addYourTokenHere'}

    payload = {'description': 'I know Python Requests!'}

    response = requests.patch(url_, headers=header_content
                              , json=payload)

    print(f'Response status code: {response.status_code}')
    repo_ = response.json()

    return repo_


if __name__ == '__main__':
    owner = 'natautomation'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    repo = update_repo(url)


#output
#Process finished with exit code 0
