*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
At start there are no sources
    Go To  ${HOME_URL}
    Title Should Be  BibTex -lähdehallintatyökalu

Can change language
    Page Should Contain  fi
    Page Should Contain  Lisää lähde
    Page Should Contain  Kirjoittaja
    Page Should Contain  Lisää tunniste

    Click Link  /language

    Page Should Contain  en
    Page Should Contain  Add source
    Page Should Contain  Author
    Page Should Contain  Add tag

*** Keywords ***
Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}
