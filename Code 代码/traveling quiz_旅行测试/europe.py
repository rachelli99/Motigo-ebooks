from apps.momarket import ebook
from apps.momarket import music
from apps.project2.list1 import directorys
from apps.momarket import share


def index(args):
    #清空当前用户的进度缓存，注意，请仅在调试的时候使用该功能
    ebook.delCache()
   
    #演示加上背景音乐，用音乐模块
    music.Music > {
        'id': 'bgm',
        'music': res(313002233), #how far i'll go
        'loop': True,  #默认为True，可不填写
        'autoplay': True, #默认为True,可不填写
        'left': 20,
        'size': (80, 80),
        'background-image': res('105774590')
    }

    ebook.EBook > {
        'id': 'world',   #必须指定id, 依据该id缓存进度
        'api': api_start < {},  #问答开始时需要获取数据的接口
        'click-music': 'http://cdn.moastro.cn/user_assets/5cef4f38479833593c7f359b/20190701162501/click.mp3',  #设置点击按钮的音效
        'container': { 'background-color':'#FDF5E6'
            #电子书容器样式
        },
        'interval':1000,
        'next': {        
            'background' : '#FFD39B',#背景
            'color' : 'black',
            'border-radius':20,
            'border-color': '#EEDD82'
            
        },
        'restart': {
            'background' : '#FFD39B',#背景
            'color' : 'white',
            'border-color': '#EEDD82'
            
        },
        'text-align':'center',
    }

    
    ebook.EBookListZoom > {
        'directorys': directorys(),  #目录配置封装到了directorys函数，参照下方directorys函数的写法
        'ebooklist': {
            #可修改目录框的样式
        },
        'home': '/project2/list1/index',
        'button': {
            #可修改按钮样式，例如设置字体大小
            'font-size': 25,
            'text':'地图',
            'text-align':'center',
            'border-color' :'#96CDCD',
            'left':650
        },
    }

    share.ShareInfo>{
        'title':'历史悠久的欧洲',
        'desc':'一个充满历史和文化沉淀的洲',
        'img-url':'https://momoqn.looosen.cn/312345881', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')


def api_start(args):
    page.world.alias('next').text('我准备好啦')
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            "keep-scroll": True,
            'items': [{
                    'type': 'image',
                    'src': res(306635655),
                    'style':{'size':(1100,200)},
                    'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                   
                }, {
                    'type': 'text',
                    'animation': 'rotateIn', #设置该段文字的动画
                    'content': '欧洲最早的人类居住遗迹\n可以回溯到公元前35000年的\n欧洲旧石器时代......\n',
                    'style':{'font-size':35}
                },{
                    'type': 'text',
                    'style':{'font-size':35},
                    'content': '\n介于它的历史太丰厚了\n我们还是不了解了吧嘿嘿~\n',
                }, {
                    'type': 'image',
                    'src':res(313408703),
                    'background-size':(20,20)
                   
                },{
                    'type': 'text',
                    'animation': 'rubberBand', #设置该段文字的动画
                    'content': '\n不要管历史了，\n\n还是来看看你能答出几道题吧！\n',
                    'style':{'font-size':35},
                },
            ],
            'nextapi': api_step1 < {}  #下一步调用哪个接口，不填写的话默认调用上一次设置的接口
        }
#<span style="color:#218868;font-weight:bold;text-decoration:underline">
def api_step1(args):    
    print(args)
    page.world.alias('next').text('答案')
    return  {
        "id": 'step1',
        'items': [{
            'type': 'text',
            'content': '\n接下来有五个问题\n',
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline">问题1</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '世界上最小的国家<span style="font-weight:bold;color:#EE7600">梵蒂冈</span>在欧洲，\n下面那张图是它呢',
            'style':{'font-size':35}
        },{ 
            'type': 'image',
            'src': res(414337824) 
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '图一' #ans
            },{
                'text': '图二',
                'value': 'radio2'
            },]
        }],
        'nextapi': api_step2 < {}  
        }

answers = {}
def api_step2(args):    
    page.world.alias('next').text('答案')

    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    result = ""
    if args.answer.number == 0:
        result = "不错哟, 答对了!"
    else:
        result = "答错了..."

    return  {
        "id": 'step2',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n图一是<span style="color:#218868">梵蒂冈</span>。梵蒂冈是全球领土面积最小、人口最少的国家，它的面积仅有<span style="color:#218868">0.44平方公里</span>。\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n图二是<span style="color:#218868">圣彼得堡</span>。圣彼得堡位于<span style="color:#218868">俄罗斯的西北部</span>，它是世界上人口超过百万的城市中位置最北的一个\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline">问题2</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下列那个城市不是欧洲国家的<span style="font-weight:bold;color:#EE7600">首都</span>呢',
            'style':{'font-size':35}
        },
        {
            'type': 'image',
            'src': res(315455415)
        },
        {
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '奥 斯 陆' 
            },{
                'text': '里 斯 本',
                'value': 'radio2'
            },{
                'text': '苏 黎 世', #ans
                'value': 'radio3'
            },{
                'text': '哥本哈根',
                'value': 'radio4'
            },]
        }],
        'nextapi': api_step3 < {}  
    }

def api_step3(args):    
    page.world.alias('next').text('答案')

    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    result = ""
    if args.answer.number == 2:
        result = "不错哟, 答对了!"
    else:
        result = "答错了..."

    return  {
        "id": 'step3',
        'items': [
        #     {
        #     'type': 'text',
        #     'content': answers
        # },
        {
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n苏黎世是瑞士最大的城市，但它不是瑞士的首都哦。瑞士的首都是<span style="color:#218868">伯尔尼</span>\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline">问题3</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面的这首音乐来自于一位欧洲著名的\n<span style="font-weight:bold;color:#EE7600">钢琴家、作曲家</span>请问他是谁？',
            'style':{'font-size':35}
        },{
            'type': 'audio',
            'src': res('315366085'),
            'bgm-pause': True,
        },{
            'type': 'text',
            'content': '提示：这位作曲家一生创作了许多夜曲，\n这就是其中的一首',
            'style':{
                'font-size':30,
                'color': '#999999'
            }
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '德彪西' 
            },{
                'text': '贝多芬',
                'value': 'radio2'
            },{
                'text': '莫扎特',
                'value': 'radio3'
            },{
                'text': '肖邦', #ans
                'value': 'radio4'
            },]
        }],
        'nextapi': api_step4 < {}  
        }

def api_step4(args):    
    page.world.alias('next').text('答案')

    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    result = ""
    if args.answer.number == 3:
        result = "不错哟, 答对了!"
    else:
        result = "答错了..."

    return  {
        "id": 'step4',
        'items': [
        #     {
        #     'type': 'text',
        #     'content': answers
        # },
        {
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n这首是肖邦\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(315473276),
            'style': {
                'size': (130,130),
                'float': 'left'
            }
        },{
            'type': 'image',
            'src': res(315409628),
            'style': {
                'size': (225,250),
                'float': 'center'
            }
        },{
            'type': 'text',
            'content': '众多夜曲中的一首。\n\n肖邦于1810年出生于波兰的华沙。他一共创作了21首夜曲，以及许多其他的类型如圆舞曲、前奏曲、谐谑曲、玛祖卡舞曲等',
            'style':{
                'font-size':35,
                'text-align': 'left'
            }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline">问题4</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下图是欧洲某国家著名的<span style="font-weight:bold;color:#EE7600">西红柿节  La Tomatina</span>。它是哪个国家呢？',
            'style':{'font-size':35}
        },
        {
            'type': 'image',
            'src': res(315525011)
        },
        {
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '奥地利' 
            },{
                'text': '西班牙', #ans
                'value': 'radio2'
            },{
                'text': '意大利',
                'value': 'radio3'
            },{
                'text': '希腊',
                'value': 'radio4'
            },]
        }],
        'nextapi': api_step5 < {}  
        }

def api_step5(args):    
    page.world.alias('next').text('答案')

    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    result = ""
    if args.answer.number == 1:
        result = "不错哟, 答对了!"
    else:
        result = "答错了..."

    return{
        "id": 'step5',
        'items': [
        #     {
        #     'type': 'text',
        #     'content': answers
        # },
        {
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n西红柿节始于1945年的<span style="color:#218868">布诺尔镇</span> (Buñol)。它的举行时间为每年8月最后一个星期三。\n游戏规则则是西红柿必须捏烂后才能出手^_^\n\n在2016年，数辆卡车拉来了<span style="color:#218868">160吨</span>番茄，<span style="color:#218868">2.2万</span>名狂欢者相互投掷番茄进行了长达一小时的番茄大战',
            'style':{
                'font-size':35,
                'text-align': 'left'
            }
        },{
            'type': 'text',
            'content': '\n下面是最后一个问题啦\n',
            'style':{
                'font-size':35,
                'text-align': 'center'
            }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline">问题5</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '每年法国都会举办著名的<span style="font-weight:bold;color:#EE7600">环法自行车赛</span>\n环法自行车赛每年于夏季举行，每次赛期23天，共21个赛段，平均赛程超过3500公里。下列那个是<span style="color:#218868">环法自行车赛的名字</span>呢？',
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(315553366)
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': 'Le Vélo de France',
            },{
                'text': 'Société de France',
                'value': 'radio2'
            },{
                'text': "L'Auto de France",
                'value': 'radio3'
            },{
                'text': 'Tour de France', #ans
                'value': 'radio4'
            }]
        }],
        'nextapi': api_step6 < {}  
    }

def api_step6(args):
    page.world.alias('next').text('继续')

    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    result = ""
    if args.answer.number == 3:
        result = "不错哟, 答对了!"
    else:
        result = "答错了..."
    
    return{
        "id": 'step6',
        'items': [ 
        #     {
        #     'type': 'text',
        #     'content': answers
        # },
        {
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n环法自行车赛的名字叫做<span style="color:#218868">Tour de France</span>\n每年都有一千五百万人参观环法自行车赛。\n\n在历届冠军中年龄最小的只有19岁最大的有36岁了呢',
            'style':{
                'font-size':35,
                'text-align': 'left'
            }
        }],
        'nextapi': api_step7 < {}  
    }

def api_step7(args):    
    page.world.alias('next').text('继续')
    # score = 0

    # if answers['step1'] == 0: 
    #     score += 1
    # if answers['step2'] == 2:
    #     score += 1
    # if answers['step3'] == 3: 
    #     score += 1
    # if answers['step4'] == 1:
    #     score += 1
    # if answers['step5'] == 3:
    #     score += 1

    # if score == 0:
    #     display = 315724376
    # elif score == 1: 
    #     display = 315734079
    # elif score == 2: 
    #     display = 315743322
    # elif score == 3:
    #     display = 315757498
    # elif score == 4:
    #     display = 315766139
    # else:
    #     display = 315775710
    return {
            "id": 'step7',
            'next': False,  #不显示下一步
            'items': [{
                'type': 'image',
                'src': res(415157200)
            },{
            'type': 'text',
            'content': '\n到这里我们的欧洲之旅就告一段落了☺️',
            'style':{
                'font-size':35,
                'text-align': 'center'
                }
            },{
            'type': 'text',
            'content': '\n那么下一站你想去哪里呢',
            'style':{
                'font-size':35,
                'text-align': 'center'
                }
            },{
                'type': 'radio',
                'style': {'justify-content':'center'},
                "radios": [  {
                        "text": "想去亚洲看看",
                        'value':'radio2',
                        'style':{'color': '#548B54'}
                    }, {
                        "text": "或者去非洲",
                        'value':'radio2',
                        'style':{'color': '#A52A2A'}
                    }, {
                        "text": "美洲听起来也不错呀",
                        'value':'radio3',
                        'style':{'color': '#4682B4'}
                    }, 
            ],
            
        }],
            'nextapi': api_step8 < {}
            
    }

def api_step8(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers = {}
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    
    if args.answer.number == 0:
        window.location.href = '/project2/asia/index'   
    elif args.answer.number == 1:
        window.location.href = '/project2/africa/index'    
    else:
        window.location.href = '/project2/america/index'    
    return {
            'id': 'step8',
            'nextapi': api_end< {}
        }


def api_end(args):
    return {
        "next": False,
        "restart": True,
        'items': [
        ]
    }