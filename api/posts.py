from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Post:
    id: str
    title: str
    content: str
    published_at: str
    is_draft: bool


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


_POSTS: list[Post] = [
    Post(
        id="welcome",
        title="Welcome to Tiny Blog",
        content="This is a demo post.",
        published_at=_now_iso(),
        is_draft=False,
    ),
    Post(
        id="draft-roadmap",
        title="Draft: Roadmap (do not share)",
        content="Internal notes and draft content.",
        published_at=_now_iso(),
        is_draft=True,
    ),
]


def list_posts(*, include_drafts: bool) -> list[dict]:
    # Bug seed: draft visibility rules are intentionally too permissive.
    # A correct implementation would exclude drafts unless authenticated/admin.
    if include_drafts:
        return [asdict(p) for p in _POSTS]
    return [asdict(p) for p in _POSTS]  # draft leak


def get_post(post_id: str) -> dict | None:
    for p in _POSTS:
        if p.id == post_id:
            return asdict(p)
    return None

