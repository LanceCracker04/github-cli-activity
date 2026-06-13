<<<<<<< HEAD
# GitHub User Activity

A small Python CLI script intended to fetch GitHub activity for a username and print a simple summary of recent actions.

## Description

This script uses the GitHub REST API to request a user's GitHub data and formats activity events into readable text.

> Note: The current implementation fetches data from the `https://api.github.com/users/{username}` endpoint, which returns profile information. The code is structured to display event summaries, so the endpoint may need to be updated to `https://api.github.com/users/{username}/events/public` for actual activity events.

## Requirements

- Python 3.7+
- Internet access

## Usage

From the project root, run:

```bash
python user_activity.py <github-username>
```

Example:

```bash
python user_activity.py octocat
```

## Output

The script prints a summary of recent GitHub activity, for example:

- 📌 Pushed 3 commit(s) to github-user-activity
- ❗ Opened an issue in octocat/Hello-World
- 🔀 Merged a pull request in octocat/Hello-World

## Files

- `user_activity.py` — main script that fetches GitHub data and formats event output.

## Notes

- The script uses only standard library modules: `argparse`, `json`, `sys`, and `urllib`.
- If you want to fetch actual public events, change the request URL in `fetch_user()` to:
  `https://api.github.com/users/{username}/events/public`.

Project Page URL: https://roadmap.sh/projects/github-user-activity
=======
# github-cli-activity
>>>>>>> f600fde83d767fdc83b7708e9aa60f95bc9757dc
