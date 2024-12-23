from telethon import TelegramClient, events
import os
from datetime import datetime

api_id = '' # app id
api_hash = '' # app hash

client = TelegramClient('session_name', api_id, api_hash, system_version="4.16.30-vxCUSTOM")

MAX_FILE_SIZE_MB = 200 # enter a file download limit, now if it exceeds more than 200 MB, it will not download the file.
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

def create_user_folder(base_path, subfolder, user_id):
    folder_path = os.path.join(base_path, subfolder, str(user_id))
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def log_message_html(log_file_path, log_content):
    try:
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(log_content)
    except Exception as e:
        print(f"Error writing log: {e}")

async def format_message_html(from_user, username, message, current_time, current_time_save, direction='incoming'):
    caption = message.text or ""
    formatted_message = ""
    current_directory = os.path.dirname(os.path.abspath(__file__))

    if username:
        user_folder_name = f"{from_user.id} ({username})"
    else:
        user_folder_name = str(from_user.id)

    user_directory = os.path.join(current_directory, 'logs', user_folder_name)

    photo_folder = os.path.join(user_directory, 'photos')
    media_folder = os.path.join(user_directory, 'media')
    sticker_folder = os.path.join(user_directory, 'stickers')

    os.makedirs(photo_folder, exist_ok=True)
    os.makedirs(media_folder, exist_ok=True)
    os.makedirs(sticker_folder, exist_ok=True)

    if direction == 'incoming':
        formatted_message += f"<div class='message incoming' style='word-wrap: break-word; overflow-wrap: break-word; max-width: 70%;'>"
        if message.photo:
            await message.download_media(file=os.path.join(photo_folder, f'{current_time_save}_{message.file.name}.jpg'))
            formatted_message += f"<p class='message-type'><strong>📩 Incoming Photo</strong></p><div class='user-info'>"
            formatted_message += f"<p>👤 From: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📂 File path: <a href='{f"photos/{current_time_save}_{message.file.name}.jpg"}' target='_blank'>{f"photos/{current_time_save}_{message.file.name}.jpg"}</a></p>"
            formatted_message += f"<p>📅 Date: {current_time}</p></div>"
            formatted_message += f"""
            <div style="text-align: center; margin: 10px 0;">
                <img src='{f"photos/{current_time_save}_{message.file.name}.jpg"}' alt='Incoming Photo' style='max-width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);'>
            </div>
            """
            formatted_message += f"<p>📝 Caption: {caption}</p>"
        elif message.sticker:
            await message.download_media(file=os.path.join(sticker_folder, f'{current_time_save}_{message.file.name}'))
            formatted_message += f"<p class='message-type'><strong>📩 Incoming Sticker</strong></p><div class='user-info'>"
            formatted_message += f"<p>👤 From: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📂 File path: <a href='{f"stickers/{current_time_save}_{message.file.name}"}' target='_blank'>{f"stickers/{current_time_save}_{message.file.name}"}</a></p>"
            formatted_message += f"<p>📅 Date: {current_time}</p></div>"
        elif message.audio or message.video or message.gif or message.file:
            if message.file.size > MAX_FILE_SIZE_BYTES:
                formatted_message += f"<p class='message-type'><strong>📩 Incoming Media (too large)</strong></p><div class='user-info'>"
                formatted_message += f"<p>👤 From: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📅 Date: {current_time}</p></div>"
                formatted_message += f"<p>📝 File size exceeds {MAX_FILE_SIZE_MB} MB, not downloading.</p>"
            else:
                await message.download_media(file=os.path.join(media_folder, f'{current_time_save}_{message.file.name}'))
                formatted_message += f"<p class='message-type'><strong>📩 Incoming Media</strong></p><div class='user-info'>"
                formatted_message += f"<p>👤 From: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📂 Media type: {message.file.mime_type}</p>"
                formatted_message += f"<p>📂 File path: <a href='{f"media/{current_time_save}_{message.file.name}"}' target='_blank'>{f"media/{current_time_save}_{message.file.name}"}</a></p><p>📅 Date: {current_time}</p></div>"
                formatted_message += f"<p>📝 Caption: {caption}</p>"
        else:
            formatted_message += f"<p class='message-type'><strong>📩 Incoming Text</strong></p><div class='user-info'>"
            formatted_message += f"<p>👤 From: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📅 Date: {current_time}</p></div>"
            formatted_message += f"<p>📝 Message: {caption}</p>"
        formatted_message += "</div>"

    else:
        formatted_message += f"<div class='message outgoing' style='word-wrap: break-word; overflow-wrap: break-word; max-width: 70%; margin-left: 30%;'>"
        if message.photo:
            await message.download_media(file=os.path.join(photo_folder, f'{current_time_save}_{message.file.name}.jpg'))
            formatted_message += f"<p class='message-type'><strong>📤 Outgoing Photo</strong></p><div class='user-info'>"
            formatted_message += f"<p>👤 To: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📂 File path: <a href='{f"photos/{current_time_save}_{message.file.name}.jpg"}' target='_blank'>{f"photos/{current_time_save}_{message.file.name}.jpg"}</a></p>"
            formatted_message += f"<p>📅 Date: {current_time}</p></div>"
            formatted_message += f"""
            <div style="text-align: center; margin: 10px 0;">
                <img src='{f"photos/{current_time_save}_{message.file.name}.jpg"}' alt='Outgoing Photo' style='max-width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);'>
            </div>
            """
            formatted_message += f"<p>📝 Caption: {caption}</p>"
        elif message.sticker:
            await message.download_media(file=os.path.join(sticker_folder, f'{current_time_save}_{message.file.name}'))
            formatted_message += f"<p class='message-type'><strong>📤 Outgoing Sticker</strong></p><div class='user-info'>"
            formatted_message += f"<p>👤 To: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📂 File path: <a href='{f"stickers/{current_time_save}_{message.file.name}"}' target='_blank'>{f"stickers/{current_time_save}_{message.file.name}"}</a></p>"
            formatted_message += f"<p>📅 Date: {current_time}</p></div>"
        elif message.audio or message.video or message.gif or message.file:
            if message.file.size > MAX_FILE_SIZE_BYTES:
                formatted_message += f"<p class='message-type'><strong>📤 Outgoing Media (too large)</strong></p><div class='user-info'>"
                formatted_message += f"<p>👤 To: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📅 Date: {current_time}</p></div>"
                formatted_message += f"<p>📝 File size exceeds {MAX_FILE_SIZE_MB} MB, not downloading.</p>"
            else:
                await message.download_media(file=os.path.join(media_folder, f'{current_time_save}_{message.file.name}'))
                formatted_message += f"<p class='message-type'><strong>📤 Outgoing Media</strong></p><div class='user-info'>"
                formatted_message += f"<p>👤 To: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📂 Media type: {message.file.mime_type}</p>"
                formatted_message += f"<p>📂 File path: <a href='{f"media/{current_time_save}_{message.file.name}"}' target='_blank'>{f"media/{current_time_save}_{message.file.name}"}</a></p><p>📅 Date: {current_time}</p></div>"
                formatted_message += f"<p>📝 Caption: {caption}</p>"
        else:
            formatted_message += f"<p class='message-type'><strong>📤 Outgoing Text</strong></p><div class='user-info'>"
            formatted_message += f"<p>👤 To: @{from_user.username or 'Unknown'} (ID: {from_user.id})</p><p>📅 Date: {current_time}</p></div>"
            formatted_message += f"<p>📝 Message: {caption}</p>"
        formatted_message += "</div>"

    return formatted_message

@client.on(events.NewMessage(incoming=True))
async def log_incoming_message(event):
    if event.is_private:
        from_user = await event.get_sender()
        username = from_user.username

        if from_user.bot:
            return

        message = event.message
        current_time_save = datetime.now().strftime("%d%m%Y-%H%M%S")
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        if username:
            user_folder_name = f"{from_user.id} ({username})"
        else:
            user_folder_name = str(from_user.id)

        user_directory = os.path.join(current_directory, 'logs', user_folder_name)
                
        if not os.path.exists(user_directory):
            os.makedirs(user_directory)

        log_file_path = os.path.join(user_directory, 'logs.html')

        photo_path = os.path.join(user_directory, 'profile.jpg')
        photo_exists = False
        if not os.path.exists(photo_path):
            try:
                await client.download_profile_photo(from_user, file=photo_path)
                photo_exists = os.path.exists(photo_path)
            except Exception:
                photo_path = None

        if not os.path.exists(log_file_path) or os.path.getsize(log_file_path) == 0:
                with open(log_file_path, 'w', encoding='utf-8') as log_file:
                    log_file.write("<html><head><style>"
                        "body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 20px; }"
                        ".message { padding: 20px; margin-bottom: 15px; border-radius: 35px; background-color: #fff; border: 1px solid #e1e1e1; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); font-size: 1.1em; }"
                        ".incoming { background-color: #e0f7fa; }"
                        ".outgoing { background-color: #fff3e0; }"
                        ".message-type { font-weight: bold; color: #00796b; margin-bottom: 10px; font-size: 1.2em; }"
                        ".user-info { font-size: 0.9em; color: #757575; margin-bottom: 10px; }"
                        "p { line-height: 1.6; font-size: 1.1em; }"
                        "a { color: #0288d1; text-decoration: none; }"
                        "img { border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); max-width: 100%; height: auto; margin: 10px 0; }"
                        "</style></head><body>")
                    log_file.write(f"<div style='padding: 20px; margin-bottom: 15px; border-radius: 50px; background-color: #fff; border: 1px solid #e1e1e1; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); font-size: 1.1em; text-align: center;'>"
                               f"<h1>📜 Chat Log</h1>"
                               f"<p>🧑‍💼 <b>Name Surname:</b> {from_user.first_name or 'Unknown'} {from_user.last_name or ''}"
                               f"<p>🔑 <b>User ID:</b> {from_user.id}</p>"
                               f"<p>👤 <b>Username:</b> @{from_user.username}</p>")
                    if from_user.phone:
                        log_file.write(f"<p>📱 <b>Phone number:</b> +{from_user.phone}</p>")
                    if from_user.username:
                        log_file.write(f"<p>🌐 <b>TON Web 3.0 Address:</b> <a href='https://t.me/{from_user.username}'>{from_user.username}.t.me</a></p>")
                    if photo_exists:
                        log_file.write(f"<img src='{"profile.jpg"}' alt='Profile Photo' style='border-radius: 50%; max-width: 150px; margin-top: 10px;'>")
                    log_file.write("</div>")
                    log_file.write(f"<p style='text-align:center; color: #757575; font-size: 0.8em; text-transform: uppercase;'>The dialogue started at {current_time} | All detailed information about the user is provided above.</p>")


        log_content = await format_message_html(from_user, username, message, current_time, current_time_save, direction='incoming')
        log_message_html(log_file_path, log_content)

@client.on(events.NewMessage(outgoing=True))
async def log_outgoing_message(event):
    if event.is_private:
        to_user = await event.get_chat()
        username = to_user.username

        if to_user.bot:
            return

        message = event.message
        current_time_save = datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        if username:
            user_folder_name = f"{to_user.id} ({username})"
        else:
            user_folder_name = str(to_user.id)

        user_directory = os.path.join(current_directory, 'logs', user_folder_name)
        
        if not os.path.exists(user_directory):
            os.makedirs(user_directory)

        log_file_path = os.path.join(user_directory, 'logs.html')

        photo_path = os.path.join(user_directory, 'profile.jpg')
        photo_exists = False
        if not os.path.exists(photo_path):
            try:
                await client.download_profile_photo(to_user, file=photo_path)
                photo_exists = os.path.exists(photo_path)
            except Exception:
                photo_path = None

        if not os.path.exists(log_file_path) or os.path.getsize(log_file_path) == 0:
                with open(log_file_path, 'w', encoding='utf-8') as log_file:
                    log_file.write("<html><head><style>"
                        "body { font-family: monospace; background-color: #f4f4f9; color: #333; margin: 0; padding: 20px; }"
                        ".message { padding: 20px; margin-bottom: 15px; border-radius: 35px; background-color: #fff; border: 1px solid #e1e1e1; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); font-size: 1.1em; }"
                        ".incoming { background-color: #e0f7fa; }"
                        ".outgoing { background-color: #fff3e0; }"
                        ".message-type { font-weight: bold; color: #00796b; margin-bottom: 10px; font-size: 1.2em; }"
                        ".user-info { font-size: 0.9em; color: #757575; margin-bottom: 10px; }"
                        "p { line-height: 1.6; font-size: 1.1em; }"
                        "a { color: #0288d1; text-decoration: none; }"
                        "img { border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); max-width: 100%; height: auto; margin: 10px 0; }"
                        "</style></head><body>")
                    log_file.write(f"<div style='padding: 20px; margin-bottom: 15px; border-radius: 50px; background-color: #fff; border: 1px solid #e1e1e1; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); font-size: 1.1em; text-align: center;'>"
                               f"<h1>📜 Chat Log</h1>"
                               f"<p>🧑‍💼 <b>Name Surname:</b> {to_user.first_name or 'Unknown'} {to_user.last_name or ''}"
                               f"<p>🔑 <b>User ID:</b> {to_user.id}</p>"
                               f"<p>👤 <b>Username:</b> @{to_user.username}</p>")
                    if to_user.phone:
                        log_file.write(f"<p>📱 <b>Phone number:</b> +{to_user.phone}</p>")
                    if to_user.username:
                        log_file.write(f"<p>🌐 <b>TON Web 3.0 Address:</b> <a href='https://t.me/{to_user.username}'>{to_user.username}.t.me</a></p>")
                    if photo_exists:
                        log_file.write(f"<img src='{"profile.jpg"}' alt='Profile Photo' style='border-radius: 50%; max-width: 150px; margin-top: 10px;'>")
                    log_file.write("</div>")
                    log_file.write(f"<p style='text-align:center; color: #757575; font-size: 0.8em; text-transform: uppercase;'>The dialogue started at {current_time} | All detailed information about the user is provided above.</p>")

        log_content = await format_message_html(to_user, username, message, current_time, current_time_save, direction='outgoing')
        log_message_html(log_file_path, log_content)

client.start()
client.run_until_disconnected()
