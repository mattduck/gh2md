Export of Github issues for [mattduck/gh2md](https://github.com/mattduck/gh2md). Generated on 2020.08.13 at 00:11:36.

# [\#12 PR](https://github.com/mattduck/gh2md/pull/12) `open`: Remove timestamp in github actions

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) opened issue at [2020-08-11 07:23](https://github.com/mattduck/gh2md/pull/12):

I try to remove timestamp in github actions and found two problem:
1. AttributeError: 'RateLimit' object has no attribute 'rate'
```console
[user@hostname]$ gh2md mattduck/gh2md issues.md -t 259fb4...
...
...
...
Traceback (most recent call last):
  File "/home/yangjincai/.local/bin/gh2md", line 8, in <module>
    sys.exit(main())
  File "/home/yangjincai/.local/lib/python3.7/site-packages/gh2md/gh2md.py", line 50, in main
    include_closed_issues=args.include_closed_issues,
  File "/home/yangjincai/.local/lib/python3.7/site-packages/gh2md/gh2md.py", line 146, in fetch_repo_and_export_to_markdown
    print_rate_limit(github_api)
  File "/home/yangjincai/.local/lib/python3.7/site-packages/gh2md/gh2md.py", line 306, in print_rate_limit
    print("Github API rate limit: {}".format(limit.rate.raw_data))
AttributeError: 'RateLimit' object has no attribute 'rate'
```
2. need to add `gh2md -I` in Github Actions.

I create this PR for testing, but the Github Actions don't run ......

it works in my private repo. 

hope this info is helpful. @mattduck 




-------------------------------------------------------------------------------

# [\#10 Issue](https://github.com/mattduck/gh2md/issues/10) `closed`: Wanna get closed issues

#### <img src="https://avatars0.githubusercontent.com/u/6499816?v=4" width="50">[Duke](https://github.com/longwdl) opened issue at [2017-06-12 08:09](https://github.com/mattduck/gh2md/issues/10):

Wanna get all issues at the same time.

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2020-07-19 19:57](https://github.com/mattduck/gh2md/issues/10#issuecomment-660699450):

For anybody reading this years later: I finally did some work on this project again. By default it will now fetch all issues + PRs, and you can selectively disabled the parts you don't want using some new flags, eg. `--no-closed-prs`.

I actually think closed issues should have always worked, but closed PRs did not.

See the help text or README for more details.


-------------------------------------------------------------------------------

# [\#3 PR](https://github.com/mattduck/gh2md/pull/3) `closed`: Config file for pyup.io

#### <img src="https://avatars0.githubusercontent.com/u/16239342?v=4" width="50">[pyup.io bot](https://github.com/pyup-bot) opened issue at [2017-05-21 12:59](https://github.com/mattduck/gh2md/pull/3):

Hi there and thanks for using pyup.io!

Since you are using a non-default config I've created one for you.

There are a lot of things you can configure on top of that, so make sure to check out the [docs](https://pyup.io/docs/configuration/) to see what I can do for you.




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

