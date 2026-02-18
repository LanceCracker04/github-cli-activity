import sys
import urllib.request
import urllib.error
import json

def fetch_activity(username):
    """Fetches user activity from the GitHub API."""
    url = f"https://api.github.com/users/{username}/events"
    
    # GitHub requires a User-Agent header, otherwise it blocks the request
    req = urllib.request.Request(url, headers={'User-Agent': 'Python-CLI-App'})

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: GitHub user '{username}' not found.")
        elif e.code == 403:
            print("Error: API rate limit exceeded. Try again later.")
        else:
            print(f"Error: Failed to fetch data (HTTP {e.code}).")
        sys.exit(1)
        
    except urllib.error.URLError as e:
        print(f"Error: Network issue. Check your connection. ({e.reason})")
        sys.exit(1)

def display_activity(events):
    """Parses and prints the event data to the terminal."""
    if not events:
        print("No recent public activity found for this user.")
        return

    # Loop through the events (limiting to the 10 most recent for clean output)
    for event in events[:10]:
        repo_name = event['repo']['name']
        event_type = event['type']
        
        # Format the output based on the specific type of GitHub event
        if event_type == 'PushEvent':
            commits = len(event['payload']['commits'])
            print(f"- Pushed {commits} commit(s) to {repo_name}")
            
        elif event_type == 'IssuesEvent':
            action = event['payload']['action']
            print(f"- {action.capitalize()} an issue in {repo_name}")
            
        elif event_type == 'WatchEvent':
            print(f"- Starred {repo_name}")
            
        elif event_type == 'CreateEvent':
            ref_type = event['payload']['ref_type']
            print(f"- Created a new {ref_type} in {repo_name}")
            
        elif event_type == 'ForkEvent':
             print(f"- Forked {repo_name}")
             
        else:
            # Fallback for events we haven't explicitly formatted
            print(f"- Triggered {event_type} in {repo_name}")

def main():
    # Ensure the user provided exactly one argument (the script name + the username)
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    
    print(f"Fetching recent activity for {username}...\n")
    events = fetch_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()