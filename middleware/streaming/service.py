import asyncio
from fastapi import Request
from sse_starlette.sse import EventSourceResponse
from caching.service import cache

async def security_event_generator(request: Request):
    while True:
        if await request.is_disconnected():
            break
        
        # Check cache for new events
        event_data = cache.get("latest_security_event")
        if event_data:
            yield {
                "event": "security_update",
                "id": "message_id",
                "retry": 15000,
                "data": event_data
            }
        
        await asyncio.sleep(5)
