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
        'music': 'https://momoqn.looosen.cn/306214761', #three_little_birds
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
        'title':'原始淳朴的非洲',
        'desc':'各种动物和各个部落融洽美满的生活',
        'img-url':'https://momoqn.looosen.cn/312345881', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')

def api_start(args):
    page.world.alias('next').text('准备好了')
    return {
            "id": 'start',     #自定义id, 可以用来设置用户的进度，
            "next": True,    #是否显示继续按钮
            "restart": False,  #是否显示重新开始按钮
            "keep-scroll": True,
            'items': [ {
                    'type': 'image',
                    'src': res(307238938),
                    'style':{'size':(1100,240)},
                    'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                   
                }, {
                    'type': 'text',
                    'animation': 'rotateIn', #设置该段文字的动画
                    'content': '\n非洲不仅是拥有国家数量最多的大洲！\n它还是人类文明的发源地！\n',
                    'style':{'font-size':35}
                }, {
                    'type': 'image',
                    'src':res(383954575),
                },{
                    'type': 'text',
                    'style':{'font-size':35},
                    'content': '\n以及动物们的天堂^_^\n\n',
                },{
                    'type': 'image',
                    'src':res(414122071),
                    'background-size':(100,100)
                },{
                    'type': 'image',
                    'src':res(414135681),
                    'background-size':(100,100)
                },{
                    'type': 'text',
                    'animation': 'rubberBand', #设置该段文字的动画
                    'content': '\n这么野生的大洲，\n你准备好开始你的探索了吗？\n',
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
            'content': '\n接下来有五个问题来考验你\n',
            'style':{'font-size':35}
        },{
            'type': 'text',
            #'content': '\n<span style="font-weight:bold;font-style:italic;text-decoration:underline ">问题1</span>',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题1</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '非洲的<span style="font-weight:bold;color:#EE7600">最西南端</span>是哪里？',
            'style':{'font-size':35}
        },{ 
            'type': 'image',
            'src': res(414006291) 
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '好  望  角' #ans
            },{
                'text': '马 达 加 斯 加',
                'value': 'radio2'
            },{
                'text': '马 六 甲 海 峡',
                'value': 'radio2'
            },{
                'text': '南  非  角',
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
            'content': '\n非洲的最西南端是好望角。好望角是西方的探险家欲为通往富庶的东方航道，故改称好望角。\n\n非洲的<span style="text-decoration:underline ">最南端</span>是<span style="color:#218868 ">厄加勒斯角</span>。厄加勒斯角位于好望角东南偏东方向约150km。\n\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题2</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面的动物们哪个是<span style="font-weight:bold;color:#EE7600">箭猪/豪猪</span>？',
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(384121107),
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '图一' 
            },{
                'text': '图二', 
                'value': 'radio2'
            },{
                'text': '图三', #ans
                'value': 'radio3'
            },{
                'text': '图四',
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
            'content': '\n图三才是正宗的豪猪',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n另外三张图都是不同品种的刺猬嘿嘿嘿\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n刺猬和豪猪是两种完全不同的动物\n\n<span style="text-decoration:underline ">刺猬</span>：体背和体侧满布棘刺，头、尾和腹面有毛。当受到惊吓时，全身棘刺竖立，卷成如刺球状，头和脚脚都会被藏起来\n\n<span style="text-decoration:underline ">豪猪</span>：从自肩部到尾部长满了长刺，刺的颜色黑白相间。在它受惊时，它尾部的刺会立即竖起\n\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '豪猪受惊时是这样子哒\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(384143316),
            'style':{'size':(400,250)}
        },{ 
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题3</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '非洲每年游客最多的国家是哪里？',
            'style':{'font-size':35}
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '肯尼亚' 
            },{
                'text': '摩洛哥',
                'value': 'radio2'
            },{
                'text': '南非', 
                'value': 'radio3'
            },{
                'text': '埃及', #ans
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
            'content': '\n<span style="text-decoration:underline ">埃及</span>是每年游客最多的非洲国家哦。埃及是四大文明古国，有着众多的古迹，例如雄伟壮阔的金字塔',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(414057259),
            'style':{'size':(400,250)}
        },{
            'type': 'text',
            'content': '\n被称为露天博物馆的卢克索',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(414065406),
            'style':{'size':(400,250)}
        },{
            'type': 'text',
            'content': '\n可以自由潜水的红海',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(414079116),
            'style':{'size':(400,250)}
        },{
            'type': 'text',
            'content': '\n以及很多其他的优美的风景和具有特色的文化建筑呢\n\n',
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
            'content': '下列哪个是<span style="font-weight:bold;color:#EE7600">非洲部落</span>的独特习俗。',
            'style':{'font-size':35} 
        },{
            'type': 'image',
            'src': res(414091624),
            'style':{'size':(400,250)}
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '女子割皮肤印花来诱惑男子', 
            },{
                'text': '练习往嘴里放盘子并以嘴大为美', 
                'value': 'radio2'
            },{
                'text': '拔掉门牙象征成年',
                'value': 'radio3'
            },{
                'text': '以上全都是', #ans
                'value': 'radio4'
            },]
        }],
        'nextapi': api_step5 < {}  
        }
#https://baijiahao.baidu.com/s?id=1626701019522695502&wfr=spider&for=pc
#https://wenku.baidu.com/view/2302993c58fafab069dc026b.html

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
            'content': '\n上面的选项全都是非洲部落的习俗\n\n',
            'style':{
                'font-size':30,
                'text-align': 'left'
            }
        },{
            'type': 'image',
            'src': res(414541220),
            'style':{'size':(400,250)}
        },{
            'type': 'text',
            'content': '在埃塞俄比亚的<span style="color: #218868 ">卡洛族</span>，姑娘们在进入青春期后时常要忍受剧痛，在胸部和腹部用刀在皮肤上切割出一些口子并把大量竹签插进伤口使它们<span style="color: #218868">呈现一定的图案</span>。这样，等伤口痊愈后,经过精心制作的图案便会保留在她们的胸部和腹部。\n',
            'style':{
                'font-size':30,
                'text-align': 'left'
            }
        },{
            'type': 'image',
            'src': res(414551897),
            'style':{'size':(400,250)}
        },{
            'type': 'text',
            'content': '\n埃塞俄比亚西南部的奥莫河流域的<span style="color: #218868;">穆尔西族</span>，穆尔西姑娘10岁左右就开始<span style="color: #218868;">练习往嘴里放盘子</span>，平时放在嘴里，吃喝时才摘下来。随着嘴唇越撑越大，最大的嘴唇能翻到头上把脸包住。\n',
            'style':{
                'font-size':30,
                'text-align': 'left'
            }
        },{
            'type': 'image',
            'src': res(414569948),
            'style':{'size':(400,250)}
        },{
            'type': 'text',
            'content': '\n另一个部落，<span style="color: #218868; ">慕库巴勒</span>的青年男女没到青春期来临的时候，都需要将自己的<span style="color: #218868;">下门牙给拔掉</span>，而上面的两个门牙也会被削成v字形状。据说之所以拔掉上门牙，是为了方便<span style="color: #218868 ">吹口哨</span>。因为这个部落里的人以打猎为生，没有通讯设备，所以只能用口哨声保持联络。',
            'style':{
                'font-size':30,
                'text-align': 'left'
            }
        },{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题5</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '这是哪个动物的叫声？',
            'style':{'font-size':35}
        },{
            'type': 'audio',
            'src': res(384091771)
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '河马',
            },{
                'text': '鳄鱼',  #ans
                'value': 'radio2'
            },{
                'text': "犀牛",
                'value': 'radio3'
            },{
                'text': '狮子', 
                'value': 'radio4'
            },]
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
            'type': 'text',
            'content': '\n这是鳄鱼的叫声哦\n',
            'style':{
                'font-size':35,
                'text-align': 'center'
            }
        },{
            'type': 'text',
            'content': '\n啥？你不信？\n',
            'style':{
                'font-size':35,
                'text-align': 'center'
            }
        },{
            'type': 'text',
            'content': '\n证据在这！\n',
            'style':{
                'font-size':35,
                'text-align': 'center'
            }
        },{
            'type': 'video',
            'src': res(384091771)
        },],
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
    # if answers['step4'] == 3:
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
            'content': '\n到这里我们的非洲之旅就告一段落了☺️',
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
                        "text": "或者去亚洲",
                        'value':'radio2',
                        'style':{'color': '#548B54'}
                    }, {
                        "text": "欧洲也不错",
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
        window.location.href = '/project2/asia/index'    
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