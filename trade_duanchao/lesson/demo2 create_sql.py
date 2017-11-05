#coding:gbk
for i in range (5):
    j = str(50000000+i)
    k = str(500000000000000+i)
    sql = u"insert into tbl_mcht_base (ID, MCHT_NO, MCHT_NM, MCHT_STATUS, MCHT_KIND, MCHT_TYPE, MCHT_RISK_LEVEL, MCHT_UP_NO, MCHT_NM_SINGLE, MCHT_ENG_NM, MCHT_AREA_NO, MCHT_ADDR, MCHT_SCOPE, MCHT_GRP, MCHT_MCC, MCHT_BRH, MCHT_EXPAND, MCHT_REFERRER, MCHT_STLM_BRH, MCHT_REG_DATE, MCHT_DISC_ID0, MCHT_DISC_ID, MCHT_DISC_CYCLE, MCHT_DISC_THIS, MCHT_DISC_SMS, MCHT_POS_NUM, MCHT_USER_NUM, MCHT_ACCT_NUM, MCHT_MEDIA_NUM, MCHT_OPR_FLAG, MCHT_RESV1, MCHT_RESV2, MCHT_RESV3, MCHT_RESV4, SOURCE, ORG_CODE, MCHT_RANK, FEE_TYPE)values (\
    '%s', '%s',  清算压力测试商户%s',  0',  B2',  0',  3', '', '', '',  2301',  哈尔滨道里区和平路37号', '',  05',  5451',  008006', 1920, null, '',  20131231', '',  MHN20003', 1,'', '', null,null, null, null, '', null, null,  30823010054512776', '',  3', '',  P005', '')"%(j,k,k)
    # txt = "%s,%s,清算压力测试商户%s,0,B2,0,3,,,,2301,哈尔滨道里区和平路37号,,05,5451,008006,1920,,,20131231,,MHN20003,1,,,,,,,,,,30823010054512776,,3,,P005, "%(j,k,k)
    print (sql)