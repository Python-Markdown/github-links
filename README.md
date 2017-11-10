# Python-Markdown Github-Links Extension

An extension to Python-Markdown which adds support for shorthand links to GitHub
users, repositories, issues and commits.

## Installation

To install the extension run the following command:

```sh
pip install mdx-gh-links
```

## Usage

To use the extension simply include its name in the list of extensions passed to
Python-Markdown.

```python
import markdown
markdown.markdown(src, extensions=['mdx_gh_links'])
```

### Configuration Options

To set configuration options, you may pass them to Markdown's `exension_configs`
keyword...

```python
markdown.markdown(
    src,
    extensions=['mdx_gh_links'],
    extension_configs={
        'mdx_gh_links': {'user': 'foo', 'repo': 'bar'}
    }
)
```

... or you may import and pass the configs directly to an instance of the
`mdx_gh_links.GithubLinks` class...

```python
from mdx_gh_links import GithubLinks
markdown.markdown(src, extensions=[GithubLinks(user='foo', repo='bar')])
```

The following configuration options are available:

#### user

A GitHub user name or organization. If no user or organization is specified in
a GitHub link, then the value of this option will be used.

#### repo

A GitHub repository. If no repository is specified in a GitHub link, then the
value of this option will be used.

## Syntax

This extension implements shorthand to specify links to GitHub in various ways.

All links in the generated HTML are assigned a `gh-link` class as well as a class
unique to that type of link. See each type for the specific class assigned.

### Mentions

Link directly to a GitHub user, organization or repository. Note that no
verification is made that an actual user, organization or repository exists. As
the syntax does not differentiate between users and organizations, all
organizations are assumed to be users. However, this assumption is only
reflected in the title of a link.

Mentions use the format `@{user}` to link to a user or organization and
`@{user}/{repo}` to link to a repository. The defaults defined in the
configuration options are ignored by mentions. A mention may be escaped by
adding a backslash immediately before the at sign (`@`).

All mentions are assigned the `gh-mention` class.

The following table provides some examples:

| shorthand   | href                         | rendered result                                                                     |
| ----------- | ---------------------------- | -------------------------------------------------------------------- |
| `@foo`      | `https://github.com/foo`     | [@foo](https://github.com/foo "GitHub User: @foo")                   |
| `@foo/bar`  | `https://github.com/foo/bar` | [@foo/bar](https://github.com/foo/bar "GitHub Repository: @foo/bar") |
| `\@123`     |                              | @foo                                                                 |
| `\@foo/bar` |                              | @foo/bar                                                             |

### Issues

Link directly to a GitHub issue or pull request (PR). Note that no verification
is made that an actual issue or PR exists. As the syntax does not differentiate
between Issues and PRs, all URLs point to "issues". Fortunately, GitHub will
properly redirect an issue URL to a PR URL if appropriate.

Issue links use the format `#{num}` or `{user}/{repo}#{num}`. `{num}` is the
number assigned to the issue or PR. `{user}` and `{repo}` will use the
defaults defined in the configuration options if not provided. An issue link may
be escaped by adding a backslash immediately before the hash mark (`#`).

All issue links are assigned the `gh-issue` class.

The following table provides various examples (with the defaults set as
`user='user', repo='repo'`):

| shorthand      | href                                         | rendered result                                                                     |
| -------------- | -------------------------------------------- | ----------------------------------------------------------------------------------- |
| `#123`         | `https://github.com/user/repo/issues/123`    | [#123](https://github.com/user/repo/issues/123 "GitHub Issue user/repo #123")       |
| `foo/bar#123`  | `https://github.com/foo/bar/issues/123`      | [foo/bar#123](https://github.com/foo/bar/issues/123 "GitHub Issue foo/bar #123")    |
| `\#123`        |                                              | #123                                                                                |
| `foo/bar\#123` |                                              | foo/bar#123                                                                         |

### Commits

Link directly to a GitHub Commit. Note that no verification is made that an
actual commit exists.

Commit links consist of a complete 40 character SHA hash and may optionally be
prefaced by `{user}@` or `{user/repo}@`. `{user}` and `{repo}` will use the
defaults defined in the configuration options if not provided. To avoid a 40
character hash from being linked, wrap it in a code span.

All commit links are assigned the `gh-commit` class.

The following table provides various examples (with the defaults set as
`user='user', repo='repo'`):

| shorthand                                          | href                                                                              | rendered result                                                                                                                                                 |
| -------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `72df691791fb36f00cf5363fefe757c8d3042656`         | `https://github.com/user/repo/commit/72df691791fb36f00cf5363fefe757c8d3042656`    | [72df691](https://github.com/user/repo/commit/72df691791fb36f00cf5363fefe757c8d3042656 "GitHub Commit: user/repo@72df691791fb36f00cf5363fefe757c8d3042656")     |
| `foo@72df691791fb36f00cf5363fefe757c8d3042656`     | `https://github.com/foo/repo/commit/72df691791fb36f00cf5363fefe757c8d3042656`     | [foo@72df691](https://github.com/foo/repo/commit/72df691791fb36f00cf5363fefe757c8d3042656 "GitHub Commit: foo/repo@72df691791fb36f00cf5363fefe757c8d3042656")   |
| `foo/bar@72df691791fb36f00cf5363fefe757c8d3042656` | `https://github.com/foo/bar/commit/72df691791fb36f00cf5363fefe757c8d3042656`      | [foo/bar@72df691](https://github.com/foo/bar/commit/72df691791fb36f00cf5363fefe757c8d3042656 "GitHub Commit: foo/bar@72df691791fb36f00cf5363fefe757c8d3042656") |
| `` `72df691791fb36f00cf5363fefe757c8d3042656` ``   |                                                                                   | `72df691791fb36f00cf5363fefe757c8d3042656`                                                                                                                      |

## License

The Python-Markdown Github-Links Extension is licensed under the [BSD License] as
defined in `LICENSE`.

[BSD License]: http://opensource.org/licenses/BSD-3-Clause

## Change Log

### Version 0.0.1 (2017/11/10)

The initial release.
