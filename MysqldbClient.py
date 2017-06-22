import Mysqldb

class MysqldbClient(object):
    def __init__(self, db, host, port, user, passwd):
        self.conn = Mysqldb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        self.cursor = conn.cursor()
        
    def insert(self, name, key, value):

        sql ='INSERT INTO {name}({key})'.format(name,key)
        self.cursor.execute(sql,value)


        
    def update(self, name, key, value, unique_key, unique_value):
        sql = 'select * from {name} where {unique_key} = {unique_value}'.format(name,unique_key,unique_value)
        self.cursor.execute(sql)
        result = self.cursor.fetchone() # 检查数据库是否有重复内容        
        if result:
            return None
        else:
            self.insert(name,key,value)
            
    def getall(self, name):
        sql = 'SELECT * FROM {name}'.format(name)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results
    
    def close(self):
        self.conn.close()
        self.cursor.close()
        
    def __enter__(self):
        pass
    
    def __exit__(self,  type, value, traceback):
        if type is None:
            self.conn.commit()
            self.close()
        else:
            self.conn.rollback()
        
    