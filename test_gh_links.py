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

import unittest
from markdown import markdown
from mdx_gh_links import GithubLinks


class TestGithubLinks(unittest.TestCase):
    maxDiff = None

    def assertMarkdownRenders(self, source, expected, **kwargs):
        'Test that source Markdown text renders to expected output.'
        configs = {'user': 'Python-Markdown', 'project': 'github-links'}
        configs.update(kwargs)
        output = markdown(source, extensions=[GithubLinks(**configs)])
        self.assertMultiLineEqual(output, expected)

    def test_issue(self):
        self.assertMarkdownRenders(
            'Issue #123.',
            '<p>Issue <a class="gh-link gh-issue" '
            'href="https://github.com/Python-Markdown/github-links/issues/123" '
            'title="GitHub Issue Python-Markdown/github-links #123">#123</a>.</p>',
        )

    def test_issue_leading_zero(self):
        self.assertMarkdownRenders(
            'Issue #012.',
            '<p>Issue <a class="gh-link gh-issue" '
            'href="https://github.com/Python-Markdown/github-links/issues/12" '
            'title="GitHub Issue Python-Markdown/github-links #12">#012</a>.</p>',
        )

    def test_non_issue(self):
        self.assertMarkdownRenders(
            'Issue #notanissue.',
            '<p>Issue #notanissue.</p>',
        )

    def test_issue_with_project(self):
        self.assertMarkdownRenders(
            'Issue Organization/Project#123.',
            '<p>Issue <a class="gh-link gh-issue" '
            'href="https://github.com/Organization/Project/issues/123" '
            'title="GitHub Issue Organization/Project #123">Organization/Project#123</a>.</p>',
        )

    def test_issue_leading_zero_with_project(self):
        self.assertMarkdownRenders(
            'Issue Organization/Project#012.',
            '<p>Issue <a class="gh-link gh-issue" '
            'href="https://github.com/Organization/Project/issues/12" '
            'title="GitHub Issue Organization/Project #12">Organization/Project#012</a>.</p>',
        )

    def test_non_issue_with_project(self):
        self.assertMarkdownRenders(
            'Issue Organization/Project#notanissue.',
            '<p>Issue Organization/Project#notanissue.</p>',
        )

    def test_escaped_issue(self):
        self.assertMarkdownRenders(
            'Issue \#123.',
            '<p>Issue #123.</p>',
        )

    def test_escaped_issue_with_project(self):
        self.assertMarkdownRenders(
            'Issue Organization/Project\#123.',
            '<p>Issue Organization/Project#123.</p>',
        )


if __name__ == '__main__':
    unittest.main()
