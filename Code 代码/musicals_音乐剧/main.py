from apps.momarket import ebook
from apps.momarket import music
from apps.momarket import share

def index(args):
    #清空当前用户的进度缓存，注意，请仅在调试的时候使用该功能
    ebook.delCache()
   
    #演示加上背景音乐，用音乐模块
    music.Music > {
        'id': 'bgm',
        'music': 'https://momoqn.looosen.cn/416464160', #defying gravity+me and the sky
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
            'background-color': '#E6E6FA'   #'#FDF5E6' F5FFFA
            #电子书容器样式
        },
        'interval':800,
        'next': {        
            'background' : '#FFFAFA',#背景  FFD39B
            'color' : 'black',
            'border-radius':20,
            'border': 'none'
            
        },
        'restart': {
            'background' : '#F5FFFA',#背景 E6E6FA
            'color' : 'black',
            'border': '#EEDD82'
        },
        'text-align':'center',
    }

    share.ShareInfo>{
        'title': '你真的看过音乐剧吗？',
        'desc':'测测你中音乐剧的毒有多深',
        'img-url':'https://momoqn.looosen.cn/416654635', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')

def api_start(args):
    page.world.alias('next').text('我绝对能全对！')
    return {
        "id": 'start',     #自定义id, 可以用来设置用户的进度，
        "next": True,    #是否显示继续按钮
        "restart": False,  #是否显示重新开始按钮
        "keep-scroll": True,
        'items': [ {
            'type': 'image',
            'src': res(416412769),
            'style':{'size':(1100,400)},
            'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
        },{
            'type': 'title',
            'content': '\n<span style="font-weight:bold; ">➡️音乐剧知识考核！⬅️</span>',
            'style':{
                'font-size': 42,
                'text-align': 'center'
            },
            'animation': 'rubberBand',
        },{
            'type': 'title',
            'content': '\n随着音乐剧在国内大火，',
            'style':{
                'font-size': 35,
                'text-align': 'center'
            },
            'animation': 'slideInUp',
        },{
            'type': 'title',
            'content': '被网易云推荐歌单轰炸过的你\n真的是音乐剧粉丝吗？',
            'style':{
                'font-size': 35,
                'text-align': 'center'
            },
            'animation': 'slideInUp',
        },{
            'type': 'title',
            'content': '\n从<span style="color: #218868 ">百老汇</span>到<span style="color: #DAA520 ">西区</span>，',
            'style':{
                'font-size': 40,
                'text-align': 'center'
            },
            'animation': 'slideInUp',
        },{
            'type': 'title',
            'content': '从<span style="color: #FF7F00 ">法剧</span>到<span style="color: #436EEE ">德奥</span>，',
            'style':{
                'font-size': 40,
                'text-align': 'center'
            },
            'animation': 'slideInUp',
        },{
            'type': 'title',
            'content': '看看下面这些题目你能拿多少分！',
            'style':{
                'font-size': 40,
                'text-align': 'center'
            },
            'animation': 'slideInUp', 
        }, {
            'type': 'image',
            'src': res(416423225),
            # 'style':{'size':(1100,400)},
            'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
        },],
        'nextapi': api_guess1 < {}  
        }

def api_guess1(args):    
    page.world.alias('next').text('答案')
    return  {
        "id": 'guess1',
        'items': [{
            'type': 'text',
            'content': '\n<span style="font-weight:bold;text-decoration:underline ">问题1</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面哪部剧不是四大音乐剧之一？\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416482000),
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': ' 歌 剧 魅 影 ' 
            },{
                'text': ' 悲 惨 世 界 ', 
                'value': 'radio2'
            },{
                'text': ' 巴 黎 圣 母 院',  #ans
                'value': 'radio3'
            },{
                'text': ' 猫 ', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess2 < {}  
        }

#answers[args.id] = args.answer.number  #记录id对应的答案
def guess2(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers = 0
    db1.set('ans', answers)
    if args.answer.number == 2:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 2:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是巴黎圣母院"

    return  {
        "id": 'guess2',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n四大音乐剧分别是<span style="color: #548B54 ">猫，悲惨世界，歌剧魅影和西贡小姐 </span> \n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416632665),
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题2</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面哪部剧在百老汇驻演时间最长？\n',
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
                'text': '  妈  妈  咪  呀  ' 
            },{
                'text': '  歌  剧  魅  影  ', #ans
                'value': 'radio2'
            },{
                'text': '  悲  惨  世  界  ', 
                'value': 'radio3'
            },{
                'text': ' 芝 加 哥  ', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess3 < {}  
        }
    

def guess3(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 1:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 1:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是歌剧魅影"

    return  {
            "id": 'guess3',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n<span style="color: #548B54 ">歌剧魅影</span>从1988年首演以来至今共有13150场演出，芝加哥紧随其后\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416496918),
            'style':{'size':(350,420)},
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题3</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面这段前奏出自哪一部音乐剧？\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'audio',
            'src': res('416431429'),
            'bgm-pause': True,
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': ' 亚 瑟 王 传 奇  ' 
            },{
                'text': ' 歌 剧 魅 影 ', 
                'value': 'radio2'
            },{
                'text': ' 摇 滚 红 与 黑 ',  #ans
                'value': 'radio3'
            },{
                'text': ' 摇 滚 莫 扎 特 ', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess4 < {}  
        }

def guess4(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 2:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 2:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是摇滚红与黑"

    return  {
            "id": 'guess4',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n这首歌是红与黑中于连演唱的荣耀向我俯首<span style="color: #548B54 ">La gloire a mes genoux</span>，个人感觉前奏风格有一点点像法扎萨聚聚的杀杀服你..',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416507771),
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题4</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面哪部音乐剧在今年（2019）没有来华巡演?\n',
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
                'text': '罗密欧与朱丽叶 ' 
            },{
                'text': '西区故事', #ans
                'value': 'radio2'
            },{
                'text': '玛蒂尔达', 
                'value': 'radio3'
            },{
                'text': '猫', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess5 < {}  
        }

def guess5(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 1:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 1:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是西区故事"

    return  {
            "id": 'guess5',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n今年的音乐剧多到爽(*¯︶¯*)',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '西区故事讲述了西区的<span style="color: #218868">两大帮派</span>经常在街头械斗，其中一个帮派首领的朋友<span style="color: #8B0A50 ">托尼</span>与另一个帮派首领的妹妹<span style="color: #CD3333">玛丽亚</span>相爱，最后双方首领大决斗造成了悲剧，<span style="color: #6B8E23">托尼惨死</span>的故事',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题5</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下图出自哪部音乐剧？\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416446328),
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '贝隆夫人 ' 
            },{
                'text': '西贡小姐 ', 
                'value': 'radio2'
            },{
                'text': '1789巴士底狱的恋人',  #ans
                'value': 'radio3'
            },{
                'text': '汉密尔顿', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess6 < {}  
        }

def guess6(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 2:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 2:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是1789巴士底狱的恋人"

    return  {
            "id": 'guess6',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(416511274),
        },{
            'type': 'text',
            'content': '\n1789巴士底狱的恋人讲述了在<span style="color: #218868 ">法国大革命</span>的浪场中，来自两个<span style="text-decoration:underline ">敌对阵营</span>的<span style="color: #8B0A50 ">奥兰普和罗南</span>从相遇、热恋、分别到重聚，经历了最疯狂和最浪漫的历史篇章',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n这一幕是1789中罗南和奥兰普的男女主对唱，超级甜^ω^ 🍬',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题6</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '以下哪部音乐剧不是改编真实历史事件？\n',
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
                'text': '汉密尔顿 ' 
            },{
                'text': '1789巴士底狱的恋人', 
                'value': 'radio2'
            },{
                'text': '西贡小姐',  #ans
                'value': 'radio3'
            },{
                'text': '悲惨世界', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess7 < {}  
        }

def guess7(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 2:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 2:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是西贡小姐"

    return  {
            "id": 'guess7',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(416523649),
        },{
            'type': 'text', 
            'content': '\n西贡小姐是基于歌剧<span style="color: #C67171 ">蝴蝶梦</span>以及越战历史背景的音乐剧，叙说了一名前<span style="color: #483D8B ">美国军人</span>克里斯(Chris）和一位无父无母的<span style="color: #CD00CD ">越南妓女</span>金（Kim）在一间<span style="color: #218868 ">西贡</span>的饭店相遇的故事。它但是并不是根据真实历史事件创作的\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416593600),
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题7</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '以下哪部音乐剧没有获得过托尼最佳音乐剧奖？\n',
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
                'text': '魔 法 坏 女 巫  ' #ans
            },{
                'text': ' 摩 门 经 ', 
                'value': 'radio2'
            },{
                'text': ' 致 埃 文 汉 森 ', 
                'value': 'radio3'
            },{
                'text': ' 汉 密 尔 顿 ', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess8 < {}  
        }

def guess8(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 0:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是魔法坏女巫"

    return  {
            "id": 'guess8',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\nWicked虽然取得了很大的商业成功但是无缘托尼奖',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n魔法坏女巫发生在一个神奇的、充满魔法的地方，<span style="color: #DAA520 ">广受欢迎的金发女生</span>Glinda，以及<span style="color: #218868 ">不被理解的绿色女生</span>Elphaba，两个看似不可能成为朋友的女生之间结下了深厚的友谊',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416535277),
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题8</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面这段音乐出自哪一部音乐剧?\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'audio',
            'src': res('416669946'),
            'bgm-pause': True,
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '  汉  密  尔  顿  '  #ans
            },{
                'text': '  阿  拉  丁  ', 
                'value': 'radio2'
            },{
                'text': '  吉  屋  出  租  ', 
                'value': 'radio3'
            },{
                'text': ' 图  兰  朵 ', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess12 < {}  
        }
    
def guess12(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 0:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是汉密尔顿"

    return  {
            "id": 'guess12',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': '\n亚历山大·汉密尔顿是美国的<span style="color: #218868 ">开国元勋</span>之一，也是美国的<span style="color: #DAA520">第一任财政部长</span>。汉密尔顿音乐剧讲述的是他一生的故事。',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'image',
            'src': res(416609076),
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题9</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面哪部音乐剧没有同时拥有德法两版（剧名不重要）？\n',
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
                'text': '罗密欧与朱丽叶 ' 
            },{
                'text': '亚瑟王传奇', 
                'value': 'radio2'
            },{
                'text': '莫扎特 ', 
                'value': 'radio3'
            },{
                'text': '伊丽莎白', #ans
                'value': 'radio4'
            },]
        }],
        'nextapi': guess9 < {}  
        }
    
def guess9(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 3:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 3:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是伊丽莎白"

    return  {
            "id": 'guess9',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(416542880),
        },{
            'type': 'text',
            'content': '\n一粒沙只有德版',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n这部剧讲述了<span style="color: #CD950C ">奥地利与匈牙利王后伊丽莎白</span>的故事，从她1854年的<span style="color: #CD2990 ">订婚和结婚</span>开始，直至她在1898年<span style="color: #483D8B ">被刺杀</span>为止，刻画了她的婚姻和她的帝国走向衰亡的过程',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">问题10</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面哪部音乐剧还没有出过中文改编版？\n',
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
                'text': ' 罗 密 欧 与 朱 丽 叶  ' #ans
            },{
                'text': ' 堂 吉 柯 德 ', 
                'value': 'radio2'
            },{
                'text': ' 猫 ', 
                'value': 'radio3'
            },{
                'text': ' 悲 惨 世 界 ', 
                'value': 'radio4'
            },]
        }],
        'nextapi': guess10< {}  
        }

def guess10(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if args.answer.number == 0:
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n正确答案是罗密欧与茱丽叶"

    return  {
            "id": 'guess10',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'image',
            'src': res(416553829),
        },{
            'type': 'text',
            'content': '\n至于改编的都怎么样，这里不予评价…',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'text',
            'content': '\n\n<span style="font-weight:bold;text-decoration:underline ">附加题!😊</span>',
            'style':{'font-size':40},
            'animation': 'rubberBand',
        },{
            'type': 'text',
            'content': '下面哪首歌不是音乐剧剧中经典曲目？\n(多选, 答案有两个)\n',
            'style':{
                'font-size':35,
                'text-align': 'left'
                }
        },{
            'type': 'checkbox',
            'style':{
                'justify-content': 'center',
            },
            'checkboxs':[{
                'text': 'All that jazz ' 
            },{
                'text': 'Defying gravity', 
                'value': 'radio2'
            },{
                'text': 'Le Carnivore ',  #ans
                'value': 'radio3'
            },{
                'text': 'La gloire à mes genoux', 
                'value': 'radio4'
            },{
                'text': 'Déchiré', 
                'value': 'radio5'
            },{
                'text': 'Avoire 20 ans ',  #ans
                'value': 'radio6'
            },{
                'text': 'Ich bin extraordinär', 
                'value': 'radio7'
            },{
                'text': 'Think of me ', 
                'value': 'radio8'
            },]
        }],
        'nextapi': guess11 < {}  
        }


def guess11(args):    
    page.world.alias('next').text('来看一下分数吧')
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    ret = ""
    for check in args.answer.checks:
        ret = ret + "%s" % (check['number'])

    if ret == "25" or ret == "52":
        a = db1.get('ans') + 10
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)

    result = ""
    if ret == "25" or ret == "52":
        result = "答对啦！!🎉"
    else:
        result = "答错了...😢\n答案是<span style='color: #548B54 '> Le Carnivore 和 Avoire 20 ans</span>"

    return  {
        "id": 'guess10',
        'items': [{
            'type': 'text',
            'content': result,
            'style':{'font-size':35}
        },{
            'type': 'text',
            'content': "Le carnivore人为刀俎收录在了法扎专辑里但是并没有在剧中出现，Avoire 20 ans二十当头是法罗朱返场曲之一，也没有在剧里出现。",
            'style':{'font-size':35}
        },],
        'nextapi': score < {}  
    }

def score(args):
    page.world.alias('next').text('继续')
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    res = str(db1.get('ans'))

    comment = ""
    if res == '0' or res == '10' or res == '20':
        comment = "是新人吧～欢迎入坑"
    elif res == '30' or res == '40' or res == '50':
        comment = "厉害了，都是被音乐剧\n毒荼的同道中人"
    else:
        comment = "给您跪下，阅剧量\n可以当剧评了吧"

    return{
        "id": 'score',
        'items': [{
            'type': 'text',
            'content': '\n\n总分：',
            'style':{'font-size':38}
        },{
            'type': 'text',
            'content': str(db1.get('ans')),
            'style':{
                    'font-size': 80,
                    'color' : '#9A32CD'
                },
            'animation': 'rubberBand'
        },{
            'type': 'text',
            'content': comment,
            'style':{'font-size':45,},
        },
        ],
        'nextapi': api_end <{}
    }

def api_end(args):
    return {
        "next": False,
        "restart": True,
        'items': [{
            'type': 'text',
            'content': "\n\n恭喜你获得托尼小杯一份 :D",
            'style':{
                'font-size':35,
                'color': '#458B74',
            }
        },{
            'type': 'image',
            'src': res(416613708),
            'animation': 'wobble',
            'animation-duration': '3s',
            'style': {'size': (400, 700)}
        },
        ]
    }