# 사용법: python3 make_snippet.py https://cdn.jsdelivr.net/gh/<계정>/revu-biz-fonts@v1/fonts/
# 결과 framer-head-end.html 을 Framer 사이트 설정 > Custom Code > End of <head> 에 붙여넣는다.
import json,sys
base=sys.argv[1].rstrip('/')+'/'
faces=json.load(open('faces.json'))
wt={'Light':300,'Regular':400,'Medium':500,'SemiBold':600,'Bold':700,'ExtraBold':800,'Black':900}
rules=['@font-face{font-family:"Pretendard %s";font-style:normal;font-weight:%d;font-display:swap;src:url(%sRevuBizSans-%s.%d.woff2) format("woff2");unicode-range:%s}'%(w,wt[w],base,w,i,ur) for w,x,i,ur in faces]
open('framer-head-end.html','w').write('<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>\n<style>\n'+'\n'.join(rules)+'\n</style>\n')
print('framer-head-end.html 생성:',len(rules),'개 선언')
