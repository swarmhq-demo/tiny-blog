# tiny-blog

A tiny blog demo repo intended for issue/feature tracking and agent evaluation.

## Structure

- `web/`: static pages + simple JS
- `api/`: a tiny FastAPI API (in-memory storage)

## Run locally (optional)

```bash
uv sync
uv run uvicorn api.server:app --reload --port 8081
```

Then open:

- `http://localhost:8081/healthz`
- `http://localhost:8081/posts`
- `http://localhost:8081/rss`

