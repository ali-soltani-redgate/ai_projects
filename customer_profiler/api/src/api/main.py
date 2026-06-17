from datetime import datetime, timezone
from enum import Enum

from fastapi import FastAPI

app = FastAPI(title="Customer Profiler API")

@app.get("/api/v1/health")
async def health_check():
    return HealthResponse(
        status=HealthStatus.healthy,
        version="0.1.0",
        timestamp=datetime.now(timezone.utc),
    )
    
class HealthStatus(str, Enum):
    healthy = "healthy"
    degraded = "degraded"
    unhealthy = "unhealthy"