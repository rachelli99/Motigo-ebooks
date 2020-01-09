from apps.momarket import ebook
from apps.momarket import music
from apps.project2.list1 import directorys
from apps.momarket import share


def index(args):
    #清空当前用户的进度缓存，注意，请仅在调试的时候使用该功能
    ebook.delCache()

    #点击继续按钮形式
   
    #演示加上背景音乐，用音乐模块
    music.Music > {
        'id': 'bgm',
        'music': 'https://momoqn.looosen.cn/306371785', #best_day_of_my_life
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
        'title':'热情奔放的美洲',
        'desc':'南美和北美欢迎你的到来',
        'img-url':'https://momoqn.looosen.cn/312345881', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')


#<span style="color: #218868;font-weight:bold;text-decoration:underline ">
def api_start(args):
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            "keep-scroll": True,
            'items': [ {
                    'type': 'image',
                    'src': res(306628619),
                    'style':{'size':(1100,200)},
                    'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                }, {
                    'type': 'text',
                    'animation': 'rotateIn', #设置该段文字的动画
                    'content': '\n一提到美洲你是先想到汉堡薯条！\n\n',
                    'style':{'font-size':35}
                },{
                    'type': 'image',
                    'src':res(414157981),
                },{
                    'type': 'text',
                    'animation': 'rotateIn', #设置该段文字的动画
                    'content': '\n还是烤肉😋\n',
                    'style':{'font-size':35}
                },{
                    'type': 'image',
                    'src':res(414162692),
                },{
                    'type': 'text',
                    'animation': 'rotateIn', 
                    'content': '\n还是emmmm......\n',
                    'style':{'font-size':35}
                },{
                    'type': 'image',
                    'src':res(414173938),
                },{
                    'type': 'text',
                    'style':{'font-size':35},
                    'content': '\n希望不是这些，\n\n因为接下来的五道题和他们仨都没啥关系\n\n',
                }, {
                    'type': 'image',
                    'src':res(182611163),
                    'background-size':(10,10)
                   
                },{
                    'type': 'text',
                    'animation': 'rubberBand', #设置该段文字的动画
                    'content': '\n让我们直接开始吧！\n\n',
                    'style':{'font-size':35},
                },
            ],
            'nextapi': api_step1 < {}  #下一步调用哪个接口，不填写的话默认调用上一次设置的接口
        }

def api_step1(args):    
    print(args)
    page.world.alias('next').text('答案')
    return  {
        "id": 'step1',
        'items': [{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题1</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;color:#EE7600">金门大桥</span>峙于美国加利福尼亚州旧金山金门海峡之上，是世界著名的桥梁之一。下面哪个是它呢',
            'style':{'font-size':35}
        },{ 
            'type': 'image',
            'src': res(383419763) 
        },{ 
            'type': 'image',
            'src': res(383399656) 
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '图一' 
            },{
                'text': '图二', #ans
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
    if args.answer.number == 1:
        result = "不错哟, 答对了!"
    else:
        result = "答错了..."

    return  {
        "id": 'step2',
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
            'content': '\n图一是葡萄牙的<span style="color: #218868 ">里斯本大桥</span>，也被称为四月二十五号大桥。曾是欧洲第一长桥，世界第三长悬索桥，于<span style="color: #218868; ">1966年8月6日</span>开始通车。\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n图二是<span style="color: #218868 ">金门大桥</span>，它于<span style="color: #218868">1937年5月27日</span>开始通车。金门大桥桥身全长1900多米，历时4年，利用10万多吨钢材，耗资达3550万美元建成。\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题2</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '世界上拥有<span style="font-weight:bold;color:#EE7600">最长海岸线</span>的国家在美洲，它的海岸线长达202,080km！它是谁呢?',
            'style':{'font-size':35}
        },
        {
            'type': 'image',
            'src': res(383434123)
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '智 利' 
            },{
                'text': '巴 西',
                'value': 'radio2'
            },{
                'text': '美 国', 
                'value': 'radio3'
            },{
                'text': '加拿大', #ans
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
    if args.answer.number == 3:
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
            'content': '\n<span style="text-decoration:underline ">加拿大</span>是拥有世界上海岸线最长的国家。跟在加拿大其后的是<span style="color: #218868 ">挪威</span>(58,133km), <span style="color: #218868 ">印尼</span>(54,720km), <span style="color: #218868">俄罗斯</span>(37,653km), <span style="color: #218868">菲律宾</span>(36,289km)\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n上图的照片位于加拿大温哥华岛的海岸线\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题3</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面的这位<span style="font-weight:bold;color:#EE7600">哥伦比亚歌手</span>为多届世界杯表演过，请问她是谁？',
            'style':{'font-size':35}
        },{
            'type': 'audio',
            'src': res('315928137'),
            'bgm-pause': True,
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': 'Pitbull' 
            },{
                'text': 'Jennifer Lopez',
                'value': 'radio2'
            },{
                'text': 'Shakira', #ans
                'value': 'radio3'
            },{
                'text': 'Bruno Mars', 
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
    if args.answer.number == 2:
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
            'content': "\nShakira出生于1977年。她曾两次获得格莱美奖并在多届世界杯上表演过，代表作包括 Hips Don't Lie、Waka Waka、La la la等很多超级好听的歌！\n",
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题4</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '美国<span style="font-weight:bold;color:#EE7600">总统山</span>上的四位总统分别是哪四位？',
            'style':{'font-size':35}
        },
        {
            'type': 'image',
            'src': res(315935577)
        },
        {
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '华盛顿, 杰弗逊, 林肯, 罗斯福' #ans
            },{
                'text': '杰克逊, 华盛顿, 罗斯福, 林肯', 
                'value': 'radio2'
            },{
                'text': '华盛顿, 杰弗逊, 肯尼迪, 麦迪逊',
                'value': 'radio3'
            },{
                'text': '杜鲁门, 林肯, 约翰逊, 华盛顿',
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
    if args.answer.number == 0:
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
            'content': '\n建造于1927-1941年，美国总统山位于<span style="color: #218868;">拉什莫尔山国家纪念公园</span> (Mt. Rushmore)。总统山上的四位总统分别为乔治·华盛顿、托马斯·杰斐逊、西奥多·罗斯福和亚伯拉罕·林肯\n',
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
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题5</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '南美洲最多人说的的<span style="font-weight:bold;color:#EE7600">两种语言</span>是哪两种呢',
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(383462166)
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '英语，法语',
            },{
                'text': '西班牙语，葡萄牙语', #ans
                'value': 'radio2'
            },{
                'text': "英语，西班牙语",
                'value': 'radio3'
            },{
                'text': '西班牙语，法语', 
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
    if args.answer.number == 1:
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
            'type': 'image',
            'src': res(383448283)
        },{
            'type': 'text',
            'content': '\n上图为南美各个国家的官方语言\n\n<span style="color: #218868; ">西班牙语</span>为10个国家的官方语言，而<span style="color: #218868 ">葡萄牙语</span>因为巴西的人口数量使其成为另一最常见的语言\n\n跟在西语和葡语之后，接下来最常见的三个语言为英语，荷兰语和法语。\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
            }
        }],
        'nextapi': api_step7 < {}  
    }

def api_step7(args):    
    # score = 0

    # if answers['step1'] == 1: 
    #     score += 1
    # if answers['step2'] == 3:
    #     score += 1
    # if answers['step3'] == 2: 
    #     score += 1
    # if answers['step4'] == 0:
    #     score += 1
    # if answers['step5'] == 1:
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
            'content': '\n到这里我们的美洲之旅就告一段落了☺️',
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
                        'style':{'color': '#4682B4'}
                    }, {
                        "text": "欧洲听起来也不错呀",
                        'value':'radio3',
                        'style':{'color': '#A52A2A'}
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
        window.location.href = '/project2/europe/index'    
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