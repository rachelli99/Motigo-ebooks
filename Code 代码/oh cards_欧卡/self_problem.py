#困扰应对 
#self2

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
        'title': '困扰应对',  #分享标题
        'desc': '解答你的困惑与难题',   #分享描述  H5分享的时候才会用到
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
    page.cards.alias('next').text('我准备好了')
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            'items': [ {
                    'type': 'image',
                    # 'animation': 'fadeIn',
                    'src': res(307971811),
                },{
                    'type': 'title',
                    'content': '|| 请先选择一个安静的、不受打扰的环境 ||',
                    'animation-duration': '0.5s',
                    'style': {
                        'text-align': 'center',
                        'color': '#BDBDBD',
                        'font-size': 30
                    },
                    'animation': 'slideInUp',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                    # "keep-scroll": False  
                }, {
                    'type': 'title',
                    'content': '生活中总会有些这样那样的不如意，这样那样的困惑和难题，让我们为难、纠结、不知所措。',  
                    'style': {
                        #'text-align': 'center',
                        'color': '#698B69',
                        'font-size': 31
                    },
                    'animation-duration': '0.5s',
                    'animation': 'slideInUp',  
                },{
                    'type': 'title',
                    'animation': 'slideInUp', 
                    'content': '\n下面这些卡牌中任意一张都到代表着一个解决的方案、想法和行动，就让卡牌帮助我们看见自己的期待，寻找更多的应对措施吧。',
                    'style': {
                        #text-align': 'center',
                        'color': '#698B69',
                        'font-size': 31
                    },
                    'animation-duration': '0.5s',
                }],
            'nextapi': api_step1 < {}  #下一步调用哪个接口，不填写的话默认调用上一次设置的接口
        }

def api_step1(args): 
    page.cards.alias('next').text('我想好了')
    return{
        'id': 'step1',
        'items': [{
            'type': 'image',
            'src': res(308233623),
            'style':{'size': (650, 150)}
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '请先安静地坐下来，做三个缓慢而深长的呼吸，跟自己的身体有一个连接……',
            'style': {
                'color': '#6E6E6E', 
                'font-size':32
            }
        },{ 
            'type': 'text',
            'animation': 'fadeIn',
            'content': '在内心想像一个你最近的困惑或者需要解决的问题',
            'style': {
                'color': '#6E6E6E', 
                'font-size':32
            }
        }],
        'nextapi': api_step2 < {}
    }

def api_step2(args):    
    print(args)
    page.cards.alias('next').text('继续')   
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
    return{
        'id': 'step01',
        'items': [{
            'type': 'image',
            'src': res(302099003)
        }],
        'nextapi': api_step3_1 <{}
    }


def api_step02(args):
    return{
        'id': 'step02',
        'items': [{
            'type': 'image',
            'src': res(302107671)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step03(args):
    return{
        'id': 'step03',
        'items': [{
            'type': 'image',
            'src': res(302112274)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step04(args):
    return{
        'id': 'step04',
        'items': [{
            'type': 'image',
            'src': res(302129644)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step05(args):
    return{
        'id': 'step05',
        'items': [{
            'type': 'image',
            'src': res(302136353)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step06(args):
    return{
        'id': 'step06',
        'items': [{
            'type': 'image',
            'src': res(302142690)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step07(args):
    return{
        'id': 'step07',
        'items': [{
            'type': 'image',
            'src': res(302152841)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step08(args):
    return{
        'id': 'step08',
        'items': [{
            'type': 'image',
            'src': res(302161089)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step09(args): 
    return{
        'id': 'step09',
        'items': [{
            'type': 'image',
            'src': res(308241940)
        }],
        'nextapi': api_step3_1 <{}
    }


def api_step010(args):
    return{
        'id': 'step010',
        'items': [{
            'type': 'image',
            'src': res(308259598)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step011(args):
    return{
        'id': 'step011',
        'items': [{
            'type': 'image',
            'src': res(308262426)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step012(args):
    return{
        'id': 'step012',
        'items': [{
            'type': 'image',
            'src': res(308278727)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step013(args):
    return{
        'id': 'step013',
        'items': [{
            'type': 'image',
            'src': res(308287465)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step014(args):
    return{
        'id': 'step014',
        'items': [{
            'type': 'image',
            'src': res(308292660)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step015(args):
    return{
        'id': 'step015',
        'items': [{
            'type': 'image',
            'src': res(308301724)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step016(args):
    return{
        'id': 'step016',
        'items': [{
            'type': 'image',
            'src': res(308315450)
        }],
        'nextapi': api_step3_1 < {}
    } 

def api_step017(args):
    return{
        'id': 'step017',
        'items': [{
            'type': 'image',
            'src': res(308326090)
        }],
        'nextapi': api_step3_1 < {}
    }

def api_step3_1(args):
    return{
        'id': 'step3_1',
        'items':[{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '这是你的卡片',
            'style':{
                'text-align': 'center',
                'font-size': 35,
                'color': '#616161'
            }
        },{
            'type': 'title',
            'animation': 'fadeIn',
            'content': '接下来会有一些问题\n请在心里默默的思考你的答案',
            'style':{
                'text-align': 'center',
                'font-size': 35,
                'color': '#616161'
            }
        }],
        'nextapi': api_step4_2 < {}
    }
def api_step4_2(args):
    page.cards.alias('next').text('下一个问题')  
    return{
        'id': 'step4_2',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '看着这张卡片，你如何解释它呢？',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step4_0 < {}
    }

def api_step4_0(args):
    page.cards.alias('next').text('下一个问题')  
    return{
        'id': 'step4',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '基于这个解释，你的感受是什么？',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step4_1< {}
    }

def api_step4_1(args):
    page.cards.alias('next').text('下一个问题')  
    return{
        'id': 'step4',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '这会让你联想到什么吗？',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step4 < {}
    }

def api_step4(args):
    page.cards.alias('next').text('下一个问题')  
    return{
        'id': 'step4',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '这张牌代表着一个解决你的困扰的方案、或者想法和行动，你会怎么解释它呢？',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step5 < {}
    }

def api_step5(args):
    page.cards.alias('next').text('下一个问题') 
    return{
        'id': 'step5',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '它对你的启发是……',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step6 < {}
    }

def api_step6(args):
    page.cards.alias('next').text('下一个问题') 
    return{
        'id': 'step6',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '你当下可以采取的行动或者计划是……',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step7 < {}
    }

def api_step7(args):
    page.cards.alias('next').text('继续') 
    return{
        'id': 'step7',
        'items': [{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '。。。。。。。。。。。。。。。。。。。。',
            'style': {
                'color': '#6E6E6E', 
                'font-size':35
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '你打算什么时候开始做呢？怎么做？还有谁可以帮助或者支持到你？',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },
        ],
        'nextapi': api_step8< {}
    }

def api_step8(args):
    return{
        'id': 'step8',
        'items': [{
            'type': 'image',
            'src': res(308186486)
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '希望刚才的回答让你对该如何应对当下的困扰有了更好的想法',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#7D26CD'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '可以的话，请把这个具体的计划/行动写下来。',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#698B22'
            }
        },{ 
            'type': 'text',
            'animation': 'fadeIn',
            'content': '你还可以问问周围的朋友，他们如何解释这张卡牌，听听不同角度的解读，\n可能对你很有帮助哦。',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#6495ED'
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
            'content': '\n当然你可以重新选择一张牌，再来一次探索。',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '\n点击右上角的【目录】可以探索欧卡其他玩法哟',
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
            'src': res(309867746),
            'style': {'size': (400, 360)}
        },{
            'type': 'text',
            'animation': 'fadeIn',
            'content': '<a href="https://mp.weixin.qq.com/s/AYAS6qYt5J_T8_HP16sO5Q">你需要更专业的帮助吗？</a>',
            'style': {
                'text-align': 'center',
                'font-size': 30,
                'color': '#616161'
            }
        },]
    }