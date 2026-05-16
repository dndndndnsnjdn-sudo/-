"""
╔══════════════════════════════════════════════════════════════════════════════╗
║         🤖  بوت استضافة وتشغيل ملفات البايثون - نسخة إدارة قوية v3.1         ║
║              Telegram Python Bot Hosting & Runner — All-in-One                ║
║                                                                              ║
║   ✅ كل شيء في ملف واحد (التوكن، الآيدي، الإعدادات، القنوات، الكود)            ║
║   ✅ كل التحكم بالأزرار — لا أوامر سلاش                                       ║
║   ✅ النقاط تُمنح فقط: عند الدعوة (مشاركة) أو الشراء أو منح المشرف يدوياً       ║
║   ✅ إدارة قنوات الاشتراك الإجباري ديناميكياً من لوحة الإدارة                  ║
║   ✅ رفع مجاني واحد عند أول دخول، بعدها كل رفع يكلف نقاطاً                    ║
║   ✅ يرفع ويستضيف ويشغّل ملفات بايثون و ZIP، ويثبت المكتبات تلقائياً           ║
║   ✅ إذا تعذّر التشغيل: يُغلَّف الملف في ZIP مع requirements.txt ويُرسَل للمالك ║
║   ✅ يعمل على أي استضافة (VPS / Heroku / Railway / Render / Termux ...)       ║
║                                                                              ║
║   التشغيل:  python bot.py                                                    ║
║   المتطلبات: راجع requirements.txt                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ════════════════════════════════════════════════════════════════════════════
# 📦  الاستيرادات
# ════════════════════════════════════════════════════════════════════════════
import os
import re
import io
import sys
import ast
import json
import time
import math
import uuid
import html
import base64
import shutil
import signal
import random
import hashlib
import zipfile
import asyncio
import logging
import platform
import tempfile
import threading
import subprocess
import traceback
import urllib.parse
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, List, Any, Tuple, Set, Union, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
from functools import wraps
from collections import defaultdict, Counter, deque

try:
    from telegram import (
        Update, InlineKeyboardButton, InlineKeyboardMarkup,
        InputFile, BotCommand, BotCommandScopeDefault, BotCommandScopeChat,
        ChatMember, LabeledPrice, ReplyKeyboardRemove, Message,
    )
    from telegram.ext import (
        Application, CommandHandler, CallbackQueryHandler,
        MessageHandler, filters, ContextTypes, ConversationHandler,
        PreCheckoutQueryHandler, JobQueue,
    )
    from telegram.constants import ParseMode, ChatAction, ChatMemberStatus
    from telegram.error import TelegramError, BadRequest, Forbidden, Conflict
except ImportError:
    print("❌ مكتبة python-telegram-bot غير مثبتة.\n   نفّذ:  pip install -r requirements.txt")
    raise

# ════════════════════════════════════════════════════════════════════════════
# ⚙️  الإعدادات الأساسية — عدّل من هنا (أو ضعها كمتغيرات بيئة)
# ════════════════════════════════════════════════════════════════════════════

# 🔑 توكن البوت — من @BotFather
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "8406671676:AAH60tLuqHb88G_kVyELs7fMHUkGbtdrSMU")

# 👑 آيدي المشرفين (يمكن إضافة أكثر من واحد)
_admin_env = os.getenv("ADMIN_IDS", "8018653004.8259194746")
ADMIN_IDS: List[int] = []
for _x in _admin_env.split(","):
    _x = _x.strip()
    if _x.lstrip("-").isdigit():
        ADMIN_IDS.append(int(_x))
if not ADMIN_IDS:
    ADMIN_IDS = [8018653004]

# 💎 سعر النقاط بنجوم تيليجرام
DEFAULT_STARS_PER_10_POINTS: int = 15

# 📁 ملفات و مجلدات العمل
DATABASE_FILE: str = os.getenv("DATABASE_FILE", "bot_database.json")
FILES_DIR: str  = os.getenv("FILES_DIR", "hosted_files")
LOGS_DIR: str   = os.getenv("LOGS_DIR", "bot_logs")
BACKUP_DIR: str = os.getenv("BACKUP_DIR", "backups")
TEMP_DIR: str   = os.getenv("TEMP_DIR", "temp_work")

# 🧱 الحدود الافتراضية
MAX_FILE_SIZE_MB: int       = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
MAX_PROCESSES_PER_USER: int = int(os.getenv("MAX_PROCESSES_PER_USER", "3"))
RUN_TIMEOUT_SECONDS: int    = int(os.getenv("RUN_TIMEOUT_SECONDS", "0"))
INSTALL_TIMEOUT_SECONDS: int= int(os.getenv("INSTALL_TIMEOUT_SECONDS", "600"))

# 🌐 معلومات البوت
BOT_VERSION: str = "3.1.0-hosting"
BOT_NAME: str    = "PyHost Pro"
SUPPORT_USERNAME: str = os.getenv("SUPPORT_USERNAME", "og4_z")  # بدون @
PAYMENT_PROVIDER_TOKEN: str = ""  # فارغ = نجوم تيليجرام XTR

# 🎬 ملصقات متحركة — ضع Sticker File ID فقط بين علامتي الاقتباس.
# الاسم تحت كل خانة يوضح مكان الاستخدام داخل البوت.
STICKERS: Dict[str, str] = {
    "upload_success": "",  # صح / نجاح رفع الملف
    "login_success": "CAACAgQAAxkBAxvcqmoHqBAYg1w5e-KMgCVC-Lh8WK_uAAIWAANf_gYhgW1qULu_b787BA",       # دخول ناجح / فتح القائمة
    "hosting_started": "",     # تشغيل الاستضافة بعد الرفع
    "installing_libs": "AAMCBAADGQEDG92sageqByBwwcqhgeL2o9qY_Ej1AT8AAhoGAAItglRSvVvA4nVI0vcBAAdtAAM7BA",      # جاري تثبيت المكتبات
    "share_link": "",          # مشاركة رابط الملف أو الدعوة
    "points_added": "",        # إضافة أو استلام نقاط
    "security_blocked": "",    # رفض ملف خطر وحظر مؤكد
    "support_error": "",        # خطأ أو تواصل مع الدعم
    "admin_action": "",         # إجراء إداري مهم
    "subscription_ok": "AAMCBAADGQEDHEtaaghlSir59abfiRa7xzqQzphFgOkAAvECAAKMI1xTvn9SAAGq3m0oAQAHbQADOwQ",      # تحقق الاشتراك الإجباري
}

# إنشاء المجلدات
for _d in (FILES_DIR, LOGS_DIR, BACKUP_DIR, TEMP_DIR):
    try:
        os.makedirs(_d, exist_ok=True)
    except Exception:
        pass

# ════════════════════════════════════════════════════════════════════════════
# 📝  السجلات
# ════════════════════════════════════════════════════════════════════════════
_log_path = os.path.join(LOGS_DIR, f"bot_{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(_log_path, encoding="utf-8"),
    ],
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)
logger = logging.getLogger("PyHostBot")

# ════════════════════════════════════════════════════════════════════════════
# 🎨  الأيقونات
# ════════════════════════════════════════════════════════════════════════════
class Icon:
    BOT="🤖"; FIRE="🔥"; STAR="⭐"; DIAMOND="💎"; ROCKET="🚀"
    LOCK="🔒"; UNLOCK="🔓"; KEY="🔑"; CHECK="✅"; CROSS="❌"
    WARN="⚠️"; INFO="ℹ️"; GIFT="🎁"; CROWN="👑"; USER="👤"
    USERS="👥"; SETTINGS="⚙️"; STATS="📊"; FILE="📄"; FOLDER="📁"
    UPLOAD="📤"; DOWNLOAD="📥"; PLAY="▶️"; STOP="⏹"; RESTART="🔄"
    DELETE="🗑"; EDIT="✏️"; SEARCH="🔍"; BELL="🔔"; BROADCAST="📢"
    LINK="🔗"; BACK="⬅️"; NEXT="➡️"; PREV="◀️"; HOME="🏠"
    SUPPORT="💬"; HEART="❤️"; CHANNEL="📣"; PIN="📌"; CLOCK="⏰"
    NOTE="📝"; TASK="✔️"; TOOLS="🛠"; LIGHT="💡"; SHIELD="🛡"
    BAN="🚫"; UNBAN="🟢"; CODE="💻"; TERMINAL="📺"; INBOX="📬"
    PLUS="➕"; MINUS="➖"; LIST="📋"; REFRESH="🔁"


# ════════════════════════════════════════════════════════════════════════════
# 💾  نماذج البيانات
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class User:
    user_id: int
    username: str = ""
    first_name: str = ""
    last_name: str = ""
    points: int = 0
    free_uploads: int = 1
    total_uploads: int = 0
    total_downloads: int = 0
    total_runs: int = 0
    invited_users: List[int] = field(default_factory=list)
    invited_by: Optional[int] = None
    invite_reward_given_for: List[int] = field(default_factory=list)
    is_banned: bool = False
    ban_reason: str = ""
    is_premium: bool = False
    premium_until: str = ""
    join_date: str = ""
    last_active: str = ""
    files: List[str] = field(default_factory=list)
    settings: Dict[str, Any] = field(default_factory=dict)
    language: str = "ar"
    purchases_total_stars: int = 0
    notifications_enabled: bool = True


@dataclass
class HostedFile:
    file_id: str
    file_name: str
    owner_id: int
    upload_date: str
    size: int = 0
    downloads: int = 0
    libraries: List[str] = field(default_factory=list)
    is_active: bool = True
    description: str = ""
    category: str = "general"
    process_id: Optional[int] = None
    run_count: int = 0
    last_run: str = ""
    last_stop: str = ""
    auto_restart: bool = False
    is_public: bool = False
    install_log: str = ""
    runtime_log: str = ""
    stored_path: str = ""
    entry_file: str = ""
    is_zip: bool = False


@dataclass
class Channel:
    chat_id: str
    title: str = ""
    invite_link: str = ""
    added_by: int = 0
    added_at: str = ""
    enabled: bool = True


# ════════════════════════════════════════════════════════════════════════════
# 💾  قاعدة البيانات
# ════════════════════════════════════════════════════════════════════════════

class Database:
    """قاعدة بيانات JSON مع قفل خيطي وحفظ تلقائي"""

    DEFAULT_SETTINGS: Dict[str, Any] = {
        "maintenance_mode": False,
        "require_subscription": True,
        "points_per_invite": 2,
        "upload_cost": 1,
        "stars_per_10_points": DEFAULT_STARS_PER_10_POINTS,
        "max_file_size_mb": MAX_FILE_SIZE_MB,
        "allowed_extensions": [".py", ".zip"],
        "welcome_message": "🎉 أهلاً بك في بوت الاستضافة وتشغيل ملفات بايثون!",
        "bot_active": True,
        "auto_install_libs": True,
        "auto_run_after_upload": True,
        "auto_restart_default": False,
        "send_zip_if_run_fails": True,
        "strict_hosting_security": True,
        "ban_on_confirmed_danger": True,
        "max_processes_per_user": MAX_PROCESSES_PER_USER,
        "run_timeout_seconds": RUN_TIMEOUT_SECONDS,
        "first_upload_free": True,
        "broadcast_throttle_ms": 50,
        "log_runtime_lines": 200,
        "public_files_enabled": True,
        "support_username": SUPPORT_USERNAME,
        "stickers": dict(STICKERS),
    }

    def __init__(self):
        self._lock = threading.RLock()
        self.users: Dict[int, User] = {}
        self.files: Dict[str, HostedFile] = {}
        self.channels: Dict[str, Channel] = {}
        self.stats: Dict[str, Any] = {
            "total_users": 0,
            "total_files": 0,
            "total_downloads": 0,
            "total_points_given": 0,
            "total_stars_received": 0,
            "total_runs": 0,
            "created_at": datetime.now().isoformat(),
        }
        self.settings: Dict[str, Any] = dict(self.DEFAULT_SETTINGS)
        self.pending_payments: Dict[int, Dict[str, Any]] = {}
        self.banned_words: List[str] = []
        self.broadcast_history: List[Dict[str, Any]] = []
        self.promo_codes: Dict[str, Dict[str, Any]] = {}
        self.security_events: List[Dict[str, Any]] = []
        self._dirty: bool = False
        self._last_save: float = 0.0
        self.load()

    # ─────────────────────────────── تحميل / حفظ ───────────────────────────────
    def load(self) -> None:
        with self._lock:
            try:
                if not os.path.exists(DATABASE_FILE):
                    self.save(force=True)
                    return
                with open(DATABASE_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for uid, udata in data.get("users", {}).items():
                    udata.pop("user_id", None)
                    self.users[int(uid)] = User(user_id=int(uid), **{k: v for k, v in udata.items() if k in User.__annotations__})
                for fid, fdata in data.get("files", {}).items():
                    fdata.pop("file_id", None)
                    self.files[fid] = HostedFile(file_id=fid, **{k: v for k, v in fdata.items() if k in HostedFile.__annotations__})
                for cid, cdata in data.get("channels", {}).items():
                    cdata.pop("chat_id", None)
                    self.channels[cid] = Channel(chat_id=cid, **{k: v for k, v in cdata.items() if k in Channel.__annotations__})
                self.stats.update(data.get("stats", {}))
                self.settings.update(data.get("settings", {}))
                self.banned_words = data.get("banned_words", [])
                self.broadcast_history = data.get("broadcast_history", [])
                self.promo_codes = data.get("promo_codes", {})
                self.security_events = data.get("security_events", [])[-300:]
                logger.info(
                    "✅ تم تحميل %d مستخدم، %d ملف، %d قناة",
                    len(self.users), len(self.files), len(self.channels),
                )
            except Exception as e:
                logger.exception("❌ خطأ في تحميل قاعدة البيانات: %s", e)

    def save(self, force: bool = False) -> None:
        with self._lock:
            try:
                now = time.time()
                if not force and (now - self._last_save) < 0.5 and not self._dirty:
                    return
                payload = {
                    "users":    {str(uid): asdict(u) for uid, u in self.users.items()},
                    "files":    {fid: asdict(f)     for fid, f in self.files.items()},
                    "channels": {cid: asdict(c)     for cid, c in self.channels.items()},
                    "stats":    self.stats,
                    "settings": self.settings,
                    "banned_words": self.banned_words,
                    "broadcast_history": self.broadcast_history[-200:],
                    "promo_codes": self.promo_codes,
                    "security_events": self.security_events[-300:],
                    "saved_at": datetime.now().isoformat(),
                }
                tmp = DATABASE_FILE + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(payload, f, ensure_ascii=False, indent=2)
                os.replace(tmp, DATABASE_FILE)
                self._last_save = now
                self._dirty = False
            except Exception as e:
                logger.exception("❌ خطأ في حفظ قاعدة البيانات: %s", e)

    def mark_dirty(self) -> None:
        self._dirty = True

    # ─────────────────────────────── مستخدمون ───────────────────────────────
    def get_user(self, user_id: int, **kwargs) -> User:
        with self._lock:
            if user_id not in self.users:
                now_iso = datetime.now().isoformat()
                self.users[user_id] = User(
                    user_id=user_id,
                    join_date=now_iso,
                    last_active=now_iso,
                    free_uploads=1 if self.settings.get("first_upload_free", True) else 0,
                    **{k: v for k, v in kwargs.items() if k in User.__annotations__},
                )
                self.stats["total_users"] = len(self.users)
                self.save(force=True)
            return self.users[user_id]

    def update_user(self, user: User, save: bool = True) -> None:
        with self._lock:
            user.last_active = datetime.now().isoformat()
            self.users[user.user_id] = user
            if save:
                self.save()
            else:
                self.mark_dirty()

    def all_users(self) -> List[User]:
        with self._lock:
            return list(self.users.values())

    def search_users(self, query: str) -> List[User]:
        q = query.strip().lower()
        out: List[User] = []
        for u in self.all_users():
            if (q in str(u.user_id) or q in (u.username or "").lower()
                    or q in (u.first_name or "").lower()
                    or q in (u.last_name or "").lower()):
                out.append(u)
        return out

    # ─────────────────────────────── ملفات ───────────────────────────────
    def add_file(self, hf: HostedFile) -> None:
        with self._lock:
            self.files[hf.file_id] = hf
            self.stats["total_files"] = len(self.files)
            self.save(force=True)

    def get_file(self, file_id: str) -> Optional[HostedFile]:
        return self.files.get(file_id)

    def remove_file(self, file_id: str) -> bool:
        with self._lock:
            hf = self.files.pop(file_id, None)
            if not hf:
                return False
            owner = self.users.get(hf.owner_id)
            if owner and file_id in owner.files:
                owner.files.remove(file_id)
            self.stats["total_files"] = len(self.files)
            self.save(force=True)
            return True

    def user_files(self, user_id: int) -> List[HostedFile]:
        return [f for f in self.files.values() if f.owner_id == user_id]

    # ─────────────────────────────── قنوات ───────────────────────────────
    def add_channel(self, ch: Channel) -> None:
        with self._lock:
            self.channels[ch.chat_id] = ch
            self.save(force=True)

    def remove_channel(self, chat_id: str) -> bool:
        with self._lock:
            if chat_id in self.channels:
                del self.channels[chat_id]
                self.save(force=True)
                return True
            return False

    def all_channels(self, enabled_only: bool = False) -> List[Channel]:
        chs = list(self.channels.values())
        if enabled_only:
            chs = [c for c in chs if c.enabled]
        return chs


# نسخة عامة من قاعدة البيانات
db = Database()


# ════════════════════════════════════════════════════════════════════════════
# 🎬 ملصقات + رسائل دعم سريعة
# ════════════════════════════════════════════════════════════════════════════

def sticker_id(name: str) -> str:
    stickers = db.settings.get("stickers") or {}
    return str(stickers.get(name) or STICKERS.get(name) or "").strip()


async def send_named_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE, name: str) -> None:
    sid = sticker_id(name)
    if not sid:
        return
    try:
        await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sid)
    except Exception as e:
        logger.debug("sticker %s failed: %s", name, e)


def support_rows(back_cb: str = "menu:main") -> List[List[InlineKeyboardButton]]:
    sup = db.settings.get("support_username") or SUPPORT_USERNAME
    rows: List[List[InlineKeyboardButton]] = []
    if sup:
        rows.append([InlineKeyboardButton(f"{Icon.SUPPORT} تكلم مع الدعم", url=f"https://t.me/{sup}")])
    rows.append([InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data=back_cb)])
    return rows


def progress_bar(percent: int, width: int = 10) -> str:
    percent = max(0, min(100, int(percent)))
    filled = round(width * percent / 100)
    return "▰" * filled + "▱" * (width - filled)


async def edit_progress(msg: Message, title: str, percent: int, detail: str = "") -> None:
    try:
        text = f"{Icon.LIGHT} <b>{escape_html(title)}</b>\n{progress_bar(percent)} <b>{percent}%</b>"
        if detail:
            text += f"\n{escape_html(detail)}"
        await msg.edit_text(text, parse_mode=ParseMode.HTML)
    except BadRequest as e:
        if "not modified" not in str(e).lower():
            logger.debug("progress edit failed: %s", e)
    except Exception as e:
        logger.debug("progress edit failed: %s", e)


async def run_blocking_with_progress(msg: Message, title: str, fn: Callable, *args) -> Any:
    task = asyncio.create_task(asyncio.to_thread(fn, *args))
    frames = [12, 22, 34, 46, 58, 69, 79, 88, 94]
    i = 0
    while not task.done():
        await edit_progress(msg, title, frames[min(i, len(frames) - 1)], "لا تغلق البوت، العملية تعمل الآن…")
        i += 1
        await asyncio.sleep(1.6)
    result = await task
    await edit_progress(msg, title, 100, "انتهت العملية.")
    return result

# ════════════════════════════════════════════════════════════════════════════
# 🔧  أدوات مساعدة عامة
# ════════════════════════════════════════════════════════════════════════════

def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


def format_size(size: int) -> str:
    s = float(size)
    for unit in ("B", "KB", "MB", "GB"):
        if s < 1024:
            return f"{s:.2f} {unit}"
        s /= 1024
    return f"{s:.2f} TB"


def format_dt(iso: str, default: str = "—") -> str:
    if not iso:
        return default
    try:
        dt = datetime.fromisoformat(iso)
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return iso


def humanize_delta(iso: str) -> str:
    if not iso:
        return "—"
    try:
        dt = datetime.fromisoformat(iso)
        delta = datetime.now() - dt
        sec = int(delta.total_seconds())
        if sec < 60:    return f"منذ {sec}ث"
        if sec < 3600:  return f"منذ {sec // 60}د"
        if sec < 86400: return f"منذ {sec // 3600}س"
        return f"منذ {sec // 86400} يوم"
    except Exception:
        return iso


def generate_file_id() -> str:
    return hashlib.md5(
        f"{datetime.now().isoformat()}{os.urandom(8).hex()}".encode()
    ).hexdigest()[:12]


def safe_filename(name: str) -> str:
    name = (name or "file").strip().replace("\\", "_").replace("/", "_")
    name = re.sub(r"[^\w.\-+ ()\[\]]+", "_", name, flags=re.U)
    return name[:120] or "file"


def chunk_list(lst: List[Any], n: int) -> List[List[Any]]:
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def shorten(text: str, limit: int = 60) -> str:
    if not text:
        return ""
    return text if len(text) <= limit else text[:limit - 1] + "…"


def escape_html(text: str) -> str:
    return html.escape(text or "")


def now_iso() -> str:
    return datetime.now().isoformat()


def parse_size_mb(s: str) -> Optional[int]:
    try:
        return int(float(s))
    except Exception:
        return None


def is_safe_ext(name: str) -> bool:
    ext = os.path.splitext(name)[1].lower()
    return ext in db.settings.get("allowed_extensions", [".py", ".zip"])


# ════════════════════════════════════════════════════════════════════════════
# 🎁  محرك النقاط — يُمنح فقط عبر: الدعوة • الشراء • منح المشرف
# ════════════════════════════════════════════════════════════════════════════

class PointSource:
    INVITE   = "invite"
    PURCHASE = "purchase"
    ADMIN    = "admin"

    ALLOWED: Set[str] = {INVITE, PURCHASE, ADMIN}


def grant_points(user: User, amount: int, source: str, note: str = "") -> bool:
    """منح نقاط — مصدر مسموح فقط. يرجع True عند النجاح."""
    if amount <= 0:
        return False
    if source not in PointSource.ALLOWED:
        logger.warning("محاولة منح نقاط من مصدر غير مسموح: %s", source)
        return False
    user.points += amount
    db.stats["total_points_given"] = db.stats.get("total_points_given", 0) + amount
    db.update_user(user, save=False)
    logger.info(
        "💎 +%d نقطة لـ %d (مصدر=%s) ملاحظة=%s",
        amount, user.user_id, source, note,
    )
    return True


def consume_points(user: User, amount: int) -> bool:
    if amount <= 0:
        return True
    if user.points < amount:
        return False
    user.points -= amount
    db.update_user(user, save=False)
    return True


# ════════════════════════════════════════════════════════════════════════════
# 🛡  ديكوريترات الحماية
# ════════════════════════════════════════════════════════════════════════════

def admin_only(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *a, **kw):
        uid = update.effective_user.id if update.effective_user else 0
        if not is_admin(uid):
            await _reply_anywhere(update, f"{Icon.BAN} هذا الإجراء للمشرفين فقط.")
            return
        return await func(update, context, *a, **kw)
    return wrapper


def check_banned(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *a, **kw):
        uid = update.effective_user.id if update.effective_user else 0
        if not uid:
            return
        u = db.get_user(uid)
        if u.is_banned:
            txt = f"{Icon.BAN} أنت محظور من استخدام البوت."
            if u.ban_reason:
                txt += f"\nالسبب: {escape_html(u.ban_reason)}"
            await _reply_anywhere(update, txt)
            return
        return await func(update, context, *a, **kw)
    return wrapper


def maintenance_gate(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *a, **kw):
        if db.settings.get("maintenance_mode") and not is_admin(update.effective_user.id):
            await _reply_anywhere(
                update,
                f"{Icon.TOOLS} البوت في وضع الصيانة حالياً. عُد بعد قليل."
            )
            return
        return await func(update, context, *a, **kw)
    return wrapper


async def _reply_anywhere(update: Update, text: str, **kw) -> None:
    """يرسل رسالة سواء جاء التحديث من رسالة أو ضغط زر."""
    try:
        if update.callback_query:
            try:
                await update.callback_query.answer()
            except Exception:
                pass
            await update.callback_query.message.reply_text(text, **kw)
        elif update.message:
            await update.message.reply_text(text, **kw)
        elif update.effective_chat:
            await update.effective_chat.send_message(text, **kw)
    except Exception as e:
        logger.warning("reply_anywhere failed: %s", e)


# ════════════════════════════════════════════════════════════════════════════
# 📣  نظام الاشتراك الإجباري الديناميكي
# ════════════════════════════════════════════════════════════════════════════

async def check_subscription(user_id: int, bot) -> Tuple[bool, List[Channel]]:
    """يرجع (مشترك في الكل، قائمة القنوات غير المشترك بها)."""
    if not db.settings.get("require_subscription", False):
        return True, []
    channels = db.all_channels(enabled_only=True)
    if not channels:
        return True, []
    missing: List[Channel] = []
    for ch in channels:
        try:
            member = await bot.get_chat_member(chat_id=ch.chat_id, user_id=user_id)
            status = getattr(member, "status", None)
            ok_statuses = {
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            }
            if status not in ok_statuses:
                missing.append(ch)
        except Forbidden:
            logger.warning("البوت ليس مشرفاً في القناة %s", ch.chat_id)
            # لا نعدّ البوت متضرراً — نعتبرها غير مشترك ليُظهر للمستخدم القناة
            missing.append(ch)
        except BadRequest as e:
            logger.warning("خطأ بالتحقق من اشتراك %s: %s", ch.chat_id, e)
            missing.append(ch)
        except Exception as e:
            logger.warning("استثناء بالتحقق من اشتراك %s: %s", ch.chat_id, e)
            missing.append(ch)
    return (len(missing) == 0), missing


def subscription_keyboard(missing: List[Channel]) -> InlineKeyboardMarkup:
    rows: List[List[InlineKeyboardButton]] = []
    for ch in missing:
        title = ch.title or ch.chat_id
        url = ch.invite_link
        if not url and ch.chat_id.startswith("@"):
            url = f"https://t.me/{ch.chat_id[1:]}"
        if url:
            rows.append([InlineKeyboardButton(f"{Icon.CHANNEL} {shorten(title, 30)}", url=url)])
        else:
            rows.append([InlineKeyboardButton(f"{Icon.CHANNEL} {shorten(title, 30)}", callback_data="noop")])
    rows.append([InlineKeyboardButton(f"{Icon.CHECK} تحققت — تابع", callback_data="check_sub")])
    return InlineKeyboardMarkup(rows)


async def enforce_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """يفرض الاشتراك. يرجع True إذا اجتاز المستخدم، False إذا أُوقف."""
    uid = update.effective_user.id
    if is_admin(uid):
        return True
    ok, missing = await check_subscription(uid, context.bot)
    if ok:
        return True
    text = (
        f"{Icon.LOCK} <b>الاشتراك إجباري</b>\n\n"
        f"للاستمرار يجب الاشتراك في القنوات التالية ثم اضغط «تحققت»:"
    )
    kb = subscription_keyboard(missing)
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text(text, reply_markup=kb, parse_mode=ParseMode.HTML)
        except Exception:
            await update.callback_query.message.reply_text(text, reply_markup=kb, parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text(text, reply_markup=kb, parse_mode=ParseMode.HTML)
    return False



# ════════════════════════════════════════════════════════════════════════════
# 🛡 حماية الاستضافة — حظر فقط عند خطر مؤكد جداً
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class SecurityScan:
    blocked: bool = False
    ban: bool = False
    score: int = 0
    reasons: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class HostingSecurity:
    """فحص دفاعي لملفات الاستضافة. لا يحظر إلا عند مؤشرات مؤكدة على استهداف المضيف."""

    CERTAIN_PATTERNS: List[Tuple[str, str]] = [
        (r"(?i)BOT_TOKEN|ADMIN_IDS|SUPPORT_USERNAME|PAYMENT_PROVIDER_TOKEN", "محاولة قراءة إعدادات بوت الاستضافة"),
        (r"(?i)bot_database\.json|hosted_files|bot_logs|backups|temp_work", "محاولة لمس ملفات الاستضافة الداخلية"),
        (r"(?i)DATABASE_FILE|FILES_DIR|LOGS_DIR|BACKUP_DIR|TEMP_DIR", "محاولة الوصول لمتغيرات مسارات الاستضافة"),
        (r"(?i)SUPABASE_SERVICE_ROLE_KEY|AWS_SECRET_ACCESS_KEY|SECRET_KEY|PRIVATE_KEY", "محاولة قراءة أسرار بيئة حساسة"),
        (r"rm\s+-rf\s+/(?:\s|$)|shutil\.rmtree\(\s*['\"]/(?:['\"]|\s)", "محاولة حذف جذر النظام"),
        (r"os\.remove\(\s*DATABASE_FILE|open\(\s*DATABASE_FILE", "محاولة تعديل قاعدة بيانات الاستضافة"),
        (r"subprocess\.(?:Popen|run|call).*?(?:curl|wget).*?\|\s*(?:sh|bash)", "تحميل وتنفيذ سكربت خارجي مباشرة"),
    ]

    WARN_PATTERNS: List[Tuple[str, str]] = [
        (r"subprocess\.|os\.system\(|eval\(|exec\(", "يستخدم تنفيذ أوامر/كود؛ مسموح لكن تحت المراقبة"),
        (r"socket\.|requests\.|aiohttp\.|httpx\.", "يتصل بالشبكة؛ طبيعي للبوتات لكن سُجّل للتتبع"),
    ]

    @classmethod
    def scan_source(cls, source: str, label: str) -> SecurityScan:
        res = SecurityScan()
        for pattern, reason in cls.CERTAIN_PATTERNS:
            if re.search(pattern, source, re.DOTALL):
                res.score += 120
                res.reasons.append(f"{label}: {reason}")
        for pattern, reason in cls.WARN_PATTERNS:
            if re.search(pattern, source, re.DOTALL):
                res.warnings.append(f"{label}: {reason}")
        if res.score >= 120:
            res.blocked = True
            res.ban = bool(db.settings.get("ban_on_confirmed_danger", True))
        return res

    @classmethod
    def merge(cls, items: List[SecurityScan]) -> SecurityScan:
        out = SecurityScan()
        for item in items:
            out.score += item.score
            out.reasons.extend(item.reasons)
            out.warnings.extend(item.warnings)
            out.blocked = out.blocked or item.blocked
            out.ban = out.ban or item.ban
        return out

    @classmethod
    def scan_file(cls, path: str, label: Optional[str] = None) -> SecurityScan:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return cls.scan_source(f.read(), label or os.path.basename(path))
        except Exception as e:
            r = SecurityScan()
            r.warnings.append(f"تعذر فحص {label or path}: {e}")
            return r

    @classmethod
    def scan_directory(cls, dir_path: str) -> SecurityScan:
        scans: List[SecurityScan] = []
        for root, _, files in os.walk(dir_path):
            for fn in files:
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, dir_path)
                if fn.endswith(".py"):
                    scans.append(cls.scan_file(full, rel))
                if fn.lower() in {".env", "id_rsa", "authorized_keys"}:
                    r = SecurityScan(blocked=True, ban=True, score=120, reasons=[f"{rel}: ملف أسرار/مفاتيح غير مسموح"])
                    scans.append(r)
        return cls.merge(scans)

    @classmethod
    def validate_zip_members(cls, zf: zipfile.ZipFile) -> SecurityScan:
        res = SecurityScan()
        for info in zf.infolist():
            name = info.filename.replace("\\", "/")
            if name.startswith("/") or "../" in name or name.startswith("../"):
                res.blocked = True
                res.ban = True
                res.score += 120
                res.reasons.append(f"مسار ZIP خطر: {name}")
        return res


def safe_extract_zip(zf: zipfile.ZipFile, target_dir: str) -> None:
    base = os.path.abspath(target_dir)
    for member in zf.infolist():
        dest = os.path.abspath(os.path.join(target_dir, member.filename))
        if not dest.startswith(base + os.sep) and dest != base:
            raise ValueError(f"مسار غير آمن داخل ZIP: {member.filename}")
    zf.extractall(target_dir)


async def reject_dangerous_upload(update: Update, context: ContextTypes.DEFAULT_TYPE, u: User, scan: SecurityScan, fname: str, work_dir: str) -> None:
    shutil.rmtree(work_dir, ignore_errors=True)
    u.is_banned = bool(scan.ban)
    u.ban_reason = "ملف خطر مؤكد يستهدف ملفات/أسرار الاستضافة" if scan.ban else "ملف مرفوض أمنياً"
    db.update_user(u)
    db.security_events.append({
        "user_id": u.user_id,
        "file": fname,
        "score": scan.score,
        "reasons": scan.reasons[:8],
        "at": now_iso(),
        "banned": bool(scan.ban),
    })
    db.save(force=True)
    await send_named_sticker(update, context, "security_blocked")
    text = (
        f"{Icon.SHIELD} <b>تم رفض الملف أمنياً</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"الملف: <code>{escape_html(fname)}</code>\n"
        f"السبب: محاولة مؤكدة للمساس بملفات/أسرار الاستضافة.\n"
        f"الإجراء: {'حظر المستخدم' if scan.ban else 'رفض الملف فقط'}"
    )
    await update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(support_rows()))
    for adm in ADMIN_IDS:
        try:
            await context.bot.send_message(
                adm,
                f"{Icon.SHIELD} خطر مؤكد مرفوض\n"
                f"المستخدم: <code>{u.user_id}</code> @{escape_html(u.username or '—')}\n"
                f"الملف: <code>{escape_html(fname)}</code>\n"
                f"الأسباب:\n" + "\n".join(f"• {escape_html(x)}" for x in scan.reasons[:8]),
                parse_mode=ParseMode.HTML,
            )
        except Exception:
            pass

# ════════════════════════════════════════════════════════════════════════════
# 📚  كاشف المكتبات التلقائي
# ════════════════════════════════════════════════════════════════════════════

class LibraryDetector:
    """يحلّل كود بايثون لاستخراج المكتبات الخارجية المطلوبة"""

    STDLIB: Set[str] = {
        "os","sys","re","io","ast","json","time","math","uuid","html","base64",
        "shutil","signal","random","hashlib","zipfile","asyncio","logging",
        "platform","tempfile","threading","subprocess","traceback","urllib",
        "datetime","typing","dataclasses","enum","functools","collections",
        "itertools","string","struct","pathlib","csv","sqlite3","socket",
        "ssl","ftplib","smtplib","email","http","queue","multiprocessing",
        "concurrent","abc","argparse","array","bisect","calendar","copy",
        "ctypes","decimal","difflib","fnmatch","fractions","gc","getopt",
        "getpass","glob","gzip","heapq","inspect","ipaddress","keyword",
        "linecache","locale","mmap","operator","pickle","pkgutil","pprint",
        "py_compile","pyclbr","reprlib","runpy","sched","secrets","select",
        "selectors","shelve","statistics","stringprep","symtable","sysconfig",
        "tabnanny","tarfile","telnetlib","textwrap","timeit","tkinter",
        "token","tokenize","trace","tracemalloc","types","unicodedata",
        "unittest","uu","warnings","wave","weakref","webbrowser","wsgiref",
        "xdrlib","xml","xmlrpc","zoneinfo","__future__",
        # إضافات مهمة (كانت ناقصة وتسبب أخطاء مثل: No matching distribution for bz2)
        "bz2","lzma","zlib","hmac","mimetypes","configparser","contextlib",
        "dis","atexit","numbers","cmath","codecs","encodings","errno",
        "fcntl","grp","pwd","posix","posixpath","ntpath","nt","resource",
        "termios","tty","pty","syslog","readline","rlcompleter","crypt",
        "audioop","colorsys","imghdr","sndhdr","filecmp","msilib","msvcrt",
        "winreg","winsound","cgi","cgitb","quopri","binascii","binhex",
        "code","codeop","compileall","contextvars","dataclasses","dbm",
        "distutils","ensurepip","faulthandler","formatter","imaplib","imp",
        "importlib","macpath","modulefinder","netrc","nis","nntplib",
        "optparse","ossaudiodev","parser","pdb","pipes","poplib","profile",
        "cProfile","pstats","pydoc","sndhdr","spwd","sre_compile",
        "sre_constants","sre_parse","stat","this","turtle","turtledemo",
        "venv","zipapp","zipimport","zoneinfo","_thread","builtins",
    }

    # خرائط أسماء import → اسم حزمة pip
    NAME_MAP: Dict[str, str] = {
        "telegram": "python-telegram-bot",
        "telebot": "pyTelegramBotAPI",
        "cv2": "opencv-python",
        "PIL": "Pillow",
        "yaml": "PyYAML",
        "bs4": "beautifulsoup4",
        "sklearn": "scikit-learn",
        "dotenv": "python-dotenv",
        "discord": "discord.py",
        "Crypto": "pycryptodome",
        "OpenSSL": "pyOpenSSL",
        "MySQLdb": "mysqlclient",
        "psycopg2": "psycopg2-binary",
        "googleapiclient": "google-api-python-client",
        "matplotlib": "matplotlib",
        "scipy": "scipy",
        "numpy": "numpy",
        "pandas": "pandas",
        "requests": "requests",
        "aiohttp": "aiohttp",
        "httpx": "httpx",
        "flask": "Flask",
        "django": "Django",
        "fastapi": "fastapi",
        "uvicorn": "uvicorn",
        "selenium": "selenium",
        "pyrogram": "Pyrogram",
        "telethon": "Telethon",
        "schedule": "schedule",
        "redis": "redis",
        "pymongo": "pymongo",
        "sqlalchemy": "SQLAlchemy",
    }

    @classmethod
    def detect_from_source(cls, source: str) -> List[str]:
        """يستخرج أسماء التحميل (import x / from x import y) من نص بايثون."""
        names: Set[str] = set()
        # محاولة AST أولاً
        try:
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        root = alias.name.split(".")[0]
                        if root:
                            names.add(root)
                elif isinstance(node, ast.ImportFrom):
                    if node.module and node.level == 0:
                        names.add(node.module.split(".")[0])
        except Exception:
            # fallback: regex سطر بسطر
            for line in source.splitlines():
                m1 = re.match(r"\s*import\s+([\w\.]+)", line)
                m2 = re.match(r"\s*from\s+([\w\.]+)\s+import\s+", line)
                if m1:
                    names.add(m1.group(1).split(".")[0])
                elif m2:
                    names.add(m2.group(1).split(".")[0])
        # تصفية المكتبات القياسية
        external = sorted([n for n in names if n and n not in cls.STDLIB])
        # تحويل إلى أسماء pip
        pip_names = [cls.NAME_MAP.get(n, n) for n in external]
        # إزالة التكرار مع الحفاظ على الترتيب
        seen: Set[str] = set()
        out: List[str] = []
        for n in pip_names:
            if n not in seen:
                seen.add(n)
                out.append(n)
        return out

    @classmethod
    def detect_from_file(cls, path: str) -> List[str]:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return cls.detect_from_source(f.read())
        except Exception as e:
            logger.warning("detect_from_file failed: %s", e)
            return []

    @classmethod
    def detect_from_directory(cls, dir_path: str) -> List[str]:
        """يفحص كل ملفات .py في مجلد و يدمج المكتبات."""
        all_libs: Set[str] = set()
        for root, _, files in os.walk(dir_path):
            for fn in files:
                if fn.endswith(".py"):
                    all_libs.update(cls.detect_from_file(os.path.join(root, fn)))
        # إذا وجد requirements.txt اعتمد عليه أيضاً
        req = os.path.join(dir_path, "requirements.txt")
        if os.path.exists(req):
            try:
                with open(req, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            pkg = re.split(r"[<>=!~ ]", line)[0]
                            if pkg:
                                all_libs.add(pkg)
            except Exception:
                pass
        return sorted(all_libs)


def write_requirements(dir_path: str, libs: List[str]) -> str:
    """يكتب requirements.txt في المسار المعطى ويعيد المسار."""
    req_path = os.path.join(dir_path, "requirements.txt")
    # دمج مع موجود
    existing: Set[str] = set()
    if os.path.exists(req_path):
        try:
            with open(req_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        existing.add(re.split(r"[<>=!~ ]", line)[0])
        except Exception:
            pass
    merged = sorted(existing.union(libs))
    with open(req_path, "w", encoding="utf-8") as f:
        f.write("# Auto-generated by PyHost Bot\n")
        for lib in merged:
            f.write(f"{lib}\n")
    return req_path


def make_zip_of_dir(src_dir: str, out_zip: str) -> str:
    """يضغط محتوى مجلد في ZIP ويعيد المسار."""
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(src_dir):
            for fn in files:
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, src_dir)
                zf.write(full, rel)
    return out_zip


# ════════════════════════════════════════════════════════════════════════════
# 🧠  مدير العمليات (تشغيل الملفات المرفوعة)
# ════════════════════════════════════════════════════════════════════════════

class ProcessManager:
    """يدير عمليات الملفات قيد التشغيل ويتابع سجلاتها."""

    def __init__(self) -> None:
        self._procs: Dict[str, subprocess.Popen] = {}
        self._logs: Dict[str, deque] = {}
        self._threads: Dict[str, threading.Thread] = {}
        self._lock = threading.RLock()

    # ───────────────────── تثبيت المكتبات ─────────────────────
    def install_libs(self, libs: List[str], cwd: str) -> Tuple[bool, str]:
        if not libs:
            return True, "لا توجد مكتبات للتثبيت."
        # تصفية إضافية: استبعد أي اسم موجود فعلاً كـ stdlib أو مثبت مسبقاً
        import importlib.util as _il
        filtered: List[str] = []
        skipped: List[str] = []
        for lib in libs:
            base = re.split(r"[<>=!~ \[]", lib)[0].strip()
            if not base:
                continue
            if base in LibraryDetector.STDLIB:
                skipped.append(base); continue
            try:
                if _il.find_spec(base) is not None and base not in LibraryDetector.NAME_MAP.values():
                    skipped.append(base); continue
            except Exception:
                pass
            filtered.append(lib)
        if not filtered:
            return True, f"كل المكتبات قياسية/مثبتة. تم تخطّي: {', '.join(skipped) or '—'}"
        try:
            cmd = [sys.executable, "-m", "pip", "install", "--upgrade",
                   "--no-cache-dir", "--disable-pip-version-check", *filtered]
            logger.info("⏬ تثبيت %s في %s (تخطّي: %s)", filtered, cwd, skipped)
            proc = subprocess.run(
                cmd, cwd=cwd, capture_output=True, text=True,
                timeout=INSTALL_TIMEOUT_SECONDS, check=False,
            )
            out = (proc.stdout or "") + "\n" + (proc.stderr or "")
            if skipped:
                out = f"(تم تخطّي قياسية/مثبتة: {', '.join(skipped)})\n" + out
            return (proc.returncode == 0), out[-4000:]
        except subprocess.TimeoutExpired:
            return False, f"⏱ تجاوز مهلة التثبيت ({INSTALL_TIMEOUT_SECONDS}ث)"
        except Exception as e:
            return False, f"خطأ بالتثبيت: {e}"

    # ───────────────────── تشغيل ─────────────────────
    def start(self, file_id: str, work_dir: str, entry: str) -> Tuple[bool, str]:
        with self._lock:
            if file_id in self._procs and self._procs[file_id].poll() is None:
                return False, "العملية تعمل بالفعل."
            entry_path = os.path.join(work_dir, entry)
            if not os.path.exists(entry_path):
                return False, f"ملف الدخول غير موجود: {entry}"
            try:
                proc = subprocess.Popen(
                    [sys.executable, "-u", entry],
                    cwd=work_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                )
                self._procs[file_id] = proc
                self._logs[file_id] = deque(maxlen=db.settings.get("log_runtime_lines", 200))
                t = threading.Thread(target=self._reader, args=(file_id,), daemon=True)
                self._threads[file_id] = t
                t.start()
                return True, f"PID={proc.pid}"
            except Exception as e:
                return False, f"فشل التشغيل: {e}"

    def _reader(self, file_id: str) -> None:
        proc = self._procs.get(file_id)
        if not proc or not proc.stdout:
            return
        try:
            for line in proc.stdout:
                self._logs[file_id].append(line.rstrip("\n"))
        except Exception as e:
            logger.warning("reader error %s: %s", file_id, e)

    def stop(self, file_id: str) -> Tuple[bool, str]:
        with self._lock:
            proc = self._procs.get(file_id)
            if not proc:
                return False, "لا توجد عملية."
            if proc.poll() is not None:
                return False, "العملية متوقفة بالفعل."
            try:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                return True, "تم الإيقاف."
            except Exception as e:
                return False, f"فشل الإيقاف: {e}"

    def is_running(self, file_id: str) -> bool:
        proc = self._procs.get(file_id)
        return bool(proc and proc.poll() is None)

    def pid(self, file_id: str) -> Optional[int]:
        proc = self._procs.get(file_id)
        return proc.pid if proc else None

    def tail_log(self, file_id: str, n: int = 30) -> str:
        log = self._logs.get(file_id)
        if not log:
            return "(لا يوجد سجل)"
        lines = list(log)[-n:]
        return "\n".join(lines) if lines else "(سجل فارغ)"

    def user_running_count(self, user_id: int) -> int:
        count = 0
        for fid in list(self._procs.keys()):
            hf = db.get_file(fid)
            if hf and hf.owner_id == user_id and self.is_running(fid):
                count += 1
        return count

    def all_running(self) -> List[str]:
        return [fid for fid in self._procs if self.is_running(fid)]


pm = ProcessManager()

# ════════════════════════════════════════════════════════════════════════════
# ⌨️  بناء لوحات الأزرار (Keyboards)
# ════════════════════════════════════════════════════════════════════════════

def kb_main_menu(user_id: int) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(f"{Icon.UPLOAD} رفع ملف", callback_data="menu:upload"),
            InlineKeyboardButton(f"{Icon.FOLDER} ملفاتي",  callback_data="menu:myfiles"),
        ],
        [
            InlineKeyboardButton(f"{Icon.DIAMOND} نقاطي",  callback_data="menu:points"),
            InlineKeyboardButton(f"{Icon.GIFT} ادعُ أصدقاءك", callback_data="menu:invite"),
        ],
        [
            InlineKeyboardButton(f"{Icon.STAR} شراء نقاط",  callback_data="menu:buy"),
            InlineKeyboardButton(f"{Icon.STATS} إحصائياتي", callback_data="menu:stats"),
        ],
        [
            InlineKeyboardButton(f"{Icon.CODE} كود نقاط",   callback_data="menu:redeem"),
            InlineKeyboardButton(f"{Icon.SUPPORT} الدعم",  callback_data="menu:support"),
        ],
        [
            InlineKeyboardButton(f"{Icon.SETTINGS} الإعدادات", callback_data="menu:settings"),
            InlineKeyboardButton(f"{Icon.SHIELD} حماية الاستضافة", callback_data="menu:security"),
        ],
        [
            InlineKeyboardButton(f"{Icon.INFO} عن البوت", callback_data="menu:about"),
        ],
    ]
    if is_admin(user_id):
        rows.append([InlineKeyboardButton(f"{Icon.CROWN} لوحة الإدارة", callback_data="admin:panel")])
    return InlineKeyboardMarkup(rows)


def kb_back(target: str = "menu:main", label: Optional[str] = None) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(label or f"{Icon.BACK} رجوع", callback_data=target)
    ]])


def kb_two(label1: str, cb1: str, label2: str, cb2: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(label1, callback_data=cb1),
        InlineKeyboardButton(label2, callback_data=cb2),
    ]])


def kb_confirm(yes_cb: str, no_cb: str = "menu:main",
               yes_label: Optional[str] = None, no_label: Optional[str] = None) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(yes_label or f"{Icon.CHECK} نعم", callback_data=yes_cb),
        InlineKeyboardButton(no_label  or f"{Icon.CROSS} لا",  callback_data=no_cb),
    ]])


def kb_admin_panel() -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(f"{Icon.STATS} إحصائيات", callback_data="admin:stats"),
            InlineKeyboardButton(f"{Icon.USERS} المستخدمون", callback_data="admin:users"),
        ],
        [
            InlineKeyboardButton(f"{Icon.FOLDER} الملفات",  callback_data="admin:files"),
            InlineKeyboardButton(f"{Icon.CHANNEL} القنوات", callback_data="admin:channels"),
        ],
        [
            InlineKeyboardButton(f"{Icon.SETTINGS} الإعدادات", callback_data="admin:settings"),
            InlineKeyboardButton(f"{Icon.BROADCAST} البث",     callback_data="admin:broadcast"),
        ],
        [
            InlineKeyboardButton(f"{Icon.DIAMOND} إضافة نقاط", callback_data="admin:addpts"),
            InlineKeyboardButton(f"{Icon.MINUS} خصم نقاط",     callback_data="admin:subpts"),
        ],
        [
            InlineKeyboardButton(f"{Icon.BAN} حظر مستخدم",   callback_data="admin:ban"),
            InlineKeyboardButton(f"{Icon.UNBAN} فك الحظر",   callback_data="admin:unban"),
        ],
        [
            InlineKeyboardButton(f"{Icon.SEARCH} بحث مستخدم", callback_data="admin:search"),
            InlineKeyboardButton(f"{Icon.TERMINAL} العمليات", callback_data="admin:procs"),
        ],
        [
            InlineKeyboardButton(f"{Icon.DOWNLOAD} نسخة احتياطية", callback_data="admin:backup"),
            InlineKeyboardButton(f"{Icon.UPLOAD} استعادة نسخة",    callback_data="admin:restore"),
        ],
        [
            InlineKeyboardButton(f"{Icon.TOOLS} وضع الصيانة",     callback_data="admin:maint"),
            InlineKeyboardButton(f"{Icon.SHIELD} كلمات محظورة",  callback_data="admin:bwords"),
        ],
        [
            InlineKeyboardButton(f"{Icon.CODE} أكواد النقاط",      callback_data="admin:codes"),
            InlineKeyboardButton(f"{Icon.SHIELD} مركز الحماية",    callback_data="admin:security"),
        ],
        [
            InlineKeyboardButton(f"🎬 الملصقات",                  callback_data="admin:stickers"),
            InlineKeyboardButton(f"{Icon.INFO} معلومات النظام",    callback_data="admin:sysinfo"),
        ],
        [
            InlineKeyboardButton(f"{Icon.LIST} سجل البث",          callback_data="admin:bhist"),
            InlineKeyboardButton(f"{Icon.SUPPORT} ضبط الدعم",      callback_data="adminset:text:support_username"),
        ],
        [InlineKeyboardButton(f"{Icon.HOME} القائمة الرئيسية", callback_data="menu:main")],
    ]
    return InlineKeyboardMarkup(rows)


def kb_buy_points() -> InlineKeyboardMarkup:
    packs = [(10, 15), (25, 35), (50, 65), (100, 120), (250, 280), (500, 540)]
    rows: List[List[InlineKeyboardButton]] = []
    row: List[InlineKeyboardButton] = []
    for i, (pts, stars) in enumerate(packs):
        row.append(InlineKeyboardButton(f"{pts} نقطة · {stars}⭐", callback_data=f"buy:{pts}:{stars}"))
        if len(row) == 2:
            rows.append(row); row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data="menu:main")])
    return InlineKeyboardMarkup(rows)


def kb_file_actions(file_id: str, is_owner: bool, running: bool, is_admin_view: bool = False) -> InlineKeyboardMarkup:
    rows: List[List[InlineKeyboardButton]] = []
    if is_owner or is_admin_view:
        if running:
            rows.append([
                InlineKeyboardButton(f"{Icon.STOP} إيقاف",    callback_data=f"file:stop:{file_id}"),
                InlineKeyboardButton(f"{Icon.RESTART} إعادة", callback_data=f"file:restart:{file_id}"),
            ])
        else:
            rows.append([
                InlineKeyboardButton(f"{Icon.PLAY} تشغيل",    callback_data=f"file:run:{file_id}"),
                InlineKeyboardButton(f"{Icon.DOWNLOAD} ZIP",  callback_data=f"file:zip:{file_id}"),
            ])
        rows.append([
            InlineKeyboardButton(f"{Icon.TERMINAL} السجل",     callback_data=f"file:log:{file_id}"),
            InlineKeyboardButton(f"{Icon.LIGHT} تثبيت المكتبات", callback_data=f"file:install:{file_id}"),
        ])
        rows.append([
            InlineKeyboardButton(f"{Icon.EDIT} تعديل الوصف",   callback_data=f"file:desc:{file_id}"),
            InlineKeyboardButton(f"{Icon.REFRESH} تبديل الإقلاع التلقائي", callback_data=f"file:auto:{file_id}"),
        ])
        rows.append([
            InlineKeyboardButton(f"{Icon.DELETE} حذف",         callback_data=f"file:del:{file_id}"),
            InlineKeyboardButton(f"{Icon.LINK} رابط مشاركة",  callback_data=f"file:share:{file_id}"),
        ])
    else:
        rows.append([InlineKeyboardButton(f"{Icon.DOWNLOAD} تحميل ZIP", callback_data=f"file:zip:{file_id}")])
    rows.append([InlineKeyboardButton(f"{Icon.BACK} ملفاتي", callback_data="menu:myfiles")])
    return InlineKeyboardMarkup(rows)


def kb_paginated(items: List[Tuple[str, str]], page: int, page_size: int,
                 base_cb: str, back_cb: str = "menu:main") -> InlineKeyboardMarkup:
    """يبني لوحة مفاتيح بصفحات. كل عنصر = (label, cb_data)."""
    total = len(items)
    pages = max(1, math.ceil(total / page_size))
    page = max(0, min(page, pages - 1))
    start = page * page_size
    end = min(start + page_size, total)
    rows: List[List[InlineKeyboardButton]] = []
    for label, cb in items[start:end]:
        rows.append([InlineKeyboardButton(label, callback_data=cb)])
    nav: List[InlineKeyboardButton] = []
    if page > 0:
        nav.append(InlineKeyboardButton(f"{Icon.PREV} السابق", callback_data=f"{base_cb}:{page-1}"))
    nav.append(InlineKeyboardButton(f"{page+1}/{pages}", callback_data="noop"))
    if page < pages - 1:
        nav.append(InlineKeyboardButton(f"التالي {Icon.NEXT}", callback_data=f"{base_cb}:{page+1}"))
    if nav:
        rows.append(nav)
    rows.append([InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data=back_cb)])
    return InlineKeyboardMarkup(rows)


def kb_settings_admin() -> InlineKeyboardMarkup:
    s = db.settings
    def b(label: str, key: str) -> InlineKeyboardButton:
        flag = Icon.CHECK if s.get(key) else Icon.CROSS
        return InlineKeyboardButton(f"{flag} {label}", callback_data=f"adminset:toggle:{key}")
    rows = [
        [b("وضع الصيانة", "maintenance_mode")],
        [b("الاشتراك إجباري", "require_subscription")],
        [b("تثبيت المكتبات تلقائياً", "auto_install_libs")],
        [b("تشغيل تلقائي بعد الرفع", "auto_run_after_upload")],
        [b("إقلاع تلقائي افتراضياً", "auto_restart_default")],
        [b("إرسال ZIP عند فشل التشغيل", "send_zip_if_run_fails")],
        [b("حماية الاستضافة", "strict_hosting_security")],
        [b("حظر عند الخطر المؤكد", "ban_on_confirmed_danger")],
        [b("الرفع المجاني الأول", "first_upload_free")],
        [b("ملفات عامة مفعّلة", "public_files_enabled")],
        [
            InlineKeyboardButton(f"💰 سعر الرفع: {s.get('upload_cost',1)} نقطة", callback_data="adminset:num:upload_cost"),
            InlineKeyboardButton(f"🎁 نقاط الدعوة: {s.get('points_per_invite',2)}", callback_data="adminset:num:points_per_invite"),
        ],
        [
            InlineKeyboardButton(f"⭐ نجوم/10 نقاط: {s.get('stars_per_10_points',15)}", callback_data="adminset:num:stars_per_10_points"),
            InlineKeyboardButton(f"📦 حجم/ميجا: {s.get('max_file_size_mb',50)}", callback_data="adminset:num:max_file_size_mb"),
        ],
        [
            InlineKeyboardButton(f"🧩 عمليات/مستخدم: {s.get('max_processes_per_user',3)}", callback_data="adminset:num:max_processes_per_user"),
            InlineKeyboardButton(f"⏱ مهلة التشغيل: {s.get('run_timeout_seconds',0)}", callback_data="adminset:num:run_timeout_seconds"),
        ],
        [InlineKeyboardButton(f"{Icon.EDIT} تعديل رسالة الترحيب", callback_data="adminset:text:welcome_message")],
        [InlineKeyboardButton(f"{Icon.SUPPORT} تعديل يوزر الدعم", callback_data="adminset:text:support_username")],
        [InlineKeyboardButton(f"{Icon.BACK} لوحة الإدارة", callback_data="admin:panel")],
    ]
    return InlineKeyboardMarkup(rows)


def kb_channels_admin() -> InlineKeyboardMarkup:
    rows: List[List[InlineKeyboardButton]] = []
    for ch in db.all_channels():
        flag = Icon.CHECK if ch.enabled else Icon.CROSS
        title = ch.title or ch.chat_id
        rows.append([
            InlineKeyboardButton(f"{flag} {shorten(title, 25)}", callback_data=f"chan:toggle:{ch.chat_id}"),
            InlineKeyboardButton(f"{Icon.DELETE}", callback_data=f"chan:del:{ch.chat_id}"),
        ])
    rows.append([
        InlineKeyboardButton(f"{Icon.PLUS} إضافة قناة", callback_data="chan:add"),
        InlineKeyboardButton(f"{Icon.REFRESH} تحديث", callback_data="admin:channels"),
    ])
    rows.append([InlineKeyboardButton(f"{Icon.BACK} لوحة الإدارة", callback_data="admin:panel")])
    return InlineKeyboardMarkup(rows)


def kb_settings_user(u: User) -> InlineKeyboardMarkup:
    notif = Icon.CHECK if u.notifications_enabled else Icon.CROSS
    rows = [
        [InlineKeyboardButton(f"{notif} الإشعارات", callback_data="userset:toggle:notif")],
        [InlineKeyboardButton(f"{Icon.LINK} رابط دعوتي", callback_data="menu:invite")],
        [InlineKeyboardButton(f"{Icon.DOWNLOAD} تصدير بياناتي", callback_data="userset:export")],
        [InlineKeyboardButton(f"{Icon.BACK} الرئيسية", callback_data="menu:main")],
    ]
    return InlineKeyboardMarkup(rows)

# ════════════════════════════════════════════════════════════════════════════
# 📜  نصوص العرض (Texts)
# ════════════════════════════════════════════════════════════════════════════

def text_welcome(u: User, bot_username: str) -> str:
    free_left = u.free_uploads
    return (
        f"{Icon.FIRE} <b>{db.settings.get('welcome_message')}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{Icon.USER} الاسم: <b>{escape_html(u.first_name or '—')}</b>\n"
        f"{Icon.DIAMOND} نقاطك: <b>{u.points}</b>\n"
        f"{Icon.GIFT} رفع مجاني متبقي: <b>{free_left}</b>\n"
        f"{Icon.UPLOAD} ملفاتك: <b>{len(u.files)}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{Icon.LIGHT} استخدم الأزرار أدناه للتنقل.\n"
        f"{Icon.LINK} رابط دعوتك:\n"
        f"<code>https://t.me/{bot_username}?start=ref{u.user_id}</code>"
    )


def text_upload_prompt(u: User) -> str:
    cost = db.settings.get("upload_cost", 1)
    if u.free_uploads > 0:
        cost_line = f"{Icon.GIFT} لديك رفع مجاني واحد — سيتم خصمه."
    else:
        cost_line = f"{Icon.DIAMOND} كل رفع يكلف <b>{cost} نقطة</b> (نقاطك: {u.points})"
    return (
        f"{Icon.UPLOAD} <b>رفع ملف بايثون أو ZIP</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{cost_line}\n\n"
        f"{Icon.INFO} أرسل الآن:\n"
        f"  • ملف <code>.py</code> واحد، أو\n"
        f"  • ملف <code>.zip</code> يحتوي مشروعك (اجعل ملف الدخول باسم <b>bot.py</b> أو <b>main.py</b>)\n\n"
        f"الحد الأقصى للحجم: <b>{db.settings.get('max_file_size_mb',50)} MB</b>"
    )


def text_points(u: User) -> str:
    s = db.settings
    return (
        f"{Icon.DIAMOND} <b>محفظة النقاط</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"رصيدك الحالي: <b>{u.points}</b> نقطة\n"
        f"رفع مجاني متبقي: <b>{u.free_uploads}</b>\n"
        f"عدد دعواتك الناجحة: <b>{len(u.invited_users)}</b>\n"
        f"إجمالي ما اشتريت بالنجوم: <b>{u.purchases_total_stars} ⭐</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{Icon.INFO} طُرق الحصول على النقاط:\n"
        f"  {Icon.GIFT} دعوة صديق → <b>{s.get('points_per_invite',2)}</b> نقطة\n"
        f"  {Icon.STAR} الشراء بالنجوم\n"
        f"  {Icon.CROWN} منح من المشرف"
    )


def text_invite(u: User, bot_username: str) -> str:
    link = f"https://t.me/{bot_username}?start=ref{u.user_id}"
    return (
        f"{Icon.GIFT} <b>ادعُ أصدقاءك واربح نقاطاً</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"عند انضمام كل صديق جديد عبر رابطك تحصل على "
        f"<b>{db.settings.get('points_per_invite',2)}</b> نقطة.\n\n"
        f"{Icon.LINK} رابطك:\n<code>{link}</code>\n\n"
        f"دعواتك الناجحة حتى الآن: <b>{len(u.invited_users)}</b>"
    )


def text_stats(u: User) -> str:
    return (
        f"{Icon.STATS} <b>إحصائياتك</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"الانضمام:  {format_dt(u.join_date)}\n"
        f"آخر نشاط:  {humanize_delta(u.last_active)}\n"
        f"الرفع:     <b>{u.total_uploads}</b>\n"
        f"التشغيل:   <b>{u.total_runs}</b>\n"
        f"التحميلات: <b>{u.total_downloads}</b>\n"
        f"النقاط:    <b>{u.points}</b>\n"
        f"الدعوات:   <b>{len(u.invited_users)}</b>\n"
        f"الملفات:   <b>{len(u.files)}</b>"
    )


def text_about() -> str:
    py = sys.version.split()[0]
    return (
        f"{Icon.BOT} <b>{BOT_NAME}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"الإصدار: <b>{BOT_VERSION}</b>\n"
        f"Python: <code>{py}</code>\n"
        f"النظام: <code>{platform.system()} {platform.release()}</code>\n"
        f"إجمالي المستخدمين: <b>{len(db.users)}</b>\n"
        f"إجمالي الملفات:    <b>{len(db.files)}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{Icon.SHIELD} مخصص للاستضافة فقط: رفع، تثبيت، تشغيل، مراقبة، نقاط، وقنوات اشتراك."
    )


def text_admin_panel() -> str:
    return (
        f"{Icon.CROWN} <b>لوحة الإدارة</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"اختر إجراء من الأزرار أدناه."
    )


def text_admin_stats() -> str:
    s = db.stats
    running = len(pm.all_running())
    return (
        f"{Icon.STATS} <b>إحصائيات البوت</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"المستخدمون:      <b>{len(db.users)}</b>\n"
        f"الملفات:         <b>{len(db.files)}</b>\n"
        f"العمليات الحيّة: <b>{running}</b>\n"
        f"إجمالي التشغيل:  <b>{s.get('total_runs',0)}</b>\n"
        f"إجمالي التحميلات:<b>{s.get('total_downloads',0)}</b>\n"
        f"النقاط الممنوحة: <b>{s.get('total_points_given',0)}</b>\n"
        f"نجوم مستلمة:     <b>{s.get('total_stars_received',0)} ⭐</b>\n"
        f"تاريخ البدء:     <b>{format_dt(s.get('created_at',''))}</b>"
    )


# ════════════════════════════════════════════════════════════════════════════
# 🚪  أوامر الدخول الأساسية (start / help)
# ════════════════════════════════════════════════════════════════════════════

@maintenance_gate
@check_banned
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    u = db.get_user(
        user.id,
        username=user.username or "",
        first_name=user.first_name or "",
        last_name=user.last_name or "",
    )

    # معالجة رابط الدعوة start=refXXXX
    args = context.args or []
    if args and args[0].startswith("ref"):
        try:
            inviter_id = int(args[0][3:])
        except Exception:
            inviter_id = 0
        if (inviter_id and inviter_id != u.user_id and not u.invited_by):
            inviter = db.users.get(inviter_id)
            if inviter:
                u.invited_by = inviter_id
                if u.user_id not in inviter.invited_users:
                    inviter.invited_users.append(u.user_id)
                # مكافأة الدعوة (تُمنح مرة واحدة لكل مدعوّ)
                if u.user_id not in inviter.invite_reward_given_for:
                    inviter.invite_reward_given_for.append(u.user_id)
                    pts = int(db.settings.get("points_per_invite", 2))
                    grant_points(inviter, pts, PointSource.INVITE, note=f"invited {u.user_id}")
                    try:
                        await context.bot.send_message(
                            inviter_id,
                            f"{Icon.GIFT} مبروك! انضم صديق جديد عبر رابطك ← +{pts} نقطة.",
                        )
                    except Exception:
                        pass
                db.update_user(inviter)
        db.update_user(u)

    if not await enforce_subscription(update, context):
        return

    await send_named_sticker(update, context, "login_success")
    me = await context.bot.get_me()
    text = text_welcome(u, me.username)
    await update.message.reply_text(
        text, reply_markup=kb_main_menu(u.user_id), parse_mode=ParseMode.HTML,
    )


@maintenance_gate
@check_banned
async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = (
        f"{Icon.INFO} <b>دليل سريع</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• اضغط زر «رفع ملف» وأرسل ملف <code>.py</code> أو <code>.zip</code>.\n"
        f"• بعد الرفع: شغّل / أوقف / حمّل / احذف من أزرار الملف.\n"
        f"• اشترِ نقاطاً بالنجوم أو ادعُ أصدقاءك لتربح.\n"
        f"• اضغط «الإدارة» لو كنت مشرفاً للوصول لكل الأدوات.\n"
    )
    await update.message.reply_text(txt, parse_mode=ParseMode.HTML, reply_markup=kb_back())

# ════════════════════════════════════════════════════════════════════════════
# 📤  استقبال الملفات و رفعها واستضافتها
# ════════════════════════════════════════════════════════════════════════════

# مفاتيح حالة المحادثة (state) داخل context.user_data
ST_AWAIT_UPLOAD       = "awaiting_upload"
ST_AWAIT_BROADCAST    = "awaiting_broadcast"
ST_AWAIT_ADDPTS_ID    = "awaiting_addpts_id"
ST_AWAIT_ADDPTS_AMT   = "awaiting_addpts_amt"
ST_AWAIT_SUBPTS_ID    = "awaiting_subpts_id"
ST_AWAIT_SUBPTS_AMT   = "awaiting_subpts_amt"
ST_AWAIT_BAN_ID       = "awaiting_ban_id"
ST_AWAIT_BAN_REASON   = "awaiting_ban_reason"
ST_AWAIT_UNBAN_ID     = "awaiting_unban_id"
ST_AWAIT_SEARCH       = "awaiting_search"
ST_AWAIT_CHAN_ADD     = "awaiting_channel"
ST_AWAIT_BWORD        = "awaiting_bword"
ST_AWAIT_SET_NUM      = "awaiting_set_num"
ST_AWAIT_SET_TEXT     = "awaiting_set_text"
ST_AWAIT_FILE_DESC    = "awaiting_file_desc"
ST_AWAIT_CODE_REDEEM  = "awaiting_code_redeem"
ST_AWAIT_CODE_CREATE  = "awaiting_code_create"


def clear_state(context: ContextTypes.DEFAULT_TYPE) -> None:
    for k in list(context.user_data.keys()):
        if k.startswith("awaiting_") or k.startswith("state_"):
            context.user_data.pop(k, None)


async def upload_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    u = db.get_user(user.id)
    if not await enforce_subscription(update, context):
        return
    cost = db.settings.get("upload_cost", 1)
    if u.free_uploads <= 0 and u.points < cost:
        text = (
            f"{Icon.WARN} <b>لا توجد نقاط كافية</b>\n"
            f"كل رفع يكلف <b>{cost}</b> نقطة، رصيدك: <b>{u.points}</b>.\n"
            f"يمكنك شراء نقاط أو دعوة أصدقاء."
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{Icon.STAR} شراء نقاط", callback_data="menu:buy"),
             InlineKeyboardButton(f"{Icon.GIFT} الدعوة",   callback_data="menu:invite")],
            [InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data="menu:main")],
        ])
        await _edit_or_send(update, text, kb)
        return
    context.user_data[ST_AWAIT_UPLOAD] = True
    await _edit_or_send(update, text_upload_prompt(u),
                        kb_back("menu:main", f"{Icon.CROSS} إلغاء"))


async def _edit_or_send(update: Update, text: str, kb: Optional[InlineKeyboardMarkup] = None) -> None:
    try:
        if update.callback_query:
            await update.callback_query.edit_message_text(
                text, reply_markup=kb, parse_mode=ParseMode.HTML, disable_web_page_preview=True,
            )
        else:
            await update.message.reply_text(
                text, reply_markup=kb, parse_mode=ParseMode.HTML, disable_web_page_preview=True,
            )
    except BadRequest as e:
        if "not modified" not in str(e).lower():
            logger.warning("_edit_or_send error: %s", e)
    except Exception as e:
        logger.warning("_edit_or_send error: %s", e)


@maintenance_gate
@check_banned
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يلتقط ملفات المستخدم. إذا كان في وضع رفع — يستضيف. وإلا يقترح زر الرفع."""
    if not context.user_data.get(ST_AWAIT_UPLOAD):
        await update.message.reply_text(
            f"{Icon.INFO} لرفع ملف اضغط الزر:",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(f"{Icon.UPLOAD} رفع ملف", callback_data="menu:upload")
            ]]),
        )
        return

    user = update.effective_user
    u = db.get_user(user.id)

    if not await enforce_subscription(update, context):
        return

    doc = update.message.document
    if not doc:
        await update.message.reply_text(f"{Icon.WARN} أرسل ملفاً وليس وسيلة أخرى.")
        return

    # تحقق الحجم
    max_bytes = int(db.settings.get("max_file_size_mb", 50)) * 1024 * 1024
    if doc.file_size and doc.file_size > max_bytes:
        await update.message.reply_text(
            f"{Icon.CROSS} الحجم يتجاوز الحد ({db.settings.get('max_file_size_mb',50)} MB)."
        )
        return

    # تحقق الامتداد
    fname = safe_filename(doc.file_name or "uploaded")
    ext = os.path.splitext(fname)[1].lower()
    allowed = db.settings.get("allowed_extensions", [".py", ".zip"])
    if ext not in allowed:
        await update.message.reply_text(
            f"{Icon.CROSS} الامتداد <code>{ext}</code> غير مسموح. المسموح: "
            f"<code>{', '.join(allowed)}</code>",
            parse_mode=ParseMode.HTML,
        )
        return

    # خصم تكلفة الرفع
    cost = int(db.settings.get("upload_cost", 1))
    used_free = False
    if u.free_uploads > 0:
        u.free_uploads -= 1
        used_free = True
    else:
        if not consume_points(u, cost):
            await update.message.reply_text(f"{Icon.WARN} نقاطك غير كافية.")
            return

    # إنشاء مجلد للملف
    file_id = generate_file_id()
    work_dir = os.path.join(FILES_DIR, file_id)
    os.makedirs(work_dir, exist_ok=True)

    # تنزيل
    await update.message.chat.send_action(ChatAction.UPLOAD_DOCUMENT)
    try:
        tg_file = await context.bot.get_file(doc.file_id)
        saved_path = os.path.join(work_dir, fname)
        await tg_file.download_to_drive(saved_path)
    except Exception as e:
        await update.message.reply_text(f"{Icon.CROSS} فشل التحميل: {e}")
        shutil.rmtree(work_dir, ignore_errors=True)
        # رد الخصم
        if used_free:
            u.free_uploads += 1
        else:
            u.points += cost
        db.update_user(u)
        return

    is_zip = ext == ".zip"
    entry = fname
    libs: List[str] = []

    # فك الضغط لو ZIP
    if is_zip:
        try:
            with zipfile.ZipFile(saved_path, "r") as zf:
                zip_scan = HostingSecurity.validate_zip_members(zf)
                if zip_scan.blocked:
                    await reject_dangerous_upload(update, context, u, zip_scan, fname, work_dir)
                    context.user_data.pop(ST_AWAIT_UPLOAD, None)
                    return
                safe_extract_zip(zf, work_dir)
        except Exception as e:
            await update.message.reply_text(f"{Icon.CROSS} ZIP تالف أو غير آمن: {e}")
            shutil.rmtree(work_dir, ignore_errors=True)
            return
        # اختيار ملف الدخول
        candidates = ["bot.py", "main.py", "app.py", "run.py", "start.py", "index.py"]
        entry = ""
        for c in candidates:
            if os.path.exists(os.path.join(work_dir, c)):
                entry = c
                break
        if not entry:
            # ابحث عن أول .py في الجذر
            for fn in os.listdir(work_dir):
                if fn.endswith(".py"):
                    entry = fn
                    break
        if not entry:
            await update.message.reply_text(
                f"{Icon.WARN} لم أجد ملف بايثون داخل ZIP. سيتم حفظه فقط للتحميل."
            )
        libs = LibraryDetector.detect_from_directory(work_dir)
    else:
        libs = LibraryDetector.detect_from_file(saved_path)

    # فحص حماية الاستضافة قبل التسجيل والتشغيل
    if db.settings.get("strict_hosting_security", True):
        scan = HostingSecurity.scan_directory(work_dir) if is_zip else HostingSecurity.scan_file(saved_path, fname)
        if scan.blocked:
            await reject_dangerous_upload(update, context, u, scan, fname, work_dir)
            context.user_data.pop(ST_AWAIT_UPLOAD, None)
            return

    # تسجيل
    hf = HostedFile(
        file_id=file_id,
        file_name=fname,
        owner_id=u.user_id,
        upload_date=now_iso(),
        size=doc.file_size or os.path.getsize(saved_path),
        libraries=libs,
        is_active=True,
        stored_path=saved_path,
        entry_file=entry,
        is_zip=is_zip,
        auto_restart=bool(db.settings.get("auto_restart_default", False)),
    )
    db.add_file(hf)
    u.files.append(file_id)
    u.total_uploads += 1
    db.update_user(u)

    # كتابة requirements
    if libs:
        write_requirements(work_dir, libs)

    # تثبيت المكتبات وتشغيل الملف تلقائياً عند الإمكان
    await send_named_sticker(update, context, "installing_libs" if libs else "upload_success")
    progress = await update.message.reply_text(
        f"{Icon.LIGHT} <b>جاري تثبيت المكتبات وتجهيز الاستضافة</b>\n{progress_bar(8)} <b>8%</b>",
        parse_mode=ParseMode.HTML,
    )
    install_msg = ""
    install_ok = True
    if libs and db.settings.get("auto_install_libs", True):
        ok, out = await run_blocking_with_progress(progress, "جاري تثبيت المكتبات", pm.install_libs, libs, work_dir)
        install_ok = bool(ok)
        hf.install_log = out
        install_msg = f"\n{Icon.CHECK} تثبيت المكتبات: ناجح" if ok else f"\n{Icon.WARN} تثبيت المكتبات: تعثر، راجع السجل"
        db.add_file(hf)
    else:
        await edit_progress(progress, "لا توجد مكتبات مطلوبة — جاري التشغيل", 75, "تجهيز بيئة الاستضافة…")

    auto_run_msg = ""
    if install_ok and entry and entry.endswith(".py") and db.settings.get("auto_run_after_upload", True):
        await edit_progress(progress, "جاري تشغيل الملف", 90, "تشغيل البوت/السكريبت الآن…")
        ok_run, run_info = pm.start(file_id, work_dir, entry)
        if ok_run:
            hf.run_count += 1
            hf.last_run = now_iso()
            u.total_runs += 1
            db.stats["total_runs"] = db.stats.get("total_runs", 0) + 1
            db.add_file(hf)
            db.update_user(u)
            auto_run_msg = f"\n{Icon.ROCKET} التشغيل التلقائي: يعمل الآن (<code>{escape_html(run_info)}</code>)"
            await send_named_sticker(update, context, "hosting_started")
        else:
            auto_run_msg = f"\n{Icon.WARN} التشغيل التلقائي تعذر: <code>{escape_html(run_info)}</code>"
            await send_named_sticker(update, context, "support_error")
    await edit_progress(progress, "تم تجهيز الاستضافة", 100, "ظهرت لوحة التحكم والإحصائيات بالأسفل.")

    # رد التأكيد المختصر والقوي
    cost_line = ("🎁 رفع مجاني" if used_free else f"💎 خُصم {cost} نقطة")
    libs_text = "، ".join(libs[:7]) + ("…" if len(libs) > 7 else "") if libs else "لا توجد"
    me = await context.bot.get_me()
    share_link = f"https://t.me/{me.username}?start=file_{file_id}"
    msg = (
        f"{Icon.CHECK} <b>تمت الاستضافة بنجاح</b>\n"
        f"{Icon.FILE} <code>{escape_html(fname)}</code> · {format_size(hf.size)}\n"
        f"{Icon.LINK} الرابط: <code>{share_link}</code>\n"
        f"{Icon.STATS} تشغيل {hf.run_count} · تحميل {hf.downloads} · مكتبات {len(libs)}\n"
        f"{Icon.USER} المالك: @{escape_html(u.username or '—')} · نقاطك {u.points}\n"
        f"{Icon.LIGHT} المكتبات: {escape_html(libs_text)}{install_msg}{auto_run_msg}\n"
        f"{Icon.SHIELD} الحماية: فحص الاستضافة اجتاز بدون خطر مؤكد.\n"
        f"{cost_line} — تحكمك بالأسفل."
    )
    await update.message.reply_text(
        msg,
        reply_markup=kb_file_actions(file_id, True, pm.is_running(file_id)),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
    for adm in ADMIN_IDS:
        try:
            await context.bot.send_message(
                adm,
                f"{Icon.UPLOAD} رفع جديد للاستضافة\n"
                f"المستخدم: <code>{u.user_id}</code> @{escape_html(u.username or '—')}\n"
                f"الملف: <code>{escape_html(fname)}</code>\n"
                f"الحجم: <b>{format_size(hf.size)}</b> | مكتبات: <b>{len(libs)}</b>\n"
                f"الرابط: <code>{share_link}</code>",
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except Exception:
            pass
    context.user_data.pop(ST_AWAIT_UPLOAD, None)


# ════════════════════════════════════════════════════════════════════════════
# 📁  إدارة ملفاتي + إجراءات الملف (تشغيل/إيقاف/سجل/حذف/ZIP/تثبيت)
# ════════════════════════════════════════════════════════════════════════════

async def show_my_files(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0) -> None:
    u = db.get_user(update.effective_user.id)
    files = db.user_files(u.user_id)
    if not files:
        text = (
            f"{Icon.FOLDER} <b>ملفاتي</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"لم ترفع أي ملف بعد.\n"
            f"اضغط الزر أدناه للرفع."
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{Icon.UPLOAD} رفع ملف", callback_data="menu:upload")],
            [InlineKeyboardButton(f"{Icon.BACK} الرئيسية", callback_data="menu:main")],
        ])
        await _edit_or_send(update, text, kb)
        return

    items: List[Tuple[str, str]] = []
    for f in sorted(files, key=lambda x: x.upload_date, reverse=True):
        flag = "🟢" if pm.is_running(f.file_id) else "⚪️"
        label = f"{flag} {shorten(f.file_name, 30)} · {format_size(f.size)}"
        items.append((label, f"file:open:{f.file_id}"))
    kb = kb_paginated(items, page, 6, base_cb="myfiles:page", back_cb="menu:main")
    text = (
        f"{Icon.FOLDER} <b>ملفاتي ({len(files)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🟢 = قيد التشغيل   ⚪️ = متوقف\n"
        f"اضغط أي ملف لإدارته."
    )
    await _edit_or_send(update, text, kb)


async def open_file(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf:
        await _edit_or_send(update, f"{Icon.CROSS} الملف غير موجود.", kb_back("menu:myfiles"))
        return
    is_owner = (hf.owner_id == u.user_id) or is_admin(u.user_id)
    running = pm.is_running(file_id)
    pid = pm.pid(file_id) if running else None
    text = (
        f"{Icon.FILE} <b>{escape_html(hf.file_name)}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🆔 المعرّف:   <code>{hf.file_id}</code>\n"
        f"📦 الحجم:     <b>{format_size(hf.size)}</b>\n"
        f"📅 الرفع:     <b>{format_dt(hf.upload_date)}</b>\n"
        f"▶️ ملف الدخول: <code>{escape_html(hf.entry_file or '—')}</code>\n"
        f"📚 المكتبات:  {escape_html('، '.join(hf.libraries[:6]) or '—')}\n"
        f"⚡ الحالة:    {'🟢 يعمل (PID '+str(pid)+')' if running else '⚪️ متوقف'}\n"
        f"🔁 إعادة تلقائية: {'مفعّل' if hf.auto_restart else 'معطّل'}\n"
        f"📈 مرات التشغيل: <b>{hf.run_count}</b>\n"
        f"📥 التحميلات:    <b>{hf.downloads}</b>\n"
        f"📝 الوصف: {escape_html(hf.description) or '—'}"
    )
    kb = kb_file_actions(file_id, is_owner, running, is_admin_view=is_admin(u.user_id))
    await _edit_or_send(update, text, kb)


async def file_run(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf:
        await _edit_or_send(update, f"{Icon.CROSS} الملف غير موجود.", kb_back("menu:myfiles"))
        return
    if hf.owner_id != u.user_id and not is_admin(u.user_id):
        await _edit_or_send(update, f"{Icon.BAN} هذا الملف ليس لك.", kb_back("menu:myfiles"))
        return
    if pm.is_running(file_id):
        await _edit_or_send(update, f"{Icon.INFO} العملية تعمل بالفعل.", kb_back(f"file:open:{file_id}"))
        return
    # تحقق من حد العمليات لكل مستخدم
    max_procs = int(db.settings.get("max_processes_per_user", MAX_PROCESSES_PER_USER))
    if not is_admin(u.user_id) and pm.user_running_count(u.user_id) >= max_procs:
        await _edit_or_send(
            update,
            f"{Icon.WARN} تجاوزت الحد الأقصى للعمليات المتزامنة ({max_procs}). أوقف ملفاً أولاً.",
            kb_back(f"file:open:{file_id}"),
        )
        return
    work_dir = os.path.dirname(hf.stored_path) or os.path.join(FILES_DIR, file_id)
    entry = hf.entry_file or hf.file_name
    ok, info = pm.start(file_id, work_dir, entry)
    if ok:
        hf.run_count += 1
        hf.last_run = now_iso()
        u.total_runs += 1
        db.stats["total_runs"] = db.stats.get("total_runs", 0) + 1
        db.add_file(hf)
        db.update_user(u)
        text = f"{Icon.PLAY} <b>تم التشغيل!</b>\n<code>{escape_html(info)}</code>"
    else:
        text = f"{Icon.CROSS} فشل التشغيل: {escape_html(info)}"
        # إرسال ZIP عند الفشل (إن مفعّل)
        if db.settings.get("send_zip_if_run_fails", True):
            await _send_project_zip(update, context, hf, reason="فشل التشغيل")
    await _edit_or_send(update, text, kb_back(f"file:open:{file_id}", f"{Icon.BACK} رجوع للملف"))


async def file_stop(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf or (hf.owner_id != u.user_id and not is_admin(u.user_id)):
        await _edit_or_send(update, f"{Icon.BAN} لا يمكنك إيقاف هذا الملف.", kb_back("menu:myfiles"))
        return
    ok, info = pm.stop(file_id)
    if ok:
        hf.last_stop = now_iso()
        db.add_file(hf)
    text = f"{Icon.STOP} {escape_html(info)}"
    await _edit_or_send(update, text, kb_back(f"file:open:{file_id}"))


async def file_restart(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    pm.stop(file_id)
    await asyncio.sleep(0.5)
    await file_run(update, context, file_id)


async def file_log(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf or (hf.owner_id != u.user_id and not is_admin(u.user_id)):
        await _edit_or_send(update, f"{Icon.BAN} لا يمكنك عرض هذا السجل.", kb_back("menu:myfiles"))
        return
    tail = pm.tail_log(file_id, 40)
    # احتواء طول السجل
    if len(tail) > 3500:
        tail = "..." + tail[-3500:]
    text = (
        f"{Icon.TERMINAL} <b>سجل التشغيل — آخر 40 سطر</b>\n"
        f"<pre>{escape_html(tail)}</pre>"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{Icon.REFRESH} تحديث", callback_data=f"file:log:{file_id}")],
        [InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data=f"file:open:{file_id}")],
    ])
    await _edit_or_send(update, text, kb)


async def file_install(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf or (hf.owner_id != u.user_id and not is_admin(u.user_id)):
        await _edit_or_send(update, f"{Icon.BAN} لا يمكنك ذلك.", kb_back("menu:myfiles"))
        return
    work_dir = os.path.dirname(hf.stored_path) or os.path.join(FILES_DIR, file_id)
    libs = LibraryDetector.detect_from_directory(work_dir)
    hf.libraries = libs
    if libs:
        write_requirements(work_dir, libs)
    if not libs:
        await _edit_or_send(update, f"{Icon.INFO} لا توجد مكتبات خارجية.",
                            kb_back(f"file:open:{file_id}"))
        return
    msg = await update.callback_query.message.reply_text(f"{Icon.LIGHT} جاري تثبيت المكتبات...", parse_mode=ParseMode.HTML) if update.callback_query else await update.message.reply_text(f"{Icon.LIGHT} جاري تثبيت المكتبات...", parse_mode=ParseMode.HTML)
    await send_named_sticker(update, context, "installing_libs")
    ok, out = await run_blocking_with_progress(msg, "جاري تثبيت المكتبات", pm.install_libs, libs, work_dir)
    hf.install_log = out
    db.add_file(hf)
    icon = Icon.CHECK if ok else Icon.WARN
    snippet = out[-1500:] if out else ""
    text = (
        f"{icon} {'تم التثبيت' if ok else 'فشل التثبيت'}\n"
        f"<pre>{escape_html(snippet)}</pre>"
    )
    await _edit_or_send(update, text, kb_back(f"file:open:{file_id}"))


async def file_delete_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf or (hf.owner_id != u.user_id and not is_admin(u.user_id)):
        await _edit_or_send(update, f"{Icon.BAN} لا يمكنك الحذف.", kb_back("menu:myfiles"))
        return
    text = (
        f"{Icon.WARN} <b>تأكيد الحذف</b>\n"
        f"سيتم حذف الملف <code>{escape_html(hf.file_name)}</code> نهائياً.\n"
        f"هل أنت متأكد؟"
    )
    kb = kb_confirm(yes_cb=f"file:del_yes:{file_id}", no_cb=f"file:open:{file_id}")
    await _edit_or_send(update, text, kb)


async def file_delete_do(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf:
        await _edit_or_send(update, f"{Icon.CROSS} الملف غير موجود.", kb_back("menu:myfiles"))
        return
    if hf.owner_id != u.user_id and not is_admin(u.user_id):
        await _edit_or_send(update, f"{Icon.BAN} لا يمكنك الحذف.", kb_back("menu:myfiles"))
        return
    pm.stop(file_id)
    work_dir = os.path.dirname(hf.stored_path) or os.path.join(FILES_DIR, file_id)
    shutil.rmtree(work_dir, ignore_errors=True)
    db.remove_file(file_id)
    await _edit_or_send(update, f"{Icon.CHECK} تم الحذف.", kb_back("menu:myfiles"))


async def file_zip(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    hf = db.get_file(file_id)
    if not hf:
        await _edit_or_send(update, f"{Icon.CROSS} الملف غير موجود.", kb_back("menu:myfiles"))
        return
    await _send_project_zip(update, context, hf, reason="طلب تحميل")


async def _send_project_zip(update: Update, context: ContextTypes.DEFAULT_TYPE,
                            hf: HostedFile, reason: str = "") -> None:
    work_dir = os.path.dirname(hf.stored_path) or os.path.join(FILES_DIR, hf.file_id)
    # تأكد من وجود requirements
    if hf.libraries:
        write_requirements(work_dir, hf.libraries)
    out_zip = os.path.join(TEMP_DIR, f"{hf.file_id}_{int(time.time())}.zip")
    try:
        make_zip_of_dir(work_dir, out_zip)
    except Exception as e:
        await _reply_anywhere(update, f"{Icon.CROSS} تعذر إنشاء ZIP: {e}")
        return
    caption = (
        f"{Icon.DOWNLOAD} <b>ملف المشروع</b>\n"
        f"الاسم: <code>{escape_html(hf.file_name)}</code>\n"
        f"السبب: {escape_html(reason or 'تحميل')}\n"
        f"يحتوي على: الملفات + <code>requirements.txt</code>"
    )
    try:
        chat = update.effective_chat
        await chat.send_action(ChatAction.UPLOAD_DOCUMENT)
        with open(out_zip, "rb") as f:
            await context.bot.send_document(
                chat_id=chat.id,
                document=InputFile(f, filename=f"{os.path.splitext(hf.file_name)[0]}.zip"),
                caption=caption,
                parse_mode=ParseMode.HTML,
            )
        hf.downloads += 1
        db.stats["total_downloads"] = db.stats.get("total_downloads", 0) + 1
        u = db.users.get(hf.owner_id)
        if u:
            u.total_downloads += 1
            db.update_user(u, save=False)
        db.add_file(hf)
    except Exception as e:
        await _reply_anywhere(update, f"{Icon.CROSS} فشل إرسال الملف: {e}")
    finally:
        try:
            os.remove(out_zip)
        except Exception:
            pass


async def file_toggle_auto(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    u = db.get_user(update.effective_user.id)
    hf = db.get_file(file_id)
    if not hf or (hf.owner_id != u.user_id and not is_admin(u.user_id)):
        await _edit_or_send(update, f"{Icon.BAN} لا يمكنك.", kb_back("menu:myfiles"))
        return
    hf.auto_restart = not hf.auto_restart
    db.add_file(hf)
    await open_file(update, context, file_id)


async def file_share(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    hf = db.get_file(file_id)
    if not hf:
        await _edit_or_send(update, f"{Icon.CROSS} الملف غير موجود.", kb_back("menu:myfiles"))
        return
    me = await context.bot.get_me()
    link = f"https://t.me/{me.username}?start=file_{file_id}"
    text = (
        f"{Icon.LINK} <b>رابط مشاركة الملف</b>\n"
        f"<code>{link}</code>\n\n"
        f"أي شخص يفتح هذا الرابط في البوت سيتمكن من تحميل ملفك (إن كان عاماً)."
    )
    await _edit_or_send(update, text, kb_back(f"file:open:{file_id}"))


async def file_desc_start(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str) -> None:
    context.user_data[ST_AWAIT_FILE_DESC] = file_id
    await _edit_or_send(
        update,
        f"{Icon.EDIT} أرسل وصفاً جديداً للملف (أو اضغط إلغاء):",
        kb_back(f"file:open:{file_id}", f"{Icon.CROSS} إلغاء"),
    )

# ════════════════════════════════════════════════════════════════════════════
# 💎  شراء النقاط بنجوم تيليجرام
# ════════════════════════════════════════════════════════════════════════════

async def show_buy_points(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    u = db.get_user(update.effective_user.id)
    text = (
        f"{Icon.STAR} <b>شراء نقاط بنجوم تيليجرام</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"رصيدك الحالي: <b>{u.points}</b> نقطة\n\n"
        f"اختر باقة:"
    )
    await _edit_or_send(update, text, kb_buy_points())


async def initiate_purchase(update: Update, context: ContextTypes.DEFAULT_TYPE,
                             points: int, stars: int) -> None:
    user = update.effective_user
    chat = update.effective_chat
    try:
        prices = [LabeledPrice(label=f"{points} نقطة", amount=stars)]
        payload = f"pts_{user.id}_{points}_{int(time.time())}"
        db.pending_payments[user.id] = {
            "payload": payload,
            "points": points,
            "stars": stars,
            "created": now_iso(),
        }
        await context.bot.send_invoice(
            chat_id=chat.id,
            title=f"{points} نقطة",
            description=f"شراء {points} نقطة لاستخدامها في رفع الملفات و الاستضافة.",
            payload=payload,
            provider_token=PAYMENT_PROVIDER_TOKEN,   # فارغ = XTR
            currency="XTR",
            prices=prices,
            start_parameter=f"buy{points}",
        )
    except Exception as e:
        logger.exception("invoice failed: %s", e)
        await _reply_anywhere(update, f"{Icon.CROSS} تعذر إنشاء فاتورة الدفع: {e}")


async def precheckout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    q = update.pre_checkout_query
    pending = db.pending_payments.get(q.from_user.id)
    if not pending or pending.get("payload") != q.invoice_payload:
        await q.answer(ok=False, error_message="انتهت صلاحية الفاتورة. أعد المحاولة.")
        return
    await q.answer(ok=True)


async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    payment = msg.successful_payment
    user = update.effective_user
    pending = db.pending_payments.pop(user.id, None) or {}
    points = int(pending.get("points") or 0)
    stars = int(payment.total_amount or pending.get("stars") or 0)
    u = db.get_user(user.id)
    if points <= 0:
        # احتياط: حاول استخراج من البايلود
        m = re.match(r"pts_(\d+)_(\d+)_", payment.invoice_payload or "")
        if m:
            points = int(m.group(2))
    if points > 0:
        grant_points(u, points, PointSource.PURCHASE, note=f"stars={stars}")
        u.purchases_total_stars += stars
        db.stats["total_stars_received"] = db.stats.get("total_stars_received", 0) + stars
        db.update_user(u)
    await msg.reply_text(
        f"{Icon.CHECK} تم استلام الدفع! أُضيفت <b>{points}</b> نقطة لرصيدك.\n"
        f"رصيدك الآن: <b>{u.points}</b>",
        reply_markup=kb_back("menu:main"),
        parse_mode=ParseMode.HTML,
    )
    # إخطار المشرفين
    for adm in ADMIN_IDS:
        try:
            await context.bot.send_message(
                adm,
                f"{Icon.STAR} دفعة جديدة:\n"
                f"المستخدم: <code>{user.id}</code> ({escape_html(user.first_name or '')})\n"
                f"النقاط: <b>{points}</b> | النجوم: <b>{stars}</b>",
                parse_mode=ParseMode.HTML,
            )
        except Exception:
            pass


# ════════════════════════════════════════════════════════════════════════════
# 🔭  عرض النقاط / الدعوة / الإحصائيات / الإعدادات / الدعم / حول
# ════════════════════════════════════════════════════════════════════════════

async def show_points(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    u = db.get_user(update.effective_user.id)
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{Icon.STAR} شراء نقاط", callback_data="menu:buy"),
         InlineKeyboardButton(f"{Icon.GIFT} ادعُ أصدقاءك", callback_data="menu:invite")],
        [InlineKeyboardButton(f"{Icon.BACK} الرئيسية", callback_data="menu:main")],
    ])
    await _edit_or_send(update, text_points(u), kb)


async def show_invite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    u = db.get_user(update.effective_user.id)
    me = await context.bot.get_me()
    link = f"https://t.me/{me.username}?start=ref{u.user_id}"
    share = urllib.parse.quote(f"جرّب هذا البوت لاستضافة ملفات بايثون! {link}")
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{Icon.LINK} مشاركة الرابط",
                              url=f"https://t.me/share/url?url={urllib.parse.quote(link)}&text={share}")],
        [InlineKeyboardButton(f"{Icon.BACK} الرئيسية", callback_data="menu:main")],
    ])
    await send_named_sticker(update, context, "share_link")
    await _edit_or_send(update, text_invite(u, me.username), kb)


async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    u = db.get_user(update.effective_user.id)
    await _edit_or_send(update, text_stats(u), kb_back("menu:main"))


async def show_settings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    u = db.get_user(update.effective_user.id)
    text = (
        f"{Icon.SETTINGS} <b>إعداداتك</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"الإشعارات: <b>{'مفعّلة' if u.notifications_enabled else 'معطّلة'}</b>"
    )
    await _edit_or_send(update, text, kb_settings_user(u))


async def show_support(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sup = db.settings.get("support_username") or SUPPORT_USERNAME
    text = (
        f"{Icon.SUPPORT} <b>الدعم الفني</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"للتواصل مع الإدارة:\n"
    )
    rows: List[List[InlineKeyboardButton]] = []
    if sup:
        rows.append([InlineKeyboardButton(f"{Icon.LINK} تواصل @{sup}", url=f"https://t.me/{sup}")])
    else:
        text += f"لم يتم ضبط حساب دعم بعد. تواصل مع المشرف."
    rows.append([InlineKeyboardButton(f"{Icon.BACK} الرئيسية", callback_data="menu:main")])
    await _edit_or_send(update, text, InlineKeyboardMarkup(rows))


async def show_about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _edit_or_send(update, text_about(), kb_back("menu:main"))




async def show_security_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"{Icon.SHIELD} <b>حماية الاستضافة</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"يفحص البوت ملفات <code>.py</code> و <code>.zip</code> قبل التشغيل.\n"
        f"يرفض فقط الخطر المؤكد مثل محاولة قراءة أسرار الاستضافة أو حذف ملفاتها.\n"
        f"الملفات الطبيعية للبوتات لا تُحظر بسبب الشبكة أو المكتبات وحدها."
    )
    await _edit_or_send(update, text, kb_back("menu:main"))


async def redeem_code_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_CODE_REDEEM] = True
    await _edit_or_send(update, f"{Icon.CODE} أرسل كود النقاط الآن:", kb_back("menu:points", f"{Icon.CROSS} إلغاء"))


async def redeem_code_do(update: Update, context: ContextTypes.DEFAULT_TYPE, raw: str) -> None:
    context.user_data.pop(ST_AWAIT_CODE_REDEEM, None)
    code = raw.strip().upper()
    promo = db.promo_codes.get(code)
    u = db.get_user(update.effective_user.id)
    if not promo or not promo.get("active", True):
        await update.message.reply_text(f"{Icon.CROSS} الكود غير صحيح أو متوقف.")
        return
    used_by = promo.setdefault("used_by", [])
    limit = int(promo.get("limit", 1))
    if u.user_id in used_by:
        await update.message.reply_text(f"{Icon.INFO} استخدمت هذا الكود سابقاً.")
        return
    if len(used_by) >= limit:
        await update.message.reply_text(f"{Icon.WARN} انتهى حد استخدام هذا الكود.")
        return
    points = int(promo.get("points", 0))
    if points <= 0:
        await update.message.reply_text(f"{Icon.CROSS} الكود لا يحتوي نقاطاً.")
        return
    used_by.append(u.user_id)
    grant_points(u, points, PointSource.ADMIN, note=f"promo:{code}")
    db.update_user(u, save=False)
    db.save(force=True)
    await send_named_sticker(update, context, "points_added")
    await update.message.reply_text(
        f"{Icon.CHECK} تم تفعيل الكود <code>{escape_html(code)}</code>\n+<b>{points}</b> نقطة · رصيدك الآن <b>{u.points}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{Icon.DIAMOND} نقاطي", callback_data="menu:points")]]),
    )


@admin_only
async def admin_codes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = f"{Icon.CODE} <b>أكواد النقاط</b>\n━━━━━━━━━━━━━━━━━━━━\n"
    if not db.promo_codes:
        text += "لا توجد أكواد."
    else:
        for code, data in list(db.promo_codes.items())[:30]:
            used = len(data.get("used_by", []))
            text += f"• <code>{escape_html(code)}</code> — {data.get('points',0)} نقطة — {used}/{data.get('limit',1)}\n"
    rows = [
        [InlineKeyboardButton(f"{Icon.PLUS} إضافة كود", callback_data="code:add"),
         InlineKeyboardButton(f"{Icon.DELETE} مسح الأكواد", callback_data="code:clear")],
        [InlineKeyboardButton(f"{Icon.BACK} لوحة الإدارة", callback_data="admin:panel")],
    ]
    await _edit_or_send(update, text, InlineKeyboardMarkup(rows))


@admin_only
async def admin_code_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_CODE_CREATE] = True
    await _edit_or_send(
        update,
        f"{Icon.CODE} أرسل الكود بهذا الشكل:\n<code>CODE 10 100</code>\nالأول الاسم، الثاني النقاط، الثالث عدد الاستخدام.",
        kb_back("admin:codes", f"{Icon.CROSS} إلغاء"),
    )


async def admin_code_add_save(update: Update, context: ContextTypes.DEFAULT_TYPE, raw: str) -> None:
    context.user_data.pop(ST_AWAIT_CODE_CREATE, None)
    parts = raw.strip().split()
    if len(parts) < 2:
        await update.message.reply_text(f"{Icon.CROSS} الصيغة: CODE POINTS LIMIT")
        return
    code = re.sub(r"[^A-Za-z0-9_-]", "", parts[0]).upper()[:32]
    points = int(parts[1])
    limit = int(parts[2]) if len(parts) > 2 else 1
    db.promo_codes[code] = {"points": points, "limit": max(1, limit), "used_by": [], "active": True, "created_by": update.effective_user.id, "created_at": now_iso()}
    db.save(force=True)
    await send_named_sticker(update, context, "admin_action")
    await update.message.reply_text(
        f"{Icon.CHECK} تم إنشاء الكود <code>{escape_html(code)}</code> بقيمة <b>{points}</b> نقطة / <b>{limit}</b> استخدام.",
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{Icon.CODE} الأكواد", callback_data="admin:codes")]]),
    )


@admin_only
async def admin_codes_clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db.promo_codes = {}
    db.save(force=True)
    await admin_codes(update, context)


@admin_only
async def admin_security(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    events = db.security_events[-20:]
    text = f"{Icon.SHIELD} <b>مركز حماية الاستضافة</b>\n━━━━━━━━━━━━━━━━━━━━\n"
    text += f"الحماية: <b>{'مفعّلة' if db.settings.get('strict_hosting_security', True) else 'معطّلة'}</b>\n"
    text += f"الحظر المؤكد: <b>{'مفعّل' if db.settings.get('ban_on_confirmed_danger', True) else 'معطّل'}</b>\n"
    text += f"أحداث أمنية: <b>{len(db.security_events)}</b>\n"
    if events:
        text += "\nآخر الأحداث:\n"
        for e in events[-8:]:
            text += f"• {format_dt(e.get('at',''))} — <code>{e.get('user_id')}</code> — {escape_html(shorten(e.get('file',''),22))}\n"
    rows = [
        [InlineKeyboardButton(f"{Icon.SHIELD} تبديل الحماية", callback_data="adminset:toggle:strict_hosting_security")],
        [InlineKeyboardButton(f"{Icon.BAN} تبديل الحظر المؤكد", callback_data="adminset:toggle:ban_on_confirmed_danger")],
        [InlineKeyboardButton(f"{Icon.BACK} لوحة الإدارة", callback_data="admin:panel")],
    ]
    await _edit_or_send(update, text, InlineKeyboardMarkup(rows))


@admin_only
async def admin_stickers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    stickers = db.settings.get("stickers") or {}
    text = f"🎬 <b>أماكن الملصقات المتحركة</b>\n━━━━━━━━━━━━━━━━━━━━\n"
    names = [
        ("upload_success", "صح / نجاح رفع ملف"),
        ("login_success", "دخول المستخدم"),
        ("hosting_started", "تشغيل الاستضافة"),
        ("installing_libs", "جاري تثبيت المكتبات"),
        ("share_link", "مشاركة رابط"),
        ("points_added", "إضافة نقاط"),
        ("security_blocked", "رفض خطر مؤكد"),
        ("support_error", "خطأ / دعم"),
        ("admin_action", "إجراء إداري"),
        ("subscription_ok", "نجاح الاشتراك"),
    ]
    for key, label in names:
        val = stickers.get(key) or STICKERS.get(key) or ""
        text += f"• <b>{escape_html(label)}</b>\n<code>{key}</code> = <code>{escape_html(val or 'ضع_ID_هنا')}</code>\n"
    await _edit_or_send(update, text, kb_back("admin:panel"))

# ════════════════════════════════════════════════════════════════════════════
# 👑  لوحة الإدارة — كل التحكم بالأزرار
# ════════════════════════════════════════════════════════════════════════════

@admin_only
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _edit_or_send(update, text_admin_panel(), kb_admin_panel())


@admin_only
async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _edit_or_send(update, text_admin_stats(), kb_back("admin:panel"))


@admin_only
async def admin_users(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0) -> None:
    users = sorted(db.all_users(), key=lambda x: x.last_active, reverse=True)
    items: List[Tuple[str, str]] = []
    for u in users:
        flag = Icon.BAN if u.is_banned else (Icon.CROWN if is_admin(u.user_id) else Icon.USER)
        label = f"{flag} {shorten(u.first_name or str(u.user_id), 20)} · {u.points}💎"
        items.append((label, f"admin:user:{u.user_id}"))
    kb = kb_paginated(items, page, 8, base_cb="admin:users:page", back_cb="admin:panel")
    text = f"{Icon.USERS} <b>المستخدمون ({len(users)})</b>"
    await _edit_or_send(update, text, kb)


@admin_only
async def admin_user_details(update: Update, context: ContextTypes.DEFAULT_TYPE, uid: int) -> None:
    u = db.users.get(uid)
    if not u:
        await _edit_or_send(update, f"{Icon.CROSS} مستخدم غير موجود.", kb_back("admin:users:page:0"))
        return
    text = (
        f"{Icon.USER} <b>تفاصيل المستخدم</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"ID:      <code>{u.user_id}</code>\n"
        f"اسم:    {escape_html(u.first_name)}\n"
        f"يوزر:   @{escape_html(u.username or '—')}\n"
        f"نقاط:   <b>{u.points}</b>\n"
        f"دعوات:  <b>{len(u.invited_users)}</b>\n"
        f"رفع:    <b>{u.total_uploads}</b>\n"
        f"تشغيل:  <b>{u.total_runs}</b>\n"
        f"محظور: <b>{'نعم' if u.is_banned else 'لا'}</b>\n"
        f"انضمام: {format_dt(u.join_date)}\n"
        f"آخر نشاط: {humanize_delta(u.last_active)}"
    )
    rows = [
        [InlineKeyboardButton(f"{Icon.PLUS} +نقاط", callback_data=f"admin:addpts_user:{uid}"),
         InlineKeyboardButton(f"{Icon.MINUS} -نقاط", callback_data=f"admin:subpts_user:{uid}")],
        [InlineKeyboardButton(f"{Icon.BAN} حظر",   callback_data=f"admin:ban_user:{uid}"),
         InlineKeyboardButton(f"{Icon.UNBAN} فك",  callback_data=f"admin:unban_user:{uid}")],
        [InlineKeyboardButton(f"{Icon.FOLDER} ملفاته ({len(u.files)})", callback_data=f"admin:user_files:{uid}")],
        [InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data="admin:users:page:0")],
    ]
    await _edit_or_send(update, text, InlineKeyboardMarkup(rows))


@admin_only
async def admin_files(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0) -> None:
    files = sorted(db.files.values(), key=lambda x: x.upload_date, reverse=True)
    items: List[Tuple[str, str]] = []
    for f in files:
        flag = "🟢" if pm.is_running(f.file_id) else "⚪️"
        items.append((f"{flag} {shorten(f.file_name,28)} · {format_size(f.size)}",
                      f"file:open:{f.file_id}"))
    kb = kb_paginated(items, page, 8, base_cb="admin:files:page", back_cb="admin:panel")
    await _edit_or_send(update, f"{Icon.FOLDER} <b>كل الملفات ({len(files)})</b>", kb)


@admin_only
async def admin_channels(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"{Icon.CHANNEL} <b>إدارة قنوات الاشتراك الإجباري</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"العدد الكلي: <b>{len(db.channels)}</b>\n"
        f"المفعّل: <b>{len(db.all_channels(True))}</b>\n\n"
        f"اضغط على قناة لتفعيلها/تعطيلها أو حذفها.\n"
        f"اضغط «إضافة قناة» لإضافة قناة جديدة."
    )
    await _edit_or_send(update, text, kb_channels_admin())


@admin_only
async def admin_channel_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_CHAN_ADD] = True
    text = (
        f"{Icon.CHANNEL} أرسل القناة بأحد الشكلين:\n"
        f"• <code>@channel_username</code>\n"
        f"• معرّف رقمي مثل <code>-1001234567890</code>\n\n"
        f"{Icon.WARN} يجب أن يكون البوت <b>مشرفاً</b> في القناة."
    )
    await _edit_or_send(update, text, kb_back("admin:channels", f"{Icon.CROSS} إلغاء"))


async def admin_channel_add_save(update: Update, context: ContextTypes.DEFAULT_TYPE, raw: str) -> None:
    raw = raw.strip()
    chat_id = raw
    if not (raw.startswith("@") or raw.lstrip("-").isdigit()):
        await update.message.reply_text(f"{Icon.CROSS} صيغة غير صحيحة.")
        return
    title = raw
    invite = ""
    try:
        chat = await context.bot.get_chat(chat_id)
        title = chat.title or chat.username or raw
        try:
            invite = await context.bot.export_chat_invite_link(chat.id)
        except Exception:
            invite = f"https://t.me/{chat.username}" if chat.username else ""
        chat_id = f"@{chat.username}" if chat.username else str(chat.id)
    except Exception as e:
        await update.message.reply_text(
            f"{Icon.WARN} لم أستطع جلب القناة (تأكد أن البوت مشرف). الخطأ: {e}\n"
            f"سأضيفها كما هي."
        )
    ch = Channel(chat_id=chat_id, title=title, invite_link=invite,
                 added_by=update.effective_user.id, added_at=now_iso(), enabled=True)
    db.add_channel(ch)
    context.user_data.pop(ST_AWAIT_CHAN_ADD, None)
    await update.message.reply_text(
        f"{Icon.CHECK} أضيفت القناة: <b>{escape_html(title)}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(f"{Icon.CHANNEL} القنوات", callback_data="admin:channels")
        ]]),
    )


@admin_only
async def admin_channel_toggle(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id: str) -> None:
    ch = db.channels.get(chat_id)
    if ch:
        ch.enabled = not ch.enabled
        db.save(force=True)
    await admin_channels(update, context)


@admin_only
async def admin_channel_delete(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id: str) -> None:
    db.remove_channel(chat_id)
    await admin_channels(update, context)


@admin_only
async def admin_settings_view(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"{Icon.SETTINGS} <b>إعدادات البوت</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"اضغط أي زر لتبديل/تعديل."
    )
    await _edit_or_send(update, text, kb_settings_admin())


@admin_only
async def admin_settings_toggle(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str) -> None:
    if key in db.settings and isinstance(db.settings[key], bool):
        db.settings[key] = not db.settings[key]
        db.save(force=True)
    await admin_settings_view(update, context)


@admin_only
async def admin_settings_num_start(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str) -> None:
    context.user_data[ST_AWAIT_SET_NUM] = key
    await _edit_or_send(update, f"{Icon.EDIT} أرسل القيمة الرقمية الجديدة لـ <b>{key}</b>:",
                        kb_back("admin:settings", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_settings_text_start(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str) -> None:
    context.user_data[ST_AWAIT_SET_TEXT] = key
    await _edit_or_send(update, f"{Icon.EDIT} أرسل النص الجديد لـ <b>{key}</b>:",
                        kb_back("admin:settings", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_broadcast_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_BROADCAST] = True
    await _edit_or_send(update, f"{Icon.BROADCAST} أرسل الرسالة المراد بثها لجميع المستخدمين الآن:",
                        kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))


async def admin_broadcast_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop(ST_AWAIT_BROADCAST, None)
    msg = update.message
    sent = 0; failed = 0
    throttle = max(1, int(db.settings.get("broadcast_throttle_ms", 50))) / 1000.0
    progress = await msg.reply_text(f"{Icon.BROADCAST} جاري البث...")
    for u in db.all_users():
        try:
            await msg.copy(chat_id=u.user_id)
            sent += 1
        except Exception:
            failed += 1
        if (sent + failed) % 25 == 0:
            try:
                await progress.edit_text(f"{Icon.BROADCAST} {sent} ✓ / {failed} ✗ ...")
            except Exception:
                pass
        await asyncio.sleep(throttle)
    db.broadcast_history.append({
        "by": update.effective_user.id, "at": now_iso(),
        "sent": sent, "failed": failed,
    })
    db.save(force=True)
    await progress.edit_text(f"{Icon.CHECK} انتهى البث.\nنُجح: <b>{sent}</b> | فشل: <b>{failed}</b>",
                             parse_mode=ParseMode.HTML)


@admin_only
async def admin_addpts_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_ADDPTS_ID] = True
    await _edit_or_send(update, f"{Icon.PLUS} أرسل آيدي المستخدم:",
                        kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_subpts_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_SUBPTS_ID] = True
    await _edit_or_send(update, f"{Icon.MINUS} أرسل آيدي المستخدم:",
                        kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_ban_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_BAN_ID] = True
    await _edit_or_send(update, f"{Icon.BAN} أرسل آيدي المستخدم للحظر:",
                        kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_unban_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_UNBAN_ID] = True
    await _edit_or_send(update, f"{Icon.UNBAN} أرسل آيدي المستخدم لفك الحظر:",
                        kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_search_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_SEARCH] = True
    await _edit_or_send(update, f"{Icon.SEARCH} أرسل اسم/يوزر/آيدي للبحث:",
                        kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_procs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    running = pm.all_running()
    text = f"{Icon.TERMINAL} <b>العمليات الحيّة ({len(running)})</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    rows: List[List[InlineKeyboardButton]] = []
    if not running:
        text += "لا توجد عمليات قيد التشغيل."
    else:
        for fid in running:
            hf = db.get_file(fid)
            if not hf: continue
            text += f"• <code>{fid}</code> · {escape_html(shorten(hf.file_name,30))} · PID={pm.pid(fid)}\n"
            rows.append([
                InlineKeyboardButton(f"{Icon.STOP} {shorten(hf.file_name,18)}", callback_data=f"file:stop:{fid}"),
                InlineKeyboardButton(f"{Icon.TERMINAL}", callback_data=f"file:log:{fid}"),
            ])
    rows.append([InlineKeyboardButton(f"{Icon.REFRESH} تحديث", callback_data="admin:procs"),
                 InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data="admin:panel")])
    await _edit_or_send(update, text, InlineKeyboardMarkup(rows))


@admin_only
async def admin_backup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db.save(force=True)
    backup_path = os.path.join(BACKUP_DIR, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip")
    try:
        with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zf:
            if os.path.exists(DATABASE_FILE):
                zf.write(DATABASE_FILE, os.path.basename(DATABASE_FILE))
            for root, _, files in os.walk(FILES_DIR):
                for fn in files:
                    full = os.path.join(root, fn)
                    rel = os.path.relpath(full, ".")
                    zf.write(full, rel)
        with open(backup_path, "rb") as f:
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=InputFile(f, filename=os.path.basename(backup_path)),
                caption=f"{Icon.DOWNLOAD} نسخة احتياطية شاملة",
            )
    except Exception as e:
        await _reply_anywhere(update, f"{Icon.CROSS} فشل النسخ: {e}")


@admin_only
async def admin_maint_toggle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db.settings["maintenance_mode"] = not db.settings.get("maintenance_mode", False)
    db.save(force=True)
    state = "مفعّل ✅" if db.settings["maintenance_mode"] else "معطّل ❌"
    await _edit_or_send(update, f"{Icon.TOOLS} وضع الصيانة الآن: <b>{state}</b>",
                        kb_back("admin:panel"))


@admin_only
async def admin_sysinfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    py = sys.version.split()[0]
    text = (
        f"{Icon.INFO} <b>معلومات النظام</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Python:    <code>{py}</code>\n"
        f"النظام:    <code>{platform.system()} {platform.release()}</code>\n"
        f"المعالج:   <code>{platform.machine()}</code>\n"
        f"المسار:    <code>{escape_html(os.getcwd())}</code>\n"
        f"المستخدمون: <b>{len(db.users)}</b>\n"
        f"الملفات:   <b>{len(db.files)}</b>\n"
        f"العمليات:  <b>{len(pm.all_running())}</b>\n"
        f"الإصدار:   <b>{BOT_VERSION}</b>"
    )
    await _edit_or_send(update, text, kb_back("admin:panel"))


@admin_only
async def admin_broadcast_history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    h = db.broadcast_history[-20:]
    text = f"{Icon.LIST} <b>سجل البث</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    if not h:
        text += "لا يوجد سجل."
    else:
        for b in h:
            text += f"• {format_dt(b.get('at',''))} — ✓{b.get('sent',0)} ✗{b.get('failed',0)} — by <code>{b.get('by','')}</code>\n"
    await _edit_or_send(update, text, kb_back("admin:panel"))


@admin_only
async def admin_bwords(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = f"{Icon.SHIELD} <b>الكلمات المحظورة</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    if not db.banned_words:
        text += "لا توجد."
    else:
        text += "\n".join(f"• <code>{escape_html(w)}</code>" for w in db.banned_words[:50])
    rows = [
        [InlineKeyboardButton(f"{Icon.PLUS} إضافة", callback_data="admin:bword_add"),
         InlineKeyboardButton(f"{Icon.DELETE} مسح الكل", callback_data="admin:bword_clear")],
        [InlineKeyboardButton(f"{Icon.BACK} رجوع", callback_data="admin:panel")],
    ]
    await _edit_or_send(update, text, InlineKeyboardMarkup(rows))


@admin_only
async def admin_bword_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[ST_AWAIT_BWORD] = True
    await _edit_or_send(update, f"{Icon.SHIELD} أرسل الكلمة المراد حظرها:",
                        kb_back("admin:bwords", f"{Icon.CROSS} إلغاء"))


@admin_only
async def admin_bword_clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db.banned_words = []
    db.save(force=True)
    await admin_bwords(update, context)


@admin_only
async def admin_restore_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        f"{Icon.UPLOAD} <b>استعادة نسخة احتياطية</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"أرسل ملف <code>backup_*.zip</code> الذي أنشأه البوت سابقاً، وسيتم استعادته.\n"
        f"(سيُستبدل ملف قاعدة البيانات وملفات المستخدمين)"
    )
    context.user_data["awaiting_restore"] = True
    await _edit_or_send(update, text, kb_back("admin:panel", f"{Icon.CROSS} إلغاء"))

# ════════════════════════════════════════════════════════════════════════════
# 🎯  موجّه ضغطات الأزرار (Callback Router)
# ════════════════════════════════════════════════════════════════════════════

@maintenance_gate
@check_banned
async def callback_router(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    q = update.callback_query
    if not q:
        return
    try:
        await q.answer()
    except Exception:
        pass
    data = q.data or ""

    # تحقق الاشتراك أولاً (إلا لأزرار التحقق نفسها)
    if data not in ("check_sub", "noop") and not is_admin(q.from_user.id):
        if not await enforce_subscription(update, context):
            return

    try:
        # ─── قوائم رئيسية ───
        if data == "noop":
            return
        if data == "check_sub":
            ok, missing = await check_subscription(q.from_user.id, context.bot)
            if ok:
                await send_named_sticker(update, context, "subscription_ok")
                me = await context.bot.get_me()
                u = db.get_user(q.from_user.id)
                await _edit_or_send(update, text_welcome(u, me.username), kb_main_menu(u.user_id))
            else:
                await _edit_or_send(update, f"{Icon.WARN} ما زلت غير مشترك في كل القنوات.",
                                    subscription_keyboard(missing))
            return

        if data == "menu:main":
            me = await context.bot.get_me()
            u = db.get_user(q.from_user.id)
            await _edit_or_send(update, text_welcome(u, me.username), kb_main_menu(u.user_id))
            return
        if data == "menu:upload":   await upload_start(update, context); return
        if data == "menu:myfiles":  await show_my_files(update, context); return
        if data == "menu:points":   await show_points(update, context); return
        if data == "menu:invite":   await show_invite(update, context); return
        if data == "menu:buy":      await show_buy_points(update, context); return
        if data == "menu:stats":    await show_stats(update, context); return
        if data == "menu:redeem":   await redeem_code_start(update, context); return
        if data == "menu:security": await show_security_info(update, context); return
        if data == "menu:settings": await show_settings(update, context); return
        if data == "menu:support":  await show_support(update, context); return
        if data == "menu:about":    await show_about(update, context); return

        # ─── ملفاتي pagination ───
        if data.startswith("myfiles:page:"):
            await show_my_files(update, context, int(data.split(":")[2])); return

        # ─── ملف: إجراءات ───
        if data.startswith("file:"):
            parts = data.split(":")
            action = parts[1]; fid = parts[2] if len(parts) > 2 else ""
            if action == "open":    await open_file(update, context, fid)
            elif action == "run":   await file_run(update, context, fid)
            elif action == "stop":  await file_stop(update, context, fid)
            elif action == "restart": await file_restart(update, context, fid)
            elif action == "log":   await file_log(update, context, fid)
            elif action == "install": await file_install(update, context, fid)
            elif action == "del":   await file_delete_confirm(update, context, fid)
            elif action == "del_yes": await file_delete_do(update, context, fid)
            elif action == "zip":   await file_zip(update, context, fid)
            elif action == "auto":  await file_toggle_auto(update, context, fid)
            elif action == "share": await file_share(update, context, fid)
            elif action == "desc":  await file_desc_start(update, context, fid)
            return

        # ─── شراء ───
        if data.startswith("buy:"):
            _, pts, stars = data.split(":")
            await initiate_purchase(update, context, int(pts), int(stars)); return

        # ─── إعدادات المستخدم ───
        if data == "userset:toggle:notif":
            u = db.get_user(q.from_user.id)
            u.notifications_enabled = not u.notifications_enabled
            db.update_user(u)
            await show_settings(update, context); return
        if data == "userset:export":
            u = db.get_user(q.from_user.id)
            payload = json.dumps(asdict(u), ensure_ascii=False, indent=2).encode("utf-8")
            await context.bot.send_document(
                chat_id=q.from_user.id,
                document=InputFile(io.BytesIO(payload), filename=f"mydata_{u.user_id}.json"),
                caption=f"{Icon.DOWNLOAD} بياناتك الشخصية",
            )
            return

        # ─── إدارة ───
        if not is_admin(q.from_user.id):
            return
        if data == "admin:panel":    await admin_panel(update, context); return
        if data == "admin:stats":    await admin_stats(update, context); return
        if data == "admin:users":    await admin_users(update, context, 0); return
        if data.startswith("admin:users:page:"): await admin_users(update, context, int(data.split(":")[3])); return
        if data.startswith("admin:user:"): await admin_user_details(update, context, int(data.split(":")[2])); return
        if data == "admin:files":    await admin_files(update, context, 0); return
        if data.startswith("admin:files:page:"): await admin_files(update, context, int(data.split(":")[3])); return
        if data == "admin:channels": await admin_channels(update, context); return
        if data == "chan:add":       await admin_channel_add_start(update, context); return
        if data.startswith("chan:toggle:"): await admin_channel_toggle(update, context, data.split(":",2)[2]); return
        if data.startswith("chan:del:"):    await admin_channel_delete(update, context, data.split(":",2)[2]); return
        if data == "admin:settings": await admin_settings_view(update, context); return
        if data.startswith("adminset:toggle:"): await admin_settings_toggle(update, context, data.split(":")[2]); return
        if data.startswith("adminset:num:"):    await admin_settings_num_start(update, context, data.split(":")[2]); return
        if data.startswith("adminset:text:"):   await admin_settings_text_start(update, context, data.split(":")[2]); return
        if data == "admin:broadcast": await admin_broadcast_start(update, context); return
        if data == "admin:addpts":    await admin_addpts_start(update, context); return
        if data == "admin:subpts":    await admin_subpts_start(update, context); return
        if data == "admin:ban":       await admin_ban_start(update, context); return
        if data == "admin:unban":     await admin_unban_start(update, context); return
        if data == "admin:search":    await admin_search_start(update, context); return
        if data == "admin:procs":     await admin_procs(update, context); return
        if data == "admin:backup":    await admin_backup(update, context); return
        if data == "admin:restore":   await admin_restore_info(update, context); return
        if data == "admin:maint":     await admin_maint_toggle(update, context); return
        if data == "admin:sysinfo":   await admin_sysinfo(update, context); return
        if data == "admin:bhist":     await admin_broadcast_history(update, context); return
        if data == "admin:codes":     await admin_codes(update, context); return
        if data == "code:add":        await admin_code_add_start(update, context); return
        if data == "code:clear":      await admin_codes_clear(update, context); return
        if data == "admin:security":  await admin_security(update, context); return
        if data == "admin:stickers":  await admin_stickers(update, context); return
        if data == "admin:bwords":    await admin_bwords(update, context); return
        if data == "admin:bword_add": await admin_bword_add_start(update, context); return
        if data == "admin:bword_clear": await admin_bword_clear(update, context); return
        # سياقات سريعة من تفاصيل مستخدم
        if data.startswith("admin:addpts_user:"):
            uid = int(data.split(":")[2])
            context.user_data[ST_AWAIT_ADDPTS_ID] = False
            context.user_data["addpts_target"] = uid
            context.user_data[ST_AWAIT_ADDPTS_AMT] = True
            await _edit_or_send(update, f"{Icon.PLUS} أرسل عدد النقاط للإضافة للمستخدم <code>{uid}</code>:",
                                kb_back(f"admin:user:{uid}", f"{Icon.CROSS} إلغاء")); return
        if data.startswith("admin:subpts_user:"):
            uid = int(data.split(":")[2])
            context.user_data["subpts_target"] = uid
            context.user_data[ST_AWAIT_SUBPTS_AMT] = True
            await _edit_or_send(update, f"{Icon.MINUS} أرسل عدد النقاط للخصم من <code>{uid}</code>:",
                                kb_back(f"admin:user:{uid}", f"{Icon.CROSS} إلغاء")); return
        if data.startswith("admin:ban_user:"):
            uid = int(data.split(":")[2])
            u = db.users.get(uid)
            if u:
                u.is_banned = True; u.ban_reason = "بواسطة لوحة الإدارة"
                db.update_user(u)
            await admin_user_details(update, context, uid); return
        if data.startswith("admin:unban_user:"):
            uid = int(data.split(":")[2])
            u = db.users.get(uid)
            if u:
                u.is_banned = False; u.ban_reason = ""
                db.update_user(u)
            await admin_user_details(update, context, uid); return
        if data.startswith("admin:user_files:"):
            uid = int(data.split(":")[2])
            files = db.user_files(uid)
            items = [(f"{'🟢' if pm.is_running(f.file_id) else '⚪️'} {shorten(f.file_name,28)}",
                      f"file:open:{f.file_id}") for f in files]
            await _edit_or_send(update, f"{Icon.FOLDER} ملفات المستخدم {uid} ({len(files)})",
                                kb_paginated(items, 0, 8, "noop", f"admin:user:{uid}"))
            return
    except Exception as e:
        logger.exception("callback error for %s: %s", data, e)
        try:
            await q.message.reply_text(f"{Icon.CROSS} خطأ: {escape_html(str(e))}",
                                       parse_mode=ParseMode.HTML)
        except Exception:
            pass


# ════════════════════════════════════════════════════════════════════════════
# 💬  معالج النصوص (لمراحل state)
# ════════════════════════════════════════════════════════════════════════════

@maintenance_gate
@check_banned
async def text_router(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    user = update.effective_user
    ud = context.user_data

    # كلمات محظورة
    if db.banned_words and not is_admin(user.id):
        low = text.lower()
        for w in db.banned_words:
            if w.lower() in low:
                await update.message.reply_text(f"{Icon.SHIELD} كلمة محظورة في رسالتك.")
                return

    # state routing
    if ud.get(ST_AWAIT_CODE_REDEEM): await redeem_code_do(update, context, text); return
    if ud.get(ST_AWAIT_CODE_CREATE) and is_admin(user.id): await admin_code_add_save(update, context, text); return
    if ud.get(ST_AWAIT_FILE_DESC):
        fid = ud.pop(ST_AWAIT_FILE_DESC)
        hf = db.get_file(fid)
        if hf and (hf.owner_id == user.id or is_admin(user.id)):
            hf.description = text[:500]; db.add_file(hf)
            await update.message.reply_text(f"{Icon.CHECK} حُدّث الوصف.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(f"{Icon.FILE} الملف", callback_data=f"file:open:{fid}")
                ]]))
        return
    if ud.get(ST_AWAIT_BROADCAST) and is_admin(user.id):
        await admin_broadcast_do(update, context); return
    if ud.get(ST_AWAIT_CHAN_ADD) and is_admin(user.id):
        await admin_channel_add_save(update, context, text); return
    if ud.get(ST_AWAIT_BWORD) and is_admin(user.id):
        db.banned_words.append(text); db.save(force=True)
        ud.pop(ST_AWAIT_BWORD, None)
        await update.message.reply_text(f"{Icon.CHECK} أضيفت.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{Icon.BACK}",callback_data="admin:bwords")]]))
        return
    if ud.get(ST_AWAIT_SEARCH) and is_admin(user.id):
        ud.pop(ST_AWAIT_SEARCH, None)
        res = db.search_users(text)[:20]
        out = f"{Icon.SEARCH} وُجد {len(res)} نتيجة:\n"
        rows = []
        for u in res:
            out += f"• <code>{u.user_id}</code> — {escape_html(u.first_name or '')} @{escape_html(u.username or '')}\n"
            rows.append([InlineKeyboardButton(f"{Icon.USER} {u.first_name or u.user_id}",
                                              callback_data=f"admin:user:{u.user_id}")])
        rows.append([InlineKeyboardButton(f"{Icon.BACK}", callback_data="admin:panel")])
        await update.message.reply_text(out, parse_mode=ParseMode.HTML,
                                        reply_markup=InlineKeyboardMarkup(rows))
        return
    if ud.get(ST_AWAIT_ADDPTS_ID) and is_admin(user.id):
        try:
            ud["addpts_target"] = int(text); ud.pop(ST_AWAIT_ADDPTS_ID); ud[ST_AWAIT_ADDPTS_AMT] = True
            await update.message.reply_text(f"{Icon.PLUS} أرسل عدد النقاط:")
        except Exception:
            await update.message.reply_text(f"{Icon.CROSS} آيدي غير صحيح.")
        return
    if ud.get(ST_AWAIT_ADDPTS_AMT) and is_admin(user.id):
        try:
            amt = int(text); uid = int(ud.pop("addpts_target")); ud.pop(ST_AWAIT_ADDPTS_AMT)
            u = db.get_user(uid)
            grant_points(u, amt, PointSource.ADMIN, note=f"by {user.id}")
            db.update_user(u)
            await update.message.reply_text(f"{Icon.CHECK} +{amt} للمستخدم {uid}. الرصيد: {u.points}")
        except Exception as e:
            await update.message.reply_text(f"{Icon.CROSS} {e}")
        return
    if ud.get(ST_AWAIT_SUBPTS_ID) and is_admin(user.id):
        try:
            ud["subpts_target"] = int(text); ud.pop(ST_AWAIT_SUBPTS_ID); ud[ST_AWAIT_SUBPTS_AMT] = True
            await update.message.reply_text(f"{Icon.MINUS} أرسل عدد النقاط للخصم:")
        except Exception:
            await update.message.reply_text(f"{Icon.CROSS} آيدي غير صحيح.")
        return
    if ud.get(ST_AWAIT_SUBPTS_AMT) and is_admin(user.id):
        try:
            amt = int(text); uid = int(ud.pop("subpts_target")); ud.pop(ST_AWAIT_SUBPTS_AMT)
            u = db.get_user(uid)
            u.points = max(0, u.points - amt); db.update_user(u)
            await update.message.reply_text(f"{Icon.CHECK} −{amt} من {uid}. الرصيد: {u.points}")
        except Exception as e:
            await update.message.reply_text(f"{Icon.CROSS} {e}")
        return
    if ud.get(ST_AWAIT_BAN_ID) and is_admin(user.id):
        try:
            uid = int(text); ud.pop(ST_AWAIT_BAN_ID)
            u = db.get_user(uid); u.is_banned = True; u.ban_reason = "من لوحة الإدارة"
            db.update_user(u)
            await update.message.reply_text(f"{Icon.BAN} حُظر {uid}.")
        except Exception as e:
            await update.message.reply_text(f"{Icon.CROSS} {e}")
        return
    if ud.get(ST_AWAIT_UNBAN_ID) and is_admin(user.id):
        try:
            uid = int(text); ud.pop(ST_AWAIT_UNBAN_ID)
            u = db.get_user(uid); u.is_banned = False; u.ban_reason = ""
            db.update_user(u)
            await update.message.reply_text(f"{Icon.UNBAN} فُكّ حظر {uid}.")
        except Exception as e:
            await update.message.reply_text(f"{Icon.CROSS} {e}")
        return
    if ud.get(ST_AWAIT_SET_NUM) and is_admin(user.id):
        key = ud.pop(ST_AWAIT_SET_NUM)
        try:
            db.settings[key] = int(text); db.save(force=True)
            await update.message.reply_text(f"{Icon.CHECK} {key} = {db.settings[key]}",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{Icon.BACK}",callback_data="admin:settings")]]))
        except Exception as e:
            await update.message.reply_text(f"{Icon.CROSS} {e}")
        return
    if ud.get(ST_AWAIT_SET_TEXT) and is_admin(user.id):
        key = ud.pop(ST_AWAIT_SET_TEXT)
        db.settings[key] = text; db.save(force=True)
        await update.message.reply_text(f"{Icon.CHECK} حُدّث {key}.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{Icon.BACK}",callback_data="admin:settings")]]))
        return

    # افتراضي: عرض القائمة الرئيسية
    me = await context.bot.get_me()
    u = db.get_user(user.id)
    await update.message.reply_text(text_welcome(u, me.username),
                                    reply_markup=kb_main_menu(u.user_id),
                                    parse_mode=ParseMode.HTML)


# ════════════════════════════════════════════════════════════════════════════
# 🔁  مهمة الإقلاع التلقائي (Auto Restart)
# ════════════════════════════════════════════════════════════════════════════

async def auto_restart_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        for fid, hf in list(db.files.items()):
            if hf.auto_restart and not pm.is_running(fid):
                work_dir = os.path.dirname(hf.stored_path) or os.path.join(FILES_DIR, fid)
                ok, _ = pm.start(fid, work_dir, hf.entry_file or hf.file_name)
                if ok:
                    hf.run_count += 1; hf.last_run = now_iso(); db.add_file(hf)
                    logger.info("🔁 إقلاع تلقائي: %s", fid)
    except Exception as e:
        logger.warning("auto_restart_job: %s", e)


async def auto_backup_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        db.save(force=True)
        # حد أقصى 10 نسخ
        backups = sorted([f for f in os.listdir(BACKUP_DIR) if f.startswith("auto_")])
        while len(backups) > 10:
            try: os.remove(os.path.join(BACKUP_DIR, backups.pop(0)))
            except Exception: pass
        path = os.path.join(BACKUP_DIR, f"auto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip")
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
            if os.path.exists(DATABASE_FILE):
                zf.write(DATABASE_FILE, os.path.basename(DATABASE_FILE))
    except Exception as e:
        logger.warning("auto_backup_job: %s", e)


# ════════════════════════════════════════════════════════════════════════════
# 🚀  نقطة الانطلاق
# ════════════════════════════════════════════════════════════════════════════

async def post_init(application: Application) -> None:
    try:
        await application.bot.set_my_commands([
            BotCommand("start", "🏠 القائمة الرئيسية"),
            BotCommand("help",  "ℹ️ مساعدة"),
        ])
    except Exception as e:
        logger.warning("set_my_commands: %s", e)
    logger.info("✅ البوت جاهز — %s v%s", BOT_NAME, BOT_VERSION)


async def global_error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    err = context.error
    if isinstance(err, Conflict):
        logger.error(
            "Conflict: يوجد تشغيل آخر لنفس توكن البوت. أوقف النسخة الثانية أو الملف المستضاف الذي يستخدم نفس التوكن."
        )
        return
    logger.exception("خطأ غير معالج: %s", err)


_INSTANCE_LOCK_HANDLE = None

def acquire_single_instance_lock() -> bool:
    global _INSTANCE_LOCK_HANDLE
    lock_path = os.path.join(tempfile.gettempdir(), hashlib.sha1(BOT_TOKEN.encode()).hexdigest()[:16] + "_pyhostbot.lock")
    _INSTANCE_LOCK_HANDLE = open(lock_path, "w")
    try:
        if os.name == "posix":
            import fcntl
            fcntl.flock(_INSTANCE_LOCK_HANDLE, fcntl.LOCK_EX | fcntl.LOCK_NB)
        else:
            import msvcrt
            msvcrt.locking(_INSTANCE_LOCK_HANDLE.fileno(), msvcrt.LK_NBLCK, 1)
        _INSTANCE_LOCK_HANDLE.write(str(os.getpid()))
        _INSTANCE_LOCK_HANDLE.flush()
        return True
    except Exception:
        return False


# ════════════════════════════════════════════════════════════════════════════
# 🌐 keep_alive — سيرفر ويب بسيط لاستضافات مثل Replit / Render مجاناً
# ════════════════════════════════════════════════════════════════════════════
def keep_alive() -> None:
    """يشغّل Flask على 0.0.0.0:PORT في Thread مستقل (لا يكسر شيئاً إن لم تكن Flask مثبتة)."""
    try:
        from flask import Flask
    except Exception as _e:
        logger.warning("Flask غير مثبت — تخطي keep_alive (%s)", _e)
        return
    port = int(os.environ.get("PORT", "8080"))
    app = Flask("keep_alive")

    @app.route("/")
    def _home():
        return "I am alive!"

    @app.route("/health")
    def _health():
        return {"ok": True, "ts": int(time.time())}

    def _run():
        try:
            app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
        except Exception as e:
            logger.warning("keep_alive crashed: %s", e)

    threading.Thread(target=_run, daemon=True, name="keep_alive").start()
    logger.info("🌐 keep_alive يعمل على المنفذ %s", port)


def main() -> None:
    if BOT_TOKEN in ("", "ضع_توكن_البوت_هنا"):
        print("\n❌ يجب ضبط BOT_TOKEN في أعلى الملف أو كمتغير بيئة BOT_TOKEN.\n")
        sys.exit(1)

    if not acquire_single_instance_lock():
        logger.error("❌ البوت يعمل بالفعل على نفس الجهاز. أوقف النسخة القديمة أولاً.")
        sys.exit(1)

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # الأوامر الأساسية فقط (الباقي بالأزرار)
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help",  cmd_help))

    # الأزرار
    app.add_handler(CallbackQueryHandler(callback_router))
    app.add_error_handler(global_error_handler)

    # المستندات (رفع ملفات)
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # الدفع
    app.add_handler(PreCheckoutQueryHandler(precheckout_handler))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_handler))

    # نصوص
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_router))

    # المهام الدورية
    try:
        jq = app.job_queue
        if jq:
            jq.run_repeating(auto_restart_job, interval=60, first=30)
            jq.run_repeating(auto_backup_job,  interval=3600, first=600)
    except Exception as e:
        logger.warning("job queue init: %s", e)

    logger.info("🚀 بدء التشغيل...")
    keep_alive()
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("⛔ تم الإيقاف بواسطة المستخدم.")
    except Exception as e:
        logger.exception("❌ خطأ قاتل: %s", e)
        sys.exit(1)
