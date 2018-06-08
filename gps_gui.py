import os,sys,time,numpy
import tkinter as tk
import gps_class,distance2points

gps_after_flag = True

def call_gps_info_get():
    global gps_after_flag
    gps_info = gps.get_gps_info().split(",")
    print(gps_info)
    
    #1つ前の座標と、今回の座剽悍の距離を取得
    distance_label["text"] = str(d2p.exchange(float(old_latitude_label["text"]),p60(gps_info[3]),float(old_longitude_label["text"]),p60(gps_info[5]))) + "m"
    
    #今回取得の情報を表示エリアへ入力
    utc_time_label["text"] = "UTC:["+utc2jp(gps_info[1])+"]"
    status_label["text"] = "status:["+gps_info[2]+"]"
    
    latitude_label["text"] = "緯度:["+str(p60(gps_info[3]))+"]"
    old_latitude_label["text"] = str(p60(gps_info[3]))
    NS_label["text"] = "北南:["+gps_info[4]+"]"
    
    longitude_label["text"] = "経度:["+str(p60(gps_info[5]))+"]"
    old_longitude_label["text"] = str(p60(gps_info[5]))
    EW_label["text"] = "東西:["+gps_info[6]+"]"
    
    speed_label["text"] = "速度:"+str(knot2km(gps_info[7]))+"]"
    orientation_label["text"] = "真方位:["+gps_info[8]+"]"
    utc_date_label["text"] = "日付:["+gps_info[9]+"]"
    orientation_gyap_label["text"] = "磁北真北差:["+gps_info[10]+"]"
    orientation_gyap_EW_label["text"] = "磁北真北差東西:["+gps_info[11]+"]"
    mode_label["text"] = "モード:["+gps_info[12]+"]"
    
    
    if gps_after_flag == True:
        llabel["text"] = gps_after_flag
        root.after(1000,call_gps_info_get)

def gps_start():
    global gps_after_flag
    gps_after_flag = True
    llabel["text"] = gps_after_flag
    call_gps_info_get()

def gps_stop():
    global gps_after_flag
    gps_after_flag = False
    llabel["text"] = gps_after_flag
    
def utc2jp(utc):
    time = utc.split(".")
    jp_time = [(i+j) for (i,j) in zip(time[0][::2],time[0][1::2])]
    h = int(jp_time[0]) + 9
    if h > 24:
        h = h-24
    return str(h) + ":" + jp_time[1] + ":" + jp_time[2]

def knot2km(speed):
    if speed == "":
        speed = "0"
    
    knot = float(speed)
    return str(knot * 1.852) + "km/h"

def p60(ido_keido):
    if ido_keido == "":
        ido_keido = "0"
    ik = float(ido_keido)
    return ik / 60

#枠を表示
root = tk.Tk()
root.title("GPS")

#GPS_classのインスタンス化
gps = gps_class.gps_info_get()

#distance2pointsのインスタンス化 2点間の距離計算するもジュール
d2p = distance2points.distance2points()

#USB接続を確認
path = '/dev/ttyUSB0'
message = "準備完了"
if not os.path.exists(path):
    message = "GPSユニットが接続されていません"

#ラベルを追加
label = tk.Label(root,text=message)
label.grid(row=1,column=0)

#実効フラグ
llabel = tk.Label(root,text=gps_after_flag)
llabel.grid(row=1,column=2)

#GPSデータの分割表示
utc_time_label = tk.Label(root,text="utc_time")
utc_time_label.grid(row=2,column=1)

status_label = tk.Label(root,text="status")
status_label.grid(row=2,column=2)

latitude_label = tk.Label(root,text="status")
latitude_label.grid(row=2,column=3)

NS_label = tk.Label(root,text="NS")
NS_label.grid(row=2,column=4)

longitude_label = tk.Label(root,text="longitude")
longitude_label.grid(row=2,column=5)

EW_label = tk.Label(root,text="EW")
EW_label.grid(row=2,column=6)

speed_label = tk.Label(root,text="speed")
speed_label.grid(row=2,column=7)

orientation_label = tk.Label(root,text="orientation")
orientation_label.grid(row=2,column=8)

utc_date_label = tk.Label(root,text="utc_date")
utc_date_label.grid(row=2,column=9)

orientation_gyap_label = tk.Label(root,text="orientation_gyap")
orientation_gyap_label.grid(row=2,column=10)

orientation_gyap_EW_label = tk.Label(root,text="orientation_gyap_EW")
orientation_gyap_EW_label.grid(row=2,column=11)

mode_label = tk.Label(root,text="mode")
mode_label.grid(row=2,column=12)

#row3
old_latitude_label = tk.Label(root,text="0")
old_latitude_label.grid(row=3,column=0)

old_longitude_label = tk.Label(root,text="0")
old_longitude_label.grid(row=3,column=1)

distance_label = tk.Label(root,text="0m")
distance_label.grid(row=3,column=2)

#ボタンを表示
start_button=tk.Button(root,text="Startボタン",command=gps_start)
start_button.grid()

end_button=tk.Button(root,text="Endボタン",command=gps_stop)
end_button.grid()

root.mainloop()