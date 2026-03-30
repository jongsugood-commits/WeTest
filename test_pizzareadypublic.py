# -*- encoding=utf8 -*-
__author__ = "Supercent"

from airtest.core.api import *

connect_device("Android:///")


def test_01_app_launch_and_loading():
    """앱 실행 및 로딩 대기"""
    touch(Template(r"tpl1746680027562.png", record_pos=(-0.346, -0.371), resolution=(1080, 2400)))
    sleep(20.0)


def test_02_close_open_ads():
    """앱오픈 광고 닫기"""
    openads = exists(Template(r"tpl1748340468070.png", record_pos=(0.355, -0.978), resolution=(1080, 2400)))
    if openads:
        touch(openads)
        print("✅ 앱오픈 광고 닫기")
    else:
        print("⏭ 광고 닫기 버튼이 없어, 다음 단계로 진행합니다.")
    sleep(3.0)


def test_03_collect_offline_reward():
    """오프라인 보상 획득"""
    give = exists(Template(r"tpl1746680138516.png", record_pos=(0.001, 0.596), resolution=(1080, 2400)))
    if give:
        touch(give)
        print("✅ 오프라인 보상 획득 완료")
    else:
        print("⏭ 획득하기 버튼이 없어, 다음 단계로 진행합니다.")
    sleep(4.0)


def test_04_move_to_money_pile():
    """돈더미 이동"""
    for _ in range(3):
        swipe((200, 1800), (50, 2200), duration=0.6)
        print("➡️ 돈더미 이동")
        sleep(0.5)


def test_05_move_to_door_making():
    """문 만들기 이동"""
    for _ in range(2):
        swipe((200, 1800), (80, 1500), duration=0.6)
        print("➡️ 문 만들기 이동")
        sleep(0.5)
    sleep(9.0)


def test_06_install_table_1():
    """테이블 설치 이동 1"""
    swipe((200, 1800), (80, 1650), duration=5.0)
    print("➡️ 테이블 설치 이동1")
    sleep(2.5)


def test_07_install_table_2():
    """테이블 설치 이동 2"""
    swipe((200, 1800), (100, 1500), duration=3.0)
    print("➡️ 테이블 설치 이동2")
    sleep(3.5)


def test_08_install_pizza_machine():
    """피자기계 설치 이동"""
    swipe((200, 1800), (40, 1400), duration=4.0)
    print("➡️ 피자기계 설치 이동")
    sleep(3.5)


def test_09_install_counter():
    """카운터 설치"""
    swipe((200, 1800), (500, 2000), duration=2.0)
    print("➡️ 카운터 설치 이동1")
    sleep(2.5)

    swipe((500, 1800), (200, 2100), duration=4.0)
    print("➡️ 카운터 설치 이동2")
    sleep(3.5)


def test_10_move_pizza_and_sell():
    """피자 옮기기 및 판매"""
    swipe((300, 1800), (400, 1300), duration=3.0)
    print("➡️ 피자옮기기")
    sleep(3.5)

    swipe((250, 1500), (250, 1800), duration=3.0)
    print("➡️ 매대 돌아오기 및 판매")
    sleep(8.5)


def test_11_clean_table():
    """테이블 청소"""
    swipe((300, 1800), (600, 1800), duration=3.0)
    print("➡️ 테이블 청소1")
    sleep(0.5)

    swipe((300, 1200), (300, 1800), duration=1.0)
    print("➡️ 테이블 청소2")
    sleep(3.5)


def test_12_throw_trash():
    """쓰레기 버리기"""
    swipe((200, 1800), (550, 1000), duration=5.0)
    print("➡️ 쓰레기 버리기")
    sleep(2.5)


def test_13_install_second_table():
    """두번째 테이블 설치"""
    swipe((300, 1800), (400, 2200), duration=2.0)
    print("➡️ 두번째 테이블 설치")
    sleep(4.5)


def test_14_menu_navigation():
    """메뉴 UI 탐색"""
    touch(Template(r"tpl1749042667145.png", record_pos=(-0.001, 0.388), resolution=(1080, 2400)))
    sleep(3.0)

    touch(Template(r"tpl1749042686153.png", record_pos=(-0.153, -0.911), resolution=(1080, 2400)))
    sleep(3.0)

    touch(Template(r"tpl1749042700315.png", record_pos=(-0.227, 0.075), resolution=(1080, 2400)))
    sleep(3.0)

    touch(Template(r"tpl1749042717128.png", record_pos=(-0.443, -0.956), resolution=(1080, 2400)))
    sleep(3.0)


def test_15_open_new_area():
    """새 지역 열기"""
    swipe((300, 1800), (100, 1300), duration=3.0)
    print("➡️ 새지역 열기")
    sleep(3.5)


def test_16_open_hr_office():
    """HR 사무실 열기 및 설정"""
    swipe((350, 1400), (500, 1200), duration=2.0)
    print("➡️ HR 사무실 열기")
    sleep(2.5)

    touch(Template(r"tpl1751462777166.png", record_pos=(0.126, 0.422), resolution=(1080, 2400)))
    sleep(1.0)

    touch(Template(r"tpl1751462849771.png", record_pos=(-0.441, -0.875), resolution=(1080, 2400)))
    sleep(6.5)


def test_17_exit_hr_office():
    """HR 사무실 나오기"""
    swipe((400, 1200), (250, 1500), duration=3.0)
    print("➡️ HR 사무소 나오기")
    sleep(2.5)

    swipe((350, 1400), (500, 1800), duration=2.5)
    print("➡️ HR 사무소 나오기2")
    sleep(2.5)


def test_18_open_upgrade_office():
    """업그레이드 사무실 열기 및 업그레이드"""
    swipe((350, 1400), (600, 1200), duration=3.5)
    print("➡️ 업그레이드 사무실 열기")
    sleep(2.5)

    touch(Template(r"tpl1751507138180.png", record_pos=(-0.001, 0.736), resolution=(1080, 2400)))
    sleep(1.0)

    touch(Template(r"tpl1751507166385.png", record_pos=(0.419, 0.158), resolution=(1080, 2400)))
    sleep(2.0)

    touch(Template(r"tpl1751507248617.png", record_pos=(-0.005, 0.484), resolution=(1080, 2400)))
    sleep(3.0)


def test_19_exit_upgrade_office():
    """업그레이드 사무실 나오기"""
    swipe((400, 1300), (250, 1500), duration=3.0)
    print("➡️ 업그레이드 사무실 나오기")
    sleep(2.5)

    swipe((350, 1400), (150, 1650), duration=7.0)
    print("➡️ 업그레이드 사무실 열기")
    sleep(2.5)


def test_20_counter_upgrade():
    """카운터 업그레이드"""
    swipe((250, 1600), (-150, 1200), duration=2.0)
    print("➡️ 카운터 업그레이드")
    sleep(2.5)

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


def test_21_expand_new_area():
    """새로운 구역 확장"""
    swipe((350, 1400), (550, 1400), duration=5.0)
    print("➡️ 새로운구역확장")
    sleep(2.5)


def test_22_install_third_table():
    """세번째 테이블 설치"""
    swipe((350, 1400), (550, 1200), duration=3.0)
    print("➡️ 세번째 테이블 설치")
    sleep(2.5)


def test_23_drive_thru_setup():
    """드라이브 스루 이동 및 설치"""
    swipe((350, 1400), (550, 1200), duration=1.0)
    print("➡️ 드라이브 스루 이동1")
    sleep(2.5)

    swipe((350, 1400), (0, 1200), duration=4.5)
    print("➡️ 드라이브 스루 이동2")
    sleep(2.5)

    swipe((350, 1400), (150, 1550), duration=7.0)
    print("➡️ 드라이브 스루 이동3")
    sleep(2.5)


def test_24_package_table_setup():
    """패키지 테이블 만들기"""
    swipe((350, 1400), (350, 1100), duration=2.0)
    print("➡️ 패키지 테이블 만들기")
    sleep(2.5)


def test_25_pizza_packaging_and_sell():
    """피자 포장 및 판매"""
    swipe((350, 1400), (450, 1700), duration=1.0)
    print("➡️ 피자옮기기")
    sleep(2.5)

    swipe((350, 1400), (450, 1300), duration=5.0)
    print("➡️ 피자옮기기2")
    sleep(2.5)

    swipe((450, 1300), (350, 1400), duration=2.5)
    print("➡️ 피자옮기기3, 피자포장")
    sleep(3.5)

    swipe((450, 1300), (350, 1400), duration=1.0)
    print("➡️ 피자포장 운반")
    sleep(2.5)

    swipe((350, 1400), (350, 1700), duration=1.5)
    print("➡️ 피자포장 판매")
    sleep(2.5)


def test_26_install_second_furnace():
    """두번째 화로 설치"""
    swipe((350, 1700), (550, 1400), duration=7.0)
    print("➡️ 두번째 화로 설치")
    sleep(2.5)


def test_27_install_fourth_table():
    """네번째 테이블 설치"""
    swipe((350, 1300), (410, 1900), duration=6.6)
    print("➡️ 네번째 테이블 설치")
    sleep(2.5)


def test_28_final_menu_navigation():
    """최종 메뉴 UI 탐색"""
    touch(Template(r"tpl1752050112906.png", record_pos=(-0.012, 0.564), resolution=(1080, 2400)))
    sleep(3.0)

    touch(Template(r"tpl1752050149677.png", record_pos=(-0.423, -0.72), resolution=(1080, 2400)))
    sleep(3.0)

    touch(Template(r"tpl1752050177621.png", record_pos=(0.006, 0.075), resolution=(1080, 2400)))
    sleep(2.0)

    touch(Template(r"tpl1752050213493.png", record_pos=(-0.006, 0.986), resolution=(1080, 2400)))
    sleep(2.0)

    touch(Template(r"tpl1752050235223.png", record_pos=(-0.005, 0.645), resolution=(1080, 2400)))
