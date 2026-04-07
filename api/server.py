from __future__ import annotations

from fastapi import FastAPI, HTTPException, Request, Response

from .comments import create_comment
from .posts import get_post, list_posts
from .rss import build_rss

app = FastAPI(title="tiny-blog api (demo)")


@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}


@app.get("/posts")
def posts(request: Request) -> dict:
    # Demo auth: treat X-Admin as an admin flag.
    include_drafts = request.headers.get("X-Admin") == "1"
    return {"posts": list_posts(include_drafts=include_drafts)}


@app.get("/posts/{post_id}")
def post(post_id: str) -> dict:
    p = get_post(post_id)
    if not p:
        raise HTTPException(status_code=404, detail="not_found")
    return p


@app.post("/posts/{post_id}/comments")
async def comment(post_id: str, request: Request) -> dict:
    body = await request.json()
    return create_comment(post_id=post_id, body=body.get("body", ""))


@app.get("/rss")
def rss(request: Request) -> Response:
    include_drafts = request.headers.get("X-Admin") == "1"
    xml = build_rss(posts=list_posts(include_drafts=include_drafts))
    return Response(content=xml, media_type="application/rss+xml")
