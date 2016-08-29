## file_sort.py ##

說明: 目前放置學習單的頁面是以檔名做排序，這隻腳本可以在檔名前加上編號，方便放到網頁上時將檔案依照班級排列。

使用方式: 

1. 建立一個input目錄跟這隻腳本放在一起，並將要排序的檔案放入。
2. 確定要排序的檔案名稱中已經有填入班級，並檢查 file_sort.py 中 file_order 這個陣列中的班級順序。
3. 執行後會直接修改 input 中的檔名。

## photo_preprocess.py ##

說明: 網站上要展示的照片不適合使用原始大小的圖檔，這隻腳本能幫你將照片壓縮並產生縮圖。以104學年的[活動剪影](http://meihoreadingproject104.appspot.com/gallery.html)為例，進入網頁後應該用裁減過的照片做為每個相簿首頁，而點擊照片後跳出的大圖應該要壓縮過。最後放置在 Google 相簿中的照片應該是原始圖檔。

使用方式:

1. 壓縮圖檔的功能是使用 [TinyPNG](https://tinypng.com/) 服務，必須事先到[開發者頁面](https://tinypng.com/developers)申請 API key。
2. 安裝 [tinify](https://tinypng.com/developers/reference/python) 套件，並將前一步驟申請的 key 填入 photo_preprocess.py。
3. 建立一個 gallery 目錄並將要處理的圖檔放入，該目錄要跟腳本放在一起。
4. 執行後會產生以下兩個目錄:
    - compress 壓縮後的圖檔，照片尺寸與原始檔案相同但較小。
    - thumb 縮小後的圖檔，預設尺寸為 300*200。