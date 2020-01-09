#主页

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
        'id': 'test',   #必须指定id, 依据该id缓存进度
        'api': api_start < {},  #问答开始时需要获取数据的接口
        'click-music': 'http://cdn.moastro.cn/user_assets/5cef4f38479833593c7f359b/20190701162501/click.mp3',  #设置点击按钮的音效
        'interval': 1500,       #items中每个item间隔多长时间出现，单位毫秒，默认1500，即1.5s
        # 'refresh-show-restart': True,  #重新进入页面的时候是否显示重新开始，默认False
        'container': {
            #电子书容器样式
            'background':'lightblue'
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
        'music': 'https://momoqn.looosen.cn/307744571',  #Do You
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
        'title': '欢迎来到欧卡的世界',  #分享标题
        'desc': '探索你的内心世界，解开你的心灵密码',   #分享描述  H5分享的时候才会用到
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
                    'src': res(301697860),
                },{
                    'type': 'title',
                    'content': '跟朋友一起玩会出现尬聊吗？',
                    # 'content': '牵动深层记忆，绘制专属于自己的心灵地图',
                    'animation-duration': '0.5s',
                    'style': {
                        'text-align': 'center',
                        'color': '#EE7600',
                        'font-size': 34
                        # 'animation-duration': '2s',
                    },
                    'animation': 'slideInUp',  #设置该段文字的动画， 动画名称列表参考https://daneden.github.io/animate.css/
                    # "keep-scroll": False  
                }, {
                    'type': 'title',
                    'content': '想营造活跃的团队氛围而苦于没有方法吗？',
                    # 'content': '准备好探索你的内心世界了吗？',  #通过一张卡片来了解你的内心情绪。\n你准备好了么？
                    'style': {
                        'text-align': 'center',
                        'color': '#698B69',
                        'font-size': 33
                    },
                    'animation-duration': '0.5s',
                    'animation': 'slideInUp',  
                },{
                    'type': 'title',
                    'animation': 'slideInUp', 
                    'content': '有些不如意或困惑不知如何应对吗？',
                    # 'content': '马上透过一张卡片，解开你的心灵密码',
                    'style': {
                        'text-align': 'center',
                        'color': '#B8860B',
                        'font-size': 34
                    },
                    'animation-duration': '0.5s',
                },{
                    'type': 'title',
                    'animation': 'slideInUp', 
                    'content': '想探索自己的内心世界，却又不知如何开始吗？',
                    'style': {
                        'text-align': 'center',
                        'color': '#7A378B',
                        'font-size': 31
                    },
                    'animation-duration': '0.5s',
                },{
                    'type': 'title',
                    'animation': 'slideInUp', 
                    'content': '欢迎来到OH Cards欧卡的世界!',
                    'style': {
                        'text-align': 'center',
                        'color': '#CD5C5C',
                        'font-size': 42
                    },
                    'animation-duration': '0.5s',
                }
            ],
            'nextapi': api_step1 < {}  #下一步调用哪个接口，不填写的话默认调用上一次设置的接口
        }

def api_step1(args):
    return{
        'id': 'step1',
        'items':[{
            # 'type':
        },{
            'type': 'image',
            # 'animation': 'slideInUp',
            'src': res(308186486)
        },{
            'type': 'text',
            'animation': 'slideInUp',
            'animation-duration': '0.5s',
            'style':{
                'font-size': 32,
                'color': '#698B22',
                'text-align': 'center'
            },
            'content': '欧卡又称为潜意识投射卡，在解读图像、文字或图像文字组合时，欧卡就会传递某种讯息。我们可以透过它来了解自我。'
        },{
            'type': 'text',
            'animation': 'slideInUp',
            'animation-duration': '0.5s',
            'style':{
                'font-size': 32,
                'color': '#DB7093',
                'text-align': 'center'
            },
            'content': '我们对于世界的认知来自自己过往的生命经验与内在信念，这些信息大部分存储在我们的潜意识中，有时候可能忘了它们的存在，但是它们却会对我们的行为举止有着重大的影响。'
        },{
            'type': 'text',
            'animation': 'slideInUp',
            'animation-duration': '0.5s',
            'style':{
                'font-size': 32,
                'color': '#CD8500',
                'text-align': 'center'
            },
            'content': '欧卡通过图像、文字等画面内容诱导出我们的生活精要、情感、个性倾向等心声。'
        }],
        'nextapi': api_step1_1< {}
    }

def api_step1_1(args):
    return{
        'id': 'step1_1',
        'items': [{
            'type': 'image',
            'src': res(303306071), #栗子
            'style':{
                'size': (500, 300)
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '在这张卡片里，你看到了什么？',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B',
                'text-align': 'center'
            }
        },{
            'type': 'image',
            'src': res(303275634) #捂脸
        }],
        'nextapi': api_step1_2 < {}
    }

def api_step1_2(args):
    return{
        'id': 'step1_2',
        'items': [{
            'type': 'title',
            'animation': 'slideInUp',
            'content': 'Rachel： ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            },
            'animation-duration': '0s'
        },{
            'type': 'image',
            'src': res(307682288),
            'style': {
                'size': (320,90),
                'float': 'left'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\nLandy: ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B',
                'text-align': 'right'
            }
        },{
            'type': 'image',
            'src': res(307699301),
            'style': {
                'size': (320,100),
                'float': 'right'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\nCoco: ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            },
            'animation-duration': '0s'
        },{
            'type': 'image',
            'src': res(307702712),
            'style': {
                'size': (330,100),
                'float': 'left'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': 'Jordan: ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B',
                'text-align': 'right'
            },
            'animation-duration': '0s'
        },{
            'type': 'image',
            'src': res(307711377),
            'style': {
                'size': (320,100),
                'float': 'right'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\nShelby:',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            },
            'animation-duration': '0s'
        },{
            'type': 'image',
            'src': res(307729986),
            'style': {
                'size': (330,100),
                'float': 'left'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\n\n\n那如果把它看作是解决你的困扰的一个行动或者想法，你会怎么解释呢?  ',
            'animation-duration': '4s',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            }
        }],
        'nextapi': api_step1_3 < {}
    }

def api_step1_3(args):
    return{
        'id': 'step1_3',
        'items':[{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\nLincy:',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            },
            'animation-duration': '0s'
        },{
            'type': 'image',
            'src': res(307807842),
            'style': {
                'size': (390,170),
                'float': 'left'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\n\n\nCarina: ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B',
                'text-align': 'right'
            },
            'animation-duration': '0s'
        },{
            'type': 'image',
            'src': res(307819956),
            'style': {
                'size': (320,100),
                'float': 'right'
            }
        }],
        'nextapi': api_step2 < {}
    }
    
def api_step2(args):
    return{
        'id': 'api_step2',
        'items': [{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\n\n\n每个人的人生经历都不同，所以对于同一张卡片，每个人都会有不同的解释 ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '因此，所有的解读讯息，都没有标准答案。以当事人依据当下感受解释卡牌，就是最合适的。 ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            }
        },{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '看了这么多，你是不是也想试一试呢？ ',
            'style':{
                'font-size': 30,
                'color': '#6C7B8B'
            }
        }],
        'nextapi': api_step3 <{}
    }

def api_step3(args):
    print(args)
    page.world.alias('next').text('继续')   
    return {
        'id': 'step3',
        'next': False,
        'items': [{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\n你想体验自我探索与反思还是团队联想玩游戏？\n点击右上角的【目录】可以更换你的选择 ',
            'style':{
                'font-size': 30,
                'color': '#698B69',
                'text-align': 'center'
            }
        },{
            'type': 'radio',
            'style': {'justify-content':'center'},
            "radios": [  {
                    "text": "自我探索与反思",
                    'value':'radio2'
                }, {
                    "text": "团队联想玩游戏",
                    'value':'radio2'
                }],            
        }],
        'nextapi': api_step4 <{}
    }

def api_step4(args):
    result = args.answer.number+1
    if result == 1:
        return{
            'id': 'api_step4',
            'nextapi': api_step5 <{}
        }
    return {
        'id': 'api_step4',
        'nextapi': api_step6 <{}
    }

def api_step5(args): #单人选项
    print(args)
    page.world.alias('next').text('继续')      
    return{
        'id': 'step5',
        'next': False,
        'items': [{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\n你想体验自我探索还是困扰应对？ ',
            'style':{
                'font-size': 30,
                'color': '#698B69',
                'text-align': 'center'
            }
        },{
            'type': 'radio',
            'style': {'justify-content':'center'},
            "radios": [  {
                    "text": "自我探索",
                    'value':'radio1'
                }, {
                    "text": "困扰应对",
                    'value':'radio2'
                }],            
        }],
        'nextapi': api_step7 <{}
    }

def api_step6(args): #多人选项
    print(args)
    page.world.alias('next').text('继续')   
    return{
        'id': 'step6',
        'next': False,
        'items': [{
            'type': 'title',
            'animation': 'slideInUp',
            'content': '\n请选择你想体验的游戏 ',
            'style':{
                'font-size': 30,
                'color': '#698B69',
                'text-align': 'center'
            }
        },{
            'type': 'radio',
            'style': {'justify-content':'center'},
            "radios": [  {
                    "text": "一起说说说",
                    'value':'radio2'
                }, {
                    "text": "正负我做主",
                    'value':'radio2'
                }, {
                    "text": "接龙讲故事",
                    'value':'radio3'
                }],            
        }],
        'nextapi': api_step8 <{}
    }

def api_step7(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers = {}
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    
    
    if args.answer.number == 0:
        window.location.href = '/Rachel/self_explore/index'   
    else:
        window.location.href = '/Rachel/self_problem/index'    
    return {
            'id': 'step7',
            'nextapi': api_end< {}
        }

def api_step8(args):    
    db1 = TinyDB(1036, 'UzfT721DhGColWXr') 
    answers = {}
    answers[args.id] = args.answer.number  #记录id对应的答案
    db1.set('answers', answers)
    
    
    if args.answer.number == 0:
        window.location.href = '/Rachel/group_diss/index'   
    elif args.answer.number == 1:
        window.location.href = '/Rachel/group_pn/index'    
    else:
        window.location.href = '/Rachel/group_story/index'    
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
