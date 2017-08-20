*** Settings ***
Resource          resource.robot

*** Test Cases ***
login_success
    [Template]    登录验证通用逻辑
    admin    123456    退出

*** Keywords ***
登录验证通用逻辑
    [Arguments]    ${username}    ${password}    ${verify_flag}
    log many    ${username}    ${password}    ${verify_flag}
    打开登录页面
    输入用户名    ${username}
    输入用户密码    ${password}
    点击登录密码
    页面应该包含    ${verify_flag}
    [Teardown]    close browser
