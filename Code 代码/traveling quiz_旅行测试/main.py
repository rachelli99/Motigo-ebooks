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
        'music': 'https://momoqn.looosen.cn/306186412', #vacation
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
        'container': { 
            'background-color':'#FDF5E6'
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
            #目录的首页，根据首页缓存用户的目录进度
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
        'title':'听说你很喜欢旅行？来证明一下',
        'desc':'据说还没有人能全部答对....',
        'img-url':'https://momoqn.looosen.cn/312345881', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')



def api_start(args):
    page.world.alias('next').text('为啥嘞')
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            "keep-scroll": True,
            'items': [ {
                    'type': 'image',
                    'src': res(305126472),
                    'style':{'size':(1100,400)},
                    'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                   
                }, {
                    'type': 'text',
                    'style':{'font-size':35},
                    'animation': 'rotateIn',
                    'content': '听说你地理一直满分？！',
                    
                },{
                    'type': 'text',
                    'style':{'font-size':35},
                    'animation': 'rotateIn',
                    'content': '\n听说你是初中历史课代表？！',
                    
                },{
                    'type': 'text',
                    'animation': 'rotateIn', 
                    'content': '\n听说你从来不走丢？！',
                    'style':{'font-size':35}
                },{
                    'type': 'text',
                    'style':{'font-size':35},
                    'animation': 'rotateIn',
                    'content': '\n听说你喜欢到世界各地旅行！',
                    
                },{
                    'type': 'text',
                    'style':{'font-size':35},
                    'animation': 'rotateIn',
                    'content': '\n那你可来对地方了',
                    
                },{
                    'type': 'image',
                    #'src':res(312345881), 
                    'src':res(414379500),
                }
            ],
            'nextapi': api_step1 < {}  #下一步调用哪个接口，不填写的话默认调用上一次设置的接口
        }

def api_step1(args):    
    print(args)
    page.world.alias('next').text('嗯对')
    return  {
            "id": 'step1',
            'items': [{
                'type': 'text',
                'content': '\n因为你将被测试是否真正的了解世界各地\n',
                'style':{'font-size':35},
                'animation': 'slideInUp',
                'animation-duration': '3s'
            },{
                'type':'image',
                'src': res(414318903) 
            }, {
                'type': 'text',
                'content': '\n不过在开始之前我们先来看一个优秀的\n喜欢跑到世界各地跳舞的小哥哥\n',
                'style':{'font-size':35},
                'animation': 'slideInUp',
                'animation-duration': '3s'
            },{
                'type': 'text',
                'content': '（真的好看！）',
                'style':{
                    'font-size':30,
                    'color': '#969696'
                },
                'animation': 'slideInUp',
            },{
                'type': 'video',
                'src': res('312825501'),
                'bgm-pause': True,  #播放视频时候的背景音乐是否暂停
            },
            {
                    'type': 'text',
                    'content': '视频: "Where the Hell is Matt? 2012"\n作者: Matt Harding, Melissa Nixon\n编辑: Rachel',
                    'style':{
                        'font-size':30,
                        'color': '#969696'
                    }
            }, {
                'type': 'text',
                'content': '\n看看去了7482815209个国家的人家,\n\n再看看自己，hmmmm是不是有点小惭愧\n\n没事虽然没去过但是我们知道的多呀！',
                'style':{'font-size':35},
                'animation': 'slideInUp',
                'animation-duration': '3s'
            },
            ],
            'nextapi': api_step2 < {}  
        }
    
def api_step2(args):    
    print(args)
    page.world.alias('next').text('继续')
    return  {
            "id": 'step2',
            'items': [ {
                'type': 'text',
                'content': '\n那就让我们收拾行囊拿起护照开始吧',
                'style':{'font-size':35},
                'animation': 'slideInUp',
                'animation-duration': '3s'
            },{
                'type': 'image',
                'src': res(414308492),
                'style': {'size': (180,200)}
            }, {
                'type': 'text',
                'content': '\n首先来选择你的目的地',
                'style':{'font-size':35},
                'animation': 'slideInUp',
                'animation-duration': '3s'
            },],
            'nextapi': api_step5 < {}  
        }

def api_step5(args):    
    print(args)
    page.world.alias('next').text('继续')                
    return {
            "id": 'step4',
            'next': False,  #不显示下一步
            'items': [{
                'type':'image',
                'src': res(414328056) 
            }, {
                'type': 'radio',
                'style': {'justify-content':'center'},
                "radios": [  {
                        "text": "想去美食多多的亚洲",
                        'value':'radio2',
                        'style':{'color': '#548B54'}
                    }, {
                        "text": "想去热情奔放的美洲",
                        'value':'radio2',
                        'style':{'color': '#A52A2A'}
                    }, {
                        "text": "想去历史悠久的欧洲",
                        'value':'radio3',
                        'style':{'color': '#4682B4'}
                    }, {
                        "text": "想去原始淳朴的非洲",
                        'value':'radio4',
                        'style':{'color': '#EE7600'}
                    }, 
            ],
        },{
                'type': 'text',
                'content': '\n在右上角的【地图】可以更换你的选择哟',
                'style':{
                    'font-size':30,
                    'color': '#A8A8A8'
                    },
                'animation': 'slideInUp',
            },],
            'nextapi': api_step6 < {}
    }

def api_step6(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers = {}
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    
    
    if args.answer.number == 0:
        window.location.href = '/project2/asia/index'   
    elif args.answer.number == 1:
        window.location.href = '/project2/america/index'    
    elif args.answer.number == 2:
        window.location.href = '/project2/europe/index'    
    else:
        window.location.href = '/project2/africa/index'    
    return {
            'id': 'step6',
            'nextapi': api_end< {}
        }


def api_end(args):
    return {
        "next": False,
        "restart": True,
        'items': [
        ]
    }