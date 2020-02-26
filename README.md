# Info
## Entry
The table of contents and overview is in [this notebook](notebooks/node0.ipynb).
The original web page of the course is http://www-static.etp.physik.uni-muenchen.de/kurs/Computing/python2/.

## How to avoid output in jupyter-notebooks being added to git
* install `pre-commit` from (https://pre-commit.com/)
* run `pre-commit install` in repository
* when `jupyter-notebook-cleanup` reports `Failed` on `git commit` (it will whenever output has been removed), `git add` the changed files again and rerun `git commit`
