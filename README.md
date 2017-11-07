# Python-Markdown Github-Links Extension

An extension to Python-Markdown which adds support for a shorthand for GitHub
specific links.

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
        'mdx_gh_links': {'user': 'foo', 'project': 'bar'}
    }
)
```

... or you may import and pass the configs directly to an instance of the
`mdx_gh_links.GithubLinks` class...

```python
from mdx_gh_links import GithubLinks
markdown.markdown(src, extensions=[GithubLinks(user='foo', project='bar')])
```

The following configuration options are available:

#### user

A GitHub user name or organization. If no user or organization is specified in
a GitHub link, then the value of this option will be used.

#### project

A GitHub project. If no project is specified in a GitHub link, then the value
of this option will be used.

## Syntax

This extension implements shorthand to specify links to GitHub in various ways.

All links in the generated HTML are assigned a `gh-link` class as well as a class
unique to that type of link. See each type for the specific class assigned. 

### Users

*Not yet implemented*

### Projects

*Not yet implemented*

### Issues

Link directly to a GitHub issue or pull request (PR). Note that no verification
is made that an actual issue or PR exists. As the syntax does not differentiate
between Issues and PRs, all URLs point to "issues". Fortunately, GitHub will
properly redirect an issue URL to a PR URL if appropriate.

Issue links use the format `#{num}` or `{user}/{project}#{num}`. `{num}` is the
number assigned to the issue or PR. `{user}` and `{project}` will use the
defaults defined in the configuration options if not provided. An issue link may
be escaped by adding a backslash immediately before the hash mark.

All issue links are assigned the `gh-issue` class.

The following table provides various examples (with the defaults set as
`user='user', project='project'`):

| shorthand         | href                                         | rendered result                                                                     |
| ----------------- | -------------------------------------------- | ----------------------------------------------------------------------------------- |
| `#123`            | `https://github.com/user/project/issues/123` | [#123](https://github.com/user/project/issues/123 "GitHub Issue user/project #123") |
| `foo/bar#123`     | `https://github.com/foo/bar/issues/123`      | [foo/bar#123](https://github.com/foo/bar/issues/123 "GitHub Issue foo/bar #123")    |
| `\#123` (escaped) |                                              | #123                                                                                |
| `foo/bar\#123`    |                                              | foo/bar#123                                                                         |

### Commits

*Not yet implemented*
