# Info
## Entry point
The table of contents and overview is in [this notebook](notebooks/node0.ipynb).
The original web page of the course is http://www-static.etp.physik.uni-muenchen.de/kurs/Computing/python2/.

## How to update your local copy with changes from git
When you work with a jupyter notebook, it will be saved automatically from time to time. This includes, e.g., also output from executing cells. When the git repository is updated, you need to download and merge them into your local copy.

To avoid merge conflicts (which are typical to happen when jupyter notebooks are edited), you will need to reset your local copy before starting the merge. The easiest way is to start from scratch, i.e. delete your working folder and re-clone the git repository.

Other methods would be:
* You can discard all local changes, but save them for possible re-use later using `git stash`.
* You can discard all local changes permanently with `git reset --hard`.

If `git status` shows no modified files, you can safely run `git pull` in your working copy to get the latest updates.

Hint: There is a plugin called [nbdime](https://nbdime.readthedocs.io/en/latest/) that conveniently allows to display changes in the notebooks.

## How to avoid output in jupyter-notebooks being added to git
* install `pre-commit` from (https://pre-commit.com/)
* run `pre-commit install` in repository
* when `jupyter-notebook-cleanup` reports `Failed` on `git commit` (it will whenever output has been removed), `git add` the changed files again and rerun `git commit`
