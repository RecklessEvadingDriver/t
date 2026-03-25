"""Tier & Quota management commands.

/settier <user_id> <tier>  – (sudo) assign a tier to a user
/myquota                   – show the calling user's tier and quota info
"""

from ..helper.ext_utils.bot_utils import new_task
from ..helper.ext_utils.db_handler import database
from ..helper.ext_utils.quota_utils import (
    TIER_DISPLAY,
    TIER_ORDER,
    get_quota_summary,
    set_user_tier,
)
from ..helper.telegram_helper.message_utils import auto_delete_message, send_message


@new_task
async def set_tier(_, message):
    """Admin command: /settier <user_id> <tier>"""
    args = message.text.split()
    if len(args) != 3:
        reply = await send_message(
            message,
            "Usage: <code>/settier &lt;user_id&gt; &lt;tier&gt;</code>\n"
            f"Valid tiers: <code>{', '.join(TIER_ORDER)}</code>",
        )
        await auto_delete_message(message, reply, stime=60)
        return

    try:
        target_id = int(args[1])
    except ValueError:
        reply = await send_message(message, "❌ Invalid user ID.")
        await auto_delete_message(message, reply, stime=60)
        return

    tier = args[2].lower()
    if tier not in TIER_ORDER:
        reply = await send_message(
            message,
            f"❌ Invalid tier <b>{tier}</b>.\n"
            f"Valid tiers: <code>{', '.join(TIER_ORDER)}</code>",
        )
        await auto_delete_message(message, reply, stime=60)
        return

    set_user_tier(target_id, tier)
    await database.update_user_data(target_id)

    reply = await send_message(
        message,
        f"✅ Tier for user <code>{target_id}</code> set to <b>{TIER_DISPLAY.get(tier, tier)}</b>.",
    )
    await auto_delete_message(message, reply, stime=90)


@new_task
async def my_quota(_, message):
    """/myquota – show the calling user's tier and quota info."""
    user_id = message.from_user.id
    summary = get_quota_summary(user_id)
    reply = await send_message(
        message,
        f"⌬ <b>Your Quota Info</b>\n│\n{summary}",
    )
    await auto_delete_message(message, reply, stime=120)
