
#QB Setup
DC4_Prod_link="http://dc4ui.p01.pro:7777/dc4custmanager/faces/browse/browsecustomers.jsp"
# DC4_preprod_link = "https://dc4ui.spspreprod.in/dc4custmanager/faces/browse/browsecustomers.jsp"
Browse_Customers="//a[@id='form1:commandLink1']"
Customers_by_TPID="//*[contains(text(),'Customers by TPID')]"
TPID_input_box="//input[@id='inputText66']"
Search_button="//a[@id='commandButton16']//img"
Company_name="//a[@id='table2:0:commandLink4']"
Profile_name="//span[@id='table2:0:outputText22']"
First_company_name="//a[@id='table2:0:commandLink4']"
Relationships="//a[contains(text(),'Relationships')]"
Relationships_Advanced="//table[@class='x5i']//a[@id='form1:showDetailItem2']"
Sender_as_Show_all="//select[@id='form1:table3-nb__xc_c']"
Receiver_as_Show_all="//select[@id='form1:table4-nb__xc_c']"
Show_all_profile="//h2[contains(text(),' is the sender')]//following::option[@value='all'][1]"
Show_all_profile2="//h2[contains(text(),' is the receiver')]//following::option[@value='all'][1]"
Relationship_Overview="//a[contains(text(),'Relationship Overview')]"
Search_TP_box="//input[@id='form1:inputText1']"
TP_Search_button="//a[@id='form1:commandButton1']//img"
Company_EDI_Summary="//div//tr[2]//td[5]"
Trading_Partner_EDI_Summary="//div//tr[2]//td[7]"
Show="//a[@id='form1:table1dd0']//img"
addExistingCapability="//a[@id='form1:table1:0:table2:addExistingCapability']//img"
choose_btn="//a[@id='form1:table1:commandButton1']//img"
cap_choose_btn="//a[@id='form1:table1:commandButton1_adfr_adfr']//img"
createCapability="//a[@id='form1:table1:0:table2:createCapability']//img"
service="//input[@id='form1:findService']"
Data_Type="//input[@id='form1:findDataType']"
Profiles_Tab="//a[contains(text(),'Profiles')]"
Toggle_profile_capability_status="//a[@id='form1:table1:0:table2:disableCapability']//img"
Add_Extention_btn="//a[@id='form1:table1:commandButton1']//img"
map_1080="//span[contains(text(),'MapExtension')]//preceding::input[1]"
map_1080_choose="//a[@id='form1:table1:commandButton2_adfr_adfr']//img"
Extention_Save_Changes="//a[@id='form1:commandButton2_adfr']//img"
submit_create_capability="//a[@id='form1:commandButton1']//img"

#RPA


TRANSACTION_TRACKER_PROD_LINK = 'https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'

BROWSER_DRIVER = "../BrowserDrivers/chromedriver.exe"
LOG_FILE_BASE_PATH = "../Logs"
REPORT_FILE_BASE_PATH = "../Reports"
RUNNER_ENVIRONMENT = "../X-Runner/RunnerEnv.xlsx"
LOGIN_ENVIRONMENT_LOCATOR_FILE_PATH = "../Resources/Login_Locators_Environment_File.xlsx"
SAILPOINT_URL='https://iam.spscommerce.com/login/login?spEntityID=https%3A%2F%2Fspscommerce.my.salesforce.com&goto=https%3A%2F%2Fiam-sso.spscommerce.com%2Fsso%2FSSORedirect%2FmetaAlias%2Fspscommerce%2Fidp%3FReqID%3D_2CAAAAXBiWUplME8wMGcwMDAwMDA0Qzk5AAAA3rjqUYFLOzRwS_UZlSFvGgKFRc7zigwDXnTkBRr4Y_SeOFUAKCn3R_yKHmKkUD9_ORPOeDsPnLQwmFIFhkqZx92B6avrXGI0ox0M-i4x9M6hqIof0cyhNZzwtJUgEYqgNv5n8Wsz2hOQPMavn1mJxQY4NTsmNJY19tKbZmejH47P2V1DqZDYi0qF7aujIaUgFegBAme390vakxe1xcjJZ8JCHrxoMu5jBxFyTaxQXkB-9QBGGlu1e3Hm9L7bC3AMGw%26index%3Dnull%26acsURL%3Dhttps%253A%252F%252Fspscommerce.my.salesforce.com%253Fso%253D00D300000000bzv%26spEntityID%3Dhttps%253A%252F%252Fspscommerce.my.salesforce.com%26binding%3Durn%253Aoasis%253Anames%253Atc%253ASAML%253A2.0%253Abindings%253AHTTP-POST'
INPUT_FILE_PATH = "../X-Runner/QB_Input.xlsx"


SALESFORCE_URL='https://spscommerce.my.salesforce.com/'
SAILPOINT_BTN=".//*[@id='idp_section_buttons']/button"
SAILPOINT_USERNAME_TEXTBOX=".//*[@id='username']"
SAILPOINT_PASSWORD_TEXTBOX=".//*[@id='password']"
SAILPOINT_CREDENTIAL_USENAME="sshetty"
SAILPOINT_CREDENTIAL_PASSWORD="R@dha$hyam108"
SAILPOINT_LOGIN_BTN=".//*[@id='signIn']/button"
QUEUE_URL="https://spscommerce.my.salesforce.com/500/o"
CROSS_SWITCH_BOX=".//*[@id='tryLexDialogX']"
QUEUE_LIST=".//*[@id='fcf']"
FS_TEAM_QUEUE=".//*[contains(text(),'FS: Team Queue (No TS)')]"
GO_BTN='.//*[@title="Go!"]'
ALL_CASES=".//*[@class='x-grid3-cell-inner x-grid3-col-CASES_CASE_NUMBER']"


#TT Locators

tt_username=".//*[@id='username']"
tt_password=".//*[@id='password']"
tt_login_btn=".//button"

tt_uname="bshetty@spscommerce.com"
tt_pw="DC4rulz"
#T ransaction Tracker UI xpath

COMPANY_SEARCH_INPUTBOX=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[1]/div/companies-chosen-select/div/ul/li/input"
TRADING_SEARCH_INPUTBOX= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[3]/div/trading-partner-chosen-select/div/ul/li/input"
START_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/label[2]/input"
END_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div/div[1]/label[2]/input"
DOCUMENT_TYPE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[3]/div/input"
SERVICE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[1]/div/sps-select/div/a/span[2]/span"
SEARCH_BTN=".//*[@id='advanced_search_dropdown']/div[2]/div/div/button[2]"
DC4ROUTER=".//*[contains(text(),'DC4Router')]"
PARCEL_ID_SEARCH_BOX=".//*[@id='advanced_search_by_input']"

xpath=".//*[@id='ui-select-choices-row-2-"
PARCEL_COUNT="html/body/app-reporting/div/div/div/div/div/section/sps-search-results-bar/div/div/div/div/span/span[3]"
VIEW="html/body/app-reporting/div/div/div/div/div/section/div[3]/div[1]/span/sps-select/div/a"
# SELECT_100=".//*[contains(text(),'100')]"
SELECT_100="html/body/app-reporting/div/div/div/div/div/section/div[3]/div[1]/span/sps-select/div/a"
CLICK_100=".//*[@id='ui-select-choices-row-11-3']"
NEXT_SEARCH_BTN="html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]"
CLEAR_SEARCH=".//*[@id='advanced_search_dropdown']/div[2]/div/div/button[1]"


CLIENT_SECRET_JSON_FILE_PATH = '../Applications/Workflows/ProductionDataMonitoring/AppResources/Production Data Monitoring-b797de93f73f.json'

DROP_DOWN_LIST=".//*[contains(@id,'ui-select-choices-row-')]"
CUSTOMER_FROM_TT_FOR_COMPANY_1=".//*[@id='ui-select-choices-row-1-"
CUSTOMER_FROM_TT_FOR_COMPANY_2="']/div/div"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1=".//*[@id='ui-select-choices-row-2-"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2="']/div/div"

#def get_CM_parcels(self,input_sheet,row)

PARCEL_ID_1=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["
PARCEL_ID_2="]/td[2]"
STATUS_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
STATUS_2="]/td[1]"
DOCUMENT_ID_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
DOCUMENT_ID_2="]/td[5]"

PARCEL_DATE_TIME_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
PARCEL_DATE_TIME_2="]/td[6]"



LAST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]"

#process test files
FIRST_FIVE_PARCELS_FILE_PATH="..\Applications\Workflows\ProcessTestFiles\AppResources\parcelIDsforSearch.txt"
FIRST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]/a"
PARCEL_FIRST_STAGE="//h4[contains(text(),'Transformations ')]/following::i[4]"
PARCEL_FIRST_STAGE_ID="//h4[contains(text(),'Transformations ')]/following::span[3]"
DOWNLOAD_LOGO_BUTTON=".//*[@id='parcels_drop']/following::i"