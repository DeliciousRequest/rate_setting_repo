import ibm_db
conn = ibm_db.connect('DATABASE=DSNDP30;HOSTNAME=DSNDP30;PORT=2646;PROTOCOL=TCPIP;UID=E0015EY;PWD=acTrpj84;', '', '')

def determineRowCount(tableName):
    sqlCount = 'SELECT COUNT(*) FROM E0015DB.' + tableName + ' WHERE COMPANY_CODE = \'MLF\''
    stmt = ibm_db.exec_immediate(conn, sqlCount)
    dictionary = ibm_db.fetch_tuple(stmt)
    rowCount = 0
    while dictionary != False:
        rowCount = int(dictionary[0])
        dictionary = ibm_db.fetch_tuple(stmt)
    return rowCount

def populateTableDump(tableName):
    sql = 'SELECT * FROM E0015DB.' + tableName + ' WHERE COMPANY_CODE = \'MLF\' FETCH FIRST ' + str(determineRowCount(tableName)) +' ROWS ONLY'
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_tuple(stmt)
    tableList = []
    while dictionary != False:
        currentRow = list(dictionary)
        for i in range(len(currentRow)):
            try:
                currentRow[i] = currentRow[i].strip()
            except:
                pass

            try:
                currentRow[i] = currentRow[i].replace('\x9f', '*')
            except:
                pass

            try:
                currentRow[i] = currentRow[i].strftime('%Y-%m-%d')
            except:
                pass

        tableList.append(currentRow)
        dictionary = ibm_db.fetch_tuple(stmt)
    return tableList

def populateTableHeaders(tableName):
    headerList = []
    headerSQL = 'SELECT * FROM SYSIBM.SYSCOLUMNS where tbname = \'' + tableName + '\' ORDER BY COLNO ASC'
    stmt = ibm_db.exec_immediate(conn, headerSQL)
    dictionary = ibm_db.fetch_assoc(stmt)
    while dictionary != False:
        headerList.append(str(dictionary['NAME']).rstrip())
        dictionary = ibm_db.fetch_assoc(stmt)
    return headerList