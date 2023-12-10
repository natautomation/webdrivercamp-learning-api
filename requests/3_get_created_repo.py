
"""GET the newly created repo"""

import requests

def get_created_repo(url_):
    """GET repo and assert values"""
    # adding code
    
    header_content = {'Authorization': 'token addYourTokenHere'}
    response = requests.get(url_, headers=header_content)

    print(f'Response status code: {response.status_code}')
    repo = response.json()
    #- 
    assert not repo["has_wiki"] != False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'natautomation'

if __name__ == "__main__":
    v_data = {"owner": {"login": "natautomation", "id": 147779652}, "name": "repo-created-with-api",
              "id": 725440644, "has_wiki": False, "private": True}
    owner = 'natautomation'
    repo = 'repo-created-with-api'
    url = f"https://api.github.com/repos/{owner}/{repo}"
    get_created_repo(url)
