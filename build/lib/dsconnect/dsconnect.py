class config_df(object):
    import pandas
    def __init__(self, df):
        self.config = df
# 01. Redshift
    def redshift(self,conid,sql):
        import psycopg2,pandas
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()        
        con = psycopg2.connect("dbname='"+str(config.dbname[0])+"' port='"+str(int(config.port[0]))+"' user='"+str(config.username[0])+"' password='"+str(config.password[0])+"' host='"+str(config.host[0])+"'")
        print('Connected to data source.')
        cur = con.cursor()        
        print('Query executing.')
        cur.execute(sql)
        try:
            df = pandas.DataFrame(cur.fetchall())
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df
# 02. MySQL database    
    def mysql(self,conid,sql):
        import mysql.connector,pandas
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()   
        con = mysql.connector.connect(user=str(config.username[0]), password=str(config.password[0]),host=str(config.host[0]),port = str(int(config.port[0])),database=str(config.dbname[0]))
        print('Connected to data source.')
        cur = con.cursor()
        print('Query executing.')
        cur.execute(sql)
        try:
            df = pandas.DataFrame(cur.fetchall())
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df
#03. Oracle database    
    def oracle(self,conid,sql):
        config = self.config
        import cx_Oracle,pandas
        config = (config[(config['conid'] == conid)]).reset_index()        
        con = cx_Oracle.connect(str(config.username[0])+'/'+str(config.password[0])+'@'+str(config.host[0])+':'+str(int(config.port[0]))+'/'+str(config.dbname[0]))
        print('Connected to data source.')
        cur = con.cursor()        
        print('Query executing.')
        cur.execute(sql)
        try:
            df = pandas.DataFrame(cur.fetchall())
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df
#04. IBM DB2 Database        
    def ibmdb(self,conid,sql):
        import ibm_db,pandas
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()        
        con = ibm_db.connect('DATABASE='+str(config.dbname[0])+';HOSTNAME='+str(config.password[0])+';PORT='+str(int(config.port[0]))+';UID='+str(config.username[0])+';PWD='+str(config.password[0])+';')
        print('Connected to data source.')
        cur = con.cursor()        
        print('Query executing.')
        cur.execute(sql)
        try:
            df = pandas.DataFrame(cur.fetchall())
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df    
#05. Microsoft SQL Server 
    def mssql(self,conid,sql):
        import pyodbc,pandas
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()        
        con = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+str(config.host[0])+";DATABASE="+str(config.dbname[0])+";UID="+str(config.username[0])+";PWD="+str(config.password[0]))
        print('Connected to data source.')
        cur = con.cursor()        
        print('Query executing.')
        cur.execute(sql)
        try:
            df = pandas.DataFrame([tuple(t) for t in cur.fetchall()])
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df
#06. Microsoft Azure Sql Database    
    def msazuresql(self,conid,sql):
        import pyodbc,pandas
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()
        con = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+str(config.host[0])+";DATABASE="+str(config.dbname[0])+";UID="+str(config.username[0])+";PWD="+str(config.password[0]))
        print('Connected to data source.')
        cur = con.cursor()
        
        print('Query executing...!')
        cur.execute(sql)
        try:
            df = pandas.DataFrame([tuple(t) for t in cur.fetchall()])
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df
#07. PostgreSQL Database    
    def postgresql(self,conid,sql):
        import psycopg2,pandas
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()        
        con = psycopg2.connect("dbname='"+str(config.dbname[0])+"' port='"+str(int(config.port[0]))+"' user='"+str(config.username[0])+"' password='"+str(config.password[0])+"' host='"+str(config.host[0])+"'")
        print('Connected to data source...!')
        cur = con.cursor()        
        print('Query executing.')
        cur.execute(sql)
        try:
            df = pandas.DataFrame(cur.fetchall())
            columnname = [i[0] for i in cur.description]
            df.columns = columnname
            print('Query Completed.')
        except:
            print('Query Completed.')
        con.commit()
        cur.close()
        con.close()
        return df
# 08. Googlesheets    
    def gsheet(self,conid):
        import pygsheets,os
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()
        path = str(config.conString[0])
        pwd = os.getcwd()
        os.chdir(path.replace('client_secret.json',""))
        con = pygsheets.authorize(path,no_cache=True)
        print('Connected to GSheet.')
        os.chdir(pwd)
        return con
    
    def sftp(self,conid):
        import pysftp
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        con = pysftp.Connection(str(config.host[0]),username=str(config.username[0]), password=str(config.password[0]), cnopts=cnopts)
        return con
    
    def s3connect(self,conid):
        import boto3,ast
        config = self.config
        config = (config[(config['conid'] == conid)]).reset_index()
        s3 = boto3.client('s3', aws_access_key_id=ast.literal_eval(config.conString[0])['accesskey'],aws_secret_access_key=ast.literal_eval(config.conString[0])['secretkey'])
        print('Connected to S3.')
        return s3
    
    def s3select(self,conid,bucket,path,select_stmnt,output_format,fielddelimiter):
        import boto3,ast
        config = self.config
        s3 = boto3.client('s3', aws_access_key_id=ast.literal_eval(config.conString[0]),aws_secret_access_key=ast.literal_eval(config.conString[0])['secretkey'])
        result = s3.select_object_content(Bucket=bucket,Key=path,ExpressionType='SQL',Expression=select_stmnt,
              InputSerialization = {'CSV': {'FileHeaderInfo': 'Use','FieldDelimiter':fielddelimiter}},OutputSerialization = {output_format.upper(): {}})
        for event in result['Payload']:
            if 'Records' in event:
                result = event['Records']['Payload'].decode('utf-8')
                print("Query Completed.")
        return result

#09. Download by URL
def byurl(url,targetpath):
    import requests
    print('Query executing.')
    res=requests.get(url)
    f=open(targetpath,'wb')
    f.write(res.content)
    print('Query Completed and file is downloaded.')

def config_df_sample():
    import pandas
    return pandas.DataFrame([[1,'redshiftxxxx.xxx.com','xyxxxxxx',5439,'xzzxz','live@123','Redshift','','psycopg2'],
              [2,'xxx.database.windows.net','xxxxzz',1433,'xzzxz','live@123','MS-AZURE-SQL','','pyodbc'],
              [3,'19x.xxx.xx.xxx','yyxxzz',1433,'vvzxz','Zxc@123','MS-SQL-SERVER','','pyodbc'],
              [4,'12x.xxx.xx.xxx','employees',1433,'scott','Zxc@123','MySQL','','mysql-connector-python'],
              [5,'12x.xxx.xx.xxx','xxmzmx',5439,'user','user@123','PostgreSQL','','psycopg2'],
              [6,'oracle.xnxnxnx.com','cxmzmx','xxxx','user123','User@123','Oracle','','cx_Oracle'],
              [7,'xnxxxx.db2.com','nmxnxmx','xxxx','user123','User@123','IBM Db2','','ibm_db'],
              [8,'','','','','','Gsheet','D:/XXX/Work/analytics/etlxxx/client_secret.json','pygsheets'],
              [9,'','','','','','AWS S3',"{'accesskey':'XXXXX', 'secretkey':'YYYYYY'}",'boto3'],
              [10,'xxxxxx.xxxx.com','','','sftpuser','pswdsftp','SFTP','','pysftp'],
              ]
     ,columns=['conid','host','dbname','port','username','password','datasourcetype','conString','PythonLibrary'])
        
