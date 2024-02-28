import execjs
import requests
# import json


def enc(reqtext):
    jstext = open("wyy.js", "r").read()
    wyyjs = execjs.compile(jstext)
    enctext = wyyjs.call("enc", reqtext)
    data_params = enctext["encText"]
    encSecKey = enctext["encSecKey"]
    return data_params, encSecKey


def search(artist):
    reqtext = {
        "hlpretag": "<span class=\"s-fc7\">",
        "hlposttag": "</span>",
        "s": artist,
        "type": "1",
        "offset": "0",
        "total": "true",
        "limit": "100",
        "csrf_token": "562bdf941a79d3db532a0f3160c74785"
    }
    data_params, encSecKey = enc(reqtext)
    cookies = {
        'NMTID': '00OP70Mq8pXZtAHrURLo1j5j_y5a60AAAGNz8qvWA',
        '_iuqxldmzr_': '32',
        '_ntes_nnid': 'f97f3184bb25b98ed071cfc5a680293d,1708588184401',
        '_ntes_nuid': 'f97f3184bb25b98ed071cfc5a680293d',
        'WEVNSM': '1.0.0',
        'WNMCID': 'clelae.1708588184844.01.0',
        'WM_TID': 'ANkWhUXis7hARFBARVOVo7Dr8YykSUzg',
        'sDeviceId': 'YD-7HzDu%2BidGn1FBgEEBQOA5qSqsI31phZm',
        'ntes_utid': 'tid._.cWit3Z3JPapBQwQRABLU9%252BD%252B9Yn02sIz._.0',
        '__snaker__id': 'pBR9WCWGZlx3A2yg',
        'gdxidpyhxdE': 'ppLc7XQkPsCvgdeKSM%2Bpf5%5C69E1XAoYfcj%2FZQdaPJA%2BiEZUoueWMXYQL5BB3tPtO%5CotaQP14uxbQgH%5Cu%2FhH%2FLk%5CBVuwJHLBJhLNrrcpOESP6NOTgMz2uJ6bXC84HGWTR5lexLWntHaKIv7YZjoeC5XxBRSdZKvDkxhx93nUPpk9hLRNe%3A1708589109055',
        'P_INFO': '17601280736|1708588295|1|music|00&99|null&null&null#gud&440100#10#0|&0||17601280736',
        '__remember_me': 'true',
        '__csrf': '62349a514f90e2f2c510a92e17199898',
        'MUSIC_U': '00C804D66E8F61C495CC0C783164F7D122D507EAC7B8DA7BD99FD9D227077D70F461FF23C628A5B22C5B7E6B90745B150149154861E203AE3E07A863B87D6468603A4572DCF35F2B51F9CA4C0CFC57562CC21CE705A9E8E3E70795770DC7F22D871CE478F06E9F0AA96C8B8CAD7DFE8F4062AEF163566459EE7852E16A726DED24C3F5DF074EB2A5CD0B8A8D747D509EE87AADC1E387176A3A913FD569C0B18ADE42BFFF467A318848FCEFD0F209517C67A837F6FB5DF9379A6D00B9700C2C9D02F5518823419DF4517030E6571532F6718358742EE9104E521BF25A626677EA56A14B225ED55F9CD43004E33EDD063DF3C871FC5318874B3E7FC6B9A7362460FEED317C9E075804A784B53066D2CB70B3CAFA278F02659269663BB7BBE318AF2A5306061C022DAAEAF4302FD45D3A873A81144C0CF2680DA5FAA828D5F51CCF1AEB3C288FBE81BC325E207339D466ADE004324784E10AB8B5B9D27AAADA63090FAAFD0E849FD20C8514311D8781D50B76',
        'ntes_kaola_ad': '1',
        'JSESSIONID-WYYY': '5nJR1iNN3T1%5Ci1qd7q25DXuNddNlxEEp8vy5g8UB%5CTFHV455gfncXBHzskgZ3Xow8jpYU%2BbN9rAWmAfgR%2B5dK1GgF%2FfXWtrsOnodUtCiSK1V%5C5H5XGm04%2FDKEF2DvCeI4MxGkfN1vv9Om3YZZi62OPD%5CcMTi3glOr%5Ct4bZl8GMCjnC%2FD%3A1708677854475',
        'WM_NI': 'iXrGArjigGGJBiKDhC9q9BbmDh3hFdBqoGVFOM7jQ%2FMQhJzLgLjAlaW1%2BB8hhX%2Fe%2B73lIwYGYdCmV1incRWnX3kG43EW6vV%2ByFVMOVw%2BD638k2gtjUCabO2AjPti3WD%2FdUk%3D',
        'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeacb67eb69f83b5cf619cef8fa3c45f868b9bacc880b693a3b2c27a83eabe8cd22af0fea7c3b92aab88bea8c47aaab7a9a8c64282b785a5eb49fbaff7a3e16788b8fd89c57082afa1a8d54e8d93f98bd4258f8fa8abf948a594a6a2ef6b95efe5a3bb64ac88e186aa3df1b48798dc4d9bbc8d8ed53babb2adb3d6669ceda5a8b7398789fa97d521bb9a9aaece5eb5f58cd7b234a9eea995e95f81bfaeb0b14baa90bc8ab25d88f1acb6ea37e2a3',
    }

    headers = {
        'authority': 'music.163.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'NMTID=00OP70Mq8pXZtAHrURLo1j5j_y5a60AAAGNz8qvWA; _iuqxldmzr_=32; _ntes_nnid=f97f3184bb25b98ed071cfc5a680293d,1708588184401; _ntes_nuid=f97f3184bb25b98ed071cfc5a680293d; WEVNSM=1.0.0; WNMCID=clelae.1708588184844.01.0; WM_TID=ANkWhUXis7hARFBARVOVo7Dr8YykSUzg; sDeviceId=YD-7HzDu%2BidGn1FBgEEBQOA5qSqsI31phZm; ntes_utid=tid._.cWit3Z3JPapBQwQRABLU9%252BD%252B9Yn02sIz._.0; __snaker__id=pBR9WCWGZlx3A2yg; gdxidpyhxdE=ppLc7XQkPsCvgdeKSM%2Bpf5%5C69E1XAoYfcj%2FZQdaPJA%2BiEZUoueWMXYQL5BB3tPtO%5CotaQP14uxbQgH%5Cu%2FhH%2FLk%5CBVuwJHLBJhLNrrcpOESP6NOTgMz2uJ6bXC84HGWTR5lexLWntHaKIv7YZjoeC5XxBRSdZKvDkxhx93nUPpk9hLRNe%3A1708589109055; P_INFO=17601280736|1708588295|1|music|00&99|null&null&null#gud&440100#10#0|&0||17601280736; __remember_me=true; __csrf=62349a514f90e2f2c510a92e17199898; MUSIC_U=00C804D66E8F61C495CC0C783164F7D122D507EAC7B8DA7BD99FD9D227077D70F461FF23C628A5B22C5B7E6B90745B150149154861E203AE3E07A863B87D6468603A4572DCF35F2B51F9CA4C0CFC57562CC21CE705A9E8E3E70795770DC7F22D871CE478F06E9F0AA96C8B8CAD7DFE8F4062AEF163566459EE7852E16A726DED24C3F5DF074EB2A5CD0B8A8D747D509EE87AADC1E387176A3A913FD569C0B18ADE42BFFF467A318848FCEFD0F209517C67A837F6FB5DF9379A6D00B9700C2C9D02F5518823419DF4517030E6571532F6718358742EE9104E521BF25A626677EA56A14B225ED55F9CD43004E33EDD063DF3C871FC5318874B3E7FC6B9A7362460FEED317C9E075804A784B53066D2CB70B3CAFA278F02659269663BB7BBE318AF2A5306061C022DAAEAF4302FD45D3A873A81144C0CF2680DA5FAA828D5F51CCF1AEB3C288FBE81BC325E207339D466ADE004324784E10AB8B5B9D27AAADA63090FAAFD0E849FD20C8514311D8781D50B76; ntes_kaola_ad=1; JSESSIONID-WYYY=5nJR1iNN3T1%5Ci1qd7q25DXuNddNlxEEp8vy5g8UB%5CTFHV455gfncXBHzskgZ3Xow8jpYU%2BbN9rAWmAfgR%2B5dK1GgF%2FfXWtrsOnodUtCiSK1V%5C5H5XGm04%2FDKEF2DvCeI4MxGkfN1vv9Om3YZZi62OPD%5CcMTi3glOr%5Ct4bZl8GMCjnC%2FD%3A1708677854475; WM_NI=iXrGArjigGGJBiKDhC9q9BbmDh3hFdBqoGVFOM7jQ%2FMQhJzLgLjAlaW1%2BB8hhX%2Fe%2B73lIwYGYdCmV1incRWnX3kG43EW6vV%2ByFVMOVw%2BD638k2gtjUCabO2AjPti3WD%2FdUk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacb67eb69f83b5cf619cef8fa3c45f868b9bacc880b693a3b2c27a83eabe8cd22af0fea7c3b92aab88bea8c47aaab7a9a8c64282b785a5eb49fbaff7a3e16788b8fd89c57082afa1a8d54e8d93f98bd4258f8fa8abf948a594a6a2ef6b95efe5a3bb64ac88e186aa3df1b48798dc4d9bbc8d8ed53babb2adb3d6669ceda5a8b7398789fa97d521bb9a9aaece5eb5f58cd7b234a9eea995e95f81bfaeb0b14baa90bc8ab25d88f1acb6ea37e2a3',
        'nm-gcore-status': '1',
        'origin': 'https://music.163.com',
        'referer': 'https://music.163.com/search/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    params = {
        'csrf_token': '62349a514f90e2f2c510a92e17199898',
    }

    data = {
        'params': data_params,
        'encSecKey': encSecKey,
    }

    response = requests.post(
        'https://music.163.com/weapi/cloudsearch/get/web',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    resjson = response.json()
    sid_list = []
    songs = resjson['result']['songs']
    i = 0
    for song in songs:
        i = i + 1
        print(i, song['ar'][0]['name'] + '-' + song['name'])
        sid_dic = {
            "id": song['id'],
            'name': song['name'],
            'artist': song['ar'][0]['name']}
        sid_list.append(sid_dic)
    return sid_list
# print(sid_list[1].get("id"))


def download_song(sid):
    reqtext = {
        'ids': '[%s]' % (sid),
        'level': 'standard',
        'encodeType': 'aac',
        'csrf_token': '62349a514f90e2f2c510a92e17199898'}

    cookies = {
        'NMTID': '00OP70Mq8pXZtAHrURLo1j5j_y5a60AAAGNz8qvWA',
        '_iuqxldmzr_': '32',
        '_ntes_nnid': 'f97f3184bb25b98ed071cfc5a680293d,1708588184401',
        '_ntes_nuid': 'f97f3184bb25b98ed071cfc5a680293d',
        'WEVNSM': '1.0.0',
        'WNMCID': 'clelae.1708588184844.01.0',
        'WM_TID': 'ANkWhUXis7hARFBARVOVo7Dr8YykSUzg',
        'sDeviceId': 'YD-7HzDu%2BidGn1FBgEEBQOA5qSqsI31phZm',
        'ntes_utid': 'tid._.cWit3Z3JPapBQwQRABLU9%252BD%252B9Yn02sIz._.0',
        '__snaker__id': 'pBR9WCWGZlx3A2yg',
        'gdxidpyhxdE': 'ppLc7XQkPsCvgdeKSM%2Bpf5%5C69E1XAoYfcj%2FZQdaPJA%2BiEZUoueWMXYQL5BB3tPtO%5CotaQP14uxbQgH%5Cu%2FhH%2FLk%5CBVuwJHLBJhLNrrcpOESP6NOTgMz2uJ6bXC84HGWTR5lexLWntHaKIv7YZjoeC5XxBRSdZKvDkxhx93nUPpk9hLRNe%3A1708589109055',
        'P_INFO': '17601280736|1708588295|1|music|00&99|null&null&null#gud&440100#10#0|&0||17601280736',
        '__remember_me': 'true',
        '__csrf': '62349a514f90e2f2c510a92e17199898',
        'MUSIC_U': '00C804D66E8F61C495CC0C783164F7D122D507EAC7B8DA7BD99FD9D227077D70F461FF23C628A5B22C5B7E6B90745B150149154861E203AE3E07A863B87D6468603A4572DCF35F2B51F9CA4C0CFC57562CC21CE705A9E8E3E70795770DC7F22D871CE478F06E9F0AA96C8B8CAD7DFE8F4062AEF163566459EE7852E16A726DED24C3F5DF074EB2A5CD0B8A8D747D509EE87AADC1E387176A3A913FD569C0B18ADE42BFFF467A318848FCEFD0F209517C67A837F6FB5DF9379A6D00B9700C2C9D02F5518823419DF4517030E6571532F6718358742EE9104E521BF25A626677EA56A14B225ED55F9CD43004E33EDD063DF3C871FC5318874B3E7FC6B9A7362460FEED317C9E075804A784B53066D2CB70B3CAFA278F02659269663BB7BBE318AF2A5306061C022DAAEAF4302FD45D3A873A81144C0CF2680DA5FAA828D5F51CCF1AEB3C288FBE81BC325E207339D466ADE004324784E10AB8B5B9D27AAADA63090FAAFD0E849FD20C8514311D8781D50B76',
        'ntes_kaola_ad': '1',
        'JSESSIONID-WYYY': 'IEqjQhKvyOJtccz6uJnDtp93erdy144jRF1lj3w%2B4%5CTsiPSkzhR%5C7QRPeynrVUx7iPqObq%5CDfYJyDtJaE3Fg0Fmgc%5CwWghOBjgDUdrKkoo1SEAybn1y4zlBGUBOoiZ37VMVlYpbH96Sl9VSxsIMMAt0Ng%2BgHbYdyKV49KPicnvjm4BDa%3A1708911066983',
        'WM_NI': 'lGD79E7EfaLyuazgTzaTrRTIxBGTSDMcKqORRBK4G3PQ91mpeeGteoOPiNjgsc0sJPJ1oKty4rjd0%2Ba6uqvzs5839wmaskyryTbX6Xf%2FFAu0aVnCQMufmAN7qU2mxaz0UnI%3D',
        'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee94bc489cabe1cce86f89b88ba6d45f879a9bacd133e9b496d0e53c8ab6a7d8d82af0fea7c3b92ab0998cd8bc4ff59baa82cf73b7bfb688d772a38cbeb3d743bc9e89b5d2508fbd8592ce5a929e85d5c639948ff7d2f07ca7bb8995e8658d90a7afe96db1bd0094c95c8aefa1acf773f8aea685b321a3eabb92f572b1ebf8d4bc7dafbfbd8cfc7abb8caeb9b554a6f18aa2f83ca38aa2a4d447b7baa3a2cd3db38bfe8efb6bbaf09b8fcc37e2a3',
    }

    headers = {
        'authority': 'music.163.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://music.163.com',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    }

    params = {
        'csrf_token': '62349a514f90e2f2c510a92e17199898',
    }
    data_params, encSecKey = enc(reqtext)
    data = {
        'params': data_params,
        'encSecKey': encSecKey,
    }

    response = requests.post(
        'https://music.163.com/weapi/song/enhance/player/url/v1',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    url = response.json().get('data')[0]["url"]

    return url


def main():
    artist = input("请输入需要查询的歌手名：")
    slist = search(artist)
    try:
        i = int(input("请输入需要下载的歌曲序号（如输入-1则退出程序）："))
    except ValueError:
        i = int(input("您输入的好像不是序号哦，请重新输入："))
    if i != -1:
        sid = slist[i - 1].get("id")
        url = download_song(sid)
        if url is not None:
            print("已获取到下载链接：", url, "\n正在为您下载.......")
            sname = slist[i - 1].get("name")
            form = url.split('.')[-1][:3]
            artist = slist[i - 1].get('artist')
            with open('./song/' + artist + '-' + sname + '.' + form, 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
            print("下载成功！")
        else:
            print("未获取到下载链接，可能是VIP专享歌曲！")
    else:
        print("感谢您的使用，再见！")
        quit()


if __name__ == '__main__':
    while True:
        main()
