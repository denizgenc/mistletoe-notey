"""
GitHub Wiki support for mistletoe_notey.
"""

import re
from mistletoe_notey.span_token import SpanToken
from mistletoe_notey.html_renderer import HTMLRenderer


__all__ = ['GithubWiki', 'GithubWikiRenderer']


class GithubWiki(SpanToken):
    pattern = re.compile(r"\[\[ *(.+?) *\| *(.+?) *\]\]")

    def __init__(self, match):
        self.target = match.group(2)


class GithubWikiRenderer(HTMLRenderer):
    def __init__(self):
        super().__init__(GithubWiki)

    def render_github_wiki(self, token):
        template = '<a href="{target}">{inner}</a>'
        target = self.escape_url(token.target)
        inner = self.render_inner(token)
        return template.format(target=target, inner=inner)
