#正负我做主

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
        'music': res(307769060), #destiny of love
        # 'https://cdn.motimaster.com/user_assets/5b68f6e01450620a09e3ad1d/20181228170438/1790094933.mp3',
        'loop': True,  #默认为True，可不填写
        'autoplay': True, #默认为True,可不填写
        ######################
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
        'title': '正负我做主',  #分享标题
        'desc': '练习自己的多元视角',   #分享描述  H5分享的时候才会用到
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
    # page.test.alias('next').text('你好')
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            'items': [ {
                    'type': 'image',
                    # 'animation': 'fadeIn',
                    'src': res(308055959),
                },{
                    'type': 'title',
                    'content': '世界是多维度的，对于一件事情\n的看法也是多维度的',
                    'animation-duration': '0.5s',
                    'style': {
                        'text-align': 'center',
                        'color': '#698B69',
                        'font-size': 36
                        # 'animation-duration': '2s',
                    },
                    'animation': 'slideInUp',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                    # "keep-scroll": False  
                }, {
                    'type': 'title',
                    'content': '让我们来一起练习自己的多元视角吧',  #通过一张卡片来了解你的内心情绪。\n你准备好了么？
                    'style': {
                        'text-align': 'center',
                        'color': '#CD5B45',
                        'font-size': 36
                    },
                    'animation-duration': '0.5s',
                    'animation': 'slideInUp',  
                }
            ],
            'nextapi': api_step1_0 < {} 
        }

def api_step1_0(args):
    page.cards.alias('next').text('来看个例子吧')   
    return{
        'id': 'step1_0',
        'items':[{
            'type': 'image',
            'src': res(309795212),
            'style': {'size': (300,165)}
        },{
            'type': 'text',
            'animation': 'slideInUp', 
            'content': '开始之前先团队定个目标吧\n（例如正负解释15次，建议以正向结束）',
            'style': {
                'text-align': 'center',
                'color': '#6CA6CD',
                'font-size': 32
            },
            'animation-duration': '0.5s',
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '选择一张卡牌并仔细看着这张它，\n它会有很多很多种解释。',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#DB7093	'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '请第一位成员以正向表述做出对卡牌的解释，也就是正面的、积极的、美好的、舒服的、\n开心的、有希望的……',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#7D26CD	'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '第二位成员请以负向表述来解释这张卡牌，也就是负面的、无奈的、厌恶的、难过的、\n哀伤的、无望的……',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#EE7600	'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '第三位成员做正向解读，\n第四位成员做负向解读，以此类推……',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#8B8B00	'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '请按照顺序轮流正负面表述，\n注意不能重复哦',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#DB7093	'
            }
        }],
        'nextapi': api_step1_1 < {} 
    }

def api_step1_1(args):
    page.cards.alias('next').text('继续')  
    return{
        'id': 'step1_1',
        'items':[{
            'type': 'image',
            'src': res(309828856),
            'style': {
                'size': (500,750)
                # 'float': 'center'
            } #滑梯欧卡
        },{
            'type': 'image',
            'src': res(309684426),
            'style': {'size': (550,1800)}
        }],
        'nextapi': api_step1 < {} 
    }

def api_step1(args):    
    print(args)
    page.cards.alias('next').text('选好了')   
    return{
        "id": 'step1',
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
            'type': 'text',
            'animation': 'fadeIn',
            'content': '看着这张卡牌，仔细体会一下，\n你的感受是什么？',
            'style':{
                'text-align': 'center',
                'font-size': 35,
                'color': '#1874CD'
            }
        }],
        'nextapi': api_step3_2< {}
    }

def api_step3_2(args):
    page.cards.alias('next').text('我们说完啦')
    return{
        'id': 'step3_2',
        'items':[{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '现在开始我们的正负向解读吧\n\n一个正向，一个负向\n轮流进行哦',
            'style':{
                'text-align': 'center',
                'font-size': 35,
                'color': '#68228B'
            }
        }],
        'nextapi': api_step4< {}
    }

def api_step4(args):
    page.cards.alias('next').text('继续')
    return{
        'id': 'step4',
        'items':[{
            'type': 'image',
            'src': res(308233623),
            'style': {'size': (700, 130)}
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '相信你们已经完成了很多轮次的正负向表述的\n游戏，现在再来看这张卡牌，\n它是正向还是负向的呢？',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#548B54'
            }
        }],
        'nextapi': api_step5< {}
    }

def api_step5(args):
    page.cards.alias('next').text('继续')
    return{
        'id': 'step5',
        'items':[{
            'type': 'image',
            'src': res(308863828),
            'style':{'size':(520, 260)}
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '我们面对外界时，经常有些自己的解释，这是好的！那是坏的！这个我喜欢！那个我讨厌！渐渐地世界被我们标签化了。',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#C67171	'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '有些时候，我们甚至容易陷于负能量，\n凡事先观察不好的部分，\n导致情绪与能量不自觉的被拉低。',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#EE7600'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '这个玩法可以让我们从不同角度看世界，逐渐将思维中性化，避免过于偏颇的主观判断。',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#009ACD'
            }
        }],
        'nextapi': api_step6< {}
    }

def api_step6(args):
    page.cards.alias('next').text('继续')
    return{
        'id': 'step6',
        'items':[{
            'type': 'image',
            'src': res(308186486),
        },{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '情绪也是这样，它来源于我们内在的信念和对于事件的解读，所以我们是可以选择自己的解读，进而决定自己的情绪和感受，让自己更舒服、更幸福的。',
            'style':{
                'text-align': 'center',
                'font-size': 32,
                'color': '#C67171	'
            }
        },{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '\n请记住，我们永远拥有\n选择的权力哦！',
            'style':{
                'text-align': 'center',
                'font-size': 48,
                'color': '#68228B'
            }
        },{
            'type': 'image',
            'src': res(308957203)
        }],
        'nextapi': api_end< {}
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
                'font-size': 35,
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