from bs4 import BeautifulSoup
import requests
import time

url ='https://cn.tripadvisor.com/Attractions-g60763-Activities-oa30-New_York_City_New_York.html'
urls=['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html'.format(str(i)) for i in range(30,60,30)]

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'cookie':'ServerPool=C; TAUnique=%1%enc%3AFiTBY4N2wl3OB0po4gk017CX986uIG8oDSe%2BCzGdxG4nuvWISCXjiA%3D%3D; TAPD=cn.tripadvisor.com; TASSK=enc%3AADvISKtm3sFbOv0NOx%2FFTKTaXDEkYCtO8a0Si1OYK0tq7aUwcR3%2B98jn5q%2BIEHxn%2F6XjJXSHJ%2BWlTuI2vwwGbhkoQCWD45oemUccotx5hDWo71XyVShHQFENbe1p1yu%2FkA%3D%3D; PMC=V2*MS.77*MD.20180406*LD.20180406; PAC=ANS7E425EOcuAZ5UYp2uY_xiQ1d__aoTIsuhL2RzvaozJL8RHnOTU4FEWi0VYXaU10FiFcBfsPefYr15zvecaveYS4puC6ptZPGKWY4qT-TOsgyPyNGZcbkgtsOejcpkoSRfdanl4mVTELPsJpGA_ymPnjqAFLWIKQTncfm2Eb5v5WBNUu-exDvJl0ZMOz5G120hozGgnzxfNG39OtuilAeqG0YV8qohzypDd7HRi8-uj6YsWMM5_FdePWJ7KfN0m4LJt4tc7pzDCVXi48aBHIjqXsS-lu4OeLosZd1-hrtXSIBfhy70N3Ct4ywOiQ10aw%3D%3D; TART=%1%enc%3AzgdKaOIJNNe9gR7rtAzuey6Do5Lal1WAQdiLsafLvUOus4Z4VBvnisf4Xlr8lOI36TFKgc4nnNY%3D; SecureLogin2=3.4%3AAA32eIKabc6UjQ%2B1Cl4N14z%2Bviw0cGMbgPeB3%2BN8YkMombZeNELDVRXdwC9k%2F4uXRA3RMwogcCuoDKLON7H%2B%2BBgzRnSETn7UmtsFjhxKPVjNYUjjGll2IJWqbA6PoL1%2Fn7untF7txqIPacrEJ4%2F%2BauD%2Fq5IZID%2Bslh9i0X8n%2B3F9X0QeLv%2BfjjUeRE6XZwnUiXRm%2FKhLgFMpVSJW3zycL9E%3D; TAAuth3=3%3Ae182238c462a0e2d565b81caad6325cf%3AAN%2FnR8EsGIAeQD18UWRuG%2FGubrk%2F88GhJpQBYh9VSmcrb3BqsG0u2n%2F1HK0KU%2F3b0ARU0hyhncQiKwaOWeIUhpgLqcyX%2FqMjjSpEjxBnfagkimrMEYGDICohKCdeFk%2FEQiDRHBc%2B6QvBqcAqNcTKE3y9IhI6JxyNbDrV8o29kjD0jb7%2FowSPY9CbWkRzVGlOX%2FaLQj%2FUiXNhK5HzgHV1cqg%3D; ki_r=; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*DSM.1523010942442*RS.1; ki_t=1523007952436%3B1523007952436%3B1523010977158%3B1%3B6; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7Ccatchsess%2C8%2C-1%7Cbrandsess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C2%2C1523097494%7CCCSess%2C1%2C-1%7CCpmPopunder_2%2C2%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1523612314%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CSCA%2C%2C-1%7CTheForkORPers%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C1%2C1586079945%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-oa30-New_York_City_New_York.html; roybatty=TNI1625!AJc%2BQukPQTG%2F4BL0PzG1KwM18xSDClLBBN2ZeizT%2FhyejdUHdvcSVocgUoCWmBLQruYXITJSnMMnf9fGRJAZ0840oOFoCVUBmOecxVa5dIUxIiT2ha7ZSSkCaQn%2FmT6VgGoKKsOYVCzqJqbu49m87oQyVoWGfLW3aO04QrzpU2SH%2C1; TASession=%1%V2ID.A6178D1A4479FDB8887B6A44D98B0071*SQ.147*PR.39776%7C*LS.DemandLoadAjax*GR.98*TCPAR.21*TBR.37*EXEX.36*ABTR.54*PHTB.79*FS.10*CPU.57*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.6308E5E905292E726BA77A1B3B758DD4*LF.en*FA.1*DF.0*IR.1*OD.null*FBH.2*MS.-1*RMS.-1*TRA.true*LD.60763; TAUD=LA-1523007476932-1*RDD-1-2018_04_06*LG-4363803-2.1.F.*LD-4363804'
}

def get_attractions(url,data=None):
    wb_data=requests.get(url,headers=headers)
    time.sleep(2)
    soup=BeautifulSoup(wb_data.text,'lxml')
    titles=soup.select( 'div.listing_info > div.listing_title > a')
    img=soup.select( 'img[height="180"]')
    cates=soup.select( 'div.listing_info > div.tag_line > div > a > span')

    if data==None:
        for titles,img,cates in zip(titles,img,cates):
            data={
                'titles':titles.get_text(),
                'img':img.get('src'),
                'cates':list(cates.stripped_strings),
            }
            print(data)

for single_url in urls:
    get_attractions(single_url)





























