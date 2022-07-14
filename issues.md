Export of Github issues for [mattduck/gh2md](https://github.com/mattduck/gh2md).

# [\#36 Issue](https://github.com/mattduck/gh2md/issues/36) `open`: Exporting issues from multiple projects I own

#### <img src="https://avatars.githubusercontent.com/u/25888380?u=ab9e23b167de76c43234ab328f5debad103fdee1&v=4" width="50">[beansrowning](https://github.com/beansrowning) opened issue at [2022-07-13 18:04](https://github.com/mattduck/gh2md/issues/36):

This might be a silly thought, but I'm curious if there's a way to bulk-export all issues/PRs across all projects without explicitly naming them all. I figured it would be easy enough to enumerate them all and loop through each, but that would also require constant updating anytime I had a new repo.

Thanks!




-------------------------------------------------------------------------------

# [\#35 Issue](https://github.com/mattduck/gh2md/issues/35) `open`: download images to git

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-10 06:19](https://github.com/mattduck/gh2md/issues/35):

currently, images have no special handling
gh2md simply uses the original image source

ideally, the user can enable image scraping

* download the images to git
* rewrite the image urls to local paths

also allow special handling of "large" images

* dont download, keep original url (cache the url somewhere to avoid re-downloading)
* compress large JPEGs
* reduce large GIFs to the first frame image
* reduce large video files to a thumbnail image

example avatar

```md
<img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">
```

<img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">

example attachment

```md
<img src="https://user-images.githubusercontent.com/12958815/177718602-943af214-24be-4209-82cc-18e6fa5d04c1.jpg" title="Mephistopheles and Margaretta  19th-century wooden double sculpture" width="10%">
```

<img src="https://user-images.githubusercontent.com/12958815/177718602-943af214-24be-4209-82cc-18e6fa5d04c1.jpg" title="Mephistopheles and Margaretta  19th-century wooden double sculpture" width="10%">


dupe #28 says "completed" but its not






-------------------------------------------------------------------------------

# [\#34 Issue](https://github.com/mattduck/gh2md/issues/34) `open`: add --version command

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-08 17:13](https://github.com/mattduck/gh2md/issues/34):

expected:

```
gh2md --version

2.1.0
```





-------------------------------------------------------------------------------

# [\#33 Issue](https://github.com/mattduck/gh2md/issues/33) `open`: with --multiple-files, generate readme.md index file

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-08 08:22](https://github.com/mattduck/gh2md/issues/33):

for better navigation

navigating an anonymous file list like

```
2020-09-22.1.issue.closed.md
2020-09-22.2.issue.closed.md
2020-11-04.3.issue.closed.md
2021-07-31.4.issue.open.md
2022-05-31.7.issue.open.md
2022-06-01.8.issue.open.md
2022-06-05.9.issue.open.md
```

is not user friendly





-------------------------------------------------------------------------------

# [\#32 Issue](https://github.com/mattduck/gh2md/issues/32) `closed`: allow to disable the "Generated on" footer

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-08 07:46](https://github.com/mattduck/gh2md/issues/32):

... to reduce diff noise


#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) commented at [2022-07-08 07:51](https://github.com/mattduck/gh2md/issues/32#issuecomment-1178671501):

argh, sorry

```py
    if is_idempotent:
        datestring = ""
    else:
        datestring = " Generated on {}.".format(
            datetime.datetime.now().strftime("%Y.%m.%d at %H:%M:%S")
        )
```

```py
    parser.add_argument(
        "-I",
        "--idempotent",
        help="Remove non-deterministic values like timestamps. Two runs of gh2md will always produce the same result, as long as the Github data has not changed.",
        action="store_true",
        dest="is_idempotent",
    )
```


-------------------------------------------------------------------------------

# [\#31 PR](https://github.com/mattduck/gh2md/pull/31) `open`: fix: use recursive mkdir

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-08 07:42](https://github.com/mattduck/gh2md/pull/31):

error was

```
$ gh2md milahu/random archive/github/issues/ --multiple-files --file-extension .ghmd
[2022-07-08 07:36:26,970] [INFO] Creating output directory: archive/github/issues/
Traceback (most recent call last):
  File "/home/runner/.local/bin/gh2md", line 8, in <module>
    sys.exit(main())
  File "/home/runner/.local/lib/python3.8/site-packages/gh2md/gh2md.py", line 797, in main
    os.mkdir(args.output_path)
FileNotFoundError: [Errno 2] No such file or directory: 'archive/github/issues/'
```

workaround:

```
mkdir -p archive/github/issues/ || true
```





-------------------------------------------------------------------------------

# [\#30 PR](https://github.com/mattduck/gh2md/pull/30) `merged`: add option --file-extension

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-07 16:31](https://github.com/mattduck/gh2md/pull/30):

part of #29 

example use

```sh
#!/bin/sh
set -e

# get issues as gfm files
gh2md milahu/random issues/ --multiple-files --file-extension .gfm

# convert to md files
find issues/ -name '*.gfm' -type f | while read f
do
  b="${f%.*}"
  #mv -v "$b.md" "$b.gfm" # no longer needed with: --file-extension .gfm
  pandoc --verbose -f gfm+hard_line_breaks -t markdown_strict "$b.gfm" -o "$b.md"
done

# delete gfm files
find issues/ -name '*.gfm' -type f | xargs rm
```



#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2022-07-07 17:25](https://github.com/mattduck/gh2md/pull/30#issuecomment-1177965843):

@milahu thanks for this. Agree with your comment on the issue re: pandoc. Maybe gfm would have been a more sensible default at the start, but it makes sense to stick with md now for backwards compatibility. PR looks good - I'll merge it now and try to get a release out later.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2022-07-07 20:11](https://github.com/mattduck/gh2md/pull/30#issuecomment-1178170467):

@milahu released as 2.1.0. Thanks again!


-------------------------------------------------------------------------------

# [\#29 Issue](https://github.com/mattduck/gh2md/issues/29) `closed`: convert between markdown flavors

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) opened issue at [2022-07-07 15:35](https://github.com/mattduck/gh2md/issues/29):

github issues use a different markdown flavor than github tree

mostly: line breaks

github issues: hard linebreaks (github flavored markdown, GFM)
github tree: soft linebreaks (traditional markdown)

**details**

[Github markdown that respects newlines](https://stackoverflow.com/questions/51049503/github-markdown-that-respects-newlines)
[Re-add soft line breaks to GitHub-flavored-markdown](https://github.com/github-community/community/discussions/10981)
[Advanced post option to override markdown linebreak setting](https://meta.discourse.org/t/advanced-post-option-to-override-markdown-linebreak-setting/81722)



#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) commented at [2022-07-07 16:05](https://github.com/mattduck/gh2md/issues/29#issuecomment-1177857611):

closing: out of scope

this is a job for ...

pandoc: convert from github flavored markdown to traditional markdown

```
pandoc -f gfm+hard_line_breaks -t markdown_strict input.md -o output.md
```

```sh
find issues/ -type f | while read f
do
  b="${f%.*}"
  mv -v "$b.md" "$b.gfm"
  pandoc --verbose -f gfm+hard_line_breaks -t markdown_strict "$b.gfm" -o "$b.md"
done
```

ideally gh2md would produce `*.gfm` files

**details**

[pandoc manual: Markdown variants](https://pandoc.org/MANUAL%202.html#markdown-variants)
https://github.com/jgm/pandoc/issues/5195


-------------------------------------------------------------------------------

# [\#28 Issue](https://github.com/mattduck/gh2md/issues/28) `closed`: Images not downloaded in the markdown

#### <img src="https://avatars.githubusercontent.com/u/12879472?v=4" width="50">[working12](https://github.com/working12) opened issue at [2022-06-30 09:26](https://github.com/mattduck/gh2md/issues/28):

This should not be the normal behavior. Because images contain meaningful and contextual information which might be helpful. 




-------------------------------------------------------------------------------

# [\#27 PR](https://github.com/mattduck/gh2md/pull/27) `merged`: Fix issue comment createdAt.

#### <img src="https://avatars.githubusercontent.com/u/1851962?u=403b8e194c60fcd4b9c6e5b194a5f717e49f93f3&v=4" width="50">[galenhuntington](https://github.com/galenhuntington) opened issue at [2022-06-28 22:15](https://github.com/mattduck/gh2md/pull/27):

I was having a problem where all comments on an issue had the same timestamps.  So far as I can tell, this is just a simple (one-letter) bug.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2022-06-29 20:13](https://github.com/mattduck/gh2md/pull/27#issuecomment-1170450210):

@galenhuntington ah damn, thanks very much. This does look like an issue. Will sort out a release for this.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2022-06-29 20:46](https://github.com/mattduck/gh2md/pull/27#issuecomment-1170477409):

@galenhuntington confirmed it works and released as 2.0.1 - https://github.com/mattduck/gh2md/blob/master/CHANGELOG.md#201-2022-06-29 - thanks again


-------------------------------------------------------------------------------

# [\#26 Issue](https://github.com/mattduck/gh2md/issues/26) `open`: Can't fetch issues from public repo

#### <img src="https://avatars.githubusercontent.com/u/581023?u=2fa91b813ce6c1161a2337869a3ee0b3cc7ab755&v=4" width="50">[kirillt](https://github.com/kirillt) opened issue at [2022-03-29 07:40](https://github.com/mattduck/gh2md/issues/26):

```
[kirill@lenovo tmp]$ gh2md ethereum/EIPs --no-prs --multiple-files eips/
[2022-03-29 10:39:54,161] [INFO] Looking for token in file: /home/kirill/.config/gh2md/token
[2022-03-29 10:39:54,161] [INFO] Looking for token in file: /home/kirill/.github-token
[2022-03-29 10:39:54,161] [WARNING] No token found. Access to private repositories will fail
[2022-03-29 10:39:54,161] [INFO] Initiating fetch for repo: ethereum/EIPs
[2022-03-29 10:39:54,162] [WARNING] Exception response from request attempt 1
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/gh2md/gh2md.py", line 364, in _post
    resp = self._request_session().post(
  File "/usr/local/lib/python3.8/site-packages/gh2md/gh2md.py", line 350, in _request_session
    self._session.headers.update({"Authorization": "token " + self.token})
TypeError: can only concatenate str (not "NoneType") to str
[2022-03-29 10:39:57,592] [WARNING] Exception response from request attempt 2
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/gh2md/gh2md.py", line 367, in _post
    resp.raise_for_status()
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 960, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.github.com/graphql
[2022-03-29 10:40:00,595] [ERROR] Request failed multiple retries, returning empty data
[2022-03-29 10:40:00,595] [ERROR] Repository data missing in response, can't proceed
Traceback (most recent call last):
  File "/usr/local/bin/gh2md", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.8/site-packages/gh2md/gh2md.py", line 791, in main
    repo = gh.fetch_and_decode_repository(
  File "/usr/local/lib/python3.8/site-packages/gh2md/gh2md.py", line 566, in fetch_and_decode_repository
    repo_data = response["data"]["repository"]
KeyError: 'data'
```

#### <img src="https://avatars.githubusercontent.com/u/1917293?v=4" width="50">[ronna](https://github.com/ronna) commented at [2022-06-22 15:03](https://github.com/mattduck/gh2md/issues/26#issuecomment-1163225851):

Hi @kirillt 

You need to set the Github token even if you just want to pull public repos.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2022-06-29 20:18](https://github.com/mattduck/gh2md/issues/26#issuecomment-1170454551):

Thanks for raising - I can update the docs + error handling here to make this more explicit


-------------------------------------------------------------------------------

# [\#25 Issue](https://github.com/mattduck/gh2md/issues/25) `closed`: gh2.md 

#### <img src="https://avatars.githubusercontent.com/u/85598201?u=758cee632b0dd7923f7c80911547585258dd4fa7&v=4" width="50">[gifhuppp](https://github.com/gifhuppp) opened issue at [2021-12-03 08:35](https://github.com/mattduck/gh2md/issues/25):

# log:
...
Writing to file: issues.md
Github API rate limit: RateLimit(core=Rate(reset=2020-09-17 02:50:05, remaining=977, limit=1000))
Done.





-------------------------------------------------------------------------------

# [\#24 Issue](https://github.com/mattduck/gh2md/issues/24) `open`: Support `since` parameter

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) opened issue at [2021-10-03 14:44](https://github.com/mattduck/gh2md/issues/24):

You're forced to retrieve issues from the begin of time right now - it'd be useful to support `since`.

This exists on issues, but I couldn't see it for PRs when I looked quickly. So may need to be issues-only




-------------------------------------------------------------------------------

# [\#23 Issue](https://github.com/mattduck/gh2md/issues/23) `open`: Support asc/desc ordering in single-file export

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) opened issue at [2021-10-03 14:43](https://github.com/mattduck/gh2md/issues/23):

Currently the output for single-file export is always oldest-first.




-------------------------------------------------------------------------------

# [\#22 Issue](https://github.com/mattduck/gh2md/issues/22) `open`: Support issue timeline events + discussions

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) opened issue at [2021-10-03 14:41](https://github.com/mattduck/gh2md/issues/22):

I don't think either of these were available when I first wrote the script - would be handy to support them.




-------------------------------------------------------------------------------

# [\#21 Issue](https://github.com/mattduck/gh2md/issues/21) `closed`: Handle rate limiting

#### <img src="https://avatars.githubusercontent.com/u/14930?u=370d01da27accdfc747349b8cf799e6dd65174ef&v=4" width="50">[adunkman](https://github.com/adunkman) opened issue at [2021-09-08 15:10](https://github.com/mattduck/gh2md/issues/21):

I’m attempting to use `gh2md` to export 8,000+ issues in a GitHub Action, and as you can imagine, I’m hitting [GitHub’s rate limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting).

I don’t think there’s an easy fix here, but wanted to open an issue to discuss if anyone sees a potential path forward. 

The only potential solution I see is to monitor API rate limiting and slow down requests, but I can imagine that would get pretty tricky. 

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-09-12 16:54](https://github.com/mattduck/gh2md/issues/21#issuecomment-917671626):

Hey @adunkman, I see a couple of things we can do here:

- Right now we're iterating over the issues and making an additional request per issue to fetch the comments, which gets through the rate limit very quickly. It looks like it's possible to instead just fetch all the comments for the repository and then correlate them in the program (https://docs.github.com/en/rest/reference/issues#list-issue-comments-for-a-repository), which would reduce the number of requests significantly.

- We could also add support for the `since` parameter - so that rather than doing a full sync every run, you can incrementally store the issues that have changed since the last run, or you can just grab issues that have changed in the last N days.

- I can also look into the Github GraphQL API - curious if that provides a way to fetch the data more efficiently.

- Those changes _might_ be enough. If you have 8000 issues each with 10 comments and we're limited to 100 issues/comments per page, it'll be 80 requests for the issues and 800 requests for the comments. If the GITHUB_TOKEN rate limit is 1000/hour, then you might just be able to do it. And it should definitely be possible authenticating via Oauth (5000/hour).

- Regardless, we could catch rate limit exceptions and wait in the program. It looks like Github provides a reset timestamp, so we could wait until then before executing the next request. This should probably be an opt-in feature so that the program doesn't unexpectedly take hours to run. If the number of issues is particularly large there could still be problems running via Github actions - super quick searching for the maximum job timeout suggests it can only run for 6 hours?

I won't be able to look into this further this coming week, but I have some time off work next week so I should be able to get a few hours to work on it. Let me know if you think these changes sound viable. I've been meaning to look into the one-request-per-issue problem for a while so will at least fix that.

#### <img src="https://avatars.githubusercontent.com/u/14930?u=370d01da27accdfc747349b8cf799e6dd65174ef&v=4" width="50">[adunkman](https://github.com/adunkman) commented at [2021-09-22 16:08](https://github.com/mattduck/gh2md/issues/21#issuecomment-925072823):

I know things are stressful in the world these days, and if you’re taking time off, I hope you can use it to relax and recharge. If that’s this project, great! Otherwise, it’s on anyone to write up a PR; not your responsibility. 😄 

I ended up writing a quick app to handle this because the GraphQL endpoint was _significantly_ less expensive — for my needs, each query returns 100 issues with all of their attached metadata (comments, authors, labels, etc), and consumed 2 request tokens ([the GraphQL API uses a token calculation](https://docs.github.com/en/graphql/overview/resource-limitations) to enforce resource limits). 

For GitHub Actions, the rate limit is 1,000 REST requests or 1,000 GraphQL tokens, so that meant I was _well_ within the resource limits by switching to GraphQL — 2 tokens per GraphQL query handles repositories with up to 50,000 issues.

Here’s the GraphQL query I used: 

```graphql
query ($owner: String!, $repo: String!, $nextPageCursor: String) {
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
  repository(owner: $owner, name: $repo) {
    issues(first: 100, after: $nextPageCursor, orderBy: { field: CREATED_AT, direction: ASC }) {
      totalCount
      pageInfo {
        endCursor
        hasNextPage
      }
      nodes {
        number
        url
        title
        body
        closed
        closedAt
        createdAt
        author {
          login,
          url
        }
        labels(first: 100) {
          totalCount
          nodes {
            name
            url
          }
        }
        comments(first: 100) {
          totalCount
          nodes {
            body
            createdAt
            author {
              login,
              url
            }
          }
        }
      }
    }
  }
}
```

… and I called using TypeScript iteratively: 

```ts
const { repository, rateLimit } = await octokit.graphql(ISSUE_BATCH_QUERY, {
  owner,
  repo,
  nextPageCursor,
}) as IssueQueryResponse;

hasNextPage = repository.issues.pageInfo.hasNextPage;
nextPageCursor = repository.issues.pageInfo.endCursor;
```

#### <img src="https://avatars.githubusercontent.com/u/14930?u=370d01da27accdfc747349b8cf799e6dd65174ef&v=4" width="50">[adunkman](https://github.com/adunkman) commented at [2021-09-22 16:10](https://github.com/mattduck/gh2md/issues/21#issuecomment-925074417):

Oh — and I’m a GraphQL newbie, so I don’t really know if I wrote that query "the right way" — if anyone has a better suggestion, I’m all ears!

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-10-03 14:40](https://github.com/mattduck/gh2md/issues/21#issuecomment-932965020):

Hey @adunkman, thanks for that graphql example! I finally worked on this today and ported the API over - as you say it's way faster and significantly more efficient on rate limits than previously.

My approach was very similar to yours, except that I paginated both issues and PRs in the same query. And then at the end I looked for any issues/PRs that still had additional pages of comments to fetch, and retrieved those separately - which is the only approach I'm aware of for paginating with nested cursors.

There are definitely a few things we could do to make this better but this is a massive improvement and will make it usable for a lot more medium/large repos. Thanks for the report + thoughts.

Gonna close this but feel free to reopen


-------------------------------------------------------------------------------

# [\#20 PR](https://github.com/mattduck/gh2md/pull/20) `merged`: Return token after it's read. Fixes #19

#### <img src="https://avatars.githubusercontent.com/u/3582096?u=b68e38db376aa74cd8621e0b93d22ce54ad0aae5&v=4" width="50">[amalmurali47](https://github.com/amalmurali47) opened issue at [2021-07-17 07:57](https://github.com/mattduck/gh2md/pull/20):



#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-07-19 06:59](https://github.com/mattduck/gh2md/pull/20#issuecomment-882292350):

Damn - this repo needs a few more tests! Appreciate the fix, thanks. Will release a new version now.


-------------------------------------------------------------------------------

# [\#19 Issue](https://github.com/mattduck/gh2md/issues/19) `closed`: GitHub token is not read from paths

#### <img src="https://avatars.githubusercontent.com/u/3582096?u=b68e38db376aa74cd8621e0b93d22ce54ad0aae5&v=4" width="50">[amalmurali47](https://github.com/amalmurali47) opened issue at [2021-07-17 07:49](https://github.com/mattduck/gh2md/issues/19):

Running gh2md with the GitHub token in `~/.config/gh2md/token` produces the following:

```
[2021-07-17 13:09:24,333] [INFO] Looking for token in file: /home/user/.config/gh2md/token
[2021-07-17 13:09:24,333] [INFO] Using token from file: /home/user/.config/gh2md/token
[2021-07-17 13:09:24,333] [INFO] Looking for token in file: /home/user/.github-token
[2021-07-17 13:09:24,333] [WARNING] No token found. Access to private repositories will fail
```

The token is resolved in the following (in order):
- A `GITHUB_ACCESS_TOKEN` environment variable.
- `~/.config/gh2md/token`
- `~/.github-token`

The problem is that, when the token is read from either of the files, its value is not returned outside to the calling function. Here's the relevant piece of code:

```python
def get_environment_token():
    try:
        token = os.environ[ENV_GITHUB_TOKEN]
        logger.info("Using token from environment")
        return token
    except KeyError:
        for path in GITHUB_ACCESS_TOKEN_PATHS:
            logger.info(f"Looking for token in file: {path}")
            if os.path.exists(path):
                logger.info(f"Using token from file: {path}")
                with open(path, "r") as f:
                    token = f.read().strip()
```

The fix would be to return the `token` after `token = f.read().strip()`.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-07-19 07:11](https://github.com/mattduck/gh2md/issues/19#issuecomment-882300773):

Thanks for this - have merged the associated PR and released a new version 1.0.4.

#### <img src="https://avatars.githubusercontent.com/u/3582096?u=b68e38db376aa74cd8621e0b93d22ce54ad0aae5&v=4" width="50">[amalmurali47](https://github.com/amalmurali47) commented at [2021-07-19 12:20](https://github.com/mattduck/gh2md/issues/19#issuecomment-882503256):

@mattduck Awesome, thank you!


-------------------------------------------------------------------------------

# [\#18 Issue](https://github.com/mattduck/gh2md/issues/18) `closed`: Issue on macOS

#### <img src="https://avatars.githubusercontent.com/u/923008?u=b06824c35b9f9f68660e04c9ecd87bd5180cb09c&v=4" width="50">[nclm](https://github.com/nclm) opened issue at [2021-06-18 14:39](https://github.com/mattduck/gh2md/issues/18):

I tried using gh2md on the computer here at work (running macOS 11.1) and all I get is this:

```
nicolas@computer ~ % gh2md user/project issues.md --login user
Github password for user :
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/bin/gh2md", line 8, in <module>
    sys.exit(main())
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/gh2md/gh2md.py", line 41, in main
    fetch_repo_and_export_to_markdown(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/gh2md/gh2md.py", line 139, in fetch_repo_and_export_to_markdown
    repo, github_api = get_github_repo(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/gh2md/gh2md.py", line 286, in get_github_repo
    return gh_owner.get_repo(repo_name), gh
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/github/NamedUser.py", line 545, in get_repo
    headers, data = self._requester.requestJsonAndCheck(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/github/Requester.py", line 353, in requestJsonAndCheck
    return self.__check(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/github/Requester.py", line 378, in __check
    raise self.__createException(status, responseHeaders, output)
github.GithubException.UnknownObjectException: 404 {"message": "Not Found", "documentation_url": "https://docs.github.com/rest/reference/repos#get-a-repository"}
```
python --version is Python 2.7.16, python3 --version is Python 3.9.5.

Any idea of what is happening? Thanks!

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-06-25 08:02](https://github.com/mattduck/gh2md/issues/18#issuecomment-868304488):

@nclm hey, sorry for slow response here.

I need to look at this more but I was able to reproduce it on my account by trying to clone a private repository using password login. I'm pretty sure this is because it doesn't handle 2FA login properly right now, and so probably I get the 404 because I'm not authenticated.

Do you have 2FA on your account? If so you can pass in an access token using one of:

- The `--token` flag.
- A `GITHUB_ACCESS_TOKEN` environment variable.
- An API token stored in `~/.github-token`.

There are a couple of things I'll look at here:

1. 2FA login support
2. Better error handling to make it clear what's happening

If this is a public repo or you don't have 2FA on your account then let me know.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-06-27 14:21](https://github.com/mattduck/gh2md/issues/18#issuecomment-869171698):

@nclm OK I looked into this properly today. It turns out that Github no longer supports username + password login authentication, and the API is returning its standard 404 response that it gives when the user isn't authenticated (https://docs.github.com/en/rest/overview/other-authentication-methods#basic-authentication).

I haven't been super active maintaining this so had missed the news last year that they were removing this. Apologies.

If you use a personal access token with the "repo" scope it should work fine for private repositories.

I've just released a new version, and now token authentication is required (unless your repo is public, in which case you don't strictly need to authenticate).

Going to close this but LMK if you still have issues.


-------------------------------------------------------------------------------

# [\#17 Issue](https://github.com/mattduck/gh2md/issues/17) `closed`: UnicodeEncodeError: 'ascii' codec can't encode character

#### <img src="https://avatars.githubusercontent.com/u/7646335?u=aca4d581478f7a156c062e36130b55a776476727&v=4" width="50">[akiicat](https://github.com/akiicat) opened issue at [2020-12-31 08:18](https://github.com/mattduck/gh2md/issues/17):

**error log**

```
Traceback (most recent call last):
  File "/home/akiicat/.local/lib/python2.7/site-packages/gh2md/gh2md.py", line 196, in export_issues_to_markdown_file
    formatted_issue = process_issue_to_markdown(issue)
  File "/home/akiicat/.local/lib/python2.7/site-packages/retrying.py", line 49, in wrapped_f
    return Retrying(*dargs, **dkw).call(f, *args, **kw)
  File "/home/akiicat/.local/lib/python2.7/site-packages/retrying.py", line 212, in call
    raise attempt.get()
  File "/home/akiicat/.local/lib/python2.7/site-packages/retrying.py", line 247, in get
    six.reraise(self.value[0], self.value[1], self.value[2])
  File "/home/akiicat/.local/lib/python2.7/site-packages/retrying.py", line 200, in call
    attempt = Attempt(fn(*args, **kwargs), attempt_number, False)
  File "/home/akiicat/.local/lib/python2.7/site-packages/gh2md/gh2md.py", line 249, in process_issue_to_markdown
    body=comment.body,
UnicodeEncodeError: 'ascii' codec can't encode character u'\u2014' in position 173: ordinal not in range(128)
Couldn't process issue due to exceptions, skipping
```

It seems the string in [templates_markdown.py](https://github.com/mattduck/gh2md/blob/master/src/gh2md/templates_markdown.py#L18) file are not Unicode strings. One of my solutions is:

```diff
# src/gh2md/templates_markdown.py
- COMMENT = r"""#### <img src="{avatar_url}" width="50">[{author}]({author_url}) commented at [{date}]({url}):
+ COMMENT = ur"""#### <img src="{avatar_url}" width="50">[{author}]({author_url}) commented at [{date}]({url}):
```


#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-01-03 19:27](https://github.com/mattduck/gh2md/issues/17#issuecomment-753664999):

@akiicat thanks for reporting this. I'm hoping to release a version with the fix sometime this week.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-03-14 20:45](https://github.com/mattduck/gh2md/issues/17#issuecomment-798976684):

@akiicat I looked into this and had missed that you're running python 2.7. I wasn't able to reproduce the issue in the latest version. I'm going to close this but I'm happy to look at it if you can reproduce in python 3.


-------------------------------------------------------------------------------

# [\#16 PR](https://github.com/mattduck/gh2md/pull/16) `merged`: Create Markdown file even after abort

#### <img src="https://avatars.githubusercontent.com/u/14315968?u=b12eaa9a39c894eb22e2a785903240ecd6149e1e&v=4" width="50">[C0D3D3V](https://github.com/C0D3D3V) opened issue at [2020-10-21 08:28](https://github.com/mattduck/gh2md/pull/16):

I think it would be great if you can abort the whole process after a rate limit and still create the markdown file for the stuff that has already been downloaded.

Especially if you have already downloaded a few thousand entries this is very annoying.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-11-01 17:20](https://github.com/mattduck/gh2md/pull/16#issuecomment-720122042):

@C0D3D3V thanks a lot for this. Sorry it's taken ages to respond - have just been super busy elsewhere. I think this is a sensible step so I'm going to test it, merge it in and do a release. IIRC this is making an API request for each issue it fetches. It would be nice to batch up multiple issues in one call - I'll try to look into whether that's possible sometime.


-------------------------------------------------------------------------------

# [\#15 PR](https://github.com/mattduck/gh2md/pull/15) `merged`: Using python3 (pip3) in Github Actions.

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) opened issue at [2020-09-17 02:40](https://github.com/mattduck/gh2md/pull/15):

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

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-11-01 16:26](https://github.com/mattduck/gh2md/pull/15#issuecomment-720114072):

Hey, sorry it's taken forever to respond - have been super busy with things. This looks great, I'm merging now.


-------------------------------------------------------------------------------

# [\#14 PR](https://github.com/mattduck/gh2md/pull/14) `merged`: git commit only if there are changes in issues.

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) opened issue at [2020-08-26 09:33](https://github.com/mattduck/gh2md/pull/14):

GitHub Actions failed for ["nothing to commit"](https://github.com/mattduck/gh2md/actions/runs/224515871).

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) commented at [2020-08-26 13:48](https://github.com/mattduck/gh2md/pull/14#issuecomment-680890979):

git commit only if there are changes in issues.
The Actions was [passed](https://github.com/0ut0fcontrol/gh2md/actions/runs/225121459) in my fork.
`git reset --hard` to https://github.com/mattduck/gh2md/pull/14/commits/5c6709d8cf45af07c15124cf3e08df0d27c4f2da to disable actions on `push` and remove `issues.md` from my fork.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-08-31 09:25](https://github.com/mattduck/gh2md/pull/14#issuecomment-683670039):

@0ut0fcontrol thanks! I noticed this was failing a while back but hadn't had the chance to look at it.


-------------------------------------------------------------------------------

# [\#13 Issue](https://github.com/mattduck/gh2md/issues/13) `closed`: Is possible to export each issue in a separated file?

#### <img src="https://avatars.githubusercontent.com/u/12011070?u=f18e95eceaa97f69b9d0c5a06270d7bdfbc44b5a&v=4" width="50">[guilhermeprokisch](https://github.com/guilhermeprokisch) opened issue at [2020-08-17 15:32](https://github.com/mattduck/gh2md/issues/13):

I want to export each issue in a separated file. It's possible to do?

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-08-31 09:29](https://github.com/mattduck/gh2md/issues/13#issuecomment-683671572):

That's not currently feature, but it wouldn't be a huge amount of work to implement. I'll try to get to it sometime, but realistically it's going to be at least a few weeks until I sit down to look at it.

#### <img src="https://avatars.githubusercontent.com/u/10154151?u=ae4d6c769564ee187f10b7947a0f288b1b746e22&v=4" width="50">[lhoupert](https://github.com/lhoupert) commented at [2021-01-29 11:32](https://github.com/mattduck/gh2md/issues/13#issuecomment-769751066):

Hi there! 
I would also be really interested in this possibility. I am using github issues as get-things-done lists :-) and it would be great to be able to easily export each individual issue as a md file. 
I got the idea after reading this nice article (https://rabernat.medium.com/advising-and-collaborating-during-a-pandemic-and-sabbatical-ca9531b82b6d).

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2021-06-27 14:33](https://github.com/mattduck/gh2md/issues/13#issuecomment-869173434):

> it's going to be at least a few weeks until I sit down to look at it.

This was not a good estimate, my bad. Nearly a year late but I finally sat down and implemented multiple file support this morning.

Now if you pass the argument `--multiple-files`, your output path will be treated as a directory (instead of the default markdown file), and each issue/PR will be written to its own file, using the same formatting that it has when it's written to a single file. You can see an example of this at https://github.com/mattduck/gh2md/tree/master/examples/gh2md-multiple-files-example.

There is a new 1.0.1 release of gh2md that includes this feature. (It also removes support for user+password login as Github dropped supporting this a while back).

Hopefully this will be useful for somebody in the future. I'm going to close this as done but LMK if any feedback/issues.

#### <img src="https://avatars.githubusercontent.com/u/12011070?u=f18e95eceaa97f69b9d0c5a06270d7bdfbc44b5a&v=4" width="50">[guilhermeprokisch](https://github.com/guilhermeprokisch) commented at [2021-08-14 03:26](https://github.com/mattduck/gh2md/issues/13#issuecomment-898809516):

Thanks, @mattduck!


-------------------------------------------------------------------------------

# [\#12 PR](https://github.com/mattduck/gh2md/pull/12) `closed`: Remove timestamp in github actions

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) opened issue at [2020-08-11 07:23](https://github.com/mattduck/gh2md/pull/12):

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

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-08-16 10:21](https://github.com/mattduck/gh2md/pull/12#issuecomment-674508568):

@0ut0fcontrol thanks a lot! I've just published a new release that includes your fix for the rate limit AttributeError. Looks like it started occurring 12 days ago. The builds are passing again now :+1: 

I'm gonna close this PR - it didn't make sense for me to merge it as the actions file for this repo should probably still just do `pip install gh2md`.

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) commented at [2020-08-16 10:41](https://github.com/mattduck/gh2md/pull/12#issuecomment-674510249):

great! thank you!


-------------------------------------------------------------------------------

# [\#11 Issue](https://github.com/mattduck/gh2md/issues/11) `closed`: A github actions example to extract issues of the repo itself

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) opened issue at [2020-07-16 07:42](https://github.com/mattduck/gh2md/issues/11):

Thank you for your great work.

I add my github actions example here, in case someone needs it.

it backups all issues every day.

Because it only backup the issues belong to the repository that contains this workflow. It does not limit by the GitHub API rate.
```console
# gh2md log:
...
Writing to file: issues.md
Github API rate limit: RateLimit(core=Rate(reset=2020-09-17 02:50:05, remaining=977, limit=1000))
Done.
```


```yaml
# .github/workflows/issues2md.yml
name: Issues2Markdown
on:
  push: # comment it to reduce update.
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
        pip3 install --user --upgrade setuptools
        pip3 install --user gh2md
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

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-07-16 21:24](https://github.com/mattduck/gh2md/issues/11#issuecomment-659682052):

@0ut0fcontrol thanks for sharing this, it's super cool! I'll find somewhere sensible to publicise it - at least link to it from the README. I think I should set it up for gh2md itself.

I'm glad this is useful for you and still working OK. I haven't used it much recently, so I'm not sure if there are any problems or obvious features that would help - feel free to open issues if you do have anything.

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) commented at [2020-07-17 06:34](https://github.com/mattduck/gh2md/issues/11#issuecomment-659893686):

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

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-07-19 06:22](https://github.com/mattduck/gh2md/issues/11#issuecomment-660595381):

@0ut0fcontrol I've added this to the repo now - worked fine first time. Thanks again!

If I get some time soon, I'll add a flag to optionally remove the timestamp message in the file - this way you'll only get a commit if the content has changed, instead of a new commit on every run due to the unique timestamp.

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) commented at [2020-07-19 17:30](https://github.com/mattduck/gh2md/issues/11#issuecomment-660680186):

@mattduck Thank you.

It seems that `gh2md` doesn't download closed PR.
Is it an expected behavior?

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-07-19 19:59](https://github.com/mattduck/gh2md/issues/11#issuecomment-660699734):

@0ut0fcontrol I've just fixed that. Back when I wrote this I didn't need to export closed PRs, and for some reason instead of making it configurable I just hardcoded it.

I've updated the default behaviour to fetch everything by default. You can selectively disable parts with `--no-closed-prs`, `--no-closed-issues`, `--no-prs` or `--no-issues`.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-07-19 20:02](https://github.com/mattduck/gh2md/issues/11#issuecomment-660700176):

I'm gonna close this issue just so I know that there's no work to do on it. Will leave it pinned though.

#### <img src="https://avatars.githubusercontent.com/u/4997466?u=e4e91ddcfbdd81cf3de82b14b4a1728323ea771d&v=4" width="50">[JimmyLv](https://github.com/JimmyLv) commented at [2020-09-16 11:44](https://github.com/mattduck/gh2md/issues/11#issuecomment-693351490):

The workflow always has this issue, is that because I am using Chinese?

```
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)
```

#### <img src="https://avatars.githubusercontent.com/u/11703338?u=53d14d965e795c793b7e23f90932482ee2e3cafa&v=4" width="50">[0ut0fcontrol](https://github.com/0ut0fcontrol) commented at [2020-09-17 02:23](https://github.com/mattduck/gh2md/issues/11#issuecomment-693768534):

@JimmyLv Yes, gh2md with python2 can not process issues with Chinese characters.
Using python3 will solve this problem, see https://github.com/0ut0fcontrol/jimmylv.github.io/commit/76a967c741a2fa6fa1080c3b631228efe1205974.

I will update the example in this issue and create a  PR to modify [`issues2md.yml`](https://github.com/mattduck/gh2md/blob/master/.github/workflows/issues2md.yml) in `gh2md`.

#### <img src="https://avatars.githubusercontent.com/u/12958815?v=4" width="50">[milahu](https://github.com/milahu) commented at [2022-07-08 08:16](https://github.com/mattduck/gh2md/issues/11#issuecomment-1178695066):

my version of `.github/workflows/issues2md.yml` (used [here](https://github.com/milahu/alchi))

* use env `GITHUB_ACCESS_TOKEN`, option `--token` was removed
* set flag `--multiple-files` to produce one file per issue
* set flag `--idempotent` to reduce diff noise
* write output files to `archive/github/issues/`
* use pandoc to convert github-markdown to strict-markdown
  * github issue: github-markdown
  * github tree: strict-markdown
  * file extension .ghmd is not-yet supported in github tree
  * debian: pandoc 2.5 (old, bugs)
  * nix: pandoc 2.17

<details>

```yaml
# .github/workflows/issues2md.yml
# https://github.com/mattduck/gh2md/issues/11

name: Issues2Markdown
on:
  #push: # comment it to reduce update.
  schedule:
    # every day
    #- cron: "0 0 * * *"
    # every hour
    - cron: "0 * * * *"
jobs:
  build:
    name: Backup github issues to markdown files
    runs-on: ubuntu-latest
    steps:
    - name: Set output path
      run: echo "GH2MD_OUTPUT_PATH=archive/github/issues/" >> $GITHUB_ENV
    - name: Check output path
      run: |
        if ! [[ "$GH2MD_OUTPUT_PATH" =~ ^[a-zA-Z0-9_/.+~-]+$ ]]; then
          echo "error: output path does not match the pattern ^[a-zA-Z0-9_/.+~-]+$"
          exit 1
        fi
    - name: checkout
      uses: actions/checkout@master
      with:
        persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal token
        fetch-depth: 0 # otherwise, you will failed to push refs to dest repo
    - name: Run gh2md
      run: |
        pip3 install --user --upgrade setuptools
        pip3 install --user gh2md
        export PATH="$HOME/.local/bin:$PATH"
        gh2md --version || true
        export GITHUB_ACCESS_TOKEN=${{ secrets.GITHUB_TOKEN }}
        # fix: RuntimeError: Output directory already exists and has files in it
        git rm -rf $GH2MD_OUTPUT_PATH
        # workaround for https://github.com/mattduck/gh2md/pull/31
        mkdir -p $GH2MD_OUTPUT_PATH || true
        gh2md $GITHUB_REPOSITORY $GH2MD_OUTPUT_PATH --idempotent --multiple-files --file-extension .ghmd
        #sudo apt-get install pandoc # pandoc 2.5 == too old
    # install nix to install pandoc 2.17
    - name: install nix
      uses: cachix/install-nix-action@master
      with:
        nix_path: nixpkgs=channel:nixos-unstable
    - name: "pandoc: convert github-markdown to strict-markdown"
      uses: workflow/nix-shell-action@main
      with:
        packages: pandoc
        script: |
          set -x
          pandoc --version || true
          find $GH2MD_OUTPUT_PATH -name '*.ghmd' -type f | while read path
          do
            base="${path%.*}"
            pandoc --verbose -f gfm+hard_line_breaks -t markdown_strict "$base.ghmd" -o "$base.md"
          done
    - name: "cleanup: move .ghmd files to separate folder"
      run: |
        mkdir -p $GH2MD_OUTPUT_PATH/ghmd/
        mv -v $GH2MD_OUTPUT_PATH*.ghmd $GH2MD_OUTPUT_PATH/ghmd/
    - name: Commit files
      run: |
        git add $GH2MD_OUTPUT_PATH
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        if ! git commit -m "up $GH2MD_OUTPUT_PATH" -a
        then
          echo nothing to commit
          exit 0
        fi
    - name: Get branch name
      shell: bash
      run: echo "##[set-output name=branch;]$(echo ${GITHUB_REF#refs/heads/})"
      id: get_branch
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        branch: ${{ steps.get_branch.outputs.branch }}
```

</details>


-------------------------------------------------------------------------------

# [\#10 Issue](https://github.com/mattduck/gh2md/issues/10) `closed`: Wanna get closed issues

#### <img src="https://avatars.githubusercontent.com/u/6499816?u=5ffea385b5dd53ab6757460e4e538cbbc4602a34&v=4" width="50">[longwdl](https://github.com/longwdl) opened issue at [2017-06-12 08:09](https://github.com/mattduck/gh2md/issues/10):

Wanna get all issues at the same time.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2020-07-19 19:57](https://github.com/mattduck/gh2md/issues/10#issuecomment-660699450):

For anybody reading this years later: I finally did some work on this project again. By default it will now fetch all issues + PRs, and you can selectively disabled the parts you don't want using some new flags, eg. `--no-closed-prs`.

I actually think closed issues should have always worked, but closed PRs did not.

See the help text or README for more details.


-------------------------------------------------------------------------------

# [\#9 PR](https://github.com/mattduck/gh2md/pull/9) `closed`: Pin requests to latest version 2.14.2

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 15:03](https://github.com/mattduck/gh2md/pull/9):


requests is not pinned to a specific version.

I'm pinning it to the latest version **2.14.2** for now.


These links might come in handy:  <a href="https://pypi.python.org/pypi/requests">PyPI</a> | <a href="https://pyup.io/changelogs/requests/">Changelog</a> | <a href="http://python-requests.org">Homepage</a> 



### Changelog
> 
>### 2.14.2

>+++++++++++++++++++

>**Bugfixes**

>- Changed a less-than to an equal-to and an or in the dependency markers to
>  widen compatibility with older setuptools releases.



>### 2.14.1

>+++++++++++++++++++

>**Bugfixes**

>- Changed the dependency markers to widen compatibility with older pip
>  releases.



>### 2.14.0

>+++++++++++++++++++

>**Improvements**

>- It is now possible to pass ``no_proxy`` as a key to the ``proxies``
>  dictionary to provide handling similar to the ``NO_PROXY`` environment
>  variable.
>- When users provide invalid paths to certificate bundle files or directories
>  Requests now raises ``IOError``, rather than failing at the time of the HTTPS
>  request with a fairly inscrutable certificate validation error.
>- The behavior of ``SessionRedirectMixin`` was slightly altered.
>  ``resolve_redirects`` will now detect a redirect by calling
>  ``get_redirect_target(response)`` instead of directly
>  querying ``Response.is_redirect`` and ``Response.headers[&#39;location&#39;]``.
>  Advanced users will be able to process malformed redirects more easily.
>- Changed the internal calculation of elapsed request time to have higher
>  resolution on Windows.
>- Added ``win_inet_pton`` as conditional dependency for the ``[socks]`` extra
>  on Windows with Python 2.7.
>- Changed the proxy bypass implementation on Windows: the proxy bypass
>  check doesn&#39;t use forward and reverse DNS requests anymore
>- URLs with schemes that begin with ``http`` but are not ``http`` or ``https``
>  no longer have their host parts forced to lowercase.

>**Bugfixes**

>- Much improved handling of non-ASCII ``Location`` header values in redirects.
>  Fewer ``UnicodeDecodeError``s are encountered on Python 2, and Python 3 now
>  correctly understands that Latin-1 is unlikely to be the correct encoding.
>- If an attempt to ``seek`` file to find out its length fails, we now
>  appropriately handle that by aborting our content-length calculations.
>- Restricted ``HTTPDigestAuth`` to only respond to auth challenges made on 4XX
>  responses, rather than to all auth challenges.
>- Fixed some code that was firing ``DeprecationWarning`` on Python 3.6.
>- The dismayed person emoticon (``/o\\``) no longer has a big head. I&#39;m sure
>  this is what you were all worrying about most.


>**Miscellaneous**

>- Updated bundled urllib3 to v1.21.1.
>- Updated bundled chardet to v3.0.2.
>- Updated bundled idna to v2.5.
>- Updated bundled certifi to 2017.4.17.



>### 2.13.0

>+++++++++++++++++++

>**Features**

>- Only load the ``idna`` library when we&#39;ve determined we need it. This will
>  save some memory for users.

>**Miscellaneous**

>- Updated bundled urllib3 to 1.20.
>- Updated bundled idna to 2.2.



>### 2.12.5

>+++++++++++++++++++

>**Bugfixes**

>- Fixed an issue with JSON encoding detection, specifically detecting
>  big-endian UTF-32 with BOM.



>### 2.12.4

>+++++++++++++++++++

>**Bugfixes**

>- Fixed regression from 2.12.2 where non-string types were rejected in the
>  basic auth parameters. While support for this behaviour has been readded,
>  the behaviour is deprecated and will be removed in the future.



>### 2.12.3

>+++++++++++++++++++

>**Bugfixes**

>- Fixed regression from v2.12.1 for URLs with schemes that begin with &quot;http&quot;.
>  These URLs have historically been processed as though they were HTTP-schemed
>  URLs, and so have had parameters added. This was removed in v2.12.2 in an
>  overzealous attempt to resolve problems with IDNA-encoding those URLs. This
>  change was reverted: the other fixes for IDNA-encoding have been judged to
>  be sufficient to return to the behaviour Requests had before v2.12.0.



>### 2.12.2

>+++++++++++++++++++

>**Bugfixes**

>- Fixed several issues with IDNA-encoding URLs that are technically invalid but
>  which are widely accepted. Requests will now attempt to IDNA-encode a URL if
>  it can but, if it fails, and the host contains only ASCII characters, it will
>  be passed through optimistically. This will allow users to opt-in to using
>  IDNA2003 themselves if they want to, and will also allow technically invalid
>  but still common hostnames.
>- Fixed an issue where URLs with leading whitespace would raise
>  ``InvalidSchema`` errors.
>- Fixed an issue where some URLs without the HTTP or HTTPS schemes would still
>  have HTTP URL preparation applied to them.
>- Fixed an issue where Unicode strings could not be used in basic auth.
>- Fixed an issue encountered by some Requests plugins where constructing a
>  Response object would cause ``Response.content`` to raise an
>  ``AttributeError``.



>### 2.12.1

>+++++++++++++++++++

>**Bugfixes**

>- Updated setuptools &#39;security&#39; extra for the new PyOpenSSL backend in urllib3.

>**Miscellaneous**

>- Updated bundled urllib3 to 1.19.1.



>### 2.12.0

>+++++++++++++++++++

>**Improvements**

>- Updated support for internationalized domain names from IDNA2003 to IDNA2008.
>  This updated support is required for several forms of IDNs and is mandatory
>  for .de domains.
>- Much improved heuristics for guessing content lengths: Requests will no
>  longer read an entire ``StringIO`` into memory.
>- Much improved logic for recalculating ``Content-Length`` headers for
>  ``PreparedRequest`` objects.
>- Improved tolerance for file-like objects that have no ``tell`` method but
>  do have a ``seek`` method.
>- Anything that is a subclass of ``Mapping`` is now treated like a dictionary
>  by the ``data=`` keyword argument.
>- Requests now tolerates empty passwords in proxy credentials, rather than
>  stripping the credentials.
>- If a request is made with a file-like object as the body and that request is
>  redirected with a 307 or 308 status code, Requests will now attempt to
>  rewind the body object so it can be replayed.

>**Bugfixes**

>- When calling ``response.close``, the call to ``close`` will be propagated
>  through to non-urllib3 backends.
>- Fixed issue where the ``ALL_PROXY`` environment variable would be preferred
>  over scheme-specific variables like ``HTTP_PROXY``.
>- Fixed issue where non-UTF8 reason phrases got severely mangled by falling
>  back to decoding using ISO 8859-1 instead.
>- Fixed a bug where Requests would not correctly correlate cookies set when
>  using custom Host headers if those Host headers did not use the native
>  string type for the platform.

>**Miscellaneous**

>- Updated bundled urllib3 to 1.19.
>- Updated bundled certifi certs to 2016.09.26.



>### 2.11.1

>+++++++++++++++++++

>**Bugfixes**

>- Fixed a bug when using ``iter_content`` with ``decode_unicode=True`` for
>  streamed bodies would raise ``AttributeError``. This bug was introduced in
>  2.11.
>- Strip Content-Type and Transfer-Encoding headers from the header block when
>  following a redirect that transforms the verb from POST/PUT to GET.



>### 2.11.0

>+++++++++++++++++++

>**Improvements**

>- Added support for the ``ALL_PROXY`` environment variable.
>- Reject header values that contain leading whitespace or newline characters to
>  reduce risk of header smuggling.

>**Bugfixes**

>- Fixed occasional ``TypeError`` when attempting to decode a JSON response that
>  occurred in an error case. Now correctly returns a ``ValueError``.
>- Requests would incorrectly ignore a non-CIDR IP address in the ``NO_PROXY``
>  environment variables: Requests now treats it as a specific IP.
>- Fixed a bug when sending JSON data that could cause us to encounter obscure
>  OpenSSL errors in certain network conditions (yes, really).
>- Added type checks to ensure that ``iter_content`` only accepts integers and
>  ``None`` for chunk sizes.
>- Fixed issue where responses whose body had not been fully consumed would have
>  the underlying connection closed but not returned to the connection pool,
>  which could cause Requests to hang in situations where the ``HTTPAdapter``
>  had been configured to use a blocking connection pool.

>**Miscellaneous**

>- Updated bundled urllib3 to 1.16.
>- Some previous releases accidentally accepted non-strings as acceptable header values. This release does not.



>### 2.10.0

>+++++++++++++++++++

>**New Features**

>- SOCKS Proxy Support! (requires PySocks; ``$ pip install requests[socks]``)

>**Miscellaneous**

>- Updated bundled urllib3 to 1.15.1.



>### 2.9.2

>++++++++++++++++++

>**Improvements**

>- Change built-in CaseInsensitiveDict (used for headers) to use OrderedDict
>  as its underlying datastore.

>**Bugfixes**

>- Don&#39;t use redirect_cache if allow_redirects=False
>- When passed objects that throw exceptions from ``tell()``, send them via
>  chunked transfer encoding instead of failing.
>- Raise a ProxyError for proxy related connection issues.



>### 2.9.1

>++++++++++++++++++

>**Bugfixes**

>- Resolve regression introduced in 2.9.0 that made it impossible to send binary
>  strings as bodies in Python 3.
>- Fixed errors when calculating cookie expiration dates in certain locales.

>**Miscellaneous**

>- Updated bundled urllib3 to 1.13.1.



>### 2.9.0

>++++++++++++++++++

>**Minor Improvements** (Backwards compatible)

>- The ``verify`` keyword argument now supports being passed a path to a
>  directory of CA certificates, not just a single-file bundle.
>- Warnings are now emitted when sending files opened in text mode.
>- Added the 511 Network Authentication Required status code to the status code
>  registry.

>**Bugfixes**

>- For file-like objects that are not seeked to the very beginning, we now
>  send the content length for the number of bytes we will actually read, rather
>  than the total size of the file, allowing partial file uploads.
>- When uploading file-like objects, if they are empty or have no obvious
>  content length we set ``Transfer-Encoding: chunked`` rather than
>  ``Content-Length: 0``.
>- We correctly receive the response in buffered mode when uploading chunked
>  bodies.
>- We now handle being passed a query string as a bytestring on Python 3, by
>  decoding it as UTF-8.
>- Sessions are now closed in all cases (exceptional and not) when using the
>  functional API rather than leaking and waiting for the garbage collector to
>  clean them up.
>- Correctly handle digest auth headers with a malformed ``qop`` directive that
>  contains no token, by treating it the same as if no ``qop`` directive was
>  provided at all.
>- Minor performance improvements when removing specific cookies by name.

>**Miscellaneous**

>- Updated urllib3 to 1.13.



>### 2.8.1

>++++++++++++++++++

>**Bugfixes**

>- Update certificate bundle to match ``certifi`` 2015.9.6.2&#39;s weak certificate
>  bundle.
>- Fix a bug in 2.8.0 where requests would raise ``ConnectTimeout`` instead of
>  ``ConnectionError``
>- When using the PreparedRequest flow, requests will now correctly respect the
>  ``json`` parameter. Broken in 2.8.0.
>- When using the PreparedRequest flow, requests will now correctly handle a
>  Unicode-string method name on Python 2. Broken in 2.8.0.



>### 2.8.0

>++++++++++++++++++

>**Minor Improvements** (Backwards Compatible)

>- Requests now supports per-host proxies. This allows the ``proxies``
>  dictionary to have entries of the form
>  ``{&#39;&lt;scheme&gt;://&lt;hostname&gt;&#39;: &#39;&lt;proxy&gt;&#39;}``. Host-specific proxies will be used
>  in preference to the previously-supported scheme-specific ones, but the
>  previous syntax will continue to work.
>- ``Response.raise_for_status`` now prints the URL that failed as part of the
>  exception message.
>- ``requests.utils.get_netrc_auth`` now takes an ``raise_errors`` kwarg,
>  defaulting to ``False``. When ``True``, errors parsing ``.netrc`` files cause
>  exceptions to be thrown.
>- Change to bundled projects import logic to make it easier to unbundle
>  requests downstream.
>- Changed the default User-Agent string to avoid leaking data on Linux: now
>  contains only the requests version.

>**Bugfixes**

>- The ``json`` parameter to ``post()`` and friends will now only be used if
>  neither ``data`` nor ``files`` are present, consistent with the
>  documentation.
>- We now ignore empty fields in the ``NO_PROXY`` environment variable.
>- Fixed problem where ``httplib.BadStatusLine`` would get raised if combining
>  ``stream=True`` with ``contextlib.closing``.
>- Prevented bugs where we would attempt to return the same connection back to
>  the connection pool twice when sending a Chunked body.
>- Miscellaneous minor internal changes.
>- Digest Auth support is now thread safe.

>**Updates**

>- Updated urllib3 to 1.12.



>### 2.7.0

>++++++++++++++++++

>This is the first release that follows our new release process. For more, see
>`our documentation
>&lt;http://docs.python-requests.org/en/latest/community/release-process/&gt;`_.

>**Bugfixes**

>- Updated urllib3 to 1.10.4, resolving several bugs involving chunked transfer
>  encoding and response framing.



>### 2.6.2

>++++++++++++++++++

>**Bugfixes**

>- Fix regression where compressed data that was sent as chunked data was not
>  properly decompressed. (2561)



>### 2.6.1

>++++++++++++++++++

>**Bugfixes**

>- Remove VendorAlias import machinery introduced in v2.5.2.

>- Simplify the PreparedRequest.prepare API: We no longer require the user to
>  pass an empty list to the hooks keyword argument. (c.f. 2552)

>- Resolve redirects now receives and forwards all of the original arguments to
>  the adapter. (2503)

>- Handle UnicodeDecodeErrors when trying to deal with a unicode URL that
>  cannot be encoded in ASCII. (2540)

>- Populate the parsed path of the URI field when performing Digest
>  Authentication. (2426)

>- Copy a PreparedRequest&#39;s CookieJar more reliably when it is not an instance
>  of RequestsCookieJar. (2527)



>### 2.6.0

>++++++++++++++++++

>**Bugfixes**

>- CVE-2015-2296: Fix handling of cookies on redirect. Previously a cookie
>  without a host value set would use the hostname for the redirected URL
>  exposing requests users to session fixation attacks and potentially cookie
>  stealing. This was disclosed privately by Matthew Daley of
>  `BugFuzz &lt;https://bugfuzz.com&gt;`_. This affects all versions of requests from
>  v2.1.0 to v2.5.3 (inclusive on both ends).

>- Fix error when requests is an ``install_requires`` dependency and ``python
>  setup.py test`` is run. (2462)

>- Fix error when urllib3 is unbundled and requests continues to use the
>  vendored import location.

>- Include fixes to ``urllib3``&#39;s header handling.

>- Requests&#39; handling of unvendored dependencies is now more restrictive.

>**Features and Improvements**

>- Support bytearrays when passed as parameters in the ``files`` argument.
>  (2468)

>- Avoid data duplication when creating a request with ``str``, ``bytes``, or
>  ``bytearray`` input to the ``files`` argument.



>### 2.5.3

>++++++++++++++++++

>**Bugfixes**

>- Revert changes to our vendored certificate bundle. For more context see
>  (2455, 2456, and http://bugs.python.org/issue23476)



>### 2.5.2

>++++++++++++++++++

>**Features and Improvements**

>- Add sha256 fingerprint support. (`shazow/urllib3540`_)

>- Improve the performance of headers. (`shazow/urllib3544`_)

>**Bugfixes**

>- Copy pip&#39;s import machinery. When downstream redistributors remove
>  requests.packages.urllib3 the import machinery will continue to let those
>  same symbols work. Example usage in requests&#39; documentation and 3rd-party
>  libraries relying on the vendored copies of urllib3 will work without having
>  to fallback to the system urllib3.

>- Attempt to quote parts of the URL on redirect if unquoting and then quoting
>  fails. (2356)

>- Fix filename type check for multipart form-data uploads. (2411)

>- Properly handle the case where a server issuing digest authentication
>  challenges provides both auth and auth-int qop-values. (2408)

>- Fix a socket leak. (`shazow/urllib3549`_)

>- Fix multiple ``Set-Cookie`` headers properly. (`shazow/urllib3534`_)

>- Disable the built-in hostname verification. (`shazow/urllib3526`_)

>- Fix the behaviour of decoding an exhausted stream. (`shazow/urllib3535`_)

>**Security**

>- Pulled in an updated ``cacert.pem``.

>- Drop RC4 from the default cipher list. (`shazow/urllib3551`_)

>.. _shazow/urllib3551: https://github.com/shazow/urllib3/pull/551
>.. _shazow/urllib3549: https://github.com/shazow/urllib3/pull/549
>.. _shazow/urllib3544: https://github.com/shazow/urllib3/pull/544
>.. _shazow/urllib3540: https://github.com/shazow/urllib3/pull/540
>.. _shazow/urllib3535: https://github.com/shazow/urllib3/pull/535
>.. _shazow/urllib3534: https://github.com/shazow/urllib3/pull/534
>.. _shazow/urllib3526: https://github.com/shazow/urllib3/pull/526



>### 2.5.1

>++++++++++++++++++

>**Behavioural Changes**

>- Only catch HTTPErrors in raise_for_status (2382)

>**Bugfixes**

>- Handle LocationParseError from urllib3 (2344)
>- Handle file-like object filenames that are not strings (2379)
>- Unbreak HTTPDigestAuth handler. Allow new nonces to be negotiated (2389)



>### 2.5.0

>++++++++++++++++++

>**Improvements**

>- Allow usage of urllib3&#39;s Retry object with HTTPAdapters (2216)
>- The ``iter_lines`` method on a response now accepts a delimiter with which
>  to split the content (2295)

>**Behavioural Changes**

>- Add deprecation warnings to functions in requests.utils that will be removed
>  in 3.0 (2309)
>- Sessions used by the functional API are always closed (2326)
>- Restrict requests to HTTP/1.1 and HTTP/1.0 (stop accepting HTTP/0.9) (2323)

>**Bugfixes**

>- Only parse the URL once (2353)
>- Allow Content-Length header to always be overridden (2332)
>- Properly handle files in HTTPDigestAuth (2333)
>- Cap redirect_cache size to prevent memory abuse (2299)
>- Fix HTTPDigestAuth handling of redirects after authenticating successfully
>  (2253)
>- Fix crash with custom method parameter to Session.request (2317)
>- Fix how Link headers are parsed using the regular expression library (2271)

>**Documentation**

>- Add more references for interlinking (2348)
>- Update CSS for theme (2290)
>- Update width of buttons and sidebar (2289)
>- Replace references of Gittip with Gratipay (2282)
>- Add link to changelog in sidebar (2273)



>### 2.4.3

>++++++++++++++++++

>**Bugfixes**

>- Unicode URL improvements for Python 2.
>- Re-order JSON param for backwards compat.
>- Automatically defrag authentication schemes from host/pass URIs. (`2249 &lt;https://github.com/kennethreitz/requests/issues/2249&gt;`_)




>### 2.4.2

>++++++++++++++++++

>**Improvements**

>- FINALLY! Add json parameter for uploads! (`2258 &lt;https://github.com/kennethreitz/requests/pull/2258&gt;`_)
>- Support for bytestring URLs on Python 3.x (`2238 &lt;https://github.com/kennethreitz/requests/pull/2238&gt;`_)

>**Bugfixes**

>- Avoid getting stuck in a loop (`2244 &lt;https://github.com/kennethreitz/requests/pull/2244&gt;`_)
>- Multiple calls to iter* fail with unhelpful error. (`2240 &lt;https://github.com/kennethreitz/requests/issues/2240&gt;`_, `2241 &lt;https://github.com/kennethreitz/requests/issues/2241&gt;`_)

>**Documentation**

>- Correct redirection introduction (`2245 &lt;https://github.com/kennethreitz/requests/pull/2245/&gt;`_)
>- Added example of how to send multiple files in one request. (`2227 &lt;https://github.com/kennethreitz/requests/pull/2227/&gt;`_)
>- Clarify how to pass a custom set of CAs (`2248 &lt;https://github.com/kennethreitz/requests/pull/2248/&gt;`_)





>### 2.4.1

>++++++++++++++++++

>- Now has a &quot;security&quot; package extras set, ``$ pip install requests[security]``
>- Requests will now use Certifi if it is available.
>- Capture and re-raise urllib3 ProtocolError
>- Bugfix for responses that attempt to redirect to themselves forever (wtf?).




>### 2.4.0

>++++++++++++++++++

>**Behavioral Changes**

>- ``Connection: keep-alive`` header is now sent automatically.

>**Improvements**

>- Support for connect timeouts! Timeout now accepts a tuple (connect, read) which is used to set individual connect and read timeouts.
>- Allow copying of PreparedRequests without headers/cookies.
>- Updated bundled urllib3 version.
>- Refactored settings loading from environment -- new `Session.merge_environment_settings`.
>- Handle socket errors in iter_content.




>### 2.3.0

>++++++++++++++++++

>**API Changes**

>- New ``Response`` property ``is_redirect``, which is true when the
>  library could have processed this response as a redirection (whether
>  or not it actually did).
>- The ``timeout`` parameter now affects requests with both ``stream=True`` and
>  ``stream=False`` equally.
>- The change in v2.0.0 to mandate explicit proxy schemes has been reverted.
>  Proxy schemes now default to ``http://``.
>- The ``CaseInsensitiveDict`` used for HTTP headers now behaves like a normal
>  dictionary when references as string or viewed in the interpreter.

>**Bugfixes**

>- No longer expose Authorization or Proxy-Authorization headers on redirect.
>  Fix CVE-2014-1829 and CVE-2014-1830 respectively.
>- Authorization is re-evaluated each redirect.
>- On redirect, pass url as native strings.
>- Fall-back to autodetected encoding for JSON when Unicode detection fails.
>- Headers set to ``None`` on the ``Session`` are now correctly not sent.
>- Correctly honor ``decode_unicode`` even if it wasn&#39;t used earlier in the same
>  response.
>- Stop advertising ``compress`` as a supported Content-Encoding.
>- The ``Response.history`` parameter is now always a list.
>- Many, many ``urllib3`` bugfixes.



>### 2.2.1

>++++++++++++++++++

>**Bugfixes**

>- Fixes incorrect parsing of proxy credentials that contain a literal or encoded &#39;&#39; character.
>- Assorted urllib3 fixes.



>### 2.2.0

>++++++++++++++++++

>**API Changes**

>- New exception: ``ContentDecodingError``. Raised instead of ``urllib3``
>  ``DecodeError`` exceptions.

>**Bugfixes**

>- Avoid many many exceptions from the buggy implementation of ``proxy_bypass`` on OS X in Python 2.6.
>- Avoid crashing when attempting to get authentication credentials from ~/.netrc when running as a user without a home directory.
>- Use the correct pool size for pools of connections to proxies.
>- Fix iteration of ``CookieJar`` objects.
>- Ensure that cookies are persisted over redirect.
>- Switch back to using chardet, since it has merged with charade.



>### 2.1.0

>++++++++++++++++++

>- Updated CA Bundle, of course.
>- Cookies set on individual Requests through a ``Session`` (e.g. via ``Session.get()``) are no longer persisted to the ``Session``.
>- Clean up connections when we hit problems during chunked upload, rather than leaking them.
>- Return connections to the pool when a chunked upload is successful, rather than leaking it.
>- Match the HTTPbis recommendation for HTTP 301 redirects.
>- Prevent hanging when using streaming uploads and Digest Auth when a 401 is received.
>- Values of headers set by Requests are now always the native string type.
>- Fix previously broken SNI support.
>- Fix accessing HTTP proxies using proxy authentication.
>- Unencode HTTP Basic usernames and passwords extracted from URLs.
>- Support for IP address ranges for no_proxy environment variable
>- Parse headers correctly when users override the default ``Host:`` header.
>- Avoid munging the URL in case of case-sensitive servers.
>- Looser URL handling for non-HTTP/HTTPS urls.
>- Accept unicode methods in Python 2.6 and 2.7.
>- More resilient cookie handling.
>- Make ``Response`` objects pickleable.
>- Actually added MD5-sess to Digest Auth instead of pretending to like last time.
>- Updated internal urllib3.
>- Fixed Lukasa&#39;s lack of taste.



>### 2.0.1

>++++++++++++++++++

>- Updated included CA Bundle with new mistrusts and automated process for the future
>- Added MD5-sess to Digest Auth
>- Accept per-file headers in multipart file POST messages.
>- Fixed: Don&#39;t send the full URL on CONNECT messages.
>- Fixed: Correctly lowercase a redirect scheme.
>- Fixed: Cookies not persisted when set via functional API.
>- Fixed: Translate urllib3 ProxyError into a requests ProxyError derived from ConnectionError.
>- Updated internal urllib3 and chardet.



>### 2.0.0

>++++++++++++++++++

>**API Changes:**

>- Keys in the Headers dictionary are now native strings on all Python versions,
>  i.e. bytestrings on Python 2, unicode on Python 3.
>- Proxy URLs now *must* have an explicit scheme. A ``MissingSchema`` exception
>  will be raised if they don&#39;t.
>- Timeouts now apply to read time if ``Stream=False``.
>- ``RequestException`` is now a subclass of ``IOError``, not ``RuntimeError``.
>- Added new method to ``PreparedRequest`` objects: ``PreparedRequest.copy()``.
>- Added new method to ``Session`` objects: ``Session.update_request()``. This
>  method updates a ``Request`` object with the data (e.g. cookies) stored on
>  the ``Session``.
>- Added new method to ``Session`` objects: ``Session.prepare_request()``. This
>  method updates and prepares a ``Request`` object, and returns the
>  corresponding ``PreparedRequest`` object.
>- Added new method to ``HTTPAdapter`` objects: ``HTTPAdapter.proxy_headers()``.
>  This should not be called directly, but improves the subclass interface.
>- ``httplib.IncompleteRead`` exceptions caused by incorrect chunked encoding
>  will now raise a Requests ``ChunkedEncodingError`` instead.
>- Invalid percent-escape sequences now cause a Requests ``InvalidURL``
>  exception to be raised.
>- HTTP 208 no longer uses reason phrase ``&quot;im_used&quot;``. Correctly uses
>  ``&quot;already_reported&quot;``.
>- HTTP 226 reason added (``&quot;im_used&quot;``).

>**Bugfixes:**

>- Vastly improved proxy support, including the CONNECT verb. Special thanks to
>  the many contributors who worked towards this improvement.
>- Cookies are now properly managed when 401 authentication responses are
>  received.
>- Chunked encoding fixes.
>- Support for mixed case schemes.
>- Better handling of streaming downloads.
>- Retrieve environment proxies from more locations.
>- Minor cookies fixes.
>- Improved redirect behaviour.
>- Improved streaming behaviour, particularly for compressed data.
>- Miscellaneous small Python 3 text encoding bugs.
>- ``.netrc`` no longer overrides explicit auth.
>- Cookies set by hooks are now correctly persisted on Sessions.
>- Fix problem with cookies that specify port numbers in their host field.
>- ``BytesIO`` can be used to perform streaming uploads.
>- More generous parsing of the ``no_proxy`` environment variable.
>- Non-string objects can be passed in data values alongside files.



>### 1.2.3

>++++++++++++++++++

>- Simple packaging fix




>### 1.2.2

>++++++++++++++++++

>- Simple packaging fix




>### 1.2.1

>++++++++++++++++++

>- 301 and 302 redirects now change the verb to GET for all verbs, not just
>  POST, improving browser compatibility.
>- Python 3.3.2 compatibility
>- Always percent-encode location headers
>- Fix connection adapter matching to be most-specific first
>- new argument to the default connection adapter for passing a block argument
>- prevent a KeyError when there&#39;s no link headers



>### 1.2.0

>++++++++++++++++++

>- Fixed cookies on sessions and on requests
>- Significantly change how hooks are dispatched - hooks now receive all the
>  arguments specified by the user when making a request so hooks can make a
>  secondary request with the same parameters. This is especially necessary for
>  authentication handler authors
>- certifi support was removed
>- Fixed bug where using OAuth 1 with body ``signature_type`` sent no data
>- Major proxy work thanks to Lukasa including parsing of proxy authentication
>  from the proxy url
>- Fix DigestAuth handling too many 401s
>- Update vendored urllib3 to include SSL bug fixes
>- Allow keyword arguments to be passed to ``json.loads()`` via the
>  ``Response.json()`` method
>- Don&#39;t send ``Content-Length`` header by default on ``GET`` or ``HEAD``
>  requests
>- Add ``elapsed`` attribute to ``Response`` objects to time how long a request
>  took.
>- Fix ``RequestsCookieJar``
>- Sessions and Adapters are now picklable, i.e., can be used with the
>  multiprocessing library
>- Update charade to version 1.0.3

>The change in how hooks are dispatched will likely cause a great deal of
>issues.



>### 1.1.0

>++++++++++++++++++

>- CHUNKED REQUESTS
>- Support for iterable response bodies
>- Assume servers persist redirect params
>- Allow explicit content types to be specified for file data
>- Make merge_kwargs case-insensitive when looking up keys



>### 1.0.3

>++++++++++++++++++

>- Fix file upload encoding bug
>- Fix cookie behavior



>### 1.0.2

>++++++++++++++++++

>- Proxy fix for HTTPAdapter.



>### 1.0.1

>++++++++++++++++++

>- Cert verification exception bug.
>- Proxy fix for HTTPAdapter.



>### 1.0.0

>++++++++++++++++++

>- Massive Refactor and Simplification
>- Switch to Apache 2.0 license
>- Swappable Connection Adapters
>- Mountable Connection Adapters
>- Mutable ProcessedRequest chain
>- /s/prefetch/stream
>- Removal of all configuration
>- Standard library logging
>- Make Response.json() callable, not property.
>- Usage of new charade project, which provides python 2 and 3 simultaneous chardet.
>- Removal of all hooks except &#39;response&#39;
>- Removal of all authentication helpers (OAuth, Kerberos)

>This is not a backwards compatible change.



>### 0.14.2

>+++++++++++++++++++

>- Improved mime-compatible JSON handling
>- Proxy fixes
>- Path hack fixes
>- Case-Insensitive Content-Encoding headers
>- Support for CJK parameters in form posts




>### 0.14.1

>+++++++++++++++++++

>- Python 3.3 Compatibility
>- Simply default accept-encoding
>- Bugfixes




>### 0.14.0

>++++++++++++++++++++

>- No more iter_content errors if already downloaded.



>### 0.13.9

>+++++++++++++++++++

>- Fix for OAuth + POSTs
>- Remove exception eating from dispatch_hook
>- General bugfixes



>### 0.13.8

>+++++++++++++++++++

>- Incredible Link header support :)



>### 0.13.7

>+++++++++++++++++++

>- Support for (key, value) lists everywhere.
>- Digest Authentication improvements.
>- Ensure proxy exclusions work properly.
>- Clearer UnicodeError exceptions.
>- Automatic casting of URLs to strings (fURL and such)
>- Bugfixes.



>### 0.13.6

>+++++++++++++++++++

>- Long awaited fix for hanging connections!



>### 0.13.5

>+++++++++++++++++++

>- Packaging fix



>### 0.13.4

>+++++++++++++++++++

>- GSSAPI/Kerberos authentication!
>- App Engine 2.7 Fixes!
>- Fix leaking connections (from urllib3 update)
>- OAuthlib path hack fix
>- OAuthlib URL parameters fix.



>### 0.13.3

>+++++++++++++++++++

>- Use simplejson if available.
>- Do not hide SSLErrors behind Timeouts.
>- Fixed param handling with urls containing fragments.
>- Significantly improved information in User Agent.
>- client certificates are ignored when verify=False



>### 0.13.2

>+++++++++++++++++++

>- Zero dependencies (once again)!
>- New: Response.reason
>- Sign querystring parameters in OAuth 1.0
>- Client certificates no longer ignored when verify=False
>- Add openSUSE certificate support



>### 0.13.1

>+++++++++++++++++++

>- Allow passing a file or file-like object as data.
>- Allow hooks to return responses that indicate errors.
>- Fix Response.text and Response.json for body-less responses.



>### 0.13.0

>+++++++++++++++++++

>- Removal of Requests.async in favor of `grequests &lt;https://github.com/kennethreitz/grequests&gt;`_
>- Allow disabling of cookie persistence.
>- New implementation of safe_mode
>- cookies.get now supports default argument
>- Session cookies not saved when Session.request is called with return_response=False
>- Env: no_proxy support.
>- RequestsCookieJar improvements.
>- Various bug fixes.



>### 0.12.1

>+++++++++++++++++++

>- New ``Response.json`` property.
>- Ability to add string file uploads.
>- Fix out-of-range issue with iter_lines.
>- Fix iter_content default size.
>- Fix POST redirects containing files.



>### 0.12.0

>+++++++++++++++++++

>- EXPERIMENTAL OAUTH SUPPORT!
>- Proper CookieJar-backed cookies interface with awesome dict-like interface.
>- Speed fix for non-iterated content chunks.
>- Move ``pre_request`` to a more usable place.
>- New ``pre_send`` hook.
>- Lazily encode data, params, files.
>- Load system Certificate Bundle if ``certify`` isn&#39;t available.
>- Cleanups, fixes.



>### 0.11.2

>+++++++++++++++++++

>- Attempt to use the OS&#39;s certificate bundle if ``certifi`` isn&#39;t available.
>- Infinite digest auth redirect fix.
>- Multi-part file upload improvements.
>- Fix decoding of invalid %encodings in URLs.
>- If there is no content in a response don&#39;t throw an error the second time that content is attempted to be read.
>- Upload data on redirects.



>### 0.11.1

>+++++++++++++++++++

>* POST redirects now break RFC to do what browsers do: Follow up with a GET.
>* New ``strict_mode`` configuration to disable new redirect behavior.




>### 0.11.0

>+++++++++++++++++++

>* Private SSL Certificate support
>* Remove select.poll from Gevent monkeypatching
>* Remove redundant generator for chunked transfer encoding
>* Fix: Response.ok raises Timeout Exception in safe_mode



>### 0.10.8

>+++++++++++++++++++

>* Generate chunked ValueError fix
>* Proxy configuration by environment variables
>* Simplification of iter_lines.
>* New `trust_env` configuration for disabling system/environment hints.
>* Suppress cookie errors.



>### 0.10.7

>+++++++++++++++++++

>* `encode_uri` = False



>### 0.10.6

>+++++++++++++++++++

>* Allow &#39;=&#39; in cookies.



>### 0.10.5

>+++++++++++++++++++

>* Response body with 0 content-length fix.
>* New async.imap.
>* Don&#39;t fail on netrc.




>### 0.10.4

>+++++++++++++++++++

>* Honor netrc.



>### 0.10.3

>+++++++++++++++++++

>* HEAD requests don&#39;t follow redirects anymore.
>* raise_for_status() doesn&#39;t raise for 3xx anymore.
>* Make Session objects picklable.
>* ValueError for invalid schema URLs.



>### 0.10.2

>+++++++++++++++++++

>* Vastly improved URL quoting.
>* Additional allowed cookie key values.
>* Attempted fix for &quot;Too many open files&quot; Error
>* Replace unicode errors on first pass, no need for second pass.
>* Append &#39;/&#39; to bare-domain urls before query insertion.
>* Exceptions now inherit from RuntimeError.
>* Binary uploads + auth fix.
>* Bugfixes.




>### 0.10.1

>+++++++++++++++++++

>* PYTHON 3 SUPPORT!
>* Dropped 2.5 Support. (*Backwards Incompatible*)



>### 0.10.0

>+++++++++++++++++++

>* ``Response.content`` is now bytes-only. (*Backwards Incompatible*)
>* New ``Response.text`` is unicode-only.
>* If no ``Response.encoding`` is specified and ``chardet`` is available, ``Response.text`` will guess an encoding.
>* Default to ISO-8859-1 (Western) encoding for &quot;text&quot; subtypes.
>* Removal of `decode_unicode`. (*Backwards Incompatible*)
>* New multiple-hooks system.
>* New ``Response.register_hook`` for registering hooks within the pipeline.
>* ``Response.url`` is now Unicode.



>### 0.9.3

>++++++++++++++++++

>* SSL verify=False bugfix (apparent on windows machines).



>### 0.9.2

>++++++++++++++++++

>* Asynchronous async.send method.
>* Support for proper chunk streams with boundaries.
>* session argument for Session classes.
>* Print entire hook tracebacks, not just exception instance.
>* Fix response.iter_lines from pending next line.
>* Fix but in HTTP-digest auth w/ URI having query strings.
>* Fix in Event Hooks section.
>* Urllib3 update.




>### 0.9.1

>++++++++++++++++++

>* danger_mode for automatic Response.raise_for_status()
>* Response.iter_lines refactor



>### 0.9.0

>++++++++++++++++++

>* verify ssl is default.




>### 0.8.9

>++++++++++++++++++

>* Packaging fix.




>### 0.8.8

>++++++++++++++++++

>* SSL CERT VERIFICATION!
>* Release of Cerifi: Mozilla&#39;s cert list.
>* New &#39;verify&#39; argument for SSL requests.
>* Urllib3 update.



>### 0.8.7

>++++++++++++++++++

>* iter_lines last-line truncation fix
>* Force safe_mode for async requests
>* Handle safe_mode exceptions more consistently
>* Fix iteration on null responses in safe_mode



>### 0.8.6

>++++++++++++++++++

>* Socket timeout fixes.
>* Proxy Authorization support.



>### 0.8.5

>++++++++++++++++++

>* Response.iter_lines!



>### 0.8.4

>++++++++++++++++++

>* Prefetch bugfix.
>* Added license to installed version.



>### 0.8.3

>++++++++++++++++++

>* Converted auth system to use simpler callable objects.
>* New session parameter to API methods.
>* Display full URL while logging.



>### 0.8.2

>++++++++++++++++++

>* New Unicode decoding system, based on over-ridable `Response.encoding`.
>* Proper URL slash-quote handling.
>* Cookies with ``[``, ``]``, and ``_`` allowed.



>### 0.8.1

>++++++++++++++++++

>* URL Request path fix
>* Proxy fix.
>* Timeouts fix.



>### 0.8.0

>++++++++++++++++++

>* Keep-alive support!
>* Complete removal of Urllib2
>* Complete removal of Poster
>* Complete removal of CookieJars
>* New ConnectionError raising
>* Safe_mode for error catching
>* prefetch parameter for request methods
>* OPTION method
>* Async pool size throttling
>* File uploads send real names
>* Vendored in urllib3



>### 0.7.6

>++++++++++++++++++

>* Digest authentication bugfix (attach query data to path)



>### 0.7.5

>++++++++++++++++++

>* Response.content = None if there was an invalid response.
>* Redirection auth handling.



>### 0.7.4

>++++++++++++++++++

>* Session Hooks fix.



>### 0.7.3

>++++++++++++++++++

>* Digest Auth fix.




>### 0.7.2

>++++++++++++++++++

>* PATCH Fix.




>### 0.7.1

>++++++++++++++++++

>* Move away from urllib2 authentication handling.
>* Fully Remove AuthManager, AuthObject, &amp;c.
>* New tuple-based auth system with handler callbacks.




>### 0.7.0

>++++++++++++++++++

>* Sessions are now the primary interface.
>* Deprecated InvalidMethodException.
>* PATCH fix.
>* New config system (no more global settings).




>### 0.6.6

>++++++++++++++++++

>* Session parameter bugfix (params merging).




>### 0.6.5

>++++++++++++++++++

>* Offline (fast) test suite.
>* Session dictionary argument merging.




>### 0.6.4

>++++++++++++++++++

>* Automatic decoding of unicode, based on HTTP Headers.
>* New ``decode_unicode`` setting.
>* Removal of ``r.read/close`` methods.
>* New ``r.faw`` interface for advanced response usage.*
>* Automatic expansion of parameterized headers.




>### 0.6.3

>++++++++++++++++++

>* Beautiful ``requests.async`` module, for making async requests w/ gevent.




>### 0.6.2

>++++++++++++++++++

>* GET/HEAD obeys allow_redirects=False.




>### 0.6.1

>++++++++++++++++++

>* Enhanced status codes experience ``\o/``
>* Set a maximum number of redirects (``settings.max_redirects``)
>* Full Unicode URL support
>* Support for protocol-less redirects.
>* Allow for arbitrary request types.
>* Bugfixes




>### 0.6.0

>++++++++++++++++++

>* New callback hook system
>* New persistent sessions object and context manager
>* Transparent Dict-cookie handling
>* Status code reference object
>* Removed Response.cached
>* Added Response.request
>* All args are kwargs
>* Relative redirect support
>* HTTPError handling improvements
>* Improved https testing
>* Bugfixes




>### 0.5.1

>++++++++++++++++++

>* International Domain Name Support!
>* Access headers without fetching entire body (``read()``)
>* Use lists as dicts for parameters
>* Add Forced Basic Authentication
>* Forced Basic is default authentication type
>* ``python-requests.org`` default User-Agent header
>* CaseInsensitiveDict lower-case caching
>* Response.history bugfix




>### 0.5.0

>++++++++++++++++++

>* PATCH Support
>* Support for Proxies
>* HTTPBin Test Suite
>* Redirect Fixes
>* settings.verbose stream writing
>* Querystrings for all methods
>* URLErrors (Connection Refused, Timeout, Invalid URLs) are treated as explicitly raised
>  ``r.requests.get(&#39;hwe://blah&#39;); r.raise_for_status()``




>### 0.4.1

>++++++++++++++++++

>* Improved Redirection Handling
>* New &#39;allow_redirects&#39; param for following non-GET/HEAD Redirects
>* Settings module refactoring




>### 0.4.0

>++++++++++++++++++

>* Response.history: list of redirected responses
>* Case-Insensitive Header Dictionaries!
>* Unicode URLs




>### 0.3.4

>++++++++++++++++++

>* Urllib2 HTTPAuthentication Recursion fix (Basic/Digest)
>* Internal Refactor
>* Bytes data upload Bugfix





>### 0.3.3

>++++++++++++++++++

>* Request timeouts
>* Unicode url-encoded data
>* Settings context manager and module




>### 0.3.2

>++++++++++++++++++

>* Automatic Decompression of GZip Encoded Content
>* AutoAuth Support for Tupled HTTP Auth




>### 0.3.1

>++++++++++++++++++

>* Cookie Changes
>* Response.read()
>* Poster fix




>### 0.3.0

>++++++++++++++++++

>* Automatic Authentication API Change
>* Smarter Query URL Parameterization
>* Allow file uploads and POST data together
>* New Authentication Manager System
>    - Simpler Basic HTTP System
>    - Supports all build-in urllib2 Auths
>    - Allows for custom Auth Handlers




>### 0.2.4

>++++++++++++++++++

>* Python 2.5 Support
>* PyPy-c v1.4 Support
>* Auto-Authentication tests
>* Improved Request object constructor



>### 0.2.3

>++++++++++++++++++

>* New HTTPHandling Methods
>    - Response.__nonzero__ (false if bad HTTP Status)
>    - Response.ok (True if expected HTTP Status)
>    - Response.error (Logged HTTPError if bad HTTP Status)
>    - Response.raise_for_status() (Raises stored HTTPError)




>### 0.2.2

>++++++++++++++++++

>* Still handles request in the event of an HTTPError. (Issue 2)
>* Eventlet and Gevent Monkeypatch support.
>* Cookie Support (Issue 1)




>### 0.2.1

>++++++++++++++++++

>* Added file attribute to POST and PUT requests for multipart-encode file uploads.
>* Added Request.url attribute for context and redirects




>### 0.2.0

>++++++++++++++++++

>* Birth!




>### 0.0.1

>++++++++++++++++++

>* Frustration
>* Conception







*Got merge conflicts? Close this PR and delete the branch. I'll create a new PR for you.*

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#8 PR](https://github.com/mattduck/gh2md/pull/8) `closed`: Pin twine to latest version 1.8.1

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 15:03](https://github.com/mattduck/gh2md/pull/8):


twine is not pinned to a specific version.

I'm pinning it to the latest version **1.8.1** for now.


These links might come in handy:  <a href="https://pypi.python.org/pypi/twine">PyPI</a> | <a href="https://pyup.io/changelogs/twine/">Changelog</a> | <a href="https://github.com/pypa/twine">Repo</a> 



### Changelog
> 
>### 1.8.1


>  * Check if a package exists if the URL is one of:

>    - ``https://pypi.python.org/pypi/``
>    - ``https://upload.pypi.org/``
>    - ``https://upload.pypi.io/``

>    This helps people with ``https://upload.pypi.io`` still in their .pypirc
>    file.



>### 1.8.0


>  * :feature:`201` Switch from upload.pypi.io to upload.pypi.org.

>  * :feature:`144` Retrieve configuration from the environment as a default.

>    - Repository URL will default to ``TWINE_REPOSITORY``

>    - Username will default to ``TWINE_USERNAME``

>    - Password will default to ``TWINE_PASSWORD``

>  * :feature:`166` Allow the Repository URL to be provided on the command-line
>    (``--repository-url``) or via an environment variable
>    (``TWINE_REPOSITORY_URL``).

>  * Generate SHA256 digest for all packages by default.

>  * :feature:`171` Generate Blake2b 256 digests for packages *if* ``pyblake2``
>    is installed. Users can use ``python -m pip install twine[with-blake2]``
>    to have ``pyblake2`` installed with Twine.

>  * Stop testing on Python 2.6. 2.6 support will be &quot;best effort&quot; until 2.0.0

>  * Warn users if they receive a 500 error when uploading to \*pypi.python.org



>### 1.7.4


>  * Correct a packaging error.



>### 1.7.3


>  * :bug:`195` Fix uploads to instances of pypiserver using
>    ``--skip-existing``. We were not properly checking the return status code
>    on the response after attempting an upload.

>  * Do not generate traffic to Legacy PyPI unless we&#39;re uploading to it or
>    uploading to Warehouse (e.g., pypi.io). This avoids the attempt to upload
>    a package to the index if we can find it on Legacy PyPI already.



>### 1.7.2


>  * :bug:`189`, :bug:`191` Fix issue where we were checking the existence of
>    packages even if the user didn&#39;t specify ``--skip-existing``.



>### 1.7.1


>  * :bug:`187` Clint was not specified in the wheel metadata as a dependency.



>### 1.7.0


>  * :feature:`142` Support ``--cert`` and ``--client-cert`` command-line flags
>    and config file options for feature parity with pip. This allows users to
>    verify connections to servers other than PyPI (e.g., local package
>    repositories) with different certificates.

>  * :feature:`152` Add progress bar to uploads.

>  * :feature:`162` Allow ``--skip-existing`` to work for 409 status codes.

>  * :feature:`167` Implement retries when the CDN in front of PyPI gives us a
>    5xx error.

>  * :feature:`177` Switch Twine to upload to pypi.io instead of
>    pypi.python.org.

>  * :bug:`186` Allow passwords to have ``%``\ s in them.



>### 1.6.5


>  * :bug:`155` Bump requests-toolbelt version to ensure we avoid
>    ConnectionErrors



>### 1.6.4


>  * :bug:`145` Paths with hyphens in them break the Wheel regular expression.

>  * :bug:`146` Exception while accessing the ``respository`` key when raising
>    a redirect exception.



>### 1.6.3


>  * :bug:`137`, :bug:`140` Uploading signatures was broken due to the pull
>    request that added large file support via ``requests-toolbelt``. This
>    caused a 500 error on PyPI and prevented package and signature upload in
>    twine 1.6.0



>### 1.6.2


>  * :bug:`132` Upload signatures with packages appropriately

>    As part of the refactor for the 1.6.0 release, we were using the wrong
>    name to find the signature file.

>    This also uncovered a bug where if you&#39;re using twine in a situation where
>    ``*`` is not expanded by your shell, we might also miss uploading
>    signatures to PyPI. Both were fixed as part of this.



>### 1.6.1


>  * :bug:`130` Fix signing support for uploads



>### 1.6.0


>  * :feature:`106` Upload wheels first to PyPI

>  * :feature:`104` Large file support via the ``requests-toolbelt``

>  * :bug:`92` Raise an exception on redirects

>  * :feature:`97` Allow the user to specify the location of their ``.pypirc``

>  * :feature:`115` Add the ``--skip-existing`` flag to ``twine upload`` to
>    allow users to skip releases that already exist on PyPI.

>  * :bug:`114` Warnings triggered by pkginfo searching for ``PKG-INFO`` files
>    should no longer be user visible.

>  * :bug:`116` Work around problems with Windows when using
>    :func:`getpass.getpass`

>  * :bug:`111` Provide more helpful messages if ``.pypirc`` is out of date.

>  * :feature:`8` Support registering new packages with ``twine register``



>### 1.5.0


>  * :bug:`85` Display information about the version of setuptools installed

>  * :bug:`61` Support deprecated pypirc file format

>  * :feature:`29` Support commands not named &quot;gpg&quot; for signing

>  * Add lower-limit to requests dependency



>### 1.4.0


>  * :bug:`28` Prevent ResourceWarning from being shown

>  * :bug:`34` List registered commands in help text

>  * :bug:`32` Use pkg_resources to load registered commands

>  * :bug:`47` Fix issue uploading packages with ``_``\ s in the name

>  * :bug:`26` Add support for uploading Windows installers

>  * :bug:`65` Expand globs and check for existence of dists to upload

>* :feature:`13` Parse ~/.pypirc ourselves and use subprocess instead of the
>  distutils.spawn module.
>* :feature:`6` Switch to a git style dispatching for the commands to enable
>  simpler commands and programmatic invocation.


>### 1.2.2







*Got merge conflicts? Close this PR and delete the branch. I'll create a new PR for you.*

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#7 PR](https://github.com/mattduck/gh2md/pull/7) `closed`: Pin flake8 to latest version 3.3.0

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 15:03](https://github.com/mattduck/gh2md/pull/7):


flake8 is not pinned to a specific version.

I'm pinning it to the latest version **3.3.0** for now.


These links might come in handy:  <a href="https://pypi.python.org/pypi/flake8">PyPI</a> | <a href="https://pyup.io/changelogs/flake8/">Changelog</a> | <a href="https://gitlab.com/pycqa/flake8">Repo</a> 



### Changelog
> 
>### 3.3.0

>-------------------

>You can view the `3.3.0 milestone`_ on GitLab for more details.

>- Add support for Python 3.6 (via dependencies). **Note** Flake8 does not
>  guarantee that all plugins will support Python 3.6.

>- Added unique error codes for all missing PyFlakes messages. (14 new
>  codes, see &quot;Error / Violation Codes&quot;)

>- Dramatically improve the performance of Flake8. (See also `GitLab!156`_)

>- Display the local file path instead of the temporary file path when
>  using the git hook. (See also `GitLab244`_)

>- Add methods to Report class that will be called when Flake8 starts and
>  finishes processing a file. (See also `GitLab251`_)

>- Fix problem where hooks should only check \*.py files. (See also
>  `GitLab268`_)

>- Fix handling of SyntaxErrors that do not include physical line information.
>  (See also `GitLab279`_)

>- Update upper bound on PyFlakes to allow for PyFlakes 1.5.0.  (See also
>  `GitLab290`_)

>- Update setuptools integration to less eagerly deduplicate packages.
>  (See also `GitLab295`_)

>- Force ``flake8 --version`` to be repeatable between invocations. (See also
>  `GitLab297`_)

>.. all links
>.. _3.3.0 milestone:
>    https://gitlab.com/pycqa/flake8/milestones/16

>.. issue links
>.. _GitLab244:
>    https://gitlab.com/pycqa/flake8/issues/244
>.. _GitLab251:
>    https://gitlab.com/pycqa/flake8/issues/251
>.. _GitLab268:
>    https://gitlab.com/pycqa/flake8/issues/268
>.. _GitLab279:
>    https://gitlab.com/pycqa/flake8/issues/279
>.. _GitLab290:
>    https://gitlab.com/pycqa/flake8/issues/290
>.. _GitLab295:
>    https://gitlab.com/pycqa/flake8/issues/295
>.. _GitLab297:
>    https://gitlab.com/pycqa/flake8/issues/297

>.. merge request links
>.. _GitLab!156:
>    https://gitlab.com/pycqa/flake8/merge_requests/156




>### 3.2.1

>-------------------

>You can view the `3.2.1 milestone`_ on GitLab for more details.

>- Fix subtle bug when deciding whether to report an on-by-default&#39;s violation
>  (See also `GitLab257`_)

>- Fix another bug around SyntaxErrors not being reported at the right column
>  and row (See also `GitLab259`_ and `GitLab237`_ for a related, previously
>  fixed bug)

>- Fix regression from 2.x where we run checks against explicitly provided
>  files, even if they don&#39;t match the filename patterns. (See also
>  `GitLab266`_)

>.. links
>.. _3.2.1 milestone:
>    https://gitlab.com/pycqa/flake8/milestones/15
>.. _GitLab237:
>    https://gitlab.com/pycqa/flake8/issues/237
>.. _GitLab257:
>    https://gitlab.com/pycqa/flake8/issues/257
>.. _GitLab259:
>    https://gitlab.com/pycqa/flake8/issues/259
>.. _GitLab266:
>    https://gitlab.com/pycqa/flake8/issues/266




>### 3.2.0

>-------------------

>You can view the `3.2.0 milestone`_ on GitLab for more details.

>- Allow for pycodestyle 2.2.0 which fixes a bug in E305 (See also
>  `GitLab256`_)

>.. links
>.. _3.2.0 milestone:
>    https://gitlab.com/pycqa/flake8/milestones/14
>.. _GitLab256:
>    https://gitlab.com/pycqa/flake8/issues/256




>### 3.1.1

>-------------------

>You can view the `3.1.1 milestone`_ on GitLab for more details.

>- Do not attempt to install/distribute a ``man`` file with the Python package;
>  leave this for others to do. (See also `GitLab254`_)

>- Fix packaging bug where wheel version constraints specified in setup.cfg did
>  not match the constraints in setup.py. (See also `GitLab255`_)

>.. links
>.. _3.1.1 milestone:
>    https://gitlab.com/pycqa/flake8/milestones/13
>.. _GitLab254:
>    https://gitlab.com/pycqa/flake8/issues/254
>.. _GitLab255:
>    https://gitlab.com/pycqa/flake8/issues/255




>### 3.1.0

>-------------------

>You can view the `3.1.0 milestone`_ on GitLab for more details.

>- Add ``--bug-report`` flag to make issue reporters&#39; lives easier.

>- Collect configuration files from the current directory when using our Git
>  hook. (See also `GitLab210`_, `GitLab218`_, `GitLab223`_)

>- Avoid unhandled exceptions when dealing with SyntaxErrors. (See also
>  `GitLab214`_, `GitLab238`_)

>- Exit early if the value for ``--diff`` is empty. (See also `GitLab226`_)

>- Handle empty ``--stdin-display-name`` values. (See also `GitLab235`_)

>- Properly report the column number of Syntax Errors. We were assuming that
>  all reports of column numbers were 0-indexed, however, SyntaxErrors report
>  the column number as 1-indexed. This caused us to report a column number
>  that was 1 past the actual position. Further, when combined with
>  SyntaxErrors that occur at a newline, this caused the position to be
>  visually off by two. (See also `GitLab237`_)

>- Fix the behaviour of ``--enable-extensions``. Previously, items specified
>  here were still ignored due to the fact that the off-by-default extension
>  codes were being left in the ``ignore`` list. (See also `GitLab239`_)

>- Fix problems around ``--select`` and ``--ignore`` behaviour that prevented
>  codes that were neither explicitly selected nor explicitly ignored from
>  being reported. (See also `GitLab242`_)

>- Truly be quiet when the user specifies ``-q`` one or more times. Previously,
>  we were showing the if the user specified ``-q`` and ``--show-source``. We
>  have fixed this bug. (See also `GitLab245`_)

>- Add new File Processor attribute, ``previous_unindented_logical_line`` to
>  accommodate pycodestyle 2.1.0. (See also `GitLab246`_)

>- When something goes wrong, exit non-zero. (See also `GitLab248`_,
>  `GitLab209`_)

>- Add ``--tee`` as an option to allow use of ``--output-file`` and printing to
>  standard out.

>- Allow the git plugin to actually be lazy when collecting files.

>- Allow for pycodestyle 2.1 series and pyflakes 1.3 series.

>.. links
>.. _3.1.0 milestone:
>    https://gitlab.com/pycqa/flake8/milestones/12
>.. _GitLab209:
>    https://gitlab.com/pycqa/flake8/issues/209
>.. _GitLab210:
>    https://gitlab.com/pycqa/flake8/issues/210
>.. _GitLab214:
>    https://gitlab.com/pycqa/flake8/issues/214
>.. _GitLab218:
>    https://gitlab.com/pycqa/flake8/issues/218
>.. _GitLab223:
>    https://gitlab.com/pycqa/flake8/issues/223
>.. _GitLab226:
>    https://gitlab.com/pycqa/flake8/issues/226
>.. _GitLab235:
>    https://gitlab.com/pycqa/flake8/issues/235
>.. _GitLab237:
>    https://gitlab.com/pycqa/flake8/issues/237
>.. _GitLab238:
>    https://gitlab.com/pycqa/flake8/issues/238
>.. _GitLab239:
>    https://gitlab.com/pycqa/flake8/issues/239
>.. _GitLab242:
>    https://gitlab.com/pycqa/flake8/issues/242
>.. _GitLab245:
>    https://gitlab.com/pycqa/flake8/issues/245
>.. _GitLab246:
>    https://gitlab.com/pycqa/flake8/issues/246
>.. _GitLab248:
>    https://gitlab.com/pycqa/flake8/issues/248




>### 3.0.4

>-------------------

>- Side-step a Pickling Error when using Flake8 with multiprocessing on Unix
>  systems. (See also `GitLab164`_)

>- Fix an Attribute Error raised when dealing with Invalid Syntax. (See also
>  `GitLab203`_)

>- Fix an unhandled Syntax Error when tokenizing files. (See also
>  `GitLab205`_)


>.. links
>.. _GitLab164:
>    https://gitlab.com/pycqa/flake8/issues/164
>.. _GitLab203:
>    https://gitlab.com/pycqa/flake8/issues/203
>.. _GitLab205:
>    https://gitlab.com/pycqa/flake8/issues/205




>### 3.0.3

>-------------------

>- Disable ``--jobs`` for any version of Python on Windows.
>  (See also `this Python bug report`_)

>- Raise exception when entry_point in plugin not callable.
>  This raises an informative error when a plugin fails to load because its
>  entry_point is not callable, which can happen with a plugin which is buggy or
>  not updated for the current version of flake8. This is nicer than raising a
>  `PicklingError` about failing to pickle a module (See also `GitLab164`_)

>- Fix `` noqa`` comments followed by a ``:`` and explanation broken by
>  3.0.0 (See also `GitLab178`_)

>- Always open our output file in append mode so we do not overwrite log
>  messages. (See also `GitLab193`_)

>- When normalizing path values read from configuration, keep in context the
>  directory where the configuration was found so that relative paths work.
>  (See also `GitLab194`_)

>- Fix issue where users were unable to ignore plugin errors that were on
>  by default. (See also `GitLab195`_)

>- Fix our legacy API StyleGuide&#39;s ``init_report`` method to actually override
>  the previous formatter. (See also `GitLab200`_)


>.. links
>.. _GitLab164:
>    https://gitlab.com/pycqa/flake8/issues/164
>.. _GitLab178:
>    https://gitlab.com/pycqa/flake8/issues/178
>.. _GitLab193:
>    https://gitlab.com/pycqa/flake8/issues/193
>.. _GitLab194:
>    https://gitlab.com/pycqa/flake8/issues/193
>.. _GitLab195:
>    https://gitlab.com/pycqa/flake8/issues/195
>.. _GitLab200:
>    https://gitlab.com/pycqa/flake8/issues/200
>.. _this Python bug report:
>    https://bugs.python.org/issue27649




>### 3.0.2

>-------------------

>- Fix local config file discovery.  (See also `GitLab181`_)

>- Fix indexing of column numbers. We accidentally were starting column indices
>  at 0 instead of 1.

>- Fix regression in handling of errors like E402 that rely on a combination of
>  attributes. (See also `GitLab186`_)


>.. links
>.. _GitLab181:
>    https://gitlab.com/pycqa/flake8/issues/181
>.. _GitLab186:
>    https://gitlab.com/pycqa/flake8/issues/186




>### 3.0.1

>-------------------

>- Fix regression in handling of `` noqa`` for multiline strings.
>  (See also `GitLab177`_)

>- Fix regression in handling of ``--output-file`` when not also using
>  ``--verbose``. (See also `GitLab180`_)

>- Fix regression in handling of ``--quiet``. (See also `GitLab180`_)

>- Fix regression in handling of ``--statistics``. (See also `GitLab180`_)


>.. links
>.. _GitLab177:
>    https://gitlab.com/pycqa/flake8/issues/177
>.. _GitLab180:
>    https://gitlab.com/pycqa/flake8/issues/180




>### 3.0.0

>-------------------

>- Rewrite our documentation from scratch! (http://flake8.pycqa.org)

>- Drop explicit support for Pythons 2.6, 3.2, and 3.3.

>- Remove dependence on pep8/pycodestyle for file processing, plugin
>  dispatching, and more. We now control all of this while keeping backwards
>  compatibility.

>- ``--select`` and ``--ignore`` can now both be specified and try to find the
>  most specific rule from each. For example, if you do ``--select E --ignore
>  E123`` then we will report everything that starts with ``E`` except for
>  ``E123``. Previously, you would have had to do ``--ignore E123,F,W`` which
>  will also still work, but the former should be far more intuitive.

>- Add support for in-line `` noqa`` comments to specify **only** the error
>  codes to be ignored, e.g., `` noqa: E123,W503``

>- Add entry-point for formatters as well as a base class that new formatters
>  can inherit from. See the documentation for more details.

>- Add detailed verbose output using the standard library logging module.

>- Enhance our usage of optparse for plugin developers by adding new parameters
>  to the ``add_option`` that plugins use to register new options.

>- Update ``--install-hook`` to require the name of version control system hook
>  you wish to install a Flake8.

>- Stop checking sub-directories more than once via the setuptools command

>- When passing a file on standard-in, allow the caller to specify
>  ``--stdin-display-name`` so the output is properly formatted

>- The Git hook now uses ``sys.executable`` to format the shebang line.
>  This allows Flake8 to install a hook script from a virtualenv that points to
>  that virtualenv&#39;s Flake8 as opposed to a global one (without the virtualenv
>  being sourced).

>- Print results in a deterministic and consistent ordering when used with
>  multiprocessing

>- When using ``--count``, the output is no longer written to stderr.

>- AST plugins can either be functions or classes and all plugins can now
>  register options so long as there are callable attributes named as we
>  expect.

>- Stop forcibly re-adding ``.tox``, ``.eggs``, and ``*.eggs`` to
>  ``--exclude``. Flake8 2.x started always appending those three patterns
>  to any exclude list (including the default and any user supplied list).
>  Flake8 3 has stopped adding these in, so you may see errors when upgrading
>  due to these patterns no longer being forcibly excluded by default if you
>  have your own exclude patterns specified.

>  To fix this, add the appropriate patterns to your exclude patterns list.

>  .. note::

>      This item was added in November of 2016, as a result of a bug
>      report.




>### 2.6.2

>------------------

>- **Bug** Fix packaging error during release process.




>### 2.6.1

>------------------

>- **Bug** Update the config files to search for to include ``setup.cfg`` and
>  ``tox.ini``. This was broken in 2.5.5 when we stopped passing
>  ``config_file`` to our Style Guide




>### 2.6.0

>------------------

>- **Requirements Change** Switch to pycodestyle as all future pep8 releases
>  will use that package name

>- **Improvement** Allow for Windows users on *select* versions of Python to
>  use ``--jobs`` and multiprocessing

>- **Improvement** Update bounds on McCabe

>- **Improvement** Update bounds on PyFlakes and blacklist known broken
>  versions

>- **Improvement** Handle new PyFlakes warning with a new error code: F405




>### 2.5.5

>------------------

>- **Bug** Fix setuptools integration when parsing config files

>- **Bug** Don&#39;t pass the user&#39;s config path as the config_file when creating a
>  StyleGuide




>### 2.5.4

>------------------

>- **Bug** Missed an attribute rename during the v2.5.3 release.




>### 2.5.3

>------------------

>- **Bug** Actually parse ``output_file`` and ``enable_extensions`` from config
>  files




>### 2.5.2

>------------------

>- **Bug** Parse ``output_file`` and ``enable_extensions`` from config files

>- **Improvement** Raise upper bound on mccabe plugin to allow for version
>  0.4.0




>### 2.5.1

>------------------

>- **Bug** Properly look for ``.flake8`` in current working directory
>  (`GitLab103`_)

>- **Bug** Monkey-patch ``pep8.stdin_get_value`` to cache the actual value in
>  stdin. This helps plugins relying on the function when run with
>  multiprocessing. (`GitLab105`_, `GitLab107`_)

>.. _GitLab103: https://gitlab.com/pycqa/flake8/issues/103
>.. _GitLab105: https://gitlab.com/pycqa/flake8/issues/105
>.. _GitLab107: https://gitlab.com/pycqa/flake8/issues/107




>### 2.5.0

>------------------

>- **Improvement** Raise cap on PyFlakes for Python 3.5 support

>- **Improvement** Avoid deprecation warnings when loading extensions
>  (`GitLab59`_, `GitLab90`_)

>- **Improvement** Separate logic to enable &quot;off-by-default&quot; extensions
>  (`GitLab67`_)

>- **Bug** Properly parse options to setuptools Flake8 command (`GitLab!41`_)

>- **Bug** Fix exceptions when output on stdout is truncated before Flake8
>  finishes writing the output (`GitLab69`_)

>- **Bug** Fix error on OS X where Flake8 can no longer acquire or create new
>  semaphores (`GitLab74`_)

>.. _GitLab!41: https://gitlab.com/pycqa/flake8/merge_requests/41
>.. _GitLab59: https://gitlab.com/pycqa/flake8/issues/59
>.. _GitLab67: https://gitlab.com/pycqa/flake8/issues/67
>.. _GitLab69: https://gitlab.com/pycqa/flake8/issues/69
>.. _GitLab74: https://gitlab.com/pycqa/flake8/issues/74
>.. _GitLab90: https://gitlab.com/pycqa/flake8/issues/90




>### 2.4.1

>------------------

>- **Bug** Do not raise a ``SystemError`` unless there were errors in the
>  setuptools command. (`GitLab39`_, `GitLab!23`_)

>- **Bug** Do not verify dependencies of extensions loaded via entry-points.

>- **Improvement** Blacklist versions of pep8 we know are broken

>.. _GitLab39: https://gitlab.com/pycqa/flake8/issues/39
>.. _GitLab!23: https://gitlab.com/pycqa/flake8/merge_requests/23




>### 2.4.0

>------------------

>- **Bug** Print filenames when using multiprocessing and ``-q`` option.
>  (`GitLab31`_)

>- **Bug** Put upper cap on dependencies. The caps for 2.4.0 are:

>  - ``pep8 &lt; 1.6`` (Related to `GitLab35`_)

>  - ``mccabe &lt; 0.4``

>  - ``pyflakes &lt; 0.9``

>  See also `GitLab32`_

>- **Bug** Files excluded in a config file were not being excluded when flake8
>  was run from a git hook. (`GitHub2`_)

>- **Improvement** Print warnings for users who are providing mutually
>  exclusive options to flake8. (`GitLab8`_, `GitLab!18`_)

>- **Feature** Allow git hook configuration to live in ``.git/config``.
>  See the updated `VCS hooks docs`_ for more details. (`GitLab!20`_)

>.. _GitHub2: https://github.com/pycqa/flake8/pull/2
>.. _GitLab8: https://gitlab.com/pycqa/flake8/issues/8
>.. _GitLab31: https://gitlab.com/pycqa/flake8/issues/31
>.. _GitLab32: https://gitlab.com/pycqa/flake8/issues/32
>.. _GitLab35: https://gitlab.com/pycqa/flake8/issues/35
>.. _GitLab!18: https://gitlab.com/pycqa/flake8/merge_requests/18
>.. _GitLab!20: https://gitlab.com/pycqa/flake8/merge_requests/20
>.. _VCS hooks docs: https://flake8.readthedocs.org/en/latest/vcs.html




>### 2.3.0

>------------------

>- **Feature**: Add ``--output-file`` option to specify a file to write to
>  instead of ``stdout``.

>- **Bug** Fix interleaving of output while using multiprocessing
>  (`GitLab17`_)

>.. _GitLab17: https://gitlab.com/pycqa/flake8/issues/17




>### 2.2.5

>------------------

>- Flush standard out when using multiprocessing

>- Make the check for &quot; flake8: noqa&quot; more strict




>### 2.2.4

>------------------

>- Fix bugs triggered by turning multiprocessing on by default (again)

>  Multiprocessing is forcibly disabled in the following cases:

>  - Passing something in via stdin

>  - Analyzing a diff

>  - Using windows

>- Fix --install-hook when there are no config files present for pep8 or
>  flake8.

>- Fix how the setuptools command parses excludes in config files

>- Fix how the git hook determines which files to analyze (Thanks Chris
>  Buccella!)




>### 2.2.3

>------------------

>- Actually turn multiprocessing on by default




>### 2.2.2

>------------------

>- Re-enable multiprocessing by default while fixing the issue Windows users
>  were seeing.




>### 2.2.1

>------------------

>- Turn off multiple jobs by default. To enable automatic use of all CPUs, use
>  ``--jobs=auto``. Fixes 155 and 154.




>### 2.2.0

>------------------

>- New option ``doctests`` to run Pyflakes checks on doctests too
>- New option ``jobs`` to launch multiple jobs in parallel
>- Turn on using multiple jobs by default using the CPU count
>- Add support for ``python -m flake8`` on Python 2.7 and Python 3
>- Fix Git and Mercurial hooks: issues 88, 133, 148 and 149
>- Fix crashes with Python 3.4 by upgrading dependencies
>- Fix traceback when running tests with Python 2.6
>- Fix the setuptools command ``python setup.py flake8`` to read
>  the project configuration




>### 2.1.0

>------------------

>- Add FLAKE8_LAZY and FLAKE8_IGNORE environment variable support to git and
>  mercurial hooks
>- Force git and mercurial hooks to repsect configuration in setup.cfg
>- Only check staged files if that is specified
>- Fix hook file permissions
>- Fix the git hook on python 3
>- Ignore non-python files when running the git hook
>- Ignore .tox directories by default
>- Flake8 now reports the column number for PyFlakes messages




>### 2.0.0

>------------------

>- Pyflakes errors are prefixed by an ``F`` instead of an ``E``
>- McCabe complexity warnings are prefixed by a ``C`` instead of a ``W``
>- Flake8 supports extensions through entry points
>- Due to the above support, we **require** setuptools
>- We publish the `documentation &lt;https://flake8.readthedocs.org/&gt;`_
>- Fixes 13: pep8, pyflakes and mccabe become external dependencies
>- Split run.py into main.py, engine.py and hooks.py for better logic
>- Expose our parser for our users
>- New feature: Install git and hg hooks automagically
>- By relying on pyflakes (0.6.1), we also fixed 45 and 35




>### 1.7.0

>------------------

>- Fixes part of 35: Exception for no WITHITEM being an attribute of Checker
>  for Python 3.3
>- Support stdin
>- Incorporate phd&#39;s builtins pull request
>- Fix the git hook
>- Update pep8.py to the latest version




>### 1.6.2

>------------------

>- fixed the NameError: global name &#39;message&#39; is not defined (46)




>### 1.6.1

>------------------

>- fixed the mercurial hook, a change from a previous patch was not properly
>  applied
>- fixed an assumption about warnings/error messages that caused an exception
>  to be thrown when McCabe is used




>### 1.6

>----------------

>- changed the signatures of the ``check_file`` function in flake8/run.py,
>  ``skip_warning`` in flake8/util.py and the ``check``, ``checkPath``
>  functions in flake8/pyflakes.py.
>- fix ``--exclude`` and ``--ignore`` command flags (14, 19)
>- fix the git hook that wasn&#39;t catching files not already added to the index
>  (29)
>- pre-emptively includes the addition to pep8 to ignore certain lines.
>  Add `` nopep8`` to the end of a line to ignore it. (37)
>- ``check_file`` can now be used without any special prior setup (21)
>- unpacking exceptions will no longer cause an exception (20)
>- fixed crash on non-existent file (38)




>### 1.5

>----------------

>- fixed the stdin
>- make sure mccabe catches the syntax errors as warnings
>- pep8 upgrade
>- added max_line_length default value
>- added Flake8Command and entry points if setuptools is around
>- using the setuptools console wrapper when available




>### 1.4

>----------------

>- git_hook: Only check staged changes for compliance
>- use pep8 1.2




>### 1.3.1

>------------------

>- fixed support for Python 2.5




>### 1.3

>----------------

>- fixed false W402 warning on exception blocks.




>### 1.2

>----------------

>- added a git hook
>- now Python 3 compatible
>- mccabe and pyflakes have warning codes like pep8 now




>### 1.1

>----------------

>- fixed the value returned by --version
>- allow the flake8: header to be more generic
>- fixed the &quot;hg hook raises &#39;physical lines&#39;&quot; bug
>- allow three argument form of raise
>- now uses setuptools if available, for &#39;develop&#39; command




>### 1.0

>----------------

>- Deactivates by default the complexity checker
>- Introduces the complexity option in the HG hook and the command line.




>### 0.9

>----------------

>- update pep8 version to 0.6.1
>- mccabe check: gracefully handle compile failure




>### 0.8

>----------------

>- fixed hg hook
>- discard unexisting files on hook check




>### 0.7

>----------------

>- Fix pep8 initialization when run through Hg
>- Make pep8 short options work when run through the command line
>- Skip duplicates when controlling files via Hg




>### 0.6

>----------------

>- Fix the McCabe metric on some loops






*Got merge conflicts? Close this PR and delete the branch. I'll create a new PR for you.*

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#6 PR](https://github.com/mattduck/gh2md/pull/6) `closed`: Pin tox to latest version 2.7.0

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 15:03](https://github.com/mattduck/gh2md/pull/6):


tox is not pinned to a specific version.

I'm pinning it to the latest version **2.7.0** for now.


These links might come in handy:  <a href="https://pypi.python.org/pypi/tox">PyPI</a> | <a href="https://pyup.io/changelogs/tox/">Changelog</a> | <a href="https://tox.readthedocs.org/">Docs</a> 



### Changelog
> 
>### 2.7.0

>-----

>- p450: Stop after the first installdeps and first testenv create hooks
>  succeed. This changes the default behaviour of `tox_testenv_create`
>  and `tox_testenv_install_deps` to not execute other registered hooks when
>  the first hook returns a result that is not `None`.
>  Thanks Anthony Sottile (asottile).

>- 271 and 464: Improve environment information for users.

>  New command line parameter: `-a` show **all** defined environments -
>  not just the ones defined in (or generated from) envlist.

>  New verbosity settings for `-l` and `-a`: show user defined descriptions
>  of the environments. This also works for generated environments from factors
>  by concatenating factor descriptions into a complete description.

>  Note that for backwards compatibility with scripts using the output of `-l`
>  it&#39;s output remains unchanged.

>  Thanks Gábor Bernát (gaborbernat).

>- 464: Fix incorrect egg-info location for modified package_dir in setup.py.
>  Thanks Selim Belhaouane (selimb).

>- 431: Add &#39;LANGUAGE&#39; to default passed environment variables.
>  Thanks Paweł Adamczak (pawalad).

>- 455: Add a Vagrantfile with a customized Arch Linux box for local testing.
>  Thanks Oliver Bestwalter (obestwalter).

>- 454: Revert 407, empty commands is not treated as an error.
>  Thanks Anthony Sottile (asottile).

>- 446: (infrastructure) Travis CI tests for tox now also run on OS X now.
>  Thanks Jason R. Coombs (jaraco).



>### 2.6.0

>-----

>- add &quot;alwayscopy&quot; config option to instruct virtualenv to always copy
>  files instead of symlinking. Thanks Igor Duarte Cardoso (igordcard).

>- pass setenv variables to setup.py during a usedevelop install.
>  Thanks Eli Collins (eli-collins).

>- replace all references to testrun.org with readthedocs ones.
>  Thanks Oliver Bestwalter (obestwalter).

>- fix 323 by avoiding virtualenv14 is not used on py32
>  (although we don&#39;t officially support py32).
>  Thanks Jason R. Coombs (jaraco).

>- add Python 3.6 to envlist and CI.
>  Thanks Andrii Soldatenko (andriisoldatenko).

>- fix glob resolution from TOX_TESTENV_PASSENV env variable
>  Thanks Allan Feldman (a-feld).



>### 2.5.0

>-----

>- slightly backward incompatible: fix issue310: the {posargs} substitution
>  now properly preserves the tox command line positional arguments. Positional
>  arguments with spaces are now properly handled.
>  NOTE: if your tox invocation previously used extra quoting for positional arguments to
>  work around issue310, you need to remove the quoting. Example:
>  tox -- &quot;&#39;some string&#39;&quot;   has to now be written simply as
>  tox -- &quot;some string&quot;
>  thanks holger krekel.  You can set ``minversion = 2.5.0`` in the ``[tox]``
>  section of ``tox.ini`` to make sure people using your tox.ini use the correct version.

>- fix 359: add COMSPEC to default passenv on windows.  Thanks
>  anthrotype.

>- add support for py36 and py37 and add py36-dev and py37(nightly) to
>  travis builds of tox. Thanks John Vandenberg.

>- fix 348: add py2 and py3 as default environments pointing to
>  &quot;python2&quot; and &quot;python3&quot; basepython executables.  Also fix 347 by
>  updating the list of default envs in the tox basic example.
>  Thanks Tobias McNulty.

>- make &quot;-h&quot; and &quot;--help-ini&quot; options work even if there is no tox.ini,
>  thanks holger krekel.

>- add {:} substitution, which is replaced with os-specific path
>  separator, thanks Lukasz Rogalski.

>- fix 305: ``downloadcache`` test env config is now ignored as pip-8
>  does caching by default. Thanks holger krekel.

>- output from install command in verbose (-vv) mode is now printed to console instead of
>  being redirected to file, thanks Lukasz Rogalski

>- fix 399.  Make sure {envtmpdir} is created if it doesn&#39;t exist at the
>  start of a testenvironment run. Thanks Manuel Jacob.

>- fix 316: Lack of commands key in ini file is now treated as an error.
>  Reported virtualenv status is &#39;nothing to do&#39; instead of &#39;commands
>  succeeded&#39;, with relevant error message displayed. Thanks Lukasz Rogalski.



>### 2.4.1

>-----

>- fix issue380: properly perform substitution again. Thanks Ian
>  Cordasco.



>### 2.4.0

>-----

>- remove PYTHONPATH from environment during the install phase because a
>  tox-run should not have hidden dependencies and the test commands will also
>  not see a PYTHONPATH.  If this causes unforeseen problems it may be
>  reverted in a bugfix release.  Thanks Jason R. Coombs.

>- fix issue352: prevent a configuration where envdir==toxinidir and
>  refine docs to warn people about changing &quot;envdir&quot;. Thanks Oliver Bestwalter and holger krekel.

>- fix issue375, fix issue330: warn against tox-setup.py integration as
>  &quot;setup.py test&quot; should really just test with the current interpreter. Thanks Ronny Pfannschmidt.

>- fix issue302: allow cross-testenv substitution where we substitute
>  with ``{x,y}`` generative syntax.  Thanks Andrew Pashkin.

>- fix issue212: allow escaping curly brace chars &quot;\{&quot; and &quot;\}&quot; if you need the
>  chars &quot;{&quot; and &quot;}&quot; to appear in your commands or other ini values.
>  Thanks John Vandenberg.

>- addresses issue66: add --workdir option to override where tox stores its &quot;.tox&quot; directory
>  and all of the virtualenv environment.  Thanks Danring.

>- introduce per-venv list_dependencies_command which defaults
>  to &quot;pip freeze&quot; to obtain the list of installed packages.
>  Thanks Ted Shaw, Holger Krekel.

>- close issue66: add documentation to jenkins page on how to avoid
>  &quot;too long shebang&quot; lines when calling pip from tox.  Note that we
>  can not use &quot;python -m pip install X&quot; by default because the latter
>  adds the CWD and pip will think X is installed if it is there.
>  &quot;pip install X&quot; does not do that.

>- new list_dependencies_command to influence how tox determines
>  which dependencies are installed in a testenv.

>- (experimental) New feature: When a search for a config file fails, tox tries loading
>  setup.cfg with a section prefix of &quot;tox&quot;.

>- fix issue275: Introduce hooks ``tox_runtest_pre``` and
>  ``tox_runtest_post`` which run before and after the tests of a venv,
>  respectively. Thanks to Matthew Schinckel and itxaka serrano.

>- fix issue317: evaluate minversion before tox config is parsed completely.
>  Thanks Sachi King for the PR.

>- added the &quot;extras&quot; environment option to specify the extras to use when doing the
>  sdist or develop install. Contributed by Alex Grönholm.

>- use pytest-catchlog instead of pytest-capturelog (latter is not
>  maintained, uses deprecated pytest API)



>### 2.3.2

>-----

>- fix issue314: fix command invocation with .py scripts on windows.

>- fix issue279: allow cross-section substitution when the value contains
>  posargs. Thanks Sachi King for the PR.



>### 2.3.1

>-----

>- fix issue294: re-allow cross-section substitution for setenv.



>### 2.3.0

>-----

>- DEPRECATE use of &quot;indexservers&quot; in tox.ini.  It complicates
>  the internal code and it is recommended to rather use the
>  devpi system for managing indexes for pip.

>- fix issue285: make setenv processing fully lazy to fix regressions
>  of tox-2.2.X and so that we can now have testenv attributes like
>  &quot;basepython&quot; depend on environment variables that are set in
>  a setenv section. Thanks Nelfin for some tests and initial
>  work on a PR.

>- allow &quot;&quot; in commands.  This is slightly incompatible with commands
>  sections that used a comment after a &quot;\&quot; line continuation.
>  Thanks David Stanek for the PR.

>- fix issue289: fix build_sphinx target, thanks Barry Warsaw.

>- fix issue252: allow environment names with special characters.
>  Thanks Julien Castets for initial PR and patience.

>- introduce experimental tox_testenv_create(venv, action) and
>  tox_testenv_install_deps(venv, action) hooks to allow
>  plugins to do additional work on creation or installing
>  deps.  These hooks are experimental mainly because of
>  the involved &quot;venv&quot; and session objects whose current public
>  API is not fully guranteed.

>- internal: push some optional object creation into tests because
>  tox core doesn&#39;t need it.



>### 2.2.1

>-----

>- fix bug where {envdir} substitution could not be used in setenv
>  if that env value is then used in {basepython}. Thanks Florian Bruhin.



>### 2.2.0

>-----

>- fix issue265 and add LD_LIBRARY_PATH to passenv on linux by default
>  because otherwise the python interpreter might not start up in
>  certain configurations (redhat software collections).  Thanks David Riddle.

>- fix issue246: fix regression in config parsing by reordering
>  such that {envbindir} can be used again in tox.ini. Thanks Olli Walsh.

>- fix issue99: the {env:...} substitution now properly uses environment
>  settings from the ``setenv`` section. Thanks Itxaka Serrano.

>- fix issue281: make --force-dep work when urls are present in
>  dependency configs.  Thanks Glyph Lefkowitz for reporting.

>- fix issue174: add new ``ignore_outcome`` testenv attribute which
>  can be set to True in which case it will produce a warning instead
>  of an error on a failed testenv command outcome.
>  Thanks Rebecka Gulliksson for the PR.

>- fix issue280: properly skip missing interpreter if
>  {envsitepackagesdir} is present in commands. Thanks BB:ceridwenv




>### 2.1.1

>----------

>- fix platform skipping for detox

>- report skipped platforms as skips in the summary



>### 2.1.0

>----------

>- fix issue258, fix issue248, fix issue253: for non-test commands
>  (installation, venv creation) we pass in the full invocation environment.

>- remove experimental --set-home option which was hardly used and
>  hackily implemented (if people want home-directory isolation we should
>  figure out a better way to do it, possibly through a plugin)

>- fix issue259: passenv is now a line-list which allows to intersperse
>  comments.  Thanks stefano-m.

>- allow envlist to be a multi-line list, to intersperse comments
>  and have long envlist settings split more naturally.  Thanks Andre Caron.

>- introduce a TOX_TESTENV_PASSENV setting which is honored
>  when constructing the set of environment variables for test environments.
>  Thanks Marc Abramowitz for pushing in this direction.




>### 2.0.2

>----------

>- fix issue247: tox now passes the LANG variable from the tox invocation
>  environment to the test environment by default.

>- add SYSTEMDRIVE into default passenv on windows to allow pip6 to work.
>  Thanks Michael Krause.




>### 2.0.1

>-----------

>- fix wheel packaging to properly require argparse on py26.



>### 2.0.0

>-----------

>- (new) introduce environment variable isolation:
>  tox now only passes the PATH and PIP_INDEX_URL variable from the tox
>  invocation environment to the test environment and on Windows
>  also ``SYSTEMROOT``, ``PATHEXT``, ``TEMP`` and ``TMP`` whereas
>  on unix additionally ``TMPDIR`` is passed.  If you need to pass
>  through further environment variables you can use the new ``passenv`` setting,
>  a space-separated list of environment variable names.  Each name
>  can make use of fnmatch-style glob patterns.  All environment
>  variables which exist in the tox-invocation environment will be copied
>  to the test environment.

>- a new ``--help-ini`` option shows all possible testenv settings and
>  their defaults.

>- (new) introduce a way to specify on which platform a testenvironment is to
>  execute: the new per-venv &quot;platform&quot; setting allows to specify
>  a regular expression which is matched against sys.platform.
>  If platform is set and doesn&#39;t match the platform spec in the test
>  environment the test environment is ignored, no setup or tests are attempted.

>- (new) add per-venv &quot;ignore_errors&quot; setting, which defaults to False.
>   If ``True``, a non-zero exit code from one command will be ignored and
>   further commands will be executed (which was the default behavior in tox &lt;
>   2.0).  If ``False`` (the default), then a non-zero exit code from one command
>   will abort execution of commands for that environment.

>- show and store in json the version dependency information for each venv

>- remove the long-deprecated &quot;distribute&quot; option as it has no effect these days.

>- fix issue233: avoid hanging with tox-setuptools integration example. Thanks simonb.

>- fix issue120: allow substitution for the commands section.  Thanks
>  Volodymyr Vitvitski.

>- fix issue235: fix AttributeError with --installpkg.  Thanks
>  Volodymyr Vitvitski.

>- tox has now somewhat pep8 clean code, thanks to Volodymyr Vitvitski.

>- fix issue240: allow to specify empty argument list without it being
>  rewritten to &quot;.&quot;.  Thanks Daniel Hahler.

>- introduce experimental (not much documented yet) plugin system
>  based on pytest&#39;s externalized &quot;pluggy&quot; system.
>  See tox/hookspecs.py for the current hooks.

>- introduce parser.add_testenv_attribute() to register an ini-variable
>  for testenv sections.  Can be used from plugins through the
>  tox_add_option hook.

>- rename internal files -- tox offers no external API except for the
>  experimental plugin hooks, use tox internals at your own risk.

>- DEPRECATE distshare in documentation





>### 1.9.2

>-----------

>- backout ability that --force-dep substitutes name/versions in
>  requirement files due to various issues.
>  This fixes issue228, fixes issue230, fixes issue231
>  which popped up with 1.9.1.



>### 1.9.1

>-----------

>- use a file instead of a pipe for command output in &quot;--result-json&quot;.
>  Fixes some termination issues with python2.6.

>- allow --force-dep to override dependencies in &quot;-r&quot; requirements
>  files.  Thanks Sontek for the PR.

>- fix issue227: use &quot;-m virtualenv&quot; instead of &quot;-mvirtualenv&quot; to make
>  it work with pyrun.  Thanks Marc-Andre Lemburg.




>### 1.9.0

>-----------

>- fix issue193: Remove ``--pre`` from the default ``install_command``; by
>  default tox will now only install final releases from PyPI for unpinned
>  dependencies. Use ``pip_pre = true`` in a testenv or the ``--pre``
>  command-line option to restore the previous behavior.

>- fix issue199: fill resultlog structure ahead of virtualenv creation

>- refine determination if we run from Jenkins, thanks Borge Lanes.

>- echo output to stdout when ``--report-json`` is used

>- fix issue11: add a ``skip_install`` per-testenv setting which
>  prevents the installation of a package. Thanks Julian Krause.

>- fix issue124: ignore command exit codes; when a command has a &quot;-&quot; prefix,
>  tox will ignore the exit code of that command

>- fix issue198: fix broken envlist settings, e.g. {py26,py27}{-lint,}

>- fix issue191: lessen factor-use checks




>### 1.8.1

>-----------

>- fix issue190: allow setenv to be empty.

>- allow escaping curly braces with &quot;\&quot;.  Thanks Marc Abramowitz for the PR.

>- allow &quot;.&quot; names in environment names such that &quot;py27-django1.7&quot; is a
>  valid environment name.  Thanks Alex Gaynor and Alex Schepanovski.

>- report subprocess exit code when execution fails.  Thanks Marius
>  Gedminas.



>### 1.8.0

>-----------

>- new multi-dimensional configuration support.  Many thanks to
>  Alexander Schepanovski for the complete PR with docs.
>  And to Mike Bayer and others for testing and feedback.

>- fix issue148: remove &quot;__PYVENV_LAUNCHER__&quot; from os.environ when starting
>  subprocesses. Thanks Steven Myint.

>- fix issue152: set VIRTUAL_ENV when running test commands,
>  thanks Florian Ludwig.

>- better report if we can&#39;t get version_info from an interpreter
>  executable. Thanks Floris Bruynooghe.




>### 1.7.2

>-----------

>- fix issue150: parse {posargs} more like we used to do it pre 1.7.0.
>  The 1.7.0 behaviour broke a lot of OpenStack projects.
>  See PR85 and the issue discussions for (far) more details, hopefully
>  resulting in a more refined behaviour in the 1.8 series.
>  And thanks to Clark Boylan for the PR.

>- fix issue59: add a config variable ``skip-missing-interpreters`` as well as
>  command line option ``--skip-missing-interpreters`` which won&#39;t fail the
>  build if Python interpreters listed in tox.ini are missing.  Thanks
>  Alexandre Conrad for PR104.

>- fix issue164: better traceback info in case of failing test commands.
>  Thanks Marc Abramowitz for PR92.

>- support optional env variable substitution, thanks Morgan Fainberg
>  for PR86.

>- limit python hashseed to 1024 on Windows to prevent possible
>  memory errors.  Thanks March Schlaich for the PR90.



>### 1.7.1

>---------

>- fix issue162: don&#39;t list python 2.5 as compatibiliy/supported

>- fix issue158 and fix issue155: windows/virtualenv properly works now:
>  call virtualenv through &quot;python -m virtualenv&quot; with the same
>  interpreter which invoked tox.  Thanks Chris Withers, Ionel Maries Cristian.



>### 1.7.0

>---------

>- don&#39;t lookup &quot;pip-script&quot; anymore but rather just &quot;pip&quot; on windows
>  as this is a pip implementation detail and changed with pip-1.5.
>  It might mean that tox-1.7 is not able to install a different pip
>  version into a virtualenv anymore.

>- drop Python2.5 compatibility because it became too hard due
>  to the setuptools-2.0 dropping support.  tox now has no
>  support for creating python2.5 based environments anymore
>  and all internal special-handling has been removed.

>- merged PR81: new option --force-dep which allows to
>  override tox.ini specified dependencies in setuptools-style.
>  For example &quot;--force-dep &#39;django&lt;1.6&#39;&quot; will make sure
>  that any environment using &quot;django&quot; as a dependency will
>  get the latest 1.5 release.  Thanks Bruno Oliveria for
>  the complete PR.

>- merged PR125: tox now sets &quot;PYTHONHASHSEED&quot; to a random value
>  and offers a &quot;--hashseed&quot; option to repeat a test run with a specific seed.
>  You can also use --hashsheed=noset to instruct tox to leave the value
>  alone.  Thanks Chris Jerdonek for all the work behind this.

>- fix issue132: removing zip_safe setting (so it defaults to false)
>  to allow installation of tox
>  via easy_install/eggs.  Thanks Jenisys.

>- fix issue126: depend on virtualenv&gt;=1.11.2 so that we can rely
>  (hopefully) on a pip version which supports --pre. (tox by default
>  uses to --pre).  also merged in PR84 so that we now call &quot;virtualenv&quot;
>  directly instead of looking up interpreters.  Thanks Ionel Maries Cristian.
>  This also fixes issue140.

>- fix issue130: you can now set install_command=easy_install {opts} {packages}
>  and expect it to work for repeated tox runs (previously it only worked
>  when always recreating).  Thanks jenisys for precise reporting.

>- fix issue129: tox now uses Popen(..., universal_newlines=True) to force
>  creation of unicode stdout/stderr streams.  fixes a problem on specific
>  platform configs when creating virtualenvs with Python3.3. Thanks
>  Jorgen Schäfer or investigation and solution sketch.

>- fix issue128: enable full substitution in install_command,
>  thanks for the PR to Ronald Evers

>- rework and simplify &quot;commands&quot; parsing and in particular posargs
>  substitutions to avoid various win32/posix related quoting issues.

>- make sure that the --installpkg option trumps any usedevelop settings
>  in tox.ini or

>- introduce --no-network to tox&#39;s own test suite to skip tests
>  requiring networks

>- introduce --sitepackages to force sitepackages=True in all
>  environments.

>- fix issue105 -- don&#39;t depend on an existing HOME directory from tox tests.



>### 1.6.1

>-----

>- fix issue119: {envsitepackagesdir} is now correctly computed and has
>  a better test to prevent regression.

>- fix issue116: make 1.6 introduced behaviour of changing to a
>  per-env HOME directory during install activities dependent
>  on &quot;--set-home&quot; for now.  Should re-establish the old behaviour
>  when no option is given.

>- fix issue118: correctly have two tests use realpath(). Thanks Barry
>  Warsaw.

>- fix test runs on environments without a home directory
>  (in this case we use toxinidir as the homedir)

>- fix issue117: python2.5 fix: don&#39;t use ``--insecure`` option because
>  its very existence depends on presence of &quot;ssl&quot;.  If you
>  want to support python2.5/pip1.3.1 based test environments you need
>  to install ssl and/or use PIP_INSECURE=1 through ``setenv``. section.

>- fix issue102: change to {toxinidir} when installing dependencies.
>  this allows to use relative path like in &quot;-rrequirements.txt&quot;.



>### 1.6.0

>-----------------

>- fix issue35: add new EXPERIMENTAL &quot;install_command&quot; testenv-option to
>  configure the installation command with options for dep/pkg install.
>  Thanks Carl Meyer for the PR and docs.

>- fix issue91: python2.5 support by vendoring the virtualenv-1.9.1
>  script and forcing pip&lt;1.4. Also the default [py25] environment
>  modifies the default installer_command (new config option)
>  to use pip without the &quot;--pre&quot; option which was introduced
>  with pip-1.4 and is now required if you want to install non-stable
>  releases.  (tox defaults to install with &quot;--pre&quot; everywhere).

>- during installation of dependencies HOME is now set to a pseudo
>  location ({envtmpdir}/pseudo-home).  If an index url was specified
>  a .pydistutils.cfg file will be written with an index_url setting
>  so that packages defining ``setup_requires`` dependencies will not
>  silently use your HOME-directory settings or https://pypi.python.org.

>- fix issue1: empty setup files are properly detected, thanks Anthon van
>  der Neuth

>- remove toxbootstrap.py for now because it is broken.

>- fix issue109 and fix issue111: multiple &quot;-e&quot; options are now combined
>  (previously the last one would win). Thanks Anthon van der Neut.

>- add --result-json option to write out detailed per-venv information
>  into a json report file to be used by upstream tools.

>- add new config options ``usedevelop`` and ``skipsdist`` as well as a
>  command line option ``--develop`` to install the package-under-test in develop mode.
>  thanks Monty Tailor for the PR.

>- always unset PYTHONDONTWRITEBYTE because newer setuptools doesn&#39;t like it

>- if a HOMEDIR cannot be determined, use the toxinidir.

>- refactor interpreter information detection to live in new
>  tox/interpreters.py file, tests in tests/test_interpreters.py.



>### 1.5.0

>-----------------

>- fix issue104: use setuptools by default, instead of distribute,
>  now that setuptools has distribute merged.

>- make sure test commands are searched first in the virtualenv

>- re-fix issue2 - add whitelist_externals to be used in ``[testenv*]``
>  sections, allowing to avoid warnings for commands such as ``make``,
>  used from the commands value.

>- fix issue97 - allow substitutions to reference from other sections
>  (thanks Krisztian Fekete)

>- fix issue92 - fix {envsitepackagesdir} to actually work again

>- show (test) command that is being executed, thanks
>  Lukasz Balcerzak

>- re-license tox to MIT license

>- depend on virtualenv-1.9.1

>- rename README.txt to README.rst to make bitbucket happier




>### 1.4.3

>-----------------

>- use pip-script.py instead of pip.exe on win32 to avoid the lock exe
>  file on execution issue (thanks Philip Thiem)

>- introduce -l|--listenv option to list configured environments
>  (thanks  Lukasz Balcerzak)

>- fix downloadcache determination to work according to docs: Only
>  make pip use a download cache if PIP_DOWNLOAD_CACHE or a
>  downloadcache=PATH testenv setting is present. (The ENV setting
>  takes precedence)

>- fix issue84 - pypy on windows creates a bin not a scripts venv directory
>  (thanks Lukasz Balcerzak)

>- experimentally introduce --installpkg=PATH option to install a package
>  rather than create/install an sdist package.  This will still require
>  and use tox.ini and tests from the current working dir (and not from the
>  remote package).

>- substitute {envsitepackagesdir} with the package installation
>  directory (closes 72) (thanks g2p)

>- issue 70 remove PYTHONDONTWRITEBYTECODE workaround now that
>  virtualenv behaves properly (thanks g2p)

>- merged tox-quickstart command, contributed by Marc Abramowitz, which
>  generates a default tox.ini after asking a few questions

>- fix 48 - win32 detection of pypy and other interpreters that are on PATH
>  (thanks Gustavo Picon)

>- fix grouping of index servers, it is now done by name instead of
>  indexserver url, allowing to use it to separate dependencies
>  into groups even if using the same default indexserver.

>- look for &quot;tox.ini&quot; files in parent dirs of current dir (closes 34)

>- the &quot;py&quot; environment now by default uses the current interpreter
>  (sys.executable) make tox&#39; own setup.py test execute tests with it
>  (closes 46)

>- change tests to not rely on os.path.expanduser (closes 60),
>  also make mock session return args[1:] for more precise checking (closes 61)
>  thanks to Barry Warsaw for both.



>### 1.4.2

>-----------------

>- fix some tests which fail if /tmp is a symlink to some other place
>- &quot;python setup.py test&quot; now runs tox tests via tox :)
>  also added an example on how to do it for your project.



>### 1.4.1

>-----------------

>- fix issue41 better quoting on windows - you can now use &quot;&lt;&quot; and &quot;&gt;&quot; in
>  deps specifications, thanks Chris Withers for reporting



>### 1.4

>-----------------

>- fix issue26 - no warnings on absolute or relative specified paths for commands
>- fix issue33 - commentchars are ignored in key-value settings allowing
>  for specifying commands like: python -c &quot;import sys ; print sys&quot;
>  which would formerly raise irritating errors because the &quot;;&quot;
>  was considered a comment
>- tweak and improve reporting
>- refactor reporting and virtualenv manipulation
>  to be more accessible from 3rd party tools
>- support value substitution from other sections
>  with the {[section]key} syntax
>- fix issue29 - correctly point to pytest explanation
>  for importing modules fully qualified
>- fix issue32 - use --system-site-packages and don&#39;t pass --no-site-packages
>- add python3.3 to the default env list, so early adopters can test
>- drop python2.4 support (you can still have your tests run on
>- fix the links/checkout howtos in the docs
>  python-2.4, just tox itself requires 2.5 or higher.



>### 1.3

>-----------------

>- fix: allow to specify wildcard filesystem paths when
>  specifying dependencies such that tox searches for
>  the highest version

>- fix issue issue21: clear PIP_REQUIRES_VIRTUALENV which avoids
>  pip installing to the wrong environment, thanks to bb&#39;s streeter

>- make the install step honour a testenv&#39;s setenv setting
>  (thanks Ralf Schmitt)




>### 1.2

>-----------------

>- remove the virtualenv.py that was distributed with tox and depend
>  on &gt;=virtualenv-1.6.4 (possible now since the latter fixes a few bugs
>  that the inlining tried to work around)
>- fix issue10: work around UnicodeDecodeError when invoking pip (thanks
>  Marc Abramowitz)
>- fix a problem with parsing {posargs} in tox commands (spotted by goodwill)
>- fix the warning check for commands to be installed in testenvironment
>  (thanks Michael Foord for reporting)



>### 1.1

>-----------------

>- fix issue5 - don&#39;t require argparse for python versions that have it
>- fix issue6 - recreate virtualenv if installing dependencies failed
>- fix issue3 - fix example on frontpage
>- fix issue2 - warn if a test command does not come from the test
>  environment
>- fixed/enhanced: except for initial install always call &quot;-U
>  --no-deps&quot; for installing the sdist package to ensure that a package
>  gets upgraded even if its version number did not change. (reported on
>  TIP mailing list and IRC)
>- inline virtualenv.py (1.6.1) script to avoid a number of issues,
>  particularly failing to install python3 environments from a python2
>  virtualenv installation.
>- rework and enhance docs for display on readthedocs.org



>### 1.0

>-----------------

>- move repository and toxbootstrap links to http://bitbucket.org/hpk42/tox
>- fix issue7: introduce a &quot;minversion&quot; directive such that tox
>  bails out if it does not have the correct version.
>- fix issue24: introduce a way to set environment variables for
>  for test commands (thanks Chris Rose)
>- fix issue22: require virtualenv-1.6.1, obsoleting virtualenv5 (thanks Jannis Leidel)
>  and making things work with pypy-1.5 and python3 more seamlessly
>- toxbootstrap.py (used by jenkins build slaves) now follows the latest release of virtualenv
>- fix issue20: document format of URLs for specifying dependencies
>- fix issue19: substitute Hudson for Jenkins everywhere following the renaming
>  of the project.  NOTE: if you used the special [tox:hudson]
>  section it will now need to be named [tox:jenkins].
>- fix issue 23 / apply some ReST fixes
>- change the positional argument specifier to use {posargs:} syntax and
>  fix issues 15 and 10 by refining the argument parsing method (Chris Rose)
>- remove use of inipkg lazy importing logic -
>  the namespace/imports are anyway very small with tox.
>- fix a fspath related assertion to work with debian installs which uses
>  symlinks
>- show path of the underlying virtualenv invocation and bootstrap
>  virtualenv.py into a working subdir
>- added a CONTRIBUTORS file



>### 0.9

>-----------------

>- fix pip-installation mixups by always unsetting PIP_RESPECT_VIRTUALENV
>  (thanks Armin Ronacher)
>- issue1: Add a toxbootstrap.py script for tox, thanks to Sridhar
>  Ratnakumar
>- added support for working with different and multiple PyPI indexservers.
>- new option: -r|--recreate to force recreation of virtualenv
>- depend on py&gt;=1.4.0 which does not contain or install the py.test
>  anymore which is now a separate distribution &quot;pytest&quot;.
>- show logfile content if there is an error (makes CI output
>  more readable)



>### 0.8

>-----------------

>- work around a virtualenv limitation which crashes if
>  PYTHONDONTWRITEBYTECODE is set.
>- run pip/easy installs from the environment log directory, avoids
>  naming clashes between env names and dependencies (thanks ronny)
>- require a more recent version of py lib
>- refactor and refine config detection to work from a single file
>  and to detect the case where a python installation overwrote
>  an old one and resulted in a new executable. This invalidates
>  the existing virtualenvironment now.
>- change all internal source to strip trailing whitespaces



>### 0.7

>-----------------

>- use virtualenv5 (my own fork of virtualenv3) for now to create python3
>  environments, fixes a couple of issues and makes tox more likely to
>  work with Python3 (on non-windows environments)

>- add ``sitepackages`` option for testenv sections so that environments
>  can be created with access to globals (default is not to have access,
>  i.e. create environments with ``--no-site-packages``.

>- addressing issue4: always prepend venv-path to PATH variable when calling subprocesses

>- fix issue2: exit with proper non-zero return code if there were
>  errors or test failures.

>- added unittest2 examples contributed by Michael Foord

>- only allow &#39;True&#39; or &#39;False&#39; for boolean config values
>  (lowercase / uppercase is irrelevant)

>- recreate virtualenv on changed configurations



>### 0.6

>-----------------

>- fix OSX related bugs that could cause the caller&#39;s environment to get
>  screwed (sorry).  tox was using the same file as virtualenv for tracking
>  the Python executable dependency and there also was confusion wrt links.
>  this should be fixed now.

>- fix long description, thanks Michael Foord



>### 0.5

>-----------------

>- initial release






*Got merge conflicts? Close this PR and delete the branch. I'll create a new PR for you.*

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#5 PR](https://github.com/mattduck/gh2md/pull/5) `closed`: Pin mock to latest version 2.0.0

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 15:03](https://github.com/mattduck/gh2md/pull/5):


mock is not pinned to a specific version.

I'm pinning it to the latest version **2.0.0** for now.


These links might come in handy:  <a href="https://pypi.python.org/pypi/mock">PyPI</a> | <a href="https://github.com/testing-cabal/mock">Repo</a> 


*I couldn't find a changelog for this release. Do you know where I can find one? [Tell me!](https://github.com/pyupio/changelogs/issues/new)*


*Got merge conflicts? Close this PR and delete the branch. I'll create a new PR for you.*

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#4 PR](https://github.com/mattduck/gh2md/pull/4) `closed`: Pin coverage to latest version 4.4.1

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 15:03](https://github.com/mattduck/gh2md/pull/4):


coverage is not pinned to a specific version.

I'm pinning it to the latest version **4.4.1** for now.


These links might come in handy:  <a href="https://pypi.python.org/pypi/coverage">PyPI</a> | <a href="https://pyup.io/changelogs/coverage/">Changelog</a> | <a href="https://coverage.readthedocs.io">Docs</a> 



### Changelog
> 
>### 4.4.1

>----------------------------

>- No code changes: just corrected packaging for Python 2.7 Linux wheels.


>.. _changes_44:



>### 4.4

>--------------------------

>- Reports could produce the wrong file names for packages, reporting ``pkg.py``
>  instead of the correct ``pkg/__init__.py``.  This is now fixed.  Thanks, Dirk
>  Thomas.

>- XML reports could produce ``&lt;source&gt;`` and ``&lt;class&gt;`` lines that together
>  didn&#39;t specify a valid source file path.  This is now fixed. (`issue 526`_)

>- Namespace packages are no longer warned as having no code. (`issue 572`_)

>- Code that uses ``sys.settrace(sys.gettrace())`` in a file that wasn&#39;t being
>  coverage-measured would prevent correct coverage measurement in following
>  code. An example of this was running doctests programmatically. This is now
>  fixed. (`issue 575`_)

>- Errors printed by the ``coverage`` command now go to stderr instead of
>  stdout.

>- Running ``coverage xml`` in a directory named with non-ASCII characters would
>  fail under Python 2. This is now fixed. (`issue 573`_)

>.. _issue 526: https://bitbucket.org/ned/coveragepy/issues/526/generated-xml-invalid-paths-for-cobertura
>.. _issue 572: https://bitbucket.org/ned/coveragepy/issues/572/no-python-source-warning-for-namespace
>.. _issue 573: https://bitbucket.org/ned/coveragepy/issues/573/cant-generate-xml-report-if-some-source
>.. _issue 575: https://bitbucket.org/ned/coveragepy/issues/575/running-doctest-prevents-complete-coverage




>### 4.4b1

>----------------------------

>- Some warnings can now be individually disabled.  Warnings that can be
>  disabled have a short name appended.  The ``[run] disable_warnings`` setting
>  takes a list of these warning names to disable. Closes both `issue 96`_ and
>  `issue 355`_.

>- The XML report now includes attributes from version 4 of the Cobertura XML
>  format, fixing `issue 570`_.

>- In previous versions, calling a method that used collected data would prevent
>  further collection.  For example, `save()`, `report()`, `html_report()`, and
>  others would all stop collection.  An explicit `start()` was needed to get it
>  going again.  This is no longer true.  Now you can use the collected data and
>  also continue measurement. Both `issue 79`_ and `issue 448`_ described this
>  problem, and have been fixed.

>- Plugins can now find unexecuted files if they choose, by implementing the
>  `find_executable_files` method.  Thanks, Emil Madsen.

>- Minimal IronPython support. You should be able to run IronPython programs
>  under ``coverage run``, though you will still have to do the reporting phase
>  with CPython.

>- Coverage.py has long had a special hack to support CPython&#39;s need to measure
>  the coverage of the standard library tests. This code was not installed by
>  kitted versions of coverage.py.  Now it is.

>.. _issue 79: https://bitbucket.org/ned/coveragepy/issues/79/save-prevents-harvesting-on-stop
>.. _issue 96: https://bitbucket.org/ned/coveragepy/issues/96/unhelpful-warnings-produced-when-using
>.. _issue 355: https://bitbucket.org/ned/coveragepy/issues/355/warnings-should-be-suppressable
>.. _issue 448: https://bitbucket.org/ned/coveragepy/issues/448/save-and-html_report-prevent-further
>.. _issue 570: https://bitbucket.org/ned/coveragepy/issues/570/cobertura-coverage-04dtd-support


>.. _changes_434:



>### 4.3.4

>----------------------------

>- Fixing 2.6 in version 4.3.3 broke other things, because the too-tricky
>  exception wasn&#39;t properly derived from Exception, described in `issue 556`_.
>  A newb mistake; it hasn&#39;t been a good few days.

>.. _issue 556: https://bitbucket.org/ned/coveragepy/issues/556/43-fails-if-there-are-html-files-in-the


>.. _changes_433:



>### 4.3.3

>----------------------------

>- Python 2.6 support was broken due to a testing exception imported for the
>  benefit of the coverage.py test suite.  Properly conditionalizing it fixed
>  `issue 554`_ so that Python 2.6 works again.

>.. _issue 554: https://bitbucket.org/ned/coveragepy/issues/554/traceback-on-python-26-starting-with-432


>.. _changes_432:



>### 4.3.2

>----------------------------

>- Using the ``--skip-covered`` option on an HTML report with 100% coverage
>  would cause a &quot;No data to report&quot; error, as reported in `issue 549`_. This is
>  now fixed; thanks, LoÃ¯c Dachary.

>- If-statements can be optimized away during compilation, for example, `if 0:`
>  or `if __debug__:`.  Coverage.py had problems properly understanding these
>  statements which existed in the source, but not in the compiled bytecode.
>  This problem, reported in `issue 522`_, is now fixed.

>- If you specified ``--source`` as a directory, then coverage.py would look for
>  importable Python files in that directory, and could identify ones that had
>  never been executed at all.  But if you specified it as a package name, that
>  detection wasn&#39;t performed.  Now it is, closing `issue 426`_. Thanks to LoÃ¯c
>  Dachary for the fix.

>- If you started and stopped coverage measurement thousands of times in your
>  process, you could crash Python with a &quot;Fatal Python error: deallocating
>  None&quot; error.  This is now fixed.  Thanks to Alex Groce for the bug report.

>- On PyPy, measuring coverage in subprocesses could produce a warning: &quot;Trace
>  function changed, measurement is likely wrong: None&quot;.  This was spurious, and
>  has been suppressed.

>- Previously, coverage.py couldn&#39;t start on Jython, due to that implementation
>  missing the multiprocessing module (`issue 551`_). This problem has now been
>  fixed. Also, `issue 322`_ about not being able to invoke coverage
>  conveniently, seems much better: ``jython -m coverage run myprog.py`` works
>  properly.

>- Let&#39;s say you ran the HTML report over and over again in the same output
>  directory, with ``--skip-covered``. And imagine due to your heroic
>  test-writing efforts, a file just acheived the goal of 100% coverage. With
>  coverage.py 4.3, the old HTML file with the less-than-100% coverage would be
>  left behind.  This file is now properly deleted.

>.. _issue 322: https://bitbucket.org/ned/coveragepy/issues/322/cannot-use-coverage-with-jython
>.. _issue 426: https://bitbucket.org/ned/coveragepy/issues/426/difference-between-coverage-results-with
>.. _issue 522: https://bitbucket.org/ned/coveragepy/issues/522/incorrect-branch-reporting-with-__debug__
>.. _issue 549: https://bitbucket.org/ned/coveragepy/issues/549/skip-covered-with-100-coverage-throws-a-no
>.. _issue 551: https://bitbucket.org/ned/coveragepy/issues/551/coveragepy-cannot-be-imported-in-jython27


>.. _changes_431:



>### 4.3.1

>----------------------------

>- Some environments couldn&#39;t install 4.3, as described in `issue 540`_. This is
>  now fixed.

>- The check for conflicting ``--source`` and ``--include`` was too simple in a
>  few different ways, breaking a few perfectly reasonable use cases, described
>  in `issue 541`_.  The check has been reverted while we re-think the fix for
>  `issue 265`_.

>.. _issue 540: https://bitbucket.org/ned/coveragepy/issues/540/cant-install-coverage-v43-into-under
>.. _issue 541: https://bitbucket.org/ned/coveragepy/issues/541/coverage-43-breaks-nosetest-with-coverage


>.. _changes_43:



>### 4.3

>--------------------------

>Special thanks to **LoÃ¯c Dachary**, who took an extraordinary interest in
>coverage.py and contributed a number of improvements in this release.

>- Subprocesses that are measured with `automatic subprocess measurement`_ used
>  to read in any pre-existing data file.  This meant data would be incorrectly
>  carried forward from run to run.  Now those files are not read, so each
>  subprocess only writes its own data. Fixes `issue 510`_.

>- The ``coverage combine`` command will now fail if there are no data files to
>  combine. The combine changes in 4.2 meant that multiple combines could lose
>  data, leaving you with an empty .coverage data file. Fixes
>  `issue 525`_, `issue 412`_, `issue 516`_, and probably `issue 511`_.

>- Coverage.py wouldn&#39;t execute `sys.excepthook`_ when an exception happened in
>  your program.  Now it does, thanks to Andrew Hoos.  Closes `issue 535`_.

>- Branch coverage fixes:

>  - Branch coverage could misunderstand a finally clause on a try block that
>    never continued on to the following statement, as described in `issue
>    493`_.  This is now fixed. Thanks to Joe Doherty for the report and LoÃ¯c
>    Dachary for the fix.

>  - A while loop with a constant condition (while True) and a continue
>    statement would be mis-analyzed, as described in `issue 496`_. This is now
>    fixed, thanks to a bug report by Eli Skeggs and a fix by LoÃ¯c Dachary.

>  - While loops with constant conditions that were never executed could result
>    in a non-zero coverage report.  Artem Dayneko reported this in `issue
>    502`_, and LoÃ¯c Dachary provided the fix.

>- The HTML report now supports a ``--skip-covered`` option like the other
>  reporting commands.  Thanks, LoÃ¯c Dachary for the implementation, closing
>  `issue 433`_.

>- Options can now be read from a tox.ini file, if any. Like setup.cfg, sections
>  are prefixed with &quot;coverage:&quot;, so ``[run]`` options will be read from the
>  ``[coverage:run]`` section of tox.ini. Implements part of `issue 519`_.
>  Thanks, Stephen Finucane.

>- Specifying both ``--source`` and ``--include`` no longer silently ignores the
>  include setting, instead it fails with a message. Thanks, Nathan Land and
>  LoÃ¯c Dachary. Closes `issue 265`_.

>- The ``Coverage.combine`` method has a new parameter, ``strict=False``, to
>  support failing if there are no data files to combine.

>- When forking subprocesses, the coverage data files would have the same random
>  number appended to the file name. This didn&#39;t cause problems, because the
>  file names had the process id also, making collisions (nearly) impossible.
>  But it was disconcerting.  This is now fixed.

>- The text report now properly sizes headers when skipping some files, fixing
>  `issue 524`_. Thanks, Anthony Sottile and LoÃ¯c Dachary.

>- Coverage.py can now search .pex files for source, just as it can .zip and
>  .egg.  Thanks, Peter Ebden.

>- Data files are now about 15% smaller.

>- Improvements in the ``[run] debug`` setting:

>  - The &quot;dataio&quot; debug setting now also logs when data files are deleted during
>    combining or erasing.

>  - A new debug option, &quot;multiproc&quot;, for logging the behavior of
>    ``concurrency=multiprocessing``.

>  - If you used the debug options &quot;config&quot; and &quot;callers&quot; together, you&#39;d get a
>    call stack printed for every line in the multi-line config output. This is
>    now fixed.

>- Fixed an unusual bug involving multiple coding declarations affecting code
>  containing code in multi-line strings: `issue 529`_.

>- Coverage.py will no longer be misled into thinking that a plain file is a
>  package when interpreting ``--source`` options.  Thanks, Cosimo Lupo.

>- If you try to run a non-Python file with coverage.py, you will now get a more
>  useful error message. `Issue 514`_.

>- The default pragma regex changed slightly, but this will only matter to you
>  if you are deranged and use mixed-case pragmas.

>- Deal properly with non-ASCII file names in an ASCII-only world, `issue 533`_.

>- Programs that set Unicode configuration values could cause UnicodeErrors when
>  generating HTML reports.  Pytest-cov is one example.  This is now fixed.

>- Prevented deprecation warnings from configparser that happened in some
>  circumstances, closing `issue 530`_.

>- Corrected the name of the jquery.ba-throttle-debounce.js library. Thanks,
>  Ben Finney.  Closes `issue 505`_.

>- Testing against PyPy 5.6 and PyPy3 5.5.

>- Switched to pytest from nose for running the coverage.py tests.

>- Renamed AUTHORS.txt to CONTRIBUTORS.txt, since there are other ways to
>  contribute than by writing code. Also put the count of contributors into the
>  author string in setup.py, though this might be too cute.

>.. _sys.excepthook: https://docs.python.org/3/library/sys.htmlsys.excepthook
>.. _issue 265: https://bitbucket.org/ned/coveragepy/issues/265/when-using-source-include-is-silently
>.. _issue 412: https://bitbucket.org/ned/coveragepy/issues/412/coverage-combine-should-error-if-no
>.. _issue 433: https://bitbucket.org/ned/coveragepy/issues/433/coverage-html-does-not-suport-skip-covered
>.. _issue 493: https://bitbucket.org/ned/coveragepy/issues/493/confusing-branching-failure
>.. _issue 496: https://bitbucket.org/ned/coveragepy/issues/496/incorrect-coverage-with-branching-and
>.. _issue 502: https://bitbucket.org/ned/coveragepy/issues/502/incorrect-coverage-report-with-cover
>.. _issue 505: https://bitbucket.org/ned/coveragepy/issues/505/use-canonical-filename-for-debounce
>.. _issue 514: https://bitbucket.org/ned/coveragepy/issues/514/path-to-problem-file-not-reported-when
>.. _issue 510: https://bitbucket.org/ned/coveragepy/issues/510/erase-still-needed-in-42
>.. _issue 511: https://bitbucket.org/ned/coveragepy/issues/511/version-42-coverage-combine-empties
>.. _issue 516: https://bitbucket.org/ned/coveragepy/issues/516/running-coverage-combine-twice-deletes-all
>.. _issue 519: https://bitbucket.org/ned/coveragepy/issues/519/coverage-run-sections-in-toxini-or-as
>.. _issue 524: https://bitbucket.org/ned/coveragepy/issues/524/coverage-report-with-skip-covered-column
>.. _issue 525: https://bitbucket.org/ned/coveragepy/issues/525/coverage-combine-when-not-in-parallel-mode
>.. _issue 529: https://bitbucket.org/ned/coveragepy/issues/529/encoding-marker-may-only-appear-on-the
>.. _issue 530: https://bitbucket.org/ned/coveragepy/issues/530/deprecationwarning-you-passed-a-bytestring
>.. _issue 533: https://bitbucket.org/ned/coveragepy/issues/533/exception-on-unencodable-file-name
>.. _issue 535: https://bitbucket.org/ned/coveragepy/issues/535/sysexcepthook-is-not-called


>.. _changes_42:



>### 4.2

>--------------------------

>- Since ``concurrency=multiprocessing`` uses subprocesses, options specified on
>  the coverage.py command line will not be communicated down to them.  Only
>  options in the configuration file will apply to the subprocesses.
>  Previously, the options didn&#39;t apply to the subprocesses, but there was no
>  indication.  Now it is an error to use ``--concurrency=multiprocessing`` and
>  other run-affecting options on the command line.  This prevents
>  failures like those reported in `issue 495`_.

>- Filtering the HTML report is now faster, thanks to Ville SkyttÃ¤.

>.. _issue 495: https://bitbucket.org/ned/coveragepy/issues/495/branch-and-concurrency-are-conflicting




>### 4.2b1

>----------------------------

>Work from the PyCon 2016 Sprints!

>- BACKWARD INCOMPATIBILITY: the ``coverage combine`` command now ignores an
>  existing ``.coverage`` data file.  It used to include that file in its
>  combining.  This caused confusing results, and extra tox &quot;clean&quot; steps.  If
>  you want the old behavior, use the new ``coverage combine --append`` option.

>- The ``concurrency`` option can now take multiple values, to support programs
>  using multiprocessing and another library such as eventlet.  This is only
>  possible in the configuration file, not from the command line. The
>  configuration file is the only way for sub-processes to all run with the same
>  options.  Fixes `issue 484`_.  Thanks to Josh Williams for prototyping.

>- Using a ``concurrency`` setting of ``multiprocessing`` now implies
>  ``--parallel`` so that the main program is measured similarly to the
>  sub-processes.

>- When using `automatic subprocess measurement`_, running coverage commands
>  would create spurious data files.  This is now fixed, thanks to diagnosis and
>  testing by Dan Riti.  Closes `issue 492`_.

>- A new configuration option, ``report:sort``, controls what column of the
>  text report is used to sort the rows.  Thanks to Dan Wandschneider, this
>  closes `issue 199`_.

>- The HTML report has a more-visible indicator for which column is being
>  sorted.  Closes `issue 298`_, thanks to Josh Williams.

>- If the HTML report cannot find the source for a file, the message now
>  suggests using the ``-i`` flag to allow the report to continue. Closes
>  `issue 231`_, thanks, Nathan Land.

>- When reports are ignoring errors, there&#39;s now a warning if a file cannot be
>  parsed, rather than being silently ignored.  Closes `issue 396`_. Thanks,
>  Matthew Boehm.

>- A new option for ``coverage debug`` is available: ``coverage debug config``
>  shows the current configuration.  Closes `issue 454`_, thanks to Matthew
>  Boehm.

>- Running coverage as a module (``python -m coverage``) no longer shows the
>  program name as ``__main__.py``.  Fixes `issue 478`_.  Thanks, Scott Belden.

>- The `test_helpers` module has been moved into a separate pip-installable
>  package: `unittest-mixins`_.

>.. _automatic subprocess measurement: http://coverage.readthedocs.io/en/latest/subprocess.html
>.. _issue 199: https://bitbucket.org/ned/coveragepy/issues/199/add-a-way-to-sort-the-text-report
>.. _issue 231: https://bitbucket.org/ned/coveragepy/issues/231/various-default-behavior-in-report-phase
>.. _issue 298: https://bitbucket.org/ned/coveragepy/issues/298/show-in-html-report-that-the-columns-are
>.. _issue 396: https://bitbucket.org/ned/coveragepy/issues/396/coverage-xml-shouldnt-bail-out-on-parse
>.. _issue 454: https://bitbucket.org/ned/coveragepy/issues/454/coverage-debug-config-should-be
>.. _issue 478: https://bitbucket.org/ned/coveragepy/issues/478/help-shows-silly-program-name-when-running
>.. _issue 484: https://bitbucket.org/ned/coveragepy/issues/484/multiprocessing-greenlet-concurrency
>.. _issue 492: https://bitbucket.org/ned/coveragepy/issues/492/subprocess-coverage-strange-detection-of
>.. _unittest-mixins: https://pypi.python.org/pypi/unittest-mixins


>.. _changes_41:



>### 4.1

>--------------------------

>- The internal attribute `Reporter.file_reporters` was removed in 4.1b3.  It
>  should have come has no surprise that there were third-party tools out there
>  using that attribute.  It has been restored, but with a deprecation warning.




>### 4.1b3

>----------------------------

>- When running your program, execution can jump from an ``except X:`` line to
>  some other line when an exception other than ``X`` happens.  This jump is no
>  longer considered a branch when measuring branch coverage.

>- When measuring branch coverage, ``yield`` statements that were never resumed
>  were incorrectly marked as missing, as reported in `issue 440`_.  This is now
>  fixed.

>- During branch coverage of single-line callables like lambdas and generator
>  expressions, coverage.py can now distinguish between them never being called,
>  or being called but not completed.  Fixes `issue 90`_, `issue 460`_ and
>  `issue 475`_.

>- The HTML report now has a map of the file along the rightmost edge of the
>  page, giving an overview of where the missed lines are.  Thanks, Dmitry
>  Shishov.

>- The HTML report now uses different monospaced fonts, favoring Consolas over
>  Courier.  Along the way, `issue 472`_ about not properly handling one-space
>  indents was fixed.  The index page also has slightly different styling, to
>  try to make the clickable detail pages more apparent.

>- Missing branches reported with ``coverage report -m`` will now say ``-&gt;exit``
>  for missed branches to the exit of a function, rather than a negative number.
>  Fixes `issue 469`_.

>- ``coverage --help`` and ``coverage --version`` now mention which tracer is
>  installed, to help diagnose problems. The docs mention which features need
>  the C extension. (`issue 479`_)

>- Officially support PyPy 5.1, which required no changes, just updates to the
>  docs.

>- The `Coverage.report` function had two parameters with non-None defaults,
>  which have been changed.  `show_missing` used to default to True, but now
>  defaults to None.  If you had been calling `Coverage.report` without
>  specifying `show_missing`, you&#39;ll need to explicitly set it to True to keep
>  the same behavior.  `skip_covered` used to default to False. It is now None,
>  which doesn&#39;t change the behavior.  This fixes `issue 485`_.

>- It&#39;s never been possible to pass a namespace module to one of the analysis
>  functions, but now at least we raise a more specific error message, rather
>  than getting confused. (`issue 456`_)

>- The `coverage.process_startup` function now returns the `Coverage` instance
>  it creates, as suggested in `issue 481`_.

>- Make a small tweak to how we compare threads, to avoid buggy custom
>  comparison code in thread classes. (`issue 245`_)

>.. _issue 90: https://bitbucket.org/ned/coveragepy/issues/90/lambda-expression-confuses-branch
>.. _issue 245: https://bitbucket.org/ned/coveragepy/issues/245/change-solution-for-issue-164
>.. _issue 440: https://bitbucket.org/ned/coveragepy/issues/440/yielded-twisted-failure-marked-as-missed
>.. _issue 456: https://bitbucket.org/ned/coveragepy/issues/456/coverage-breaks-with-implicit-namespaces
>.. _issue 460: https://bitbucket.org/ned/coveragepy/issues/460/confusing-html-report-for-certain-partial
>.. _issue 469: https://bitbucket.org/ned/coveragepy/issues/469/strange-1-line-number-in-branch-coverage
>.. _issue 472: https://bitbucket.org/ned/coveragepy/issues/472/html-report-indents-incorrectly-for-one
>.. _issue 475: https://bitbucket.org/ned/coveragepy/issues/475/generator-expression-is-marked-as-not
>.. _issue 479: https://bitbucket.org/ned/coveragepy/issues/479/clarify-the-need-for-the-c-extension
>.. _issue 481: https://bitbucket.org/ned/coveragepy/issues/481/asyncioprocesspoolexecutor-tracing-not
>.. _issue 485: https://bitbucket.org/ned/coveragepy/issues/485/coveragereport-ignores-show_missing-and




>### 4.1b2

>----------------------------

>- Problems with the new branch measurement in 4.1 beta 1 were fixed:

>  - Class docstrings were considered executable.  Now they no longer are.

>  - ``yield from`` and ``await`` were considered returns from functions, since
>    they could tranfer control to the caller.  This produced unhelpful &quot;missing
>    branch&quot; reports in a number of circumstances.  Now they no longer are
>    considered returns.

>  - In unusual situations, a missing branch to a negative number was reported.
>    This has been fixed, closing `issue 466`_.

>- The XML report now produces correct package names for modules found in
>  directories specified with ``source=``.  Fixes `issue 465`_.

>- ``coverage report`` won&#39;t produce trailing whitespace.

>.. _issue 465: https://bitbucket.org/ned/coveragepy/issues/465/coveragexml-produces-package-names-with-an
>.. _issue 466: https://bitbucket.org/ned/coveragepy/issues/466/impossible-missed-branch-to-a-negative




>### 4.1b1

>----------------------------

>- Branch analysis has been rewritten: it used to be based on bytecode, but now
>  uses AST analysis.  This has changed a number of things:

>  - More code paths are now considered runnable, especially in
>    ``try``/``except`` structures.  This may mean that coverage.py will
>    identify more code paths as uncovered.  This could either raise or lower
>    your overall coverage number.

>  - Python 3.5&#39;s ``async`` and ``await`` keywords are properly supported,
>    fixing `issue 434`_.

>  - Some long-standing branch coverage bugs were fixed:

>    - `issue 129`_: functions with only a docstring for a body would
>      incorrectly report a missing branch on the ``def`` line.

>    - `issue 212`_: code in an ``except`` block could be incorrectly marked as
>      a missing branch.

>    - `issue 146`_: context managers (``with`` statements) in a loop or ``try``
>      block could confuse the branch measurement, reporting incorrect partial
>      branches.

>    - `issue 422`_: in Python 3.5, an actual partial branch could be marked as
>      complete.

>- Pragmas to disable coverage measurement can now be used on decorator lines,
>  and they will apply to the entire function or class being decorated.  This
>  implements the feature requested in `issue 131`_.

>- Multiprocessing support is now available on Windows.  Thanks, Rodrigue
>  Cloutier.

>- Files with two encoding declarations are properly supported, fixing
>  `issue 453`_. Thanks, Max Linke.

>- Non-ascii characters in regexes in the configuration file worked in 3.7, but
>  stopped working in 4.0.  Now they work again, closing `issue 455`_.

>- Form-feed characters would prevent accurate determination of the beginning of
>  statements in the rest of the file.  This is now fixed, closing `issue 461`_.

>.. _issue 129: https://bitbucket.org/ned/coveragepy/issues/129/misleading-branch-coverage-of-empty
>.. _issue 131: https://bitbucket.org/ned/coveragepy/issues/131/pragma-on-a-decorator-line-should-affect
>.. _issue 146: https://bitbucket.org/ned/coveragepy/issues/146/context-managers-confuse-branch-coverage
>.. _issue 212: https://bitbucket.org/ned/coveragepy/issues/212/coverage-erroneously-reports-partial
>.. _issue 422: https://bitbucket.org/ned/coveragepy/issues/422/python35-partial-branch-marked-as-fully
>.. _issue 434: https://bitbucket.org/ned/coveragepy/issues/434/indexerror-in-python-35
>.. _issue 453: https://bitbucket.org/ned/coveragepy/issues/453/source-code-encoding-can-only-be-specified
>.. _issue 455: https://bitbucket.org/ned/coveragepy/issues/455/unusual-exclusions-stopped-working-in
>.. _issue 461: https://bitbucket.org/ned/coveragepy/issues/461/multiline-asserts-need-too-many-pragma


>.. _changes_403:



>### 4.0.3

>----------------------------

>- Fixed a mysterious problem that manifested in different ways: sometimes
>  hanging the process (`issue 420`_), sometimes making database connections
>  fail (`issue 445`_).

>- The XML report now has correct ``&lt;source&gt;`` elements when using a
>  ``--source=`` option somewhere besides the current directory.  This fixes
>  `issue 439`_. Thanks, Arcady Ivanov.

>- Fixed an unusual edge case of detecting source encodings, described in
>  `issue 443`_.

>- Help messages that mention the command to use now properly use the actual
>  command name, which might be different than &quot;coverage&quot;.  Thanks to Ben
>  Finney, this closes `issue 438`_.

>.. _issue 420: https://bitbucket.org/ned/coveragepy/issues/420/coverage-40-hangs-indefinitely-on-python27
>.. _issue 438: https://bitbucket.org/ned/coveragepy/issues/438/parameterise-coverage-command-name
>.. _issue 439: https://bitbucket.org/ned/coveragepy/issues/439/incorrect-cobertura-file-sources-generated
>.. _issue 443: https://bitbucket.org/ned/coveragepy/issues/443/coverage-gets-confused-when-encoding
>.. _issue 445: https://bitbucket.org/ned/coveragepy/issues/445/django-app-cannot-connect-to-cassandra


>.. _changes_402:



>### 4.0.2

>----------------------------

>- More work on supporting unusually encoded source. Fixed `issue 431`_.

>- Files or directories with non-ASCII characters are now handled properly,
>  fixing `issue 432`_.

>- Setting a trace function with sys.settrace was broken by a change in 4.0.1,
>  as reported in `issue 436`_.  This is now fixed.

>- Officially support PyPy 4.0, which required no changes, just updates to the
>  docs.

>.. _issue 431: https://bitbucket.org/ned/coveragepy/issues/431/couldnt-parse-python-file-with-cp1252
>.. _issue 432: https://bitbucket.org/ned/coveragepy/issues/432/path-with-unicode-characters-various
>.. _issue 436: https://bitbucket.org/ned/coveragepy/issues/436/disabled-coverage-ctracer-may-rise-from


>.. _changes_401:



>### 4.0.1

>----------------------------

>- When combining data files, unreadable files will now generate a warning
>  instead of failing the command.  This is more in line with the older
>  coverage.py v3.7.1 behavior, which silently ignored unreadable files.
>  Prompted by `issue 418`_.

>- The --skip-covered option would skip reporting on 100% covered files, but
>  also skipped them when calculating total coverage.  This was wrong, it should
>  only remove lines from the report, not change the final answer.  This is now
>  fixed, closing `issue 423`_.

>- In 4.0, the data file recorded a summary of the system on which it was run.
>  Combined data files would keep all of those summaries.  This could lead to
>  enormous data files consisting of mostly repetitive useless information. That
>  summary is now gone, fixing `issue 415`_.  If you want summary information,
>  get in touch, and we&#39;ll figure out a better way to do it.

>- Test suites that mocked os.path.exists would experience strange failures, due
>  to coverage.py using their mock inadvertently.  This is now fixed, closing
>  `issue 416`_.

>- Importing a ``__init__`` module explicitly would lead to an error:
>  ``AttributeError: &#39;module&#39; object has no attribute &#39;__path__&#39;``, as reported
>  in `issue 410`_.  This is now fixed.

>- Code that uses ``sys.settrace(sys.gettrace())`` used to incur a more than 2x
>  speed penalty.  Now there&#39;s no penalty at all. Fixes `issue 397`_.

>- Pyexpat C code will no longer be recorded as a source file, fixing
>  `issue 419`_.

>- The source kit now contains all of the files needed to have a complete source
>  tree, re-fixing `issue 137`_ and closing `issue 281`_.

>.. _issue 281: https://bitbucket.org/ned/coveragepy/issues/281/supply-scripts-for-testing-in-the
>.. _issue 397: https://bitbucket.org/ned/coveragepy/issues/397/stopping-and-resuming-coverage-with
>.. _issue 410: https://bitbucket.org/ned/coveragepy/issues/410/attributeerror-module-object-has-no
>.. _issue 415: https://bitbucket.org/ned/coveragepy/issues/415/repeated-coveragedataupdates-cause
>.. _issue 416: https://bitbucket.org/ned/coveragepy/issues/416/mocking-ospathexists-causes-failures
>.. _issue 418: https://bitbucket.org/ned/coveragepy/issues/418/json-parse-error
>.. _issue 419: https://bitbucket.org/ned/coveragepy/issues/419/nosource-no-source-for-code-path-to-c
>.. _issue 423: https://bitbucket.org/ned/coveragepy/issues/423/skip_covered-changes-reported-total


>.. _changes_40:



>### 4.0

>--------------------------



>### 4.0b3

>----------------------------

>- Reporting on an unmeasured file would fail with a traceback.  This is now
>  fixed, closing `issue 403`_.

>- The Jenkins ShiningPanda plugin looks for an obsolete file name to find the
>  HTML reports to publish, so it was failing under coverage.py 4.0.  Now we
>  create that file if we are running under Jenkins, to keep things working
>  smoothly. `issue 404`_.

>- Kits used to include tests and docs, but didn&#39;t install them anywhere, or
>  provide all of the supporting tools to make them useful.  Kits no longer
>  include tests and docs.  If you were using them from the older packages, get
>  in touch and help me understand how.

>.. _issue 403: https://bitbucket.org/ned/coveragepy/issues/403/hasherupdate-fails-with-typeerror-nonetype
>.. _issue 404: https://bitbucket.org/ned/coveragepy/issues/404/shiningpanda-jenkins-plugin-cant-find-html




>### 4.0b2

>----------------------------

>- 4.0b1 broke ``--append`` creating new data files.  This is now fixed, closing
>  `issue 392`_.

>- ``py.test --cov`` can write empty data, then touch files due to ``--source``,
>  which made coverage.py mistakenly force the data file to record lines instead
>  of arcs.  This would lead to a &quot;Can&#39;t combine line data with arc data&quot; error
>  message.  This is now fixed, and changed some method names in the
>  CoverageData interface.  Fixes `issue 399`_.

>- `CoverageData.read_fileobj` and `CoverageData.write_fileobj` replace the
>  `.read` and `.write` methods, and are now properly inverses of each other.

>- When using ``report --skip-covered``, a message will now be included in the
>  report output indicating how many files were skipped, and if all files are
>  skipped, coverage.py won&#39;t accidentally scold you for having no data to
>  report.  Thanks, Krystian Kichewko.

>- A new conversion utility has been added:  ``python -m coverage.pickle2json``
>  will convert v3.x pickle data files to v4.x JSON data files.  Thanks,
>  Alexander Todorov.  Closes `issue 395`_.

>- A new version identifier is available, `coverage.version_info`, a plain tuple
>  of values similar to `sys.version_info`_.

>.. _issue 392: https://bitbucket.org/ned/coveragepy/issues/392/run-append-doesnt-create-coverage-file
>.. _issue 395: https://bitbucket.org/ned/coveragepy/issues/395/rfe-read-pickled-files-as-well-for
>.. _issue 399: https://bitbucket.org/ned/coveragepy/issues/399/coverageexception-cant-combine-line-data
>.. _sys.version_info: https://docs.python.org/3/library/sys.htmlsys.version_info




>### 4.0b1

>----------------------------

>- Coverage.py is now licensed under the Apache 2.0 license.  See NOTICE.txt for
>  details.  Closes `issue 313`_.

>- The data storage has been completely revamped.  The data file is now
>  JSON-based instead of a pickle, closing `issue 236`_.  The `CoverageData`
>  class is now a public supported documented API to the data file.

>- A new configuration option, ``[run] note``, lets you set a note that will be
>  stored in the `runs` section of the data file.  You can use this to annotate
>  the data file with any information you like.

>- Unrecognized configuration options will now print an error message and stop
>  coverage.py.  This should help prevent configuration mistakes from passing
>  silently.  Finishes `issue 386`_.

>- In parallel mode, ``coverage erase`` will now delete all of the data files,
>  fixing `issue 262`_.

>- Coverage.py now accepts a directory name for ``coverage run`` and will run a
>  ``__main__.py`` found there, just like Python will.  Fixes `issue 252`_.
>  Thanks, Dmitry Trofimov.

>- The XML report now includes a ``missing-branches`` attribute.  Thanks, Steve
>  Peak.  This is not a part of the Cobertura DTD, so the XML report no longer
>  references the DTD.

>- Missing branches in the HTML report now have a bit more information in the
>  right-hand annotations.  Hopefully this will make their meaning clearer.

>- All the reporting functions now behave the same if no data had been
>  collected, exiting with a status code of 1.  Fixed ``fail_under`` to be
>  applied even when the report is empty.  Thanks, Ionel Cristian MÄrieÈ.

>- Plugins are now initialized differently.  Instead of looking for a class
>  called ``Plugin``, coverage.py looks for a function called ``coverage_init``.

>- A file-tracing plugin can now ask to have built-in Python reporting by
>  returning `&quot;python&quot;` from its `file_reporter()` method.

>- Code that was executed with `exec` would be mis-attributed to the file that
>  called it.  This is now fixed, closing `issue 380`_.

>- The ability to use item access on `Coverage.config` (introduced in 4.0a2) has
>  been changed to a more explicit `Coverage.get_option` and
>  `Coverage.set_option` API.

>- The ``Coverage.use_cache`` method is no longer supported.

>- The private method ``Coverage._harvest_data`` is now called
>  ``Coverage.get_data``, and returns the ``CoverageData`` containing the
>  collected data.

>- The project is consistently referred to as &quot;coverage.py&quot; throughout the code
>  and the documentation, closing `issue 275`_.

>- Combining data files with an explicit configuration file was broken in 4.0a6,
>  but now works again, closing `issue 385`_.

>- ``coverage combine`` now accepts files as well as directories.

>- The speed is back to 3.7.1 levels, after having slowed down due to plugin
>  support, finishing up `issue 387`_.

>.. _issue 236: https://bitbucket.org/ned/coveragepy/issues/236/pickles-are-bad-and-you-should-feel-bad
>.. _issue 252: https://bitbucket.org/ned/coveragepy/issues/252/coverage-wont-run-a-program-with
>.. _issue 262: https://bitbucket.org/ned/coveragepy/issues/262/when-parallel-true-erase-should-erase-all
>.. _issue 275: https://bitbucket.org/ned/coveragepy/issues/275/refer-consistently-to-project-as-coverage
>.. _issue 313: https://bitbucket.org/ned/coveragepy/issues/313/add-license-file-containing-2-3-or-4
>.. _issue 380: https://bitbucket.org/ned/coveragepy/issues/380/code-executed-by-exec-excluded-from
>.. _issue 385: https://bitbucket.org/ned/coveragepy/issues/385/coverage-combine-doesnt-work-with-rcfile
>.. _issue 386: https://bitbucket.org/ned/coveragepy/issues/386/error-on-unrecognised-configuration
>.. _issue 387: https://bitbucket.org/ned/coveragepy/issues/387/performance-degradation-from-371-to-40

>.. 40 issues closed in 4.0 below here




>### 4.0a6

>----------------------------

>- Python 3.5b2 and PyPy 2.6.0 are supported.

>- The original module-level function interface to coverage.py is no longer
>  supported.  You must now create a ``coverage.Coverage`` object, and use
>  methods on it.

>- The ``coverage combine`` command now accepts any number of directories as
>  arguments, and will combine all the data files from those directories.  This
>  means you don&#39;t have to copy the files to one directory before combining.
>  Thanks, Christine Lytwynec.  Finishes `issue 354`_.

>- Branch coverage couldn&#39;t properly handle certain extremely long files. This
>  is now fixed (`issue 359`_).

>- Branch coverage didn&#39;t understand yield statements properly.  Mickie Betz
>  persisted in pursuing this despite Ned&#39;s pessimism.  Fixes `issue 308`_ and
>  `issue 324`_.

>- The COVERAGE_DEBUG environment variable can be used to set the
>  ``[run] debug`` configuration option to control what internal operations are
>  logged.

>- HTML reports were truncated at formfeed characters.  This is now fixed
>  (`issue 360`_).  It&#39;s always fun when the problem is due to a `bug in the
>  Python standard library &lt;http://bugs.python.org/issue19035&gt;`_.

>- Files with incorrect encoding declaration comments are no longer ignored by
>  the reporting commands, fixing `issue 351`_.

>- HTML reports now include a timestamp in the footer, closing `issue 299`_.
>  Thanks, Conrad Ho.

>- HTML reports now begrudgingly use double-quotes rather than single quotes,
>  because there are &quot;software engineers&quot; out there writing tools that read HTML
>  and somehow have no idea that single quotes exist.  Capitulates to the absurd
>  `issue 361`_.  Thanks, Jon Chappell.

>- The ``coverage annotate`` command now handles non-ASCII characters properly,
>  closing `issue 363`_.  Thanks, Leonardo Pistone.

>- Drive letters on Windows were not normalized correctly, now they are. Thanks,
>  Ionel Cristian MÄrieÈ.

>- Plugin support had some bugs fixed, closing `issue 374`_ and `issue 375`_.
>  Thanks, Stefan Behnel.

>.. _issue 299: https://bitbucket.org/ned/coveragepy/issues/299/inserted-created-on-yyyy-mm-dd-hh-mm-in
>.. _issue 308: https://bitbucket.org/ned/coveragepy/issues/308/yield-lambda-branch-coverage
>.. _issue 324: https://bitbucket.org/ned/coveragepy/issues/324/yield-in-loop-confuses-branch-coverage
>.. _issue 351: https://bitbucket.org/ned/coveragepy/issues/351/files-with-incorrect-encoding-are-ignored
>.. _issue 354: https://bitbucket.org/ned/coveragepy/issues/354/coverage-combine-should-take-a-list-of
>.. _issue 359: https://bitbucket.org/ned/coveragepy/issues/359/xml-report-chunk-error
>.. _issue 360: https://bitbucket.org/ned/coveragepy/issues/360/html-reports-get-confused-by-l-in-the-code
>.. _issue 361: https://bitbucket.org/ned/coveragepy/issues/361/use-double-quotes-in-html-output-to
>.. _issue 363: https://bitbucket.org/ned/coveragepy/issues/363/annotate-command-hits-unicode-happy-fun
>.. _issue 374: https://bitbucket.org/ned/coveragepy/issues/374/c-tracer-lookups-fail-in
>.. _issue 375: https://bitbucket.org/ned/coveragepy/issues/375/ctracer_handle_return-reads-byte-code




>### 4.0a5

>----------------------------

>- Plugin support is now implemented in the C tracer instead of the Python
>  tracer. This greatly improves the speed of tracing projects using plugins.

>- Coverage.py now always adds the current directory to sys.path, so that
>  plugins can import files in the current directory (`issue 358`_).

>- If the `config_file` argument to the Coverage constructor is specified as
>  &quot;.coveragerc&quot;, it is treated as if it were True.  This means setup.cfg is
>  also examined, and a missing file is not considered an error (`issue 357`_).

>- Wildly experimental: support for measuring processes started by the
>  multiprocessing module.  To use, set ``--concurrency=multiprocessing``,
>  either on the command line or in the .coveragerc file (`issue 117`_). Thanks,
>  Eduardo Schettino.  Currently, this does not work on Windows.

>- A new warning is possible, if a desired file isn&#39;t measured because it was
>  imported before coverage.py was started (`issue 353`_).

>- The `coverage.process_startup` function now will start coverage measurement
>  only once, no matter how many times it is called.  This fixes problems due
>  to unusual virtualenv configurations (`issue 340`_).

>- Added 3.5.0a1 to the list of supported CPython versions.

>.. _issue 117: https://bitbucket.org/ned/coveragepy/issues/117/enable-coverage-measurement-of-code-run-by
>.. _issue 340: https://bitbucket.org/ned/coveragepy/issues/340/keyerror-subpy
>.. _issue 353: https://bitbucket.org/ned/coveragepy/issues/353/40a3-introduces-an-unexpected-third-case
>.. _issue 357: https://bitbucket.org/ned/coveragepy/issues/357/behavior-changed-when-coveragerc-is
>.. _issue 358: https://bitbucket.org/ned/coveragepy/issues/358/all-coverage-commands-should-adjust




>### 4.0a4

>----------------------------

>- Plugins can now provide sys_info for debugging output.

>- Started plugins documentation.

>- Prepared to move the docs to readthedocs.org.




>### 4.0a3

>----------------------------

>- Reports now use file names with extensions.  Previously, a report would
>  describe a/b/c.py as &quot;a/b/c&quot;.  Now it is shown as &quot;a/b/c.py&quot;.  This allows
>  for better support of non-Python files, and also fixed `issue 69`_.

>- The XML report now reports each directory as a package again.  This was a bad
>  regression, I apologize.  This was reported in `issue 235`_, which is now
>  fixed.

>- A new configuration option for the XML report: ``[xml] package_depth``
>  controls which directories are identified as packages in the report.
>  Directories deeper than this depth are not reported as packages.
>  The default is that all directories are reported as packages.
>  Thanks, Lex Berezhny.

>- When looking for the source for a frame, check if the file exists. On
>  Windows, .pyw files are no longer recorded as .py files. Along the way, this
>  fixed `issue 290`_.

>- Empty files are now reported as 100% covered in the XML report, not 0%
>  covered (`issue 345`_).

>- Regexes in the configuration file are now compiled as soon as they are read,
>  to provide error messages earlier (`issue 349`_).

>.. _issue 69: https://bitbucket.org/ned/coveragepy/issues/69/coverage-html-overwrite-files-that-doesnt
>.. _issue 235: https://bitbucket.org/ned/coveragepy/issues/235/package-name-is-missing-in-xml-report
>.. _issue 290: https://bitbucket.org/ned/coveragepy/issues/290/running-programmatically-with-pyw-files
>.. _issue 345: https://bitbucket.org/ned/coveragepy/issues/345/xml-reports-line-rate-0-for-empty-files
>.. _issue 349: https://bitbucket.org/ned/coveragepy/issues/349/bad-regex-in-config-should-get-an-earlier




>### 4.0a2

>----------------------------

>- Officially support PyPy 2.4, and PyPy3 2.4.  Drop support for
>  CPython 3.2 and older versions of PyPy.  The code won&#39;t work on CPython 3.2.
>  It will probably still work on older versions of PyPy, but I&#39;m not testing
>  against them.

>- Plugins!

>- The original command line switches (`-x` to run a program, etc) are no
>  longer supported.

>- A new option: `coverage report --skip-covered` will reduce the number of
>  files reported by skipping files with 100% coverage.  Thanks, Krystian
>  Kichewko.  This means that empty `__init__.py` files will be skipped, since
>  they are 100% covered, closing `issue 315`_.

>- You can now specify the ``--fail-under`` option in the ``.coveragerc`` file
>  as the ``[report] fail_under`` option.  This closes `issue 314`_.

>- The ``COVERAGE_OPTIONS`` environment variable is no longer supported.  It was
>  a hack for ``--timid`` before configuration files were available.

>- The HTML report now has filtering.  Type text into the Filter box on the
>  index page, and only modules with that text in the name will be shown.
>  Thanks, Danny Allen.

>- The textual report and the HTML report used to report partial branches
>  differently for no good reason.  Now the text report&#39;s &quot;missing branches&quot;
>  column is a &quot;partial branches&quot; column so that both reports show the same
>  numbers.  This closes `issue 342`_.

>- If you specify a ``--rcfile`` that cannot be read, you will get an error
>  message.  Fixes `issue 343`_.

>- The ``--debug`` switch can now be used on any command.

>- You can now programmatically adjust the configuration of coverage.py by
>  setting items on `Coverage.config` after construction.

>- A module run with ``-m`` can be used as the argument to ``--source``, fixing
>  `issue 328`_.  Thanks, Buck Evan.

>- The regex for matching exclusion pragmas has been fixed to allow more kinds
>  of whitespace, fixing `issue 334`_.

>- Made some PyPy-specific tweaks to improve speed under PyPy.  Thanks, Alex
>  Gaynor.

>- In some cases, with a source file missing a final newline, coverage.py would
>  count statements incorrectly.  This is now fixed, closing `issue 293`_.

>- The status.dat file that HTML reports use to avoid re-creating files that
>  haven&#39;t changed is now a JSON file instead of a pickle file.  This obviates
>  `issue 287`_ and `issue 237`_.

>.. _issue 237: https://bitbucket.org/ned/coveragepy/issues/237/htmlcov-with-corrupt-statusdat
>.. _issue 287: https://bitbucket.org/ned/coveragepy/issues/287/htmlpy-doesnt-specify-pickle-protocol
>.. _issue 293: https://bitbucket.org/ned/coveragepy/issues/293/number-of-statement-detection-wrong-if-no
>.. _issue 314: https://bitbucket.org/ned/coveragepy/issues/314/fail_under-param-not-working-in-coveragerc
>.. _issue 315: https://bitbucket.org/ned/coveragepy/issues/315/option-to-omit-empty-files-eg-__init__py
>.. _issue 328: https://bitbucket.org/ned/coveragepy/issues/328/misbehavior-in-run-source
>.. _issue 334: https://bitbucket.org/ned/coveragepy/issues/334/pragma-not-recognized-if-tab-character
>.. _issue 342: https://bitbucket.org/ned/coveragepy/issues/342/console-and-html-coverage-reports-differ
>.. _issue 343: https://bitbucket.org/ned/coveragepy/issues/343/an-explicitly-named-non-existent-config




>### 4.0a1

>----------------------------

>- Python versions supported are now CPython 2.6, 2.7, 3.2, 3.3, and 3.4, and
>  PyPy 2.2.

>- Gevent, eventlet, and greenlet are now supported, closing `issue 149`_.
>  The ``concurrency`` setting specifies the concurrency library in use.  Huge
>  thanks to Peter Portante for initial implementation, and to Joe Jevnik for
>  the final insight that completed the work.

>- Options are now also read from a setup.cfg file, if any.  Sections are
>  prefixed with &quot;coverage:&quot;, so the ``[run]`` options will be read from the
>  ``[coverage:run]`` section of setup.cfg.  Finishes `issue 304`_.

>- The ``report -m`` command can now show missing branches when reporting on
>  branch coverage.  Thanks, Steve Leonard. Closes `issue 230`_.

>- The XML report now contains a &lt;source&gt; element, fixing `issue 94`_.  Thanks
>  Stan Hu.

>- The class defined in the coverage module is now called ``Coverage`` instead
>  of ``coverage``, though the old name still works, for backward compatibility.

>- The ``fail-under`` value is now rounded the same as reported results,
>  preventing paradoxical results, fixing `issue 284`_.

>- The XML report will now create the output directory if need be, fixing
>  `issue 285`_.  Thanks, Chris Rose.

>- HTML reports no longer raise UnicodeDecodeError if a Python file has
>  undecodable characters, fixing `issue 303`_ and `issue 331`_.

>- The annotate command will now annotate all files, not just ones relative to
>  the current directory, fixing `issue 57`_.

>- The coverage module no longer causes deprecation warnings on Python 3.4 by
>  importing the imp module, fixing `issue 305`_.

>- Encoding declarations in source files are only considered if they are truly
>  comments.  Thanks, Anthony Sottile.

>.. _issue 57: https://bitbucket.org/ned/coveragepy/issues/57/annotate-command-fails-to-annotate-many
>.. _issue 94: https://bitbucket.org/ned/coveragepy/issues/94/coverage-xml-doesnt-produce-sources
>.. _issue 149: https://bitbucket.org/ned/coveragepy/issues/149/coverage-gevent-looks-broken
>.. _issue 230: https://bitbucket.org/ned/coveragepy/issues/230/show-line-no-for-missing-branches-in
>.. _issue 284: https://bitbucket.org/ned/coveragepy/issues/284/fail-under-should-show-more-precision
>.. _issue 285: https://bitbucket.org/ned/coveragepy/issues/285/xml-report-fails-if-output-file-directory
>.. _issue 303: https://bitbucket.org/ned/coveragepy/issues/303/unicodedecodeerror
>.. _issue 304: https://bitbucket.org/ned/coveragepy/issues/304/attempt-to-get-configuration-from-setupcfg
>.. _issue 305: https://bitbucket.org/ned/coveragepy/issues/305/pendingdeprecationwarning-the-imp-module
>.. _issue 331: https://bitbucket.org/ned/coveragepy/issues/331/failure-of-encoding-detection-on-python2


>.. _changes_371:



>### 3.7.1

>----------------------------

>- Improved the speed of HTML report generation by about 20%.

>- Fixed the mechanism for finding OS-installed static files for the HTML report
>  so that it will actually find OS-installed static files.


>.. _changes_37:



>### 3.7

>--------------------------

>- Added the ``--debug`` switch to ``coverage run``.  It accepts a list of
>  options indicating the type of internal activity to log to stderr.

>- Improved the branch coverage facility, fixing `issue 92`_ and `issue 175`_.

>- Running code with ``coverage run -m`` now behaves more like Python does,
>  setting sys.path properly, which fixes `issue 207`_ and `issue 242`_.

>- Coverage.py can now run .pyc files directly, closing `issue 264`_.

>- Coverage.py properly supports .pyw files, fixing `issue 261`_.

>- Omitting files within a tree specified with the ``source`` option would
>  cause them to be incorrectly marked as unexecuted, as described in
>  `issue 218`_.  This is now fixed.

>- When specifying paths to alias together during data combining, you can now
>  specify relative paths, fixing `issue 267`_.

>- Most file paths can now be specified with username expansion (``~/src``, or
>  ``~build/src``, for example), and with environment variable expansion
>  (``build/$BUILDNUM/src``).

>- Trying to create an XML report with no files to report on, would cause a
>  ZeroDivideError, but no longer does, fixing `issue 250`_.

>- When running a threaded program under the Python tracer, coverage.py no
>  longer issues a spurious warning about the trace function changing: &quot;Trace
>  function changed, measurement is likely wrong: None.&quot;  This fixes `issue
>  164`_.

>- Static files necessary for HTML reports are found in system-installed places,
>  to ease OS-level packaging of coverage.py.  Closes `issue 259`_.

>- Source files with encoding declarations, but a blank first line, were not
>  decoded properly.  Now they are.  Thanks, Roger Hu.

>- The source kit now includes the ``__main__.py`` file in the root coverage
>  directory, fixing `issue 255`_.

>.. _issue 92: https://bitbucket.org/ned/coveragepy/issues/92/finally-clauses-arent-treated-properly-in
>.. _issue 164: https://bitbucket.org/ned/coveragepy/issues/164/trace-function-changed-warning-when-using
>.. _issue 175: https://bitbucket.org/ned/coveragepy/issues/175/branch-coverage-gets-confused-in-certain
>.. _issue 207: https://bitbucket.org/ned/coveragepy/issues/207/run-m-cannot-find-module-or-package-in
>.. _issue 242: https://bitbucket.org/ned/coveragepy/issues/242/running-a-two-level-package-doesnt-work
>.. _issue 218: https://bitbucket.org/ned/coveragepy/issues/218/run-command-does-not-respect-the-omit-flag
>.. _issue 250: https://bitbucket.org/ned/coveragepy/issues/250/uncaught-zerodivisionerror-when-generating
>.. _issue 255: https://bitbucket.org/ned/coveragepy/issues/255/directory-level-__main__py-not-included-in
>.. _issue 259: https://bitbucket.org/ned/coveragepy/issues/259/allow-use-of-system-installed-third-party
>.. _issue 261: https://bitbucket.org/ned/coveragepy/issues/261/pyw-files-arent-reported-properly
>.. _issue 264: https://bitbucket.org/ned/coveragepy/issues/264/coverage-wont-run-pyc-files
>.. _issue 267: https://bitbucket.org/ned/coveragepy/issues/267/relative-path-aliases-dont-work


>.. _changes_36:



>### 3.6

>--------------------------

>- Added a page to the docs about troublesome situations, closing `issue 226`_,
>  and added some info to the TODO file, closing `issue 227`_.

>.. _issue 226: https://bitbucket.org/ned/coveragepy/issues/226/make-readme-section-to-describe-when
>.. _issue 227: https://bitbucket.org/ned/coveragepy/issues/227/update-todo




>### 3.6b3

>----------------------------

>- Beta 2 broke the nose plugin. It&#39;s fixed again, closing `issue 224`_.

>.. _issue 224: https://bitbucket.org/ned/coveragepy/issues/224/36b2-breaks-nosexcover




>### 3.6b2

>----------------------------

>- Coverage.py runs on Python 2.3 and 2.4 again. It was broken in 3.6b1.

>- The C extension is optionally compiled using a different more widely-used
>  technique, taking another stab at fixing `issue 80`_ once and for all.

>- Combining data files would create entries for phantom files if used with
>  ``source`` and path aliases.  It no longer does.

>- ``debug sys`` now shows the configuration file path that was read.

>- If an oddly-behaved package claims that code came from an empty-string
>  file name, coverage.py no longer associates it with the directory name,
>  fixing `issue 221`_.

>.. _issue 221: https://bitbucket.org/ned/coveragepy/issues/221/coveragepy-incompatible-with-pyratemp




>### 3.6b1

>----------------------------

>- Wildcards in ``include=`` and ``omit=`` arguments were not handled properly
>  in reporting functions, though they were when running.  Now they are handled
>  uniformly, closing `issue 143`_ and `issue 163`_.  **NOTE**: it is possible
>  that your configurations may now be incorrect.  If you use ``include`` or
>  ``omit`` during reporting, whether on the command line, through the API, or
>  in a configuration file, please check carefully that you were not relying on
>  the old broken behavior.

>- The **report**, **html**, and **xml** commands now accept a ``--fail-under``
>  switch that indicates in the exit status whether the coverage percentage was
>  less than a particular value.  Closes `issue 139`_.

>- The reporting functions coverage.report(), coverage.html_report(), and
>  coverage.xml_report() now all return a float, the total percentage covered
>  measurement.

>- The HTML report&#39;s title can now be set in the configuration file, with the
>  ``--title`` switch on the command line, or via the API.

>- Configuration files now support substitution of environment variables, using
>  syntax like ``${WORD}``.  Closes `issue 97`_.

>- Embarrassingly, the ``[xml] output=`` setting in the .coveragerc file simply
>  didn&#39;t work.  Now it does.

>- The XML report now consistently uses file names for the file name attribute,
>  rather than sometimes using module names.  Fixes `issue 67`_.
>  Thanks, Marcus Cobden.

>- Coverage percentage metrics are now computed slightly differently under
>  branch coverage.  This means that completely unexecuted files will now
>  correctly have 0% coverage, fixing `issue 156`_.  This also means that your
>  total coverage numbers will generally now be lower if you are measuring
>  branch coverage.

>- When installing, now in addition to creating a &quot;coverage&quot; command, two new
>  aliases are also installed.  A &quot;coverage2&quot; or &quot;coverage3&quot; command will be
>  created, depending on whether you are installing in Python 2.x or 3.x.
>  A &quot;coverage-X.Y&quot; command will also be created corresponding to your specific
>  version of Python.  Closes `issue 111`_.

>- The coverage.py installer no longer tries to bootstrap setuptools or
>  Distribute.  You must have one of them installed first, as `issue 202`_
>  recommended.

>- The coverage.py kit now includes docs (closing `issue 137`_) and tests.

>- On Windows, files are now reported in their correct case, fixing `issue 89`_
>  and `issue 203`_.

>- If a file is missing during reporting, the path shown in the error message
>  is now correct, rather than an incorrect path in the current directory.
>  Fixes `issue 60`_.

>- Running an HTML report in Python 3 in the same directory as an old Python 2
>  HTML report would fail with a UnicodeDecodeError. This issue (`issue 193`_)
>  is now fixed.

>- Fixed yet another error trying to parse non-Python files as Python, this
>  time an IndentationError, closing `issue 82`_ for the fourth time...

>- If `coverage xml` fails because there is no data to report, it used to
>  create a zero-length XML file.  Now it doesn&#39;t, fixing `issue 210`_.

>- Jython files now work with the ``--source`` option, fixing `issue 100`_.

>- Running coverage.py under a debugger is unlikely to work, but it shouldn&#39;t
>  fail with &quot;TypeError: &#39;NoneType&#39; object is not iterable&quot;.  Fixes `issue
>  201`_.

>- On some Linux distributions, when installed with the OS package manager,
>  coverage.py would report its own code as part of the results.  Now it won&#39;t,
>  fixing `issue 214`_, though this will take some time to be repackaged by the
>  operating systems.

>- Docstrings for the legacy singleton methods are more helpful.  Thanks Marius
>  Gedminas.  Closes `issue 205`_.

>- The pydoc tool can now show documentation for the class `coverage.coverage`.
>  Closes `issue 206`_.

>- Added a page to the docs about contributing to coverage.py, closing
>  `issue 171`_.

>- When coverage.py ended unsuccessfully, it may have reported odd errors like
>  ``&#39;NoneType&#39; object has no attribute &#39;isabs&#39;``.  It no longer does,
>  so kiss `issue 153`_ goodbye.

>.. _issue 60: https://bitbucket.org/ned/coveragepy/issues/60/incorrect-path-to-orphaned-pyc-files
>.. _issue 67: https://bitbucket.org/ned/coveragepy/issues/67/xml-report-filenames-may-be-generated
>.. _issue 89: https://bitbucket.org/ned/coveragepy/issues/89/on-windows-all-packages-are-reported-in
>.. _issue 97: https://bitbucket.org/ned/coveragepy/issues/97/allow-environment-variables-to-be
>.. _issue 100: https://bitbucket.org/ned/coveragepy/issues/100/source-directive-doesnt-work-for-packages
>.. _issue 111: https://bitbucket.org/ned/coveragepy/issues/111/when-installing-coverage-with-pip-not
>.. _issue 137: https://bitbucket.org/ned/coveragepy/issues/137/provide-docs-with-source-distribution
>.. _issue 139: https://bitbucket.org/ned/coveragepy/issues/139/easy-check-for-a-certain-coverage-in-tests
>.. _issue 143: https://bitbucket.org/ned/coveragepy/issues/143/omit-doesnt-seem-to-work-in-coverage
>.. _issue 153: https://bitbucket.org/ned/coveragepy/issues/153/non-existent-filename-triggers
>.. _issue 156: https://bitbucket.org/ned/coveragepy/issues/156/a-completely-unexecuted-file-shows-14
>.. _issue 163: https://bitbucket.org/ned/coveragepy/issues/163/problem-with-include-and-omit-filename
>.. _issue 171: https://bitbucket.org/ned/coveragepy/issues/171/how-to-contribute-and-run-tests
>.. _issue 193: https://bitbucket.org/ned/coveragepy/issues/193/unicodedecodeerror-on-htmlpy
>.. _issue 201: https://bitbucket.org/ned/coveragepy/issues/201/coverage-using-django-14-with-pydb-on
>.. _issue 202: https://bitbucket.org/ned/coveragepy/issues/202/get-rid-of-ez_setuppy-and
>.. _issue 203: https://bitbucket.org/ned/coveragepy/issues/203/duplicate-filenames-reported-when-filename
>.. _issue 205: https://bitbucket.org/ned/coveragepy/issues/205/make-pydoc-coverage-more-friendly
>.. _issue 206: https://bitbucket.org/ned/coveragepy/issues/206/pydoc-coveragecoverage-fails-with-an-error
>.. _issue 210: https://bitbucket.org/ned/coveragepy/issues/210/if-theres-no-coverage-data-coverage-xml
>.. _issue 214: https://bitbucket.org/ned/coveragepy/issues/214/coveragepy-measures-itself-on-precise


>.. _changes_353:



>### 3.5.3

>----------------------------

>- Line numbers in the HTML report line up better with the source lines, fixing
>  `issue 197`_, thanks Marius Gedminas.

>- When specifying a directory as the source= option, the directory itself no
>  longer needs to have a ``__init__.py`` file, though its sub-directories do,
>  to be considered as source files.

>- Files encoded as UTF-8 with a BOM are now properly handled, fixing
>  `issue 179`_.  Thanks, Pablo Carballo.

>- Fixed more cases of non-Python files being reported as Python source, and
>  then not being able to parse them as Python.  Closes `issue 82`_ (again).
>  Thanks, Julian Berman.

>- Fixed memory leaks under Python 3, thanks, Brett Cannon. Closes `issue 147`_.

>- Optimized .pyo files may not have been handled correctly, `issue 195`_.
>  Thanks, Marius Gedminas.

>- Certain unusually named file paths could have been mangled during reporting,
>  `issue 194`_.  Thanks, Marius Gedminas.

>- Try to do a better job of the impossible task of detecting when we can&#39;t
>  build the C extension, fixing `issue 183`_.

>- Testing is now done with `tox`_, thanks, Marc Abramowitz.

>.. _issue 147: https://bitbucket.org/ned/coveragepy/issues/147/massive-memory-usage-by-ctracer
>.. _issue 179: https://bitbucket.org/ned/coveragepy/issues/179/htmlreporter-fails-when-source-file-is
>.. _issue 183: https://bitbucket.org/ned/coveragepy/issues/183/install-fails-for-python-23
>.. _issue 194: https://bitbucket.org/ned/coveragepy/issues/194/filelocatorrelative_filename-could-mangle
>.. _issue 195: https://bitbucket.org/ned/coveragepy/issues/195/pyo-file-handling-in-codeunit
>.. _issue 197: https://bitbucket.org/ned/coveragepy/issues/197/line-numbers-in-html-report-do-not-align
>.. _tox: http://tox.readthedocs.org/


>.. _changes_352:



>### 3.5.2

>----------------------------



>### 3.5.2b1

>------------------------------

>- The HTML report has slightly tweaked controls: the buttons at the top of
>  the page are color-coded to the source lines they affect.

>- Custom CSS can be applied to the HTML report by specifying a CSS file as
>  the ``extra_css`` configuration value in the ``[html]`` section.

>- Source files with custom encodings declared in a comment at the top are now
>  properly handled during reporting on Python 2.  Python 3 always handled them
>  properly.  This fixes `issue 157`_.

>- Backup files left behind by editors are no longer collected by the source=
>  option, fixing `issue 168`_.

>- If a file doesn&#39;t parse properly as Python, we don&#39;t report it as an error
>  if the file name seems like maybe it wasn&#39;t meant to be Python.  This is a
>  pragmatic fix for `issue 82`_.

>- The ``-m`` switch on ``coverage report``, which includes missing line numbers
>  in the summary report, can now be specified as ``show_missing`` in the
>  config file.  Closes `issue 173`_.

>- When running a module with ``coverage run -m &lt;modulename&gt;``, certain details
>  of the execution environment weren&#39;t the same as for
>  ``python -m &lt;modulename&gt;``.  This had the unfortunate side-effect of making
>  ``coverage run -m unittest discover`` not work if you had tests in a
>  directory named &quot;test&quot;.  This fixes `issue 155`_ and `issue 142`_.

>- Now the exit status of your product code is properly used as the process
>  status when running ``python -m coverage run ...``.  Thanks, JT Olds.

>- When installing into pypy, we no longer attempt (and fail) to compile
>  the C tracer function, closing `issue 166`_.

>.. _issue 142: https://bitbucket.org/ned/coveragepy/issues/142/executing-python-file-syspath-is-replaced
>.. _issue 155: https://bitbucket.org/ned/coveragepy/issues/155/cant-use-coverage-run-m-unittest-discover
>.. _issue 157: https://bitbucket.org/ned/coveragepy/issues/157/chokes-on-source-files-with-non-utf-8
>.. _issue 166: https://bitbucket.org/ned/coveragepy/issues/166/dont-try-to-compile-c-extension-on-pypy
>.. _issue 168: https://bitbucket.org/ned/coveragepy/issues/168/dont-be-alarmed-by-emacs-droppings
>.. _issue 173: https://bitbucket.org/ned/coveragepy/issues/173/theres-no-way-to-specify-show-missing-in


>.. _changes_351:



>### 3.5.2.b1





>### 3.5.1

>----------------------------

>- The




-------------------------------------------------------------------------------

# [\#3 PR](https://github.com/mattduck/gh2md/pull/3) `closed`: Config file for pyup.io

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 12:59](https://github.com/mattduck/gh2md/pull/3):

Hi there and thanks for using pyup.io!

Since you are using a non-default config I've created one for you.

There are a lot of things you can configure on top of that, so make sure to check out the [docs](https://pyup.io/docs/configuration/) to see what I can do for you.




-------------------------------------------------------------------------------

# [\#2 Issue](https://github.com/mattduck/gh2md/issues/2) `closed`: Initial Update

#### <img src="https://avatars.githubusercontent.com/u/16239342?u=8454ae029661131445080f023e1efccc29166485&v=4" width="50">[pyup-bot](https://github.com/pyup-bot) opened issue at [2017-05-21 12:59](https://github.com/mattduck/gh2md/issues/2):

Hi 👊

This is my first visit to this fine repo, but it seems you have been working hard to keep all dependencies updated so far.

Once you have closed this issue, I'll create separate pull requests for every update as soon as I find one.

That's it for now!

Happy merging! 🤖





-------------------------------------------------------------------------------

# [\#1 Issue](https://github.com/mattduck/gh2md/issues/1) `closed`: Example issue
**Labels**: `enhancement`


#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) opened issue at [2017-05-20 18:11](https://github.com/mattduck/gh2md/issues/1):

I'm making an issue just so I can run this tool against its own repository.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2017-05-20 18:11](https://github.com/mattduck/gh2md/issues/1#issuecomment-302889476):

This is a comment.

#### <img src="https://avatars.githubusercontent.com/u/1607892?u=196bf09c14472eee8dccaaecbef3c16974c8e69f&v=4" width="50">[mattduck](https://github.com/mattduck) commented at [2017-05-20 18:11](https://github.com/mattduck/gh2md/issues/1#issuecomment-302889489):

Closing, as the example data now exists.


-------------------------------------------------------------------------------

