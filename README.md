# AB BOTS - Advanced Telegram Bot

![Version](https://img.shields.io/badge/version-4.0.0--enhanced-blue.svg)
![License](https://img.shields.io/badge/license-AGPL--3.0-green.svg)
![Python](https://img.shields.io/badge/python-3.10+-yellow.svg)
![Branding](https://img.shields.io/badge/Powered%20by-AB%20BOTS-blueviolet.svg)

```
╔══════════════════════════════════════════════════════╗
║          █████╗ ██████╗     ██████╗  ██████╗ ████████╗███████╗        ║
║         ██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝        ║
║         ███████║██████╔╝    ██████╔╝██║   ██║   ██║   ███████╗        ║
║         ██╔══██║██╔══██╗    ██╔══██╗██║   ██║   ██║   ╚════██║        ║
║         ██║  ██║██████╔╝    ██████╔╝╚██████╔╝   ██║   ███████║        ║
║         ╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝        ║
╚══════════════════════════════════════════════════════╝
```

An advanced, feature-rich Telegram bot for mirroring, leeching, and managing downloads from various sources including torrents, direct links, Google Drive, Mega, JDownloader, and more. **Enhanced with modern UI, detailed progress tracking, and professional branding.**

## ✨ NEW FEATURES (v4.0 Enhanced)

### 🎨 Redesigned UI
- **Professional Branding**: AB BOTS branding in mono bold fonts throughout the bot
- **Enhanced Progress Display**: Beautiful progress bars with detailed metadata
- **Modern Message Format**: Clean, structured messages with emojis and boxes
- **Real-time Updates**: Live progress updates showing:
  - Current file being processed
  - Download/Upload speed with icons
  - ETA and elapsed time
  - File count and size information
  - Seeders/Leechers for torrents
  - Detailed system statistics

### 📊 Enhanced Status Messages
- **Visual Headers**: Beautiful ASCII art headers with AB BOTS branding
- **Detailed Metadata Display**:
  - File size with progress
  - Processing status
  - Speed metrics
  - Time remaining
  - User information
  - Engine details
- **Better Organization**: Structured information boxes with clear separators
- **Icon-Rich Interface**: Intuitive icons for every piece of information

## 🌟 Core Features

### Download Methods
- **Torrent Downloads**: qBittorrent and Aria2c support
- **Direct Links**: HTTP/HTTPS direct downloads with resume capability
- **Google Drive**: Clone, download, and manage GDrive files
- **Mega**: Full Mega.nz integration
- **YouTube/Media**: yt-dlp powered downloads from 1000+ sites
- **Telegram Files**: Download from Telegram channels/chats
- **JDownloader**: Integration with JDownloader2
- **Usenet/NZB**: SABnzbd support for Usenet downloads
- **Rclone**: Support for 40+ cloud services

### Upload Destinations
- **Telegram**: Leech files directly to Telegram
- **Google Drive**: Upload to GDrive with service account support
- **Rclone**: Upload to any rclone-supported cloud storage
- **YouTube**: Direct upload to YouTube (with metadata)

### Media Processing
- **FFMPEG Integration**: Custom FFMPEG commands for media conversion
- **Extract Archives**: Automatic extraction of zip, rar, 7z, tar, etc.
- **Create Archives**: Archive files before upload
- **Split Files**: Split large files into smaller parts
- **Merge Videos**: Merge multiple video files
- **Metadata Editing**: Add/edit video, audio, and subtitle metadata
- **Thumbnail Support**: Custom thumbnails for uploads
- **MediaInfo**: Get detailed media information

### Advanced Features
- **Multi-Language Support**: Bengali (bn) and English (en)
- **RSS Feed**: Automated RSS monitoring and downloads
- **Torrent Search**: Search torrents from multiple sources
- **IMDB Integration**: Fetch movie/series information
- **Clone/Sync**: Clone GDrive files or sync with rclone
- **Bulk Downloads**: Process multiple links at once
- **User Settings**: Customizable per-user settings
- **Shortener Support**: Integrate URL shorteners
- **Telegraph Support**: Upload to Telegraph
- **Plugin System**: Extensible plugin architecture
- **Task Queue**: Smart queue management system
- **Enhanced Status Updates**: Real-time download/upload status with detailed progress
- **Force Subscription**: Require channel subscription
- **Login Protection**: Optional password protection

### Management Features
- **Task Management**: Start, stop, pause tasks
- **User Control**: Authorized users and sudo system
- **Chat Permissions**: Control bot access per chat
- **Storage Limits**: Set download/upload limits
- **Time Limits**: Task timeout and user interval limits
- **Broadcast**: Send messages to all users
- **Database**: MongoDB for persistent storage
- **Statistics**: Bot usage statistics
- **Services Management**: Control integrated services
- **Speed Test**: Check bot's network speed

## 📋 Requirements

### Mandatory
- **BOT_TOKEN**: Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- **OWNER_ID**: Your Telegram User ID
- **TELEGRAM_API**: API ID from [my.telegram.org](https://my.telegram.org)
- **TELEGRAM_HASH**: API Hash from [my.telegram.org](https://my.telegram.org)
- **DATABASE_URL**: MongoDB connection string

### Optional Services
- **Google Drive API**: For GDrive features (token.pickle, credentials.json)
- **Rclone**: For cloud storage support (rclone.conf)
- **JDownloader**: MyJDownloader account (email & password)
- **Mega**: Mega.nz credentials
- **Usenet**: SABnzbd server configuration
- **Telegraph**: Automatic account creation
- **Shorteners**: FileLion, StreamWish API keys

## 🚀 Deployment

### Docker (Recommended)

1. **Clone the repository**:
```bash
git clone https://github.com/RecklessEvadingDriver/t.git
cd t
```

2. **Install Docker** (if not installed):
```bash
chmod +x docker-install.sh
./docker-install.sh
```

3. **Configure the bot**:
```bash
cp config_sample.py config.py
nano config.py  # Edit with your values
```

4. **Build and run**:
```bash
chmod +x run.sh
./run.sh
```

Or manually:
```bash
docker compose up -d --build
```

### Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

The `heroku.yml` file is configured for easy Heroku deployment.

### CapRover Deployment

Use the provided `captain-definition` file for CapRover deployment.

### Koyeb Deployment

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/RecklessEvadingDriver/t&branch=master&name=ab-bots&dockerfile=Dockerfile)

The `koyeb.yaml` file is configured for easy Koyeb deployment.

1. Click the **Deploy to Koyeb** button above, or use the [Koyeb CLI](https://www.koyeb.com/docs/cli/installation):
```bash
koyeb deploy --config koyeb.yaml
```

2. Set the required environment variables in the Koyeb dashboard:
   - `BOT_TOKEN`, `OWNER_ID`, `TELEGRAM_API`, `TELEGRAM_HASH`, `DATABASE_URL`

3. Optionally set `BASE_URL` to your Koyeb app URL (e.g., `https://ab-bots-yourname.koyeb.app`) and `BASE_URL_PORT` to `80`.


## 🎮 Bot Commands

### Download Commands
- `/mirror` - Mirror to cloud
- `/leech` - Leech to Telegram
- `/qbmirror` - qBittorrent mirror
- `/qbleech` - qBittorrent leech
- `/yt` - YouTube/media download
- `/ytq` - YouTube with quality selection
- `/clone` - Clone GDrive/Rclone files
- `/tdl` - TMV direct download

### Management Commands
- `/cancel` - Cancel a task
- `/cancelall` - Cancel all tasks
- `/status` - Show all active tasks (Enhanced UI!)
- `/stats` - Bot statistics
- `/speed` - Speed test
- `/restart` - Restart bot
- `/log` - Get bot logs

### Media Commands
- `/mediainfo` - Get media information
- `/metadata` - Edit metadata
- `/imdb` - Search IMDB
- `/search` - Torrent search
- `/nzbsearch` - NZB search

### Google Drive Commands
- `/gdsearch` - Search in GDrive
- `/gdcount` - Count GDrive files
- `/gddelete` - Delete from GDrive

### Settings Commands
- `/users` - User settings
- `/bsettings` - Bot settings
- `/help` - Help message
- `/cmd` - Available commands

### Admin Commands
- `/auth` - Authorize user/chat
- `/unauth` - Unauthorize user/chat
- `/addsu` - Add sudo user
- `/rmsu` - Remove sudo user
- `/broadcast` - Broadcast message
- `/shell` - Execute shell command
- `/exec` - Execute Python code
- `/clearlocals` - Clear local cache
- `/service` - Manage services

### RSS Commands
- `/rss` - RSS menu
- `/rsssub` - Subscribe to RSS
- `/rssunsub` - Unsubscribe from RSS
- `/rsslist` - List RSS subscriptions

## 📝 Command Usage Examples

### Mirror/Leech
```bash
# Simple mirror
/mirror https://example.com/file.zip

# Mirror with new name
/mirror https://example.com/file.zip -n CustomName.zip

# Leech with extraction
/leech https://example.com/archive.zip -e

# Leech with password and new name
/leech https://example.com/file.zip -n NewName.zip -z password

# Multi-link mirror (reply to first link)
/mirror -i 5

# Bulk download
/mirror -b (reply to message with multiple links)

# Mirror to custom folder
/mirror https://example.com/file.zip -m Movies/Action

# Upload to specific location
/mirror https://example.com/file.zip -up gdrive_id
/mirror https://example.com/file.zip -up remote:path/to/folder
```

### YouTube Download
```bash
# Download video
/yt https://youtube.com/watch?v=xxxxx

# Download with quality selection
/ytq https://youtube.com/watch?v=xxxxx

# Download audio only
/yt https://youtube.com/watch?v=xxxxx -audio

# Download with custom name
/yt https://youtube.com/watch?v=xxxxx -n "My Video"

# Download with options
/yt https://youtube.com/watch?v=xxxxx -opt format:best

# Download with FFMPEG processing
/yt https://youtube.com/watch?v=xxxxx -ff ["-c:v", "libx264"]
```

### Clone/Sync
```bash
# Clone GDrive
/clone https://drive.google.com/file/d/xxxxx

# Clone to custom destination
/clone https://drive.google.com/file/d/xxxxx -up gdrive_id

# Sync with rclone
/clone remote:path/to/source -up remote:path/to/dest -sync
```

### Additional Arguments
- `-e` - Extract archive
- `-z password` - Archive password
- `-sp 2gb` - Split size
- `-t tg-link` - Custom thumbnail
- `-au username:password` - HTTP auth
- `-audr` - Audio extract
- `-m folder` - Move to folder
- `-up destination` - Upload destination
- `-ff [commands]` - FFMPEG commands
- `-n name` - New name
- `-b` - Bulk mode
- `-i number` - Multi links
- `-sync` - Sync mode (rclone)

## 🔧 Advanced Setup

### Service Accounts (Google Drive)
1. Generate service accounts using `gen_scripts/gen_sa_accounts.py`
2. Add service accounts to shared drive
3. Place JSON files in `accounts/` folder
4. Set `USE_SERVICE_ACCOUNTS = True`

### Rclone Setup
1. Generate rclone.conf: `rclone config`
2. Place in root directory or set `RCLONE_PATH`
3. Configure remotes for various cloud services

### JDownloader Setup
1. Create MyJDownloader account
2. Set `JD_EMAIL` and `JD_PASS` in config
3. Bot will auto-connect on startup

### Usenet/SABnzbd Setup
Configure `USENET_SERVERS` in config with your Usenet provider details.

### Search API Setup
Configure torrent search plugins in `SEARCH_PLUGINS` array.

## 🔌 Plugin System

The bot supports custom plugins. Place plugin files in `bot/modules/` and they will be auto-loaded.

### Plugin Manager Commands
- `/plugins` - List plugins
- `/plugin enable <name>` - Enable plugin
- `/plugin disable <name>` - Disable plugin

## 🗄️ Database

MongoDB is used for:
- User settings
- RSS feeds
- Bot configuration
- Task history
- Statistics

## 📊 Web Interface

Access web interface at `http://your-ip:BASE_URL_PORT` (default: 80)
- Set `BASE_URL` for external access
- Set `WEB_PINCODE` for security

## 🛠️ Troubleshooting

### Common Issues

**Bot not responding**: Check bot token and permissions

**Download fails**: Check storage space and limits

**GDrive errors**: Verify token.pickle and credentials

**Upload fails**: Check upload destination configuration

**Queue not working**: Verify queue settings in config

### Logs
- Check Docker logs: `docker logs madxleechbot`
- Get logs via bot: `/log`
- Check specific service logs in respective folders

## 🔄 Updates

### Auto-Update
Set `UPSTREAM_REPO` and `UPSTREAM_BRANCH` in config for auto-updates.

### Manual Update
```bash
git pull
docker compose up -d --build
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

See [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for educational purposes. Users are responsible for complying with copyright laws and terms of service of various platforms.

## 🙏 Credits

- **Pyrogram**: Telegram MTProto API framework
- **yt-dlp**: Media downloader
- **Aria2**: Download utility
- **qBittorrent**: Torrent client
- **Rclone**: Cloud storage manager
- **JDownloader**: Download manager
- **SABnzbd**: Usenet client
- **Original ADV-ML Project**: Base codebase

## 📞 Support

For support and updates:
- GitHub Issues: [Report Issues](https://github.com/RecklessEvadingDriver/t/issues)

## 🌟 Features Roadmap

- [x] Enhanced UI with professional branding
- [x] Detailed progress tracking with metadata
- [x] Better status message formatting
- [ ] More cloud storage providers
- [ ] Advanced filtering options
- [ ] Better web interface
- [ ] Mobile app
- [ ] Multi-bot support
- [ ] Advanced analytics

---

<div align="center">

**Powered by AB BOTS** 🚀

*Advanced Telegram Bot with Enhanced UI & Features*

Made with ❤️ by the AB BOTS Team

</div>
