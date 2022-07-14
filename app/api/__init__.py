import json

def checkParm(cond, content):
    res = ""
    for i in cond:
        if(i not in content.keys()):
            res += "缺少必要參數 %s\n" % i
    
    return res



def default( obj):
    
    if isinstance(obj, bytearray):  # 返回内容如果包含bytearray类型的数据
        return str(obj, encoding='utf-8')
    else:
        return"omg"
