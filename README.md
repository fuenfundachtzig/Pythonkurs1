[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fuenfundachtzig/Pythonkurs1/HEAD?filepath=notebooks%2Fnode0.ipynb)

# Info
## Entry point
The table of contents and overview is in [this notebook](notebooks/node0.ipynb).
The original web page of the course is http://www-static.etp.physik.uni-muenchen.de/kurs/Computing/python2/.
You can run the notebooks online by clicking the blue button reading `binder` above.

## Hints
General hints useful in this context.

### How to update your local copy with changes from git
When you work with a jupyter notebook, it will be saved automatically from time to time. This includes, e.g., also output from executing cells. When the git repository is updated, you need to download and merge them into your local copy.

To avoid merge conflicts (which are typical to happen when jupyter notebooks are edited), you will need to reset your local copy before starting the merge. The easiest way is to start from scratch, i.e. delete your working folder and re-clone the git repository.

Other methods would be:
* You can discard all local changes, but save them for possible re-use later using `git stash`.
* You can discard all local changes permanently with `git reset --hard`.

If `git status` shows no modified files, you can safely run `git pull` in your working copy to get the latest updates. Often, it's easiest to just try `git pull --rebase` to pull the changes and put your own changes on top of them.

Hint: There is a plugin called [nbdime](https://nbdime.readthedocs.io/en/latest/) that conveniently allows to display changes in the notebooks.

### How to avoid output in jupyter-notebooks being added to git
* install `pre-commit` from (https://pre-commit.com/)
* run `pre-commit install` in repository
* when `jupyter-notebook-cleanup` reports `Failed` on `git commit` (it will whenever output has been removed), `git add` the changed files again and rerun `git commit`

### Cherry-picking from a second repository
* add the source as another remote: `git remote add public [URL]`
* fetch commits: `git fetch public`
* list them: `git log public/master`
* cherry pick commit A..B: `git cherry-pick A^..B`
* pushing to our master: `git push origin master`

### Checking the installed Jupyter kernels
List them with `jupyter kernelspec list`. Check JSON file there to make sure the correct Python version is called. Find out which Python version in running in a notebook:
```
import sys
print (sys.version)
```

