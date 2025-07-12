from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging


def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # 1 hour
    return properties

def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses

    hit_ratio = hits / total if total > 0 else 0.0

    # Log the metrics
    logging.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio:.2f}")

    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2)
    }
