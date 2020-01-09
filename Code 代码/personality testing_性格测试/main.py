from apps.momarket import ebook
from apps.momarket import music
from apps.momarket import share

def index(args):
    #清空当前用户的进度缓存，注意，请仅在调试的时候使用该功能
    ebook.delCache()
   
    #演示加上背景音乐，用音乐模块
    music.Music > {
        'id': 'bgm',
        'music': 'https://momoqn.looosen.cn/423723670', #夜的钢琴曲们
        'loop': True,  #默认为True，可不填写
        'autoplay': True, #默认为True,可不填写
        'left': 20,
        'size': (80, 80),
        'background-image': res('105774590')
    }

    ebook.EBook > {
        'id': 'unicorn',   #必须指定id, 依据该id缓存进度
        'api': api_start < {},  #问答开始时需要获取数据的接口
        'click-music': 'http://cdn.moastro.cn/user_assets/5cef4f38479833593c7f359b/20190701162501/click.mp3',  #设置点击按钮的音效
        'container': { 
            'background-color': '#F0F8FF'   #'#FDF5E6' F5FFFA
            #电子书容器样式
        },
        'interval':1000,
        'next': {        
            'background' : '#E6E6FA',#背景  FFD39B
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
        'title': '拯救独角兽',
        'desc':'快来救出一只属于你的🦄️',
        'img-url':'https://momoqn.looosen.cn/425651806', 
        'success':shareSuccess<{}
    }

@pythonjs
def shareSuccess(args):
    alert('哇，感谢你的分享！')
#answers[args.id] = args.answer.number  #记录id对应的答案

def api_start(args):
    page.unicorn.alias('next').text('我准备好了')
    return {
        "id": 'start',     #自定义id, 可以用来设置用户的进度，
        "next": True,    #是否显示继续按钮
        "restart": False,  #是否显示重新开始按钮
        "keep-scroll": True,
        'items': [ 
            {
            'type': 'image',
            'src': res(424679475),
            #'style':{'size':(1100,400)},
            'animation': 'lightSpeedIn',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
        },{
            'type': 'text',
            'content': '\n很久很久以前，在遥远的地方有一个部落。这个部落的人们生活的开心幸福，因为在这片土地有一群能给人们带来好运独角兽们。\n',
            'style':{
                'font-size': 32,
                'text-align': 'left'
            },
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(423772599),
            #'style':{'size':(420,250)},
            'animation': 'slideInUp', 
        },{
            'type': 'text',
            'content': '（本文所有炫酷的图片都可以长按保存）',
            'style':{
                'font-size': 28,
                'color': '#ABABAB'
            },
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '\n这群独角兽每到春天就发出七彩的光，而看到它的光的人就会家庭祥和，富裕美满。',
            'style':{
                'font-size': 32,
                'text-align': 'left'
            },
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '在一天深夜里，一群黑衣人潜入了部落，偷走了独角兽们。从此之后这个部落一蹶不振……',
            'style':{
                'font-size': 32,
                'text-align': 'left'
            },
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '看着百姓流离，部落衰败，在下一个春天来临之前的寒冬，部落首领求助于部落里最有智慧的先知。',
            'style':{
                'font-size': 32,
                'text-align': 'left'
            },
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(423807888),
            'style':{'size':(400,270)},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '先知告诉首领，黑衣人来自西北的摩卡部落，只有最勇敢、睿智的战士才能冲破障碍，救回独角兽。',
            'style':{
                'font-size': 32,
                'text-align': 'left'
            },
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '于是勇士们踏上了寻找独角兽之旅，其中的一位就是你….',
            'style':{
                'font-size': 32,
                'text-align': 'left'
            },
            'animation': 'slideInUp',
        },],
        'nextapi': step1 < {}  
        }

def step1(args):    
    page.unicorn.alias('next').text('怎么办呢？')
    return  {
        "id": 'step1',
        'items': [{
            'type': 'text',
            'content': '\n按照先知给的羊皮卷',
            'style':{
                'font-size': 32,
                #'text-align': 'left'
            },
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '你穿过了雨林',
            'style':{'font-size': 32,},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(423859710),
            'style':{'size':(300,180)},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '渡过了大河',
            'style':{'font-size': 32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(423985706),
            #'style':{'size':(700,350)},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '走进了沙漠',
            'style':{'font-size': 32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(423904408),
            'style':{'size':(700,400)},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '又累又渴的你实在没有力气再坚持下去了',
            'style':{'font-size': 32},
            'animation': 'slideInUp', 
        },],
        'nextapi': step2 < {}  
    }

def step2(args):    
    page.unicorn.alias('next').text('继续')
    return  {
        "id": 'step2',
        'items': [{
            'type': 'text',
            'content': '\n突然你的眼前隐隐约约出现了一个隘口',
            'style':{'font-size': 32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '慢慢走近，隘口前面放置了三个不同的水果\n',
            'style':{'font-size':32, }
        },{
            'type': 'text',
            'content': '\n你向左看去\n',
            'style':{'font-size':32, }
        },{
            'type': 'image',
            'src': res(426013673),
        },{
            'type': 'text',
            'content': '再向中间看看\n',
            'style':{'font-size':32, }
        },{
            'type': 'image',
            'src': res(426021201),
            'style':{'size':(500,400)},
        },{
            'type': 'text',
            'content': '再往右边看\n',
            'style':{'font-size':32, }
        },{
            'type': 'image',
            'src': res(426032297),
        },{
            'type': 'text',
            'content': '饥渴难耐的你决定拿起\n',
            'style':{'font-size':32, }
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '绿油油的西瓜' 
            },{
                'text': '饱满欲滴的蜜桃', 
                'value': 'radio2'
            },{
                'text': '晶莹剔透的葡萄',  #ans
                'value': 'radio3'
            },]
        }],
        'nextapi': divide < {}  
        }
        

def divide(args):
    result = args.answer.number
    if result == 0:
        return{
            'id': 'divide',
            'items': [{
            'type': 'text',
            'content': '这时，西瓜后面的大门吱吱嘎嘎的打开了。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '一道告示出现在你面前：',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '“我已经等候很久了，欢迎来到黑山，\n等待你的将是许多道由重兵把守的关卡，\n只有最勇敢睿智的人才能成功闯关，\n并将得偿所愿，否则，\n哈哈哈哈……”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '勇士请进' 
            },{
                'text': '胆小鬼请回', 
                'value': 'radio2'
            },]
        }],
        'nextapi': watermelon <{}
        }
    elif result == 1:
        return{
            'id': 'divide',
            'items': [{
            'type': 'text',
            'content': '这时，蜜桃后面的大门吱吱嘎嘎的打开了。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '一道告示出现在你面前：',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '“我已经等候很久了，欢迎来到黑山，\n等待你的将是许多道由重兵把守的关卡，\n只有最勇敢睿智的人才能成功闯关，\n并将得偿所愿，否则，\n哈哈哈哈……”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '勇士请进' 
            },{
                'text': '胆小鬼请回', 
                'value': 'radio2'
            },]
        }],
        'nextapi': watermelon <{}
        }

    else:
        return{
            'id': 'divide',
            'items': [{
            'type': 'text',
            'content': '这时，葡萄后面的大门吱吱嘎嘎的打开了。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '一道告示出现在你面前：',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '“我已经等候很久了，欢迎来到黑山，\n等待你的将是许多道由重兵把守的关卡，\n只有最勇敢睿智的人才能成功闯关，\n并将得偿所愿，否则，\n哈哈哈哈……”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '勇士请进' 
            },{
                'text': '胆小鬼请回', 
                'value': 'radio2'
            },]
        }],
        'nextapi': watermelon <{}
        }

#########################################################################################
#########################################################################################

def watermelon(args):    
    page.unicorn.alias('next').text('继续')
    result = args.answer.number
    if result == 0:
        return{
            'id': 'watermelon',
            'items': [{
            'type': 'text',
            'content': '你勇敢的迈进了大门',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '出现在你跟前的是一条崎岖蜿蜒的石板路。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '走啊走啊，突然一道关卡出现在你眼前。\n你抬起头，赫然入目的是 “山海关 ”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        }],
            'nextapi': watermelon1 < {}  
        }
    return {
        'id': 'watermelon',
        'items': [{
            'type': 'text',
            'content': '你的心里有一丝恐惧',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '但想起临行前首领和村民们的期待，\n你还是鼓起勇气走了进去。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '你抬起头，赫然入目的是 “山海关 ”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        }],
        'nextapi': watermelon1 < {}  
    }

def watermelon1(args):
    return{
        'id': 'watermelon1',
        'items': [{
            'type': 'text',
            'content': '走近山海关，门口的卫兵拿起了一张图片\n\n并严肃的说："凭你的第一感觉，快速回答我！图中的女人为何掩面？她的情绪是怎样的？"',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424119325),
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '悲伤，女人发现丈夫的婚外情' 
            },{
                'text': '忧虑，丈夫酒醉在床上', 
                'value': 'radio2'
            },{
                'text': '关心，丈夫病重躺在床上，可能即将死去 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon2 < {}  
    }

def watermelon2(args):    
    page.unicorn.alias('next').text('继续')
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers = 0
    db1.set('ans', answers)
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 2
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 3
        db1.set('ans', a)

    return  {
        'id': 'watermelon2',
        'items': [{
            'type': 'text',
            'content': '“嗯，很好，继续前行。前面还有很多关卡，\n祝你好运”。士兵说着，打开了关口。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '两岸的石壁越来越窄。突然，在路的右侧\n你发现了一只正伸着脖子，盯着你的小乌龟。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(426449265),
            #'style':{'size':(200,160)},
        },{
            'type': 'text',
            'content': '“带上我吧，我已经在这里被困了很久了”，\n小乌龟可怜兮兮的说着。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '仁慈的你带着小乌龟走啊走啊，峰回路转，\n你看到了一块石头，上面写着 “黄崖关”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '守门的卫兵拦下你，并说到：“年轻人啊，你只要能快速解答完我的困惑即可通过此关。图中床上女子状态怎样？”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424128745), #TAT2
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '身患重病' 
            },{
                'text': '沉睡', 
                'value': 'radio2'
            },{
                'text': '已死去 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon3 < {}  
    }

def watermelon3(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 2
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 3
        db1.set('ans', a)

    return  {
        'id': 'watermelon2',
        'items': [{
            'type': 'text',
            'content': '听到你的选择，侍卫点了点头，打开了关口。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '扑面而来的是习习的凉风，\n周围绿树成荫，小溪的水汩汩的流着。\n小乌龟跟你说：“感谢你，我的恩人，我们就此别过吧。希望你一路顺利。”', #作为报答，我只能告诉你下一个关卡你可能会觉得有点热。
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(425153069),
        },
#         {
#             'type': 'text',
#             'content': '\n你继续前行着，来到了 “居庸关 ”',
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },{
#             'type': 'text',
#             'content': '守门的卫兵拿着两根缠绕的水管，并说到：“这两根水管冷热交替，猜猜看，我现在手中感觉到的是”',
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },{
#             'type': 'image',
#             'src': res(424275486), # TAT8
#         },{
#             'type': 'radio',
#             'style':{
#                 'justify-content': 'center',
#             },
#             'radios':[{
#                 'text': '冰水' 
#             },{
#                 'text': '凉水', 
#                 'value': 'radio2'
#             },{
#                 'text': '温水 ', 
#                 'value': 'radio3'
#             },{
#                 'text': '热水 ', 
#                 'value': 'radio4'
#             },]
#         }],
#         'nextapi': watermelon4 < {}  
#     }

# def watermelon4(args):    
#     db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
#     if args.answer.number == 0:
#         a = db1.get('ans') + 0
#         db1.set('ans', a)
#     else:
#         a = db1.get('ans') + 0
#         db1.set('ans', a)
    
#     result = ""
#     if args.answer.number == 3:
#         result = "卫兵满意的点点头：“恭喜你答对了，这是铺满地毯的路，请放心的继续前行吧。”"
#     else:
#         result = "卫兵眉头一皱：“答错了！哼哼，你只能走这一条铺满荆棘的路。”"

#     return  {
#         'id': 'watermelon4',
#         'items': [{
#             'type': 'text',
#             'content': result,
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },
        {
            'type': 'text',
            'content': '一直走着，在路的尽头，你看到了\n “紫荆关 ”三个大字',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '旁边的卫兵指着墙上的图像，说：\n“图中戴领结的男子是女子的什么人？”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424132019), # TAT3
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '秘密情人' 
            },{
                'text': '老板或者顶头上司', 
                'value': 'radio2',
            },{
                'text': '可以帮助她的有权有势的人 ', 
                'value': 'radio3',
            },],
        }],
        'nextapi': watermelon5 < {}  
    }

def watermelon5(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 2
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 3
        db1.set('ans', a)

    return  {
        'id': 'watermelon5',
        'items': [{
            'type': 'text',
            'content': '嗯，士兵点着头，赞许了你的回答。\n并为你打开了关口。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '继续向前走，突然路边的两个人映入了\n你的眼帘，你好奇的看向他们',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '你觉得老妇人的眼神流露出怎样的情绪？',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424147556), # TAT4
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '邪恶，她们之间可能隐藏着冲突' 
            },{
                'text': '焦虑，关心', 
                'value': 'radio2'
            },{
                'text': '同情 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon6 < {}  
    }

def watermelon6(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 3
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 2
        db1.set('ans', a)

    return  {
        'id': 'watermelon6',
        'items': [{
            'type': 'text',
            'content': '你在心里对自己说：管她是什么情绪呢！我的肚子饿的不行了，还是先尽快找到吃得要紧。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '继续前行着，过了一会，只见一个馒头铺子出现在了路边。你向老板求两个馒头充饥。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image', 
            'src': res(425163368),
        },{
            'type': 'text',
            'content': '老板说：“我已在此地多年，我的客人\n必须要回答我的问题才能得到馒头。”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '“你看这幅画，我画的这个女\n正在打开房门，她打算做什么？”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },
#         {
#             'type': 'text',
#             'content': '“我有一个弟弟，有一天他摔了一跤导致他现在失去平衡卧床在家。你要是能说出他是怎么摔得我送你两个馒头。”',
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },{
#             'type': 'radio',
#             'style':{
#                 'justify-content': 'center',
#             },
#             'radios':[{
#                 'text': '向前摔' 
#             },{
#                 'text': '向后摔', 
#                 'value': 'radio2'
#             },{
#                 'text': '向左摔 ', 
#                 'value': 'radio3'
#             },{
#                 'text': '向右摔 ', 
#                 'value': 'radio3'
#             },]
#         }],
#         'nextapi': watermelon7 < {}  
#     }

# def watermelon7(args):    
#     db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
#     if args.answer.number == 0:
#         a = db1.get('ans') + 0
#         db1.set('ans', a)
#     else:
#         a = db1.get('ans') + 0
#         db1.set('ans', a)
    
#     result = ""
#     if args.answer.number == 1:
#         result = "“恭喜你答对了，这是两个馒头和我独家配制的酸梅汤，可以解乏提神醒脑并迅速恢复体能” 老板说道。"
#     else:
#         result = "“这都答不对，给你一杯水，你走吧” 老板说道。"

#     return  {
#         'id': 'watermelon7',
#         'items': [{
#             'type': 'text',
#             'content': result,
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },{
#             'type': 'text',
#             'content': '你继续前行着，来到了 “雁门关”',
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },{
#             'type': 'text',
#             'content': '守门的卫兵指了指自己曾经画的一幅画：“看看你和我想的一不一样，我画的这个女子正在打开房门，她打算做什么？”',
#             'style':{'font-size':32},
#             'animation': 'slideInUp',
#         },
        {
            'type': 'image',
            'src': res(424159408), # TAT5
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '她要进男友的房间，\n她一直很想看看房间里的布局陈设' 
            },{
                'text': '她下班了，刚刚回家', 
                'value': 'radio2'
            },{
                'text': '她准备拿东西，然后去做饭 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon8 < {}  
    }


def watermelon8(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 2
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 3
        db1.set('ans', a)

    return  {
        'id': 'watermelon8',
        'items': [{
            'type': 'text',
            'content': '“嗯，答的不错。这是两个馒头和我独家配制的酸梅汤，可以解乏提神醒脑并迅速恢复体能” 老板说道。',  #卫兵说：“怪不得你能来到这么远，果然厉害，你要再接再厉”，并打开了关门。
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '又走了很久，迎面而来的是一片热闹的集市。这里的交易很独特，只要凭自己的真实感受回答问题就能得到你想要的东西。',
            'style':{'font-size':32},
            'animation': 'slideInUp', 
        },{
            'type': 'image',
            'src': res(425638426),
        },{
            'type': 'text',
            'content': '你选择了一个品类齐全的小店，\n以便拿到自己最需要的东西。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '门口的牌子上写着：\n“这个人物打扮成这样是为什么？”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424172788), # TAT6
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '打扮成别人认不出来的样子去袭击仇人' 
            },{
                'text': '抢劫商店', 
                'value': 'radio2'
            },{
                'text': '参加万圣节活动 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon9 < {}  
    }

def watermelon9(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 2
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 3
        db1.set('ans', a)

    return  {
        'id': 'watermelon9',
        'items': [{
            'type': 'text',
            'content': '回答完，你拿上需要的东西继续前行。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '在集市的的出口一个人拦下了你，',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '他说到：“前面就是最后一关了。\n来，年轻人，吃点苹果吧。”', #回答对我的问题你就可以带上我所有的苹果：我有8个篮子装满了苹果，每个篮子都有苹果且苹果不超过3个，至少有几个篮子里的苹果数量相同？
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '“吃了我的苹果将有助你顺利通过下一关，”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(425642159),
            'style': {'size': (250,250)},
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '吃一个' 
            },{
                'text': '吃两个', 
                'value': 'radio2'
            },{
                'text': '吃三个 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon10 < {}  
    }

def watermelon10(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 0
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 0
        db1.set('ans', a)
    
    result = ""
    if args.answer.number == 0:
        result = "“恭喜你答对了，你现在是这些苹果的主人了”"
    else:
        result = "“答错了，不过没关系，刚跟你开个玩笑，请继续前行吧，祝你好运!”"

    return  {
        'id': 'watermelon10',
        'items': [
        #     {
        #     'type': 'text',
        #     'content': result,
        #     'style':{'font-size':32},
        #     'animation': 'slideInUp',
        # },
        {
            'type': 'text',
            'content': '吃下了苹果，想到即将要完成自己的使命了， \n你的心情变得愉悦了起来。',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },
        {
            'type': 'text',
            'content': '走出了集市，你来到了一片平原。\n四周的人烟渐渐的变得稀少，\n你抬头一看，“阳关”两个大字赫然入目，',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'text',
            'content': '守门的卫兵说：“这个女子化妆是为什么？”',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424184840), # TAT7
        },{
            'type': 'radio',
            'style':{
                'justify-content': 'center',
            },
            'radios':[{
                'text': '遮掩已经衰老的面容，并希望能够挽救婚姻危机' 
            },{
                'text': '以更加饱满的精神状态去见大客户', 
                'value': 'radio2'
            },{
                'text': '去和男朋友约会 ', 
                'value': 'radio3'
            },]
        }],
        'nextapi': watermelon_end < {}  
    }

def watermelon_end(args):    
    page.unicorn.alias('next').text('来看下你解救的独角兽')
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    if args.answer.number == 0:
        a = db1.get('ans') + 1
        db1.set('ans', a)
    elif args.answer.number == 1:
        a = db1.get('ans') + 2
        db1.set('ans', a)
    else:
        a = db1.get('ans') + 3
        db1.set('ans', a)

    total = db1.get('ans') 
    if total > 6 and total <12: #7-11
        return  {
            'id': 'watermelon_end',
            'items': [{
                'type': 'text',
                'content': '卫兵听完说：“怪不得你能来到这么远，\n果然厉害，你要再接再厉”，并打开了关门。',
                'style':{'font-size':32},
                'animation': 'slideInUp',
            },{
                'type': 'text',
                'content': '眼前渐渐的开阔了起来\n\n经历了几番风雨\n\n你终于来到了关押独角兽的城堡之一\n\n你不负部落的希望成功了',
                'style':{'font-size':32},
                'animation': 'slideInUp',
            }],
            'nextapi': unicorn_green < {}  
        }
    elif total > 11 and total < 17: #12-16
        return  {
            'id': 'watermelon_end',
            'items': [{
                'type': 'text',
                'content': '卫兵听完说：“怪不得你能来到这么远，\n果然厉害，你要再接再厉”，并打开了关门。',
                'style':{'font-size':32},
                'animation': 'slideInUp',
            },{
                'type': 'text',
                'content': '眼前渐渐的开阔了起来\n\n经历了几番风雨\n\n你终于来到了关押独角兽的城堡之一\n\n你不负部落的希望成功了',
                'style':{'font-size':32},
                'animation': 'slideInUp',
            },],
            'nextapi': unicorn_orange < {}  
        }
    else: #17-21
            return  {
            'id': 'watermelon_end',
            'items': [{
                'type': 'text',
                'content': '卫兵听完说：“怪不得你能来到这么远，\n果然厉害，你要再接再厉”，并打开了关门。',
                'style':{'font-size':32},
                'animation': 'slideInUp',
            },{
                'type': 'text',
                'content': '眼前渐渐的开阔了起来\n\n经历了几番风雨\n\n你终于来到了关押独角兽的城堡之一\n\n你不负部落的希望成功了',
                'style':{'font-size':32},
                'animation': 'slideInUp',
            },],
            'nextapi': unicorn_purple < {}  
        }

def unicorn_green(args):
    page.unicorn.alias('next').text('哇')
    return{
        'id': 'unicorn_green',
        'items': [{
            'type': 'text',
            'content': '恭喜你拯救了一只绿色的独角兽',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(426059010)
        },],
        'nextapi': api_last < {}          
    }

def unicorn_orange(args):
    page.unicorn.alias('next').text('哇')
    return{
        'id': 'unicorn_green',
        'items': [{
            'type': 'text',
            'content': '恭喜你拯救了一只橙色的独角兽',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(426066186)
        },],
        'nextapi': api_last < {}          
    }

def unicorn_purple(args):
    page.unicorn.alias('next').text('哇')
    return{
        'id': 'unicorn_green',
        'items': [{
            'type': 'text',
            'content': '恭喜你拯救了一只紫色的独角兽',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(426077257)
        },],
        'nextapi': api_last < {}          
    }

def api_last(args):
    page.unicorn.alias('next').text('了解更多')
    return{
        'id': 'unicorn_green',
        'items': [{
            'type': 'text',
            'content': '再次拿出先知给的羊皮卷，只见上面写着：\n',
            'style':{'font-size':32},
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424477248)
        },{
            'type': 'text',
            'content': '绿色的独角兽是一只非常善于隐藏自己的独角兽，没人知道它心里到底在想什么。同时它防御心理很强，不愿意轻易相信别人，大多时候宁愿自己独处也不愿意和其他独角兽在一起。也许它的魅力就在于神秘吧。很多独角兽都想接近它，但它内心与外界的距离感始终存在。它只有摆正对生活的态度，才能过上正常的快乐生活。其他独角兽的建议对它影响很大，它需要对这些建议进行过滤，有选择地采用，不要被这些建议搞得焦头烂额。\n',
            'style':{
                'font-size':32,
                'color': '#228B22',
                'text-align': 'left',
            },
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424486158)
        },{
            'type': 'text',
            'content': '橙色的独角兽是一只能想到就能做到的独角兽。它是个现实主义者，浪漫色彩非常淡薄，对金钱有一定的执着心。并且它头脑清晰，有很强的独创能力。踏实、勤奋是它的一惯风格，但它缺乏挑战新事务的勇气，再加上它平时比较少言，给其它独角兽感觉比较冷漠，往往需要一段时间才能融到团体中。橙色的独角兽知道自己凡事不应只顾及眼前，要学会长远的规划。过分谨慎也会令它错过很多机会。\n',
            'style':{
                'font-size':32,
                'color': '#FF7F00',
                'text-align': 'left',
            },
            'animation': 'slideInUp',
        },{
            'type': 'image',
            'src': res(424499178)
        },{
            'type': 'text',
            'content': '紫色的独角兽是一只性格开朗、乐观、平易近人的独角兽。在平时和朋友交往中能设身处地地为他们着想，另外善于在公众面前提升自己的形象，因此深受大家的信任。紫独角兽在群体中是个受欢迎的中心人物，它做事很慎重，谦恭有礼，即使再棘手的事情也能处理得恰倒好处。诚信是它重要的处事原则，它页具有压抑自己为别人着想的品质。紫色的独角兽知道自己应该适当学会拒绝，会让自己更快乐。',
            'style':{
                'font-size':32,
                'color': '#9B30FF',
                'text-align': 'left',
            },
            'animation': 'slideInUp',
        },],
        'nextapi': api_end < {}   
    }

def api_end(args):
    return {
        "next": False,
        "restart": True,
        'items': [{
            'type': 'text',
            'content': "\n你所拯救的独角兽便是你内心的幻想和精神活动的投射。刚才一部分关卡的问题则是来自主题统觉测验 “Thematic Apperception Test” 的问题。",
            'style':{
                'font-size':32,
                'color': '#A8A8A8',
                'text-align': 'left',
            }
        },{
            'type': 'text',
            'content': "这是1935年美国心理学家Henry Murray研究出的投射法个人测验来呈现测试者内心。",
            'style':{
                'font-size':32,
                'color': '#A8A8A8',
                'text-align': 'left',
            }
        }]
    }