# 주식 수익률 계산기
# 매수가와 현재가를 입력하면 수익률, 손익금액을 계산해줍니다.

def calculate_return(ticker, buy_price, current_price, quantity):
    """수익률과 손익 계산"""
    total_buy    = buy_price * quantity
    total_now    = current_price * quantity
    profit       = total_now - total_buy
    profit_rate  = (profit / total_buy) * 100
    return {
        "ticker":      ticker.upper(),
        "buy_price":   buy_price,
        "current":     current_price,
        "quantity":    quantity,
        "total_buy":   total_buy,
        "total_now":   total_now,
        "profit":      profit,
        "profit_rate": profit_rate,
    }

def print_result(r):
    """결과 출력"""
    sign = "+" if r["profit"] >= 0 else ""
    print()
    print(f"  ─────────────────────────────")
    print(f"  [{r['ticker']}]")
    print(f"  매수가     : ${r['buy_price']:,.2f}")
    print(f"  현재가     : ${r['current']:,.2f}")
    print(f"  수량       : {r['quantity']}주")
    print(f"  매수 총액  : ${r['total_buy']:,.2f}")
    print(f"  현재 평가액: ${r['total_now']:,.2f}")
    print(f"  손익       : {sign}${r['profit']:,.2f}")
    print(f"  수익률     : {sign}{r['profit_rate']:.2f}%")
    print(f"  ─────────────────────────────")

def get_float(prompt):
    """숫자 입력 (잘못된 입력 처리 포함)"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  0보다 큰 숫자를 입력해주세요.")
                continue
            return value
        except ValueError:
            print("  숫자만 입력해주세요.")

def get_int(prompt):
    """정수 입력"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  0보다 큰 정수를 입력해주세요.")
                continue
            return value
        except ValueError:
            print("  정수만 입력해주세요.")

def main():
    print("==============================")
    print("   📈 주식 수익률 계산기")
    print("==============================")

    portfolio = []

    while True:
        print("\n  [메뉴]")
        print("  1. 종목 추가")
        print("  2. 전체 포트폴리오 요약")
        print("  3. 종료")
        choice = input("\n  선택 > ").strip()

        if choice == "1":
            print()
            ticker       = input("  종목 티커 (예: VOO, QQQ, TSMC) > ").strip()
            buy_price    = get_float("  매수가 ($) > ")
            current_price = get_float("  현재가 ($) > ")
            quantity     = get_int("  수량 (주) > ")

            result = calculate_return(ticker, buy_price, current_price, quantity)
            portfolio.append(result)
            print_result(result)

        elif choice == "2":
            if not portfolio:
                print("\n  아직 추가된 종목이 없어요.")
                continue

            total_buy = sum(r["total_buy"] for r in portfolio)
            total_now = sum(r["total_now"] for r in portfolio)
            total_profit = total_now - total_buy
            total_rate = (total_profit / total_buy) * 100
            sign = "+" if total_profit >= 0 else ""

            print()
            print("  ══════════════════════════════")
            print("   포트폴리오 전체 요약")
            print("  ══════════════════════════════")
            for r in portfolio:
                s = "+" if r["profit"] >= 0 else ""
                print(f"  {r['ticker']:<6} {s}{r['profit_rate']:.2f}%  |  {s}${r['profit']:,.2f}")
            print("  ──────────────────────────────")
            print(f"  총 매수액  : ${total_buy:,.2f}")
            print(f"  총 평가액  : ${total_now:,.2f}")
            print(f"  총 손익    : {sign}${total_profit:,.2f}")
            print(f"  총 수익률  : {sign}{total_rate:.2f}%")
            print("  ══════════════════════════════")

        elif choice == "3":
            print("\n  프로그램을 종료합니다. 👋\n")
            break

        else:
            print("  1, 2, 3 중에서 선택해주세요.")

if __name__ == "__main__":
    main()
