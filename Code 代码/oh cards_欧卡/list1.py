from apps.momarket import ebook

def index(args):
    #ebook.delCache()
    ebook.EBookList > {
        'directorys': directorys(),  #目录配置封装到了directorys函数，参照下方directorys函数的写法
        'home': index < {}   #目录的首页，根据首页缓存用户的目录进度
    }

def cards(args):
    #ebook.delCache()
    ebook.EBook > {
        'id': 'cards',   #必须指定id, 依据该id缓存进度
        'api': api_start < {'cards': 1},
        'container': {
        }
    }

    #演示悬浮右上角的目录
    ebook.EBookListZoom > {
        'directorys': directorys(),  #目录配置封装到了directorys函数，参照下方directorys函数的写法
        'home': index < {},    #目录的首页，根据首页缓存用户的目录进度
        'ebooklist': {
            #可修改目录框的样式
        },
        'button': {
            #可修改按钮样式，例如设置字体大小
            'font-size': 25,
            'text':'目录',
            'text-align':'center',
            'border-color' :'#96CDCD',
            'background': '#ABABAB'
        }
    }


def directorys():
    return [ {
                'title': '主选页面',  #分类标题
                'style': {      #标题样式
                    'background-color': '#EE6A50',
                    'color':'#FFFFFF'
                },
                'items': [
                    {
                        'url': 'https://momo.mogomiyou.com.cn/Rachel/main/index',   #每项对应的页面，也可以直接填写链接字符串
                        'title': '回到主页',
                        'thumb': {
                            'src': res('307677297'),  #封面图，可设置宽高等
                            'size': (80,60)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#DEDEDE'
                        }  
                    },
                ]
            },{
                'title': '自我探索与反思',
                'style': {      #标题样式
                    'background-color': '#EE6A50',
                    'color':'#FFFFFF'
                },
                'items': [
                    {
                        'url': 'https://momo.mogomiyou.com.cn/Rachel/self_explore/index',
                        'thumb': {
                            'src': res('307677297'),  #封面图，可设置宽高等
                            'size': (80,60)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#DEDEDE'
                        },
                        'title': '自我探索'
                    },
                    {
                        'url': 'https://momo.mogomiyou.com.cn/Rachel/self_problem/index',
                        'thumb': {
                            'src': res('307677297'),  #封面图，可设置宽高等
                            'size': (80,60)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#DEDEDE'
                        },
                        'title': '困扰应对'
                    }],
            }, {
                'title': '团队联想玩游戏',
                'style': {      #标题样式
                    'background-color': '#EE6A50',
                    'color':'#ffffff'
                },
                'items': [
                    {
                        'url': 'https://momo.mogomiyou.com.cn/Rachel/group_diss/index',
                        'thumb': {
                            'src': res('307677297'),  #封面图，可设置宽高等
                            'size': (80,60)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#DEDEDE'
                        },
                        'title': '一起说说说'
                    },{
                        'url': 'https://momo.mogomiyou.com.cn/Rachel/group_pn/index',
                        'thumb': {
                            'src': res('307677297'), 
                            'size': (80,60)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#DEDEDE'
                        },
                        'title': '正负我做主'
                    },{
                        'url': 'https://momo.mogomiyou.com.cn/Rachel/group_story/index',
                        'thumb': {
                            'src': res('307677297'),  
                            'size': (80,60)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#DEDEDE'
                        },
                        'title': '接龙讲故事'
                    }]
            }
        ]     