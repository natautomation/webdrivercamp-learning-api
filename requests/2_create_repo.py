"""Send POST request to create"""
#delete token!

import requests
from pprint import pprint
#pprint import pprint

def create_repo(url):
    # adding code
    """create repo POST request"""

    # Use actual token!!!
    header_content = {'Authorization': 'token addYourTokenHere'}
    payload = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, headers=header_content, json=payload)
    print(f'Response status code: {response.status_code}')

    return response.json()

if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)
    #print(repo)

#output correst:

# Response status code: 201
# {'allow_auto_merge': False,
#  'allow_forking': True,
#  'allow_merge_commit': True,
#  'allow_rebase_merge': True,
#  'allow_squash_merge': True,
#  'allow_update_branch': False,
#  'archive_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/{archive_format}{/ref}',
#  'archived': False,
#  'assignees_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/assignees{/user}',
#  'blobs_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/git/blobs{/sha}',
#  'branches_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/branches{/branch}',
#  'clone_url': 'https://github.com/natautomation/repo-created-with-api.git',
#  'collaborators_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/collaborators{/collaborator}',
#  'comments_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/comments{/number}',
#  'commits_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/commits{/sha}',
#  'compare_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/compare/{base}...{head}',
#  'contents_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/contents/{+path}',
#  'contributors_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/contributors',
#  'created_at': '2023-11-30T06:28:32Z',
#  'default_branch': 'main',
#  'delete_branch_on_merge': False,
#  'deployments_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/deployments',
#  'description': None,
#  'disabled': False,
#  'downloads_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/downloads',
#  'events_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/events',
#  'fork': False,
#  'forks': 0,
#  'forks_count': 0,
#  'forks_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/forks',
#  'full_name': 'natautomation/repo-created-with-api',
#  'git_commits_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/git/commits{/sha}',
#  'git_refs_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/git/refs{/sha}',
#  'git_tags_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/git/tags{/sha}',
#  'git_url': 'git://github.com/natautomation/repo-created-with-api.git',
#  'has_discussions': False,
#  'has_downloads': True,
#  'has_issues': True,
#  'has_pages': False,
#  'has_projects': True,
#  'has_wiki': False,
#  'homepage': None,
#  'hooks_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/hooks',
#  'html_url': 'https://github.com/natautomation/repo-created-with-api',
#  'id': 725440644,
#  'is_template': False,
#  'issue_comment_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/issues/comments{/number}',
#  'issue_events_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/issues/events{/number}',
#  'issues_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/issues{/number}',
#  'keys_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/keys{/key_id}',
#  'labels_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/labels{/name}',
#  'language': None,
#  'languages_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/languages',
#  'license': None,
#  'merge_commit_message': 'PR_TITLE',
#  'merge_commit_title': 'MERGE_MESSAGE',
#  'merges_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/merges',
#  'milestones_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/milestones{/number}',
#  'mirror_url': None,
#  'name': 'repo-created-with-api',
#  'network_count': 0,
#  'node_id': 'R_kgDOKz1YhA',
#  'notifications_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/notifications{?since,all,participating}',
#  'open_issues': 0,
#  'open_issues_count': 0,
#  'owner': {'avatar_url': 'https://avatars.githubusercontent.com/u/147779652?v=4',
#            'events_url': 'https://api.github.com/users/natautomation/events{/privacy}',
#            'followers_url': 'https://api.github.com/users/natautomation/followers',
#            'following_url': 'https://api.github.com/users/natautomation/following{/other_user}',
#            'gists_url': 'https://api.github.com/users/natautomation/gists{/gist_id}',
#            'gravatar_id': '',
#            'html_url': 'https://github.com/natautomation',
#            'id': 147779652,
#            'login': 'natautomation',
#            'node_id': 'U_kgDOCM7wRA',
#            'organizations_url': 'https://api.github.com/users/natautomation/orgs',
#            'received_events_url': 'https://api.github.com/users/natautomation/received_events',
#            'repos_url': 'https://api.github.com/users/natautomation/repos',
#            'site_admin': False,
#            'starred_url': 'https://api.github.com/users/natautomation/starred{/owner}{/repo}',
#            'subscriptions_url': 'https://api.github.com/users/natautomation/subscriptions',
#            'type': 'User',
#            'url': 'https://api.github.com/users/natautomation'},
#  'permissions': {'admin': True,
#                  'maintain': True,
#                  'pull': True,
#                  'push': True,
#                  'triage': True},
#  'private': True,
#  'pulls_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/pulls{/number}',
#  'pushed_at': '2023-11-30T06:28:33Z',
#  'releases_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/releases{/id}',
#  'size': 0,
#  'squash_merge_commit_message': 'COMMIT_MESSAGES',
#  'squash_merge_commit_title': 'COMMIT_OR_PR_TITLE',
#  'ssh_url': 'git@github.com:natautomation/repo-created-with-api.git',
#  'stargazers_count': 0,
#  'stargazers_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/stargazers',
#  'statuses_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/statuses/{sha}',
#  'subscribers_count': 0,
#  'subscribers_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/subscribers',
#  'subscription_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/subscription',
#  'svn_url': 'https://github.com/natautomation/repo-created-with-api',
#  'tags_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/tags',
#  'teams_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/teams',
#  'topics': [],
#  'trees_url': 'https://api.github.com/repos/natautomation/repo-created-with-api/git/trees{/sha}',
#  'updated_at': '2023-11-30T06:28:33Z',
#  'url': 'https://api.github.com/repos/natautomation/repo-created-with-api',
#  'use_squash_pr_title_as_default': False,
#  'visibility': 'private',
#  'watchers': 0,
#  'watchers_count': 0,
#  'web_commit_signoff_required': False}
#
# Process finished with exit code 0
