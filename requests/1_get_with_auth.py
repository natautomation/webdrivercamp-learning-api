"""Send GET request with Auth"""

import requests

def get_with_auth(url_):
    # code adding here
    """GET with Auth function"""

    #check token/delete after  graded assignment !!!!
 
    header_content = {'Authorization': 'token addYourTokenHere'}
    response = requests.get(url_, headers=header_content)
    print(f'Response status code: {response.status_code}')

    return len(response.json()), response.headers


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")

  
#output
# Response status code: 200
# Total Repos: 6
# Response headers: {'Server': 'GitHub.com', 'Date': 'Sat, 02 Dec 2023 03:08:08 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Cache-Control': 'private, max-age=60, s-maxage=60', 'Vary': 'Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding, Accept, X-Requested-With', 'ETag': 'W/"a3949fcfd78ded502265459de7e19c94d263cf2a02475783fee5a9ea88c179e9"', 'X-OAuth-Scopes': 'admin:enterprise, admin:gpg_key, admin:org, admin:org_hook, admin:public_key, admin:repo_hook, admin:ssh_signing_key, audit_log, codespace, copilot, delete:packages, delete_repo, gist, notifications, project, repo, user, workflow, write:discussion, write:packages', 'X-Accepted-OAuth-Scopes': '', 'X-GitHub-Media-Type': 'github.v3; format=json', 'x-github-api-version-selected': '2022-11-28', 'X-RateLimit-Limit': '5000', 'X-RateLimit-Remaining': '4999', 'X-RateLimit-Reset': '1701490088', 'X-RateLimit-Used': '1', 'X-RateLimit-Resource': 'core', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': 'C6D4:69E3:5F59045:6287EFD:656A9F98'}
# 
# Process finished with exit code 0
