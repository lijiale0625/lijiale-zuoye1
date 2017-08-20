*** Settings ***
Library           Selenium2Library

*** Variables ***
${base_url}       http://localhost/bugfree/index.php/site/login

*** Keywords ***
打开登录页面
    [Arguments]    ${base_url}
    Open Browser    ${base_url}
    Title Should Be    登录 - BugFree

输入用户名
    [Arguments]    ${username}
    Input Text    id=LoginForm_username    ${username}

输入用户密码
    [Arguments]    ${password}
    Input Text    id=LoginForm_password    ${password}

点击登录密码
    click button    id=SubmitLoginBTN

页面应该包含
    [Arguments]    ${arg1}
    Page Should Contain    ${arg1}
