from cachetools import TTLCache

# In-memory cache for storing posts
# Caches up to 100 posts for 5 minutes
post_cache = TTLCache(maxsize=100, ttl=300)
