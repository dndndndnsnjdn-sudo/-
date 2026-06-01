#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                          ║
║   ██████╗ ██╗   ██╗██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██████╗  ██████╗      ║
║   ██╔══██╗╚██╗ ██╔╝██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔═══██╗     ║
║   ██████╔╝ ╚████╔╝ ███████║██║   ██║███████╗   ██║       ██████╔╝██████╔╝██║   ██║     ║
║   ██╔═══╝   ╚██╔╝  ██╔══██║██║   ██║╚════██║   ██║       ██╔═══╝ ██╔══██╗██║   ██║     ║
║   ██║        ██║   ██║  ██║╚██████╔╝███████║   ██║       ██║     ██║  ██║╚██████╔╝     ║
║   ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝     ║
║                                                                                          ║
║                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                     ║
║                    🔥 PyHost PRO ULTRA v10.0 — MEGA EDITION 🔥                          ║
║                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                     ║
║                                                                                          ║
║  ═══════════════════════════  الميزات الرئيسية  ═══════════════════════════             ║
║  ✅ نظام موافقة يدوية — المشرف يوافق أو يرفض كل ملف قبل تشغيله                         ║
║  ✅ لوحة إدارة شاملة منظمة بأقسام واضحة — أزرار فقط بدون أوامر                         ║
║  ✅ ذكاء اصطناعي لتحليل الكود وكشف المخاطر والتقييم التلقائي                           ║
║  ✅ استضافة Python + ZIP مع تثبيت المكتبات تلقائياً                                     ║
║  ✅ تصدير البوت كملف ZIP جاهز (bot.py + requirements.txt)                               ║
║  ✅ نظام إدارة الأدمنز — إضافة وإزالة وصلاحيات متدرجة                                  ║
║  ✅ نظام بريميوم متقدم مع انتهاء تلقائي وأكواد ترقية                                    ║
║  ✅ لوحة متصدرين مع نقاط وترتيب وإنجازات                                               ║
║  ✅ بث متقدم للكل / البريميوم / الجدد / المحددين                                        ║
║  ✅ مراقبة CPU / RAM / قرص في الوقت الفعلي                                             ║
║  ✅ Rate Limiting ضد الفلود مع حجب تلقائي مؤقت                                         ║
║  ✅ نسخ احتياطي تلقائي مجدول + استعادة فورية                                            ║
║  ✅ سجل تدقيق شامل لكل العمليات الحساسة                                                ║
║  ✅ إشعارات فورية لكل حدث مهم مع تفاصيل كاملة                                          ║
║  ✅ إيقاف/تشغيل/إعادة تشغيل جماعي للعمليات                                             ║
║  ✅ جدولة تشغيل الملفات بوقت محدد                                                       ║
║  ✅ حماية API متقدمة — يمنع سرقة التوكن ومحاولات الاختراق                              ║
║  ✅ يعمل على VPS / Railway / Render / Replit / Termux / أي سيرفر                       ║
║                                                                                          ║
║  ───────────────────────────────────────────────────────────────────────────────────    ║
║   التشغيل:  python bot.py                                                               ║
║   المتطلبات: pip install -r requirements.txt                                            ║
║   المطور: PyHost PRO ULTRA Team                                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
"""

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📦 الاستيرادات الأساسية                       ║
# ╚══════════════════════════════════════════════════════════════════╝
import os, re, io, sys, ast, json, time, math, uuid, html, base64, shutil
import signal, random, hashlib, zipfile, asyncio, logging, platform, tempfile
import threading, subprocess, traceback, urllib.parse, copy, struct, inspect
import textwrap, itertools, functools, operator, secrets, string
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, List, Any, Tuple, Set, Union, Callable, Iterator
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from functools import wraps, lru_cache, partial
from collections import defaultdict, Counter, deque, OrderedDict
from pathlib import Path
from contextlib import asynccontextmanager, suppress
from concurrent.futures import ThreadPoolExecutor

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

try:
    import humanize
    HAS_HUMANIZE = True
except ImportError:
    HAS_HUMANIZE = False

try:
    from telegram import (
        Update, InlineKeyboardButton, InlineKeyboardMarkup,
        InputFile, BotCommand, BotCommandScopeDefault,
        ChatMember, Message, Document, PhotoSize,
        ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,
        LabeledPrice, ShippingAddress,
    )
    from telegram.ext import (
        Application, CommandHandler, CallbackQueryHandler,
        MessageHandler, filters, ContextTypes,
        ConversationHandler, JobQueue,
    )
    from telegram.constants import ParseMode, ChatAction, ChatMemberStatus, FileSizeLimit
    from telegram.error import (
        TelegramError, BadRequest, Forbidden, Conflict,
        NetworkError, RetryAfter, TimedOut,
    )
except ImportError:
    print("❌ مكتبة python-telegram-bot غير مثبتة.\n   نفّذ:  pip install -r requirements.txt")
    sys.exit(1)

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ⚙️ الإعدادات الأساسية                         ║
# ╚══════════════════════════════════════════════════════════════════╝

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "8406671676:AAHqCZWaL4h0F7gfAZF0VCcrWOYOy7tf8Sk")

_admin_raw = os.getenv("ADMIN_IDS", "8018653004")
ADMIN_IDS: List[int] = []
for _x in _admin_raw.split(","):
    _x = _x.strip()
    if _x.lstrip("-").isdigit():
        ADMIN_IDS.append(int(_x))
if not ADMIN_IDS:
    ADMIN_IDS = [8018653004]

DATABASE_FILE: str          = os.getenv("DATABASE_FILE",          "bot_database.json")
FILES_DIR: str              = os.getenv("FILES_DIR",               "hosted_files")
LOGS_DIR: str               = os.getenv("LOGS_DIR",               "bot_logs")
BACKUP_DIR: str             = os.getenv("BACKUP_DIR",             "backups")
TEMP_DIR: str               = os.getenv("TEMP_DIR",               "temp_work")
PENDING_DIR: str            = os.getenv("PENDING_DIR",            "pending_files")
AUDIT_LOG_FILE: str         = os.getenv("AUDIT_LOG_FILE",         "audit.log")
EXPORT_DIR: str             = os.getenv("EXPORT_DIR",             "exports")

MAX_FILE_SIZE_MB: int           = int(os.getenv("MAX_FILE_SIZE_MB",           "50"))
MAX_PROCESSES_PER_USER: int     = int(os.getenv("MAX_PROCESSES_PER_USER",     "3"))
MAX_PROCESSES_PREMIUM: int      = int(os.getenv("MAX_PROCESSES_PREMIUM",      "8"))
RUN_TIMEOUT_SECONDS: int        = int(os.getenv("RUN_TIMEOUT_SECONDS",        "0"))
INSTALL_TIMEOUT_SECONDS: int    = int(os.getenv("INSTALL_TIMEOUT_SECONDS",    "600"))
RATE_LIMIT_MESSAGES: int        = int(os.getenv("RATE_LIMIT_MESSAGES",        "15"))
RATE_LIMIT_WINDOW: int          = int(os.getenv("RATE_LIMIT_WINDOW",          "10"))
AUTO_BACKUP_INTERVAL_HOURS: int = int(os.getenv("AUTO_BACKUP_INTERVAL_HOURS", "6"))
MAX_LOG_LINES: int              = int(os.getenv("MAX_LOG_LINES",              "500"))
AI_RISK_THRESHOLD: float        = float(os.getenv("AI_RISK_THRESHOLD",        "0.7"))
MAX_OUTPUT_LENGTH: int          = int(os.getenv("MAX_OUTPUT_LENGTH",          "4000"))

BOT_VERSION: str      = "10.0.0-MEGA"
BOT_NAME: str         = "PyHost PRO ULTRA"
SUPPORT_USERNAME: str = os.getenv("SUPPORT_USERNAME", "support")
# إنشاء المجلدات
for _d in (FILES_DIR, LOGS_DIR, BACKUP_DIR, TEMP_DIR, PENDING_DIR, EXPORT_DIR):
    os.makedirs(_d, exist_ok=True)

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📝 نظام السجلات المتقدم                       ║
# ╚══════════════════════════════════════════════════════════════════╝

_log_path = os.path.join(LOGS_DIR, f"bot_{datetime.now().strftime('%Y%m%d')}.log")

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG':    '\033[36m',
        'INFO':     '\033[32m',
        'WARNING':  '\033[33m',
        'ERROR':    '\033[31m',
        'CRITICAL': '\033[35m',
    }
    RESET = '\033[0m'
    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{color}{record.levelname:<8}{self.RESET}"
        return super().format(record)

_fmt = "%(asctime)s │ %(levelname)s │ %(name)s │ %(message)s"
_file_handler = logging.FileHandler(_log_path, encoding="utf-8")
_file_handler.setFormatter(logging.Formatter(_fmt))
_console_handler = logging.StreamHandler(sys.stdout)
_console_handler.setFormatter(ColorFormatter(_fmt))

logging.basicConfig(level=logging.INFO, handlers=[_file_handler, _console_handler])
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)
logger = logging.getLogger("PyHostBot")

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🎨 مكتبة الأيقونات الكاملة                    ║
# ╚══════════════════════════════════════════════════════════════════╝

class I:
    """أيقونات الواجهة — مركزية لسهولة التعديل"""
    # الحالة والنتائج
    OK="✅"; FAIL="❌"; WARN="⚠️"; INFO="ℹ️"; NEW="🆕"; HOT="🔥"
    # المستخدمون
    USER="👤"; USERS="👥"; CROWN="👑"; ADMIN="🛡️"; OWNER="💎"; BOT="🤖"
    # الأمان
    LOCK="🔒"; UNLOCK="🔓"; KEY="🔑"; SHIELD="🛡"; BAN="🚫"; UNBAN="🟢"
    SECURE="🔐"; TOKEN="🔑"; API="🌐"
    # الملفات والكود
    FILE="📄"; FOLDER="📁"; ZIP="🗜️"; CODE="💻"; PY="🐍"; LOG="📋"
    UPLOAD="📤"; DOWNLOAD="📥"; EXPORT="📦"; IMPORT="📥"; BACKUP="💾"
    # العمليات
    PLAY="▶️"; STOP="⏹️"; RESTART="🔄"; KILL="💀"; PAUSE="⏸️"
    RUN="🏃"; QUEUE="📬"; SCHED="⏰"
    # النظام
    CPU="⚡"; RAM="🧠"; DISK="💽"; NET="🌐"; SERVER="🖥️"; TERM="📺"
    # الإحصائيات والترتيب
    STATS="📊"; CHART="📈"; TROPHY="🏆"; MEDAL="🥇"; STAR="⭐"; POINTS="💠"
    # التفاعل
    BELL="🔔"; BROAD="📢"; MSG="💬"; LINK="🔗"; PIN="📌"; EDIT="✏️"
    # التنقل
    BACK="⬅️"; NEXT="➡️"; HOME="🏠"; MENU="☰"; UP="⬆️"; DOWN="⬇️"
    # المميزات
    PREM="💫"; GIFT="🎁"; DIAMOND="💎"; ROCKET="🚀"; MAGIC="✨"; POWER="💪"
    # الذكاء الاصطناعي
    AI="🧠"; SCAN="🔬"; ANALYZE="🔭"; RISK="⚠️"; BUG="🐛"; CLEAN="✅"
    QUALITY="⭐"; SCORE="🎯"
    # الوقت
    CLOCK="⏰"; TIMER="⏱️"; CAL="📅"; DATE="🗓️"
    # متنوع
    SETTINGS="⚙️"; TOOLS="🛠️"; DELETE="🗑️"; COPY="📋"; TAG="🏷️"
    NOTE="📝"; TASK="✔️"; LIGHT="💡"; SEARCH="🔍"; REFRESH="🔁"
    PLUS="➕"; MINUS="➖"; CHECK="☑️"; CIRCLE="🔵"; RED="🔴"; GREEN="🟢"
    YELLOW="🟡"; PURPLE="🟣"; ORANGE="🟠"; WHITE="⚪"
    # التزيين
    FIRE="🔥"; GEM="💎"; FLASH="⚡"; SPARK="✨"; WAVE="〰️"

# ╔══════════════════════════════════════════════════════════════════╗
# ║               🎨 مولّد الزخارف والفواصل والأطر                   ║
# ╚══════════════════════════════════════════════════════════════════╝

class Art:
    """أدوات الزخرفة النصية"""

    @staticmethod
    def box(title: str, content: str, style: int = 1) -> str:
        """إنشاء صندوق نصي مزخرف"""
        styles = [
            ("╔", "═", "╗", "║", "╚", "═", "╝"),
            ("┌", "─", "┐", "│", "└", "─", "┘"),
            ("╭", "─", "╮", "│", "╰", "─", "╯"),
            ("▛", "▀", "▜", "▌", "▙", "▄", "▟"),
        ]
        s = styles[min(style, len(styles)-1)]
        tl, tm, tr, mid, bl, bm, br = s
        width = 60
        top    = f"{tl}{tm * (width-2)}{tr}"
        ttitle = f"{mid}  {title.center(width-4)}  {mid}"
        sep    = f"{mid}{tm * (width-2)}{mid}"
        body   = []
        for line in content.split("\n"):
            chunks = textwrap.wrap(line, width - 4) or [""]
            for chunk in chunks:
                body.append(f"{mid}  {chunk:<{width-4}}  {mid}")
        bottom = f"{bl}{bm * (width-2)}{br}"
        return "\n".join([top, ttitle, sep] + body + [bottom])

    @staticmethod
    def separator(char: str = "═", width: int = 40, label: str = "") -> str:
        if label:
            pad = (width - len(label) - 2) // 2
            return f"{'━' * pad} {label} {'━' * (width - pad - len(label) - 2)}"
        return char * width

    @staticmethod
    def header(text: str) -> str:
        line = "━" * 38
        return f"<b>{line}\n✦ {text}\n{line}</b>"

    @staticmethod
    def section(emoji: str, title: str) -> str:
        return f"\n{emoji} <b>{'─'*3} {title} {'─'*3}</b>"

    @staticmethod
    def field(label: str, value: Any, emoji: str = "▪️") -> str:
        return f"  {emoji} <b>{label}:</b> <code>{value}</code>"

    @staticmethod
    def progress_bar(value: float, total: float, width: int = 20, label: str = "") -> str:
        if total <= 0: pct = 0
        else: pct = min(1.0, value / total)
        filled = int(pct * width)
        empty  = width - filled
        if pct < 0.5:   color = "🟩"
        elif pct < 0.75: color = "🟨"
        else:            color = "🟥"
        bar = "█" * filled + "░" * empty
        pct_str = f"{pct*100:.1f}%"
        if label:
            return f"{label}: [{bar}] {pct_str}"
        return f"[{bar}] {pct_str}"

    @staticmethod
    def bullet_list(items: List[str], icon: str = "•") -> str:
        return "\n".join(f"  {icon} {item}" for item in items)

    @staticmethod
    def numbered_list(items: List[str]) -> str:
        return "\n".join(f"  {i+1}. {item}" for i, item in enumerate(items))

    @staticmethod
    def table(headers: List[str], rows: List[List[str]]) -> str:
        if not rows: return "لا توجد بيانات"
        widths = [max(len(str(h)), max((len(str(r[i])) for r in rows if i < len(r)), default=0))
                  for i, h in enumerate(headers)]
        sep   = "┼".join("─" * (w + 2) for w in widths)
        sep   = f"├{sep}┤"
        top   = "┬".join("─" * (w + 2) for w in widths)
        top   = f"┌{top}┐"
        bot   = "┴".join("─" * (w + 2) for w in widths)
        bot   = f"└{bot}┘"
        head  = "│".join(f" {str(h).center(w)} " for h, w in zip(headers, widths))
        head  = f"│{head}│"
        lines = [f"<code>{top}", head, sep]
        for row in rows:
            r = "│".join(f" {str(row[i] if i < len(row) else '').ljust(w)} " for i, w in enumerate(widths))
            lines.append(f"│{r}│")
        lines.append(f"{bot}</code>")
        return "\n".join(lines)

    @staticmethod
    def status_badge(status: str) -> str:
        badges = {
            "running":  "🟢 يعمل",
            "stopped":  "🔴 متوقف",
            "pending":  "🟡 انتظار",
            "approved": "✅ مقبول",
            "rejected": "❌ مرفوض",
            "error":    "💥 خطأ",
            "premium":  "💫 بريميوم",
            "banned":   "🚫 محظور",
            "admin":    "🛡️ مشرف",
        }
        return badges.get(status.lower(), f"⚪ {status}")

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🗄️ نماذج البيانات                             ║
# ╚══════════════════════════════════════════════════════════════════╝

class FileStatus(str, Enum):
    PENDING  = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    RUNNING  = "running"
    STOPPED  = "stopped"
    ERROR    = "error"

class UserRole(str, Enum):
    OWNER   = "owner"
    ADMIN   = "admin"
    PREMIUM = "premium"
    USER    = "user"
    BANNED  = "banned"

class AdminPermission(str, Enum):
    APPROVE_FILES  = "approve_files"
    MANAGE_USERS   = "manage_users"
    BROADCAST      = "broadcast"
    VIEW_STATS     = "view_stats"
    MANAGE_PREMIUM = "manage_premium"
    VIEW_LOGS      = "view_logs"
    MANAGE_ADMINS  = "manage_admins"
    KILL_PROCESSES = "kill_processes"
    BACKUP         = "backup"
    FULL_ACCESS    = "full_access"

@dataclass
class HostedFile:
    file_id:        str       = field(default_factory=lambda: str(uuid.uuid4())[:8].upper())
    user_id:        int       = 0
    original_name:  str       = ""
    stored_name:    str       = ""
    file_type:      str       = "python"  # python | zip | other
    size_bytes:     int       = 0
    status:         str       = FileStatus.PENDING.value
    uploaded_at:    str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    approved_at:    Optional[str] = None
    approved_by:    Optional[int] = None
    rejected_at:    Optional[str] = None
    rejected_by:    Optional[int] = None
    reject_reason:  str       = ""
    run_count:      int       = 0
    last_run:       Optional[str] = None
    tags:           List[str] = field(default_factory=list)
    description:    str       = ""
    ai_score:       float     = 0.0
    ai_risks:       List[str] = field(default_factory=list)
    ai_verdict:     str       = ""
    install_output: str       = ""
    process_pid:    Optional[int] = None
    schedule:       Optional[str] = None
    is_public:      bool      = False
    telegram_file_id: str     = ""

@dataclass
class UserRecord:
    user_id:        int       = 0
    username:       str       = ""
    first_name:     str       = ""
    last_name:      str       = ""
    role:           str       = UserRole.USER.value
    joined_at:      str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    last_active:    str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    is_banned:      bool      = False
    ban_reason:     str       = ""
    is_premium:     bool      = False
    premium_until:  Optional[str] = None
    premium_plan:   str       = ""
    points:         int       = 0
    invites:        int       = 0
    referred_by:    Optional[int] = None
    file_count:     int       = 0
    run_count:      int       = 0
    total_storage:  int       = 0
    promo_codes_used: List[str] = field(default_factory=list)
    notifications:  bool      = True
    language:       str       = "ar"
    admin_perms:    List[str] = field(default_factory=list)
    notes:          str       = ""
    achievements:   List[str] = field(default_factory=list)
    daily_runs:     int       = 0
    daily_date:     str       = ""
    login_streak:   int       = 0
    last_login_date: str      = ""
    warning_count:  int       = 0
    referral_code:  str       = field(default_factory=lambda: secrets.token_hex(4).upper())

@dataclass
class PromoCode:
    code:        str       = ""
    plan:        str       = "monthly"
    days:        int       = 30
    max_uses:    int       = 1
    used_count:  int       = 0
    used_by:     List[int] = field(default_factory=list)
    created_by:  int       = 0
    created_at:  str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    expires_at:  Optional[str] = None
    is_active:   bool      = True
    description: str       = ""

@dataclass
class BroadcastRecord:
    bcast_id:    str       = field(default_factory=lambda: str(uuid.uuid4())[:8].upper())
    admin_id:    int       = 0
    message:     str       = ""
    target:      str       = "all"
    sent_count:  int       = 0
    fail_count:  int       = 0
    created_at:  str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    finished_at: Optional[str] = None

@dataclass
class AuditEntry:
    entry_id:   str  = field(default_factory=lambda: str(uuid.uuid4())[:12])
    timestamp:  str  = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    actor_id:   int  = 0
    action:     str  = ""
    target:     str  = ""
    details:    str  = ""
    ip_hint:    str  = ""

@dataclass
class ScheduledTask:
    task_id:     str       = field(default_factory=lambda: str(uuid.uuid4())[:8].upper())
    user_id:     int       = 0
    file_id:     str       = ""
    run_at:      str       = ""
    repeat:      str       = "once"  # once | daily | hourly | weekly
    is_active:   bool      = True
    created_at:  str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    last_run:    Optional[str] = None
    run_count:   int       = 0

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🗄️ قاعدة البيانات الرئيسية                    ║
# ╚══════════════════════════════════════════════════════════════════╝

class Database:
    """قاعدة بيانات JSON متكاملة مع ذاكرة تخزين مؤقتة وتزامن"""

    def __init__(self, path: str):
        self.path = path
        self._lock = asyncio.Lock()
        self._data: Dict[str, Any] = {}
        self._dirty = False
        self._save_task: Optional[asyncio.Task] = None
        self._load()

    def _default_structure(self) -> Dict[str, Any]:
        return {
            "meta": {
                "version": BOT_VERSION,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "total_saves": 0,
            },
            "users":      {},
            "files":      {},
            "promo_codes": {},
            "broadcasts":  [],
            "audit_log":   [],
            "scheduled_tasks": {},
            "settings": {
                "maintenance_mode":      False,
                "registration_open":     True,
                "max_file_size_mb":      MAX_FILE_SIZE_MB,
                "max_processes_user":    MAX_PROCESSES_PER_USER,
                "max_processes_premium": MAX_PROCESSES_PREMIUM,
                "welcome_message":       "",
                "rules_message":         "",
                "require_approval":      True,
                "ai_analysis_enabled":   True,
                "auto_install_libs":     True,
                "rate_limit_enabled":    True,
                "global_stats": {
                    "total_uploads": 0,
                    "total_runs":    0,
                    "total_users":   0,
                    "start_time":    datetime.now(timezone.utc).isoformat(),
                },
            },
        }

    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self._data = json.load(f)
                # ترقية هيكل البيانات إذا لزم
                self._migrate()
                logger.info(f"✅ قاعدة البيانات محملة: {len(self._data.get('users', {}))} مستخدم")
            except Exception as e:
                logger.error(f"❌ خطأ في تحميل قاعدة البيانات: {e}")
                self._data = self._default_structure()
        else:
            self._data = self._default_structure()
            self._save_sync()
            logger.info("✅ قاعدة بيانات جديدة أنشئت")

    def _migrate(self):
        defaults = self._default_structure()
        for key, val in defaults.items():
            if key not in self._data:
                self._data[key] = val
        for key, val in defaults["settings"].items():
            if key not in self._data.get("settings", {}):
                self._data.setdefault("settings", {})[key] = val

    def _save_sync(self):
        try:
            tmp = self.path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self._data, f, ensure_ascii=False, indent=2, default=str)
            shutil.move(tmp, self.path)
            self._data.setdefault("meta", {})["total_saves"] = \
                self._data["meta"].get("total_saves", 0) + 1
            self._dirty = False
        except Exception as e:
            logger.error(f"❌ خطأ في حفظ قاعدة البيانات: {e}")

    async def save(self):
        async with self._lock:
            if self._dirty:
                await asyncio.get_event_loop().run_in_executor(None, self._save_sync)

    async def save_now(self):
        async with self._lock:
            await asyncio.get_event_loop().run_in_executor(None, self._save_sync)

    def mark_dirty(self):
        self._dirty = True

    # ─── المستخدمون ───────────────────────────────────────────────

    def get_user(self, user_id: int) -> Optional[UserRecord]:
        raw = self._data["users"].get(str(user_id))
        if not raw: return None
        try:
            return UserRecord(**{k: v for k, v in raw.items() if k in UserRecord.__dataclass_fields__})
        except Exception:
            return UserRecord(**raw) if raw else None

    def get_or_create_user(self, user_id: int, **kwargs) -> Tuple["UserRecord", bool]:
        existing = self.get_user(user_id)
        if existing:
            # تحديث الاسم إذا تغير
            changed = False
            for k, v in kwargs.items():
                if hasattr(existing, k) and getattr(existing, k) != v and v:
                    setattr(existing, k, v)
                    changed = True
            if changed:
                self.save_user(existing)
            return existing, False
        u = UserRecord(user_id=user_id, **kwargs)
        if user_id in ADMIN_IDS:
            u.role = UserRole.OWNER.value if user_id == ADMIN_IDS[0] else UserRole.ADMIN.value
            u.admin_perms = [AdminPermission.FULL_ACCESS.value]
        self.save_user(u)
        self._data["settings"]["global_stats"]["total_users"] += 1
        self.mark_dirty()
        return u, True

    def save_user(self, u: UserRecord):
        self._data["users"][str(u.user_id)] = asdict(u)
        self.mark_dirty()

    def all_users(self) -> List[UserRecord]:
        users = []
        for raw in self._data["users"].values():
            try:
                users.append(UserRecord(**{k: v for k, v in raw.items()
                                           if k in UserRecord.__dataclass_fields__}))
            except Exception:
                pass
        return users

    def search_users(self, query: str) -> List[UserRecord]:
        q = query.lower()
        return [u for u in self.all_users()
                if q in str(u.user_id) or q in (u.username or "").lower()
                or q in (u.first_name or "").lower()]

    # ─── الملفات ───────────────────────────────────────────────────

    def get_file(self, file_id: str) -> Optional[HostedFile]:
        raw = self._data["files"].get(file_id)
        if not raw: return None
        try:
            return HostedFile(**{k: v for k, v in raw.items() if k in HostedFile.__dataclass_fields__})
        except Exception:
            return None

    def save_file(self, hf: HostedFile):
        self._data["files"][hf.file_id] = asdict(hf)
        self.mark_dirty()

    def delete_file(self, file_id: str):
        self._data["files"].pop(file_id, None)
        self.mark_dirty()

    def user_files(self, user_id: int) -> List[HostedFile]:
        files = []
        for raw in self._data["files"].values():
            if raw.get("user_id") == user_id:
                try:
                    files.append(HostedFile(**{k: v for k, v in raw.items()
                                               if k in HostedFile.__dataclass_fields__}))
                except Exception:
                    pass
        return sorted(files, key=lambda f: f.uploaded_at, reverse=True)

    def pending_files(self) -> List[HostedFile]:
        files = []
        for raw in self._data["files"].values():
            if raw.get("status") == FileStatus.PENDING.value:
                try:
                    files.append(HostedFile(**{k: v for k, v in raw.items()
                                               if k in HostedFile.__dataclass_fields__}))
                except Exception:
                    pass
        return sorted(files, key=lambda f: f.uploaded_at)

    def all_files(self) -> List[HostedFile]:
        files = []
        for raw in self._data["files"].values():
            try:
                files.append(HostedFile(**{k: v for k, v in raw.items()
                                           if k in HostedFile.__dataclass_fields__}))
            except Exception:
                pass
        return sorted(files, key=lambda f: f.uploaded_at, reverse=True)

    # ─── أكواد الترقية ─────────────────────────────────────────────

    def get_promo(self, code: str) -> Optional[PromoCode]:
        raw = self._data["promo_codes"].get(code.upper())
        if not raw: return None
        try:
            return PromoCode(**{k: v for k, v in raw.items() if k in PromoCode.__dataclass_fields__})
        except Exception:
            return None

    def save_promo(self, p: PromoCode):
        self._data["promo_codes"][p.code.upper()] = asdict(p)
        self.mark_dirty()

    def delete_promo(self, code: str):
        self._data["promo_codes"].pop(code.upper(), None)
        self.mark_dirty()

    def all_promos(self) -> List[PromoCode]:
        promos = []
        for raw in self._data["promo_codes"].values():
            try:
                promos.append(PromoCode(**{k: v for k, v in raw.items()
                                          if k in PromoCode.__dataclass_fields__}))
            except Exception:
                pass
        return promos

    # ─── سجل التدقيق ──────────────────────────────────────────────

    def add_audit(self, actor_id: int, action: str, target: str = "", details: str = ""):
        entry = AuditEntry(actor_id=actor_id, action=action, target=target, details=details)
        self._data.setdefault("audit_log", []).append(asdict(entry))
        if len(self._data["audit_log"]) > 2000:
            self._data["audit_log"] = self._data["audit_log"][-1500:]
        self.mark_dirty()

    def recent_audit(self, n: int = 50) -> List[AuditEntry]:
        entries = []
        for raw in self._data.get("audit_log", [])[-n:]:
            try:
                entries.append(AuditEntry(**{k: v for k, v in raw.items()
                                            if k in AuditEntry.__dataclass_fields__}))
            except Exception:
                pass
        return list(reversed(entries))

    # ─── المهام المجدولة ──────────────────────────────────────────

    def get_task(self, task_id: str) -> Optional[ScheduledTask]:
        raw = self._data["scheduled_tasks"].get(task_id)
        if not raw: return None
        return ScheduledTask(**{k: v for k, v in raw.items() if k in ScheduledTask.__dataclass_fields__})

    def save_task(self, t: ScheduledTask):
        self._data["scheduled_tasks"][t.task_id] = asdict(t)
        self.mark_dirty()

    def user_tasks(self, user_id: int) -> List[ScheduledTask]:
        tasks = []
        for raw in self._data["scheduled_tasks"].values():
            if raw.get("user_id") == user_id:
                try:
                    tasks.append(ScheduledTask(**{k: v for k, v in raw.items()
                                                  if k in ScheduledTask.__dataclass_fields__}))
                except Exception:
                    pass
        return tasks

    # ─── الإعدادات ────────────────────────────────────────────────

    def get_setting(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        obj = self._data.get("settings", {})
        for k in keys:
            if not isinstance(obj, dict):
                return default
            obj = obj.get(k, default)
        return obj

    def set_setting(self, key: str, value: Any):
        keys = key.split(".")
        obj = self._data.setdefault("settings", {})
        for k in keys[:-1]:
            obj = obj.setdefault(k, {})
        obj[keys[-1]] = value
        self.mark_dirty()

    # ─── الإحصائيات ───────────────────────────────────────────────

    def global_stats(self) -> Dict[str, Any]:
        s = self._data.get("settings", {}).get("global_stats", {})
        users = self.all_users()
        files = self.all_files()
        return {
            "total_users":    len(users),
            "active_users":   sum(1 for u in users if not u.is_banned),
            "banned_users":   sum(1 for u in users if u.is_banned),
            "premium_users":  sum(1 for u in users if u.is_premium),
            "admin_count":    sum(1 for u in users if u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)),
            "total_files":    len(files),
            "pending_files":  sum(1 for f in files if f.status == FileStatus.PENDING.value),
            "approved_files": sum(1 for f in files if f.status == FileStatus.APPROVED.value),
            "running_files":  sum(1 for f in files if f.status == FileStatus.RUNNING.value),
            "total_uploads":  s.get("total_uploads", 0),
            "total_runs":     s.get("total_runs", 0),
            "start_time":     s.get("start_time", ""),
            "total_saves":    self._data.get("meta", {}).get("total_saves", 0),
        }

    def leaderboard(self, sort_by: str = "points", limit: int = 20) -> List[UserRecord]:
        users = [u for u in self.all_users() if not u.is_banned]
        key_map = {
            "points":    lambda u: u.points,
            "files":     lambda u: u.file_count,
            "runs":      lambda u: u.run_count,
            "invites":   lambda u: u.invites,
            "storage":   lambda u: u.total_storage,
        }
        key_fn = key_map.get(sort_by, key_map["points"])
        return sorted(users, key=key_fn, reverse=True)[:limit]

    # ─── النسخ الاحتياطي ──────────────────────────────────────────

    def create_backup(self) -> str:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(BACKUP_DIR, f"backup_{ts}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2, default=str)
        return path

    def restore_backup(self, path: str) -> bool:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._data = data
            self._save_sync()
            return True
        except Exception as e:
            logger.error(f"خطأ في استعادة النسخة الاحتياطية: {e}")
            return False

    def list_backups(self) -> List[str]:
        if not os.path.exists(BACKUP_DIR):
            return []
        files = [f for f in os.listdir(BACKUP_DIR) if f.startswith("backup_") and f.endswith(".json")]
        return sorted(files, reverse=True)


# ─── إنشاء مثيل عالمي ──────────────────────────────────────────────
db = Database(DATABASE_FILE)

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🧠 نظام تحليل الذكاء الاصطناعي                ║
# ╚══════════════════════════════════════════════════════════════════╝

class AIAnalyzer:
    """محلل ذكي للكود — يكتشف المخاطر ويقيّم الجودة"""

    RISK_PATTERNS = {
        "critical": [
            (r"os\.system\s*\(", "استدعاء نظام مباشر عبر os.system"),
            (r"subprocess\.(call|run|Popen|check_output)\s*\(.+shell\s*=\s*True", "تنفيذ shell مع shell=True"),
            (r"eval\s*\(", "استخدام eval() — خطر تنفيذ كود عشوائي"),
            (r"exec\s*\(", "استخدام exec() — خطر تنفيذ كود عشوائي"),
            (r"__import__\s*\(", "استيراد ديناميكي مشبوه"),
            (r"compile\s*\(.+exec", "تجميع وتنفيذ كود ديناميكي"),
            (r"globals\s*\(\)\s*\[", "تعديل المتغيرات العامة مباشرة"),
            (r"ctypes", "استخدام ctypes — وصول مباشر للذاكرة"),
            (r"socket\.bind|socket\.listen|socket\.accept", "فتح خادم شبكة"),
            (r"http\.server|socketserver|BaseHTTPServer", "تشغيل خادم HTTP"),
        ],
        "high": [
            (r"import\s+os\b", "استيراد مكتبة os — قد يصل للملفات"),
            (r"open\s*\(.+['\"]w", "فتح ملف للكتابة"),
            (r"shutil\.(rmtree|remove|move)", "حذف أو تحريك ملفات"),
            (r"requests\.(get|post|put|delete|patch)", "طلبات HTTP خارجية"),
            (r"urllib\.request|urllib\.urlopen", "طلبات URL مباشرة"),
            (r"ftplib|smtplib|imaplib|poplib", "بروتوكولات شبكة متقدمة"),
            (r"pickle\.(load|loads)", "تحميل pickle — خطر تنفيذ كود"),
            (r"marshal\.(load|loads)", "تحميل marshal غير آمن"),
            (r"threading\.Thread|multiprocessing", "إنشاء خيوط أو عمليات متعددة"),
        ],
        "medium": [
            (r"open\s*\(", "فتح ملف"),
            (r"os\.(getcwd|listdir|walk|scandir)", "استعراض الملفات"),
            (r"sys\.argv|sys\.path", "الوصول لمسارات النظام"),
            (r"getpass|keyring", "استخدام بيانات المصادقة"),
            (r"time\.sleep\s*\(\s*\d{3,}", "تأخير طويل جداً"),
            (r"while\s+True\s*:", "حلقة لانهائية"),
            (r"random\.(choice|randint|random)", "استخدام عشوائية — عادي"),
            (r"import\s+socket\b", "استيراد مكتبة socket"),
        ],
        "low": [
            (r"print\s*\(", "استخدام print"),
            (r"input\s*\(", "طلب إدخال من المستخدم"),
            (r"logging\.", "استخدام logging"),
            (r"datetime\.", "استخدام datetime"),
            (r"json\.(load|dump|loads|dumps)", "معالجة JSON"),
            (r"re\.(search|match|findall|sub)", "تعابير منتظمة"),
        ],
    }

    QUALITY_PATTERNS = {
        "good": [
            (r"def\s+\w+\s*\(", "دوال معرّفة بشكل صحيح"),
            (r'"""[\s\S]+?"""', "توثيق docstring"),
            (r"try\s*:.+except", "معالجة استثناءات"),
            (r"if\s+__name__\s*==\s*['\"]__main__['\"]", "نقطة دخول صحيحة"),
            (r"class\s+\w+", "تعريف فئات OOP"),
            (r"#.+", "تعليقات في الكود"),
            (r"logging\.", "استخدام logging احترافي"),
            (r"type\s*\(|isinstance\s*\(", "التحقق من الأنواع"),
        ],
        "warning": [
            (r"pass\b", "استخدام pass — قد يكون كوداً ناقصاً"),
            (r"TODO|FIXME|HACK|XXX", "ملاحظات TODO غير منجزة"),
            (r"except\s*:", "التقاط كل الاستثناءات بدون تحديد"),
            (r"global\s+\w+", "متغيرات عامة — تجنّب إن أمكن"),
        ],
    }

    KNOWN_LIBS = {
        "standard": {
            "os", "sys", "re", "json", "time", "datetime", "math", "random",
            "string", "io", "csv", "pathlib", "shutil", "copy", "enum",
            "typing", "dataclasses", "functools", "itertools", "collections",
            "logging", "traceback", "threading", "asyncio", "concurrent",
            "subprocess", "socket", "hashlib", "base64", "struct", "uuid",
            "urllib", "http", "email", "html", "xml", "zipfile", "tarfile",
            "configparser", "argparse", "textwrap", "unicodedata", "codecs",
        },
        "popular": {
            "requests", "aiohttp", "flask", "fastapi", "django", "tornado",
            "numpy", "pandas", "matplotlib", "scipy", "sklearn", "tensorflow",
            "torch", "PIL", "cv2", "bs4", "lxml", "selenium", "playwright",
            "sqlalchemy", "pymongo", "redis", "celery", "pydantic", "typer",
            "click", "rich", "colorama", "tqdm", "dotenv", "yaml", "toml",
            "telegram", "discord", "tweepy", "slack_sdk", "boto3", "google",
            "stripe", "twilio", "sendgrid", "cryptography", "jwt", "passlib",
        },
    }

    @classmethod
    def analyze(cls, code: str, filename: str = "") -> Dict[str, Any]:
        """تحليل شامل للكود"""
        result = {
            "score":        100.0,
            "risk_level":   "safe",
            "risks":        [],
            "warnings":     [],
            "info":         [],
            "quality":      [],
            "imports":      [],
            "unknown_libs": [],
            "line_count":   0,
            "function_count": 0,
            "class_count":  0,
            "complexity":   "simple",
            "verdict":      "✅ الكود آمن",
            "recommendation": "يمكن الموافقة على هذا الملف",
            "analysis_time": "",
        }

        start = time.time()
        lines = code.split("\n")
        result["line_count"] = len(lines)

        # ─── فحص المخاطر ───────────────────────────────────────────
        penalty = 0.0
        for level, patterns in cls.RISK_PATTERNS.items():
            for pattern, desc in patterns:
                try:
                    matches = re.findall(pattern, code, re.IGNORECASE | re.MULTILINE)
                    if matches:
                        entry = {
                            "level": level,
                            "desc":  desc,
                            "count": len(matches),
                            "lines": cls._find_pattern_lines(code, pattern),
                        }
                        if level == "critical":
                            result["risks"].append(entry)
                            penalty += 30.0
                        elif level == "high":
                            result["risks"].append(entry)
                            penalty += 10.0
                        elif level == "medium":
                            result["warnings"].append(entry)
                            penalty += 3.0
                        else:
                            result["info"].append(entry)
                            penalty += 0.5
                except re.error:
                    pass

        # ─── تقييم الجودة ─────────────────────────────────────────
        for level, patterns in cls.QUALITY_PATTERNS.items():
            for pattern, desc in patterns:
                try:
                    if re.search(pattern, code, re.IGNORECASE | re.MULTILINE | re.DOTALL):
                        result["quality"].append({"level": level, "desc": desc})
                        if level == "good":
                            penalty -= 2.0
                        else:
                            penalty += 1.0
                except re.error:
                    pass

        # ─── تحليل AST ────────────────────────────────────────────
        try:
            tree = ast.parse(code)
            fns   = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
            cls_  = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
            imps  = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]

            result["function_count"] = len(fns)
            result["class_count"]    = len(cls_)

            for imp in imps:
                if isinstance(imp, ast.Import):
                    for alias in imp.names:
                        result["imports"].append(alias.name.split(".")[0])
                elif isinstance(imp, ast.ImportFrom) and imp.module:
                    result["imports"].append(imp.module.split(".")[0])

            all_known = cls.KNOWN_LIBS["standard"] | cls.KNOWN_LIBS["popular"]
            result["unknown_libs"] = list({
                lib for lib in result["imports"]
                if lib and lib not in all_known
            })

            if len(fns) > 30 or result["line_count"] > 500:
                result["complexity"] = "complex"
            elif len(fns) > 10 or result["line_count"] > 150:
                result["complexity"] = "moderate"

        except SyntaxError as e:
            result["risks"].append({
                "level": "critical",
                "desc":  f"خطأ نحوي في الكود: {e}",
                "count": 1,
                "lines": [e.lineno],
            })
            penalty += 50.0
            result["complexity"] = "invalid"
        except Exception:
            pass

        # ─── الحكم النهائي ────────────────────────────────────────
        result["score"] = max(0.0, min(100.0, 100.0 - penalty))
        score = result["score"]
        critical_count = sum(1 for r in result["risks"] if r["level"] == "critical")
        high_count     = sum(1 for r in result["risks"] if r["level"] == "high")

        if critical_count > 0 or score < 30:
            result["risk_level"] = "critical"
            result["verdict"]    = "🔴 الكود خطير جداً"
            result["recommendation"] = "يُنصح برفض هذا الملف — يحتوي على كود خطير"
        elif high_count > 2 or score < 50:
            result["risk_level"] = "high"
            result["verdict"]    = "🟠 الكود عالي الخطورة"
            result["recommendation"] = "مراجعة دقيقة مطلوبة قبل الموافقة"
        elif score < 70:
            result["risk_level"] = "medium"
            result["verdict"]    = "🟡 الكود متوسط الخطورة"
            result["recommendation"] = "يمكن الموافقة مع الحذر"
        elif score < 90:
            result["risk_level"] = "low"
            result["verdict"]    = "🟢 الكود منخفض الخطورة"
            result["recommendation"] = "يمكن الموافقة عليه"
        else:
            result["risk_level"] = "safe"
            result["verdict"]    = "✅ الكود آمن تماماً"
            result["recommendation"] = "يمكن الموافقة بثقة"

        result["analysis_time"] = f"{(time.time() - start)*1000:.1f}ms"
        return result

    @staticmethod
    def _find_pattern_lines(code: str, pattern: str) -> List[int]:
        lines = []
        for i, line in enumerate(code.split("\n"), 1):
            try:
                if re.search(pattern, line, re.IGNORECASE):
                    lines.append(i)
            except re.error:
                pass
        return lines[:5]

    @classmethod
    def format_report(cls, result: Dict[str, Any], filename: str = "") -> str:
        """تنسيق تقرير التحليل بشكل جميل"""
        lines = []
        lines.append(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append(f"{I.AI} <b>تقرير تحليل الذكاء الاصطناعي</b>")
        if filename:
            lines.append(f"{I.FILE} <code>{html.escape(filename)}</code>")
        lines.append(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # النتيجة
        score = result["score"]
        bar   = Art.progress_bar(score, 100, 20)
        lines.append(f"\n{I.SCORE} <b>النتيجة:</b> <code>{score:.1f}/100</code>")
        lines.append(f"<code>{bar}</code>")
        lines.append(f"{I.SHIELD} <b>الحكم:</b> {result['verdict']}")
        lines.append(f"{I.LIGHT} <b>التوصية:</b> {result['recommendation']}")

        # إحصائيات
        lines.append(f"\n{I.STATS} <b>إحصائيات الكود:</b>")
        lines.append(f"  • الأسطر: <code>{result['line_count']}</code>  •  الدوال: <code>{result['function_count']}</code>  •  الفئات: <code>{result['class_count']}</code>")
        lines.append(f"  • التعقيد: <code>{result['complexity']}</code>  •  وقت التحليل: <code>{result['analysis_time']}</code>")

        # المكتبات الغير معروفة
        if result["unknown_libs"]:
            libs_str = ", ".join(f"<code>{l}</code>" for l in result["unknown_libs"][:8])
            lines.append(f"\n{I.WARN} <b>مكتبات غير معروفة ({len(result['unknown_libs'])}):</b> {libs_str}")

        # المخاطر
        if result["risks"]:
            lines.append(f"\n{I.RISK} <b>المخاطر ({len(result['risks'])}):</b>")
            for r in result["risks"][:5]:
                lvl_icon = "🔴" if r["level"] == "critical" else "🟠"
                ln_str = ", ".join(f"L{l}" for l in r.get("lines", [])[:3])
                lines.append(f"  {lvl_icon} {r['desc']}"
                             + (f" — <code>{ln_str}</code>" if ln_str else ""))

        # التحذيرات
        if result["warnings"]:
            lines.append(f"\n{I.WARN} <b>تحذيرات ({len(result['warnings'])}):</b>")
            for w in result["warnings"][:3]:
                lines.append(f"  🟡 {w['desc']}")

        # نقاط الجودة
        good_q = [q for q in result["quality"] if q["level"] == "good"]
        if good_q:
            lines.append(f"\n{I.QUALITY} <b>نقاط الجودة:</b>")
            for q in good_q[:3]:
                lines.append(f"  ✅ {q['desc']}")

        lines.append(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return "\n".join(lines)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ⚡ مدير العمليات                              ║
# ╚══════════════════════════════════════════════════════════════════╝

@dataclass
class RunningProcess:
    pid:         int       = 0
    file_id:     str       = ""
    user_id:     int       = 0
    file_name:   str       = ""
    started_at:  str       = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    process:     Any       = field(default=None, repr=False, compare=False)
    output_buf:  deque     = field(default_factory=lambda: deque(maxlen=500), repr=False, compare=False)
    error_buf:   deque     = field(default_factory=lambda: deque(maxlen=200), repr=False, compare=False)
    is_stopping: bool      = False

class ProcessManager:
    """إدارة عمليات Python قيد التشغيل"""

    def __init__(self):
        self._processes: Dict[str, RunningProcess] = {}  # file_id -> RunningProcess
        self._lock = threading.Lock()
        self._executor = ThreadPoolExecutor(max_workers=20, thread_name_prefix="proc")

    def count_user(self, user_id: int) -> int:
        with self._lock:
            return sum(1 for rp in self._processes.values()
                      if rp.user_id == user_id and rp.process and rp.process.poll() is None)

    def get_all_running(self) -> List[RunningProcess]:
        with self._lock:
            return [rp for rp in self._processes.values()
                   if rp.process and rp.process.poll() is None]

    def get_process(self, file_id: str) -> Optional[RunningProcess]:
        with self._lock:
            return self._processes.get(file_id)

    def is_running(self, file_id: str) -> bool:
        rp = self.get_process(file_id)
        return rp is not None and rp.process is not None and rp.process.poll() is None

    def get_output(self, file_id: str, last_n: int = 50) -> Tuple[str, str]:
        with self._lock:
            rp = self._processes.get(file_id)
            if not rp:
                return "", ""
            out = "\n".join(list(rp.output_buf)[-last_n:])
            err = "\n".join(list(rp.error_buf)[-last_n:])
            return out, err

    async def start_process(
        self,
        file_path: str,
        file_id: str,
        user_id: int,
        file_name: str,
        work_dir: str,
    ) -> Tuple[bool, str]:
        """تشغيل ملف Python"""
        if self.is_running(file_id):
            return False, "العملية تعمل بالفعل"

        try:
            env = os.environ.copy()
            env["PYTHONUNBUFFERED"] = "1"
            env["PYTHONIOENCODING"] = "utf-8"

            proc = subprocess.Popen(
                [sys.executable, "-u", file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=work_dir,
                env=env,
                text=True,
                encoding="utf-8",
                errors="replace",
            )

            rp = RunningProcess(
                pid=proc.pid,
                file_id=file_id,
                user_id=user_id,
                file_name=file_name,
                process=proc,
            )

            with self._lock:
                self._processes[file_id] = rp

            # قراءة المخرجات في خيوط منفصلة
            self._executor.submit(self._read_stream, rp, proc.stdout, rp.output_buf)
            self._executor.submit(self._read_stream, rp, proc.stderr, rp.error_buf)

            logger.info(f"▶️ بدأ تشغيل {file_name} (PID:{proc.pid}) للمستخدم {user_id}")
            return True, f"PID: {proc.pid}"

        except Exception as e:
            logger.error(f"خطأ في تشغيل {file_name}: {e}")
            return False, str(e)

    def _read_stream(self, rp: RunningProcess, stream, buf: deque):
        try:
            for line in iter(stream.readline, ""):
                buf.append(line.rstrip())
        except Exception:
            pass
        finally:
            with suppress(Exception):
                stream.close()

    def stop_process(self, file_id: str) -> Tuple[bool, str]:
        with self._lock:
            rp = self._processes.get(file_id)
        if not rp or not rp.process:
            return False, "العملية غير موجودة"
        if rp.process.poll() is not None:
            return False, "العملية متوقفة بالفعل"

        rp.is_stopping = True
        try:
            rp.process.terminate()
            try:
                rp.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                rp.process.kill()
                rp.process.wait(timeout=3)
            logger.info(f"⏹️ أُوقفت عملية {rp.file_name} (PID:{rp.pid})")
            return True, f"تم الإيقاف (PID:{rp.pid})"
        except Exception as e:
            return False, str(e)

    def stop_all_user(self, user_id: int) -> int:
        count = 0
        with self._lock:
            fids = [fid for fid, rp in self._processes.items() if rp.user_id == user_id]
        for fid in fids:
            ok, _ = self.stop_process(fid)
            if ok: count += 1
        return count

    def stop_all(self) -> int:
        count = 0
        with self._lock:
            fids = list(self._processes.keys())
        for fid in fids:
            ok, _ = self.stop_process(fid)
            if ok: count += 1
        return count

    def process_stats(self, file_id: str) -> Dict[str, Any]:
        rp = self.get_process(file_id)
        if not rp or not rp.process:
            return {}
        stats = {"pid": rp.pid, "status": "unknown", "cpu": 0.0, "mem": 0}
        try:
            p = psutil.Process(rp.pid)
            stats["status"] = p.status()
            stats["cpu"]    = p.cpu_percent(interval=0.1)
            stats["mem"]    = p.memory_info().rss
        except Exception:
            stats["status"] = "stopped" if rp.process.poll() is not None else "running"
        started = datetime.fromisoformat(rp.started_at.replace("Z", "+00:00"))
        stats["uptime"] = str(datetime.now(timezone.utc) - started).split(".")[0]
        return stats


proc_mgr = ProcessManager()

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📦 مدير الملفات                              ║
# ╚══════════════════════════════════════════════════════════════════╝

class FileManager:
    """إدارة تخزين وتثبيت ملفات المستخدمين"""

    @staticmethod
    def user_dir(user_id: int) -> str:
        d = os.path.join(FILES_DIR, str(user_id))
        os.makedirs(d, exist_ok=True)
        return d

    @staticmethod
    def pending_dir(user_id: int) -> str:
        d = os.path.join(PENDING_DIR, str(user_id))
        os.makedirs(d, exist_ok=True)
        return d

    @staticmethod
    def file_path(user_id: int, stored_name: str, pending: bool = False) -> str:
        base = FileManager.pending_dir(user_id) if pending else FileManager.user_dir(user_id)
        return os.path.join(base, stored_name)

    @staticmethod
    def human_size(size_bytes: int) -> str:
        if HAS_HUMANIZE:
            return humanize.naturalsize(size_bytes)
        for unit in ("B", "KB", "MB", "GB"):
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"

    @staticmethod
    def disk_usage() -> Dict[str, Any]:
        total, used, free = 0, 0, 0
        for d in (FILES_DIR, PENDING_DIR, LOGS_DIR, BACKUP_DIR):
            if os.path.exists(d):
                for root, dirs, files in os.walk(d):
                    for fname in files:
                        fsize = 0
                        with suppress(OSError):
                            fsize = os.path.getsize(os.path.join(root, fname))
                        used += fsize
        return {"used": used, "human": FileManager.human_size(used)}

    @staticmethod
    async def install_requirements(
        work_dir: str,
        req_file: Optional[str] = None,
        extra_libs: Optional[List[str]] = None,
    ) -> Tuple[bool, str]:
        """تثبيت متطلبات Python"""
        cmds = []

        if req_file and os.path.exists(req_file):
            cmds.append([sys.executable, "-m", "pip", "install", "-r", req_file,
                         "--quiet", "--disable-pip-version-check", "--no-warn-script-location"])
        if extra_libs:
            cmds.append([sys.executable, "-m", "pip", "install"] + extra_libs +
                        ["--quiet", "--disable-pip-version-check", "--no-warn-script-location"])

        if not cmds:
            return True, "لا توجد متطلبات لتثبيتها"

        all_output = []
        for cmd in cmds:
            try:
                proc = await asyncio.create_subprocess_exec(
                    *cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.STDOUT,
                    cwd=work_dir,
                )
                stdout, _ = await asyncio.wait_for(
                    proc.communicate(), timeout=INSTALL_TIMEOUT_SECONDS
                )
                out = stdout.decode("utf-8", errors="replace") if stdout else ""
                all_output.append(out)
                if proc.returncode != 0:
                    return False, "\n".join(all_output)
            except asyncio.TimeoutError:
                return False, "انتهت مهلة التثبيت"
            except Exception as e:
                return False, str(e)

        return True, "\n".join(all_output)

    @staticmethod
    def extract_imports_from_code(code: str) -> List[str]:
        """استخراج المكتبات غير القياسية من الكود"""
        stdlib = AIAnalyzer.KNOWN_LIBS["standard"]
        imports = set()
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        lib = alias.name.split(".")[0]
                        if lib not in stdlib:
                            imports.add(lib)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    lib = node.module.split(".")[0]
                    if lib not in stdlib:
                        imports.add(lib)
        except Exception:
            pass
        return list(imports)

    @staticmethod
    async def prepare_zip_file(
        zip_path: str,
        file_id: str,
        user_id: int,
    ) -> Tuple[bool, str, Optional[str]]:
        """استخراج ملف ZIP وإيجاد الملف الرئيسي"""
        extract_dir = os.path.join(FileManager.user_dir(user_id), f"{file_id}_extracted")
        os.makedirs(extract_dir, exist_ok=True)
        try:
            with zipfile.ZipFile(zip_path, "r") as zf:
                zf.extractall(extract_dir)
        except Exception as e:
            return False, f"خطأ في فك الضغط: {e}", None

        # البحث عن الملف الرئيسي
        candidates = ["main.py", "app.py", "run.py", "bot.py", "start.py", "index.py"]
        main_file = None
        for c in candidates:
            p = os.path.join(extract_dir, c)
            if os.path.exists(p):
                main_file = p
                break
        if not main_file:
            py_files = list(Path(extract_dir).rglob("*.py"))
            if py_files:
                main_file = str(py_files[0])

        if not main_file:
            return False, "لم يُعثر على ملف Python رئيسي في الـ ZIP", None

        return True, f"تم استخراج ZIP — الملف الرئيسي: {os.path.basename(main_file)}", main_file

    @staticmethod
    def create_export_zip(include_db: bool = False) -> str:
        """إنشاء ملف ZIP للتصدير"""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_path = os.path.join(EXPORT_DIR, f"export_{ts}.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            # الملف الرئيسي
            bot_file = os.path.abspath(__file__)
            zf.write(bot_file, "bot.py")
            # requirements.txt
            req_path = os.path.join(os.path.dirname(bot_file), "requirements.txt")
            if os.path.exists(req_path):
                zf.write(req_path, "requirements.txt")
            else:
                zf.writestr("requirements.txt", REQUIREMENTS_CONTENT)
            # ملف .env.example
            zf.writestr(".env.example", ENV_EXAMPLE_CONTENT)
            # ملف README
            zf.writestr("README.md", README_CONTENT)
            # قاعدة البيانات
            if include_db and os.path.exists(DATABASE_FILE):
                zf.write(DATABASE_FILE, "bot_database.json")
        return zip_path


REQUIREMENTS_CONTENT = """# PyHost PRO ULTRA — متطلبات
python-telegram-bot==21.5
psutil==5.9.8
aiohttp==3.10.5
aiofiles==23.2.1
humanize==4.10.0
tabulate==0.9.0
colorlog==6.8.2
APScheduler==3.10.4
cryptography==43.0.1
Pillow==10.4.0
"""

ENV_EXAMPLE_CONTENT = """# ملف الإعدادات — انسخ هذا إلى .env وعدّل القيم
BOT_TOKEN=ضع_توكن_البوت_هنا
ADMIN_IDS=123456789,987654321
DATABASE_FILE=bot_database.json
FILES_DIR=hosted_files
LOGS_DIR=bot_logs
BACKUP_DIR=backups
TEMP_DIR=temp_work
PENDING_DIR=pending_files
MAX_FILE_SIZE_MB=50
MAX_PROCESSES_PER_USER=3
RUN_TIMEOUT_SECONDS=0
RATE_LIMIT_MESSAGES=15
RATE_LIMIT_WINDOW=10
AUTO_BACKUP_INTERVAL_HOURS=6
SUPPORT_USERNAME=support
"""

README_CONTENT = """# 🔥 PyHost PRO ULTRA v10.0 — MEGA EDITION

## 🚀 التشغيل

```bash
# تثبيت المتطلبات
pip install -r requirements.txt

# إعداد التوكن
export BOT_TOKEN="توكن_البوت_هنا"
export ADMIN_IDS="123456789"

# تشغيل البوت
python bot.py
```

## ⚙️ الإعدادات (متغيرات البيئة)

انسخ `.env.example` إلى `.env` وعدّل القيم.

## 🌐 الاستضافة

- **VPS/سيرفر عادي**: `python bot.py` أو `nohup python bot.py &`
- **Railway**: أضف `BOT_TOKEN` و`ADMIN_IDS` في Environment Variables
- **Render**: نفس Railway
- **Replit**: أضف المتغيرات في Secrets

## ✨ الميزات الرئيسية

- نظام موافقة يدوية على كل ملف قبل تشغيله
- لوحة إدارة شاملة بالأزرار
- تحليل ذكاء اصطناعي للكود
- نظام بريميوم وأكواد ترقية
- لوحة متصدرين ونقاط
- بث متقدم للمستخدمين
- نسخ احتياطي تلقائي
- مراقبة الموارد
"""

file_mgr = FileManager()

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🛡️ نظام الحماية والصلاحيات                   ║
# ╚══════════════════════════════════════════════════════════════════╝

# Rate Limiter
class RateLimiter:
    def __init__(self):
        self._windows: Dict[int, deque] = defaultdict(lambda: deque())
        self._blocked: Dict[int, float] = {}

    def check(self, user_id: int) -> Tuple[bool, float]:
        now = time.time()
        # هل محجوب مؤقتاً؟
        if user_id in self._blocked:
            remaining = self._blocked[user_id] - now
            if remaining > 0:
                return False, remaining
            del self._blocked[user_id]

        window = self._windows[user_id]
        cutoff = now - RATE_LIMIT_WINDOW
        while window and window[0] < cutoff:
            window.popleft()
        window.append(now)

        if len(window) > RATE_LIMIT_MESSAGES:
            self._blocked[user_id] = now + 30  # حجب 30 ثانية
            return False, 30.0
        return True, 0.0


rate_limiter = RateLimiter()


def _has_perm(u: UserRecord, perm: AdminPermission) -> bool:
    if u.role == UserRole.OWNER.value:
        return True
    if AdminPermission.FULL_ACCESS.value in u.admin_perms:
        return True
    return perm.value in u.admin_perms


def require_admin(perm: AdminPermission = AdminPermission.FULL_ACCESS):
    """ديكوراتور للتحقق من صلاحيات الأدمن"""
    def decorator(fn):
        @wraps(fn)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
            if not update.effective_user:
                return
            uid = update.effective_user.id
            u, _ = db.get_or_create_user(uid)
            if u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
                await _answer_cb_or_msg(update, f"{I.BAN} ليس لديك صلاحية للوصول لهذه الميزة.")
                return
            if not _has_perm(u, perm):
                await _answer_cb_or_msg(update, f"{I.LOCK} لا تملك صلاحية: <code>{perm.value}</code>")
                return
            return await fn(update, context, *args, **kwargs)
        return wrapper
    return decorator


def require_not_banned(fn):
    @wraps(fn)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        if not update.effective_user:
            return
        uid = update.effective_user.id
        u = db.get_user(uid)
        if u and u.is_banned:
            reason = f" — {u.ban_reason}" if u.ban_reason else ""
            await _answer_cb_or_msg(update, f"{I.BAN} أنت محظور من استخدام البوت{reason}.")
            return
        return await fn(update, context, *args, **kwargs)
    return wrapper


def rate_limited(fn):
    @wraps(fn)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        if not update.effective_user:
            return fn(update, context, *args, **kwargs)
        uid = update.effective_user.id
        u = db.get_user(uid)
        if u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value):
            return await fn(update, context, *args, **kwargs)
        if not db.get_setting("rate_limit_enabled", True):
            return await fn(update, context, *args, **kwargs)
        ok, wait = rate_limiter.check(uid)
        if not ok:
            await _answer_cb_or_msg(update,
                f"{I.WARN} أنت ترسل رسائل بسرعة كبيرة.\n"
                f"{I.TIMER} انتظر <code>{wait:.0f}</code> ثانية.")
            return
        return await fn(update, context, *args, **kwargs)
    return wrapper

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🔘 مولّد لوحات المفاتيح                       ║
# ╚══════════════════════════════════════════════════════════════════╝

def _kb(rows: List[List[Tuple[str, str]]]) -> InlineKeyboardMarkup:
    """
    صنع InlineKeyboard من قائمة صفوف.
    كل عنصر هو (نص_الزر, callback_data)
    إذا callback_data يبدأ بـ 'http' يصبح زر رابط.
    """
    keyboard = []
    for row in rows:
        kb_row = []
        for label, data in row:
            if data.startswith("http://") or data.startswith("https://"):
                kb_row.append(InlineKeyboardButton(label, url=data))
            else:
                kb_row.append(InlineKeyboardButton(label, callback_data=data))
        keyboard.append(kb_row)
    return InlineKeyboardMarkup(keyboard)


async def _answer_cb_or_msg(
    update: Update,
    text: str,
    kb: Optional[InlineKeyboardMarkup] = None,
    parse_mode: str = ParseMode.HTML,
    edit: bool = False,
):
    """إرسال رد سواء كان callback أو رسالة عادية"""
    if update.callback_query:
        await update.callback_query.answer()
        if edit:
            with suppress(BadRequest):
                await update.callback_query.edit_message_text(
                    text, reply_markup=kb, parse_mode=parse_mode
                )
            return
        await update.callback_query.message.reply_text(
            text, reply_markup=kb, parse_mode=parse_mode
        )
    elif update.message:
        await update.message.reply_text(text, reply_markup=kb, parse_mode=parse_mode)


async def safe_send(bot, chat_id: int, text: str, **kwargs) -> Optional[Message]:
    try:
        return await bot.send_message(chat_id, text, **kwargs)
    except Forbidden:
        logger.debug(f"المستخدم {chat_id} حجب البوت")
    except BadRequest as e:
        logger.warning(f"BadRequest لـ {chat_id}: {e}")
    except Exception as e:
        logger.error(f"خطأ إرسال لـ {chat_id}: {e}")
    return None


async def safe_edit(msg: Message, text: str, **kwargs) -> bool:
    with suppress(BadRequest, TelegramError):
        await msg.edit_text(text, **kwargs)
        return True
    return False

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🏠 لوحات القوائم الرئيسية                     ║
# ╚══════════════════════════════════════════════════════════════════╝

def _user_display(u: UserRecord) -> str:
    name = u.first_name or u.username or str(u.user_id)
    badges = []
    if u.role == UserRole.OWNER.value: badges.append(f"{I.CROWN}مالك")
    elif u.role == UserRole.ADMIN.value: badges.append(f"{I.ADMIN}مشرف")
    if u.is_premium: badges.append(f"{I.PREM}بريميوم")
    if u.is_banned: badges.append(f"{I.BAN}محظور")
    badge_str = " ".join(badges)
    return f"{name} {badge_str}".strip()


def build_main_menu(user: UserRecord) -> Tuple[str, InlineKeyboardMarkup]:
    """القائمة الرئيسية للمستخدم"""
    is_admin = user.role in (UserRole.ADMIN.value, UserRole.OWNER.value)
    maintenance = db.get_setting("maintenance_mode", False)

    name = user.first_name or user.username or "مستخدم"
    role_icon = {
        UserRole.OWNER.value:   f"{I.CROWN} مالك",
        UserRole.ADMIN.value:   f"{I.ADMIN} مشرف",
        UserRole.PREMIUM.value: f"{I.PREM} بريميوم",
        UserRole.USER.value:    f"{I.USER} عضو",
    }.get(user.role, f"{I.USER} عضو")

    status_line = ""
    if maintenance and not is_admin:
        status_line = f"\n\n{I.WARN} <b>البوت في وضع الصيانة مؤقتاً</b>"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FIRE} <b>مرحباً بك في {BOT_NAME}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{I.USER} <b>الاسم:</b> {html.escape(name)}\n"
        f"{I.TAG}  <b>الدور:</b> {role_icon}\n"
        f"{I.POINTS} <b>النقاط:</b> <code>{user.points:,}</code>\n"
        f"{I.FILE} <b>ملفاتي:</b> <code>{user.file_count}</code> ملف\n"
        f"{I.RUN} <b>تشغيلاتي:</b> <code>{user.run_count:,}</code>\n"
        f"{status_line}"
        f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.LIGHT} <b>اختر من القائمة:</b>"
    )

    rows = [
        [(f"{I.UPLOAD} رفع ملف جديد",    "cmd_upload"),
         (f"{I.FOLDER} ملفاتي",           "my_files_0")],
        [(f"{I.RUN} عملياتي النشطة",      "my_procs"),
         (f"{I.SCHED} جدولة تشغيل",       "my_schedule")],
        [(f"{I.TROPHY} المتصدرون",         "leaderboard_0"),
         (f"{I.PREM} بريميوم",            "premium_info")],
        [(f"{I.STATS} إحصائياتي",         "my_stats"),
         (f"{I.SETTINGS} إعداداتي",       "my_settings")],
        [(f"{I.GIFT} أكواد الترقية",      "redeem_code"),
         (f"{I.LINK} رابط الإحالة",       "my_referral")],
        [(f"{I.MSG} الدعم الفني",         "contact_support"),
         (f"{I.INFO} عن البوت",           "about_bot")],
    ]

    if is_admin:
        rows.append([(f"{I.SHIELD} ━━ لوحة الإدارة ━━", "admin_main")])

    return text, _kb(rows)


def build_admin_main(user: UserRecord) -> Tuple[str, InlineKeyboardMarkup]:
    """لوحة الإدارة الرئيسية"""
    stats = db.global_stats()
    running = len(proc_mgr.get_all_running())
    pending = len(db.pending_files())

    alerts = []
    if pending > 0: alerts.append(f"{I.BELL} {pending} ملف ينتظر الموافقة")
    if running > 0: alerts.append(f"{I.GREEN} {running} عملية نشطة")
    alerts_str = "\n".join(alerts) if alerts else f"{I.OK} لا توجد تنبيهات"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.SHIELD} <b>لوحة الإدارة — {BOT_NAME}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{I.STATS} <b>إحصائيات سريعة:</b>\n"
        f"  {I.USERS} المستخدمون: <code>{stats['total_users']}</code>  "
        f"  {I.PREM} بريميوم: <code>{stats['premium_users']}</code>\n"
        f"  {I.FILE} الملفات: <code>{stats['total_files']}</code>  "
        f"  {I.RUN} التشغيلات: <code>{stats['total_runs']}</code>\n"
        f"  {I.QUEUE} انتظار: <code>{stats['pending_files']}</code>  "
        f"  {I.GREEN} نشطة: <code>{running}</code>\n\n"
        f"{I.BELL} <b>التنبيهات:</b>\n{alerts_str}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<b>اختر القسم:</b>"
    )

    rows = [
        [(f"{I.QUEUE} ━ الملفات المعلقة ({pending}) ━", "pending_list_0")],
        [(f"{I.USERS} إدارة المستخدمين",   "admin_users_0"),
         (f"{I.ADMIN} إدارة الأدمنز",       "admin_admins")],
        [(f"{I.FILE} إدارة الملفات",        "admin_files_0"),
         (f"{I.RUN} العمليات النشطة",        "admin_procs")],
        [(f"{I.PREM} إدارة البريميوم",       "admin_premium"),
         (f"{I.TAG} أكواد الترقية",          "admin_promos")],
        [(f"{I.BROAD} بث رسالة",             "admin_broadcast"),
         (f"{I.STATS} إحصائيات شاملة",       "admin_stats")],
        [(f"{I.SERVER} موارد النظام",         "admin_system"),
         (f"{I.LOG} سجل التدقيق",            "admin_audit_0")],
        [(f"{I.BACKUP} نسخ احتياطي",          "admin_backup"),
         (f"{I.SETTINGS} الإعدادات",          "admin_settings")],
        [(f"{I.EXPORT} تصدير البوت ZIP",       "admin_export_bot"),
         (f"{I.REFRESH} تحديث",               "admin_main")],
        [(f"{I.HOME} الرئيسية",               "start")],
    ]

    return text, _kb(rows)

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📱 معالجات الأوامر                            ║
# ╚══════════════════════════════════════════════════════════════════╝

@rate_limited
@require_not_banned
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    u, is_new = db.get_or_create_user(
        user.id,
        username=user.username or "",
        first_name=user.first_name or "",
        last_name=user.last_name or "",
    )

    # تحديث آخر نشاط
    u.last_active = datetime.now(timezone.utc).isoformat()
    # streak تسجيل الدخول
    today = datetime.now(timezone.utc).date().isoformat()
    if u.last_login_date != today:
        if u.last_login_date == (datetime.now(timezone.utc) - timedelta(days=1)).date().isoformat():
            u.login_streak += 1
            if u.login_streak % 7 == 0:
                u.points += 50  # مكافأة أسبوعية
        else:
            u.login_streak = 1
        u.last_login_date = today
        u.points += 2  # نقطتان لكل تسجيل دخول
    db.save_user(u)

    if is_new:
        # معالجة رمز الإحالة
        if context.args:
            ref_code = context.args[0]
            for ru in db.all_users():
                if ru.referral_code == ref_code and ru.user_id != user.id:
                    ru.invites += 1
                    ru.points  += 25
                    u.referred_by = ru.user_id
                    db.save_user(ru)
                    break
        db.save_user(u)
        # إشعار الأدمن بمستخدم جديد
        asyncio.create_task(_notify_admins_new_user(context, u))

    text, kb = build_main_menu(u)
    if update.callback_query:
        await update.callback_query.answer()
        with suppress(BadRequest):
            await update.callback_query.edit_message_text(text, reply_markup=kb, parse_mode=ParseMode.HTML)
    elif update.message:
        await update.message.reply_text(text, reply_markup=kb, parse_mode=ParseMode.HTML)


async def _notify_admins_new_user(context: ContextTypes.DEFAULT_TYPE, u: UserRecord):
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.BELL} <b>مستخدم جديد!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  {I.USER} الاسم: {html.escape(u.first_name or 'بدون اسم')}\n"
        f"  {I.TAG}  يوزر: @{html.escape(u.username or 'بدون')}\n"
        f"  {I.KEY}  ID: <code>{u.user_id}</code>\n"
        f"  {I.CAL}  التاريخ: <code>{datetime.now().strftime('%Y-%m-%d %H:%M')}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    kb = _kb([[(f"{I.USERS} عرض ملف المستخدم", f"view_user_{u.user_id}")]])
    for aid in ADMIN_IDS:
        await safe_send(context.bot, aid, text, parse_mode=ParseMode.HTML, reply_markup=kb)


@rate_limited
@require_not_banned
async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u, _ = db.get_or_create_user(update.effective_user.id)
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.LIGHT} <b>دليل استخدام {BOT_NAME}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{I.UPLOAD} <b>رفع الملفات:</b>\n"
        f"  أرسل أي ملف .py أو .zip مباشرةً\n"
        f"  ⤷ يتم التحليل الآلي أولاً\n"
        f"  ⤷ ينتظر موافقة المشرف\n"
        f"  ⤷ عند الموافقة يصبح جاهزاً للتشغيل\n\n"
        f"{I.PLAY} <b>التشغيل:</b>\n"
        f"  من {I.FOLDER} ملفاتي → اختر الملف → تشغيل\n\n"
        f"{I.PREM} <b>البريميوم:</b>\n"
        f"  • عمليات أكثر ({MAX_PROCESSES_PREMIUM} بدلاً من {MAX_PROCESSES_PER_USER})\n"
        f"  • أولوية في الموافقة\n"
        f"  • لا حدود للتخزين\n"
        f"  احصل عليه بـ {I.GIFT} كود ترقية أو من المشرف\n\n"
        f"{I.POINTS} <b>النقاط:</b>\n"
        f"  • +2 لكل تسجيل دخول يومي\n"
        f"  • +5 لكل رفع ملف\n"
        f"  • +3 لكل تشغيل ناجح\n"
        f"  • +25 لكل إحالة ناجحة\n\n"
        f"{I.LINK} <b>الإحالة:</b>\n"
        f"  اضغط «رابط الإحالة» لتحصل على رابطك الخاص\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.MSG} للدعم: تواصل مع @{SUPPORT_USERNAME}"
    )
    await _answer_cb_or_msg(update, text, _kb([[(f"{I.HOME} الرئيسية", "start")]]))


@rate_limited
async def cmd_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u, _ = db.get_or_create_user(uid)
    if u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await _answer_cb_or_msg(update, f"{I.LOCK} أنت لست مشرفاً.")
        return
    text, kb = build_admin_main(u)
    await _answer_cb_or_msg(update, text, kb, edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📤 معالج رفع الملفات                          ║
# ╚══════════════════════════════════════════════════════════════════╝

@rate_limited
@require_not_banned
async def handle_file_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """استقبال ومعالجة الملفات المرفوعة"""
    msg = update.message
    doc = msg.document if msg else None
    if not doc:
        return

    user = update.effective_user
    u, _ = db.get_or_create_user(user.id,
                                  username=user.username or "",
                                  first_name=user.first_name or "")

    # فحص وضع الصيانة
    if db.get_setting("maintenance_mode") and u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await msg.reply_text(f"{I.WARN} البوت في وضع الصيانة حالياً. حاول لاحقاً.")
        return

    # فحص نوع الملف
    fname  = doc.file_name or "unknown"
    ext    = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
    allowed_exts = {"py", "zip"}
    if ext not in allowed_exts:
        await msg.reply_text(
            f"{I.FAIL} نوع الملف غير مدعوم.\n"
            f"المدعوم: <code>.py</code> و <code>.zip</code>",
            parse_mode=ParseMode.HTML
        )
        return

    # فحص الحجم
    size_mb = doc.file_size / (1024 * 1024)
    max_mb  = MAX_FILE_SIZE_MB
    if size_mb > max_mb:
        await msg.reply_text(
            f"{I.FAIL} الملف كبير جداً ({size_mb:.1f} MB).\n"
            f"الحد المسموح: {max_mb} MB"
        )
        return

    # رسالة الانتظار
    wait_msg = await msg.reply_text(
        f"{I.UPLOAD} <b>جاري معالجة الملف...</b>\n"
        f"<code>{'▓' * 5}{'░' * 15}</code>",
        parse_mode=ParseMode.HTML
    )

    # تحميل الملف
    try:
        tg_file  = await doc.get_file()
        file_id  = str(uuid.uuid4())[:8].upper()
        safe_name = re.sub(r"[^\w.\-]", "_", fname)
        stored   = f"{file_id}_{safe_name}"
        pend_dir = FileManager.pending_dir(user.id)
        dest     = os.path.join(pend_dir, stored)

        await safe_edit(wait_msg,
            f"{I.DOWNLOAD} <b>جاري التحميل...</b>\n<code>{'▓' * 10}{'░' * 10}</code>",
            parse_mode=ParseMode.HTML)
        await tg_file.download_to_drive(dest)
    except Exception as e:
        await safe_edit(wait_msg, f"{I.FAIL} فشل تحميل الملف: <code>{html.escape(str(e))}</code>",
                        parse_mode=ParseMode.HTML)
        return

    # إنشاء سجل الملف
    hf = HostedFile(
        file_id=file_id,
        user_id=user.id,
        original_name=fname,
        stored_name=stored,
        file_type="zip" if ext == "zip" else "python",
        size_bytes=doc.file_size,
        status=FileStatus.PENDING.value,
        telegram_file_id=doc.file_id,
    )

    # ─── تحليل الذكاء الاصطناعي ───────────────────────────────────
    ai_result = {}
    if db.get_setting("ai_analysis_enabled", True) and ext == "py":
        await safe_edit(wait_msg,
            f"{I.AI} <b>جاري تحليل الكود بالذكاء الاصطناعي...</b>\n<code>{'▓' * 15}{'░' * 5}</code>",
            parse_mode=ParseMode.HTML)
        try:
            with open(dest, "r", encoding="utf-8", errors="replace") as f:
                code = f.read()
            ai_result = AIAnalyzer.analyze(code, fname)
            hf.ai_score   = ai_result["score"]
            hf.ai_risks   = [r["desc"] for r in ai_result["risks"][:5]]
            hf.ai_verdict = ai_result["verdict"]
        except Exception as e:
            logger.warning(f"AI analysis failed: {e}")

    db.save_file(hf)

    # تحديث إحصائيات المستخدم
    u.file_count += 1
    u.points     += 5
    u.total_storage += doc.file_size
    db.save_user(u)
    db.set_setting("global_stats.total_uploads",
                   db.get_setting("global_stats.total_uploads", 0) + 1)
    db.add_audit(user.id, "file_upload", f"file:{file_id}", fname)
    await db.save_now()

    # ─── رسالة تأكيد للمستخدم ─────────────────────────────────────
    ai_line = ""
    if ai_result:
        ai_line = (
            f"\n\n{I.AI} <b>تحليل الذكاء الاصطناعي:</b>\n"
            f"  النتيجة: <code>{ai_result['score']:.0f}/100</code>  |  {ai_result['verdict']}\n"
            f"  التوصية: {ai_result['recommendation']}"
        )

    user_text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.OK} <b>تم استقبال الملف بنجاح!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.FILE} <b>الاسم:</b> <code>{html.escape(fname)}</code>\n"
        f"  {I.KEY}  <b>المعرف:</b> <code>{file_id}</code>\n"
        f"  {I.DISK} <b>الحجم:</b> <code>{FileManager.human_size(doc.file_size)}</code>\n"
        f"  {I.TAG}  <b>النوع:</b> <code>{hf.file_type}</code>\n"
        f"  {I.CLOCK} <b>الحالة:</b> {Art.status_badge('pending')}"
        f"{ai_line}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.BELL} <b>ينتظر الملف موافقة المشرف.</b>\n"
        f"سيتم إشعارك فور البت في الطلب."
    )
    await safe_edit(wait_msg, user_text, parse_mode=ParseMode.HTML)

    # ─── إشعار الأدمنز بطلب الموافقة ─────────────────────────────
    asyncio.create_task(_notify_admins_pending(context, hf, u, ai_result))


async def _notify_admins_pending(
    context: ContextTypes.DEFAULT_TYPE,
    hf: HostedFile,
    u: UserRecord,
    ai_result: Dict[str, Any],
):
    """إرسال إشعار للأدمنز بملف ينتظر الموافقة"""
    risk_color = {
        "safe":     "🟢", "low": "🟢",
        "medium":   "🟡",
        "high":     "🟠", "critical": "🔴",
    }.get(ai_result.get("risk_level", "safe"), "⚪")

    ai_section = ""
    if ai_result:
        ai_section = (
            f"\n{I.AI} <b>تحليل الذكاء الاصطناعي:</b>\n"
            f"  النتيجة: <code>{ai_result.get('score', 0):.0f}/100</code>  "
            f"{risk_color} {ai_result.get('verdict', '')}\n"
            f"  التوصية: {ai_result.get('recommendation', '')}"
        )
        if ai_result.get("risks"):
            risks_str = "\n".join(f"    ⚠️ {r['desc']}" for r in ai_result["risks"][:3])
            ai_section += f"\n  <b>مخاطر:</b>\n{risks_str}"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.BELL} <b>طلب موافقة جديد!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{I.USER} <b>المستخدم:</b> {html.escape(u.first_name or 'بدون اسم')}\n"
        f"  @{html.escape(u.username or 'بدون')}  |  ID: <code>{u.user_id}</code>\n"
        f"  الدور: {Art.status_badge(u.role)}  |  النقاط: <code>{u.points}</code>\n\n"
        f"{I.FILE} <b>الملف:</b> <code>{html.escape(hf.original_name)}</code>\n"
        f"  المعرف: <code>{hf.file_id}</code>\n"
        f"  الحجم: <code>{FileManager.human_size(hf.size_bytes)}</code>\n"
        f"  النوع: <code>{hf.file_type}</code>"
        f"{ai_section}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.LIGHT} <b>هل توافق على تشغيل هذا الملف؟</b>"
    )

    kb = _kb([
        [(f"{I.OK} ✦ موافقة",              f"approve_file_{hf.file_id}"),
         (f"{I.FAIL} ✦ رفض",               f"reject_file_{hf.file_id}")],
        [(f"{I.AI} تقرير تفصيلي",          f"ai_report_{hf.file_id}"),
         (f"{I.USER} ملف المستخدم",        f"view_user_{u.user_id}")],
        [(f"{I.QUEUE} جميع المعلقة",        "pending_list_0")],
    ])

    for aid in ADMIN_IDS:
        await safe_send(context.bot, aid, text, parse_mode=ParseMode.HTML, reply_markup=kb)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🔘 معالج الـ Callbacks الرئيسي                 ║
# ╚══════════════════════════════════════════════════════════════════╝

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """موزّع مركزي لكل callback"""
    q   = update.callback_query
    uid = q.from_user.id
    data = q.data or ""

    u, _ = db.get_or_create_user(uid,
                                   username=q.from_user.username or "",
                                   first_name=q.from_user.first_name or "")
    if u.is_banned:
        await q.answer(f"أنت محظور من استخدام البوت.", show_alert=True)
        return

    # توجيه حسب data
    if data == "start":
        await cmd_start(update, context)
    elif data == "cmd_upload":
        await q.answer()
        await q.message.reply_text(
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.UPLOAD} <b>رفع ملف جديد</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"أرسل الملف مباشرةً:\n"
            f"  • <code>.py</code> — ملف بايثون\n"
            f"  • <code>.zip</code> — ملف مضغوط (يجب أن يحتوي .py)\n\n"
            f"  الحد الأقصى للحجم: <code>{MAX_FILE_SIZE_MB} MB</code>\n\n"
            f"{I.LIGHT} أرسل الملف الآن 👇",
            parse_mode=ParseMode.HTML,
            reply_markup=_kb([[(f"{I.BACK} رجوع", "start")]])
        )
    elif data.startswith("my_files_"):
        await cb_my_files(update, context, int(data.split("_")[-1]))
    elif data == "my_procs":
        await cb_my_procs(update, context)
    elif data == "my_schedule":
        await cb_my_schedule(update, context)
    elif data.startswith("leaderboard_"):
        await cb_leaderboard(update, context, int(data.split("_")[-1]))
    elif data == "premium_info":
        await cb_premium_info(update, context)
    elif data == "my_stats":
        await cb_my_stats(update, context)
    elif data == "my_settings":
        await cb_my_settings(update, context)
    elif data == "redeem_code":
        await cb_redeem_code(update, context)
    elif data == "my_referral":
        await cb_my_referral(update, context)
    elif data == "contact_support":
        await cb_support(update, context)
    elif data == "about_bot":
        await cb_about(update, context)
    # ─── ملف محدد ──────────────────────────────────────────────────
    elif data.startswith("file_view_"):
        await cb_file_view(update, context, data[len("file_view_"):])
    elif data.startswith("file_run_"):
        await cb_file_run(update, context, data[len("file_run_"):])
    elif data.startswith("file_stop_"):
        await cb_file_stop(update, context, data[len("file_stop_"):])
    elif data.startswith("file_restart_"):
        await cb_file_restart(update, context, data[len("file_restart_"):])
    elif data.startswith("file_log_"):
        await cb_file_log(update, context, data[len("file_log_"):])
    elif data.startswith("file_delete_"):
        await cb_file_delete_confirm(update, context, data[len("file_delete_"):])
    elif data.startswith("file_del_confirm_"):
        await cb_file_delete_exec(update, context, data[len("file_del_confirm_"):])
    elif data.startswith("file_install_"):
        await cb_file_install(update, context, data[len("file_install_"):])
    # ─── موافقة/رفض الملفات ────────────────────────────────────────
    elif data.startswith("approve_file_"):
        await cb_approve_file(update, context, data[len("approve_file_"):])
    elif data.startswith("reject_file_"):
        await cb_reject_file_prompt(update, context, data[len("reject_file_"):])
    elif data.startswith("ai_report_"):
        await cb_ai_report(update, context, data[len("ai_report_"):])
    # ─── لوحة الإدارة ──────────────────────────────────────────────
    elif data == "admin_main":
        await cmd_admin(update, context)
    elif data.startswith("pending_list_"):
        await cb_pending_list(update, context, int(data.split("_")[-1]))
    elif data.startswith("admin_users_"):
        await cb_admin_users(update, context, int(data.split("_")[-1]))
    elif data == "admin_admins":
        await cb_admin_admins(update, context)
    elif data.startswith("admin_files_"):
        await cb_admin_files(update, context, int(data.split("_")[-1]))
    elif data == "admin_procs":
        await cb_admin_procs(update, context)
    elif data == "admin_premium":
        await cb_admin_premium(update, context)
    elif data == "admin_promos":
        await cb_admin_promos(update, context)
    elif data == "admin_broadcast":
        await cb_admin_broadcast_menu(update, context)
    elif data == "admin_stats":
        await cb_admin_stats(update, context)
    elif data == "admin_system":
        await cb_admin_system(update, context)
    elif data.startswith("admin_audit_"):
        await cb_admin_audit(update, context, int(data.split("_")[-1]))
    elif data == "admin_backup":
        await cb_admin_backup(update, context)
    elif data == "admin_settings":
        await cb_admin_settings(update, context)
    elif data == "admin_export_bot":
        await cb_admin_export_bot(update, context)
    elif data.startswith("view_user_"):
        await cb_view_user(update, context, int(data[len("view_user_"):]))
    elif data.startswith("user_ban_"):
        await cb_user_ban(update, context, int(data[len("user_ban_"):]))
    elif data.startswith("user_unban_"):
        await cb_user_unban(update, context, int(data[len("user_unban_"):]))
    elif data.startswith("user_prem_"):
        await cb_user_grant_premium(update, context, int(data[len("user_prem_"):]))
    elif data.startswith("user_revoke_prem_"):
        await cb_user_revoke_premium(update, context, int(data[len("user_revoke_prem_"):]))
    elif data.startswith("user_add_admin_"):
        await cb_user_add_admin(update, context, int(data[len("user_add_admin_"):]))
    elif data.startswith("user_remove_admin_"):
        await cb_user_remove_admin(update, context, int(data[len("user_remove_admin_"):]))
    elif data.startswith("user_reset_pts_"):
        await cb_user_reset_points(update, context, int(data[len("user_reset_pts_"):]))
    elif data.startswith("user_add_pts_"):
        await cb_user_add_points_prompt(update, context, int(data[len("user_add_pts_"):]))
    elif data.startswith("user_warn_"):
        await cb_user_warn(update, context, int(data[len("user_warn_"):]))
    elif data.startswith("user_files_"):
        await cb_user_files(update, context, int(data[len("user_files_"):]))
    elif data == "admin_stopall":
        await cb_admin_stopall(update, context)
    elif data.startswith("admin_kill_"):
        await cb_admin_kill_proc(update, context, data[len("admin_kill_"):])
    elif data.startswith("broadcast_"):
        await cb_broadcast(update, context, data)
    elif data.startswith("backup_"):
        await cb_backup_action(update, context, data)
    elif data.startswith("setting_toggle_"):
        await cb_setting_toggle(update, context, data[len("setting_toggle_"):])
    elif data.startswith("promo_"):
        await cb_promo_action(update, context, data)
    elif data.startswith("grant_prem_days_"):
        await cb_grant_prem_days(update, context, data)
    elif data == "noop":
        await q.answer()
    else:
        await q.answer(f"⚠️ إجراء غير معروف: {data[:30]}", show_alert=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📁 إدارة ملفات المستخدم                       ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_my_files(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    uid   = update.effective_user.id
    files = db.user_files(uid)
    per   = 5
    total_pages = max(1, math.ceil(len(files) / per))
    page  = max(0, min(page, total_pages - 1))
    chunk = files[page*per:(page+1)*per]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FOLDER} <b>ملفاتي ({len(files)} ملف)</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    if not files:
        text += f"{I.INFO} لا توجد ملفات بعد.\nارفع ملفك الأول الآن! {I.UPLOAD}"
    else:
        for i, hf in enumerate(chunk, page*per+1):
            status_icon = {
                "pending":  "🟡",
                "approved": "🔵",
                "running":  "🟢",
                "stopped":  "🔴",
                "rejected": "❌",
                "error":    "💥",
            }.get(hf.status, "⚪")
            text += (
                f"{i}. {status_icon} <b>{html.escape(hf.original_name)}</b>\n"
                f"   <code>{hf.file_id}</code>  •  {FileManager.human_size(hf.size_bytes)}\n"
                f"   {Art.status_badge(hf.status)}  •  تشغيل: {hf.run_count}x\n\n"
            )
        text += f"━ صفحة {page+1}/{total_pages} ━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    rows = []
    for hf in chunk:
        rows.append([(f"{I.FILE} {hf.original_name[:25]}", f"file_view_{hf.file_id}")])

    nav = []
    if page > 0: nav.append((f"{I.PREV} السابق", f"my_files_{page-1}"))
    if page < total_pages - 1: nav.append((f"{I.NEXT} التالي", f"my_files_{page+1}"))
    if nav: rows.append(nav)
    rows.append([(f"{I.UPLOAD} رفع ملف جديد", "cmd_upload"), (f"{I.HOME} الرئيسية", "start")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_file_view(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    u   = db.get_user(uid)
    is_admin = u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)

    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return
    if hf.user_id != uid and not is_admin:
        await update.callback_query.answer("❌ لا تملك صلاحية عرض هذا الملف", show_alert=True)
        return

    is_running = proc_mgr.is_running(file_id)
    stats      = proc_mgr.process_stats(file_id) if is_running else {}

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FILE} <b>تفاصيل الملف</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.FILE} <b>الاسم:</b> <code>{html.escape(hf.original_name)}</code>\n"
        f"  {I.KEY}  <b>المعرف:</b> <code>{hf.file_id}</code>\n"
        f"  {I.TAG}  <b>النوع:</b> <code>{hf.file_type}</code>\n"
        f"  {I.DISK} <b>الحجم:</b> <code>{FileManager.human_size(hf.size_bytes)}</code>\n"
        f"  {I.CLOCK} <b>الحالة:</b> {Art.status_badge(hf.status)}\n"
        f"  {I.RUN} <b>عدد التشغيل:</b> <code>{hf.run_count}</code>\n"
        f"  {I.CAL} <b>الرفع:</b> <code>{hf.uploaded_at[:10]}</code>\n"
    )

    if hf.ai_verdict:
        text += f"  {I.AI} <b>AI:</b> {hf.ai_verdict} (<code>{hf.ai_score:.0f}/100</code>)\n"

    if is_running and stats:
        text += (
            f"\n{I.GREEN} <b>العملية نشطة:</b>\n"
            f"  PID: <code>{stats.get('pid', 'N/A')}</code>  |  "
            f"CPU: <code>{stats.get('cpu', 0):.1f}%</code>  |  "
            f"RAM: <code>{FileManager.human_size(stats.get('mem', 0))}</code>\n"
            f"  مدة التشغيل: <code>{stats.get('uptime', 'N/A')}</code>\n"
        )

    if hf.description:
        text += f"\n{I.NOTE} <b>الوصف:</b> {html.escape(hf.description)}"

    text += f"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    rows = []
    can_run = hf.status in (FileStatus.APPROVED.value, FileStatus.STOPPED.value, FileStatus.ERROR.value)
    can_stop = is_running

    if can_run and not is_running:
        rows.append([(f"{I.PLAY} ✦ تشغيل", f"file_run_{file_id}")])
    if can_stop:
        rows.append([(f"{I.STOP} ✦ إيقاف", f"file_stop_{file_id}"),
                     (f"{I.RESTART} إعادة تشغيل", f"file_restart_{file_id}")])
    if is_running:
        rows.append([(f"{I.LOG} عرض المخرجات", f"file_log_{file_id}")])

    if hf.status == FileStatus.APPROVED.value and not is_running:
        rows.append([(f"{I.TOOLS} تثبيت المكتبات", f"file_install_{file_id}")])

    if hf.ai_score > 0:
        rows.append([(f"{I.AI} تقرير AI التفصيلي", f"ai_report_{file_id}")])

    rows.append([(f"{I.DELETE} حذف الملف", f"file_delete_{file_id}"),
                 (f"{I.BACK} رجوع", f"my_files_0")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_file_run(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    u   = db.get_user(uid)
    is_admin = u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)

    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return
    if hf.user_id != uid and not is_admin:
        await update.callback_query.answer("❌ ليس ملفك", show_alert=True)
        return
    if hf.status not in (FileStatus.APPROVED.value, FileStatus.STOPPED.value, FileStatus.ERROR.value):
        status_msg = {
            FileStatus.PENDING.value:  "الملف ينتظر الموافقة",
            FileStatus.REJECTED.value: "الملف مرفوض",
        }.get(hf.status, f"لا يمكن تشغيل الملف (الحالة: {hf.status})")
        await update.callback_query.answer(f"⚠️ {status_msg}", show_alert=True)
        return
    if proc_mgr.is_running(file_id):
        await update.callback_query.answer("⚠️ الملف يعمل بالفعل", show_alert=True)
        return

    # فحص حد العمليات
    max_procs = MAX_PROCESSES_PREMIUM if (u and u.is_premium) else MAX_PROCESSES_PER_USER
    if proc_mgr.count_user(uid) >= max_procs and not is_admin:
        await update.callback_query.answer(
            f"⚠️ وصلت للحد الأقصى ({max_procs} عمليات)", show_alert=True)
        return

    await update.callback_query.answer("▶️ جاري التشغيل...")

    # تحضير مسار الملف
    file_path = FileManager.file_path(uid, hf.stored_name)
    if not os.path.exists(file_path):
        # إذا كان الملف في pending (تم نقله عند الموافقة)
        file_path = FileManager.file_path(uid, hf.stored_name, pending=False)
    work_dir = os.path.dirname(file_path)

    ok, msg = await proc_mgr.start_process(file_path, file_id, uid, hf.original_name, work_dir)
    if ok:
        hf.status   = FileStatus.RUNNING.value
        hf.run_count += 1
        hf.last_run  = datetime.now(timezone.utc).isoformat()
        db.save_file(hf)
        u.run_count += 1
        u.points    += 3
        db.save_user(u)
        db.set_setting("global_stats.total_runs",
                       db.get_setting("global_stats.total_runs", 0) + 1)
        db.add_audit(uid, "file_run", f"file:{file_id}", f"PID:{msg}")
        await db.save_now()
        await update.callback_query.message.reply_text(
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.PLAY} <b>الملف يعمل الآن!</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n"
            f"  {I.KEY}  <code>{msg}</code>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            parse_mode=ParseMode.HTML,
            reply_markup=_kb([
                [(f"{I.LOG} عرض المخرجات", f"file_log_{file_id}"),
                 (f"{I.STOP} إيقاف", f"file_stop_{file_id}")],
                [(f"{I.BACK} عرض الملف", f"file_view_{file_id}")],
            ])
        )
    else:
        hf.status = FileStatus.ERROR.value
        db.save_file(hf)
        await update.callback_query.message.reply_text(
            f"{I.FAIL} <b>فشل التشغيل:</b>\n<code>{html.escape(msg)}</code>",
            parse_mode=ParseMode.HTML
        )


async def cb_file_stop(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    u   = db.get_user(uid)
    is_admin = u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)

    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return
    if hf.user_id != uid and not is_admin:
        await update.callback_query.answer("❌ ليس ملفك", show_alert=True)
        return

    ok, msg = proc_mgr.stop_process(file_id)
    if ok:
        hf.status = FileStatus.STOPPED.value
        db.save_file(hf)
        db.add_audit(uid, "file_stop", f"file:{file_id}")
        await db.save_now()
        await update.callback_query.answer(f"⏹️ تم الإيقاف")
        await update.callback_query.message.reply_text(
            f"{I.STOP} <b>تم إيقاف الملف</b>\n"
            f"<code>{html.escape(hf.original_name)}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup=_kb([[(f"{I.BACK} عرض الملف", f"file_view_{file_id}")]])
        )
    else:
        await update.callback_query.answer(f"⚠️ {msg}", show_alert=True)


async def cb_file_restart(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    if not hf: return
    proc_mgr.stop_process(file_id)
    await asyncio.sleep(1)
    # إعادة استخدام منطق التشغيل
    await cb_file_run(update, context, file_id)


async def cb_file_log(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    u   = db.get_user(uid)
    is_admin = u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)

    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return
    if hf.user_id != uid and not is_admin:
        await update.callback_query.answer("❌ ليس ملفك", show_alert=True)
        return

    out, err = proc_mgr.get_output(file_id, last_n=30)
    status_icon = "🟢 يعمل" if proc_mgr.is_running(file_id) else "🔴 متوقف"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.TERM} <b>مخرجات الملف</b>  {status_icon}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    if out:
        trimmed = out[-MAX_OUTPUT_LENGTH:]
        text += f"<b>stdout:</b>\n<pre>{html.escape(trimmed)}</pre>\n"
    if err:
        trimmed_e = err[-2000:]
        text += f"\n<b>stderr:</b>\n<pre>{html.escape(trimmed_e)}</pre>\n"
    if not out and not err:
        text += f"{I.INFO} لا توجد مخرجات بعد."

    text += f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        text, parse_mode=ParseMode.HTML,
        reply_markup=_kb([
            [(f"{I.REFRESH} تحديث", f"file_log_{file_id}"),
             (f"{I.STOP} إيقاف", f"file_stop_{file_id}")],
            [(f"{I.BACK} عرض الملف", f"file_view_{file_id}")],
        ])
    )


async def cb_file_delete_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    hf = db.get_file(file_id)
    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.WARN} <b>تأكيد الحذف</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"هل تريد حذف هذا الملف نهائياً؟\n"
        f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n"
        f"  <code>{file_id}</code>\n\n"
        f"{I.WARN} <b>هذا الإجراء لا يمكن التراجع عنه!</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([
            [(f"{I.FAIL} نعم، احذف", f"file_del_confirm_{file_id}"),
             (f"{I.OK} لا، تراجع", f"file_view_{file_id}")],
        ])
    )


async def cb_file_delete_exec(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    u   = db.get_user(uid)
    is_admin = u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)

    if not hf or (hf.user_id != uid and not is_admin):
        await update.callback_query.answer("❌ لا تملك صلاحية الحذف", show_alert=True)
        return

    # إيقاف العملية إن كانت تعمل
    if proc_mgr.is_running(file_id):
        proc_mgr.stop_process(file_id)

    # حذف الملف الفعلي
    for path in [
        FileManager.file_path(hf.user_id, hf.stored_name),
        FileManager.file_path(hf.user_id, hf.stored_name, pending=True),
    ]:
        with suppress(FileNotFoundError):
            os.remove(path)

    db.delete_file(file_id)
    if u and u.user_id == hf.user_id:
        u.file_count = max(0, u.file_count - 1)
        u.total_storage = max(0, u.total_storage - hf.size_bytes)
        db.save_user(u)
    db.add_audit(uid, "file_delete", f"file:{file_id}", hf.original_name)
    await db.save_now()
    await update.callback_query.answer("🗑️ تم الحذف")
    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.OK} <b>تم حذف الملف بنجاح</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([[(f"{I.FOLDER} ملفاتي", "my_files_0"), (f"{I.HOME} الرئيسية", "start")]])
    )


async def cb_file_install(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return

    await update.callback_query.answer("⏳ جاري تثبيت المكتبات...")
    msg = await update.callback_query.message.reply_text(
        f"{I.TOOLS} <b>جاري تثبيت المكتبات...</b>",
        parse_mode=ParseMode.HTML
    )

    file_path = FileManager.file_path(uid, hf.stored_name)
    work_dir  = os.path.dirname(file_path)
    req_file  = os.path.join(work_dir, "requirements.txt")
    req_file  = req_file if os.path.exists(req_file) else None

    extra_libs = None
    if hf.file_type == "python":
        with suppress(Exception):
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
            extra_libs = FileManager.extract_imports_from_code(code)
            # إزالة المكتبات المدمجة
            extra_libs = [l for l in extra_libs if l not in AIAnalyzer.KNOWN_LIBS["standard"]]

    ok, output = await FileManager.install_requirements(work_dir, req_file, extra_libs or [])
    hf.install_output = output[:2000]
    db.save_file(hf)
    await db.save_now()

    result_icon = I.OK if ok else I.FAIL
    await safe_edit(
        msg,
        f"{result_icon} <b>{'تم التثبيت بنجاح' if ok else 'فشل التثبيت'}</b>\n\n"
        f"<pre>{html.escape(output[:1500])}</pre>",
        parse_mode=ParseMode.HTML
    )


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ✅ نظام الموافقة والرفض                       ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_approve_file(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    """موافقة الأدمن على الملف"""
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    hf = db.get_file(file_id)
    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return
    if hf.status != FileStatus.PENDING.value:
        await update.callback_query.answer(f"⚠️ الملف ليس في الانتظار (الحالة: {hf.status})", show_alert=True)
        return

    # نقل الملف من pending إلى hosted
    pending_path = FileManager.file_path(hf.user_id, hf.stored_name, pending=True)
    approved_path = FileManager.file_path(hf.user_id, hf.stored_name, pending=False)

    moved = False
    if os.path.exists(pending_path):
        try:
            shutil.move(pending_path, approved_path)
            moved = True
        except Exception as e:
            logger.error(f"خطأ نقل الملف: {e}")

    hf.status      = FileStatus.APPROVED.value
    hf.approved_at = datetime.now(timezone.utc).isoformat()
    hf.approved_by = uid
    db.save_file(hf)
    db.add_audit(uid, "file_approve", f"file:{file_id}", hf.original_name)
    await db.save_now()

    admin_name = u.first_name or u.username or str(uid)
    await update.callback_query.answer("✅ تمت الموافقة")
    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.OK} <b>تمت الموافقة على الملف</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n"
        f"  {I.KEY}  <code>{file_id}</code>\n"
        f"  {I.ADMIN} وافق عليه: {html.escape(admin_name)}\n"
        f"{'  ' + I.OK + ' تم نقل الملف للتشغيل' if moved else '  ' + I.WARN + ' تحذير: لم يُعثر على الملف المادي'}",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([
            [(f"{I.PLAY} تشغيل الآن", f"file_run_{file_id}"),
             (f"{I.FILE} عرض الملف",  f"file_view_{file_id}")],
            [(f"{I.QUEUE} المعلقة",   "pending_list_0"),
             (f"{I.HOME} الإدارة",    "admin_main")],
        ])
    )

    # إشعار صاحب الملف
    owner = db.get_user(hf.user_id)
    if owner and owner.notifications:
        await safe_send(
            context.bot, hf.user_id,
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.OK} <b>تمت الموافقة على ملفك!</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n\n"
            f"{I.PLAY} يمكنك الآن تشغيله من ملفاتي.",
            parse_mode=ParseMode.HTML,
            reply_markup=_kb([[(f"{I.PLAY} تشغيل الآن", f"file_run_{file_id}")]])
        )


async def cb_reject_file_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    """طلب سبب الرفض"""
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    hf = db.get_file(file_id)
    if not hf:
        await update.callback_query.answer("❌ الملف غير موجود", show_alert=True)
        return

    await update.callback_query.answer()

    # أسباب رفض جاهزة
    reasons_kb = _kb([
        [(f"🔴 كود خطير",         f"reject_exec_{file_id}_كود_يحتوي_على_أوامر_خطيرة"),
         (f"🟠 مشبوه",            f"reject_exec_{file_id}_الملف_مشبوه_ويحتاج_مراجعة")],
        [(f"🟡 حجم كبير",         f"reject_exec_{file_id}_حجم_الملف_كبير_جداً"),
         (f"⚠️ مكتبات غير مسموح", f"reject_exec_{file_id}_يستخدم_مكتبات_غير_مسموح_بها")],
        [(f"❌ مخالفة القواعد",   f"reject_exec_{file_id}_يخالف_قواعد_الاستخدام"),
         (f"🚫 محتوى غير لائق",   f"reject_exec_{file_id}_محتوى_غير_لائق")],
        [(f"{I.BACK} تراجع",       f"pending_list_0")],
    ])

    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FAIL} <b>رفض الملف</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n\n"
        f"اختر سبب الرفض:",
        parse_mode=ParseMode.HTML,
        reply_markup=reasons_kb
    )

    # تخزين context لاستخدامه في reject_exec
    context.bot_data[f"reject_{file_id}"] = True


async def _execute_reject(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    file_id: str,
    reason: str,
):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    hf  = db.get_file(file_id)
    if not hf: return

    hf.status       = FileStatus.REJECTED.value
    hf.rejected_at  = datetime.now(timezone.utc).isoformat()
    hf.rejected_by  = uid
    hf.reject_reason = reason
    db.save_file(hf)
    db.add_audit(uid, "file_reject", f"file:{file_id}", f"سبب: {reason}")
    await db.save_now()

    admin_name = (u.first_name if u else None) or str(uid)
    await update.callback_query.answer("❌ تم الرفض")
    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FAIL} <b>تم رفض الملف</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n"
        f"  {I.NOTE} السبب: {html.escape(reason)}\n"
        f"  {I.ADMIN} رفضه: {html.escape(admin_name)}",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([
            [(f"{I.QUEUE} المعلقة", "pending_list_0"),
             (f"{I.HOME} الإدارة",  "admin_main")],
        ])
    )

    # إشعار صاحب الملف
    owner = db.get_user(hf.user_id)
    if owner and owner.notifications:
        await safe_send(
            context.bot, hf.user_id,
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.FAIL} <b>تم رفض ملفك</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  {I.FILE} <code>{html.escape(hf.original_name)}</code>\n"
            f"  {I.NOTE} السبب: {html.escape(reason)}\n\n"
            f"{I.MSG} للاستفسار تواصل مع @{SUPPORT_USERNAME}",
            parse_mode=ParseMode.HTML
        )


async def cb_ai_report(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    hf  = db.get_file(file_id)
    u   = db.get_user(uid)
    is_admin = u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value)

    if not hf: return
    if hf.user_id != uid and not is_admin:
        await update.callback_query.answer("❌ لا صلاحية", show_alert=True)
        return

    # إعادة التحليل
    file_path = FileManager.file_path(hf.user_id, hf.stored_name)
    if not os.path.exists(file_path):
        file_path = FileManager.file_path(hf.user_id, hf.stored_name, pending=True)

    await update.callback_query.answer()

    if hf.file_type != "python" or not os.path.exists(file_path):
        await update.callback_query.message.reply_text(
            f"{I.INFO} تحليل AI متاح فقط لملفات .py"
        )
        return

    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            code = f.read()
        result = AIAnalyzer.analyze(code, hf.original_name)
        report = AIAnalyzer.format_report(result, hf.original_name)
        await update.callback_query.message.reply_text(
            report, parse_mode=ParseMode.HTML,
            reply_markup=_kb([[(f"{I.BACK} رجوع", f"file_view_{file_id}")]])
        )
    except Exception as e:
        await update.callback_query.message.reply_text(
            f"{I.FAIL} فشل التحليل: <code>{html.escape(str(e))}</code>",
            parse_mode=ParseMode.HTML
        )


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📋 قائمة الملفات المعلقة                      ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_pending_list(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    files   = db.pending_files()
    per     = 5
    total_p = max(1, math.ceil(len(files) / per))
    page    = max(0, min(page, total_p - 1))
    chunk   = files[page*per:(page+1)*per]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.QUEUE} <b>الملفات المعلقة ({len(files)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    if not files:
        text += f"{I.OK} لا توجد ملفات تنتظر الموافقة {I.CLEAN}"
    else:
        for i, hf in enumerate(chunk, page*per+1):
            owner = db.get_user(hf.user_id)
            owner_str = f"@{owner.username}" if (owner and owner.username) else str(hf.user_id)
            age = ""
            with suppress(Exception):
                up = datetime.fromisoformat(hf.uploaded_at.replace("Z", "+00:00"))
                delta = datetime.now(timezone.utc) - up
                age = f"منذ {int(delta.total_seconds()/60)} دق"
            text += (
                f"{i}. {I.FILE} <b>{html.escape(hf.original_name)}</b>\n"
                f"   المعرف: <code>{hf.file_id}</code>  •  {owner_str}\n"
                f"   {FileManager.human_size(hf.size_bytes)}  •  {age}\n"
            )
            if hf.ai_verdict:
                text += f"   {I.AI} {hf.ai_verdict}\n"
            text += "\n"

        text += f"━ صفحة {page+1}/{total_p} ━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    rows = []
    for hf in chunk:
        rows.append([
            (f"{I.OK} قبول — {hf.original_name[:18]}", f"approve_file_{hf.file_id}"),
            (f"{I.FAIL} رفض",                          f"reject_file_{hf.file_id}"),
        ])

    nav = []
    if page > 0: nav.append((f"{I.PREV} السابق", f"pending_list_{page-1}"))
    if page < total_p - 1: nav.append((f"{I.NEXT} التالي", f"pending_list_{page+1}"))
    if nav: rows.append(nav)
    rows.append([(f"{I.REFRESH} تحديث", f"pending_list_{page}"),
                 (f"{I.BACK} الإدارة", "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    👥 إدارة المستخدمين                           ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_users(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    users = sorted(db.all_users(), key=lambda x: x.joined_at, reverse=True)
    per   = 8
    total_p = max(1, math.ceil(len(users) / per))
    page    = max(0, min(page, total_p - 1))
    chunk   = users[page*per:(page+1)*per]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.USERS} <b>إدارة المستخدمين ({len(users)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    for i, user in enumerate(chunk, page*per+1):
        badges = []
        if user.role == UserRole.OWNER.value: badges.append("👑")
        elif user.role == UserRole.ADMIN.value: badges.append("🛡️")
        if user.is_premium: badges.append("💫")
        if user.is_banned: badges.append("🚫")
        badge_str = " ".join(badges)
        name = html.escape(user.first_name or user.username or str(user.user_id))
        text += (
            f"{i}. {badge_str} <b>{name}</b>  <code>{user.user_id}</code>\n"
            f"   {I.POINTS} {user.points}  •  {I.FILE} {user.file_count}  •  {I.RUN} {user.run_count}\n\n"
        )

    text += f"━ صفحة {page+1}/{total_p} ━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    rows = []
    for user in chunk:
        rows.append([(
            f"{Art.status_badge(user.role)[:3]} {html.escape((user.first_name or user.username or str(user.user_id))[:20])}",
            f"view_user_{user.user_id}"
        )])

    nav = []
    if page > 0: nav.append((f"{I.PREV}", f"admin_users_{page-1}"))
    if page < total_p - 1: nav.append((f"{I.NEXT}", f"admin_users_{page+1}"))
    if nav: rows.append(nav)
    rows.append([(f"{I.REFRESH} تحديث", f"admin_users_{page}"),
                 (f"{I.BACK} الإدارة",  "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_view_user(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer     = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target:
        await update.callback_query.answer("❌ المستخدم غير موجود", show_alert=True)
        return

    files    = db.user_files(target_uid)
    running  = proc_mgr.count_user(target_uid)
    prem_str = ""
    if target.is_premium:
        if target.premium_until:
            prem_str = f"  حتى: <code>{target.premium_until[:10]}</code>"
        else:
            prem_str = "  دائم"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.USER} <b>ملف المستخدم</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.USER} <b>الاسم:</b> {html.escape(target.first_name or 'بدون')}\n"
        f"  {I.TAG}  <b>يوزر:</b> @{html.escape(target.username or 'بدون')}\n"
        f"  {I.KEY}  <b>ID:</b> <code>{target.user_id}</code>\n"
        f"  {I.SHIELD} <b>الدور:</b> {Art.status_badge(target.role)}\n"
        f"  {I.GREEN if not target.is_banned else I.RED} "
        f"<b>الحالة:</b> {'🚫 محظور' if target.is_banned else '🟢 نشط'}\n"
    )
    if target.is_banned and target.ban_reason:
        text += f"  {I.NOTE} <b>سبب الحظر:</b> {html.escape(target.ban_reason)}\n"
    text += (
        f"  {I.PREM} <b>بريميوم:</b> {'✅' + prem_str if target.is_premium else '❌'}\n\n"
        f"  {I.STATS} <b>الإحصائيات:</b>\n"
        f"  {I.POINTS} النقاط: <code>{target.points:,}</code>\n"
        f"  {I.FILE} الملفات: <code>{len(files)}</code>  •  "
        f"{I.RUN} التشغيل: <code>{target.run_count}</code>\n"
        f"  {I.LINK} الإحالات: <code>{target.invites}</code>  •  "
        f"{I.WARN} تحذيرات: <code>{target.warning_count}</code>\n"
        f"  {I.GREEN} نشط الآن: <code>{running}</code> عملية\n"
        f"  {I.CAL} الانضمام: <code>{target.joined_at[:10]}</code>\n"
        f"  {I.CLOCK} آخر نشاط: <code>{target.last_active[:10]}</code>\n"
    )
    if target.notes:
        text += f"\n  {I.NOTE} <b>ملاحظة:</b> {html.escape(target.notes)}\n"
    text += f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # أزرار الإجراءات
    rows = []
    is_self = viewer_uid == target_uid
    is_owner_target = target.role == UserRole.OWNER.value

    if not is_self and not is_owner_target:
        if target.is_banned:
            rows.append([(f"{I.UNBAN} فك الحظر", f"user_unban_{target_uid}")])
        else:
            rows.append([(f"{I.BAN} حظر المستخدم", f"user_ban_{target_uid}")])

        if target.is_premium:
            rows.append([(f"{I.MINUS} سحب البريميوم", f"user_revoke_prem_{target_uid}")])
        else:
            rows.append([(f"{I.PREM} منح بريميوم", f"user_prem_{target_uid}")])

        if viewer.role == UserRole.OWNER.value:
            if target.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
                rows.append([(f"{I.ADMIN} ترقية لأدمن", f"user_add_admin_{target_uid}")])
            else:
                rows.append([(f"{I.MINUS} إزالة من الأدمنز", f"user_remove_admin_{target_uid}")])

        rows.append([
            (f"{I.WARN} تحذير", f"user_warn_{target_uid}"),
            (f"{I.POINTS} إضافة نقاط", f"user_add_pts_{target_uid}"),
        ])

    rows.append([(f"{I.FILE} ملفات المستخدم", f"user_files_{target_uid}")])
    rows.append([(f"{I.BACK} قائمة المستخدمين", "admin_users_0"),
                 (f"{I.HOME} الإدارة", "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_user_ban(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target:
        await update.callback_query.answer("❌ المستخدم غير موجود", show_alert=True)
        return
    if target.role == UserRole.OWNER.value:
        await update.callback_query.answer("⚠️ لا يمكن حظر المالك", show_alert=True)
        return

    target.is_banned   = True
    target.ban_reason  = "حظر من قبل المشرف"
    target.role        = UserRole.BANNED.value
    db.save_user(target)
    db.add_audit(viewer_uid, "user_ban", str(target_uid))

    # إيقاف عملياته
    stopped = proc_mgr.stop_all_user(target_uid)
    await db.save_now()
    await update.callback_query.answer("🚫 تم الحظر")
    await cb_view_user(update, context, target_uid)

    # إشعار المحظور
    await safe_send(
        context.bot, target_uid,
        f"{I.BAN} تم حظرك من استخدام البوت.\n"
        f"للاستفسار تواصل مع @{SUPPORT_USERNAME}"
    )


async def cb_user_unban(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target:
        await update.callback_query.answer("❌ المستخدم غير موجود", show_alert=True)
        return

    target.is_banned  = False
    target.ban_reason = ""
    target.role       = UserRole.USER.value
    db.save_user(target)
    db.add_audit(viewer_uid, "user_unban", str(target_uid))
    await db.save_now()
    await update.callback_query.answer("🟢 تم فك الحظر")
    await cb_view_user(update, context, target_uid)
    await safe_send(context.bot, target_uid,
                    f"{I.UNBAN} تم فك حظرك! يمكنك استخدام البوت الآن.")


async def cb_user_grant_premium(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.PREM} <b>منح بريميوم</b>  للمستخدم <code>{target_uid}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"اختر مدة البريميوم:",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([
            [(f"7 أيام",   f"grant_prem_days_{target_uid}_7"),
             (f"30 يوم",   f"grant_prem_days_{target_uid}_30")],
            [(f"90 يوم",   f"grant_prem_days_{target_uid}_90"),
             (f"365 يوم",  f"grant_prem_days_{target_uid}_365")],
            [(f"دائم ♾️",  f"grant_prem_days_{target_uid}_0")],
            [(f"{I.BACK} رجوع", f"view_user_{target_uid}")],
        ])
    )


async def cb_grant_prem_days(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    parts = data.split("_")
    # grant_prem_days_{uid}_{days}
    viewer_uid  = update.effective_user.id
    viewer      = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    try:
        target_uid = int(parts[3])
        days       = int(parts[4])
    except (IndexError, ValueError):
        await update.callback_query.answer("❌ بيانات غير صحيحة", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target:
        await update.callback_query.answer("❌ المستخدم غير موجود", show_alert=True)
        return

    target.is_premium = True
    if days == 0:
        target.premium_until = None
        target.premium_plan  = "lifetime"
        until_str = "دائم ♾️"
    else:
        until_dt = datetime.now(timezone.utc) + timedelta(days=days)
        target.premium_until = until_dt.isoformat()
        target.premium_plan  = f"{days}d"
        until_str = until_dt.strftime("%Y-%m-%d")
    target.points += 50  # نقاط هدية
    if target.role == UserRole.USER.value:
        target.role = UserRole.PREMIUM.value
    db.save_user(target)
    db.add_audit(viewer_uid, "grant_premium", str(target_uid), f"days:{days}")
    await db.save_now()
    await update.callback_query.answer(f"✅ تم منح البريميوم لـ {days or '∞'} يوم")
    await update.callback_query.edit_message_text(
        f"{I.OK} <b>تم منح البريميوم بنجاح!</b>\n"
        f"  المستخدم: <code>{target_uid}</code>\n"
        f"  المدة: <code>{until_str}</code>",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([[(f"{I.BACK} ملف المستخدم", f"view_user_{target_uid}")]])
    )
    await safe_send(
        context.bot, target_uid,
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.PREM} <b>تهانينا! تم تفعيل البريميوم</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  المدة: <code>{until_str}</code>\n"
        f"  العمليات: <code>{MAX_PROCESSES_PREMIUM}</code> في وقت واحد\n"
        f"  +50 نقطة هدية! {I.GIFT}",
        parse_mode=ParseMode.HTML
    )


async def cb_user_revoke_premium(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target:
        await update.callback_query.answer("❌ المستخدم غير موجود", show_alert=True)
        return

    target.is_premium    = False
    target.premium_until = None
    target.premium_plan  = ""
    if target.role == UserRole.PREMIUM.value:
        target.role = UserRole.USER.value
    db.save_user(target)
    db.add_audit(viewer_uid, "revoke_premium", str(target_uid))
    await db.save_now()
    await update.callback_query.answer("✅ تم سحب البريميوم")
    await cb_view_user(update, context, target_uid)


async def cb_user_add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role != UserRole.OWNER.value:
        await update.callback_query.answer("❌ فقط المالك يمكنه ترقية أدمنز", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target:
        await update.callback_query.answer("❌ المستخدم غير موجود", show_alert=True)
        return

    target.role       = UserRole.ADMIN.value
    target.admin_perms = [
        AdminPermission.APPROVE_FILES.value,
        AdminPermission.MANAGE_USERS.value,
        AdminPermission.BROADCAST.value,
        AdminPermission.VIEW_STATS.value,
        AdminPermission.MANAGE_PREMIUM.value,
        AdminPermission.VIEW_LOGS.value,
        AdminPermission.KILL_PROCESSES.value,
    ]
    db.save_user(target)
    db.add_audit(viewer_uid, "add_admin", str(target_uid))
    await db.save_now()
    await update.callback_query.answer("✅ تمت الترقية للأدمن")
    await cb_view_user(update, context, target_uid)
    await safe_send(
        context.bot, target_uid,
        f"{I.ADMIN} <b>تهانينا! تمت ترقيتك لمشرف في البوت.</b>\n"
        f"استخدم /admin للوصول للوحة الإدارة.",
        parse_mode=ParseMode.HTML
    )


async def cb_user_remove_admin(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role != UserRole.OWNER.value:
        await update.callback_query.answer("❌ فقط المالك يمكنه إزالة الأدمنز", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target: return

    target.role        = UserRole.USER.value
    target.admin_perms = []
    db.save_user(target)
    db.add_audit(viewer_uid, "remove_admin", str(target_uid))
    await db.save_now()
    await update.callback_query.answer("✅ تمت إزالة صلاحيات الأدمن")
    await cb_view_user(update, context, target_uid)


async def cb_user_warn(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target: return
    target.warning_count += 1
    db.save_user(target)
    db.add_audit(viewer_uid, "user_warn", str(target_uid))
    await db.save_now()
    await update.callback_query.answer(f"⚠️ تم التحذير ({target.warning_count})")
    await safe_send(
        context.bot, target_uid,
        f"{I.WARN} <b>تحذير من الإدارة!</b>\n"
        f"هذا تحذير رقم {target.warning_count}.\n"
        f"3 تحذيرات = حظر تلقائي."
    )
    if target.warning_count >= 3:
        target.is_banned  = True
        target.ban_reason = "3 تحذيرات متراكمة"
        target.role       = UserRole.BANNED.value
        db.save_user(target)
        await db.save_now()
        await safe_send(context.bot, target_uid, f"{I.BAN} تم حظرك تلقائياً لتراكم التحذيرات.")


async def cb_user_reset_points(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target = db.get_user(target_uid)
    if not target: return
    target.points = 0
    db.save_user(target)
    db.add_audit(viewer_uid, "reset_points", str(target_uid))
    await db.save_now()
    await update.callback_query.answer("✅ تم إعادة النقاط لصفر")
    await cb_view_user(update, context, target_uid)


async def cb_user_add_points_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    await update.callback_query.answer()
    # تخزين حالة الانتظار
    context.user_data["add_pts_target"] = target_uid
    await update.callback_query.message.reply_text(
        f"{I.POINTS} <b>إضافة نقاط للمستخدم <code>{target_uid}</code></b>\n\n"
        f"أرسل العدد الذي تريد إضافته (مثال: 100):",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([[(f"{I.BACK} إلغاء", f"view_user_{target_uid}")]])
    )


async def cb_user_files(update: Update, context: ContextTypes.DEFAULT_TYPE, target_uid: int):
    viewer_uid = update.effective_user.id
    viewer = db.get_user(viewer_uid)
    if not viewer or viewer.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    files = db.user_files(target_uid)
    text  = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FOLDER} <b>ملفات المستخدم {target_uid}</b> ({len(files)})\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    for i, hf in enumerate(files[:10], 1):
        text += (
            f"{i}. {Art.status_badge(hf.status)} <code>{html.escape(hf.original_name)}</code>\n"
            f"   {FileManager.human_size(hf.size_bytes)}  •  تشغيل {hf.run_count}x\n\n"
        )
    if not files:
        text += f"{I.INFO} لا توجد ملفات."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text, parse_mode=ParseMode.HTML,
        reply_markup=_kb([
            [(f"{I.BACK} ملف المستخدم", f"view_user_{target_uid}"),
             (f"{I.HOME} الإدارة", "admin_main")]
        ])
    )


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🛡️ إدارة الأدمنز                             ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_admins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role != UserRole.OWNER.value:
        await update.callback_query.answer("❌ فقط المالك", show_alert=True)
        return

    admins = [a for a in db.all_users()
              if a.role in (UserRole.ADMIN.value, UserRole.OWNER.value)]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.ADMIN} <b>إدارة الأدمنز ({len(admins)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    for i, admin in enumerate(admins, 1):
        role_icon = I.CROWN if admin.role == UserRole.OWNER.value else I.ADMIN
        perms     = ", ".join(admin.admin_perms[:3]) if admin.admin_perms else "كاملة"
        text += (
            f"{i}. {role_icon} <b>{html.escape(admin.first_name or admin.username or str(admin.user_id))}</b>\n"
            f"   ID: <code>{admin.user_id}</code>  •  صلاحيات: <code>{perms}</code>\n\n"
        )

    rows = [[( f"{I.USER} عرض ملف {a.first_name or str(a.user_id)}", f"view_user_{a.user_id}")] for a in admins[:5]]
    rows.append([(f"{I.BACK} الإدارة", "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📁 إدارة الملفات (أدمن)                       ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_files(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    all_files = db.all_files()
    per       = 8
    total_p   = max(1, math.ceil(len(all_files) / per))
    page      = max(0, min(page, total_p - 1))
    chunk     = all_files[page*per:(page+1)*per]

    running = sum(1 for f in all_files if f.status == FileStatus.RUNNING.value)
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FILE} <b>إدارة الملفات ({len(all_files)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  🟢 نشط: {running}  •  🟡 انتظار: {len(db.pending_files())}  •  "
        f"الكل: {len(all_files)}\n\n"
    )

    for i, hf in enumerate(chunk, page*per+1):
        owner = db.get_user(hf.user_id)
        owner_str = f"@{owner.username}" if (owner and owner.username) else str(hf.user_id)
        text += (
            f"{i}. {Art.status_badge(hf.status)[:3]} "
            f"<code>{html.escape(hf.original_name[:25])}</code>\n"
            f"   {owner_str}  •  {FileManager.human_size(hf.size_bytes)}\n\n"
        )

    text += f"━ صفحة {page+1}/{total_p} ━━━━━━━━━━━━━━━━━━━━━━━━━"
    rows = [[( f"{I.FILE} {hf.original_name[:20]}", f"file_view_{hf.file_id}")] for hf in chunk]
    nav = []
    if page > 0: nav.append((f"{I.PREV}", f"admin_files_{page-1}"))
    if page < total_p - 1: nav.append((f"{I.NEXT}", f"admin_files_{page+1}"))
    if nav: rows.append(nav)
    rows.append([(f"{I.BACK} الإدارة", "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ⚡ العمليات النشطة (أدمن)                      ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_procs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    procs = proc_mgr.get_all_running()
    text  = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.GREEN} <b>العمليات النشطة ({len(procs)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    if not procs:
        text += f"{I.INFO} لا توجد عمليات نشطة."
    else:
        for i, rp in enumerate(procs, 1):
            stats   = proc_mgr.process_stats(rp.file_id)
            owner   = db.get_user(rp.user_id)
            own_str = f"@{owner.username}" if (owner and owner.username) else str(rp.user_id)
            text += (
                f"{i}. {I.GREEN} <b>{html.escape(rp.file_name)}</b>\n"
                f"   PID: <code>{rp.pid}</code>  •  المستخدم: {own_str}\n"
                f"   CPU: <code>{stats.get('cpu',0):.1f}%</code>  •  "
                f"RAM: <code>{FileManager.human_size(stats.get('mem',0))}</code>  •  "
                f"مدة: <code>{stats.get('uptime','?')}</code>\n\n"
            )

    rows = []
    for rp in procs[:5]:
        rows.append([(f"{I.STOP} إيقاف {rp.file_name[:20]}", f"admin_kill_{rp.file_id}")])
    rows.append([(f"{I.STOP} إيقاف الكل",   "admin_stopall"),
                 (f"{I.REFRESH} تحديث",      "admin_procs")])
    rows.append([(f"{I.BACK} الإدارة",        "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_admin_kill_proc(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    ok, msg = proc_mgr.stop_process(file_id)
    hf = db.get_file(file_id)
    if hf and ok:
        hf.status = FileStatus.STOPPED.value
        db.save_file(hf)
        db.add_audit(uid, "admin_kill_proc", f"file:{file_id}")
        await db.save_now()
    await update.callback_query.answer(f"{'⏹️ تم الإيقاف' if ok else '⚠️ ' + msg}")
    await cb_admin_procs(update, context)


async def cb_admin_stopall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    count = proc_mgr.stop_all()
    # تحديث حالة الملفات
    for hf in db.all_files():
        if hf.status == FileStatus.RUNNING.value:
            hf.status = FileStatus.STOPPED.value
            db.save_file(hf)
    db.add_audit(uid, "stop_all_procs", "", f"أُوقف {count} عملية")
    await db.save_now()
    await update.callback_query.answer(f"⏹️ أُوقف {count} عملية")
    await cb_admin_procs(update, context)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    💫 إدارة البريميوم                            ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    premium_users = [pu for pu in db.all_users() if pu.is_premium]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.PREM} <b>إدارة البريميوم ({len(premium_users)} مستخدم)</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    now = datetime.now(timezone.utc)
    expired_count = 0
    for pu in premium_users[:10]:
        expired = False
        until_str = "دائم"
        if pu.premium_until:
            try:
                until = datetime.fromisoformat(pu.premium_until.replace("Z", "+00:00"))
                if until < now:
                    expired = True
                    expired_count += 1
                    until_str = "منتهي"
                else:
                    days_left = (until - now).days
                    until_str = f"{days_left} يوم"
            except Exception:
                until_str = "غير معروف"

        icon = "⏰" if expired else "✅"
        name = html.escape(pu.first_name or pu.username or str(pu.user_id))
        text += (
            f"  {icon} <b>{name}</b>  <code>{pu.user_id}</code>\n"
            f"     الخطة: <code>{pu.premium_plan or 'N/A'}</code>  •  "
            f"المدة: <code>{until_str}</code>\n\n"
        )

    if expired_count > 0:
        text += f"\n{I.WARN} {expired_count} اشتراك منتهي — يمكن تنظيفها أدناه"

    rows = [
        [(f"{I.TOOLS} تنظيف المنتهية ({expired_count})", "promo_cleanup_expired")],
        [(f"{I.BACK} الإدارة", "admin_main")],
    ]
    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_premium_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.PREM} <b>البريميوم — المميزات الحصرية</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.OK} عمليات متزامنة: <code>{MAX_PROCESSES_PREMIUM}</code> (عادي: {MAX_PROCESSES_PER_USER})\n"
        f"  {I.OK} أولوية موافقة على الملفات\n"
        f"  {I.OK} لا حدود للتخزين\n"
        f"  {I.OK} إحصائيات تفصيلية متقدمة\n"
        f"  {I.OK} تقارير AI محسّنة\n"
        f"  {I.OK} جدولة عمليات متقدمة\n"
        f"  {I.OK} دعم فني مميز\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.GIFT} للحصول على البريميوم:\n"
        f"  • تواصل مع @{SUPPORT_USERNAME}\n"
        f"  • أو استخدم كود ترقية"
    )
    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.GIFT} أدخل كود", "redeem_code"),
                                  (f"{I.BACK} رجوع", "start")]]),
                            edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🎁 أكواد الترقية                              ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_promos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    promos = db.all_promos()
    text   = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.TAG} <b>أكواد الترقية ({len(promos)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    for p in promos[:10]:
        active_icon = "🟢" if p.is_active else "🔴"
        text += (
            f"  {active_icon} <code>{p.code}</code>\n"
            f"     الخطة: <code>{p.plan}</code>  •  الأيام: <code>{p.days}</code>\n"
            f"     الاستخدام: <code>{p.used_count}/{p.max_uses}</code>\n\n"
        )

    if not promos:
        text += f"{I.INFO} لا توجد أكواد بعد."

    rows = [
        [(f"{I.PLUS} إنشاء كود جديد", "promo_create")],
        [(f"{I.BACK} الإدارة", "admin_main")],
    ]
    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_promo_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    uid = update.effective_user.id
    u   = db.get_user(uid)

    if data == "promo_create":
        if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
            await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
            return
        # إنشاء كود تلقائي
        code   = secrets.token_hex(4).upper()
        promo  = PromoCode(
            code=code,
            plan="monthly",
            days=30,
            max_uses=5,
            created_by=uid,
        )
        db.save_promo(promo)
        db.add_audit(uid, "promo_create", code)
        await db.save_now()
        await update.callback_query.answer("✅ تم إنشاء الكود")
        await update.callback_query.edit_message_text(
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.OK} <b>تم إنشاء كود الترقية</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"  {I.TAG} الكود: <code>{code}</code>\n"
            f"  {I.CAL} الأيام: <code>30</code>\n"
            f"  {I.USERS} الحد الأقصى: <code>5</code> استخدامات",
            parse_mode=ParseMode.HTML,
            reply_markup=_kb([[(f"{I.BACK} الأكواد", "admin_promos")]])
        )

    elif data == "promo_cleanup_expired":
        now = datetime.now(timezone.utc)
        cleaned = 0
        for pu in db.all_users():
            if pu.is_premium and pu.premium_until:
                try:
                    until = datetime.fromisoformat(pu.premium_until.replace("Z", "+00:00"))
                    if until < now:
                        pu.is_premium    = False
                        pu.premium_until = None
                        pu.premium_plan  = ""
                        if pu.role == UserRole.PREMIUM.value:
                            pu.role = UserRole.USER.value
                        db.save_user(pu)
                        cleaned += 1
                except Exception:
                    pass
        await db.save_now()
        await update.callback_query.answer(f"✅ تم تنظيف {cleaned} اشتراك منتهي")
        await cb_admin_premium(update, context)


async def cb_redeem_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    context.user_data["waiting_promo_code"] = True
    await _answer_cb_or_msg(update,
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.GIFT} <b>استرداد كود ترقية</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"أرسل الكود الآن:",
        _kb([[(f"{I.BACK} رجوع", "start")]]),
    )


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📢 نظام البث المتقدم                          ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_broadcast_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    stats = db.global_stats()
    text  = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.BROAD} <b>نظام البث المتقدم</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.USERS} الكل: <code>{stats['total_users']}</code>\n"
        f"  {I.PREM} البريميوم: <code>{stats['premium_users']}</code>\n"
        f"  {I.OK} النشطون: <code>{stats['active_users']}</code>\n\n"
        f"اختر الفئة المستهدفة:"
    )
    rows = [
        [(f"{I.USERS} بث لكل المستخدمين",        "broadcast_all"),
         (f"{I.PREM} بث للبريميوم فقط",           "broadcast_premium")],
        [(f"{I.OK} بث للنشطين (7 أيام)",          "broadcast_active"),
         (f"{I.NEW} بث للجدد (24 ساعة)",          "broadcast_new")],
        [(f"{I.BACK} الإدارة",                     "admin_main")],
    ]
    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    target_map = {
        "broadcast_all":     "all",
        "broadcast_premium": "premium",
        "broadcast_active":  "active",
        "broadcast_new":     "new",
    }
    target = target_map.get(data, "all")
    context.user_data["broadcast_target"] = target
    context.user_data["waiting_broadcast"] = True

    target_labels = {
        "all":     "كل المستخدمين",
        "premium": "البريميوم فقط",
        "active":  "النشطين (7 أيام)",
        "new":     "الجدد (24 ساعة)",
    }
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.BROAD} <b>البث لـ: {target_labels[target]}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"أرسل الرسالة الآن (نص/صورة/ملف):\n\n"
        f"{I.INFO} يمكنك استخدام HTML للتنسيق",
        parse_mode=ParseMode.HTML,
        reply_markup=_kb([[(f"{I.BACK} إلغاء", "admin_broadcast")]])
    )


async def _execute_broadcast(
    bot,
    text: str,
    target: str,
    admin_id: int,
) -> Tuple[int, int]:
    all_users = db.all_users()
    now = datetime.now(timezone.utc)

    if target == "premium":
        targets = [u for u in all_users if u.is_premium and not u.is_banned]
    elif target == "active":
        targets = [u for u in all_users if not u.is_banned and
                   (now - datetime.fromisoformat(u.last_active.replace("Z","+00:00"))).days <= 7]
    elif target == "new":
        targets = [u for u in all_users if not u.is_banned and
                   (now - datetime.fromisoformat(u.joined_at.replace("Z","+00:00"))).total_seconds() <= 86400]
    else:
        targets = [u for u in all_users if not u.is_banned]

    sent = fail = 0
    for user in targets:
        if user.user_id == admin_id:
            continue
        if not user.notifications:
            continue
        result = await safe_send(bot, user.user_id, text, parse_mode=ParseMode.HTML)
        if result: sent += 1
        else: fail += 1
        await asyncio.sleep(0.05)

    rec = BroadcastRecord(
        admin_id=admin_id, message=text[:200], target=target,
        sent_count=sent, fail_count=fail,
        finished_at=datetime.now(timezone.utc).isoformat()
    )
    db._data.setdefault("broadcasts", []).append(asdict(rec))
    db.mark_dirty()
    await db.save_now()
    return sent, fail


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📊 الإحصائيات والنظام                         ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    stats   = db.global_stats()
    procs   = len(proc_mgr.get_all_running())
    disk    = FileManager.disk_usage()
    start_t = stats.get("start_time", "")
    uptime  = "غير معروف"
    with suppress(Exception):
        start = datetime.fromisoformat(start_t.replace("Z", "+00:00"))
        delta = datetime.now(timezone.utc) - start
        h, r  = divmod(int(delta.total_seconds()), 3600)
        m, s  = divmod(r, 60)
        uptime = f"{h}س {m}د {s}ث"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.CHART} <b>الإحصائيات الشاملة</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  ──────── المستخدمون ────────\n"
        f"  {I.USERS} الكل:      <code>{stats['total_users']:,}</code>\n"
        f"  {I.OK}   النشطون:   <code>{stats['active_users']:,}</code>\n"
        f"  {I.PREM} البريميوم: <code>{stats['premium_users']:,}</code>\n"
        f"  {I.ADMIN} الأدمنز:  <code>{stats['admin_count']:,}</code>\n"
        f"  {I.BAN}  المحظورون: <code>{stats['banned_users']:,}</code>\n\n"
        f"  ──────── الملفات ────────\n"
        f"  {I.FILE} الكل:      <code>{stats['total_files']:,}</code>\n"
        f"  {I.QUEUE} انتظار:   <code>{stats['pending_files']:,}</code>\n"
        f"  {I.OK}  مقبول:     <code>{stats['approved_files']:,}</code>\n"
        f"  {I.GREEN} نشط:     <code>{stats['running_files']:,}</code>\n\n"
        f"  ──────── النشاط ────────\n"
        f"  {I.UPLOAD} الرفعات: <code>{stats['total_uploads']:,}</code>\n"
        f"  {I.RUN}   التشغيل:  <code>{stats['total_runs']:,}</code>\n"
        f"  {I.GREEN} نشط الآن: <code>{procs}</code>\n\n"
        f"  ──────── النظام ────────\n"
        f"  {I.DISK} المساحة:  <code>{disk['human']}</code>\n"
        f"  {I.CLOCK} الوقت:   <code>{uptime}</code>\n"
        f"  {I.SERVER} الإصدار: <code>{BOT_VERSION}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.REFRESH} تحديث", "admin_stats"),
                                  (f"{I.BACK} الإدارة", "admin_main")]]),
                            edit=True)


async def cb_admin_system(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.SERVER} <b>موارد النظام</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    if HAS_PSUTIL:
        cpu_pct  = psutil.cpu_percent(interval=1)
        mem      = psutil.virtual_memory()
        disk     = psutil.disk_usage("/")
        net      = psutil.net_io_counters() if hasattr(psutil, "net_io_counters") else None
        cpu_bar  = Art.progress_bar(cpu_pct, 100, 20, "CPU")
        mem_bar  = Art.progress_bar(mem.percent, 100, 20, "RAM")
        disk_bar = Art.progress_bar(disk.percent, 100, 20, "قرص")

        text += (
            f"  {I.CPU} <b>المعالج:</b>\n"
            f"  <code>{cpu_bar}</code>  <code>{cpu_pct:.1f}%</code>\n\n"
            f"  {I.RAM} <b>الذاكرة:</b>\n"
            f"  <code>{mem_bar}</code>\n"
            f"  مستخدم: <code>{FileManager.human_size(mem.used)}</code>  "
            f"الكل: <code>{FileManager.human_size(mem.total)}</code>\n\n"
            f"  {I.DISK} <b>القرص:</b>\n"
            f"  <code>{disk_bar}</code>\n"
            f"  مستخدم: <code>{FileManager.human_size(disk.used)}</code>  "
            f"الكل: <code>{FileManager.human_size(disk.total)}</code>\n\n"
        )
        if net:
            text += (
                f"  {I.NET} <b>الشبكة:</b>\n"
                f"  {I.UPLOAD} أرسل: <code>{FileManager.human_size(net.bytes_sent)}</code>  "
                f"  {I.DOWNLOAD} استقبل: <code>{FileManager.human_size(net.bytes_recv)}</code>\n\n"
            )
    else:
        text += f"  {I.WARN} psutil غير متوفر — تثبيت المتطلبات مطلوب\n\n"

    text += (
        f"  ──────── معلومات البوت ────────\n"
        f"  {I.SERVER} النظام:  <code>{platform.system()} {platform.release()}</code>\n"
        f"  {I.CODE} Python:  <code>{sys.version.split()[0]}</code>\n"
        f"  {I.BOT} الإصدار: <code>{BOT_VERSION}</code>\n"
        f"  {I.GREEN} العمليات: <code>{len(proc_mgr.get_all_running())}</code> نشطة\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.REFRESH} تحديث", "admin_system"),
                                  (f"{I.BACK} الإدارة", "admin_main")]]),
                            edit=True)


async def cb_my_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u:
        return

    files    = db.user_files(uid)
    running  = proc_mgr.count_user(uid)
    approved = sum(1 for f in files if f.status in (FileStatus.APPROVED.value, FileStatus.RUNNING.value))

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.STATS} <b>إحصائياتك الشخصية</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.POINTS} النقاط: <code>{u.points:,}</code>\n"
        f"  {I.TROPHY} الإحالات: <code>{u.invites}</code>\n"
        f"  {I.CHART} streak: <code>{u.login_streak}</code> يوم\n\n"
        f"  ──────── الملفات ────────\n"
        f"  {I.FILE} الكل: <code>{len(files)}</code>\n"
        f"  {I.OK}  مقبول: <code>{approved}</code>\n"
        f"  {I.GREEN} نشط الآن: <code>{running}</code>\n"
        f"  {I.RUN} إجمالي تشغيل: <code>{u.run_count:,}</code>\n"
        f"  {I.DISK} إجمالي التخزين: <code>{FileManager.human_size(u.total_storage)}</code>\n\n"
        f"  ──────── المستوى ────────\n"
    )

    # نظام المستويات
    levels = [
        (0,    "🥉 مبتدئ"),
        (100,  "🥈 متوسط"),
        (500,  "🥇 متقدم"),
        (1000, "💎 خبير"),
        (5000, "👑 أسطورة"),
    ]
    current_level = levels[0][1]
    for threshold, name in reversed(levels):
        if u.points >= threshold:
            current_level = name
            break

    text += (
        f"  المستوى: <b>{current_level}</b>\n"
        f"  النقاط: <code>{u.points:,}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.HOME} الرئيسية", "start")]]),
                            edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🏆 المتصدرون                                  ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    sort_options = ["points", "files", "runs", "invites"]
    per_page = 10
    sort_by  = sort_options[page % len(sort_options)] if page > 3 else "points"

    # أبسط: page 0-3 للترتيب، نستخدم رقم مختلف للصفحات الفعلية
    leaders = db.leaderboard(sort_by="points", limit=20)
    uid = update.effective_user.id
    my_rank = next((i+1 for i, u in enumerate(leaders) if u.user_id == uid), None)

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.TROPHY} <b>لوحة المتصدرين — النقاط</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    medals = ["🥇", "🥈", "🥉"] + [f"{i}." for i in range(4, 21)]
    for i, leader in enumerate(leaders[:15]):
        is_me = "◀️ أنت" if leader.user_id == uid else ""
        name  = html.escape(leader.first_name or leader.username or str(leader.user_id))
        badge = "💫" if leader.is_premium else ""
        text += (
            f"{medals[i]} {badge}<b>{name}</b>  {is_me}\n"
            f"   {I.POINTS} <code>{leader.points:,}</code>  •  "
            f"{I.FILE} {leader.file_count}  •  "
            f"{I.RUN} {leader.run_count}\n\n"
        )

    if my_rank:
        text += f"\n{I.USER} ترتيبك: <b>#{my_rank}</b>"

    text += f"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    await _answer_cb_or_msg(update, text,
                            _kb([
                                [(f"{I.CHART} ترتيب الملفات",    "leaderboard_1"),
                                 (f"{I.RUN} ترتيب التشغيل",       "leaderboard_2")],
                                [(f"{I.REFRESH} تحديث",            "leaderboard_0"),
                                 (f"{I.HOME} الرئيسية",            "start")],
                            ]),
                            edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    💾 النسخ الاحتياطي                            ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_backup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    backups = db.list_backups()
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.BACKUP} <b>النسخ الاحتياطية ({len(backups)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    for b in backups[:5]:
        size = 0
        with suppress(OSError):
            size = os.path.getsize(os.path.join(BACKUP_DIR, b))
        text += f"  {I.FILE} <code>{b}</code>  ({FileManager.human_size(size)})\n"

    if not backups:
        text += f"{I.INFO} لا توجد نسخ احتياطية."

    rows = [
        [(f"{I.BACKUP} إنشاء نسخة الآن",         "backup_create"),
         (f"{I.DOWNLOAD} تحميل آخر نسخة",         "backup_download")],
        [(f"{I.BACK} الإدارة",                     "admin_main")],
    ]
    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_backup_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    if data == "backup_create":
        await update.callback_query.answer("⏳ جاري الإنشاء...")
        path = db.create_backup()
        db.add_audit(uid, "backup_create", path)
        await db.save_now()
        await update.callback_query.message.reply_text(
            f"{I.OK} <b>تم إنشاء النسخة الاحتياطية</b>\n"
            f"<code>{os.path.basename(path)}</code>",
            parse_mode=ParseMode.HTML
        )
        await cb_admin_backup(update, context)

    elif data == "backup_download":
        backups = db.list_backups()
        if not backups:
            await update.callback_query.answer("❌ لا توجد نسخ احتياطية", show_alert=True)
            return
        path = os.path.join(BACKUP_DIR, backups[0])
        await update.callback_query.answer("⏳ جاري الإرسال...")
        try:
            await update.callback_query.message.reply_document(
                document=InputFile(path, filename=os.path.basename(path)),
                caption=f"{I.BACKUP} <b>النسخة الاحتياطية الأخيرة</b>",
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            await update.callback_query.message.reply_text(
                f"{I.FAIL} فشل الإرسال: {e}"
            )


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ⚙️ الإعدادات                                  ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    maintenance   = db.get_setting("maintenance_mode",    False)
    registration  = db.get_setting("registration_open",   True)
    approval      = db.get_setting("require_approval",    True)
    ai_analysis   = db.get_setting("ai_analysis_enabled", True)
    auto_install  = db.get_setting("auto_install_libs",   True)
    rate_limit    = db.get_setting("rate_limit_enabled",  True)

    def tog(v): return "🟢 مفعّل" if v else "🔴 معطّل"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.SETTINGS} <b>إعدادات البوت</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.WARN}  وضع الصيانة:      {tog(maintenance)}\n"
        f"  {I.USERS} التسجيل مفتوح:    {tog(registration)}\n"
        f"  {I.QUEUE} الموافقة مطلوبة:  {tog(approval)}\n"
        f"  {I.AI}   تحليل الذكاء:      {tog(ai_analysis)}\n"
        f"  {I.TOOLS} تثبيت تلقائي:     {tog(auto_install)}\n"
        f"  {I.SHIELD} Rate Limiting:   {tog(rate_limit)}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

    rows = [
        [(f"{'🔴 وضع صيانة' if maintenance else '🟢 وضع صيانة'}",
          "setting_toggle_maintenance_mode")],
        [(f"{'🔴 إيقاف التسجيل' if registration else '🟢 فتح التسجيل'}",
          "setting_toggle_registration_open")],
        [(f"{'🔴 إلغاء الموافقة اليدوية' if approval else '🟢 تفعيل الموافقة اليدوية'}",
          "setting_toggle_require_approval")],
        [(f"{'🔴 إيقاف AI' if ai_analysis else '🟢 تفعيل AI'}",
          "setting_toggle_ai_analysis_enabled")],
        [(f"{'🔴 إيقاف التثبيت التلقائي' if auto_install else '🟢 تفعيل التثبيت التلقائي'}",
          "setting_toggle_auto_install_libs")],
        [(f"{'🔴 إيقاف Rate Limit' if rate_limit else '🟢 تفعيل Rate Limit'}",
          "setting_toggle_rate_limit_enabled")],
        [(f"{I.BACK} الإدارة", "admin_main")],
    ]

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_setting_toggle(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    current = db.get_setting(key, False)
    db.set_setting(key, not current)
    db.add_audit(uid, "toggle_setting", key, f"{current} → {not current}")
    await db.save_now()
    await update.callback_query.answer(f"✅ تم التغيير: {key}")
    await cb_admin_settings(update, context)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📤 تصدير البوت ZIP                            ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_export_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    await update.callback_query.answer("⏳ جاري الإنشاء...")
    msg = await update.callback_query.message.reply_text(
        f"{I.EXPORT} <b>جاري تجهيز ملف ZIP...</b>",
        parse_mode=ParseMode.HTML
    )

    try:
        zip_path = FileManager.create_export_zip(include_db=False)
        db.add_audit(uid, "export_bot_zip", zip_path)
        await db.save_now()
        await safe_edit(msg, f"{I.OK} <b>تم! جاري الإرسال...</b>", parse_mode=ParseMode.HTML)
        await update.callback_query.message.reply_document(
            document=InputFile(zip_path, filename="pyhost_pro_ultra.zip"),
            caption=(
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"{I.FIRE} <b>PyHost PRO ULTRA v{BOT_VERSION}</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"  {I.FILE} bot.py\n"
                f"  {I.FILE} requirements.txt\n"
                f"  {I.FILE} .env.example\n"
                f"  {I.FILE} README.md\n\n"
                f"  التشغيل:\n"
                f"  <code>pip install -r requirements.txt</code>\n"
                f"  <code>python bot.py</code>"
            ),
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        await safe_edit(msg,
                        f"{I.FAIL} فشل التصدير: <code>{html.escape(str(e))}</code>",
                        parse_mode=ParseMode.HTML)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📋 سجل التدقيق                                ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_admin_audit(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await update.callback_query.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    entries = db.recent_audit(100)
    per     = 8
    total_p = max(1, math.ceil(len(entries) / per))
    page    = max(0, min(page, total_p - 1))
    chunk   = entries[page*per:(page+1)*per]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.LOG} <b>سجل التدقيق ({len(entries)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    for e in chunk:
        actor = db.get_user(e.actor_id)
        name  = (actor.first_name or str(e.actor_id)) if actor else str(e.actor_id)
        ts    = e.timestamp[:16].replace("T", " ")
        target_str = f" → {e.target}" if e.target else ""
        detail_str = f"\n   {e.details}" if e.details else ""
        text += (
            f"  {I.CLOCK} <code>{ts}</code>\n"
            f"  {I.USER} {html.escape(name)}  {I.TAG} <code>{e.action}</code>"
            f"{html.escape(target_str)}{html.escape(detail_str)}\n\n"
        )

    if not entries:
        text += f"{I.INFO} لا توجد سجلات."

    text += f"━ صفحة {page+1}/{total_p} ━━━━━━━━━━━━━━━━━━━━━━━━━"
    nav = []
    if page > 0: nav.append((f"{I.PREV}", f"admin_audit_{page-1}"))
    if page < total_p - 1: nav.append((f"{I.NEXT}", f"admin_audit_{page+1}"))
    rows = [nav] if nav else []
    rows.append([(f"{I.REFRESH} تحديث", f"admin_audit_{page}"),
                 (f"{I.BACK} الإدارة",  "admin_main")])

    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📝 إعداداتي الشخصية                           ║
# ╚══════════════════════════════════════════════════════════════════╝

async def cb_my_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u: return

    notif_icon = "🔔 مفعّلة" if u.notifications else "🔕 معطّلة"
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.SETTINGS} <b>إعداداتي</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.BELL} الإشعارات: {notif_icon}\n"
        f"  {I.LINK} رمز الإحالة: <code>{u.referral_code}</code>\n"
        f"  {I.COPY} ID: <code>{u.user_id}</code>\n"
    )

    rows = [
        [(f"{'🔕 إيقاف الإشعارات' if u.notifications else '🔔 تفعيل الإشعارات'}",
          "toggle_my_notifs")],
        [(f"{I.HOME} الرئيسية", "start")],
    ]
    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_my_referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u   = db.get_user(uid)
    if not u: return

    bot_username = context.bot.username or "bot"
    ref_link = f"https://t.me/{bot_username}?start={u.referral_code}"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.LINK} <b>نظام الإحالة</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  رمزك: <code>{u.referral_code}</code>\n"
        f"  رابطك:\n"
        f"  <code>{ref_link}</code>\n\n"
        f"  {I.TROPHY} إحالاتك: <code>{u.invites}</code>\n"
        f"  {I.POINTS} +25 نقطة لكل إحالة ناجحة\n\n"
        f"  شارك الرابط مع أصدقائك!"
    )
    await _answer_cb_or_msg(update, text, _kb([[(f"{I.HOME} الرئيسية", "start")]]), edit=True)


async def cb_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.MSG} <b>الدعم الفني</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  {I.USER} للتواصل: @{SUPPORT_USERNAME}\n\n"
        f"  {I.LIGHT} قبل التواصل تأكد من:\n"
        f"  • قراءة دليل الاستخدام /help\n"
        f"  • إرسال تفاصيل المشكلة بوضوح\n"
        f"  • إرفاق رقم معرف الملف إن وجد"
    )
    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.BACK} رجوع", "start")]]),
                            edit=True)


async def cb_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.FIRE} <b>{BOT_NAME}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"  الإصدار: <code>{BOT_VERSION}</code>\n\n"
        f"  {I.OK} استضافة Python + ZIP\n"
        f"  {I.OK} موافقة يدوية على الملفات\n"
        f"  {I.OK} تحليل ذكاء اصطناعي\n"
        f"  {I.OK} لوحة إدارة متكاملة\n"
        f"  {I.OK} نظام بريميوم\n"
        f"  {I.OK} متصدرون ونقاط\n"
        f"  {I.OK} بث متقدم\n"
        f"  {I.OK} نسخ احتياطي تلقائي\n"
        f"  {I.OK} يعمل على أي سيرفر\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.HOME} الرئيسية", "start")]]),
                            edit=True)


async def cb_my_procs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid   = update.effective_user.id
    procs = [rp for rp in proc_mgr.get_all_running() if rp.user_id == uid]

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.GREEN} <b>عملياتي النشطة ({len(procs)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    if not procs:
        text += f"{I.INFO} لا توجد عمليات نشطة حالياً."
    else:
        for i, rp in enumerate(procs, 1):
            stats = proc_mgr.process_stats(rp.file_id)
            text += (
                f"{i}. {I.GREEN} <b>{html.escape(rp.file_name)}</b>\n"
                f"   PID: <code>{rp.pid}</code>  •  "
                f"CPU: <code>{stats.get('cpu',0):.1f}%</code>  •  "
                f"مدة: <code>{stats.get('uptime','?')}</code>\n\n"
            )

    rows = []
    for rp in procs:
        rows.append([
            (f"{I.LOG} سجل {rp.file_name[:15]}", f"file_log_{rp.file_id}"),
            (f"{I.STOP} إيقاف",                  f"file_stop_{rp.file_id}"),
        ])
    rows.append([(f"{I.REFRESH} تحديث", "my_procs"), (f"{I.HOME} الرئيسية", "start")])
    await _answer_cb_or_msg(update, text, _kb(rows), edit=True)


async def cb_my_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid   = update.effective_user.id
    tasks = db.user_tasks(uid)

    text = (
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{I.SCHED} <b>مهامي المجدولة ({len(tasks)})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    if not tasks:
        text += (
            f"{I.INFO} لا توجد مهام مجدولة.\n\n"
            f"{I.LIGHT} لجدولة ملف:\n"
            f"  اذهب لملف → تفاصيل → جدولة تشغيل"
        )
    else:
        for i, t in enumerate(tasks[:10], 1):
            hf    = db.get_file(t.file_id)
            fname = hf.original_name if hf else t.file_id
            icon  = "🟢" if t.is_active else "🔴"
            text += (
                f"{i}. {icon} <code>{html.escape(fname[:25])}</code>\n"
                f"   التشغيل: <code>{t.run_at[:16]}</code>  •  "
                f"التكرار: <code>{t.repeat}</code>\n\n"
            )

    await _answer_cb_or_msg(update, text,
                            _kb([[(f"{I.HOME} الرئيسية", "start")]]),
                            edit=True)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    📩 معالجات النصوص (الحالات)                   ║
# ╚══════════════════════════════════════════════════════════════════╝

@rate_limited
@require_not_banned
async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة الرسائل النصية للحالات المختلفة"""
    msg  = update.message
    text = msg.text or ""
    uid  = update.effective_user.id

    # ─── كود بريميوم ──────────────────────────────────────────────
    if context.user_data.pop("waiting_promo_code", False):
        code  = text.strip().upper()
        promo = db.get_promo(code)
        u     = db.get_user(uid)

        if not promo:
            await msg.reply_text(
                f"{I.FAIL} الكود غير موجود أو غير صحيح.",
                reply_markup=_kb([[(f"{I.HOME} الرئيسية", "start")]])
            )
            return
        if not promo.is_active:
            await msg.reply_text(
                f"{I.FAIL} هذا الكود غير فعّال.",
                reply_markup=_kb([[(f"{I.HOME} الرئيسية", "start")]])
            )
            return
        if promo.used_count >= promo.max_uses:
            await msg.reply_text(
                f"{I.FAIL} انتهت استخدامات هذا الكود.",
                reply_markup=_kb([[(f"{I.HOME} الرئيسية", "start")]])
            )
            return
        if uid in promo.used_by:
            await msg.reply_text(
                f"{I.FAIL} لقد استخدمت هذا الكود من قبل.",
                reply_markup=_kb([[(f"{I.HOME} الرئيسية", "start")]])
            )
            return
        if promo.expires_at:
            with suppress(Exception):
                exp = datetime.fromisoformat(promo.expires_at.replace("Z", "+00:00"))
                if datetime.now(timezone.utc) > exp:
                    await msg.reply_text(
                        f"{I.FAIL} انتهت صلاحية هذا الكود.",
                        reply_markup=_kb([[(f"{I.HOME} الرئيسية", "start")]])
                    )
                    return

        # تطبيق الكود
        promo.used_count += 1
        promo.used_by.append(uid)
        db.save_promo(promo)

        if u:
            u.is_premium = True
            until = datetime.now(timezone.utc) + timedelta(days=promo.days)
            u.premium_until = until.isoformat()
            u.premium_plan  = promo.plan
            if u.role == UserRole.USER.value:
                u.role = UserRole.PREMIUM.value
            u.promo_codes_used.append(code)
            u.points += 30
            db.save_user(u)

        db.add_audit(uid, "redeem_promo", code)
        await db.save_now()

        await msg.reply_text(
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.OK} <b>تم تفعيل الكود بنجاح!</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  الكود: <code>{code}</code>\n"
            f"  المدة: <code>{promo.days}</code> يوم\n"
            f"  +30 نقطة هدية! {I.GIFT}",
            parse_mode=ParseMode.HTML,
            reply_markup=_kb([[(f"{I.HOME} الرئيسية", "start")]])
        )
        return

    # ─── بث رسالة ──────────────────────────────────────────────────
    if context.user_data.get("waiting_broadcast"):
        target = context.user_data.pop("broadcast_target", "all")
        context.user_data.pop("waiting_broadcast", None)

        u = db.get_user(uid)
        if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
            await msg.reply_text(f"{I.LOCK} ليس لديك صلاحية.")
            return

        wait = await msg.reply_text(f"{I.BROAD} <b>جاري الإرسال...</b>", parse_mode=ParseMode.HTML)
        sent, fail = await _execute_broadcast(context.bot, text, target, uid)
        db.add_audit(uid, "broadcast", target, f"أُرسل:{sent} فشل:{fail}")
        await safe_edit(
            wait,
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.OK} <b>اكتمل البث</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  {I.OK} أُرسل: <code>{sent}</code>\n"
            f"  {I.FAIL} فشل: <code>{fail}</code>",
            parse_mode=ParseMode.HTML
        )
        return

    # ─── إضافة نقاط ────────────────────────────────────────────────
    target_uid = context.user_data.pop("add_pts_target", None)
    if target_uid and text.strip().isdigit():
        u = db.get_user(uid)
        if u and u.role in (UserRole.ADMIN.value, UserRole.OWNER.value):
            pts    = int(text.strip())
            target = db.get_user(target_uid)
            if target:
                target.points += pts
                db.save_user(target)
                db.add_audit(uid, "add_points", str(target_uid), f"+{pts}")
                await db.save_now()
                await msg.reply_text(
                    f"{I.OK} <b>تم إضافة {pts} نقطة للمستخدم {target_uid}</b>",
                    parse_mode=ParseMode.HTML
                )
        return

    # ─── رد افتراضي ────────────────────────────────────────────────
    await msg.reply_text(
        f"{I.LIGHT} استخدم /start للقائمة الرئيسية\n"
        f"أو أرسل ملف .py/.zip مباشرةً"
    )


# ─── معالج reject_exec الجديد ─────────────────────────────────────
async def handle_reject_exec(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة ضغط زر رفض الملف مع سبب جاهز"""
    q    = update.callback_query
    data = q.data or ""
    if not data.startswith("reject_exec_"):
        return

    uid = q.from_user.id
    u   = db.get_user(uid)
    if not u or u.role not in (UserRole.ADMIN.value, UserRole.OWNER.value):
        await q.answer("❌ ليس لديك صلاحية", show_alert=True)
        return

    parts = data.split("_", 4)
    # reject_exec_{file_id}_{reason}
    if len(parts) < 5:
        await q.answer("❌ بيانات غير صحيحة")
        return

    file_id = parts[2]
    reason  = parts[4].replace("_", " ")
    await _execute_reject(update, context, file_id, reason)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🔔 نظام الإشعارات والمهام المجدولة            ║
# ╚══════════════════════════════════════════════════════════════════╝

async def job_auto_backup(context: ContextTypes.DEFAULT_TYPE):
    """نسخ احتياطي تلقائي دوري"""
    try:
        path = db.create_backup()
        logger.info(f"✅ نسخة احتياطية تلقائية: {os.path.basename(path)}")
        # حذف النسخ القديمة (أبقِ آخر 10)
        backups = db.list_backups()
        for old in backups[10:]:
            with suppress(OSError):
                os.remove(os.path.join(BACKUP_DIR, old))
    except Exception as e:
        logger.error(f"خطأ في النسخ الاحتياطي التلقائي: {e}")


async def job_check_premium_expiry(context: ContextTypes.DEFAULT_TYPE):
    """فحص انتهاء اشتراكات البريميوم"""
    now = datetime.now(timezone.utc)
    expired = []
    for u in db.all_users():
        if u.is_premium and u.premium_until:
            with suppress(Exception):
                until = datetime.fromisoformat(u.premium_until.replace("Z", "+00:00"))
                if until < now:
                    u.is_premium    = False
                    u.premium_until = None
                    u.premium_plan  = ""
                    if u.role == UserRole.PREMIUM.value:
                        u.role = UserRole.USER.value
                    db.save_user(u)
                    expired.append(u.user_id)
                elif (until - now).total_seconds() < 86400:  # 24 ساعة قبل الانتهاء
                    await safe_send(
                        context.bot, u.user_id,
                        f"{I.WARN} <b>تنبيه:</b> اشتراكك البريميوم سينتهي خلال 24 ساعة!",
                        parse_mode=ParseMode.HTML
                    )

    if expired:
        await db.save_now()
        for uid in expired:
            await safe_send(
                context.bot, uid,
                f"{I.INFO} <b>انتهى اشتراكك البريميوم.</b>\n"
                f"تواصل مع @{SUPPORT_USERNAME} للتجديد.",
                parse_mode=ParseMode.HTML
            )


async def job_save_db(context: ContextTypes.DEFAULT_TYPE):
    """حفظ دوري لقاعدة البيانات"""
    await db.save()


async def job_check_running_processes(context: ContextTypes.DEFAULT_TYPE):
    """فحص العمليات المنتهية وتحديث حالتها"""
    for file_id, rp in list(proc_mgr._processes.items()):
        if rp.process and rp.process.poll() is not None:
            hf = db.get_file(file_id)
            if hf and hf.status == FileStatus.RUNNING.value:
                exit_code = rp.process.returncode
                hf.status = FileStatus.STOPPED.value if exit_code == 0 else FileStatus.ERROR.value
                db.save_file(hf)
                # إشعار صاحب الملف
                owner = db.get_user(rp.user_id)
                if owner and owner.notifications:
                    icon = I.STOP if exit_code == 0 else I.FAIL
                    await safe_send(
                        context.bot, rp.user_id,
                        f"{icon} <b>انتهت عملية: {html.escape(rp.file_name)}</b>\n"
                        f"كود الخروج: <code>{exit_code}</code>",
                        parse_mode=ParseMode.HTML
                    )
    await db.save()


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🚀 تهيئة وتشغيل البوت                         ║
# ╚══════════════════════════════════════════════════════════════════╝

async def post_init(application: Application):
    """تهيئة ما بعد بدء التشغيل"""
    # إعداد أوامر البوت
    commands = [
        BotCommand("start",  "القائمة الرئيسية"),
        BotCommand("help",   "دليل الاستخدام"),
        BotCommand("admin",  "لوحة الإدارة"),
        BotCommand("upload", "رفع ملف جديد"),
        BotCommand("files",  "ملفاتي"),
        BotCommand("procs",  "عملياتي النشطة"),
        BotCommand("stats",  "إحصائياتي"),
        BotCommand("top",    "لوحة المتصدرين"),
        BotCommand("redeem", "استرداد كود ترقية"),
    ]
    await application.bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    # إنشاء مستخدمي الأدمن
    for aid in ADMIN_IDS:
        role = UserRole.OWNER.value if aid == ADMIN_IDS[0] else UserRole.ADMIN.value
        u, _ = db.get_or_create_user(aid, role=role)
        if u.role != role:
            u.role = role
            u.admin_perms = [AdminPermission.FULL_ACCESS.value]
            db.save_user(u)

    await db.save_now()
    logger.info(
        f"\n{'='*60}\n"
        f"  {BOT_NAME} v{BOT_VERSION}\n"
        f"  الأدمنز: {ADMIN_IDS}\n"
        f"  قاعدة البيانات: {DATABASE_FILE}\n"
        f"  الملفات: {FILES_DIR}\n"
        f"{'='*60}"
    )

    # إشعار الأدمن بالبدء
    for aid in ADMIN_IDS:
        await safe_send(
            application.bot, aid,
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{I.ROCKET} <b>البوت بدأ التشغيل!</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  الإصدار: <code>{BOT_VERSION}</code>\n"
            f"  الوقت: <code>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</code>",
            parse_mode=ParseMode.HTML
        )


def build_application() -> Application:
    """بناء تطبيق البوت مع كل المعالجات"""
    if BOT_TOKEN in ("ضع_توكن_البوت_هنا", "", "YOUR_TOKEN_HERE"):
        logger.critical("❌ BOT_TOKEN غير مضبوط! عدّل ملف .env أو متغير البيئة")
        sys.exit(1)

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .concurrent_updates(True)
        .build()
    )

    # ─── الأوامر ────────────────────────────────────────────────
    app.add_handler(CommandHandler("start",  cmd_start))
    app.add_handler(CommandHandler("help",   cmd_help))
    app.add_handler(CommandHandler("admin",  cmd_admin))
    app.add_handler(CommandHandler("upload", lambda u,c: _answer_cb_or_msg(u, f"{I.UPLOAD} أرسل ملف .py أو .zip مباشرةً")))
    app.add_handler(CommandHandler("files",  lambda u,c: cb_my_files(u, c, 0)))
    app.add_handler(CommandHandler("procs",  cb_my_procs))
    app.add_handler(CommandHandler("stats",  cb_my_stats))
    app.add_handler(CommandHandler("top",    lambda u,c: cb_leaderboard(u, c, 0)))
    app.add_handler(CommandHandler("redeem", cb_redeem_code))

    # ─── Callbacks ──────────────────────────────────────────────
    # reject_exec يجب أن يكون قبل callback_handler العام
    app.add_handler(CallbackQueryHandler(
        handle_reject_exec,
        pattern="^reject_exec_"
    ))
    app.add_handler(CallbackQueryHandler(
        lambda u, c: cb_user_reset_points(u, c, int(u.callback_query.data.split("_")[-1])),
        pattern="^user_reset_pts_"
    ))
    app.add_handler(CallbackQueryHandler(
        lambda u, c: cb_setting_toggle(u, c, u.callback_query.data[len("setting_toggle_"):]),
        pattern="^setting_toggle_"
    ))
    app.add_handler(CallbackQueryHandler(callback_handler))

    # ─── الرسائل ────────────────────────────────────────────────
    app.add_handler(MessageHandler(
        filters.Document.ALL,
        handle_file_upload
    ))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_text_message
    ))

    # ─── المهام المجدولة ────────────────────────────────────────
    jq = app.job_queue
    if jq:
        jq.run_repeating(job_save_db,                  interval=60,          first=30)
        jq.run_repeating(job_auto_backup,              interval=AUTO_BACKUP_INTERVAL_HOURS*3600, first=300)
        jq.run_repeating(job_check_premium_expiry,     interval=3600,         first=120)
        jq.run_repeating(job_check_running_processes,  interval=30,           first=30)

    return app


def main():
    """نقطة الدخول الرئيسية"""
    print(f"""
╔══════════════════════════════════════════════════════════╗
║  🔥 {BOT_NAME} v{BOT_VERSION}  ║
╠══════════════════════════════════════════════════════════╣
║  BOT_TOKEN: {'✅ مضبوط' if BOT_TOKEN not in ('ضع_توكن_البوت_هنا', '', 'YOUR_TOKEN_HERE') else '❌ غير مضبوط!'}
║  ADMIN_IDS: {ADMIN_IDS}
║  DATABASE:  {DATABASE_FILE}
╚══════════════════════════════════════════════════════════╝
""")

    app = build_application()

    logger.info(f"🚀 تشغيل {BOT_NAME} v{BOT_VERSION}")
    app.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
    )


if __name__ == "__main__":
    main()
