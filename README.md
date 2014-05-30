# Skyjam (Google Music) Downloader

A simple script that downloads your Google Play music.

## How to use

1. clone this repo
2. use python 2.7
3. recommended: use a virtualenv (very recommended: use pyenv virtualenv)
4. `pip install -r requirements.txt` or `pip install gmusicapi`
5. `python download.py` (will perform OAuth the first time)

Downloads go into a `dl` directory. If you want to put your music somewhere
else, use a symlink.

Files are named `album artist/album/track - title.mp3`. If a file with this
name exists, it is not downloaded again.

Logging goes to `dl.log`.
Tip: `tail -f | egrep 'download (skipped|success|failed)'`.
Pro tip: `grep 'download failed' | sort`.

## Why? There's Google's Music Manager or the Chrome extension already!

Music Manager fails to download some songs, its logs are unusable, and it
obliviously redownloads everything when you retry.

The NaCl Google Music Chrome extension allows you to download your songs, but
you can add to the queue at most per album, you can't cancel it, you can view a
lrogress list but that's all and there's no log of failures.

IOW, both are absurdly optimist, hopelessly unreliable pieces of software
mostly due to poor UI.

This little piece of code aims to give you information on failure and laziness
on retry.

## License

3BSD. See [LICENSE](LICENSE).
