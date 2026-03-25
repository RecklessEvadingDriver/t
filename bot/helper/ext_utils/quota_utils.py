"""
User Tier & Daily Quota System

Tiers: free, premium, vip
Each tier can have a daily bandwidth quota (bytes). 0 = unlimited.

Usage is tracked per-user per-calendar-day (UTC). When a user completes
a task, the bytes transferred are recorded. Subsequent tasks check against
the limit before starting.
"""

from datetime import datetime, timezone
from time import time

from ... import user_data, LOGGER
from ...core.config_manager import Config
from ..ext_utils.bot_utils import update_user_ldata

TIER_ORDER = {"free": 0, "premium": 1, "vip": 2}

TIER_DISPLAY = {
    "free": "🆓 Free",
    "premium": "⭐ Premium",
    "vip": "💎 VIP",
}


def _today_utc() -> str:
    """Return today's date string in UTC (YYYY-MM-DD)."""
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def get_user_tier(user_id: int) -> str:
    """Return the tier for *user_id* (default: Config.USER_DEFAULT_TIER)."""
    ud = user_data.get(user_id, {})
    return ud.get("USER_TIER", Config.USER_DEFAULT_TIER or "free").lower()


def get_tier_quota(tier: str) -> int:
    """
    Return the daily quota in bytes for *tier*.
    0 means unlimited.
    """
    tier = tier.lower()
    mapping = {
        "free": int(Config.FREE_DAILY_QUOTA or 0),
        "premium": int(Config.PREMIUM_DAILY_QUOTA or 0),
        "vip": int(Config.VIP_DAILY_QUOTA or 0),
    }
    return mapping.get(tier, 0)


def get_used_today(user_id: int) -> int:
    """Return bytes already used by *user_id* today (UTC)."""
    ud = user_data.get(user_id, {})
    today = _today_utc()
    quota_info = ud.get("QUOTA_USAGE", {})
    if quota_info.get("date") != today:
        return 0
    return int(quota_info.get("bytes", 0))


def record_usage(user_id: int, size_bytes: int) -> None:
    """Add *size_bytes* to today's usage for *user_id*."""
    if size_bytes <= 0:
        return
    today = _today_utc()
    ud = user_data.setdefault(user_id, {})
    quota_info = ud.get("QUOTA_USAGE", {})
    if quota_info.get("date") != today:
        quota_info = {"date": today, "bytes": 0}
    quota_info["bytes"] = int(quota_info["bytes"]) + size_bytes
    update_user_ldata(user_id, "QUOTA_USAGE", quota_info)


def check_quota(user_id: int, required_bytes: int = 0) -> tuple[bool, str]:
    """
    Check whether *user_id* is within their daily quota.

    Returns:
        (allowed: bool, reason: str)
        reason is empty when allowed is True.
    """
    tier = get_user_tier(user_id)
    limit = get_tier_quota(tier)
    if limit <= 0:
        return True, ""

    used = get_used_today(user_id)
    remaining = limit - used

    if required_bytes > 0 and required_bytes > remaining:
        from .status_utils import get_readable_file_size
        return (
            False,
            (
                f"❌ <b>Daily Quota Exceeded</b>\n"
                f"┟ <b>Tier</b> → {TIER_DISPLAY.get(tier, tier)}\n"
                f"┠ <b>Daily Limit</b> → {get_readable_file_size(limit)}\n"
                f"┠ <b>Used Today</b> → {get_readable_file_size(used)}\n"
                f"┖ <b>Remaining</b> → {get_readable_file_size(remaining)}\n\n"
                "<i>Your quota resets at midnight UTC.</i>"
            ),
        )

    if used >= limit:
        from .status_utils import get_readable_file_size
        return (
            False,
            (
                f"❌ <b>Daily Quota Exhausted</b>\n"
                f"┟ <b>Tier</b> → {TIER_DISPLAY.get(tier, tier)}\n"
                f"┠ <b>Daily Limit</b> → {get_readable_file_size(limit)}\n"
                f"┖ <b>Used Today</b> → {get_readable_file_size(used)}\n\n"
                "<i>Your quota resets at midnight UTC.</i>"
            ),
        )

    return True, ""


def set_user_tier(user_id: int, tier: str) -> bool:
    """
    Set the tier for *user_id*.  Returns True on success.
    """
    tier = tier.lower()
    if tier not in TIER_ORDER:
        return False
    update_user_ldata(user_id, "USER_TIER", tier)
    LOGGER.info(f"Set tier for user {user_id} to {tier}")
    return True


def get_quota_summary(user_id: int) -> str:
    """Return a human-readable quota summary for *user_id*."""
    from .status_utils import get_readable_file_size

    tier = get_user_tier(user_id)
    limit = get_tier_quota(tier)
    used = get_used_today(user_id)
    tier_label = TIER_DISPLAY.get(tier, tier)

    if limit <= 0:
        return (
            f"┟ <b>Tier</b> → {tier_label}\n"
            f"┖ <b>Daily Quota</b> → Unlimited"
        )

    remaining = max(0, limit - used)
    pct = min(100, int(used * 100 / limit)) if limit else 0
    return (
        f"┟ <b>Tier</b> → {tier_label}\n"
        f"┠ <b>Daily Limit</b> → {get_readable_file_size(limit)}\n"
        f"┠ <b>Used Today</b> → {get_readable_file_size(used)} ({pct}%)\n"
        f"┖ <b>Remaining</b> → {get_readable_file_size(remaining)}"
    )
