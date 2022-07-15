from ..database import db

def create(data):
    print("enter here")
    sql=f"insert into translate(video_id,user_id,start_time,end_time,text) values(\'{data['video_id']}\',\'{data['user_id']}\',\'{data['start_time']}\',\'{data['end_time']}\',\'{data['text']}\')"
    print("QQ")
    return db.insert(sql)
