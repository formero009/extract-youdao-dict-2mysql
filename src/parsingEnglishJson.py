# coding = utf8

from MysqlConnector import MySQLConnector
from Conf import wordFilePath
import json
import os
from pymysql.converters import escape_string


def loopLines(filepath, listOfLines):
    line_count = 1
    sql_line = ''
    for line in listOfLines:
        sql_line = sql_line + '( '

        word = ''
        sentenceStr = ''
        trans_cn_tmp = ''
        trans_en_tmp = ''
        usphone = ''
        usspeech = ''
        ukphone = ''
        ukspeech = ''
        phraseStr = ''
        bookId = ''

        kdict = json.loads(line)
        word = kdict['headWord']
        sql_line = sql_line + '"'+word+'"' + ', '

        content = kdict['content']['word']['content']
        
        #例句列表
        if 'sentence' in content.keys():
            sentences = content['sentence']
            if sentences is not None:
                sentenceStr = json.dumps(sentences, ensure_ascii=False)
        sql_line = sql_line + '"'+escape_string(sentenceStr)+'"' + ', '
        
        
        # 翻译列表
        trans = content['trans']
        for tran in trans:
            pos = ''
            if 'pos' in tran.keys():
                pos = tran['pos']
            if 'tranCn' in tran.keys():
                tcn = pos + '|' + tran['tranCn'] + ' ; '
                trans_cn_tmp = trans_cn_tmp + tcn
                trans_cn_tmp.replace(',', '，')
            if 'tranOther' in tran.keys():
                ten = pos + '|' + tran['tranOther'] + ' ; '
                trans_en_tmp = trans_en_tmp + ten
                trans_en_tmp.replace(',', '，')

        sql_line = sql_line + '"'+escape_string(trans_cn_tmp[0:-2])+'"' + ', '
        sql_line = sql_line + '"'+escape_string(trans_en_tmp[0:-2])+'"' + ', '

        if 'usphone' in content.keys():
            usphone = content['usphone']
        sql_line = sql_line + '"'+escape_string(usphone)+'"' + ', '
        if 'usspeech' in content.keys():
            usspeech = content['usspeech']
        sql_line = sql_line + '"'+escape_string(usspeech)+'"' + ', '
        if 'ukphone' in content.keys():
            ukphone = content['ukphone']
        sql_line = sql_line + '"'+escape_string(ukphone)+'"' + ', '
        if 'ukspeech' in content.keys():
            ukspeech = content['ukspeech']
        sql_line = sql_line + '"'+escape_string(ukspeech)+'"' + ', '

        if 'phrase' in content.keys():
            phrases = content['phrase']['phrases']
            phraseStr = json.dumps(phrases, ensure_ascii=False)
        sql_line = sql_line + '"'+escape_string(phraseStr)+'"' + ', '
        if 'bookId' in kdict.keys():
            bookId = kdict['bookId']
        sql_line = sql_line + '"'+bookId+'"' + ', '
        bookName = filepath
        sql_line = sql_line + '"'+escape_string(bookName)+'"' + ' )'

        # 根据解析出来的json数据生成对应sql语句
        sql_line = sql_line + ','

        if line_count == 10:
            line_count = 1

            sql = "insert into daily_words(word,sentences,trans_cn,trans_en,usphone,usspeech,ukphone,ukspeech,phrase,book_id,book_name) values " + \
                sql_line[0:-1]
            # print(sql)
            conn = MySQLConnector()
            result = conn.insert_data(sql)
            print('file: ', filepath, ' status: ', str(result))
            if 'Error' in str(result):
                loghandler = open("D:/englishwords/log",
                                  "w", encoding='utf-8')
                loghandler.write(sql)
                loghandler.close()
            sql = ''
            sql_line = ''
        line_count += 1


if __name__ == '__main__':

    # 解析json文件
    for root, dirs, files in os.walk(wordFilePath):
        for f in files:
            if f.endswith("json"):
                fileHandler = open(os.path.join(root, f), 
                                   "r", encoding='utf-8')
                listOfLines = fileHandler.readlines()
                fileHandler.close()
                loopLines(os.path.join(root, f), listOfLines)
