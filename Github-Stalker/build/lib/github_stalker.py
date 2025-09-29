import requests
import argparse
from collections import defaultdict

# response = requests.get("https://api.github.com/users/zacharee/events")
# response = requests.get("https://api.github.com/users/kamranahmedse/events")

class Github_Stalker:
    def __init__(self, username):
        response = requests.get(f"https://api.github.com/users/{username}/events")
        self.rtj = response.json()
        self.report = ""
        print("Here's what "+ username + " has been up to...")

    def push_fetch(self):
        
        counter_dict = defaultdict(int)

        for event in self.rtj:
            # print(self.rtj)
            if event["type"] == "PushEvent":
                counter_dict[event["repo"]["name"]] += 1

            elif event["type"] == "WatchEvent":
                self.report += f"Starred the " + event["repo"]["name"] + " repo.\n"

            elif event["type"] == "DeleteEvent":
                self.report += f"Deleted the " + event["repo"]["name"] + " repo.\n"
            
            elif event["type"] == "IssuesEvent":
                if event["payload"]["action"] == "closed":
                    self.report += f"Closed the '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"

                elif event["payload"]["action"] == "opened":
                    self.report += f"Created a new '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"

                elif event["payload"]["action"] == "edited":
                    self.report += f"Modified the '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"

                elif event["payload"]["action"] == "deldted":
                    self.report += f"Deleted the '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"
            
            elif event["type"] == "IssueCommentEvent":
                if event["payload"]["action"] == "created":
                    self.report += f"Commented '"+ event["payload"]["comment"]["body"] +"' on the '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"
                elif event["payload"]["action"] == "edited":
                    self.report += f"Edited the '"+ event["payload"]["comment"]["body"] +"' on the '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"
                elif event["payload"]["action"] == "deleted":
                    self.report += f"Deleted the '"+ event["payload"]["comment"]["body"] +"' on the '"+ event["payload"]["issue"]["title"] +"' issue in the " + event["repo"]["name"] + " repo.\n"

            elif event["type"] == "PullRequestEvent":
                if event["payload"]["action"] == "opened":
                    self.report += f"Created a pull request titled '"+ event["payload"]["pull_request"]["title"] +"' in the '"+ event["repo"]["name"] +" repo.\n"
                elif event["payload"]["action"] == "closed":
                    self.report += f"Closed the pull request titled '"+ event["payload"]["pull_request"]["title"] +"' in the '"+ event["repo"]["name"] +" repo.\n"
                elif event["payload"]["action"] == "edited":
                    self.report += f"Modified the pull request titled '"+ event["payload"]["pull_request"]["title"] +"' in the '"+ event["repo"]["name"] +" repo.\n"

        for res in counter_dict:
            self.report += f"Pushed "+ str(counter_dict[res]) + " commits to the "+ res + " repo.\n"

        if self.report == "":
            print("This user hasn't made any public updates yet")
        print(self.report)


def main():
    parser = argparse.ArgumentParser(description="GitHub Stalker")
    parser.add_argument("username", help="The github username of the person you're hunting down")
    
    cli_arg = parser.parse_args()

    Github_Stalker(cli_arg.username).push_fetch()

    # operation.push_fetch()

if __name__ == "__main__":
    main()