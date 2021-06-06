import jsbeautifier, requests, re, json

JS_URL="https://www.urbanstaroma.com/cdn-cgi/challenge-platform/h/g/orchestrate/captcha/v1?ray=65b001425858c4f8"

def download(url):
    r = requests.get(url)
    return r.text

def prettify(js):
    opts = jsbeautifier.BeautifierOptions(options=dict(
        # unescape_strings=True,
        # jslint_happy=True,
    ))
    return jsbeautifier.beautify(js, opts=opts)

B_SHIFT_RE = re.compile(r"}\(b, (?P<shift>\d+)\)")
B_RE = re.compile(r"b = '(?P<b>.*)'\.split\('{'\)")


def b_shifter(js):
    b = []
    shift_num = int(B_SHIFT_RE.search(js).group('shift'))
    def subber(m:re.Match):
        b_string = m.group('b')
        bb = b_string.split('{')
        b.extend(bb[shift_num:])
        b.extend(bb[:shift_num])
        return json.dumps(b)
    subbed = B_RE.sub(subber, js, 1).splitlines()
    c_removed = subbed[:2] + [ subbed[6][subbed[6].find(' c'):] ] + subbed[7:]
    return b, '\n'.join(c_removed)
        

hex_re = re.compile(r"0x[a-f0-9]+")
sub_re = re.compile(r"(?P<index>\[c\('0x[a-f0-9]+'\)\])|(?P<value>c\('0x[a-f0-9]+'\))")

def make_substitutions(b, script):
    def subber(m):
        if (p := m.group('index')):
            h = hex_re.search(p).group(0)[2:]
            index = b[int(h, 16)]
            return ("."+index if index.isidentifier() else "[" + repr(index) + "]") + " "
        p = m.group(0)
        h = hex_re.search(p).group(0)[2:]
        return repr(b[int(h, 16)])
    script = sub_re.sub(subber, script_shifted)
    return script


if __name__ == '__main__':
    script = download(JS_URL)
    script_pretty = prettify(script)
    b, script_shifted = b_shifter(script_pretty)
    script = make_substitutions(b, script_shifted)


    script_pretty = prettify(script)
    print(script_pretty)