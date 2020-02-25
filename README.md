# Info
## Entry
The table of contents and overview is in [this notebook](node0.ipynb).

## How to avoid output in jupyter-notebooks being added to git
* install `pre-commit` from (https://pre-commit.com/)
* run `pre-commit install` in repository
* when `jupyter-notebook-cleanup` reports "Failed" on commit, git-add the changed files again (from which the output has been removed) and retry
