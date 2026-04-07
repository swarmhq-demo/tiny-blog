from __future__ import annotations


_BANNED_SUBSTRINGS = ["http://", "https://", "buy now", "free money"]


def moderate_comment(body: str) -> dict:
    """
    Demo moderation. Intentionally weak for bug scoping.
    """
    text = (body or "").strip()
    if not text:
        return {"ok": False, "reason": "empty"}

    lowered = text.lower()

    # Bug seed: this misses obvious variants and doesn't normalize whitespace.
    for s in _BANNED_SUBSTRINGS:
        if s in lowered:
            return {"ok": False, "reason": "spam_detected"}

    return {"ok": True}


def create_comment(*, post_id: str, body: str) -> dict:
    verdict = moderate_comment(body)
    if not verdict["ok"]:
        return {"status": "rejected", "post_id": post_id, "reason": verdict["reason"]}
    return {"status": "accepted", "post_id": post_id}

