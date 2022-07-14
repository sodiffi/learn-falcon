import db

def create(data):
    sql=f"insert into translate(video_id,user_id,start_time,end_time,text) values('{data.video_id}','{data.user_id}','{data.start_time}','{data.end_time}','{data.text}')"
    return db.insert(sql)
