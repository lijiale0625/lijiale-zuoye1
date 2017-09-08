*** Settings ***
Library           SudsLibrary
Library           Collections

*** Variables ***
${url}            http://172.30.0.169:8099/mchtService?wsdl

*** Keywords ***
wsdl请求
    [Arguments]    ${Methods}    ${values}    ${exception}
    Comment
    ${result}=    Call Soap Method    ${Methods}    ${values}
    Should Be Equal    ${result}    ${exception}

创建client类
    Create Soap Client    ${url}
    Set Port    MchtServiceWSPort
