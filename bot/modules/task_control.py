"""
Task Control – Pause / Resume / Cancel via inline buttons or text commands.

Text command:
    /taskctl pause <gid>
    /taskctl resume <gid>
    /taskctl cancel <gid>

Callback data (from inline keyboard in status message):
    taskctl pause  <gid> <owner_user_id>
    taskctl resume <gid> <owner_user_id>
    taskctl cancel <gid> <owner_user_id>
"""

from pyrogram.errors import QueryIdInvalid

from .. import task_dict_lock, user_data
from ..core.config_manager import Config
from ..core.tg_client import TgClient
from ..core.torrent_manager import TorrentManager
from ..helper.ext_utils.bot_utils import new_task
from ..helper.ext_utils.status_utils import get_task_by_gid, MirrorStatus
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.message_utils import (
    auto_delete_message,
    send_message,
)


def _is_authorized(actor_id: int, owner_id: int) -> bool:
    """Return True if *actor_id* may control the task owned by *owner_id*."""
    if actor_id == Config.OWNER_ID:
        return True
    if actor_id == owner_id:
        return True
    ud = user_data.get(actor_id, {})
    return bool(ud.get("SUDO"))


async def _pause_task(task) -> str:
    """Pause *task* if the engine supports it. Return a result message."""
    eng = task.engine
    gid = task.gid()
    try:
        if eng.startswith("Aria2"):
            await TorrentManager.aria2.forcePause(gid)
            return "⏸ Download paused."
        elif eng.startswith("qBit"):
            await TorrentManager.qbittorrent.torrents.stop([task._info.hash])
            return "⏸ Download paused."
        else:
            return "⚠️ Pause is not supported for this task type."
    except Exception as e:
        return f"❌ Failed to pause: {e}"


async def _resume_task(task) -> str:
    """Resume *task* if the engine supports it. Return a result message."""
    eng = task.engine
    gid = task.gid()
    try:
        if eng.startswith("Aria2"):
            await TorrentManager.aria2.unpause(gid)
            return "▶️ Download resumed."
        elif eng.startswith("qBit"):
            await TorrentManager.qbittorrent.torrents.resume([task._info.hash])
            return "▶️ Download resumed."
        else:
            return "⚠️ Resume is not supported for this task type."
    except Exception as e:
        return f"❌ Failed to resume: {e}"


@new_task
async def task_control_cmd(_, message):
    """Handle /taskctl <action> <gid>."""
    args = message.text.split()
    if len(args) < 3:
        reply = await send_message(
            message,
            "Usage: <code>/taskctl &lt;pause|resume|cancel&gt; &lt;gid&gt;</code>",
        )
        await auto_delete_message(message, reply, stime=60)
        return

    action = args[1].lower()
    gid = args[2]
    user_id = message.from_user.id

    task = await get_task_by_gid(gid)
    if task is None:
        reply = await send_message(message, f"❌ No task found with GID <code>{gid}</code>.")
        await auto_delete_message(message, reply, stime=60)
        return

    owner_id = task.listener.user_id
    if not _is_authorized(user_id, owner_id):
        reply = await send_message(message, "❌ This task does not belong to you.")
        await auto_delete_message(message, reply, stime=60)
        return

    if action == "pause":
        result = await _pause_task(task)
    elif action == "resume":
        result = await _resume_task(task)
    elif action == "cancel":
        obj = task.task()
        await obj.cancel_task()
        result = "⏹ Task cancelled."
    else:
        result = f"❌ Unknown action: <code>{action}</code>. Use pause, resume, or cancel."

    reply = await send_message(message, result)
    await auto_delete_message(message, reply, stime=60)


@new_task
async def task_control_cb(_, query):
    """Handle callback queries: taskctl <action> <gid> <owner_user_id>."""
    data = query.data.split()
    if len(data) < 3:
        try:
            await query.answer("Invalid callback data.", show_alert=True)
        except QueryIdInvalid:
            pass
        return

    action = data[1].lower()
    gid = data[2]
    owner_id = int(data[3]) if len(data) > 3 else 0
    actor_id = query.from_user.id

    if not _is_authorized(actor_id, owner_id):
        try:
            await query.answer("❌ This task does not belong to you.", show_alert=True)
        except QueryIdInvalid:
            pass
        return

    task = await get_task_by_gid(gid)
    if task is None:
        try:
            await query.answer(f"Task {gid} not found.", show_alert=True)
        except QueryIdInvalid:
            pass
        return

    if action == "pause":
        result = await _pause_task(task)
    elif action == "resume":
        result = await _resume_task(task)
    elif action == "cancel":
        obj = task.task()
        await obj.cancel_task()
        result = "⏹ Task cancelled."
    else:
        result = f"Unknown action: {action}"

    try:
        await query.answer(result, show_alert=True)
    except QueryIdInvalid:
        pass
