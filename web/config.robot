*** Settings ***
Library     SeleniumLibrary    run_on_failure=Log And Capture Error    screenshot_root_directory=screenshot
Library     FakerLibrary
Library     String

Resource    pages/_PAGES_IMPORT.robot

*** Variables ***
${BROWSER}      Chrome
${URL}          https://demo.midtrans.com/
${IFRAME}       snap-midtrans

&{VALID_CC}     NUMBER=4811111111111114
...             EXPIRY=0720
...             CVV=123

&{INVALID_CC}   NUMBER=4911111111111113
...             EXPIRY=0720
...             CVV=123

${OTP}          112233
