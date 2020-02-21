import asyncio
import os
from constants import *

from aiohttp.client import ClientSession
from octomachinery.github.api.tokens import GitHubOAuthToken
from octomachinery.github.api.raw_client import RawGitHubAPI


async def main():
    access_token = GitHubOAuthToken(GITHUB_TOKEN)
    async with ClientSession() as http_session:
        gh = RawGitHubAPI(
            access_token,
            session=http_session,
            user_agent='gloriasky',
        )
        await gh.post(
            '/repos/mariatta/strange-relationship/issues',
            data={
                'title': 'We got a problem',
                'body': 'Use more emoji!',
            },
        )
        await gh.patch(
            '/repos/mariatta/strange-relationship/issues{/number}',
            data={'state': 'closed'},
            url_vars={'number': '242'},
        )


asyncio.run(main())