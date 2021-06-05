import re

f = open("new-1.js")
out = open("new-2.js", "w")
b = ["DKfBU","Neixx","JVLGm","Microsoft.XMLHTTP","fPUEO","twafp","cNounce","push","mwZqb","HHNtj","Udcyy","cwLfD","EwDKl","ZByHY","OdIqU","/cdn-cgi/challenge-platform/","ftYLD","dSSZS","kUpTT","JsiLM","nuzXd","mFKdD","brEUE","wJHII","nzrEs","waFXr","tejUJ","jc-content","FmpSv","tQYWS","uzcPh","cFPWv","JSON.stringify","IuqGk","yAZXM","CYJsU","charAt","sqmNf","createElement","getElementById","ActiveXObject","FsnTw","npjGK","vgudf","vFOpg","join","ftqUf","ohgQt","wZnsT","nfbgP","SQDhd","oSLiS","qzqbQ","zwOqn","Line: ","hasOwnProperty","cf-please-wait","split","zxggS","text/javascript","rFjjB","addEventListener","Date","pzTQI","XaEEt","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=","dfViB","yzXfK","OJTsl","lXZcr","chReq","uHjltCSeK","UsAkq","EfNqX","_cf_chl_enter","DNxgH","getUTCHours","EpyND","[[[ERROR]]]:","ceSrj","wHsoW","cHash","_cf_chl_hload","SoDcW","bAwWQ","yjs","toLowerCase","ACGqG","ExjNE","JuSTe","JkkZp","_cf_chl_ctx","MNKmT","getTime","vtlMW","uSpnp","application/x-www-form-urlencoded","lvWTs","igVgq","mwOQF","FITad","Opcno","JSON","NUXDd","Romsi","BThGl","ZuHjz","UpzfW","cRay","none","nAGQy","parse","PaBEu","-alert-error\">This is taking longer than expected, please reload the page.</p>","PBiJh","vehux","Message: ","WHfKk","POST","pfcIS","appendChild","block","hzAFV","QAoxj","VJXuA","WJsGA","fromCharCode","PhTkY","loaded","ontimeout","SHA256","hDVkx","cf_chl_prog","DOMContentLoaded","mnQFj","jPxOe","onreadystatechange","Zweex","flow/ov","lmatl","readystatechange","FMHAR","yjs-content","IBNTw","pDNoS","<p class=\"","NNCds","olwNH","CuDrh","bieJU","nEsiv","sVnXF","min","NLjaF","zMNXn","dsVrS","getUTCSeconds","VuvBN","substring","_cf_chl_done_ran","wtFro","kwATs","string","JmrtL","cf_chl_","0123456789abcdef","number","WfrpxPzj90b-YkdSB5$KXQ6tF8cyswUCD+LThGgmoneqZHMJaN3RIO7il24v1uEAV","aGyyY","object","hUtBc","This browser is not supported.","XSXhK","kIqqd","SkfRE","jc-spinner-please-wait","cf_chl_rc_i","Math","=; Max-Age=-99999999;","fozIZ","sendRequest","GEeaz","kjjkX","DeSFL","stringify","LJSDY","hmVEd","test","iIzNP","SxnSX","rwvRE","navigator","console","IyESg","tHcxM","DWRKq","MYwlH","nwDuU","KjgZL","getUTCDate","BsgaS","0000","QEZjw","sQtbP","tqZRm","jXRMz","expires=","%2b","challenge-form","vpHWG","xdJPj","EtiTI","NHOhH","-spinner-please-wait","pQKKI","SUzGI","chC","YVzBt","pDQff","/0.6181260850835241:1622898196:7dfd9a425396f87e75d82e6dc4d05c5c5c2ec8f54aaac4ce1ac83254c8364165/","nQPwj","boolean","navPX","JkoCN","lastIndex","NqpyE","GGIPM","GqCtw","CF-Challenge","agPmZ","timeout","getUTCMonth","yqKiJ","URL: ","Function","NtUZe","sSurA","status","interactive","Column: ","type","bFuzj","cgrfo","BxdBK","aTYPW","lQDyG","ixRan","OPoxs","eUIOU","tPyJR","null","_cf_atob",";path=/","evhVy","fOekF","alert","IMxVP","charCodeAt","HvqUa","djteb","send","style","_cf_chl_hloaded","_cf_chl_opt","KlUEK","replace","aZskF","WFwzQ","DCsTn","ozLPT","CTpSG","getUTCFullYear","uPfdA","EAJlz","rZEhX","cookie","xyecP","nOjjblkSVi","getElementsByTagName","ZdTIE"," - ","setTime","PeCOr","oKuaS","NIkzl","href","NFeHp","iJfuL","gDJMP","src","fqrtf","MESdv","nyZcq","gZIrI","opFKO","PMlxh","WMwCx","Content-type","YDWqY","PbjKU","prototype","zrkuq","GuuAF","xYSgE","wADVn","EddQl","Thfw","protocol","innerHTML","oOejO","call","prVWC","getUTCMinutes","ggSyn","ZRTLT","<div class=\"yjs-content\"><p style=\"background-color: #de5052; border-color: #521010; color: #fff;\" class=\"cf-alert cf-alert-error\">&#35813;&#32593;&#31449;&#36164;&#28304;&#26080;&#27861;&#36890;&#36807;&#27492;&#22320;&#22336;&#35775;&#38382;&#12290;</p></div>","length","jc-please-wait","IkeZS","Script Error: See Browser Console for Detail","HpEsa","OdTqV","JaXPy","tcQxA","===","HICXk","NZQzi","BInNP","cLt","valueOf","bOpFd","ChlsB","pWmwV","erUWx","oYrZC","jeLaw","pVHSu","JnrSH","oiNwD","toString","cf-content","CSUqC","JIKrR","XMLHttpRequest","pYteA","jAzlC","DBTST","bjMRi","JSON.parse","cRq","attachEvent","AtscI","toJSON","0|1|3|4|2","oPwRbaTIuVdr8BxX29Oiqhy4fWpvC7EKSmFe3lkcnYGLJZM0QHN6gj51tzsDAU","CmQJL","yCNHP","STfaD","dTjyg","yjs-spinner-please-wait","cType","MJzim","setRequestHeader","CkCOG","apply","document","NyXKS","parseInt","JpbWX","ZQuSq","ukyMw","no-cookie-warning","[object Array]","zLydn","ErQmP","complete","<div class=\"cf-content\"><p style=\"background-color: #de5052; border-color: #521010; color: #fff;\" class=\"cf-alert cf-alert-error\">This web property is not accessible via this address.</p></div>","hvQLY","sQUIm","sajAB","gzlJx","bqDow","mOwLg","indexOf","Mxpzq","https://hcaptcha.com/1/api.js?render=explicit&recaptchacompat=off&onload=_cf_chl_hload","cvId","function","HboHm","slice","onerror","tUoNE","PcpAx","_cf_chl_done","zfAGU","LvrPM","vokaw","emQqh","3|2|0|1|4","BDJzG","eXDBU","open","brMVN","atob","hostname","log","display","location","0|3|1|2|4","oJjAp","ZdcjM","STZcH","bnIRk","ZgAKQ","KCJIy","chCAS","setTimeout","0|4|3|1|5|2","uPweC","location-mismatch-warning","Ywbtw","dOtAG","HCpGO","readyState","JjoVo","BAvAy","responseText","uZCIC","mNkEE","XSUwg","pqMxD","script error","sJGZU","VqQwF","YtYhG","cjbNk","QNuti","ccwaW","MpKcP","script","XjIaZ","PhZyp","AZfLP","xoKAy","EuQLb","tOFCC","zrHwG","ByzyP","WldSM","AfTAw","FpagV","Error object: ","xhlAW","DEvxh","-alert ","VpjMj","ABGMf","cookieEnabled","<div class=\"jc-content\"><p style=\"background-color: #de5052; border-color: #521010; color: #fff;\" class=\"jc-alert jc-alert-error\">&#35813;&#32593;&#31449;&#36164;&#28304;&#26080;&#27861;&#36890;&#36807;&#27492;&#22320;&#22336;&#35775;&#38382;&#12290;</p></div>","taaPtL","pow","DCdHm","nMlwe","JGYjh","PWeKl","rqJus"]


hex_re = re.compile(r"0x[a-f0-9]+")
sub_re = re.compile(r"(?P<index>\[c\('0x[a-f0-9]+'\)\])|(?P<value>c\('0x[a-f0-9]+'\))")

text = """
    d = this || self,
    e = d[c('0x16d')],
    f = [],
    g = function(C, B, A, z, v, u, t) {
        return t = {},
        t[c('0x7a')] = function(D, E) {
            return D !== E
        }
        ,
        t[c('0x17e')] = function(D, E) {
            return D < E
        }
        ,
        t[c('0x1ab')] = function(D, E) {
            return D + E
        }
        ,
        t[c('0xe1')] = c('0x111'),
        t[c('0x1e')] = c('0x162'),
        t[c('0x137')] = function(D, E) {

    else
                return isFinite(this[c('0x149')]() || '') ? C[c('0x12f')](C[c('0x12f')](C[c('0x3a')](C[c('0xb3')](this[c('0x10f')]() + '-', D(C[c('0xf4')](this[c('0xe7')](), 1))) + '-', C[c('0x14a')](D, this[c('0xc7')]())) + 'T' + C[c('0x14a')](D, this[c('0x4c')]()) + ':' + D(this[c('0x138')]()), ':') + C[c('0x1c1')](D, this[c('0x9c')]()), 'Z') : null
        }
"""

def subber(m):

    if (p := m.group('index')):
        h = hex_re.search(p).group(0)[2:]
        index = b[int(h, 16)]
        return ("."+index if index.isidentifier() else "[" + repr(index) + "]") + " "
    p = m.group(0)
    h = hex_re.search(p).group(0)[2:]
    return repr(b[int(h, 16)])

print(sub_re.sub(subber, f.read()))