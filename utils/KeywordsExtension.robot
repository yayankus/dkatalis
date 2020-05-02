*** Keywords ***
Open Midtrans Website
  Open Browser    url=${URL}    browser=${BROWSER}
  Maximize Browser Window

Log And Capture Error
  Capture Page Screenshot
  Log Source

Generate User Data
  ${name}=          FakerLibrary.Name
  ${email}=         FakerLibrary.Email    mail.com
  ${phoneNumber}=   FakerLibrary.Random Number    digits=11   fix_len=${TRUE}
  ${city}=          FakerLibrary.City
  ${address}=       FakerLibrary.Address
  ${postalCode}=    FakerLibrary.Postcode

  &{USER}=    Create Dictionary    NAME=${name}
  ...   EMAIL=${email}    PHONE=+62${phoneNumber}
  ...   CITY=${city}      ADDRESS=${address}
  ...   POSTCODE=${postalCode}
  [Return]    ${USER}

Convert Price To Integer
  [Arguments]   ${price}
  ${price}=   Remove String    ${price}    - Rp
  ${price}=   Remove String    ${price}    ,
  Convert To Integer    ${price}
  [Return]    ${price}
