from rich.table import Table
import argparse
from InquirerPy import inquirer as inquirer
from InquirerPy import prompt   
from InquirerPy.validator import PathValidator, ValidationError
from rich import table
import os
import sys
import subprocess
from InquirerPy import prompt
from InquirerPy.enum import INQUIRERPY_KEYBOARD_INTERRUPT
from pydriller import Repository, Git
import logging
from rich.console import Console
from InquirerPy import prompt
import time
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
class DrillerWorker:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = Repository(self.repo_path)

        function_names=['show_last_20_commits', 'show_non_merge_commits', 'commit_history_retrieval', 'developer_contributions_analysis', 'code_evolution_analysis', 'impact_analysis', 'repository_summary', 'branch_comparison', 'commit_message_search', 'anomaly_detection', 'release_history', 'file_history_analysis', 'merge_commit_analysis']
        
        def __call__(self, function_name):
            if function_name in self.function_names:
                return getattr(self, function_name)()
            else:
                return "Invalid operation selected. Please try again."
            
        for function_name in function_names:
            logging.debug(f"Creating function {function_name}")
            exec(f"{function_name} = lambda self: self('{function_name}')")
            logging.debug(f"Created function {function_name}")        
            
    def show_last_20_commits(self):
        """
        Show the last 20 commits in the repository in a colorful way with rich library and panel/tables
        """
        Table=None
        import rich 
        from rich.table import Table
        Table = Table(title="Last 20 Commits")
        commits = list(self.repo.traverse_commits())
        Table.add_column("Hash", style="cyan")
        Table.add_column("Message", style="magenta")
        Table.add_column("Author Email", style="green")
        Table.add_column("Author Name", style="green")
        Table.add_column("Author Date", style="green")
        Table.add_column("Committer Email", style="green")
        Table.add_column("Committer Name", style="green")
        Table.add_column("Committer Date", style="green")
        
        
        for commit in commits[:20]:
            print(commit.hash, commit.msg)
            Table.add_row(commit.hash, commit.msg, commit.author.email, commit.author.name, str(commit.author_date), commit.committer.email, commit.committer.name, str(commit.committer_date))

        os.system("cls" if os.name == "nt" else "clear")
        console = Console()
        console.print(Table)
            
    def show_non_merge_commits(self,verbose=False):
        """
        Display highlights of non-merge commits, including modified files and changes.
        """
        repo = self.repo
        commits = repo.traverse_commits()
        non_merge_commits = [commit for commit in commits if commit.merge is False]
        # display in a tree format of commits with children modified_files, and the rich library tables and panels can contrast to show
        # the differences between the commits and the modified files
        console = Console()
        
        for commit in non_merge_commits:
            table = Table(title="Commit")
            table.add_column("Hash", style="cyan")
            table.add_column("Message", style="magenta")
            if verbose:
                table.add_column("Author Email", style="dark_green")
                table.add_column("Author Name", style="green")
                table.add_column("Author Date", style="dark_green")
                table.add_column("Committer Email", style="dark_green")
                table.add_column("Committer Name", style="dark_green")
                table.add_column("Committer Date", style="dark_green")
                table.add_row(commit.hash, commit.msg, commit.author.email, commit.author.name, str(commit.author_date), commit.committer.email, commit.committer.name, str(commit.committer_date))
            else:
                table.add_row(commit.hash, commit.msg)
            for file in commit.modified_files:

                file_table = Table(title="Modified Files")
                file_table.add_column("File Name", style="cyan")
                file_table.add_column("Change Type", style="magenta")
                if verbose:
                    file_table.add_column("Lines Added", style="dark_green")
                    file_table.add_column("Lines Removed", style="dark_green")
                    file_table.add_row(file.filename, file.change_type.name, (file.change_type==file.change_type.MODIFY and file.nloc) or '0', (file.change_type==file.change_type.MODIFY and file.nloc) or '0')
                else:
                    file_table.add_row(file.filename, file.change_type.name )
                    
             
        final_table = Table(title="")
        final_table.add_column("Hash", style="dark_green")
        final_table.add_column("Message", style="dark_green")
        final_table.add_row( table, file_table ) 
        
        console.print(final_table)           
    
    def commit_history_retrieval(self):
        """
        List all commits in the repository with filtering options like date range and author.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        for commit in commits:
            pass
                    
    def developer_contributions_analysis(self):
        """
        Analyze contributions per developer, including commit counts and lines of code.
        """
        repo = self.repo
        commits = list(repo.traverse_commits()) 
        developers = {}
        for commit in commits:
            if commit.author.email not in developers:
                developers[commit.author.email] = 0

    def code_evolution_analysis(self):
        """
        Track changes to specific files or directories over time.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        for commit in commits:
            for file in commit.modified_files:
                pass                
    
    def impact_analysis(self):
        """
        Assess the impact of changes by identifying affected files and potential issues.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        for commit in commits:
            for file in commit.modified_files:
                pass
            # identify affected files
        affected_files = {}
        for commit in commits:
            for file in commit.modified_files:
                if file.filename not in affected_files:
                    affected_files[file.filename] = 0
                affected_files[file.filename] += 1
        # identify potential issues
        potential_issues = {}
        for commit in commits:
            for file in commit.modified_files:
                if file.filename not in potential_issues:
                    potential_issues[file.filename] = []
                potential_issues[file.filename].append(commit.hash)

    def repository_get_branches_pydriller(self):
        """
        List all branches in the repository.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        branches = []
        for commit in commits:
            if commit.branches not in branches:
                for branch in commit.branches:
                    branches.append(branch)
        
    def repository_summary(self):
        """
        Generate a summary of the repository, including total commits, contributors, and language usage.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        print("Total commits:", len(commits))
        authors = set()
        for commit in commits:
            authors.add(commit.author.email)
        print("Total contributors:", len(authors))

                

        files = {}
        for commit in commits:
            for diff in commit.modified_files:
                if diff.new_path not in files:
                    files[diff.new_path] = 0
                files[diff.new_path] += 1
        print("Files changed:", len(files))

        languages = {}
        for file in files:
            extension = file.split(".")[-1]
            if extension not in languages:
                languages[extension] = 0
            languages[extension] += 1
        print("Languages used:", languages)
        
        print ("what files have been modified the most in the repos commits")
        print (sorted(files.items(), key=lambda x: x[1], reverse=True))

    

            
    def branch_comparison(self):

        """
        Compare two branches to identify differences and potential merge conflicts.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        branches = list(commits[0].branches)
        

        # compare two branches
        branch1 = "master"
        branch2 = "develop"
        for commit in commits:
            if branch1 in commit.branches and branch2 in commit.branches:
                pass                    

    def commit_message_search(self):

        """
        Search commit messages for keywords to find relevant changes or decisions.
        """
        repo = self.repo
        commits = list(repo.traverse_commits()) 
        keyword = "bug"
        for commit in commits:
            if keyword in commit.msg:
                pass
    
    def anomaly_detection(self):

        """
        Identify anomalies in commit patterns, such as large commits or frequent reverts.
        """
        repo = self.repo
        commits = list(repo.traverse_commits()) 
        # large commits
        # frequent reverts
        # frequent changes to the same file
        # frequent changes to the same line

    def release_history(self):

        """
        List releases and associated details, including tags and changes.
        """
        repo = self.repo
        tags=[]
        tagged_commits = Git('.').get_tagged_commits()
        for commit in tagged_commits:
            tags.append(commit.tag)
        
    def file_history_analysis(self):

        """
        Trace the history of changes to a specific file, including diffs and commit references.
        """
        repo = self.repo
        commits = list(repo.traverse_commits())
        
        file_path = "README.md"
        for commit in commits:
            for diff in commit.modified_files:
                if diff.new_path == file_path:
                    pass
    
    def merge_commit_analysis(self):    
                    
            """
            Analyze merge commits to understand merging patterns and conflicts resolution.
            """
            repo = self.repo
            commits = list(repo.traverse_commits())     
            merge_commits = [commit for commit in commits if len(commit.parents) > 1]
          
class DrillerOutput:
    def __init__(self,input_text, dw=None):
        self.input_text = input_text
        self.dw=dw
        logging.basicConfig(level=logging.FATAL)
        console = Console()
        
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        
    def print_ascii_art(self):
        self.clear_screen()
        print ("""  
        ██████╗░░█████╗░░█████╗░██╗░░░░░██╗░░░██╗███████╗██████╗░
        ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║░░░██║██╔════╝██╔══██╗
        ██████╦╝██║░░██║██║░░██║██║░░░░░██║░░░██║█████╗░░██████╔╝
        ██╔══██╗██║░░██║██║░░██║██║░░░░░██║░░░██║██╔══╝░░██╔══██╗
        ██████╦╝╚█████╔╝╚█████╔╝███████╗╚██████╔╝███████╗██║░░██║
                
        """)
            
    def create_beautiful_card_with_rich_library(self):
        console = Console()
        console.print("Header", style="bold blue")
        console.print("Header", style="bold blue")
        
        card_items = [
            {"title": "Total Commits", "value": "100"},
            {"title": "Total Contributors", "value": "10"},
            {"title": "Languages", "value": "Python, Java, JavaScript"},
        ]
        table = Table(title="Repository Summary")
        table.add_column("Title", style="bold")
        table.add_column("Value")
        for item in card_items:
            table.add_row(item["title"], item["value"])
        console.print(table)
    
    def show_last_20_commits(self, repo_path):
         """
         Show the last 20 commits in the repository.
            """
         repo = Repository(repo_path)
         commits = list(repo.traverse_commits())
         for commit in commits[:20]:
            pass    

    def print_static_output(self, output_text):
        console = Console()
        console.print(output_text, style="bold green")

    def do_menu_logic(self, answers=None, args=None, dw=None, do=None):
        if (do==None):
            do=DrillerOutput(None)
        elif (dw==None):
            dw=DrillerWorker(args.repo_path)
            
        while True:  # Start an infinite loop
            os.system("cls" if os.name == "nt" else "clear")    
            do.print_ascii_art()
            answers = prompt(operations)
            if answers == None:
                break
            if answers["selected_operation"] == "Show Last 20 Commits":
                self.dw.show_last_20_commits()
            elif answers["selected_operation"] == "Analyze merge commits to understand merging patterns and conflicts resolution.":
                self.dw.merge_commit_analysis()
            elif answers["selected_operation"] == "Merge Commit Analysis":
                self.dw.merge_commit_analysis()
            elif answers["selected_operation"] == "Show Non-Merge Commits Highlight Reel":
                self.dw.show_non_merge_commits()
            elif answers["selected_operation"] == "Commit History Retrieval":
                self.dw.commit_history_retrieval()
            elif answers["selected_operation"] == "Developer Contributions Analysis":
                self.dw.developer_contributions_analysis()
            elif answers["selected_operation"] == "Code Evolution Analysis":
                self.dw.code_evolution_analysis()        
            elif answers["selected_operation"] == "Impact Analysis":
                self.dw.impact_analysis()
            elif answers["selected_operation"] == "Repository Summary":
                self.dw.repository_summary()
            elif answers["selected_operation"] == "Branch Comparison":
                self.dw.branch_comparison()
            elif answers["selected_operation"] == "Commit Message Search":
                self.dw.commit_message_search()
            elif answers["selected_operation"] == "Anomaly Detection":
                self.dw.anomaly_detection()
            elif answers["selected_operation"] == "Release History":
                self.dw.release_history()
            elif answers["selected_operation"] == "File History Analysis":
                self.dw.file_history_analysis()
            else:
                print("Invalid operation selected. Please try again.")
                time.sleep(2)
                continue
            input("Press enter to continue...")    

def get_arguments(args):
    answers=None
    parser = argparse.ArgumentParser(description="Enhanced CLI Tool for Git Repository Analysis")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    file_history_parser = subparsers.add_parser("file_history", help="Analyze file history")
    file_history_parser.add_argument("--repo_path", type=str, help="Path to the repository", required=False)
    file_history_parser.add_argument("--file_path", type=str, help="Path to the file within the repository", required=False)
    console = Console()
    args = parser.parse_args(args)
    dw=DrillerWorker(args.repo_path)
    do=DrillerOutput(None, dw)
    do.do_menu_logic()
    
def main():
    args=None
    dod=None
    print('processing...')
    print('done')
    input('press enter when complete...')
    dod = get_arguments(sys.argv[1:])

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")    
    main()
