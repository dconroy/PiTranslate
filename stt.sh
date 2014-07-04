#DaveConroy.com
#7/4//14
#stt.sh

#part 1
echo "Recording your Speech (Ctrl+C to Transcribe)"
arecord -D plughw:0,0 -f cd -t wav -d 0 -q -r 16000 | flac - -s -f --best --sample-rate 16000 -o daveconroy.flac;

#part 2
python text-to-translate.py



