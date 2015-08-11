import urllib2
import urllib
import cPickle as pickle
import base64

class BackdoorClient(object):
    def __init__(self, url="http://127.0.0.1:8899"):
        self.url = url

    def set(self, **kwargs):
        return self._post_('set', kwargs)

    def gets(self, *args):
        return self._post_('get', args)

    def get(self, arg):
        return self.gets(arg)[arg]

    def execs(self, *cmds):
        return self._post_('exec', cmds)

    def _post_(self, method, obj):
        data = pickle.dumps(obj)
        request = urllib2.Request(self.url + '/' + method, data)
        response = urllib2.urlopen(request).read()
        return pickle.loads(response)

if __name__ == "__main__":
    client = BackdoorClient("http://127.0.0.1:8899")
    print 'set', client.set(a=1)
    print 'exec', client.execs(*"""
import vision
filepath = vision.__file__
a = a+1
b = 2 * a
""".split('\n'))
    print 'get', client.get('filepath')




