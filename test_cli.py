import argparse
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator, ValidationError
from rich.console import Console
from rich.table import Table
import os
import argparse
from InquirerPy import inquirer as inquirer
from InquirerPy import prompt   
from InquirerPy.validator import PathValidator, ValidationError
from rich.console import Console
from rich.table import Table
import os
import sys
import subprocess
from InquirerPy import prompt
from InquirerPy.enum import INQUIRERPY_KEYBOARD_INTERRUPT
from pydriller import Repository
# Setup rich console
console = Console()
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def print_ascii_art():
    pass    
class DrillerWorker:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = None    
    def show_last_20_commits(self):
        """
        Show the last 20 commits in the repository.
        """
        repo = self.repo
        repo = Repository(self.repo_path)
        commits = list(repo.iter_commits(max_count=20))
        for commit in commits:
            print(commit.hexsha, commit.summary)
            
    def show_non_merge_commits(self):
        """
        Display highlights of non-merge commits, including modified files and changes.
        """
        repo = self.repo
        non_merge_commits = list(repo.iter_commits(no_merges=True))
        for commit in non_merge_commits:
            print(commit.hexsha, commit.summary)
            for diff in commit.diff():
                print(diff.a_path, diff.b_path)
                print(diff.diff)

    def commit_history_retrieval(self):
        """
        List all commits in the repository with filtering options like date range and author.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        for commit in commits:
            print(commit.hexsha, commit.summary, commit.authored_datetime, commit.author)
            
    def developer_contributions_analysis(self):
        """
        Analyze contributions per developer, including commit counts and lines of code.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        developers = {}
        for commit in commits:
            if commit.author.email not in developers:
                developers[commit.author.email] = 0
            developers[commit.author.email] += 1
        for developer, commit_count in developers.items():
            print(developer, commit_count)

    def code_evolution_analysis(self):
        """
        Track changes to specific files or directories over time.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        for commit in commits:
            for diff in commit.diff():
                print(diff.a_path, diff.b_path, diff.diff)

    def impact_analysis(self):
        """
        Assess the impact of changes by identifying affected files and potential issues.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        for commit in commits:
            for diff in commit.diff():
                print(diff.a_path, diff.b_path, diff.diff)

    def repository_summary(self):
        """
        Generate a summary of the repository, including total commits, contributors, and language usage.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        print("Total commits:", len(commits))
        contributors = {commit.author.email for commit in commits}
        print("Contributors:", len(contributors))
        languages = {
            blob.name.split(".")[-1]
            for blob in repo.tree.traverse()
            if blob.type == "blob"
        }
        print("Languages:", languages)
        # most commonly chnaged files
        # most commonly changed lines
        # most commonly changed directories

        files = {}
        for commit in commits:
            for diff in commit.diff():
                if diff.a_path not in files:
                    files[diff.a_path] = 0
                files[diff.a_path] += 1
        sorted_files = sorted(files.items(), key=lambda x: x[1], reverse=True)
        print("Most commonly changed files:", sorted_files[:5])
        
    def branch_comparison(self):

        """
        Compare two branches to identify differences and potential merge conflicts.
        """
        repo = self.repo
        branches = list(repo.branches)
        print(branches)
        # compare branches
        # identify differences
        # identify potential merge conflicts

    def commit_message_search(self):

        """
        Search commit messages for keywords to find relevant changes or decisions.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        keyword = "bug"
        for commit in commits:
            if keyword in commit.message:
                print(commit.hexsha, commit.summary)

    def anomaly_detection(self):

        """
        Identify anomalies in commit patterns, such as large commits or frequent reverts.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        # large commits
        # frequent reverts
        # frequent changes to the same file
        # frequent changes to the same line

    def release_history(self):

        """
        List releases and associated details, including tags and changes.
        """
        repo = self.repo
        tags = list(repo.tags)
        for tag in tags:
            print(tag.name, tag.commit)

    def file_history_analysis(self):

        """
        Trace the history of changes to a specific file, including diffs and commit references.
        """
        repo = self.repo
        commits = list(repo.iter_commits())
        file_path = "README.md"
        for commit in commits:
            for diff in commit.diff():
                if diff.a_path == file_path:
                    print(diff.a_path, diff.b_path, diff.diff)

    def merge_commit_analysis(self):    
                    
            """
            Analyze merge commits to understand merging patterns and conflicts resolution.
            """
            repo = self.repo
            commits = list(repo.iter_commits())
            merge_commits = [commit for commit in commits if len(commit.parents) > 1]
            for commit in merge_commits:
                print(commit.hexsha, commit.summary)
                print(commit.parents)
                for diff in commit.diff():
                    print(diff.a_path, diff.b_path, diff.diff)
          
class DrillerOutput:
     def __init__(self,input_text):
        self.input_text = input_text
        # use rich to print the input text
        console.print(input_text)

        # ADD any style
        console.print(input_text, style="bold red")
        
        # ADD any style
        console.print(input_text, style="bold red")
        
        # ADD any style
        console.print(input_text, style="bold red")
        
     def show_last_20_commits(self, repo_path):
         """
         Show the last 20 commits in the repository.
         """ 
         for commit in Repository(repo_path).traverse_commits():
             print(commit.hash, commit.msg)
def main():

    
    parser = argparse.ArgumentParser(description="Enhanced CLI Tool for Git Repository Analysis")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Adding subparsers for operations, similar to previous examples
    # Example subparser: File History Analysis
    file_history_parser = subparsers.add_parser("file_history", help="Analyze file history")
    file_history_parser.add_argument("--repo_path", type=str, help="Path to the repository", required=False)
    file_history_parser.add_argument("--file_path", type=str, help="Path to the file within the repository", required=False)
    
    args = parser.parse_args()

    # Handling for specific commands
    # Placeholder for command handling and operations implementation
    clear_screen()
    console.print('Header', style="bold blue")
    operations = [  
        {
            "type": "list",
            "message": "SELECT AN OPERATION TO PERFORM",
            "name": "selected_operation",
            "choices": [
                "Show Last 20 Commits",
                "Analyze merge commits to understand merging patterns and conflicts resolution.", 
                "Merge Commit Analysis",
                "Show Non-Merge Commits Highlight Reel",
                "Commit History Retrieval",
                "Developer Contributions Analysis",
                "Code Evolution Analysis",
                "Impact Analysis",
                "Repository Summary",
                "Branch Comparison",
                "Commit Message Search",
                "Anomaly Detection",
                "Release History",
                "File History Analysis",
            ],
        }
    ]
    
    from InquirerPy import prompt

    answers = prompt(operations)
    import time
    time.sleep(2)
    
    clear_screen()
    print ("Header")

    dw=DrillerWorker(args.repo_path)
    do=DrillerOutput(answers)

    print (answers)
    
    answers = answers["selected_operation"]
    
    if answers == "Show Last 20 Commits":
        do.show_last_20_commits(args.repo_path)
    elif answers == "Show Non-Merge Commits Highlight Reel":
        dw.show_non_merge_commits(args.repo_path)
    elif answers == "Commit History Retrieval":
        dw.commit_history_retrieval(args.repo_path)
    elif answers == "Developer Contributions Analysis":
        dw.developer_contributions_analysis(args.repo_path)
    elif answers == "Code Evolution Analysis":
        dw.code_evolution_analysis(args.repo_path)
    elif answers == "Impact Analysis":  
        dw.impact_analysis(args.repo_path)
    elif answers == "Repository Summary":
        dw.repository_summary(args.repo_path)
    elif answers == "Branch Comparison":
        dw.branch_comparison(args.repo_path)
    elif answers == "Commit Message Search":
        dw.commit_message_search(args.repo_path)
    elif answers == "Anomaly Detection":
        dw.anomaly_detection(args.repo_path)
    elif answers == "Release History":
        dw.release_history(args.repo_path)
    elif answers == "File History Analysis":
        dw.file_history_analysis(args.repo_path)
    elif answers == "Merge Commit Analysis":
        dw.merge_commit_analysis(args.repo_path)
    else:
        console.print("Invalid operation selected. Please try again.", style="bold red")
 
        
if __name__ == "__main__":
    main()
                
a="""

    # Path: test_cli.py
    # path/filename: test_complete_cli_tool.py

        
    # Path: test_cli.py
    # path/filename: test_cli_tool_integration.py
    import os
    import sys

    import unittest
    from unittest.mock import patch
    from io import StringIO
    from complete_cli_tool import main
            
    class TestCliToolIntegration(unittest.TestCase):
    import os
    import sys
    import unittest
    from unittest.mock import patch
    from io import StringIO
    from complete_cli_tool import main

    class TestCompleteCliTool(unittest.TestCase):
        @patch("sys.stdout", new_callable=StringIO)
        def test_main(self, mock_stdout):
            with patch("builtins.input", side_effect=["1", "1"]):
                main()
                expected_output = "Header"
                self.assertIn(expected_output, mock_stdout.getvalue())

    if __name__ == "__main__":
        unittest.main() 
    # Path: test_cli.py
    # path/filename: test_enhanced_cli_tool.py

    import os
    import sys
    import unittest
    from unittest.mock import patch
    from io import StringIO
    from enhanced_cli_tool import main

    class TestEnhancedCliTool(unittest.TestCase):
        @patch("sys.stdout", new_callable=StringIO)
        def test_main(self, mock_stdout):
            with patch("builtins.input", side_effect=["1", "1"]):
                main()
                expected_output = "Header"
                self.assertIn(expected_output, mock_stdout.getvalue())

    if __name__ == "__main__":
        unittest.main()
        
        @patch("sys.stdout", new_callable=StringIO)
        def test_main(self, mock_stdout):
            with patch("builtins.input", side_effect=["1", "1"]):
                main()
                expected_output = "Header"
                self.assertIn(expected_output, mock_stdout.getvalue())
                    
                    if __name__ == "__main__":
                        unittest.main()
                        # Path: test_cli.py
                        #   
                        # path/filename: test_cli_tool_integration.py
                        #   
                        #   
                        # import os
                        # import sys
                        #   
                        # import unittest
                        #   
                        # from complete_cli_tool import main
                        #       
                        #           
                        # class TestCliToolIntegration(unittest.TestCase):
                        #   def test_main(self):
                        #    with patch("builtins.input", side_effect=["1", "1"]):
                        #       main()      
                        #       
                        #       `

    """
