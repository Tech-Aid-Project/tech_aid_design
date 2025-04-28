import os

def validate_branch_and_pr_title(branch, pr_title):
    """
    Validates if the branch name and PR title follow the 'TADSG-' pattern.
    Args:
        branch (str): The name of the branch to validate.
        pr_title (str): The title of the pull request (PR) to validate.
    Returns:
        bool: True if both the branch and the pull request follow the 'TADSG-' pattern, False otherwise.
    Prints:
        str: A message indicating whether the branch and PR title are valid or specifying the validation error.
    """

    # Verify if the branch starts with 'TADSG-'
    if not branch.startswith("TADSG-"):
        print(f"The branch '{branch}' does not start with the pattern 'TADSG-'.")
        return False
    # Verify if the branch contains with 'TADSG-'
    if "TADSG-" not in pr_title:
        print(f"The PR title '{pr_title}' does not contain the pattern 'TADSG-'.")
        return False
    
    print(f"Validation successful: The branch '{branch}' and the PR title '{pr_title}' follow the 'TADSG-' pattern.")

    return True

if __name__ == "__main__":
    PR_BRANCH = os.getenv("GITHUB_HEAD_REF")
    PR_TITLE = os.getenv("PR_TITLE")
    
    if not PR_BRANCH:
        raise ValueError("The environment variable GITHUB_HEAD_REF is not defined.")
    if not PR_TITLE:
        raise ValueError("The environment variable PR_TITLE is not defined.")
    
    print(f"Captured PR branch: {PR_BRANCH}")
    print(f"Captured PR title: {PR_TITLE}")

    if not validate_branch_and_pr_title(PR_BRANCH, PR_TITLE):
        exit(1)
