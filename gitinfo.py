import requests

# GitHub Personal Access Token
TOKEN = "your github token"

def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_data = response.json()
        return repo_data
    else:
        print(f"Error: Unable to fetch data for {owner}/{repo}")
        return None

def main():
    owner = input("Enter the owner of the repository: ")
    repo = input("Enter the name of the repository: ")
    
    repo_info = get_repo_info(owner, repo)
    if repo_info:
        print("Repository Information:")
        print(f"Name: {repo_info['name']}")
        print(f"Description: {repo_info['description']}")
        print(f"Language: {repo_info['language']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
        print(f"URL: {repo_info['html_url']}")
    else:
        print("Failed to retrieve repository information.")

if __name__ == "__main__":
    main()
