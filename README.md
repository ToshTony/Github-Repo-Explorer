# GitHub Repo Explorer

GitHub Repo Explorer is a Python script that fetches information about a GitHub repository using the GitHub API. It provides details such as the repository name, description, primary language, stars, forks, and URL.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

### Prerequisites

- Python installed on your system
- GitHub Personal Access Token (instructions on how to generate one [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token))

### Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/github-repo-explorer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd github-repo-explorer
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory if you haven't already.
3. Run the script:

   ```bash
   python github_repo_explorer.py
   ```

4. Follow the prompts and enter the owner and name of the repository you want to fetch information about.
5. If prompted, enter your GitHub Personal Access Token when prompted.
6. The script will then fetch and display information about the specified repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
