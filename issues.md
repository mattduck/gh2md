Export of Github issues for [mattduck/gh2md](https://github.com/mattduck/gh2md). Generated on 2020.07.19 at 05:59:43.

# [\#11 Issue](https://github.com/mattduck/gh2md/issues/11) `open`: A github actions example to extract issues of the repo itself

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) opened issue at [2020-07-16 07:42](https://github.com/mattduck/gh2md/issues/11):

Thank you for your great work.

I add my github actions example here, in case someone needs it.

it backups all issues every days.

Because it only backup the issues belong to the repository that contains this workflow. It do not limit by GitHub API rate.
```console
# gh2md log:
...
Exported 28 issues
Writing to file: issues.md
Github API rate limit: {u'reset': 1594884997, u'limit': 15000, u'remaining': 15000}
Done.
```


```yaml
# .github/workflows/issues2md.yml
name: Issues2Markdown
on:
  push:
  schedule:
    # every day
    - cron: "0 0 * * *"
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
      with:
        persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal token
        fetch-depth: 0 # otherwise, you will failed to push refs to dest repo
    - name: Backup github issues to a markdown file.
      run: |
        pip install wheel
        pip install --user gh2md
        $HOME/.local/bin/gh2md $GITHUB_REPOSITORY issues.md --token ${{ secrets.GITHUB_TOKEN }}
        git add issues.md
    - name: Commit files
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git commit -m "Backup all issues into issues.md" -a
    - name: Extract branch name
      shell: bash
      run: echo "##[set-output name=branch;]$(echo ${GITHUB_REF#refs/heads/})"
      id: extract_branch
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        branch: ${{ steps.extract_branch.outputs.branch }}

```

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2020-07-16 21:24](https://github.com/mattduck/gh2md/issues/11#issuecomment-659682052):

@0ut0fcontrol thanks for sharing this, it's super cool! I'll find somewhere sensible to publicise it - at least link to it from the README. I think I should set it up for gh2md itself.

I'm glad this is useful for you and still working OK. I haven't used it much recently, so I'm not sure if there are any problems or obvious features that would help - feel free to open issues if you do have anything.

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) commented at [2020-07-17 06:34](https://github.com/mattduck/gh2md/issues/11#issuecomment-659893686):

@mattduck `gh2md` works well. If I found any problems or features I will open a issues for it.

My purpose is to backup my repo with issues.

And the issues is **readable** even when I do not has access to github.com.

Combining `gh2md` and `pandoc --self-contained` served my purpose.

(I am not test other tools yet, this may not be the best way to do this.)

Here is a script to setup crontab to fetch repos and convert `issues.md` to `issues.html`.
```bash
#!/bin/bash

# crontab -e
# 0 1 * * * bash path_to/backup_issues/backup_issues.sh &> path_to/backup_issues/backup_issues.sh.log
# backup_issues
# ├── backup_issues.sh
# ├── repo1
# ├── repo2
# └── repo3

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
for i in $DIR/*/; do
    date
    cd $i
    pwd
    git fetch --all --verbose
    git pull
    test -f issues.md && pandoc --self-contained issues.md -o issues.html --metadata title=backup_issues
    test -f issues.html && echo "backup issues in ${i}issues.html"
    echo "#############################################################################"
done
```


-------------------------------------------------------------------------------

# [\#10 Issue](https://github.com/mattduck/gh2md/issues/10) `open`: Wanna get closed issues

#### <img src="https://avatars0.githubusercontent.com/u/6499816?v=4" width="50">[Duke](https://github.com/longwdl) opened issue at [2017-06-12 08:09](https://github.com/mattduck/gh2md/issues/10):

Wanna get all issues at the same time.




-------------------------------------------------------------------------------

# [\#2 Issue](https://github.com/mattduck/gh2md/issues/2) `closed`: Initial Update

#### <img src="https://avatars0.githubusercontent.com/u/16239342?v=4" width="50">[pyup.io bot](https://github.com/pyup-bot) opened issue at [2017-05-21 12:59](https://github.com/mattduck/gh2md/issues/2):

Hi 👊

This is my first visit to this fine repo, but it seems you have been working hard to keep all dependencies updated so far.

Once you have closed this issue, I'll create separate pull requests for every update as soon as I find one.

That's it for now!

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#1 Issue](https://github.com/mattduck/gh2md/issues/1) `closed`: Example issue
**Labels**: `enhancement`


#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) opened issue at [2017-05-20 18:11](https://github.com/mattduck/gh2md/issues/1):

I'm making an issue just so I can run this tool against its own repository.

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2017-05-20 18:11](https://github.com/mattduck/gh2md/issues/1#issuecomment-302889476):

This is a comment.

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2017-05-20 18:11](https://github.com/mattduck/gh2md/issues/1#issuecomment-302889489):

Closing, as the example data now exists.


-------------------------------------------------------------------------------

