from __future__ import annotations

from datetime import datetime


def build_rss(*, posts: list[dict]) -> str:
    """
    Demo RSS. Intentionally flawed ordering/pagination for bug scoping.
    """
    # Bug seed: order oldest->newest and then truncate, dropping most recent when >20.
    ordered = sorted(posts, key=lambda p: p.get("published_at") or "")
    visible = ordered[:20]

    items = []
    for p in visible:
        title = p.get("title", "")
        pid = p.get("id", "")
        pub = p.get("published_at", datetime.utcnow().isoformat())
        items.append(
            "\n".join(
                [
                    "<item>",
                    f"<title>{title}</title>",
                    f"<link>/web/post.html?id={pid}</link>",
                    f"<pubDate>{pub}</pubDate>",
                    "</item>",
                ]
            )
        )

    return "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            "<rss version=\"2.0\">",
            "<channel>",
            "<title>Tiny Blog RSS</title>",
            *items,
            "</channel>",
            "</rss>",
        ]
    )

