from apps.momarket import ebook

def index(args):
    ebook.delCache()
    ebook.EBookList > {
        'directorys': directorys(),  #目录配置封装到了directorys函数，参照下方directorys函数的写法
        'home': index < {}   #目录的首页，根据首页缓存用户的目录进度
    }

def world(args):
    ebook.delCache()
    #参照问答模块示例实现一个题目
    ebook.EBook > {
        'id': 'world',   #必须指定id, 依据该id缓存进度
        'api': api_start < {'world': 1},
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
            'text':'其他',
            'text-align':'center',
            'border-color' :'#96CDCD',
            
        }
    }


def directorys():
    return [ {
                'title': '主选页面',  #分类标题
                'style': {      #标题样式
                    'background-color': '#6E8B3D',
                    'color':'#FFF68F'
                },
                'items': [
                    {
                        'url': 'https://momo.mogomiyou.com.cn/project2/main/index',   #每项对应的页面，也可以直接填写链接字符串
                        'title': '回到主页',
                        'thumb': {
                            'src': res('312202961'),  #封面图，可设置宽高等
                            'size': (95, 90)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#D3D3D3'
                        }  
                    },
                    
                ]
            },{
                'title': '目的地',
                'style': {      #标题样式
                    'background-color': '#6E8B3D',
                    'color':'#FFF68F'
                },
                'items': [
                    {
                        'url': 'https://momo.mogomiyou.com.cn/project2/america/index',
                        'thumb': {
                            'src': res('312215029'),  #封面图，可设置宽高等
                            'size': (110,100)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#D3D3D3'
                        },
                        'title': '美洲'
                    },
                   
                    {
                        'url': 'https://momo.mogomiyou.com.cn/project2/asia/index',
                        'thumb': {
                            'src': res('312227370'),  #封面图，可设置宽高等
                            'size': (110,100)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#D3D3D3'
                        },
                        'title': '亚洲'
                    },
                    {
                        'url': 'https://momo.mogomiyou.com.cn/project2/europe/index',
                        'thumb': {
                            'src': res('312233804'),  #封面图，可设置宽高等
                            'size': (110,100)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#D3D3D3'
                        },
                        'title': '欧洲'
                    },
                    {
                        'url': 'https://momo.mogomiyou.com.cn/project2/africa/index',
                        'thumb': {
                            'src': res('312246290'),  #封面图，可设置宽高等
                            'size': (110,100)
                        },
                        'style': {
                            'color': '#2F4F4F',
                            'background-color':'#D3D3D3'
                        },
                        'title': '非洲'
                    }
                ]
            }
        ]     