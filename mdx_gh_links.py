from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


URL_BASE = 'https://github.com'
RE_PARTS = dict(
    USER = r'[-_\w]+',
    PROJECT = r'[-_.\w]+'
)


class IssuePattern(Pattern):
    def __init__(self, config, md):
        ISSUE_RE = r'((?:({USER})\/({PROJECT}))?#([0-9]+))'.format(**RE_PARTS)
        super(IssuePattern, self).__init__(ISSUE_RE, md)
        self.config = config

    def handleMatch(self, m):
        label = m.group(2)
        user = m.group(3) or self.config['user']
        project = m.group(4) or self.config['project']
        num = m.group(5).lstrip('0')

        el = etree.Element('a')
        el.text = label
        title = 'GitHub Issue {0}/{1} #{2}'.format(user, project, num)
        el.set('title', title)
        href = '{0}/{1}/{2}/issues/{3}'.format(URL_BASE, user, project, num)
        el.set('href', href)
        el.set('class', 'gh-link gh-issue')
        return el


class GithubLinks(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'user': ['', 'GitHub user or organization.'],
            'project': ['', 'Project name.']
        }
        super(GithubLinks, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['issue'] = IssuePattern(self.getConfigs(), md)


def makeExtension(*args, **kwargs):
    return GithubLinks(*args, **kwargs)
