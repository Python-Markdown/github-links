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
