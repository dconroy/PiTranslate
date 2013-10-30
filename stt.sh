#DaveConroy.com
#10/29/13
#stt.sh

echo "Recording your Speech (Ctrl+C to Transcribe)"
arecord -D plughw:0,0 -f cd -t wav -d 0 -q -r 16000 | flac - -s -f --best --sample-rate 16000 -o daveconroy.flac;

echo "Converting Speech to Text..."
wget -q -U "Mozilla/5.0" --post-file daveconroy.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v1/recognize?lang=en-us&client=chromium" | cut -d\" -f12  > stt.txt

echo "You Said:"
value=`cat stt.txt`
echo "$value"

#part 2
#python pitranslate.py -o en -d es -t "$value"

