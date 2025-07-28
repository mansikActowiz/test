
import requests
import json
import gzip
from parsel import Selector
import re
import requests

cookies = {
    'WC_SESSION_ESTABLISHED': 'true',
    'WC_PERSISTENT': 'lWlNkiiKQF4dFDzOPJgCoPjm2qj2e6ofemHoQBwhD4I%3D%3B2025-07-02+05%3A08%3A02.997_1751458082942-35239_10301_-1002%2C-1%2CUSD%2CWZr1shFRa33WQ0wQ5MVT4%2B2%2BwSXDNwxpBl3JhQK8ISOCj9e77Wtk9f7LZqipZKmaXTf%2BIoMbIIOKefv0aP7mYQ%3D%3D_10301',
    'WC_AUTHENTICATION_-1002': '-1002%2CtMlGzWl0cXkJgxNmSw2bN88J4PwPTaLQto2HrkgAI8Q%3D',
    'WC_ACTIVEPOINTER': '-1%2C10301',
    'WC_USERACTIVITY_-1002': '-1002%2C10301%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1377652778%2CyoOPlDrITgClRQpov6POaJoKuBkYRJ2EpGrimEBHEkOHN3Ds77TQaK5qyeMuuDTf1oH3hjVjJSduaERMUfb9yct8Imhh5hUEv7Nmpx515%2BvKqk264QDTq914XdQO0wJSLDMankVHGeqDd1CwHkbYFDJpGZc9xKyA7Qj89RlAAmeET580esAwRbr5sBwJRnsJakbR89uHoRJ%2BEnS7G%2B%2FKyavOnnN93iTkzicHAx5az25qdZAaH%2FNcwp5ZveMOIQYe',
    'WC_GENERIC_ACTIVITYDATA': '[46096470446%3Atrue%3Afalse%3A0%3AstIX2Ynut9fCqcSf9NcvQ1hFfKI7A5XOdDMJLa9zIpk%3D][com.ibm.commerce.context.entitlement.EntitlementContext|120577%253B120572%253B120591%253B120563%253B120565%253B120570%253B120571%253B120568%253B120569%253B120757%253B120754%253B120752%253B120758%253B120753%253B120756%253B120755%253B120751%253B121092%253B120765%253B120926%253B121112%253B120762%253B120763%253B120761%253B120933%253B120920%253B120573%253B120574%253B4000000000000101005%253B60501%253B4000000000000001002%26null%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1751458082942-35239][com.ibm.commerce.context.globalization.GlobalizationContext|-1%26USD%26-1%26USD][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.costco.commerce.member.context.ProfileApiTokenCustomContext|null][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null][com.costco.pharmacy.commerce.common.context.PharmacyCustomContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10701%26null%26false%26false%26false][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10301%26-1002%26-1002%26-1]',
    'BCO': 'pm3',
    'akaas_AS01': '2147483647~rv=72~id=002046ff7f9974e6750e469f1a8b4e89',
    'selectedLanguage': '-1',
    'kndctr_97B21CFE5329614E0A490D45_AdobeOrg_identity': 'CiYzOTUwMTUzMTMyMTAwMDQ0MjM0MzA2NTk0NjkyNTc5MTM2NzE4NVIRCJ71pdj8MhgBKgRJTkQxMAHwAZ71pdj8Mg==',
    'AMCV_97B21CFE5329614E0A490D45%40AdobeOrg': 'MCMID|39501531321000442343065946925791367185',
    'invCheckPostalCode': '98101',
    'invCheckStateCode': 'WA',
    'invCheckCity': 'Times%20Square',
    'CriteoSessionUserId': '9ccc6296-b6f4-454c-b068-7305682e0ce7',
    'WAREHOUSEDELIVERY_WHS': '%7B%22distributionCenters%22%3A%5B%221250-3pl%22%2C%221321-wm%22%2C%221456-3pl%22%2C%22283-wm%22%2C%22561-wm%22%2C%22725-wm%22%2C%22731-wm%22%2C%22758-wm%22%2C%22759-wm%22%2C%22847_0-cor%22%2C%22847_0-cwt%22%2C%22847_0-edi%22%2C%22847_0-ehs%22%2C%22847_0-membership%22%2C%22847_0-mpt%22%2C%22847_0-spc%22%2C%22847_0-wm%22%2C%22847_1-cwt%22%2C%22847_1-edi%22%2C%22847_d-fis%22%2C%22847_lg_n1f-edi%22%2C%22847_lux_us01-edi%22%2C%22847_NA-cor%22%2C%22847_NA-pharmacy%22%2C%22847_NA-wm%22%2C%22847_ss_u362-edi%22%2C%22847_wp_r458-edi%22%2C%22951-wm%22%2C%22952-wm%22%2C%229847-wcs%22%5D%2C%22groceryCenters%22%3A%5B%22115-bd%22%5D%2C%22nearestWarehouse%22%3A%7B%22catalog%22%3A%221-wh%22%7D%2C%22pickUpCenters%22%3A%5B%5D%7D',
    'STORELOCATION': '%7B%22storeLocation%22%3A%7B%22zip%22%3A%2298134%22%2C%22city%22%3A%22Seattle%22%7D%7D',
    'C_WHLOC': 'USWA',
    'AKA_A2': 'A',
    'bm_ss': 'ab8e18ef4e',
    'JSESSIONID': '0000JJdGrUBW9Np0yJnhyhWbs41:1g210fcp8',
    'kndctr_97B21CFE5329614E0A490D45_AdobeOrg_cluster': 'ind1',
    'mboxEdgeCluster': '41',
    'BVBRANDSID': '4338d0f7-af8d-494e-9a0c-2fb9751e9da6',
    'BVBRANDID': '083579d4-42bc-4534-b190-a416adc9956f',
    'bm_mi': '434D79E0D8815887CCC1AFF73C8ED61B~YAAQ7/Q3FwEnOLCXAQAANC/RzxzhHVaYf5GDBKmh/KBlI0HAF0w9GQ1ABSluKiMorhXqS8/K+TqAj7JG76nELEygHXVjRoO/tKejbE3cyh4HPB/MB4rl31OADTj9jffneuRRqqU+IRVVk8Ppg0A81eCZKJhSFwb8puCvJT/yw1ga42ZCjK507JfpGd21o7561gWkfHSddJ+2s0yatOH28uwpFlBJsEfqqK+HZ8gW6tPnNs5eCB54YDoMqk3Oh3B38PW1C2GpqDHlbtUVwAoxRqs/lGypdfetlv1QW2P/yH8kFmqpdLjedn9rRb/tdMsMbwzz4TVF+YwEtGmMpCHKtokM~1',
    'ak_bmsc': '2CB7C12026697346F42DBC4DD83B2CB6~000000000000000000000000000000~YAAQ7/Q3FygsOLCXAQAAs/DRzxzBVCG8dhpVmYzpPsH1NDG6B5/FIOGtIn2ksfw57PB1BmHPWn7KugupUcdoDxesVhi/HFJO9N00MSroxb3HU/3+3/4Z78VmvZAwsBNVhabK3qOwuGat37yuJcZi2DrUOtCyPdYaJMUxPthvesDyrFRjPd98GrtZtZ/JivEo1412QSMHkJiCgiZwNYXybYb17KCQja/0mGcdZyudkzKPslqGWLP+4bU1FWP8/mE86BP27wfP+BHm6QAe51GQQn3OYSg4i4yjbDx6DOt6vbHVqdFjh7i49bka982oZS/Ne+LBlilmRUNdiRL77NKF4OqzbhDBmFfMkE65v+0YiJgi8Qb2p45sIOm2vQPlCN8qeiWk+zEHYtetud7KrnMbp0/W/D2hyJTe6Y3nY44uamfvZE59NEPX9Ob2DnJk7wnaUym34wgz3c/f01VjsAOgkVprTWXIybLtNNwhi/FX+WAmuGnPwqCtwSHptKxjNh4lKnYzZ8pRnsDx5wsC',
    'bm_so': '9BD53DAE6CA51BCEC4838BC39A5D1A8D461932BB52586E3C5CEDB09DE2FC59DE~YAAQ7/Q3FyosOLCXAQAAs/DRzwQPVpxfuY9IbEhqrkejWqe+sNnjBKtRGRNyaPxP1Q6No4auPSg/XsJI+ZK9gkFuUqA4JiSyNiR2irfImwqrfQeAVIe909iOx1fL7KofZEBEcQwHFMzMRW/Pu4ZbGPqMncgRXAZj7VBdEPGgGyyOpRdu2qJYOFRiw6UiUg+ENLcPGtsjoIzlz+YjeqpIvSTteAWyEri/XJZl8H/vWHD2ADTq+R+EuObuNO6X/+WVbnqLf650N1Yl+3T0b/W/Jdz63qGvlBkOM0T6xCQ3WOqqK5QBJ4lOKuFw7YlQiiQJ6AbWBxt735tz1JT2/IJACY0PaRGbHM9Gccxxgq78RMSgwTkJ3aLnmR3FGyxthnv6Y0OV57WgYObMuH9WcX+LydoK+LG+w04PoCTHO9JwJxYjNtqYEk4rXnn+Pd9MHxXMrj7GHqnBIeXEuYZzNZM=',
    'bm_sz': '989F92207D7410CBB7A6D1AEA913BE84~YAAQ7/Q3FywsOLCXAQAAs/DRzxwJp9bi7zoy1gZx3I40eu8OjcRAQyQG+pEC/sRWWfZpPYkdY5QaHHb8Vy+qJddOD0/ZFeN0GuRjaHfsucyTRZurN6FOL3vTSBUREAvTJB/n2OY8tpvswfeAA5fNjRmEpG4DorQ5+cctbxmjlhxQuzsHyQhQpHTuMgJ/hyJbh/HrKsaDToAf8BPGzDDi+afxZRoYGD9cFZfVj8MmZc0VxXb0Jfx3oQoxhfS7Z5Ud7g2ssQKGu9GH0sdPYAuTgyI183NZNirMeSNNcYvu+1WfL5AOOvXAtzhfa8MRZ7fOBhxI3sA75tmWeVbAesOwRWxMozqvz/HOryTvC+g/n3yXf89jpcOsv/uXhnmgivGS4ttvGwBZwsuYvDKMzOJlh8WqEKWt0kQaHielOQM=~3160373~4342070',
    '_abck': '4661DE08543510A5A899A98FD5F4CE84~0~YAAQ7/Q3FzEsOLCXAQAAJfLRzw7qFahu3Xkglhsg2xdneRWNiH9CXOlzNx8S3oAtcTdFlKhC0ZSBhwPtPdlzBxvCdnkgnzZwDPIcgWG0L8KT1x6f+0cJxJRxSzNTOsYHv1xfWWbc/ViSdqSdHFX3AvX6Oj/vezhZAvzvCbOm0IpvjJMav5cWx6Roj2HYjVuUyIQDXgtl4/mx8cFPx/aHE/6SCPIg1TlhQ4q6iaWem1CaPTUMHVcyq6ljmqfZtSoaFv3QG36p68nR/bi85n+IJgibKXjynfcxctgM3N8QsJ6YuYdx4IedOlTbJPpjZyMxmTrm4Tv6ynaZj8G+0o8B46BW8zVgG+O3jiK+q5+M1SXfCOaFX1wJo3+3P5MdBnb7Gsem97MVDM1GzR6AGDaRPuhjS+NHyhFdazktNq7Vb3vGwG0z70W7XoiBQsIGZMzCbR1kXccNXw6Pi/8PRe8SuVmAnauujweKQ2L0AdmFgqnIRJ8/f+tzdttdRAi7SvoZUkwDQCHyPbAgIKZRKofeZzB8Pvt08uEm/gD2fVgvUdaKJ11iX9UUDYkufR+U050bAALdFOd8Yau33cCrdx46ctq/d96careGIqm6RzO91YuORHhj+SedkcsOXOW3qfqp~-1~-1~1751541784',
    'mbox': 'session%2339501531321000442343065946925791367185%2DiIrlvq%231751540193',
    'bm_s': 'YAAQ7/Q3F1ssOLCXAQAAhfjRzwMO5xPRC61fhWuLt/pvDd3DIx5Gu3+Zf/SUzYzhCr8soDRh/IRjiK8fj0ayysMjdnrO/vrcvN7X40GK52ghDTpNS0ihKwNkKH6/x+2SjSwwlVmR2PdIHyDTsDSMNe++77uVh3byx8GcQMxADtujC5i5Xgs5O8j/ky6Ydt9R5w5qdSEp1p4iiUISgVs3G0bcDvmsHtFU7BB9qmXT7DTxI0RP7GXtd4Rdm5N1yDUXcWrkaqdYfOSqDHcijoWEx9WPnHK9/wv4Z2h7k5vDegaks4Se3lde+O44lfMjv4jo8Klsep1RElMSugHZHKa7ojKjej1LbYogUcfSo0nFS2jdNZwjsmrJPpzW1ilVyUGtUKoBCVwj+SCDFgEHPT2IuxhyHSGL1eVzVoqdc7xee3oUh1KNRFxZRYSuz1+LDhcxTP64afkelyYrdRdHmq7SUI0jLEPu5j7M91cC4Cxne5P38ZP/2j+teGgk9D4GEzppPntZQR8tLkFpxJO2SIPG681J/lJiJhOYSuq6HfRxHNEoaTZaD06b6oJ+yimQiIzZL1l4hKE=',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Jul+03+2025+15%3A54%3A59+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1147e6f6-a20a-477a-8e82-6e78d22b99c2&interactionCount=1&landingPath=NotLandingPage&groups=BG117%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_BG%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'cto_bundle': 'hXabOF9hdlpuSHdXS0lodiUyQldHWWRLbFVpYUtnaXhHU2wxbkRrSEdQZ1JmbWRzUzdKVXNZdjJHJTJCd2dlNzU0SmQxbFE1RSUyRjBBJTJCMXd2YVViZmdvazdSZmJOaWlNWHNTWk1EQkNYVFVpeEM0ViUyRkklMkZqVDVMUWVlTEowZnRvZ1ZRTU9RUUtwdGppYkw4ZzRMZ01YQzdBcFZ0JTJGSyUyQnl5aU4lMkJmNExWWUhCYnl3T0xyYXdWQ2g5JTJCUGZ6YW1yVFc1b2w1JTJCY210ZnRISUVGVDlUZUh2UTcyQnZ2QWF2QWxwQjJBJTJGc003Y0dlT2V4MWk4ZHZlQlM1RTZ6Zm50QXNGS090YVpZeFNTbTNKVkhuMjZSZ3JYNG5jckh3Z0Q3dGY5OVpKVmslMkIlMkJHaVpjWm1Pb1Y4TEMlMkJXMUh3WER5Z1pObVBjelFUbGNnWTRtUg',
    '_lr_hb_-costco%2Fproduction-vrwno': '{%22heartbeat%22:1751538301328}',
    'RT': '"z=1&dm=www.costco.com&si=699c4b3a-6f41-456c-a09f-15923d9f4168&ss=mcn8odqm&sl=1&tt=56w&bcn=%2F%2F684d0d48.akstat.io%2F&ld=572"',
    'bm_lso': '9BD53DAE6CA51BCEC4838BC39A5D1A8D461932BB52586E3C5CEDB09DE2FC59DE~YAAQ7/Q3FyosOLCXAQAAs/DRzwQPVpxfuY9IbEhqrkejWqe+sNnjBKtRGRNyaPxP1Q6No4auPSg/XsJI+ZK9gkFuUqA4JiSyNiR2irfImwqrfQeAVIe909iOx1fL7KofZEBEcQwHFMzMRW/Pu4ZbGPqMncgRXAZj7VBdEPGgGyyOpRdu2qJYOFRiw6UiUg+ENLcPGtsjoIzlz+YjeqpIvSTteAWyEri/XJZl8H/vWHD2ADTq+R+EuObuNO6X/+WVbnqLf650N1Yl+3T0b/W/Jdz63qGvlBkOM0T6xCQ3WOqqK5QBJ4lOKuFw7YlQiiQJ6AbWBxt735tz1JT2/IJACY0PaRGbHM9Gccxxgq78RMSgwTkJ3aLnmR3FGyxthnv6Y0OV57WgYObMuH9WcX+LydoK+LG+w04PoCTHO9JwJxYjNtqYEk4rXnn+Pd9MHxXMrj7GHqnBIeXEuYZzNZM=^1751538302134',
    'akavpau_zezxapz5yf': '1751538660~id=e0d632fd0b572f72dcd90b7f4943d0fd',
    'bm_sv': '8EF76AED4FF29936B7F024DA58143575~YAAQ7/Q3F1kuOLCXAQAARF/SzxwmBIUaidr6GFZsbVRuiL/MhN/VH0Pc/RGgJ2dTb9sBt6eF/MCJgL7sxkySW2vR66g/I7oiux57r32P4L7C3VLs/0DNTVBZJ7axYugpllzE/vSFz9kgFCRTXfgV0OJTzdAmmlE60pMmzy7I+BTmHlkmIfWrS3nqQkhzq7fnGSLVNC2kaiywS6VKT7ewkhwdD3NPWUh5LPoercQfgITenq8415cg0SXQF3YxZRUqTg==~1',
    '_lr_tabs_-costco%2Fproduction-vrwno': '{%22recordingID%22:%226-0197cfcf-31a8-76b4-b010-e5b1246ee09e%22%2C%22sessionID%22:0%2C%22lastActivity%22:1751538339676%2C%22hasActivity%22:true%2C%22confirmed%22:false%2C%22recordingConditionThreshold%22:%228.55370693574593%22}',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'WC_SESSION_ESTABLISHED=true; WC_PERSISTENT=lWlNkiiKQF4dFDzOPJgCoPjm2qj2e6ofemHoQBwhD4I%3D%3B2025-07-02+05%3A08%3A02.997_1751458082942-35239_10301_-1002%2C-1%2CUSD%2CWZr1shFRa33WQ0wQ5MVT4%2B2%2BwSXDNwxpBl3JhQK8ISOCj9e77Wtk9f7LZqipZKmaXTf%2BIoMbIIOKefv0aP7mYQ%3D%3D_10301; WC_AUTHENTICATION_-1002=-1002%2CtMlGzWl0cXkJgxNmSw2bN88J4PwPTaLQto2HrkgAI8Q%3D; WC_ACTIVEPOINTER=-1%2C10301; WC_USERACTIVITY_-1002=-1002%2C10301%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1377652778%2CyoOPlDrITgClRQpov6POaJoKuBkYRJ2EpGrimEBHEkOHN3Ds77TQaK5qyeMuuDTf1oH3hjVjJSduaERMUfb9yct8Imhh5hUEv7Nmpx515%2BvKqk264QDTq914XdQO0wJSLDMankVHGeqDd1CwHkbYFDJpGZc9xKyA7Qj89RlAAmeET580esAwRbr5sBwJRnsJakbR89uHoRJ%2BEnS7G%2B%2FKyavOnnN93iTkzicHAx5az25qdZAaH%2FNcwp5ZveMOIQYe; WC_GENERIC_ACTIVITYDATA=[46096470446%3Atrue%3Afalse%3A0%3AstIX2Ynut9fCqcSf9NcvQ1hFfKI7A5XOdDMJLa9zIpk%3D][com.ibm.commerce.context.entitlement.EntitlementContext|120577%253B120572%253B120591%253B120563%253B120565%253B120570%253B120571%253B120568%253B120569%253B120757%253B120754%253B120752%253B120758%253B120753%253B120756%253B120755%253B120751%253B121092%253B120765%253B120926%253B121112%253B120762%253B120763%253B120761%253B120933%253B120920%253B120573%253B120574%253B4000000000000101005%253B60501%253B4000000000000001002%26null%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1751458082942-35239][com.ibm.commerce.context.globalization.GlobalizationContext|-1%26USD%26-1%26USD][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.costco.commerce.member.context.ProfileApiTokenCustomContext|null][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null][com.costco.pharmacy.commerce.common.context.PharmacyCustomContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10701%26null%26false%26false%26false][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10301%26-1002%26-1002%26-1]; BCO=pm3; akaas_AS01=2147483647~rv=72~id=002046ff7f9974e6750e469f1a8b4e89; selectedLanguage=-1; kndctr_97B21CFE5329614E0A490D45_AdobeOrg_identity=CiYzOTUwMTUzMTMyMTAwMDQ0MjM0MzA2NTk0NjkyNTc5MTM2NzE4NVIRCJ71pdj8MhgBKgRJTkQxMAHwAZ71pdj8Mg==; AMCV_97B21CFE5329614E0A490D45%40AdobeOrg=MCMID|39501531321000442343065946925791367185; invCheckPostalCode=98101; invCheckStateCode=WA; invCheckCity=Times%20Square; CriteoSessionUserId=9ccc6296-b6f4-454c-b068-7305682e0ce7; WAREHOUSEDELIVERY_WHS=%7B%22distributionCenters%22%3A%5B%221250-3pl%22%2C%221321-wm%22%2C%221456-3pl%22%2C%22283-wm%22%2C%22561-wm%22%2C%22725-wm%22%2C%22731-wm%22%2C%22758-wm%22%2C%22759-wm%22%2C%22847_0-cor%22%2C%22847_0-cwt%22%2C%22847_0-edi%22%2C%22847_0-ehs%22%2C%22847_0-membership%22%2C%22847_0-mpt%22%2C%22847_0-spc%22%2C%22847_0-wm%22%2C%22847_1-cwt%22%2C%22847_1-edi%22%2C%22847_d-fis%22%2C%22847_lg_n1f-edi%22%2C%22847_lux_us01-edi%22%2C%22847_NA-cor%22%2C%22847_NA-pharmacy%22%2C%22847_NA-wm%22%2C%22847_ss_u362-edi%22%2C%22847_wp_r458-edi%22%2C%22951-wm%22%2C%22952-wm%22%2C%229847-wcs%22%5D%2C%22groceryCenters%22%3A%5B%22115-bd%22%5D%2C%22nearestWarehouse%22%3A%7B%22catalog%22%3A%221-wh%22%7D%2C%22pickUpCenters%22%3A%5B%5D%7D; STORELOCATION=%7B%22storeLocation%22%3A%7B%22zip%22%3A%2298134%22%2C%22city%22%3A%22Seattle%22%7D%7D; C_WHLOC=USWA; AKA_A2=A; bm_ss=ab8e18ef4e; JSESSIONID=0000JJdGrUBW9Np0yJnhyhWbs41:1g210fcp8; kndctr_97B21CFE5329614E0A490D45_AdobeOrg_cluster=ind1; mboxEdgeCluster=41; BVBRANDSID=4338d0f7-af8d-494e-9a0c-2fb9751e9da6; BVBRANDID=083579d4-42bc-4534-b190-a416adc9956f; bm_mi=434D79E0D8815887CCC1AFF73C8ED61B~YAAQ7/Q3FwEnOLCXAQAANC/RzxzhHVaYf5GDBKmh/KBlI0HAF0w9GQ1ABSluKiMorhXqS8/K+TqAj7JG76nELEygHXVjRoO/tKejbE3cyh4HPB/MB4rl31OADTj9jffneuRRqqU+IRVVk8Ppg0A81eCZKJhSFwb8puCvJT/yw1ga42ZCjK507JfpGd21o7561gWkfHSddJ+2s0yatOH28uwpFlBJsEfqqK+HZ8gW6tPnNs5eCB54YDoMqk3Oh3B38PW1C2GpqDHlbtUVwAoxRqs/lGypdfetlv1QW2P/yH8kFmqpdLjedn9rRb/tdMsMbwzz4TVF+YwEtGmMpCHKtokM~1; ak_bmsc=2CB7C12026697346F42DBC4DD83B2CB6~000000000000000000000000000000~YAAQ7/Q3FygsOLCXAQAAs/DRzxzBVCG8dhpVmYzpPsH1NDG6B5/FIOGtIn2ksfw57PB1BmHPWn7KugupUcdoDxesVhi/HFJO9N00MSroxb3HU/3+3/4Z78VmvZAwsBNVhabK3qOwuGat37yuJcZi2DrUOtCyPdYaJMUxPthvesDyrFRjPd98GrtZtZ/JivEo1412QSMHkJiCgiZwNYXybYb17KCQja/0mGcdZyudkzKPslqGWLP+4bU1FWP8/mE86BP27wfP+BHm6QAe51GQQn3OYSg4i4yjbDx6DOt6vbHVqdFjh7i49bka982oZS/Ne+LBlilmRUNdiRL77NKF4OqzbhDBmFfMkE65v+0YiJgi8Qb2p45sIOm2vQPlCN8qeiWk+zEHYtetud7KrnMbp0/W/D2hyJTe6Y3nY44uamfvZE59NEPX9Ob2DnJk7wnaUym34wgz3c/f01VjsAOgkVprTWXIybLtNNwhi/FX+WAmuGnPwqCtwSHptKxjNh4lKnYzZ8pRnsDx5wsC; bm_so=9BD53DAE6CA51BCEC4838BC39A5D1A8D461932BB52586E3C5CEDB09DE2FC59DE~YAAQ7/Q3FyosOLCXAQAAs/DRzwQPVpxfuY9IbEhqrkejWqe+sNnjBKtRGRNyaPxP1Q6No4auPSg/XsJI+ZK9gkFuUqA4JiSyNiR2irfImwqrfQeAVIe909iOx1fL7KofZEBEcQwHFMzMRW/Pu4ZbGPqMncgRXAZj7VBdEPGgGyyOpRdu2qJYOFRiw6UiUg+ENLcPGtsjoIzlz+YjeqpIvSTteAWyEri/XJZl8H/vWHD2ADTq+R+EuObuNO6X/+WVbnqLf650N1Yl+3T0b/W/Jdz63qGvlBkOM0T6xCQ3WOqqK5QBJ4lOKuFw7YlQiiQJ6AbWBxt735tz1JT2/IJACY0PaRGbHM9Gccxxgq78RMSgwTkJ3aLnmR3FGyxthnv6Y0OV57WgYObMuH9WcX+LydoK+LG+w04PoCTHO9JwJxYjNtqYEk4rXnn+Pd9MHxXMrj7GHqnBIeXEuYZzNZM=; bm_sz=989F92207D7410CBB7A6D1AEA913BE84~YAAQ7/Q3FywsOLCXAQAAs/DRzxwJp9bi7zoy1gZx3I40eu8OjcRAQyQG+pEC/sRWWfZpPYkdY5QaHHb8Vy+qJddOD0/ZFeN0GuRjaHfsucyTRZurN6FOL3vTSBUREAvTJB/n2OY8tpvswfeAA5fNjRmEpG4DorQ5+cctbxmjlhxQuzsHyQhQpHTuMgJ/hyJbh/HrKsaDToAf8BPGzDDi+afxZRoYGD9cFZfVj8MmZc0VxXb0Jfx3oQoxhfS7Z5Ud7g2ssQKGu9GH0sdPYAuTgyI183NZNirMeSNNcYvu+1WfL5AOOvXAtzhfa8MRZ7fOBhxI3sA75tmWeVbAesOwRWxMozqvz/HOryTvC+g/n3yXf89jpcOsv/uXhnmgivGS4ttvGwBZwsuYvDKMzOJlh8WqEKWt0kQaHielOQM=~3160373~4342070; _abck=4661DE08543510A5A899A98FD5F4CE84~0~YAAQ7/Q3FzEsOLCXAQAAJfLRzw7qFahu3Xkglhsg2xdneRWNiH9CXOlzNx8S3oAtcTdFlKhC0ZSBhwPtPdlzBxvCdnkgnzZwDPIcgWG0L8KT1x6f+0cJxJRxSzNTOsYHv1xfWWbc/ViSdqSdHFX3AvX6Oj/vezhZAvzvCbOm0IpvjJMav5cWx6Roj2HYjVuUyIQDXgtl4/mx8cFPx/aHE/6SCPIg1TlhQ4q6iaWem1CaPTUMHVcyq6ljmqfZtSoaFv3QG36p68nR/bi85n+IJgibKXjynfcxctgM3N8QsJ6YuYdx4IedOlTbJPpjZyMxmTrm4Tv6ynaZj8G+0o8B46BW8zVgG+O3jiK+q5+M1SXfCOaFX1wJo3+3P5MdBnb7Gsem97MVDM1GzR6AGDaRPuhjS+NHyhFdazktNq7Vb3vGwG0z70W7XoiBQsIGZMzCbR1kXccNXw6Pi/8PRe8SuVmAnauujweKQ2L0AdmFgqnIRJ8/f+tzdttdRAi7SvoZUkwDQCHyPbAgIKZRKofeZzB8Pvt08uEm/gD2fVgvUdaKJ11iX9UUDYkufR+U050bAALdFOd8Yau33cCrdx46ctq/d96careGIqm6RzO91YuORHhj+SedkcsOXOW3qfqp~-1~-1~1751541784; mbox=session%2339501531321000442343065946925791367185%2DiIrlvq%231751540193; bm_s=YAAQ7/Q3F1ssOLCXAQAAhfjRzwMO5xPRC61fhWuLt/pvDd3DIx5Gu3+Zf/SUzYzhCr8soDRh/IRjiK8fj0ayysMjdnrO/vrcvN7X40GK52ghDTpNS0ihKwNkKH6/x+2SjSwwlVmR2PdIHyDTsDSMNe++77uVh3byx8GcQMxADtujC5i5Xgs5O8j/ky6Ydt9R5w5qdSEp1p4iiUISgVs3G0bcDvmsHtFU7BB9qmXT7DTxI0RP7GXtd4Rdm5N1yDUXcWrkaqdYfOSqDHcijoWEx9WPnHK9/wv4Z2h7k5vDegaks4Se3lde+O44lfMjv4jo8Klsep1RElMSugHZHKa7ojKjej1LbYogUcfSo0nFS2jdNZwjsmrJPpzW1ilVyUGtUKoBCVwj+SCDFgEHPT2IuxhyHSGL1eVzVoqdc7xee3oUh1KNRFxZRYSuz1+LDhcxTP64afkelyYrdRdHmq7SUI0jLEPu5j7M91cC4Cxne5P38ZP/2j+teGgk9D4GEzppPntZQR8tLkFpxJO2SIPG681J/lJiJhOYSuq6HfRxHNEoaTZaD06b6oJ+yimQiIzZL1l4hKE=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jul+03+2025+15%3A54%3A59+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1147e6f6-a20a-477a-8e82-6e78d22b99c2&interactionCount=1&landingPath=NotLandingPage&groups=BG117%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_BG%3A1%2CC0004%3A1&AwaitingReconsent=false; cto_bundle=hXabOF9hdlpuSHdXS0lodiUyQldHWWRLbFVpYUtnaXhHU2wxbkRrSEdQZ1JmbWRzUzdKVXNZdjJHJTJCd2dlNzU0SmQxbFE1RSUyRjBBJTJCMXd2YVViZmdvazdSZmJOaWlNWHNTWk1EQkNYVFVpeEM0ViUyRkklMkZqVDVMUWVlTEowZnRvZ1ZRTU9RUUtwdGppYkw4ZzRMZ01YQzdBcFZ0JTJGSyUyQnl5aU4lMkJmNExWWUhCYnl3T0xyYXdWQ2g5JTJCUGZ6YW1yVFc1b2w1JTJCY210ZnRISUVGVDlUZUh2UTcyQnZ2QWF2QWxwQjJBJTJGc003Y0dlT2V4MWk4ZHZlQlM1RTZ6Zm50QXNGS090YVpZeFNTbTNKVkhuMjZSZ3JYNG5jckh3Z0Q3dGY5OVpKVmslMkIlMkJHaVpjWm1Pb1Y4TEMlMkJXMUh3WER5Z1pObVBjelFUbGNnWTRtUg; _lr_hb_-costco%2Fproduction-vrwno={%22heartbeat%22:1751538301328}; RT="z=1&dm=www.costco.com&si=699c4b3a-6f41-456c-a09f-15923d9f4168&ss=mcn8odqm&sl=1&tt=56w&bcn=%2F%2F684d0d48.akstat.io%2F&ld=572"; bm_lso=9BD53DAE6CA51BCEC4838BC39A5D1A8D461932BB52586E3C5CEDB09DE2FC59DE~YAAQ7/Q3FyosOLCXAQAAs/DRzwQPVpxfuY9IbEhqrkejWqe+sNnjBKtRGRNyaPxP1Q6No4auPSg/XsJI+ZK9gkFuUqA4JiSyNiR2irfImwqrfQeAVIe909iOx1fL7KofZEBEcQwHFMzMRW/Pu4ZbGPqMncgRXAZj7VBdEPGgGyyOpRdu2qJYOFRiw6UiUg+ENLcPGtsjoIzlz+YjeqpIvSTteAWyEri/XJZl8H/vWHD2ADTq+R+EuObuNO6X/+WVbnqLf650N1Yl+3T0b/W/Jdz63qGvlBkOM0T6xCQ3WOqqK5QBJ4lOKuFw7YlQiiQJ6AbWBxt735tz1JT2/IJACY0PaRGbHM9Gccxxgq78RMSgwTkJ3aLnmR3FGyxthnv6Y0OV57WgYObMuH9WcX+LydoK+LG+w04PoCTHO9JwJxYjNtqYEk4rXnn+Pd9MHxXMrj7GHqnBIeXEuYZzNZM=^1751538302134; akavpau_zezxapz5yf=1751538660~id=e0d632fd0b572f72dcd90b7f4943d0fd; bm_sv=8EF76AED4FF29936B7F024DA58143575~YAAQ7/Q3F1kuOLCXAQAARF/SzxwmBIUaidr6GFZsbVRuiL/MhN/VH0Pc/RGgJ2dTb9sBt6eF/MCJgL7sxkySW2vR66g/I7oiux57r32P4L7C3VLs/0DNTVBZJ7axYugpllzE/vSFz9kgFCRTXfgV0OJTzdAmmlE60pMmzy7I+BTmHlkmIfWrS3nqQkhzq7fnGSLVNC2kaiywS6VKT7ewkhwdD3NPWUh5LPoercQfgITenq8415cg0SXQF3YxZRUqTg==~1; _lr_tabs_-costco%2Fproduction-vrwno={%22recordingID%22:%226-0197cfcf-31a8-76b4-b010-e5b1246ee09e%22%2C%22sessionID%22:0%2C%22lastActivity%22:1751538339676%2C%22hasActivity%22:true%2C%22confirmed%22:false%2C%22recordingConditionThreshold%22:%228.55370693574593%22}',
}

url_lst=['https://www.costco.com/collin-street-bakery-mini-pecan-cake-bundle-9-oz-per-cake.product.4000275908.html',
    "https://www.costco.com/collin-street-bakery-mini-pecan-cake-bundle-9-oz-per-cake.product.4000275908.html",
    "https://www.costco.com/davids-cookies-mile-high-peanut-butter-cake-68-lbs-14-servings.product.100338715.html",
    "https://www.costco.com/st-michel-madeleine-classic-french-sponge-cake-100---count.product.100517831.html",
    "https://www.costco.com/davids-cookies-mango--strawberry-cheesecake-2-count-28-slices-total.product.100496548.html",
    "https://www.costco.com/austin-cake-ball-catering-assortment-48-cake-balls.product.4000035726.html",
    "https://www.costco.com/davids-cookies-no-sugar-added-cheesecake--marble-truffle-cake-2-pack-28-slices-total.product.100494269.html",
    "https://www.costco.com/davids-cookies-premier-chocolate-cake-72-lbs-serves-14.product.100338718.html",
    "https://www.costco.com/davids-cookies-chocolate-fudge-birthday-cake-375-lbs--includes-party-pack-16-servings.product.100431056.html",
    "https://www.costco.com/collin-street-bakery-cake-bites-bundle-deluxe-fruitcake--pineapple-pecan-cake-2-pack-24-bites-total.product.4000284537.html",
    "https://www.costco.com/mary-macleods-gluten-free-shortbread-cookies-mixed-assortment-8-pack.product.100799668.html",
    "https://www.costco.com/ferraras-bakery-new-york-cheesecake-2-pack.product.100760705.html",
    "https://www.costco.com/the-cake-bake-shop-8-round-pixie-fetti-cake-16-22-servings.product.4000181454.html",
    "https://www.costco.com/mary-macleods-shortbread-variety-tin-3-pack-24-cookies-per-tin.product.4000159297.html",
    "https://www.costco.com/ferraras-bakery-8-in-tiramisu-cake-2-pack.product.4000233634.html",
    "https://www.costco.com/the-cake-bake-shop-8-round-chocolate-cake-16-22-servings.product.4000181494.html",
    "https://www.costco.com/davids-cookies-10-rainbow-cake--12-servings.product.100498608.html",
    "https://www.costco.com/davids-cookies-variety-cheesecakes-2-pack-28-slices-total.product.100158259.html",
    "https://www.costco.com/davids-cookies-brownie-and-cookie-combo-pack.product.100130229.html",
    "https://www.costco.com/davids-cookies-90-piece-gourmet-chocolate-chunk-frozen-cookie-dough.product.100651546.html",
    "https://www.costco.com/collin-street-bakery-cinnamon-coffee-cake-379-lb.product.4000275903.html",
    "https://www.costco.com/davids-cookies-butter-pecan-meltaways-3-pack-6-lb-total.product.4000315234.html",
    "https://www.costco.com/hostess-cupcakes--twinkies-32-count.product.4000153042.html",
    "https://www.costco.com/la-grande-galette-french-butter-cookies-13-lb-6-pack.product.100302567.html"


         ]

costco_lst=[]

for i in url_lst:
    print(i)
    name=i.split('/')[-1]
    print(name)
    response=requests.get(i,cookies=cookies,headers=headers)




    print(response.status_code)

    raw_html=response.text
# print(raw_html)

    output_path=fr'C:\Users\Madri.Gadani\Desktop\madri\costco\html_page_extraction\costco1_{name}.html'
    gzip_output_path=fr'C:\Users\Madri.Gadani\Desktop\madri\costco\html_page_extraction\costco_gzip1_{name}.html'

    #
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(raw_html)
    print("HTML content fetched and written successfully.")

    with open(output_path, 'rb') as file_binary:
        with gzip.open(output_path + '.gz', 'wb') as file_gzip:
            file_gzip.writelines(file_binary)
    print('file has been saved in compressed zip file.')





    selector = Selector(text=raw_html)

    title=selector.xpath('//div[@class="product-h1-container-v2 visible-lg-block visible-xl-block"]/h1/text()').get()
    print('title:',title)

    # price=selector.xpath('//div[@id="pull-right-price"]/span/text()').getall()
    # print('price:',price)

    match = re.search(r"priceTotal:\s*initialize\(([\d.]+)\)", response.text)
    if match:
        price = match.group(1)
        print("Price:", price)
    else:
        print("Price not found")


    features=selector.xpath('//ul[@class="pdp-features"]//text()').getall()
    print('features:',features)
    cleaned_features = [item.strip() for item in features if item.strip()]

    for i, feature in enumerate(cleaned_features, 1):
        print(f"{i}. {feature}")


    img_link = selector.xpath('//img[@id="initialProductImageSticky"]/@src').get()
    print("Image Link:", img_link)

    costco_dict={
        'title':title,
        'price':price,
        'features':cleaned_features,
        'img_link':img_link,


    }
    costco_lst.append(costco_dict)
print(costco_lst)

json_path=r'C:\Users\Madri.Gadani\Desktop\madri\costco\costco_json.json'


with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(costco_lst, f, indent=4, ensure_ascii=False)

print("✅ JSON saved after full cleaning.")



exit(0)

