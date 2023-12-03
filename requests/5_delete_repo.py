"""Send DELETE request"""
import requests


def delete_repo(url_):
    """DELETE function"""
    # adding code here

    header_content = {'Authorization': 'token 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'}

    response = requests.delete(url_, headers=header_content)

    print(f'Response status code: {response.status_code}')


if __name__ == "__main__":
    owner = 'natautomation'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    delete_repo(url)

#output
#Response status code: 201

#Process finished with exit code 0
