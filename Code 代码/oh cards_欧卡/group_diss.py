#一起说说说

from apps.momarket import ebook
from apps.momarket import music
from apps.Rachel.list1 import directorys
from apps.momarket import share
from apps.momarket import login

def index(args):
    #清空当前用户的进度缓存，注意，请仅在调试的时候使用该功能
    #ebook.delCache()

    #点击继续按钮形式
    ebook.EBook > {
        'id': 'cards',   #必须指定id, 依据该id缓存进度
        'api': api_start < {},  #问答开始时需要获取数据的接口
        'click-music': 'http://cdn.moastro.cn/user_assets/5cef4f38479833593c7f359b/20190701162501/click.mp3',  #设置点击按钮的音效
        'interval': 1500,       #items中每个item间隔多长时间出现，单位毫秒，默认1500，即1.5s
        # 'refresh-show-restart': True,  #重新进入页面的时候是否显示重新开始，默认False
        'container': {
            #电子书容器样式
            'background':'#FFFACD'
        },
        'next': {
            #继续按钮样式
            'background': '#79CDCD',
            'border': 'none'
        },
        'restart': {
            #重启按钮样式
            'background': '#79CDCD',
            'border': 'none'
        }
    }
    
    #演示加上背景音乐，用音乐模块
    music.Music > {
        'id': 'bgm',
        'music': res(307771299), #scene
        # 'https://cdn.motimaster.com/user_assets/5b68f6e01450620a09e3ad1d/20181228170438/1790094933.mp3',
        'loop': True,  #默认为True，可不填写
        'autoplay': True, #默认为True,可不填写
        'left': 20,
        'size': (80, 80),
        'background-image': res('105774590')
    }

    #全局修改动画时长，按下方注释
    Style > {
        'selector': '.animated',
        'animation-duration': '2s'
    }

    if isweixin():          #判断是否为微信
        info = login.OpenInfoLogin()
    else:
        info = login.ScanInfoLogin()

    oid = decrypt(args.oid)  #解密oid参数，由于分享出来的oid参数已加密，所以这里需要解密
    if not oid:
        oid = info['openid'] #默认为主人状态
    
    if oid == info['openid']:
        Box > {
            'text': '您是该页面主人'
        }
    
    share.ShareInfo > {
        'title': '一起说说说',  #分享标题
        'desc': '充分发挥联想能力和创意能力',   #分享描述  H5分享的时候才会用到
        # 'url': '/editor/index/',  #分享后的URL可以为一个真实的链接
        'url': index < {  
            #也可以为一个自己定义的函数，分享后将访问该函数对应的页面
            #注意此处index非固定的，只是演示，可以是自己定义的任何一个页面函数，例如test函数，分享后访问的将是test函数对应的页面
            'oid': encrypt(oid)   #分享出去还是保持原主人的页面,为保护用户的openid，对openid进行加密后分享
        },  
        'img-url': 'https://momoqn.looosen.cn/301697860',
        'success': shareSuccess < {}
        #分享的封面图
    }

    ebook.EBookListZoom > {
        'directorys': directorys(),  #目录配置封装到了directorys函数，参照下方directorys函数的写法
            #目录的首页，根据首页缓存用户的目录进度
        'ebooklist': {
            #可修改目录框的样式
        },
        'home': '/Rachel/list1/index',
        'button': {
            #可修改按钮样式，例如设置字体大小
            'font-size': 25,
            'text':'目录',
            'text-align':'center',
            'border-color' :'#96CDCD',
            'left':650
            
        },
    }

@pythonjs
def shareSuccess(args):
    alert('分享成功')

def showup(args):
    #上滑翻页形式
    ebook.EBookUp > {
        'id': 'test',   #必须指定id, 依据该id缓存进度
        'api': api_start < {},  #问答开始时需要获取数据的接口
        'container': {
            'background': 'black'  #翻页的形式需要给页面设置一个背景，不然各个页面显示就叠加到一起了
        }
    }

def showleft(args):
    #上滑翻页形式
    ebook.EBookLeft > {
        'id': 'test',   #必须指定id, 依据该id缓存进度
        'api': api_start < {},  #问答开始时需要获取数据的接口
        'container': {
            'background': 'yellow'  #翻页的形式需要给页面设置一个背景，不然各个页面显示就叠加到一起了
        }
    }

#重点词语突出
def api_start(args):
    page.cards.alias('next').text('规则是什么？')
    return {
        "id": 'start',     #自定义id, 可以用来设置用户的进度，
        "next": True,    #是否显示继续按钮
        "restart": False,  #是否显示重新开始按钮
                'items': [ {
                'type': 'image',
                # 'animation': 'fadeIn',
                'src': res(308019053),
            },{
                'type': 'title',
                'content': '让我们来一起充分发挥自己的联想能力\n和创意能力吧!',
                'animation-duration': '0.5s',
                'style': {
                    'text-align': 'center',
                    'color': '#6495ED',
                    'font-size': 36
                    # 'animation-duration': '2s',
                },
                'animation': 'slideInUp',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                # "keep-scroll": False  
            },{
            'type': 'title',
            'content': '请随意点开一张卡牌，并仔细看着这张牌，它会有很多很多种解释。请和朋友们一起轮流说出自己对于该卡牌的描述、解释或联想',
            'style':{
                'text-align': 'center',
                'font-size': 34,
                'color': '#698B69'
            }
        }],
        'nextapi': api_step1 <{}
    }

def api_step1(args): 
    page.cards.alias('next').text('我们准备好了！')
    return{
        'id': 'step1',
        'items': [{
            'type': 'image',
            'src': res(308346034)
        }, ],
        'nextapi': api_step2 < {}
    }

def api_step2(args):    
    print(args)
    page.cards.alias('next').text('选好了')   
    return{
        "id": 'step2',
        'items': [{
            'type': 'title',
            'content': '在下列卡片中随意点开一张',
            'style':{
                'text-align': 'center',
                'font-size': 30,
                'color': '#698B69'
            }
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            #'retry': True,
            'radios':[{
                'text': '卡片1'
            },{
                'text': '卡片2',
                'value': 'radio2'
            },{
                'text': '卡片3',
                'value': 'radio3'
            },{
                'text': '卡片4',
                'value': 'radio4'
            },{
                'text': '卡片5'
            },{
                'text': '卡片6'
            },{
                'text': '卡片7'
            },{
                'text': '卡片8'
            },{
                'text': '卡片9'
            },{
                'text': '卡片10',
            },{
                'text': '卡片11'
            },{
                'text': '卡片12'
            },{
                'text': '卡片13'
            },{
                'text': '卡片14'
            },{
                'text': '卡片15'
            },{
                'text': '卡片16'
            },{
                'text': '卡片17'
            }]
        }],
        'nextapi': api_step3 <{}
    }

def api_step3(args):
    result = args.answer.number+1
    if result == 1:
        return{
             'id': 'step3',
            #  'next': False,
              'nextapi': api_step01<{}
              }
    elif result == 2:
        return{
             'id': 'step3',
              'nextapi': api_step02<{}
              }
    elif result == 3:
        return{
             'id': 'step3',
              'nextapi': api_step03<{}
              }
    elif result == 4:
        return{
             'id': 'step3',
              'nextapi': api_step04<{}
              }
    elif result == 5:
        return{
             'id': 'step3',
              'nextapi': api_step05<{}
              }
    elif result == 6:
        return{
             'id': 'step3',
              'nextapi': api_step06<{}
              }
    elif result == 7:
        return{
             'id': 'step3',
              'nextapi': api_step07<{}
              }
    elif result == 8:
        return{
             'id': 'step3',
              'nextapi': api_step08<{}
              }
    elif result == 9:
        return{
             'id': 'step3',
              'nextapi': api_step09<{}
              }
    elif result == 10:
        return{
             'id': 'step3',
              'nextapi': api_step010<{}
              }
    elif result == 11:
        return{
             'id': 'step3',
              'nextapi': api_step011<{}
              }
    elif result == 12:
        return{
             'id': 'step3',
              'nextapi': api_step012<{}
              }
    elif result == 13:
        return{
             'id': 'step3',
              'nextapi': api_step013<{}
              }
    elif result == 14:
        return{
             'id': 'step3',
              'nextapi': api_step014<{}
              }
    elif result == 15:
        return{
             'id': 'step3',
              'nextapi': api_step015<{}
              } 
    elif result == 16:
        return{
             'id': 'step3',
              'nextapi': api_step016<{}
              }

    return{
        'id': 'step3',
        'nextapi': api_step017 <{}
    }


def api_step01(args): 
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step01',
        'items': [{
            'type': 'image',
            'src': res(302099003)
        }],
        'nextapi': api_step3_1 <{}
    }


def api_step02(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step02',
        'items': [{
            'type': 'image',
            'src': res(302107671)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step03(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step03',
        'items': [{
            'type': 'image',
            'src': res(302112274)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step04(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step04',
        'items': [{
            'type': 'image',
            'src': res(302129644)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step05(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step05',
        'items': [{
            'type': 'image',
            'src': res(302136353)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step06(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step06',
        'items': [{
            'type': 'image',
            'src': res(302142690)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step07(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step07',
        'items': [{
            'type': 'image',
            'src': res(302152841)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step08(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step08',
        'items': [{
            'type': 'image',
            'src': res(302161089)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step09(args): 
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step09',
        'items': [{
            'type': 'image',
            'src': res(308241940)
        }],
        'nextapi': api_step3_1 <{}
    }


def api_step010(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step010',
        'items': [{
            'type': 'image',
            'src': res(308259598)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step011(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step011',
        'items': [{
            'type': 'image',
            'src': res(308262426)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step012(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step012',
        'items': [{
            'type': 'image',
            'src': res(308278727)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step013(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step013',
        'items': [{
            'type': 'image',
            'src': res(308287465)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step014(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step014',
        'items': [{
            'type': 'image',
            'src': res(308292660)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step015(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step015',
        'items': [{
            'type': 'image',
            'src': res(308301724)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step016(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step016',
        'items': [{
            'type': 'image',
            'src': res(308315450)
        }],
        'nextapi': api_step3_1 < {}
    } 

def api_step017(args):
    page.cards.alias('next').text('继续')   
    return{
        'id': 'step017',
        'items': [{
            'type': 'image',
            'src': res(308326090)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step3_1(args):
    page.cards.alias('next').text('继续')
    return{
        'id': 'step3_1',
        'items':[{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '看着这张卡片，开始我们的轮流解读吧\n 一个接一个，不能重复哦',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#DB7093	'
            }
        }],
        'nextapi': api_step3_2 < {}
    }

def api_step3_2(args):
    page.cards.alias('next').text('我们说完啦')
    return{
        'id': 'step3_2',
        'items':[{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '已经解释了几轮了，最初的目的达到了吗？',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#71C671	'
            }
        }],
        'nextapi': api_step4 < {}
    }

def api_step4(args):
    page.cards.alias('next').text('继续')
    return{
        'id': 'step4',
        'items':[{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '是不是被自己的想象力、\n创意力惊到了呢？',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#7A378B	'
            }
        },{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '是不是跟伙伴们的互动更多、\n更亲近了呢？',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#6CA6CD	'
            }
        }],
        'nextapi': api_end < {}
    }

def api_end(args):
    return {
        "next": False,
        "restart": True,
        'items': [{ 
            'type': 'text',
            'animation': 'fadeIn',
            'content': '\n可以换张卡片再来一次哦',
            'style': {
                'text-align': 'center',
                'font-size': 32,
                'color': '#616161'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '\n点击右上角的【目录】可以探索欧卡的其他玩法',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '\n注：参考书目《欧卡，翻转你的命运》 黄乔伊 著',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },{
            'type': 'image',
            'src': res(308809804)
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '<a href="https://mp.weixin.qq.com/s/AYAS6qYt5J_T8_HP16sO5Q">你需要更专业的帮助吗？</a>',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        }
        ]
    }