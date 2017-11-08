"""
Github Links - A Python-Markdown Extension.

BSD License

Copyright (c) 2017 by Waylan Limberg. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

*   Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
*   Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
*   Neither the name of HTMLTree nor the names of its contributors may be
    used to endorse or promote products derived from this software without
    specific prior written permission.

THIS SOFTWARE IS PROVIDED BY WAYLAN LIMBERG ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL ANY CONTRIBUTORS TO Github-Links Extension
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


URL_BASE = 'https://github.com'
RE_PARTS = dict(
    USER=r'[-_\w]+',
    PROJECT=r'[-_.\w]+'
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
