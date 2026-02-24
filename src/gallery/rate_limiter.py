"""
Rate limiter for pre.SENT.

Prevents runaway API costs by limiting generation frequency
per visitor and globally. Uses in-memory tracking (no database).
"""

import time
import threading
from collections import defaultdict

class RateLimiter:
    """Simple in-memory rate limiter."""

    def __init__(self, min_interval=15, max_per_hour=30, global_max_per_hour=200):
        """
        Args:
            min_interval: Minimum seconds between generations per client
            max_per_hour: Maximum generations per client per hour
            global_max_per_hour: Maximum total generations per hour
        """
        self.min_interval = min_interval
        self.max_per_hour = max_per_hour
        self.global_max_per_hour = global_max_per_hour

        self.last_generation = defaultdict(float)
        self.hourly_counts = defaultdict(list)
        self.global_counts = []
        self.lock = threading.Lock()

    def check(self, client_id):
        """
        Check if a generation is allowed.

        Args:
            client_id: IP address or session identifier

        Returns:
            Tuple of (allowed: bool, wait_seconds: float, reason: str)
        """
        now = time.time()
        hour_ago = now - 3600

        with self.lock:
            # Clean old entries
            self.hourly_counts[client_id] = [
                t for t in self.hourly_counts[client_id] if t > hour_ago
            ]
            self.global_counts = [
                t for t in self.global_counts if t > hour_ago
            ]

            # Check minimum interval
            elapsed = now - self.last_generation[client_id]
            if elapsed < self.min_interval:
                wait = self.min_interval - elapsed
                return False, wait, f"Please wait {wait:.0f} seconds"

            # Check hourly client limit
            if len(self.hourly_counts[client_id]) >= self.max_per_hour:
                return False, 0, "Hourly limit reached. Come back soon."

            # Check global hourly limit
            if len(self.global_counts) >= self.global_max_per_hour:
                return False, 0, "Gallery is busy. Try again in a moment."

            return True, 0, ""

    def record(self, client_id):
        """Record a successful generation."""
        now = time.time()
        with self.lock:
            self.last_generation[client_id] = now
            self.hourly_counts[client_id].append(now)
            self.global_counts.append(now)
