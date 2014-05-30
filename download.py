import sys
import os
import logging

from gmusicapi.clients import Musicmanager

logging.basicConfig(filename='dl.log', level=logging.DEBUG)

if os.path.exists('oauth.cred'):
    pass
else:
    Musicmanager.perform_oauth('oauth.cred', True)

manager = Musicmanager()

manager.login('oauth.cred')

logging.info('starting download')
count = 0
for songs in manager.get_uploaded_songs(True):
    for song in songs:
        count = count + 1

        dartist = 'dl/%s' % (song['album_artist'] or song['artist'])
        if not os.path.exists(dartist):
            os.mkdir(dartist)

        dalbum = '%s/%s' % (dartist, song['album'])
        if not os.path.exists(dalbum):
            os.mkdir(dalbum)

        fsong = '%s/%02d - %s.mp3' % (dalbum,
                                      song['track_number'],
                                      song['title'].replace('/', '_'))

        sys.stdout.write("%05d %s\n" % (count, fsong))
        if not os.path.exists(fsong):
            audio = None
            try:
                filename, audio = manager.download_song(song['id'])
                logging.info('download success: "%s"' % fsong)
            except KeyboardInterrupt:
                sys.exit(1)  # move this up
            except Exception, e:
                logging.error('download failed: "%s" %s' % (fsong, e))
            else:
                with open(fsong, 'wb') as f:
                    f.write(audio)
        else:
            logging.info('download skipped: "%s"' % fsong)

sys.stdout.write('\n')
