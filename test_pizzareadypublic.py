# -*- encoding=utf8 -*-
__author__ = "Supercent"

from airtest.core.api import *

connect_device("Android:///")


touch(Template(r"tpl1746680027562.png", record_pos=(-0.346, -0.371), resolution=(1080, 2400)))


# 2. 앱 로딩 대기
sleep(20.0)


openads = exists(Template(r"tpl1748340468070.png", record_pos=(0.355, -0.978), resolution=(1080, 2400)))

if openads:
    touch(openads)
    print("✅ 앱오픈 광고 닫기")
else:
    print("⏭ 광고 닫기 버튼이 없어, 다음 단계로 진행합니다.")
    
sleep(3.0)


give = exists(Template(r"tpl1746680138516.png", record_pos=(0.001, 0.596), resolution=(1080, 2400)))

if give:
    touch(give)
    print("✅ 오프라인 보상 획득 완료")
else:
    print("⏭ 획득하기 버튼이 없어, 다음 단계로 진행합니다.")
    
    
    
sleep(4.0)


def move_right(duration=1.0):
    swipe((200, 1800), (50, 2200), duration=0.6)
    print("➡️ 돈더미 이동")

# 반복 루프
for _ in range(3):
    move_right(duration=0.3)  # 짧게 조작
    sleep(0.5)

def move_right(duration=1.0):
    swipe((200, 1800), (80, 1500), duration=0.6)
    print("➡️ 문 만들기 이동")

for _ in range(2):
    move_right(duration=0.3)  # 짧게 조작
    sleep(0.5)

sleep(9.0)
    
def move_right(duration=1.0):
    swipe((200, 1800), (80, 1650), duration=5.0)
    print("➡️ 테이블 설치 이동1")

for _ in range(1):
    move_right(duration=5.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((200, 1800), (100, 1500), duration=3.0)
    print("➡️ 테이블 설치 이동2")

for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)
    
sleep(3.0)

def move_right(duration=1.0):
    swipe((200, 1800), (40, 1400), duration=4.0)
    print("➡️ 피자기계 설치 이동")
    
for _ in range(1):
    move_right(duration=4.0)  # 길게 조작
    sleep(0.5)
    
sleep(3.0)

def move_right(duration=1.0):
    swipe((200, 1800), (500, 2000), duration=2.0)
    print("➡️ 카운터 설치 이동1")
    
for _ in range(1):
    move_right(duration=2.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((500, 1800), (200, 2100), duration=4.0)
    print("➡️ 카운터 설치 이동2")
    
for _ in range(1):
    move_right(duration=4.0)  # 길게 조작
    sleep(0.5)

sleep(3.0)

def move_right(duration=1.0):
    swipe((300, 1800), (400, 1300), duration=3.0)
    print("➡️ 피자옮기기")
    
for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)
    
sleep(3.0)

def move_right(duration=1.0):
    swipe((250, 1500), (250, 1800), duration=3.0)
    print("➡️ 매대 돌아오기 및 판매")
    
for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)   

sleep(8.0)

def move_right(duration=1.0):
    swipe((300, 1800), (600, 1800), duration=3.0)
    print("➡️ 테이블 청소1")

for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)

def move_right(duration=1.0):
    swipe((300, 1200), (300, 1800), duration=1.0)
    print("➡️ 테이블 청소2")

for _ in range(1):
    move_right(duration=1.0)  # 길게 조작
    sleep(0.5)
    
sleep(3.0)

def move_right(duration=1.0):
    swipe((200, 1800), (550, 1000), duration=5.0)
    print("➡️ 쓰레기 버리기")

for _ in range(1):
    move_right(duration=5.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((300, 1800), (400, 2200), duration=2.0)
    print("➡️ 두번째 테이블 설치")

for _ in range(1):
    move_right(duration=2.0)  # 길게 조작
    sleep(0.5)

sleep(4.0)    
touch(Template(r"tpl1749042667145.png", record_pos=(-0.001, 0.388), resolution=(1080, 2400)))

sleep(3.0)
touch(Template(r"tpl1749042686153.png", record_pos=(-0.153, -0.911), resolution=(1080, 2400)))
sleep(3.0)
touch(Template(r"tpl1749042700315.png", record_pos=(-0.227, 0.075), resolution=(1080, 2400)))

sleep(3.0)

touch(Template(r"tpl1749042717128.png", record_pos=(-0.443, -0.956), resolution=(1080, 2400)))

sleep(3.0)

def move_right(duration=1.0):
    swipe((300, 1800), (100, 1300), duration=3.0)
    print("➡️ 새지역 열기")

for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)

sleep(3.0)

def move_right(duration=1.0):
    swipe((350, 1400), (500, 1200), duration=2.0)
    print("➡️ HR 사무실 열기")

for _ in range(1):
    move_right(duration=2.0)  # 길게 조작
    sleep(0.5)

sleep(2.0)

touch(Template(r"tpl1751462777166.png", record_pos=(0.126, 0.422), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1751462849771.png", record_pos=(-0.441, -0.875), resolution=(1080, 2400)))
sleep(1.0)



sleep(6.0)

def move_right(duration=1.0):
    swipe((400, 1200), (250, 1500), duration=3.0)
    print("➡️ HR 사무소 나오기")

for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)

sleep(2.0)


def move_right(duration=1.0):
    swipe((350, 1400), (500, 1800), duration=2.5)
    print("➡️ HR 사무소 나오기2")

for _ in range(1):
    move_right(duration=2.5)  # 길게 조작
    sleep(0.5)

sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (600, 1200), duration=3.5)
    print("➡️ 업그레이드 사무실 열기")

for _ in range(1):
    move_right(duration=3.5)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

touch(Template(r"tpl1751507138180.png", record_pos=(-0.001, 0.736), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1751507166385.png", record_pos=(0.419, 0.158), resolution=(1080, 2400)))

sleep(2.0)
touch(Template(r"tpl1751507248617.png", record_pos=(-0.005, 0.484), resolution=(1080, 2400)))
sleep(3.0)

def move_right(duration=1.0):
    swipe((400, 1300), (250, 1500), duration=3.0)
    print("➡️ 업그레이드 사무실 나오기")

for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)

sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (150, 1650), duration=7.0)
    print("➡️ 업그레이드 사무실 열기")

for _ in range(1):
    move_right(duration=7.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((250, 1600), (-150, 1200), duration=2.0)
    print("➡️ 카운터 업그레이드")

for _ in range(1):
    move_right(duration=2.0)  # 길게 조작
    sleep(0.5)

sleep(2.0)

touch(Template(r"tpl1751509252030.png", record_pos=(-0.31, 0.428), resolution=(1080, 2400)))

sleep(1.0)
 
touch(Template(r"tpl1751509288122.png", record_pos=(0.005, 0.443), resolution=(1080, 2400)))

sleep(1.0)

touch(Template(r"tpl1751509311297.png", record_pos=(0.315, 0.422), resolution=(1080, 2400)))

sleep(2.0)

touch(Template(r"tpl1751509359498.png", record_pos=(-0.314, 0.801), resolution=(1080, 2400)))

sleep(2.0)


    

    

touch(Template(r"tpl1752045083897.png", record_pos=(0.001, 0.575), resolution=(1080, 2400)))

sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (550, 1400), duration=5.0)
    print("➡️ 새로운구역확장")

for _ in range(1):
    move_right(duration=5.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (550, 1200), duration=3.0)
    print("➡️ 세번째 테이블 설치")

for _ in range(1):
    move_right(duration=3.0)  # 길게 조작
    sleep(0.5)

sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (550, 1200), duration=1.0)
    print("➡️ 드라이브 스루 이동1")

for _ in range(1):
    move_right(duration=1.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (0, 1200), duration=4.5)
    print("➡️ 드라이브 스루 이동2")

for _ in range(1):
    move_right(duration=4.5)  # 길게 조작
    sleep(0.5)  

sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (150, 1550), duration=7.0)
    print("➡️ 드라이브 스루 이동3")

for _ in range(1):
    move_right(duration=5.0)  # 길게 조작
    sleep(0.5)
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (350, 1100), duration=2.0)
    print("➡️ 패키지 테이블 만들기")

for _ in range(1):
    move_right(duration=2.0)  # 길게 조작
    sleep(0.5)    

sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (450, 1700), duration=1.0)
    print("➡️ 피자옮기기")

for _ in range(1):
    move_right(duration=1.0)  # 길게 조작
    sleep(0.5)
    
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((350, 1400), (450, 1300), duration=5.0)
    print("➡️ 피자옮기기2")

for _ in range(1):
    move_right(duration=5.0)  # 길게 조작
    sleep(0.5)  
    
    
sleep(2.0)

def move_right(duration=1.0):
    swipe((450, 1300), (350, 1400), duration=2.5)
    print("➡️ 피자옮기기3, 피자포장")

for _ in range(1):
    move_right(duration=2.5)  # 길게 조작
    sleep(0.5)

    
sleep(3.0)    
    
def move_right(duration=1.0):
    swipe((450, 1300), (350, 1400), duration=1.0)
    print("➡️ 피자포장 운반")

for _ in range(1):
    move_right(duration=1.0)  # 길게 조작
    sleep(0.5)     
    
sleep(2.0)    
    
def move_right(duration=1.0):
    swipe((350, 1400), (350, 1700), duration=1.5)
    print("➡️ 피자포장 판매")

for _ in range(1):
    move_right(duration=1.5)  # 길게 조작
    sleep(0.5) 
    
    
sleep(2.0)    
    
def move_right(duration=1.0):
    swipe((350, 1700), (550, 1400), duration=7.0)
    print("➡️ 두번째 화로 설치")

for _ in range(1):
    move_right(duration=7.0)  # 길게 조작
    sleep(0.5) 
    
    
sleep(2.0)    
    
def move_right(duration=1.0):
    swipe((350, 1300), (410, 1900), duration=6.6)
    print("➡️ 네번째 테이블 설치")

for _ in range(1):
    move_right(duration=6.6)  # 길게 조작
    sleep(0.5)

sleep(2.0)    
    
touch(Template(r"tpl1752050112906.png", record_pos=(-0.012, 0.564), resolution=(1080, 2400)))


sleep(3.0)

touch(Template(r"tpl1752050149677.png", record_pos=(-0.423, -0.72), resolution=(1080, 2400)))

sleep(3.0)

touch(Template(r"tpl1752050177621.png", record_pos=(0.006, 0.075), resolution=(1080, 2400)))

sleep(2.0)

touch(Template(r"tpl1752050213493.png", record_pos=(-0.006, 0.986), resolution=(1080, 2400)))

sleep(2.0)

touch(Template(r"tpl1752050235223.png", record_pos=(-0.005, 0.645), resolution=(1080, 2400)))


