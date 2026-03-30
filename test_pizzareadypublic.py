# -*- encoding=utf8 -*-
__author__ = "Supercent"

from airtest.core.api import *

connect_device("Android:///")


# ============================================================
# 헬퍼 함수
# ============================================================

def safe_touch(template, timeout=10, msg=""):
    """
    템플릿이 화면에 나타날 때까지 대기 후 터치.
    고정 sleep 대신 wait를 사용하여 빠르면 빠른 대로, 느리면 느린 대로 대응.
    """
    try:
        pos = wait(template, timeout=timeout)
        touch(pos)
        print(f"✅ {msg}")
        return True
    except TargetNotFoundError:
        print(f"⚠️ {msg} - 템플릿 미발견 (timeout={timeout}s)")
        return False


def safe_exists(template, msg=""):
    """
    있으면 터치, 없으면 스킵. 광고/보상처럼 있을 수도 없을 수도 있는 요소에 사용.
    """
    target = exists(template)
    if target:
        touch(target)
        print(f"✅ {msg}")
        return True
    else:
        print(f"⏭ {msg} - 요소 없음, 스킵")
        return False


def move_character(start, end, duration=3.0, msg=""):
    """
    캐릭터 이동 (swipe) 후 간격 대기.
    """
    swipe(start, end, duration=duration)
    print(f"➡️ {msg}")
    sleep(0.5)


# ============================================================
# 스크린 템플릿 (한 곳에서 관리)
# ============================================================

TPL_APP_ICON = Template(r"tpl1746680027562.png", record_pos=(-0.346, -0.371), resolution=(1080, 2400))
TPL_OPEN_ADS_CLOSE = Template(r"tpl1748340468070.png", record_pos=(0.355, -0.978), resolution=(1080, 2400))
TPL_OFFLINE_REWARD = Template(r"tpl1746680138516.png", record_pos=(0.001, 0.596), resolution=(1080, 2400))
TPL_MENU_1 = Template(r"tpl1749042667145.png", record_pos=(-0.001, 0.388), resolution=(1080, 2400))
TPL_MENU_2 = Template(r"tpl1749042686153.png", record_pos=(-0.153, -0.911), resolution=(1080, 2400))
TPL_MENU_3 = Template(r"tpl1749042700315.png", record_pos=(-0.227, 0.075), resolution=(1080, 2400))
TPL_MENU_4 = Template(r"tpl1749042717128.png", record_pos=(-0.443, -0.956), resolution=(1080, 2400))
TPL_HR_ENTER = Template(r"tpl1751462777166.png", record_pos=(0.126, 0.422), resolution=(1080, 2400))
TPL_HR_CONFIRM = Template(r"tpl1751462849771.png", record_pos=(-0.441, -0.875), resolution=(1080, 2400))
TPL_UPGRADE_1 = Template(r"tpl1751507138180.png", record_pos=(-0.001, 0.736), resolution=(1080, 2400))
TPL_UPGRADE_2 = Template(r"tpl1751507166385.png", record_pos=(0.419, 0.158), resolution=(1080, 2400))
TPL_UPGRADE_3 = Template(r"tpl1751507248617.png", record_pos=(-0.005, 0.484), resolution=(1080, 2400))
TPL_COUNTER_1 = Template(r"tpl1751509252030.png", record_pos=(-0.31, 0.428), resolution=(1080, 2400))
TPL_COUNTER_2 = Template(r"tpl1751509288122.png", record_pos=(0.005, 0.443), resolution=(1080, 2400))
TPL_COUNTER_3 = Template(r"tpl1751509311297.png", record_pos=(0.315, 0.422), resolution=(1080, 2400))
TPL_COUNTER_CONFIRM = Template(r"tpl1751509359498.png", record_pos=(-0.314, 0.801), resolution=(1080, 2400))
TPL_EXPAND_CONFIRM = Template(r"tpl1752045083897.png", record_pos=(0.001, 0.575), resolution=(1080, 2400))
TPL_FINAL_1 = Template(r"tpl1752050112906.png", record_pos=(-0.012, 0.564), resolution=(1080, 2400))
TPL_FINAL_2 = Template(r"tpl1752050149677.png", record_pos=(-0.423, -0.72), resolution=(1080, 2400))
TPL_FINAL_3 = Template(r"tpl1752050177621.png", record_pos=(0.006, 0.075), resolution=(1080, 2400))
TPL_FINAL_4 = Template(r"tpl1752050213493.png", record_pos=(-0.006, 0.986), resolution=(1080, 2400))
TPL_FINAL_5 = Template(r"tpl1752050235223.png", record_pos=(-0.005, 0.645), resolution=(1080, 2400))


# ============================================================
# 테스트 케이스
# ============================================================

def test_01_app_launch_and_loading():
    """앱 실행 및 로딩 대기"""
    touch(TPL_APP_ICON)
    sleep(20.0)
    # 검증: 광고 닫기 버튼 또는 보상 버튼 중 하나가 떠야 로딩 완료
    loaded = exists(TPL_OPEN_ADS_CLOSE) or exists(TPL_OFFLINE_REWARD)
    assert loaded, "앱 로딩 실패 - 로딩 후 예상 화면이 나타나지 않음"


def test_02_close_open_ads():
    """앱오픈 광고 닫기"""
    safe_exists(TPL_OPEN_ADS_CLOSE, msg="앱오픈 광고 닫기")
    sleep(3.0)


def test_03_collect_offline_reward():
    """오프라인 보상 획득"""
    safe_exists(TPL_OFFLINE_REWARD, msg="오프라인 보상 획득")
    sleep(4.0)


def test_04_move_to_money_pile():
    """돈더미 이동"""
    for i in range(3):
        move_character((200, 1800), (50, 2200), duration=0.6, msg=f"돈더미 이동 {i+1}/3")
        sleep(0.5)


def test_05_move_to_door_making():
    """문 만들기 이동"""
    for i in range(2):
        move_character((200, 1800), (80, 1500), duration=0.6, msg=f"문 만들기 이동 {i+1}/2")
        sleep(0.5)
    sleep(9.0)


def test_06_install_table_1():
    """테이블 설치 이동 1"""
    move_character((200, 1800), (80, 1650), duration=5.0, msg="테이블 설치 이동1")
    sleep(2.0)


def test_07_install_table_2():
    """테이블 설치 이동 2"""
    move_character((200, 1800), (100, 1500), duration=3.0, msg="테이블 설치 이동2")
    sleep(3.0)


def test_08_install_pizza_machine():
    """피자기계 설치 이동"""
    move_character((200, 1800), (40, 1400), duration=4.0, msg="피자기계 설치 이동")
    sleep(3.0)


def test_09_install_counter():
    """카운터 설치"""
    move_character((200, 1800), (500, 2000), duration=2.0, msg="카운터 설치 이동1")
    sleep(2.0)

    move_character((500, 1800), (200, 2100), duration=4.0, msg="카운터 설치 이동2")
    sleep(3.0)


def test_10_move_pizza_and_sell():
    """피자 옮기기 및 판매"""
    move_character((300, 1800), (400, 1300), duration=3.0, msg="피자옮기기")
    sleep(3.0)

    move_character((250, 1500), (250, 1800), duration=3.0, msg="매대 돌아오기 및 판매")
    sleep(8.0)


def test_11_clean_table():
    """테이블 청소"""
    move_character((300, 1800), (600, 1800), duration=3.0, msg="테이블 청소1")

    move_character((300, 1200), (300, 1800), duration=1.0, msg="테이블 청소2")
    sleep(3.0)


def test_12_throw_trash():
    """쓰레기 버리기"""
    move_character((200, 1800), (550, 1000), duration=5.0, msg="쓰레기 버리기")
    sleep(2.0)


def test_13_install_second_table():
    """두번째 테이블 설치"""
    move_character((300, 1800), (400, 2200), duration=2.0, msg="두번째 테이블 설치")
    sleep(4.0)


def test_14_menu_navigation():
    """메뉴 UI 탐색"""
    result_1 = safe_touch(TPL_MENU_1, timeout=10, msg="메뉴 진입")
    assert result_1, "메뉴 버튼을 찾을 수 없음"

    result_2 = safe_touch(TPL_MENU_2, timeout=10, msg="메뉴 항목 선택")
    assert result_2, "메뉴 항목을 찾을 수 없음"

    safe_touch(TPL_MENU_3, timeout=10, msg="메뉴 확인")
    sleep(3.0)

    safe_touch(TPL_MENU_4, timeout=10, msg="메뉴 닫기")
    sleep(3.0)


def test_15_open_new_area():
    """새 지역 열기"""
    move_character((300, 1800), (100, 1300), duration=3.0, msg="새지역 열기")
    sleep(3.0)


def test_16_open_hr_office():
    """HR 사무실 열기 및 설정"""
    move_character((350, 1400), (500, 1200), duration=2.0, msg="HR 사무실 이동")
    sleep(2.0)

    result = safe_touch(TPL_HR_ENTER, timeout=10, msg="HR 사무실 진입")
    assert result, "HR 사무실 진입 버튼을 찾을 수 없음"

    safe_touch(TPL_HR_CONFIRM, timeout=10, msg="HR 설정 확인")
    sleep(6.0)


def test_17_exit_hr_office():
    """HR 사무실 나오기"""
    move_character((400, 1200), (250, 1500), duration=3.0, msg="HR 사무소 나오기")
    sleep(2.0)

    move_character((350, 1400), (500, 1800), duration=2.5, msg="HR 사무소 나오기2")
    sleep(2.0)


def test_18_open_upgrade_office():
    """업그레이드 사무실 열기 및 업그레이드 진행"""
    move_character((350, 1400), (600, 1200), duration=3.5, msg="업그레이드 사무실 이동")
    sleep(2.0)

    result_1 = safe_touch(TPL_UPGRADE_1, timeout=10, msg="업그레이드 메뉴 진입")
    assert result_1, "업그레이드 메뉴를 찾을 수 없음"

    result_2 = safe_touch(TPL_UPGRADE_2, timeout=10, msg="업그레이드 항목 선택")
    assert result_2, "업그레이드 항목을 찾을 수 없음"

    result_3 = safe_touch(TPL_UPGRADE_3, timeout=10, msg="업그레이드 확인")
    assert result_3, "업그레이드 확인 버튼을 찾을 수 없음"
    sleep(3.0)


def test_19_exit_upgrade_office():
    """업그레이드 사무실 나오기"""
    move_character((400, 1300), (250, 1500), duration=3.0, msg="업그레이드 사무실 나오기")
    sleep(2.0)

    move_character((350, 1400), (150, 1650), duration=7.0, msg="메인 영역 복귀")
    sleep(2.0)


def test_20_counter_upgrade():
    """카운터 업그레이드"""
    move_character((250, 1600), (-150, 1200), duration=2.0, msg="카운터 업그레이드 이동")
    sleep(2.0)

    result_1 = safe_touch(TPL_COUNTER_1, timeout=10, msg="카운터 업그레이드 1단계")
    assert result_1, "카운터 업그레이드 1단계 실패"

    safe_touch(TPL_COUNTER_2, timeout=10, msg="카운터 업그레이드 2단계")
    sleep(1.0)

    safe_touch(TPL_COUNTER_3, timeout=10, msg="카운터 업그레이드 3단계")
    sleep(2.0)

    safe_touch(TPL_COUNTER_CONFIRM, timeout=10, msg="카운터 업그레이드 확정")
    sleep(2.0)

    safe_touch(TPL_EXPAND_CONFIRM, timeout=10, msg="확장 확인")
    sleep(2.0)


def test_21_expand_new_area():
    """새로운 구역 확장"""
    move_character((350, 1400), (550, 1400), duration=5.0, msg="새로운 구역 확장")
    sleep(2.0)


def test_22_install_third_table():
    """세번째 테이블 설치"""
    move_character((350, 1400), (550, 1200), duration=3.0, msg="세번째 테이블 설치")
    sleep(2.0)


def test_23_drive_thru_setup():
    """드라이브 스루 이동 및 설치"""
    move_character((350, 1400), (550, 1200), duration=1.0, msg="드라이브 스루 이동1")
    sleep(2.0)

    move_character((350, 1400), (0, 1200), duration=4.5, msg="드라이브 스루 이동2")
    sleep(2.0)

    move_character((350, 1400), (150, 1550), duration=7.0, msg="드라이브 스루 이동3")
    sleep(2.0)


def test_24_package_table_setup():
    """패키지 테이블 만들기"""
    move_character((350, 1400), (350, 1100), duration=2.0, msg="패키지 테이블 만들기")
    sleep(2.0)


def test_25_pizza_packaging_and_sell():
    """피자 포장 및 판매"""
    move_character((350, 1400), (450, 1700), duration=1.0, msg="피자옮기기")
    sleep(2.0)

    move_character((350, 1400), (450, 1300), duration=5.0, msg="피자옮기기2")
    sleep(2.0)

    move_character((450, 1300), (350, 1400), duration=2.5, msg="피자포장")
    sleep(3.0)

    move_character((450, 1300), (350, 1400), duration=1.0, msg="피자포장 운반")
    sleep(2.0)

    move_character((350, 1400), (350, 1700), duration=1.5, msg="피자포장 판매")
    sleep(2.0)


def test_26_install_second_furnace():
    """두번째 화로 설치"""
    move_character((350, 1700), (550, 1400), duration=7.0, msg="두번째 화로 설치")
    sleep(2.0)


def test_27_install_fourth_table():
    """네번째 테이블 설치"""
    move_character((350, 1300), (410, 1900), duration=6.6, msg="네번째 테이블 설치")
    sleep(2.0)


def test_28_final_menu_navigation():
    """최종 메뉴 UI 탐색 및 완료 검증"""
    result_1 = safe_touch(TPL_FINAL_1, timeout=10, msg="최종 메뉴 1단계")
    assert result_1, "최종 메뉴 1단계 버튼을 찾을 수 없음"

    result_2 = safe_touch(TPL_FINAL_2, timeout=10, msg="최종 메뉴 2단계")
    assert result_2, "최종 메뉴 2단계 버튼을 찾을 수 없음"

    result_3 = safe_touch(TPL_FINAL_3, timeout=10, msg="최종 메뉴 3단계")
    assert result_3, "최종 메뉴 3단계 버튼을 찾을 수 없음"

    result_4 = safe_touch(TPL_FINAL_4, timeout=10, msg="최종 메뉴 4단계")
    assert result_4, "최종 메뉴 4단계 버튼을 찾을 수 없음"

    result_5 = safe_touch(TPL_FINAL_5, timeout=10, msg="최종 메뉴 5단계 - 테스트 완료")
    assert result_5, "최종 메뉴 5단계 버튼을 찾을 수 없음"

    print("🎉 Pizza Ready Public 전체 플로우 테스트 완료")
