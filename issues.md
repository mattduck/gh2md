Export of Github issues for [mattduck/gh2md](https://github.com/mattduck/gh2md).

# [\#16 PR](https://github.com/mattduck/gh2md/pull/16) `open`: Create Markdown file even after abort

#### <img src="https://avatars2.githubusercontent.com/u/14315968?v=4" width="50">[Daniel Vogt](https://github.com/C0D3D3V) opened issue at [2020-10-21 08:28](https://github.com/mattduck/gh2md/pull/16):

I think it would be great if you can abort the whole process after a rate limit and still create the markdown file for the stuff that has already been downloaded.

Especially if you have already downloaded a few thousand entries this is very annoying.




-------------------------------------------------------------------------------

# [\#15 PR](https://github.com/mattduck/gh2md/pull/15) `open`: Using python3 (pip3) in Github Actions.

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) opened issue at [2020-09-17 02:40](https://github.com/mattduck/gh2md/pull/15):

> The workflow always has this issue, is that because I am using Chinese?
> ```
> UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)
> ```
> _Originally posted by @JimmyLv in https://github.com/mattduck/gh2md/issues/11#issuecomment-693351490_

</br>

> @JimmyLv Yes, gh2md with python2 can not process issues with Chinese characters.
> Using python3 will solve this problem, see https://github.com/0ut0fcontrol/jimmylv.github.io/commit/76a967c741a2fa6fa1080c3b631228efe1205974.
> 
> I will update the example in this issue and create a  PR to modify [`issues2md.yml`](https://github.com/mattduck/gh2md/blob/master/.github/workflows/issues2md.yml) in `gh2md`.
> 
> _Originally posted by @0ut0fcontrol in https://github.com/mattduck/gh2md/issues/11#issuecomment-693768534_




-------------------------------------------------------------------------------

# [\#14 PR](https://github.com/mattduck/gh2md/pull/14) `closed`: git commit only if there are changes in issues.

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) opened issue at [2020-08-26 09:33](https://github.com/mattduck/gh2md/pull/14):

GitHub Actions failed for ["nothing to commit"](https://github.com/mattduck/gh2md/actions/runs/224515871).

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) commented at [2020-08-26 13:48](https://github.com/mattduck/gh2md/pull/14#issuecomment-680890979):

git commit only if there are changes in issues.
The Actions was [passed](https://github.com/0ut0fcontrol/gh2md/actions/runs/225121459) in my fork.
`git reset --hard` to https://github.com/mattduck/gh2md/pull/14/commits/5c6709d8cf45af07c15124cf3e08df0d27c4f2da to disable actions on `push` and remove `issues.md` from my fork.

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2020-08-31 09:25](https://github.com/mattduck/gh2md/pull/14#issuecomment-683670039):

@0ut0fcontrol thanks! I noticed this was failing a while back but hadn't had the chance to look at it.


-------------------------------------------------------------------------------

# [\#13 Issue](https://github.com/mattduck/gh2md/issues/13) `open`: Is possible to export each issue in a separated file?

#### <img src="https://avatars3.githubusercontent.com/u/12011070?v=4" width="50">[Guilherme Prokisch](https://github.com/guilhermeprokisch) opened issue at [2020-08-17 15:32](https://github.com/mattduck/gh2md/issues/13):

I want to export each issue in a separated file. It's possible to do?

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2020-08-31 09:29](https://github.com/mattduck/gh2md/issues/13#issuecomment-683671572):

That's not currently feature, but it wouldn't be a huge amount of work to implement. I'll try to get to it sometime, but realistically it's going to be at least a few weeks until I sit down to look at it.


-------------------------------------------------------------------------------

# [\#12 PR](https://github.com/mattduck/gh2md/pull/12) `closed`: Remove timestamp in github actions

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

#### <img src="https://avatars2.githubusercontent.com/u/1607892?v=4" width="50">[Matt Duck](https://github.com/mattduck) commented at [2020-08-16 10:21](https://github.com/mattduck/gh2md/pull/12#issuecomment-674508568):

@0ut0fcontrol thanks a lot! I've just published a new release that includes your fix for the rate limit AttributeError. Looks like it started occurring 12 days ago. The builds are passing again now :+1: 

I'm gonna close this PR - it didn't make sense for me to merge it as the actions file for this repo should probably still just do `pip install gh2md`.

#### <img src="https://avatars3.githubusercontent.com/u/11703338?v=4" width="50">[jcyang](https://github.com/0ut0fcontrol) commented at [2020-08-16 10:41](https://github.com/mattduck/gh2md/pull/12#issuecomment-674510249):

great! thank you!


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

