import StringIO
import os.path
import pycurl


#variables
filename = 'daveconroy.flac'
key = 'xxx'
url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=' + key

#send the file to google speech api
c = pycurl.Curl()
c.setopt(pycurl.VERBOSE, 0)
c.setopt(pycurl.URL, url)
fout = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, fout.write)

c.setopt(pycurl.POST, 1)
c.setopt(pycurl.HTTPHEADER, [
                'Content-Type: audio/x-flac; rate=16000'])

filesize = os.path.getsize(filename)
c.setopt(pycurl.POSTFIELDSIZE, filesize)
fin = open(filename, 'rb')
c.setopt(pycurl.READFUNCTION, fin.read)
c.perform()

response_code = c.getinfo(pycurl.RESPONSE_CODE)
response_data = fout.getvalue()

#since google replies with mutliple json strings, the built in python json decoders dont work well
start_loc = response_data.find("transcript")
tempstr = response_data[start_loc+13:]
end_loc = tempstr.find("\"")
final_result = tempstr[:end_loc]

c.close()


print "You Said:" + final_result

#part 2
os.system("python PiTranslate.py -o en -d es -t '" + final_result + "'")
