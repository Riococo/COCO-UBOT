# ram - UserBot
# Copyright (c) 2022 ram-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/ram-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import MAN2, MAN3, MAN4, MAN5, bot, branch

MSG_ON = """
🔥 **ram-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
➠ **Managed By** {}
━━
"""
try:
    user = bot.get_me()
    mention = f"[{user.first_name}](tg://user?id={user.id})"
except BaseException:
    pass


async def ram_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"🔥 **ram-Userbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{version}@{branch}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
                )
    except BaseException:
        pass
    try:
        if MAN2:
            if BOTLOG_CHATID != 0:
                await MAN2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if MAN3:
            if BOTLOG_CHATID != 0:
                await MAN3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if MAN4:
            if BOTLOG_CHATID != 0:
                await MAN4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if MAN5:
            if BOTLOG_CHATID != 0:
                await MAN5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
