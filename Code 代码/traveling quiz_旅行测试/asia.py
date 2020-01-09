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
        'music': 'https://momoqn.looosen.cn/306236943', #my_wish,
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
        # 'home': '/ebook/list/index',
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
        'title':'美食多多的亚洲',
        'desc':'每天吃的不重样，让你的灵魂绽放',
        'img-url':'https://momoqn.looosen.cn/312345881', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')



def api_start(args):
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            "keep-scroll": True,
            'items': [ {
                    'type': 'image',
                    'src': res(307225600),
                    'style':{'size':(1100,300)},
                    'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                   
                }, {
                    'type': 'text',
                    'animation': 'rotateIn', 
                    'content': '\n作为人口数量最多的洲',
                    'style':{'font-size':35}
                },{
                    'type': 'text',
                    'animation': 'rotateIn', 
                    'content': '\n和土地面积最大的洲\n',
                    'style':{'font-size':35}
                }, {
                    'type': 'text',
                    'animation': 'rotateIn', 
                    'content': '\n亚洲怎么还是各种美食最多的洲呢😌😌\n\n',
                    'style':{'font-size':35}
                   
                },{
                    'type': 'image',
                    'src':res(315827773),
                    #'background-size':(10,10)
                },{
                    'type': 'text',
                    'animation': 'rubberBand', #设置该段文字的动画
                    'content': '\n每天吃的不重样心里真是美滋滋，\n\n那你对自己的亚洲之旅有信心么？\n让我们来看一下你知道多少吧！\n\n',
                    'style':{'font-size':35},
                },
            ],
            'nextapi': api_step1 < {}  #下一步调用哪个接口，不填写的话默认调用上一次设置的接口
        }
#<span style="color: #218868;font-weight:bold;text-decoration:underline ">
def api_step1(args):    
    print(args)
    page.world.alias('next').text('答案')
    return  {
        "id": 'step1',
        'items': [{
            'type': 'text',
            'content': '\n接下来有五个问题来考验你\n',
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题1</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '\n筷子是亚洲都有的特色。\n请问哪个国家发明了<span style="font-weight:bold;color:#EE7600">筷子</span>',
            'style':{'font-size':35}
        },{ 
            'type': 'image',
            'src': res(315839878) 
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '中国' #ans
            },{
                'text': '日本',
                'value': 'radio2'
            },{
                'text': '韩国',
                'value': 'radio2'
            },{
                'text': '新加坡',
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
            'content': '\n筷子当然是中国发明的啦\n\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '传说<span style="color: #218868;">大禹</span>为了治水，三过家门而不入，平常吃饭也在野外。由于比较<span style="color: #218868; ">赶时间</span>，每次锅里的兽肉一熟，大禹就要抓来吃。但是刚出锅的肉太<span style="color: #218868; ">烫</span>了，所以大禹折了树枝，用树枝夹着吃。后来大家发现用树枝吃饭比较方便，经过不断改良，产生了筷子。\n\n',
            'style':{
                'font-size':32,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题2</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;color:#EE7600">米</span>是众多亚洲国家最喜爱的主食之一。它有很多很多种吃法...\n比如说直接吃',
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(383708513),
            'style':{'size':(400,320)}
        },{
            'type': 'text',
            'content': '炒一下',
            'style':{'font-size':35,}
        },{
            'type': 'image',
            'src': res(383673835),
            'style':{'size':(500,350)}
        },{
            'type': 'text',
            'content': '做成八宝饭',
            'style':{'font-size':35,}
        },{
            'type': 'image',
            'src': res(383718247),
            'style':{'size':(500,350)}
        },{
            'type': 'text',
            'content': '或者包成粽子',
            'style':{'font-size':35,}
        },{
            'type': 'image',
            'src': res(383692486),
            'style':{'size':(400,270)}
        },{
            'type': 'text',
            'content': '那下面的这两种米的做法分别是哪里的做法呢？',
            'style':{'font-size':37}
        },{
            'type': 'image',
            'src': res(383848949)
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '马来西亚, 泰国' 
            },{
                'text': '中国, 泰国', #ans
                'value': 'radio2'
            },{
                'text': '菲律宾, 马来西亚', 
                'value': 'radio3'
            },{
                'text': '泰国, 菲律宾',
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
    if args.answer.number == 1:
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
            'content': '\n图一是中国的云南的竹筒饭，图二是泰国的菠萝炒饭\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n<span style="text-decoration:underline ">竹筒饭</span>的做法很简单：砍下一节竹筒 ，装进适量的米和水，放在火堆中烤熟，当竹筒表层烧焦时，饭就熟了。劈开竹筒，米饭香软可口，有<span style="color: #218868 ">香竹之清香和米饭之芬芳</span>。\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n<span style="text-decoration:underline ">菠萝饭</span>具有正宗的泰国风味，因为它融<span style="color: #218868 ">甜、酸、辣、鲜、香</span>于一体。而且颜色丰富的它还没入口就已经让眼睛饱餐一顿了\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{ 
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题3</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面这段语音是不同亚洲国家语言的同一个表述，请问这段表述是什么',
            'style':{'font-size':35}
        },{
            'type': 'audio',
            'src': res('315851769'),
            'bgm-pause': True,
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '再见' 
            },{
                'text': '谢谢',
                'value': 'radio2'
            },{
                'text': '你好', #ans
                'value': 'radio3'
            },{
                'text': '不客气', 
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
            'content': '\n这些表述都在说你好哟\n\n它们分别是日语、韩语、印度语、泰语和越南语\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '<span style="font-weight:bold;text-decoration:underline ">问题4</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '在世界顶级的肉食料理中,<span style="font-weight:bold;color:#EE7600">日本和牛</span>的地位是牢不可破的。由于日本和牛的肉多汁细嫩、肌肉脂肪中饱和脂肪酸含量很低，风味独特，肉用价值极高，和牛肉是目前世界上最昂贵的牛肉。',
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(383913205)
        },{
            'type': 'image',
            'src': res(383924917)
        },{
            'type': 'text',
            'content': '\n请问被认为最高级的和牛吃法是什么？',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '铁板烧', 
            },{
                'text': '寿喜锅', 
                'value': 'radio2'
            },{
                'text': '炭烤',
                'value': 'radio3'
            },{
                'text': '刺身', #ans
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
    if args.answer.number == 3:
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
            'content': '\n刺身选用A5级的和牛。能选为刺身的牛肉都肉质细嫩柔软，毫不腥膻，还带有一丝丝清甜甘润，你唯一需要思考的只有一件事：如何让它不那么过分的好吃^ ^',
            'style':{
                'font-size':35,
                'text-align': 'left'
            }
        },{
            'type': 'image',
            'src': res(383937633)
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
            'content': '东南亚的水果可是出了名的好吃\n下列选项中的哪个水果并不在图片中呢？',
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(315879734)
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '菠萝蜜',
            },{
                'text': '红毛丹',
                'value': 'radio2'
            },{
                'text': "番石榴",
                'value': 'radio3'
            },{
                'text': '番茄枝', 
                'value': 'radio4'
            },{
                'text': '山竹',
                'value': 'radio5'
            },{
                'text': '荔枝', #ans
                'value': 'radio6'
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
    if args.answer.number == 5:
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
            'content': '\n荔枝并不在图片里哦~\n\n图片里分别是：山竹、龙眼、菠萝蜜、番石榴、锦灯笼、榴莲、番茄枝、红毛丹',
            'style':{
                'font-size':35,
                'text-align': 'left'
            }
        }],
        'nextapi': api_step7 < {}  
    }

def api_step7(args):    
    # score = 0

    # if answers['step1'] == 0: 
    #     score += 1
    # if answers['step2'] == 1:
    #     score += 1
    # if answers['step3'] == 2: 
    #     score += 1
    # if answers['step4'] == 3:
    #     score += 1
    # if answers['step5'] == 5:
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
            'content': '\n到这里我们的亚洲之旅就告一段落了☺️',
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
                        "text": "想去美洲看看",
                        'value':'radio2',
                        'style':{'color': '#4682B4'}
                    }, {
                        "text": "或者去非洲",
                        'value':'radio2',
                        'style':{'color': '#548B54'}
                    }, {
                        "text": "听起欧洲来也不错呀",
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
        window.location.href = '/project2/america/index'   
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